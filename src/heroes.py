"""Heroes table: one row per playable hero."""
from __future__ import annotations

from .text import clean, fmt, label, tidy

COLUMNS = [
    "key", "name", "hero_type", "hero_tags", "role", "gun_tag", "weapon_tags",
    "base_health", "health_per_boon", "health_regen",
    "bullet_damage", "bullet_damage_per_boon", "pellets_per_shot", "damage_per_shot",
    "fire_rate", "fire_rate_max_spin", "bullets_per_burst", "weapon_dps_level_1", "sustained_dps_level_1", "dps_per_boon",
    "clip_size", "reload_time", "reloads_single_bullets", "bullet_velocity",
    "falloff_start", "falloff_end", "falloff_end_damage_scale",
    "can_headshot", "headshot_bonus_scale_pct", "headshot_damage_taken_reduction_pct", "move_speed_while_shooting_scale",
    "light_melee", "heavy_melee", "light_melee_per_boon", "heavy_melee_per_boon",
    "move_speed", "sprint_speed", "dash_distance", "air_dash_distance",
    "stamina", "stamina_recovery_seconds",
    "spirit_power_per_boon", "base_bullet_resist", "bullet_resist_per_boon", "base_spirit_resist", "spirit_resist_per_boon",
    "base_melee_resist", "debuff_resist", "innate_bullet_lifesteal_pct",
    "bullet_lifesteal_effectiveness", "spirit_lifesteal_effectiveness", "spirit_scaling",
    "ability_1", "ability_2", "ability_3", "ability_4",
]


# The source repeats a spirit scaling under the stats derived from it; one entry is enough.
_DERIVED_SCALING = {"DPS", "SustainedDPS", "RoundsPerSecond"}


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
        # Some multi-pellet guns hit a target once however many pellets land
        # (the files' HitOnceAcrossAllBullets); their damage per shot is one pellet.
        "damage_per_shot": (
            None if bullet_damage is None or pellets is None
            else bullet_damage if weapon.get("HitOnceAcrossAllBullets") else tidy(bullet_damage * pellets)
        ),
        "fire_rate_max_spin": _get(weapon, "RoundsPerSecondAtMaxSpin"),
        "fire_rate": _get(weapon, "RoundsPerSecond"),
        "bullets_per_burst": _get(weapon, "BulletsPerBurst"),
        "weapon_dps_level_1": _get(weapon, "DPS"),
        "sustained_dps_level_1": _get(weapon, "SustainedDPS"),
        "dps_per_boon": _get(scaling, "DPS"),
        "clip_size": _get(weapon, "ClipSize"),
        "reload_time": _get(weapon, "ReloadTime"),
        "reloads_single_bullets": bool(weapon["ReloadSingle"]) if "ReloadSingle" in weapon else None,
        "falloff_end_damage_scale": _get(weapon, "FalloffEndScale"),
        "can_headshot": bool(weapon["CanCrit"]) if "CanCrit" in weapon else None,
        "headshot_bonus_scale_pct": _get(hero, "CritDamageBonusPercent"),
        "headshot_damage_taken_reduction_pct": _get(hero, "CritDamageReceivedPercent") or None,
        "bullet_resist_per_boon": _get(scaling, "BulletResist"),
        "spirit_resist_per_boon": _get(scaling, "TechResist"),
        "debuff_resist": _get(hero, "DebuffResist"),
        "innate_bullet_lifesteal_pct": _get(hero, "BulletLifesteal"),
        "bullet_lifesteal_effectiveness": _get(hero, "HeroBulletLifestealEffectiveness"),
        "spirit_lifesteal_effectiveness": _get(hero, "HeroSpiritLifestealEffectiveness"),
        "move_speed_while_shooting_scale": _get(weapon, "ShootMoveSpeed"),
        "dash_distance": _get(hero, "GroundDashDistanceInMeters"),
        "air_dash_distance": _get(hero, "AirDashDistanceInMeters"),
        "base_melee_resist": _get(hero, "MeleeResist"),
        "spirit_scaling": "; ".join(
            f"{label(loc, stat)}: {fmt(value)}" for stat, value in (hero.get("SpiritScaling") or {}).items()
            if isinstance(value, (int, float)) and value and stat not in _DERIVED_SCALING
        ) or None,
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
