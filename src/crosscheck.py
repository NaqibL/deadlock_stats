"""Cross-check the sheet against the raw game files (SteamDB GameTracking-Deadlock).

The primary source is Deadbot's parse of the game files. The raw ``.vdata``
files are parsed here independently, so a disagreement means one of the two
parsers (or this tool's reading of the primary source) is wrong, or the two
sources are at different game builds.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from .abilities import split_value
from .items import SHOP_TIERS
from .text import number, tidy

RAW_SLOTS = {"EItemSlotType_WeaponMod": "Weapon", "EItemSlotType_Armor": "Armor", "EItemSlotType_Tech": "Tech"}
SPIRIT_SCALE_CLASSES = {
    "scale_function_tech_damage", "scale_function_healing_spirit_scale", None,
}
ENGINE_UNITS_PER_METRE = 1 / 0.0254  # the raw files store speeds and distances in inches
_SKIP_PROPS = {"Key", "Name", "IsDisabled", "Upgrades", "BehaviourBits"}
_ITEM_META = {
    "Name", "Description", "Cost", "Tier", "Activation", "Slot", "Components", "TargetTypes", "ShopFilters",
    "IsDisabled", "StreetBrawl", "IsImbue", "PropertyUpgrades", "CorruptedUpgrades",
}


@dataclass
class CrossCheck:
    available: bool = True
    note: str = ""
    raw_build: str = ""
    compared: dict = field(default_factory=dict)
    disagreements: list = field(default_factory=list)

    def count(self, what: str, n: int = 1):
        self.compared[what] = self.compared.get(what, 0) + n

    def differ(self, entity: str, fieldname: str, sheet, raw):
        self.disagreements.append((entity, fieldname, sheet, raw))


def _same(a, b, tolerance=1e-3) -> bool:
    if a is None or b is None:
        return a is None and b is None
    return abs(float(a) - float(b)) <= tolerance * max(1.0, abs(float(a)), abs(float(b)))


def _truthy(value) -> bool:
    return value is True or (isinstance(value, str) and value.lower() == "true")


def raw_released_heroes(raw_heroes: dict) -> dict:
    return {
        key: hero
        for key, hero in raw_heroes.items()
        if isinstance(hero, dict)
        and hero.get("m_eHeroDevelopmentState") == "EHeroDevState_Release"
        and not _truthy(hero.get("m_bDisabled"))
    }


def raw_property(raw_ability: dict, prop: str):
    """``(value, spirit_scale)`` of a raw ability / item property, or ``(None, None)`` if absent."""
    entry = ((raw_ability or {}).get("m_mapAbilityProperties") or {}).get(prop)
    if not isinstance(entry, dict):
        return None, None
    value, _ = number(entry.get("m_strValue"))
    scale = entry.get("m_subclassScaleFunction") or {}
    spirit = None
    if isinstance(scale, dict) and isinstance(scale.get("m_flStatScale"), (int, float)):
        stat = scale.get("m_eSpecificStatScaleType")
        # A scale function that names no stat ("EStatsCount" is the enum's unset
        # value) scales with spirit power, unless its class is for another stat.
        unnamed = stat in (None, "EStatsCount") and scale.get("_class") in SPIRIT_SCALE_CLASSES
        if stat == "ETechPower" or unnamed:
            spirit = tidy(scale["m_flStatScale"])
    return value, spirit


def _compare_properties(result: CrossCheck, entity: str, sheet_props: dict, raw_ability: dict, what: str, skip):
    for prop, raw_value in sheet_props.items():
        if prop in skip or isinstance(raw_value, bool):
            continue
        value, _, scales = split_value(raw_value)
        if value is None:
            continue
        other, other_spirit = raw_property(raw_ability, prop)
        if other is None:
            continue  # not a plain property in the raw files (derived by the primary source)
        result.count(what)
        if not _same(value, other) and not _same(value * ENGINE_UNITS_PER_METRE, other):
            result.differ(entity, prop, value, other)
        if "spirit" in scales or other_spirit:
            result.count(what + " (spirit scaling)")
            if not _same(scales.get("spirit", 0), other_spirit or 0):
                result.differ(entity, prop + " spirit scaling", scales.get("spirit"), other_spirit)


def cross_check(primary: dict, raw: dict, hero_rows: list, ability_rows: list, item_rows: list) -> CrossCheck:
    result = CrossCheck(raw_build=raw["version"].get("ClientVersion", ""))
    sheet_build = primary["version"].get("ClientVersion", "")
    if result.raw_build != sheet_build:
        result.note = (
            f"sources are at different game builds (sheet {sheet_build}, cross-check {result.raw_build}); "
            "disagreements below may be real patch changes"
        )
    raw_heroes, raw_abilities = raw["heroes"], raw["abilities"]

    # Heroes: the playable set, then the key numbers.
    released = raw_released_heroes(raw_heroes)
    sheet_keys = {row["key"] for row in hero_rows}
    result.count("hero roster")
    for key in sorted(sheet_keys - set(released)):
        result.differ(key, "playable", "in sheet", "not a released, enabled hero in the raw files")
    for key in sorted(set(released) - sheet_keys):
        result.differ(key, "playable", "not in sheet", "released and enabled in the raw files")
    for row in hero_rows:
        hero = raw_heroes.get(row["key"])
        if not isinstance(hero, dict):
            continue
        stats = hero.get("m_mapStartingStats") or {}
        level = hero.get("m_mapStandardLevelUpUpgrades") or {}
        weapon_key = (hero.get("m_mapBoundAbilities") or {}).get("ESlot_Weapon_Primary")
        weapon = ((raw_abilities.get(weapon_key) or {}).get("m_mapWeaponInfos") or {}).get("primary") or {}
        pairs = [
            ("base_health", stats.get("EMaxHealth")),
            ("health_per_boon", level.get("MODIFIER_VALUE_BASE_HEALTH_FROM_LEVEL")),
            ("bullet_damage", weapon.get("m_flBulletDamage")),
            ("bullet_damage_per_boon", level.get("MODIFIER_VALUE_BASE_BULLET_DAMAGE_FROM_LEVEL")),
            ("pellets_per_shot", weapon.get("m_iBullets")),
            ("clip_size", weapon.get("m_iClipSize")),
            ("spirit_power_per_boon", level.get("MODIFIER_VALUE_TECH_POWER")),
        ]
        for name, other in pairs:
            other, _ = number(other)
            if other is None:
                continue
            result.count("hero " + name)
            if not _same(row[name], other):
                result.differ(row["name"], name, row[name], other)
        for slot in ("1", "2", "3", "4"):
            bound = (primary["heroes"][row["key"]].get("BoundAbilities") or {}).get(slot, {}).get("Key")
            other = (hero.get("m_mapBoundAbilities") or {}).get(f"ESlot_Signature_{slot}")
            result.count("hero ability slots")
            if bound != other:
                result.differ(row["name"], f"ability slot {slot}", bound, other)

    # Abilities: every numeric property and its spirit scaling.
    for row in ability_rows:
        raw_ability = raw_abilities.get(row["key"])
        if not isinstance(raw_ability, dict):
            result.differ(f"{row['hero']} / {row['name']}", "ability", "in sheet", "missing from the raw files")
            continue
        _compare_properties(
            result, f"{row['hero']} / {row['name']}", primary["abilities"][row["key"]], raw_ability,
            "ability properties", _SKIP_PROPS,
        )

    # Items: tier, category, cost, then every numeric property.
    prices = raw["generic"].get("m_nItemPricePerTier") or []
    for row in item_rows:
        raw_item = raw_abilities.get(row["key"])
        if not isinstance(raw_item, dict):
            result.differ(row["name"], "item", "in sheet", "missing from the raw files")
            continue
        source_item = primary["items"][row["key"]]
        tier = str(raw_item.get("m_iItemTier", "")).replace("EModTier_", "")
        tier = int(tier) if tier.isdigit() else None
        result.count("item tier")
        if tier != row["tier"]:
            result.differ(row["name"], "tier", row["tier"], tier)
        result.count("item cost")
        price = prices[tier] if tier is not None and tier < len(prices) else None
        if price != row["cost"]:
            result.differ(row["name"], "cost", row["cost"], price)
        result.count("item category")
        if RAW_SLOTS.get(raw_item.get("m_eItemSlotType")) != source_item.get("Slot"):
            result.differ(row["name"], "category", source_item.get("Slot"), raw_item.get("m_eItemSlotType"))
        result.count("item enabled")
        if _truthy(raw_item.get("m_bDisabled")):
            result.differ(row["name"], "enabled", "in sheet", "disabled in the raw files")
        _compare_properties(result, row["name"], source_item, raw_item, "item properties", _ITEM_META)

    # Raw shop items the sheet does not have (other than Street Brawl ones the primary source marks).
    sheet_items = {row["key"] for row in item_rows}
    for key, raw_item in raw_abilities.items():
        if not isinstance(raw_item, dict) or key in sheet_items:
            continue
        tier = str(raw_item.get("m_iItemTier", "")).replace("EModTier_", "")
        if not tier.isdigit() or int(tier) not in SHOP_TIERS or raw_item.get("m_eItemSlotType") not in RAW_SLOTS:
            continue
        if _truthy(raw_item.get("m_bDisabled")):
            continue
        source_item = primary["items"].get(key) or {}
        if source_item.get("StreetBrawl") or not source_item.get("Name"):
            continue
        result.differ(source_item.get("Name") or key, "item", "not in sheet", "enabled shop item in the raw files")
    return result
