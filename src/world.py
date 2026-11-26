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
    "key", "name", "group", "health", "health_second", "health_third", "health_phase_2",
    "health_gain_per_minute", "health_growth_pct_per_minute",
    "bullet_resist_pct", "spirit_resist_pct", "damage_absorbed_per_second",
    "weapon_dps", "melee_damage", "dps_vs_players", "dps_vs_troopers", "damage_growth_pct_per_minute",
    "soul_reward", "soul_reward_growth_pct_per_minute",
    "first_spawn_seconds", "respawn_seconds", "respawn_change_per_kill_seconds", "respawn_min_seconds", "note",
]
POWERUP_COLUMNS = ["key", "name", "stat", "value_at_start", "value_at_max", "start_minute", "max_minute",
                   "duration_seconds", "first_spawn_seconds", "respawn_seconds"]
BUFF_COLUMNS = ["key", "name", "stat", "level_1", "level_2", "level_3", "level_2_from_minute", "level_3_from_minute",
                "drop_weight"]
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
    ("destroyable_building", "Objective", "Citadel_Hud_KillFeedShieldName", "ShrinesGoldKill", None),
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

# What a reader needs to know to read each row. Statements about how a unit
# behaves are from Valve's patch notes (date given); see knowledge/settled.md.
UNIT_NOTES = {
    "npc_boss_tier1": "Soul reward is the team total. Also has a resist that decays over the match "
                      "(+50% to -50% over 12 min, patch note 2026-05-22), not in the files read.",
    "npc_boss_tier2": "health / second / third: each Walker left standing gets tougher as others die. Soul reward "
                      "is the team total. Decaying resist +65% to -65% over 18 min (patch note 2026-03-06). "
                      "Latest patch note on bullet resist says +15%; files say 35.",
    "npc_barrack_boss": "Soul reward is the team total.",
    "destroyable_building": "health is the first Shrine, health_second the other once one has died. "
                            "Invulnerable until a pair of Base Guardians is destroyed (patch note 2026-05-22).",
    "npc_boss_tier3": "health_gain_per_minute applies from minute 20 (phase 1). Files say 12000 / 12000; the last "
                      "patch note giving Patron health (2024-12-06) said 7500 / 13500.",
    "npc_super_neutral": "Present from 0:00. Health is fixed when it spawns: base plus gain per minute of game time. "
                         "Respawn shortens by 60s per kill down to 300s. Soaks a flat amount of damage per second, "
                         "growing 5 per minute. Files say 15600 health; latest patch note (2026-03-06) says 13000.",
    "trooper_normal": "Health is +50% after 35 minutes. Bounty is in the Rules table.",
    "trooper_melee": "Health is +50% after 35 minutes.",
    "trooper_medic": "Health is +50% after 35 minutes. Damage grows 3% per minute.",
    "neutral_trooper_weak": "Values are per creep at minute 0.",
    "neutral_trooper_normal": "Values are per creep at minute 0.",
    "neutral_trooper_strong": "Values are per creep at minute 0. Patch notes imply a 420s respawn; files say 335.",
    "neutral_sinners_sacrifice": "Melee only: bullets and abilities do nothing. Health is a hit counter. "
                                 "Returns 80 damage per hit.",
}
# Units whose generic weapon block is not what any target takes: the files give
# per-target damage instead (guardians, troopers) or the unit does not shoot.
_NO_WEAPON_DPS = {"npc_boss_tier1", "npc_barrack_boss", "trooper_normal", "trooper_melee", "trooper_medic",
                  "neutral_sinners_sacrifice"}


# Server settings (convars.json) that are gameplay rules. Where a patch note states
# the same number, it matches these (checked 2026-11: respawn curve, trooper bounty
# and waves, urn reward, rift timing, kill bounty).
CONVAR_RULES = [
    ("citadel_player_starting_gold", "Starting souls"),
    ("citadel_item_sell_price_ratio", "Item sell value (fraction of price)"),
    ("citadel_player_gold_reward_min", "Hero kill bounty at 0:00 (souls)"),
    ("citadel_player_gold_reward_max", "Hero kill bounty at full ramp (souls)"),
    ("citadel_player_gold_reward_time", "Hero kill bounty reaches full ramp at (s)"),
    ("citadel_player_gold_reward_first_kill_bonus", "Bonus for each player's first kill (souls)"),
    ("citadel_bounty_player_assist_window", "Assist window (s)"),
    ("citadel_player_gold_killer_to_assist_ratio", "Killer's share relative to an assister's"),
    ("citadel_trooper_gold_reward", "Trooper bounty at 0:00 (souls)"),
    ("citadel_trooper_gold_reward_bonus_per_minute", "Trooper bounty growth per minute (souls)"),
    ("citadel_super_trooper_gold_mult", "Super trooper bounty multiplier"),
    ("citadel_trooper_spawn_initial", "First trooper wave at (s)"),
    ("citadel_trooper_spawn_interval_early", "Trooper wave interval, early (s)"),
    ("citadel_trooper_spawn_interval_late", "Trooper wave interval, late (s)"),
    ("citadel_trooper_spawn_interval_late_time", "Late wave interval starts at (min)"),
    ("citadel_trooper_spawn_interval_very_late", "Trooper wave interval, very late (s)"),
    ("citadel_trooper_spawn_interval_very_late_time", "Very late wave interval starts at (min)"),
    ("citadel_trooper_health_mult", "Trooper health multiplier, late game"),
    ("citadel_trooper_health_mult_gametime", "Trooper late-game health starts at (min)"),
    ("citadel_neutral_health_growth_pct_per_min", "Neutral creep health growth per minute (%)"),
    ("citadel_player_spawn_time_min_ramp_1", "Respawn time until 5 min (s)"),
    ("citadel_player_spawn_time_min_ramp_2", "Respawn time at 20 min (s)"),
    ("citadel_player_spawn_time_min_ramp_3", "Respawn time at 30 min (s)"),
    ("citadel_player_spawn_time_max_ramp_3", "Respawn time at 40 min (s)"),
    ("citadel_player_spawn_time_max_respawn_time", "Respawn time cap (s)"),
    ("citadel_player_death_no_heroes_respawn_penalty", "Extra respawn time when not killed by a hero (s)"),
    ("citadel_player_spawn_time_rich_nw_penalty_min_ramp_extratime", "Extra respawn time when richer than enemy average, minimum (s)"),
    ("citadel_player_spawn_time_rich_nw_penalty_max_ramp_extratime", "Extra respawn time when richer than enemy average, maximum (s)"),
    ("citadel_tier3_phase1_kill_respawn_reduction", "Respawn time cut for the losing team when a Patron first falls (s)"),
    ("citadel_crate_spawn_initial_delay", "Soul Urn first spawn (s)"),
    ("citadel_crate_respawn_interval", "Soul Urn spawn interval (s)"),
    ("citadel_crate_reward_base", "Soul Urn reward at 0:00 (souls)"),
    ("citadel_crate_reward_time_multiplier", "Soul Urn reward growth per minute (souls)"),
    ("citadel_idol_cashin_buff_count", "Soul Urn permanent buffs for the runner"),
    ("citadel_idol_duration_until_decay", "Soul Urn reward starts decaying after (s)"),
    ("citadel_idol_decay_duration", "Soul Urn reward decays over (s)"),
    ("citadel_koth_spawn_initial_delay", "Unstable Rift first spawn (s, plus or minus the window)"),
    ("citadel_koth_spawn_window", "Unstable Rift spawn window (s)"),
    ("citadel_koth_respawn_interval", "Unstable Rift spawn interval (s)"),
    ("citadel_koth_warning_time", "Unstable Rift warning before spawn (s)"),
    ("citadel_koth_reward_base", "Unstable Rift reward at 0:00 (souls)"),
    ("citadel_koth_reward_time_multiplier", "Unstable Rift reward growth per minute (souls)"),
    ("citadel_player_gold_per_level_postmax", "Souls per level after the last boon"),
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


def _convar(primary: dict, name: str):
    """A numeric server setting from convars.json, or None."""
    value = (primary.get("convars") or {}).get(name)
    if isinstance(value, dict):
        value = value.get("value")
    return _num(value)


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
        base = npcs.get("trooper_base") or {}
        versus = lambda target: _num(((unit.get(target) or base.get(target)) or {}).get("BaseDPS"))  # noqa: E731
        is_trooper, is_neutral = group == "Trooper", key.startswith("neutral_trooper")
        row = {column: None for column in UNIT_COLUMNS}
        row.update({
            "key": key,
            "name": clean(loc.get(name, ""), loc) or name,
            "group": group,
            "health": _num(unit.get("MaxHealth")) or _num(unit.get("StartingHealth")) or _num(unit.get("MaxHealthGenerator")),
            "health_second": _num((unit.get("EmpoweredModifierLevel1") or {}).get("MaxHealth")) or _num(unit.get("MaxHealthGeneratorSecond")),
            "health_third": _num((unit.get("EmpoweredModifierLevel2") or {}).get("MaxHealth")),
            "health_phase_2": _num(unit.get("Phase2Health")),
            "health_gain_per_minute": _num(unit.get("HealthGainPerMinute"))
                                      or _num((unit.get("ObjectiveHealthGrowthPhase1") or {}).get("GrowthPerMinute")),
            "health_growth_pct_per_minute": _convar(primary, "citadel_neutral_health_growth_pct_per_min") if is_neutral else None,
            "bullet_resist_pct": _modifier(unit, "BULLET_ARMOR_DAMAGE_RESIST", "BULLET_DAMAGE_REDUCTION_PERCENT"),
            "spirit_resist_pct": _modifier(unit, "ABILITY_DAMAGE_REDUCTION_PERCENT"),
            "damage_absorbed_per_second": _num((unit.get("ShieldLogic") or {}).get("BaseAbsorptionPerSecond")),
            "weapon_dps": None if key in _NO_WEAPON_DPS else _num(weapon.get("DPS")),
            "melee_damage": _num(unit.get("MeleeDamage")),
            "dps_vs_players": _num(unit.get("PlayerDPS")) or (versus("VSPlayer") if is_trooper else None),
            "dps_vs_troopers": _num(unit.get("TrooperDPS")) or (versus("VSTrooper") if is_trooper else None),
            "damage_growth_pct_per_minute": _num((unit.get("NeutralDamageGrowth") or {}).get("DamageGrowthPctPerMin"))
                                            or (_num(unit.get("DPSPctGrowthPerMinute")) or None),
            "soul_reward": _num(unit.get("GoldReward")) or _num(bounties.get(bounty)),
            "soul_reward_growth_pct_per_minute": _num(unit.get("GoldRewardBonusPercentPerMinute")),
            "first_spawn_seconds": _num(camp.get("InitialSpawnDelayInSeconds")),
            "respawn_seconds": _num(camp.get("SpawnIntervalInSeconds")),
            "respawn_change_per_kill_seconds": _num(camp.get("SpawnIntervalChange")) or None,
            "respawn_min_seconds": _num(camp.get("SpawnIntervalMin")) or None,
            "note": UNIT_NOTES.get(key),
        })
        rows.append(row)
    return rows, missing


def _stat_name(loc: dict, modifier: str) -> str:
    text = loc.get(f"{modifier}_label")
    if isinstance(text, str) and text.strip():
        return clean(text, loc)
    return modifier.replace("MODIFIER_VALUE_", "").replace("_", " ").title()


def build_powerups(primary: dict) -> list:
    """The timed powerups at the bridges: what each gives early and at full strength."""
    misc, loc = primary.get("misc") or {}, primary["loc"]
    spawner = misc.get("citadel_item_powerup_spawner") or {}
    rows = []
    for key in spawner.get("PickupChances") or {}:
        modifier = (misc.get(key) or {}).get("Modifer") or {}
        for value in modifier.get("ModifierValues") or []:
            rows.append({
                "key": key, "name": clean(loc.get(key, ""), loc) or key,
                "stat": _stat_name(loc, value.get("ModifierValue", "")),
                "value_at_start": _num(value.get("valueMin")), "value_at_max": _num(value.get("valueMax")),
                "start_minute": _num(modifier.get("TimeMin")), "max_minute": _num(modifier.get("TimeMax")),
                "duration_seconds": _num(modifier.get("Duration")),
                "first_spawn_seconds": _num(spawner.get("InitialSpawnTime")),
                "respawn_seconds": _num(spawner.get("SpawnInterval")),
            })
    return rows


def build_permanent_buffs(primary: dict) -> list:
    """The permanent stat buffs (golden statues and other sources), by level."""
    misc, loc = primary.get("misc") or {}, primary["loc"]
    loot = ((primary.get("generic") or {}).get("BreakablePowerupLootParams") or {}).get("PickupsByMatchTimeMins") or {}
    minutes = sorted(int(m) for m in loot if str(m).isdigit())
    weights = loot.get(str(minutes[0])) or {} if minutes else {}
    rows = []
    for key in sorted(k for k in misc if k.endswith("_permanent_pickup")):
        levels = [misc.get(key) or {}, misc.get(key + "_lv2") or {}, misc.get(key + "_lv3") or {}]
        values = [{v.get("ModifierValue"): _num(v.get("value")) for v in (lvl.get("Modifer") or {}).get("ScriptValues") or []}
                  for lvl in levels]
        for stat in values[0]:
            rows.append({
                "key": key, "name": clean(loc.get(levels[0].get("NameLocString") or "", ""), loc) or key,
                "stat": _stat_name(loc, stat or ""),
                "level_1": values[0].get(stat), "level_2": values[1].get(stat), "level_3": values[2].get(stat),
                "level_2_from_minute": minutes[1] if len(minutes) > 1 else None,
                "level_3_from_minute": minutes[2] if len(minutes) > 2 else None,
                "drop_weight": _num(weights.get(key)),
            })
    return rows


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
    for field, rule in (("Tier1GoldKill", "Guardian kill bounty, team total (souls)"), ("Tier2GoldKill", "Walker kill bounty, team total (souls)"),
                        ("BaseGuardiansGoldKill", "Base Guardian kill bounty, team total (souls)"), ("ShrinesGoldKill", "Shrine kill bounty, team total (souls)"),
                        ("NearPlayerSplitPct", "Objective bounty: share to nearby players (%), rest split among all six")):
        add(rule, objective.get(field), f"ObjectiveParams.{field}")
    # Meaning of the two share lists is from the patch notes (2025-11-21, 2025-11-23,
    # 2025-12-16): the value is what EACH player gets, so the total paid is N times it.
    for index, value in enumerate(generic.get("HeroKillGoldShareFrac") or []):
        add(f"Hero kill: average share of the bounty per participant, {index + 1} in the kill",
            value, f"HeroKillGoldShareFrac[{index}]")
    for index, value in enumerate(generic.get("TrooperKillGoldShareFrac") or []):
        add(f"Trooper kill: share of the bounty each player gets, {index + 1} nearby",
            value, f"TrooperKillGoldShareFrac[{index}]")
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
    for convar, rule in CONVAR_RULES:
        add(rule, _convar(primary, convar), f"convar {convar}")
    return rows
