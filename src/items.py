"""Items table: one row per purchasable shop item.

Effects are split into three buckets, using the tooltip sections in
``item-cards.json``:

* innate      - stats the buyer always has. Properties in a section of type
                ``Innate`` (unless flagged conditional), plus any property
                flagged ``IntrinsicallyProvidedInAbility``.
* enemy       - effects applied to enemies. The files only flag a handful of
                these (``ConditionallyEnemyApplied``), so the rest are
                recognised by property type (resist reduction, slow), by a
                status effect, or by property name (damage dealt, debuff
                durations, healing reduction). This part is an approximation.
* conditional - everything else in a ``Passive`` / ``Active`` section:
                conditional, proc and on-use effects on the buyer.

Some real stats are on no tooltip section in the primary source (Refresher's
resists, for example). The raw game files settle those: a property the game
"provides" as a stat (``m_eProvidedPropertyType``) with a non-zero base value
is innate when it carries no usage flag, and conditional or enemy-applied when
flagged so. Values with no such raw property (enhanced-variant numbers, tuning
constants) stay in ``unlisted_properties``.
"""
from __future__ import annotations

import re

from .text import clean, fmt, label, number, postfix

SLOT_TOKENS = {"Weapon": "CitadelCategoryWeapon", "Armor": "CitadelCategoryArmor", "Tech": "CitadelCategoryTech"}
SHOP_TIERS = (1, 2, 3, 4)

# Innate stat columns: column -> source keys.
STAT_COLUMNS = {
    "weapon_damage_pct": ("BaseAttackDamagePercent",),
    "fire_rate_pct": ("BonusFireRate",),
    "ammo_pct": ("BonusClipSizePercent",),
    "bonus_health": ("BonusHealth",),
    "health_regen": ("BonusHealthRegen",),
    "out_of_combat_regen": ("OutOfCombatHealthRegen",),
    "bullet_resist_pct": ("BulletResist",),
    "spirit_resist_pct": ("TechResist",),
    "spirit_power": ("TechPower", "SpiritPower", "SpiritPowerInnate"),
    "bullet_lifesteal_pct": ("BulletLifestealPercent",),
    "spirit_lifesteal_pct": ("AbilityLifestealPercentHero",),
    "cooldown_reduction_pct": ("CooldownReduction",),
    "move_speed": ("BonusMoveSpeed",),
    "sprint_speed": ("BonusSprintSpeed",),
}
_STAT_BY_KEY = {key: column for column, keys in STAT_COLUMNS.items() for key in keys}

COLUMNS = [
    "key", "name", "category", "tier", "cost", "activation", "activation_type", "cooldown", "is_imbue",
    "builds_from", "upgrades_into",
    *STAT_COLUMNS,
    "other_innate_stats", "stats_not_on_tooltip", "conditional_effects", "enemy_effects",
    "unlisted_properties", "effect_text",
]

ENEMY_TYPES = {"bullet_armor_down", "tech_armor_down", "slow"}
ENEMY_KEY = re.compile(
    r"^(Damage|DPS|DPSMax|SpiritDamage|ImpactDamage|ExplosionDamage|ExplodeDamage|DamagePerChain|DamagePulseAmount"
    r"|BulletsBonusMagicDamage|ProcBonusMagicDamage|CurrentHealthDamage|MaxHealthDamage|MaxHPDamage|PercentDamage"
    r"|HealthPctDamage|DotHealthPercent|MaxHealthPercentAsDPS"
    r"|HealAmpReceivePenaltyPercent|HealAmpRegenPenaltyPercent|TechPowerReduction|MagicIncreasePerStack"
    r"|SlowDuration|StunDuration|SilenceDuration|FreezeDuration|DebuffDuration|DotDuration|TetherDuration"
    r"|FireRateSlow|FireRateSlowDuration|ResistReductionDuration|DazeDuration|EMPDuration)$"
)
_BORING = {"AbilityUnitTargetLimit", "AbilityCooldownBetweenCharge", "ChannelMoveSpeed"}
_SECTIONS = ("Info1", "Info2", "Info3", "Info4")


def classify_item(key: str, item: dict) -> str | None:
    """Return ``None`` for an item purchasable in the standard shop, otherwise why it is excluded."""
    if not item.get("Name"):
        return "no English name (placeholder, base class or non-item ability)"
    if item.get("IsDisabled"):
        return "disabled in the game files"
    if item.get("StreetBrawl"):
        return "Street Brawl mode only"
    if item.get("Slot") not in SLOT_TOKENS:
        return "no shop category"
    if item.get("Tier") not in SHOP_TIERS:
        return f"not a shop tier (tier {item.get('Tier')})"
    return None


def split_items(items: dict):
    shop, excluded = {}, []
    for key, item in items.items():
        reason = classify_item(key, item)
        if reason is None:
            shop[key] = item
        else:
            excluded.append((key, item.get("Name") or "", reason))
    return shop, excluded


def bucket(section_type: str | None, prop: dict) -> str:
    """Which bucket a tooltip property belongs to: ``innate``, ``conditional`` or ``enemy``."""
    flag = prop.get("UsageFlags") or ""
    if flag == "IntrinsicallyProvidedInAbility":
        return "innate"
    is_enemy = (
        flag == "ConditionallyEnemyApplied"
        or prop.get("Type") in ENEMY_TYPES
        or bool(prop.get("StatusEffect"))
        or bool(ENEMY_KEY.match(prop.get("Key") or ""))
    )
    if section_type == "Innate" and not flag.startswith("Conditionally"):
        return "innate"
    return "enemy" if is_enemy else "conditional"


def prop_text(prop: dict, loc: dict) -> str:
    key = prop.get("Key") or ""
    value, unit = number(prop.get("Value"))
    shown = fmt(value) if value is not None else str(prop.get("Value"))
    text = f"{label(loc, key, prop.get('LocTokenOverride'))}: {shown}{unit or postfix(loc, key)}"
    scale = prop.get("Scale")
    scales = scale if isinstance(scale, list) else [scale] if scale else []
    extras = []
    for entry in scales:
        coefficient, _ = number(entry.get("Value"))
        if coefficient is not None:
            kind = {"spirit": "spirit power", "power_increase": "boon"}.get(entry.get("Type"), entry.get("Type"))
            extras.append(f"+{fmt(coefficient)} x {kind}")
    if extras:
        text += f" ({', '.join(extras)})"
    if prop.get("StatusEffect"):
        text += f" [{prop['StatusEffect']}]"
    return text


def _section_props(section: dict):
    return list(section.get("Main") or []) + list(section.get("Alt") or [])


def _section_tag(section: dict) -> str:
    kind = section.get("Type") or "Effect"
    cooldown, _ = number(section.get("Cooldown"))
    return f"[{kind}, {fmt(cooldown)}s cooldown]" if cooldown else f"[{kind}]"


def unlisted_bucket(prop_key: str, raw_item: dict | None) -> str | None:
    """Bucket for a property that is on no tooltip section, decided by the raw game files.

    Returns ``None`` when the raw files do not show it to be a stat the item provides.
    """
    entry = ((raw_item or {}).get("m_mapAbilityProperties") or {}).get(prop_key)
    if not isinstance(entry, dict) or not entry.get("m_eProvidedPropertyType"):
        return None
    value, _ = number(entry.get("m_strValue"))
    if not value:
        return None
    flag = entry.get("m_eStatsUsageFlags") or ""
    kind = {"Type": entry.get("m_strCSSClass"), "Key": prop_key, "UsageFlags": flag}
    as_effect = bucket("Passive", kind)
    if as_effect == "enemy" or flag:
        return as_effect  # a slow or resist reduction is an enemy effect even when unflagged
    return "innate"


def item_row(key: str, item: dict, card: dict, loc: dict, names: dict, upgrades_into: dict,
             raw_item: dict | None = None) -> dict:
    row = {column: None for column in COLUMNS}
    values = {k: number(v)[0] for k, v in item.items()}
    components = item.get("Components") or []
    row.update(
        key=key,
        name=item.get("Name"),
        category=loc.get(SLOT_TOKENS.get(item.get("Slot"), ""), item.get("Slot")),
        tier=item.get("Tier"),
        cost=item.get("Cost"),
        activation="Passive" if item.get("Activation") == "Passive" else "Active",
        activation_type=item.get("Activation"),
        is_imbue=bool(item.get("IsImbue")),
        builds_from="; ".join(names.get(c, c) for c in components) or None,
        upgrades_into="; ".join(sorted(names.get(c, c) for c in upgrades_into.get(key, []))) or None,
    )

    other_innate, conditional, enemy, texts, shown = [], [], [], [], set()
    active_cooldown = passive_cooldown = None
    for name in _SECTIONS:
        section = card.get(name)
        if not section:
            continue
        cooldown, _ = number(section.get("Cooldown"))
        if cooldown:
            if section.get("Type") == "Active" and active_cooldown is None:
                active_cooldown = cooldown
            elif passive_cooldown is None:
                passive_cooldown = cooldown
        description = clean(loc.get((section.get("DescKey") or "").lstrip("#"), ""), loc, values)
        if description:
            texts.append(f"{_section_tag(section)} {description}")
        section_conditional, section_enemy = [], []
        for prop in _section_props(section):
            prop_key = prop.get("Key") or ""
            shown.add(prop_key)
            where = bucket(section.get("Type"), prop)
            if where == "innate":
                column = _STAT_BY_KEY.get(prop_key)
                value, _ = number(prop.get("Value"))
                if column and row[column] is None and value is not None:
                    row[column] = value
                else:
                    other_innate.append(prop_text(prop, loc))
            elif where == "enemy":
                section_enemy.append(prop_text(prop, loc))
            else:
                section_conditional.append(prop_text(prop, loc))
        if section_conditional:
            conditional.append(f"{_section_tag(section)} " + "; ".join(section_conditional))
        if section_enemy:
            enemy.append(f"{_section_tag(section)} " + "; ".join(section_enemy))

    top_description = clean(item.get("Description"), loc, values)
    if top_description and not any(top_description in text for text in texts):
        texts.insert(0, top_description)

    unlisted, hidden_innate, hidden_conditional, hidden_enemy = [], [], [], []
    for prop_key, prop in (card.get("Other") or {}).items():
        if prop_key in _BORING or prop_key in shown:
            continue
        value, unit = number(prop.get("Value"))
        if value is None:
            continue
        where = unlisted_bucket(prop_key, raw_item)
        if where == "innate":
            column = _STAT_BY_KEY.get(prop_key)
            if column and row[column] is None:
                row[column] = value
            else:
                other_innate.append(prop_text(prop, loc))
            hidden_innate.append(prop_text(prop, loc))
        elif where == "enemy":
            hidden_enemy.append(prop_text(prop, loc))
        elif where == "conditional":
            hidden_conditional.append(prop_text(prop, loc))
        else:
            unlisted.append(f"{prop_key}={fmt(value)}{unit or ''}")
    if hidden_conditional:
        conditional.append("[Not on tooltip] " + "; ".join(hidden_conditional))
    if hidden_enemy:
        enemy.append("[Not on tooltip] " + "; ".join(hidden_enemy))

    row["cooldown"] = active_cooldown if active_cooldown is not None else passive_cooldown
    if row["cooldown"] is None:
        fallback = values.get("AbilityCooldown")
        row["cooldown"] = fallback if fallback and fallback > 0 else None
    row["other_innate_stats"] = "; ".join(other_innate) or None
    row["stats_not_on_tooltip"] = "; ".join(hidden_innate) or None
    row["conditional_effects"] = " | ".join(conditional) or None
    row["enemy_effects"] = " | ".join(enemy) or None
    row["unlisted_properties"] = "; ".join(unlisted) or None
    row["effect_text"] = " | ".join(texts) or None
    return row


def build_items(primary: dict, raw: dict | None = None):
    """Return ``(rows, excluded)`` for the items table, sorted by category, tier, name."""
    items, cards, loc = primary["items"], primary["item_cards"], primary["loc"]
    raw_abilities = (raw or {}).get("abilities") or {}
    shop, excluded = split_items(items)
    names = {key: item.get("Name") or key for key, item in items.items()}
    upgrades_into = {}
    for key, item in shop.items():
        for component in item.get("Components") or []:
            upgrades_into.setdefault(component, []).append(key)
    rows = [
        item_row(key, item, cards.get(key) or {}, loc, names, upgrades_into, raw_abilities.get(key))
        for key, item in shop.items()
    ]
    order = {"Weapon": 0, "Vitality": 1, "Spirit": 2}
    rows.sort(key=lambda r: (order.get(r["category"], 9), r["tier"], (r["name"] or "").lower()))
    return rows, excluded
