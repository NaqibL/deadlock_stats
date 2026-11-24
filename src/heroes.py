"""Heroes table: one row per playable hero."""
from __future__ import annotations

from .text import clean, tidy

COLUMNS = [
    "key", "name", "hero_type", "hero_tags", "role", "gun_tag", "weapon_tags",
    "base_health", "health_per_boon", "health_regen",
    "bullet_damage", "bullet_damage_per_boon", "pellets_per_shot", "damage_per_shot",
    "fire_rate", "weapon_dps_level_1", "clip_size", "reload_time", "bullet_velocity",
    "falloff_start", "falloff_end",
    "light_melee", "heavy_melee", "light_melee_per_boon", "heavy_melee_per_boon",
    "move_speed", "sprint_speed", "stamina", "stamina_recovery_seconds", "stamina_regen_per_second",
    "spirit_power_per_boon", "base_bullet_resist", "base_spirit_resist",
    "ability_1", "ability_2", "ability_3", "ability_4",
]


def classify(key: str, hero: dict) -> str | None:
    """Return ``None`` for a playable hero, otherwise the reason it is excluded.

    The primary source has no single "released" flag. ``InDevelopment`` cannot be
    used: it is still true for heroes that are live in the roster. What separates
    real heroes from the rest is: not disabled, has a hero id, and has a hero
    type (Brawler, Mystic, ...). The cross-check confirms this set against the
    raw files' ``m_eHeroDevelopmentState``.
    """
    if hero.get("IsDisabled"):
        return "disabled in the game files"
    if hero.get("Id") is None:
        return "no hero id (alternate form of another hero, not separately pickable)"
    if not hero.get("Type"):
        return "no hero type (test or debug hero)"
    if not hero.get("Name"):
        return "no English name"
    return None


def split_heroes(heroes: dict):
    """Split the source heroes into playable ones and ``(key, name, reason)`` exclusions."""
    playable, excluded = {}, []
    for key, hero in heroes.items():
        reason = classify(key, hero)
        if reason is None:
            playable[key] = hero
        else:
            excluded.append((key, hero.get("Name") or "", reason))
    return playable, excluded


def alternate_forms(heroes: dict, playable: dict) -> dict:
    """Map playable hero key -> list of ``(form_key, form_hero)`` for its alternate forms."""
    forms = {}
    for key, hero in heroes.items():
        if hero.get("Id") is not None or hero.get("IsDisabled"):
            continue
        for base_key in playable:
            if key != base_key and key.startswith(base_key + "_"):
                forms.setdefault(base_key, []).append((key, hero))
    return forms


def _get(mapping, key):
    value = (mapping or {}).get(key)
    return tidy(value) if isinstance(value, (int, float)) and not isinstance(value, bool) else None


def _loc_token(loc: dict, token) -> str:
    return clean(loc.get(str(token or "").lstrip("#"), ""), loc)


def hero_row(key: str, hero: dict, loc: dict, raw_hero: dict | None = None) -> dict:
    """``raw_hero`` is the hero's entry in the raw game files; it supplies the
    hero tags and gun tag, which the primary source does not carry."""
    raw_hero = raw_hero if isinstance(raw_hero, dict) else {}
    hero_tags = [t for t in (_loc_token(loc, tag) for tag in raw_hero.get("m_vecHeroTags") or []) if t]
    weapon = hero.get("Weapon") or {}
    scaling = hero.get("LevelScaling") or {}
    bullet_damage = _get(weapon, "BulletDamage")
    pellets = _get(weapon, "BulletsPerShot")
    tags = [clean(loc.get(tag, ""), loc) or tag for tag in weapon.get("WeaponTypes") or []]
    abilities = hero.get("BoundAbilities") or {}
    row = {
        "key": key,
        "name": hero.get("Name"),
        "hero_type": hero.get("Type"),
        "hero_tags": "; ".join(hero_tags) or None,
        "gun_tag": _loc_token(loc, raw_hero.get("m_strGunTag")) or None,
        "role": clean(loc.get(hero.get("Role") or "", ""), loc) or None,
        "weapon_tags": "; ".join(tags) or None,
        "base_health": _get(hero, "MaxHealth"),
        "health_per_boon": _get(scaling, "MaxHealth"),
        "health_regen": _get(hero, "BaseHealthRegen"),
        "bullet_damage": bullet_damage,
        "bullet_damage_per_boon": _get(scaling, "BulletDamage"),
        "pellets_per_shot": pellets,
        "damage_per_shot": tidy(bullet_damage * pellets) if bullet_damage is not None and pellets is not None else None,
        "fire_rate": _get(weapon, "RoundsPerSecond"),
        "weapon_dps_level_1": _get(weapon, "DPS"),
        "clip_size": _get(weapon, "ClipSize"),
        "reload_time": _get(weapon, "ReloadTime"),
        "bullet_velocity": _get(weapon, "BulletSpeed"),
        "falloff_start": _get(weapon, "FalloffStartRange"),
        "falloff_end": _get(weapon, "FalloffEndRange"),
        "light_melee": _get(hero, "LightMeleeDamage"),
        "heavy_melee": _get(hero, "HeavyMeleeDamage"),
        "light_melee_per_boon": _get(scaling, "LightMeleeDamage"),
        "heavy_melee_per_boon": _get(scaling, "HeavyMeleeDamage"),
        "move_speed": _get(hero, "MaxMoveSpeed"),
        "sprint_speed": _get(hero, "SprintSpeed"),
        "stamina": _get(hero, "Stamina"),
        "stamina_recovery_seconds": _get(hero, "StaminaCooldown"),
        "stamina_regen_per_second": _get(hero, "StaminaRegenPerSecond"),
        "spirit_power_per_boon": _get(scaling, "TechPower"),
        "base_bullet_resist": _get(hero, "BulletResist"),
        "base_spirit_resist": _get(hero, "TechResist"),
    }
    for slot in ("1", "2", "3", "4"):
        row[f"ability_{slot}"] = (abilities.get(slot) or {}).get("Name")
    return row


def build_heroes(primary: dict, raw: dict | None = None):
    """Return ``(rows, excluded)`` for the heroes table, sorted by name."""
    playable, excluded = split_heroes(primary["heroes"])
    raw_heroes = (raw or {}).get("heroes") or {}
    rows = [hero_row(key, hero, primary["loc"], raw_heroes.get(key)) for key, hero in playable.items()]
    rows.sort(key=lambda r: (r["name"] or "").lower())
    return rows, excluded
