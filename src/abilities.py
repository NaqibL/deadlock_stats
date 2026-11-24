"""Abilities table: one row per hero ability."""
from __future__ import annotations

from .heroes import alternate_forms, split_heroes
from .text import clean, fmt, humanise, label, number, postfix, tidy

COLUMNS = [
    "hero", "form", "slot", "key", "name", "description",
    "cooldown", "charges", "charge_cooldown", "duration", "cast_range",
    "damage", "damage_spirit_scale", "dps", "dps_spirit_scale",
    "heal", "barrier", "radius", "slow_percent", "slow_duration", "stun_duration",
    "other_properties", "spirit_scaling", "other_scaling", "internal_properties",
    "upgrade_1", "upgrade_2", "upgrade_3",
]

# Own-column properties: column -> source property keys, first match wins.
MAIN_PROPERTIES = {
    "cooldown": ("AbilityCooldown",),
    "charges": ("AbilityCharges",),
    "charge_cooldown": ("AbilityCooldownBetweenCharge",),
    "duration": ("AbilityDuration",),
    "cast_range": ("AbilityCastRange",),
    "damage": ("Damage",),
    "dps": ("DPS",),
    "heal": ("HealAmount",),
    "barrier": ("CombatBarrier",),
    "radius": ("Radius",),
    "slow_percent": ("SlowPercent",),
    "slow_duration": ("SlowDuration",),
    "stun_duration": ("StunDuration",),
}
_MAIN_KEYS = {key for keys in MAIN_PROPERTIES.values() for key in keys}

# Scale types that only say "this value is affected by the generic duration /
# range / cooldown stats". They are not build-maths coefficients.
TRIVIAL_SCALES = {"duration", "cooldown", "range", "radius", "max_charges", "charge_cooldown", "healing"}
SCALE_NAMES = {
    "spirit": "spirit power",
    "power_increase": "boon",
    "melee": "melee damage",
    "heavy_melee": "heavy melee damage",
    "weapon_damage": "weapon damage",
    "weapon_damage_increase": "weapon damage %",
    "weapon_power": "weapon power",
}
_UNIT_BY_TYPE = {"duration": "s", "cooldown": "s", "charge_cooldown": "s", "distance": "m", "range": "m", "cast": "s"}
_SKIP_INTERNAL = {"Key", "Name", "IsDisabled", "Upgrades", "BehaviourBits", "AbilityUnitTargetLimit", "ChannelMoveSpeed"}


def split_value(raw):
    """Split a source property into ``(value, unit, scales)``.

    ``scales`` maps scale type -> coefficient. A property is either a bare
    value or ``{"Value": v, "Scale": {...} | [{...}, ...]}``.
    """
    scales = {}
    if isinstance(raw, dict):
        if "Value" not in raw:
            return None, None, {}
        scale = raw.get("Scale")
        for entry in scale if isinstance(scale, list) else [scale] if scale else []:
            coefficient, _ = number(entry.get("Value"))
            if entry.get("Type") and coefficient:  # a zero coefficient is a placeholder for an upgrade
                scales[entry["Type"]] = coefficient
        raw = raw["Value"]
    value, unit = number(raw)
    return value, unit, scales


def spirit_scale(raw):
    """Spirit power (``TechPower``) coefficient of a property, or ``None``."""
    return split_value(raw)[2].get("spirit")


def _unit(loc, key, unit, kind=None):
    return unit or postfix(loc, key) or _UNIT_BY_TYPE.get(kind or "", "")


def _scale_text(scales: dict) -> str:
    parts = [f"+{fmt(c)} x {SCALE_NAMES.get(t, t)}" for t, c in scales.items() if t not in TRIVIAL_SCALES]
    return f" ({', '.join(parts)})" if parts else ""


def _card_props(card: dict):
    """Yield the labelled properties shown on an ability's tooltip card."""
    seen = set()
    for name, prop in (card.get("Headers") or {}).items():
        if name not in seen:
            seen.add(name)
            yield name, prop
    for section_name in ("Info1", "Info2", "Info3", "Info4"):
        section = card.get(section_name) or {}
        main = section.get("Main") or {}
        props = list(main.get("Props") or []) if isinstance(main, dict) else list(main)
        for prop in props + list(section.get("Alt") or []):
            key = prop.get("Key")
            if key and key not in seen:
                seen.add(key)
                yield key, prop


def upgrade_text(upgrade: dict, loc: dict, card_upgrade: dict | None = None) -> str:
    """Readable text for one ability upgrade tier, numbers first."""
    parts = []
    for key, raw in (upgrade or {}).items():
        if key == "DescKey":
            continue
        value, unit, scales = split_value(raw)
        if not value and not scales:
            continue  # nothing changes: a zero placeholder
        name = label(loc, key)
        bits = []
        if value:
            sign = "+" if value > 0 else ""
            bits.append(f"{sign}{fmt(value)}{_unit(loc, key, unit)}")
        for scale_type, coefficient in scales.items():
            if scale_type not in TRIVIAL_SCALES:
                bits.append(f"+{fmt(coefficient)} x {SCALE_NAMES.get(scale_type, scale_type)} scaling")
        if not bits:
            bits.append("0")
        parts.append(f"{name} {' and '.join(bits)}")
    text = "; ".join(parts)
    desc_key = (card_upgrade or {}).get("DescKey")
    described = clean(loc.get(desc_key or "", ""), loc)
    if described:
        text = f"{text} | {described}" if text else described
    return text


def describe(key: str, card: dict, loc: dict) -> str:
    """Ability description: the tooltip card's section texts, in order, without repeats."""
    desc_keys = [card.get("DescKey"), key + "_desc"]
    desc_keys += [(card.get(name) or {}).get("DescKey") for name in ("Info1", "Info2", "Info3", "Info4")]
    parts = []
    for desc_key in desc_keys:
        text = clean(loc.get((desc_key or "").lstrip("#"), ""), loc)
        if text and text not in parts:
            parts.append(text)
    return " ".join(parts)


def ability_row(hero_name: str, form: str | None, slot: int, key: str, ability: dict, card: dict, loc: dict) -> dict:
    row = {column: None for column in COLUMNS}
    row.update(hero=hero_name, form=form, slot=slot, key=key, name=ability.get("Name") or card.get("Name"))
    row["description"] = describe(key, card, loc) or None

    for column, keys in MAIN_PROPERTIES.items():
        for source_key in keys:
            value = split_value(ability.get(source_key))[0]
            # 0 and -1 mean "does not apply" for cooldowns, charges and the like.
            if value is not None and value > 0:
                row[column] = value
                break
    row["damage_spirit_scale"] = spirit_scale(ability.get("Damage"))
    row["dps_spirit_scale"] = spirit_scale(ability.get("DPS"))

    spirit, other_scaling, shown = [], [], set(_MAIN_KEYS)
    for source_key, raw in ability.items():
        scales = split_value(raw)[2]
        name = label(loc, source_key)
        if "spirit" in scales:
            spirit.append(f"{name}: {fmt(scales['spirit'])}")
        for scale_type, coefficient in scales.items():
            if scale_type != "spirit" and scale_type not in TRIVIAL_SCALES:
                other_scaling.append(f"{name}: {fmt(coefficient)} per {SCALE_NAMES.get(scale_type, scale_type)}")

    other = []
    for source_key, prop in _card_props(card):
        shown.add(source_key)
        if source_key in _MAIN_KEYS:
            continue
        value, unit, scales = split_value({"Value": prop.get("Value"), "Scale": prop.get("Scale")})
        if value is None or (value == 0 and not any(t not in TRIVIAL_SCALES for t in scales)):
            continue
        name = clean(prop.get("Name"), loc)
        if not name or name.startswith("Unknown("):
            name = label(loc, source_key)
        status = f" [{prop['StatusEffect']}]" if prop.get("StatusEffect") else ""
        other.append(f"{name}{status}: {fmt(value)}{_unit(loc, source_key, unit, prop.get('Type'))}{_scale_text(scales)}")

    internal = []
    for source_key, raw in ability.items():
        if source_key in shown or source_key in _SKIP_INTERNAL:
            continue
        value, unit, scales = split_value(raw)
        if value is None or isinstance(raw, bool):
            continue
        internal.append(f"{source_key}={fmt(value)}{unit or ''}{_scale_text(scales)}")

    row["other_properties"] = "; ".join(other) or None
    row["spirit_scaling"] = "; ".join(spirit) or None
    row["other_scaling"] = "; ".join(other_scaling) or None
    row["internal_properties"] = "; ".join(internal) or None

    upgrades = ability.get("Upgrades") or []
    card_upgrades = card.get("Upgrades") or []
    for index in range(3):
        if index < len(upgrades):
            card_upgrade = card_upgrades[index] if index < len(card_upgrades) else None
            row[f"upgrade_{index + 1}"] = upgrade_text(upgrades[index], loc, card_upgrade) or None
    return row


def build_abilities(primary: dict):
    """Return ``(rows, problems)``. Four rows per playable hero, plus alternate-form abilities."""
    heroes, abilities, cards, loc = primary["heroes"], primary["abilities"], primary["ability_cards"], primary["loc"]
    playable, _ = split_heroes(heroes)
    forms = alternate_forms(heroes, playable)
    rows, problems = [], []
    for hero_key, hero in playable.items():
        variants = [(None, hero_key, hero)]
        variants += [(form_hero.get("Name") or form_key, form_key, form_hero) for form_key, form_hero in forms.get(hero_key, [])]
        base_keys = {(hero.get("BoundAbilities") or {}).get(s, {}).get("Key") for s in ("1", "2", "3", "4")}
        for form, variant_key, variant in variants:
            for slot in ("1", "2", "3", "4"):
                bound = (variant.get("BoundAbilities") or {}).get(slot)
                if not bound:
                    if form is None:
                        problems.append(f"{hero.get('Name')}: no ability bound to slot {slot}")
                    continue
                key = bound.get("Key")
                if form is not None and key in base_keys:
                    continue  # shared with the base form, already listed
                ability = abilities.get(key)
                if ability is None:
                    problems.append(f"{hero.get('Name')}: ability {key} (slot {slot}) is not in ability-data.json")
                    continue
                card = (cards.get(variant_key) or {}).get(slot) or {}
                rows.append(ability_row(hero.get("Name"), form, int(slot), key, ability, card, loc))
    rows.sort(key=lambda r: ((r["hero"] or "").lower(), r["form"] or "", r["slot"]))
    return rows, problems
