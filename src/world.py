"""Game-wide tables that matter for build theory: investment bonuses, soul
progression, objectives and creeps, and a few global rules.

These come from the primary source's ``item-investment-data.json``,
``soul-unlock-data.json``, ``npc-data.json``, ``misc-data.json`` and
``generic-data.json``. They are data tables from the files, not derived formulas.
"""
from __future__ import annotations

from .text import clean, tidy

INVESTMENT_COLUMNS = ["category", "souls_spent", "bonus", "bonus_unit", "bonus_stat"]
PROGRESSION_COLUMNS = [
    "level", "souls_required", "boon", "ability_unlock", "ability_point",
    "total_boons", "total_ability_unlocks", "total_ability_points",
]
UNIT_COLUMNS = [
    "key", "name", "group", "health", "health_phase_2", "health_gain_per_minute",
    "bullet_resist_pct", "spirit_resist_pct", "weapon_dps", "bullet_damage", "melee_damage",
    "dps_vs_players", "dps_vs_troopers", "soul_reward", "soul_reward_growth_pct_per_minute",
    "first_spawn_seconds", "respawn_seconds",
]
RULE_COLUMNS = ["rule", "value", "source_field"]

_INVESTMENT_STAT = {
    "Weapon": "Citadel_ModBonus_WeaponInvestmentDesc",
    "Vitality": "Citadel_ModBonus_ArmorInvestmentDesc",
    "Spirit": "Citadel_ModBonus_TechInvestmentDesc",
}

# The files hold bare numbers. The units are from Valve's patch notes (2025-11-21,
# 2026-03-21, 2026-04-30): weapon and vitality bonuses are written with a % sign,
# vitality as "% base hp", and spirit as a plain amount of spirit power.
_INVESTMENT_UNIT = {"Weapon": "% weapon damage", "Vitality": "% of base health", "Spirit": "spirit power (flat)"}

# (source key, group, name or localisation token, objective bounty field, neutral camp key)
# The files give no display name for some units; those names are written here.
UNITS = [
    ("npc_boss_tier1", "Objective", "guardian_unit", "Tier1GoldKill", None),
    ("npc_boss_tier2", "Objective", "walker_unit", "Tier2GoldKill", None),
    ("npc_barrack_boss", "Objective", "Base Guardian", "BaseGuardiansGoldKill", None),
    ("npc_boss_tier3", "Objective", "Citadel_Hud_KillFeedTitan", None, None),
    ("npc_super_neutral", "Objective", "Mid Boss", None, "neutral_camp_midboss"),
    ("trooper_normal", "Trooper", "Citadel_AttackerClass_CLASS_TROOPER", None, None),
    ("trooper_melee", "Trooper", "Citadel_AttackerClass_CLASS_TROOPER_MELEE", None, None),
    ("trooper_medic", "Trooper", "Citadel_AttackerClass_CLASS_TROOPER_MEDIC", None, None),
    ("neutral_trooper_weak", "Neutral camp", "Small camp creep", None, "neutral_camp_weak"),
    ("neutral_trooper_normal", "Neutral camp", "Medium camp creep", None, "neutral_camp_medium"),
    ("neutral_trooper_strong", "Neutral camp", "Large camp creep", None, "neutral_camp_strong"),
    ("neutral_sinners_sacrifice", "Neutral camp", "neutral_sinners", None, "neutral_camp_vaults"),
]


def _num(value):
    return tidy(value) if isinstance(value, (int, float)) and not isinstance(value, bool) else None


def build_investment(primary: dict) -> list:
    """Bonus granted at each souls-spent threshold, per shop category."""
    data = (primary.get("investment") or {}).get("ItemInvestments") or {}
    loc = primary["loc"]
    rows = []
    for category in ("Weapon", "Vitality", "Spirit"):
        stat = clean(loc.get(_INVESTMENT_STAT[category], ""), loc) or None
        for step in data.get(category) or []:
            rows.append({
                "category": category, "souls_spent": _num(step.get("GoldThreshold")),
                "bonus": _num(step.get("Bonus")), "bonus_unit": _INVESTMENT_UNIT[category],
                "bonus_stat": stat,
            })
    return rows


def build_progression(primary: dict) -> list:
    """What each soul threshold grants: a boon, an ability unlock, an ability point."""
    rows, boons, unlocks, points = [], 0, 0, 0
    for level, step in enumerate(primary.get("soul_unlocks") or []):
        boon = 1 if step.get("PowerIncrease") else 0
        unlock = int(step.get("AbilityUnlocks") or 0)
        point = int(step.get("AbilityPoints") or 0)
        boons, unlocks, points = boons + boon, unlocks + unlock, points + point
        rows.append({
            "level": level, "souls_required": _num(step.get("RequiredSouls")),
            "boon": boon or None, "ability_unlock": unlock or None, "ability_point": point or None,
            "total_boons": boons, "total_ability_unlocks": unlocks, "total_ability_points": points,
        })
    return rows


def _modifier(unit: dict, *names):
    for modifier in unit.get("IntrinsicModifiers") or []:
        for name in names:
            if isinstance(modifier, dict) and name in modifier:
                return _num(modifier[name])
    return None


def build_units(primary: dict):
    """Return ``(rows, missing)`` for objectives, troopers and neutral creeps."""
    npcs, misc, loc = primary.get("npcs") or {}, primary.get("misc") or {}, primary["loc"]
    bounties = (primary.get("generic") or {}).get("ObjectiveParams") or {}
    rows, missing = [], []
    for key, group, name, bounty, camp_key in UNITS:
        unit = npcs.get(key)
        if not isinstance(unit, dict):
            missing.append(key)
            continue
        weapon = unit.get("Weapon") or {}
        camp = misc.get(camp_key) or {} if camp_key else {}
        rows.append({
            "key": key,
            "name": clean(loc.get(name, ""), loc) or name,
            "group": group,
            "health": _num(unit.get("MaxHealth")) or _num(unit.get("StartingHealth")),
            "health_phase_2": _num(unit.get("Phase2Health")),
            "health_gain_per_minute": _num(unit.get("HealthGainPerMinute")),
            "bullet_resist_pct": _modifier(unit, "BULLET_ARMOR_DAMAGE_RESIST", "BULLET_DAMAGE_REDUCTION_PERCENT"),
            "spirit_resist_pct": _modifier(unit, "ABILITY_DAMAGE_REDUCTION_PERCENT"),
            "weapon_dps": _num(weapon.get("DPS")),
            "bullet_damage": _num(weapon.get("BulletDamage")),
            "melee_damage": _num(unit.get("MeleeDamage")),
            "dps_vs_players": _num(unit.get("PlayerDPS")),
            "dps_vs_troopers": _num(unit.get("TrooperDPS")),
            "soul_reward": _num(unit.get("GoldReward")) or _num(bounties.get(bounty)),
            "soul_reward_growth_pct_per_minute": _num(unit.get("GoldRewardBonusPercentPerMinute")),
            "first_spawn_seconds": _num(camp.get("InitialSpawnDelayInSeconds")),
            "respawn_seconds": _num(camp.get("SpawnIntervalInSeconds")),
        })
    return rows, missing


def build_rules(primary: dict) -> list:
    """A few global numbers. ``source_field`` is the name in the game files, so
    the reading of each value can be checked."""
    generic = primary.get("generic") or {}
    rows = []

    def add(rule, value, field):
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            rows.append({"rule": rule, "value": tidy(value), "source_field": field})

    for tier, price in enumerate(generic.get("ItemPricePerTier") or []):
        if 1 <= tier <= 4:
            add(f"Item price, tier {tier}", price, f"ItemPricePerTier[{tier}]")
    objective = generic.get("ObjectiveParams") or {}
    for field, rule in (("Tier1GoldKill", "Guardian kill bounty (souls)"), ("Tier2GoldKill", "Walker kill bounty (souls)"),
                        ("BaseGuardiansGoldKill", "Base Guardian kill bounty (souls)"), ("ShrinesGoldKill", "Shrine kill bounty (souls)"),
                        ("NearPlayerSplitPct", "Objective bounty share for nearby players (%)")):
        add(rule, objective.get(field), f"ObjectiveParams.{field}")
    for field, rule in (("HeroKillGoldShareFrac", "Hero kill soul share"), ("TrooperKillGoldShareFrac", "Trooper kill soul share")):
        for index, value in enumerate(generic.get(field) or []):
            add(f"{rule}, {index + 1} player(s) sharing", value, f"{field}[{index}]")
    # Rejuvenator: only the fields the current design uses. The files still carry
    # TrooperHealthMult and PlayerRespawnMult lists, but the 2025-07-29 patch notes
    # say the Rejuvenator no longer buffs troopers or shortens respawns, so they are
    # left out. See knowledge/mechanics/mid-boss-and-rejuvenator.md.
    rejuv = generic.get("RejuvParams") or {}
    add("Rejuvenator duration (s)", rejuv.get("RejuvinatorBuffDuration"), "RejuvParams.RejuvinatorBuffDuration")
    add("Rejuvenator drop count", rejuv.get("RejuvinatorDropCount"), "RejuvParams.RejuvinatorDropCount")
    add("Rejuvenator time to drop (s)", rejuv.get("RejuvinatorDropDuration"), "RejuvParams.RejuvinatorDropDuration")
    pickup = ((primary.get("misc") or {}).get("citadel_item_pickup_rejuv") or {}).get("RebirthModifier") or {}
    add("Rejuvenator revive delay (s)", pickup.get("RespawnDelay"), "citadel_item_pickup_rejuv.RebirthModifier.RespawnDelay")
    add("Rejuvenator revive health (%)", pickup.get("RespawnLifePct"), "citadel_item_pickup_rejuv.RebirthModifier.RespawnLifePct")
    return rows
