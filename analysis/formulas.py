"""Formulas for reasoning about Deadlock builds, read against the sheet in ``output/``.

Every function says how far its rule can be trusted:

- **Data**: the number or rule is in the game files the sheet is built from.
- **Settled**: ``knowledge/settled.md`` answers it from the files, server settings or patch notes.
- **Community**: from deadlock.wiki (player-written), not from the files or Valve.
- **Inferred**: no source states it; it follows from field names or arithmetic.
- **Assumption**: chosen so the arithmetic can go ahead; ``analysis/formulas.md`` says how to test it.

See ``analysis/formulas.md`` for the explanation, worked examples and tests.
"""

from __future__ import annotations

import csv
from functools import lru_cache
from pathlib import Path

OUTPUT = Path(__file__).resolve().parent.parent / "output"


# ---------------------------------------------------------------- loading


@lru_cache(maxsize=None)
def table(name: str, output_dir: str | None = None) -> list[dict]:
    """Rows of ``output/<name>.csv`` as dicts of strings."""
    path = Path(output_dir) if output_dir else OUTPUT
    with open(path / f"{name}.csv", newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _num(value: str) -> float | None:
    return float(value) if value not in ("", None) else None


def rule(source_field: str) -> float:
    """A value from ``rules.csv`` by its ``source_field`` (Data)."""
    for row in table("rules"):
        if row["source_field"] == source_field:
            return float(row["value"])
    raise KeyError(source_field)


def hero(name: str) -> dict:
    for row in table("heroes"):
        if row["name"] == name:
            return row
    raise KeyError(name)


# ---------------------------------------------------------------- souls and levels


def level_at(souls: float) -> dict:
    """The last ``progression.csv`` row reached with this many souls collected (Data).

    Returns boons, ability unlocks and ability points held. Whether the 600 starting
    souls count toward thresholds is open.
    """
    reached = [r for r in table("progression") if float(r["souls_required"]) <= souls]
    row = reached[-1]
    return {k: int(row[k]) for k in ("level", "total_boons", "total_ability_unlocks", "total_ability_points")}


def hero_stat(name: str, stat: str, boons: int) -> float:
    """Base plus per-boon growth (Data): ``stat`` + ``stat_per_boon`` x boons.

    ``stat`` is a base column: ``base_health``, ``bullet_damage``, ``light_melee``,
    ``heavy_melee``, or ``weapon_dps_level_1`` (grows by ``dps_per_boon``).
    """
    h = hero(name)
    growth = {
        "base_health": "health_per_boon",
        "bullet_damage": "bullet_damage_per_boon",
        "light_melee": "light_melee_per_boon",
        "heavy_melee": "heavy_melee_per_boon",
        "weapon_dps_level_1": "dps_per_boon",
    }[stat]
    return float(h[stat]) + float(h[growth]) * boons


def spirit_power_from_boons(name: str, boons: int) -> float:
    """Spirit power a hero holds from boons alone (Data)."""
    return float(hero(name)["spirit_power_per_boon"]) * boons


# ---------------------------------------------------------------- investment


def investment_bonus(category: str, souls_spent: float) -> float:
    """Investment bonus held after spending this many souls in a shop tab (Data; units Settled).

    Weapon: % weapon damage. Vitality: % of base health. Spirit: flat spirit power.
    ``bonus`` is the cumulative total at each threshold, not an increment.
    """
    rows = [r for r in table("investment") if r["category"] == category and float(r["souls_spent"]) <= souls_spent]
    return float(rows[-1]["bonus"]) if rows else 0.0


def health_with_vitality(name: str, boons: int, vitality_spent: float, item_health: float = 0.0,
                         applies_to_boon_health: bool = True) -> float:
    """Max health from base, boons, vitality investment and item bonus health.

    Inferred: the vitality % applies to starting health plus boon health ("Base Health")
    and not to item bonus health. ``applies_to_boon_health=False`` gives the other reading.
    """
    h = hero(name)
    start = float(h["base_health"])
    boon_health = float(h["health_per_boon"]) * boons
    base = start + boon_health if applies_to_boon_health else start
    return start + boon_health + base * investment_bonus("Vitality", vitality_spent) / 100 + item_health


def gun_dps(name: str, boons: int, weapon_damage_pct: float) -> float:
    """Gun DPS with a weapon damage bonus.

    Assumption: all weapon damage % (investment and items) adds into one bonus that
    multiplies base-plus-boon damage. Open; see formulas.md, test 1.
    """
    return hero_stat(name, "weapon_dps_level_1", boons) * (1 + weapon_damage_pct / 100)


# ---------------------------------------------------------------- abilities


def ability_value(base: float, spirit_coefficient: float, spirit_power: float) -> float:
    """Ability value = base + coefficient x spirit power (Settled). Upgrades add to both terms."""
    return base + spirit_coefficient * spirit_power


def spirit_gain_per_100(base: float, spirit_coefficient: float) -> float:
    """Extra value from 100 spirit power, as a fraction of base (computed)."""
    return spirit_coefficient * 100 / base


# ---------------------------------------------------------------- resists (Community: deadlock.wiki)


def _stack(fractions) -> float:
    remaining = 1.0
    for f in fractions:
        remaining *= 1 - f
    return 1 - remaining


def total_resist(resists) -> float:
    """Resists stack multiplicatively: 1 - (1 - R1)(1 - R2)... (Community). Fractions, not %."""
    return _stack(resists)


def total_reduction(reductions) -> float:
    """Resist reductions (shred) stack multiplicatively among themselves (Community)."""
    return _stack(reductions)


def final_resist(resists=(), reductions=()) -> float:
    """Total resist minus total reduction; can go negative (Community)."""
    return total_resist(resists) - total_reduction(reductions)


def damage_taken(resist: float) -> float:
    """Fraction of incoming damage taken at a final resist; above 1 when resist is negative (Community)."""
    return 1 - resist


def effective_health(health: float, resist: float) -> float:
    """Damage needed to kill: health / (1 - resist). Follows from the stacking rule."""
    return health / damage_taken(resist)


def shred_damage_gain(target_resist: float, shred: float) -> float:
    """Relative damage gain from shred against a target's resist: (1 - R + S) / (1 - R) - 1."""
    return damage_taken(target_resist - shred) / damage_taken(target_resist) - 1


# ---------------------------------------------------------------- sharing souls


def trooper_share(players: int) -> dict:
    """Trooper bounty fraction for each nearby player, and the team total (Settled)."""
    each = rule(f"TrooperKillGoldShareFrac[{players - 1}]")
    return {"each": each, "team_total": each * players}


def hero_kill_split(bounty: float, players: int) -> dict:
    """Souls from a hero kill for the killer, each assister and the team.

    Settled: the table value is the average share per participant, so the team total is
    N x value x bounty. Inferred: the killer gets ``killer_to_assist_ratio`` (2.2) times an
    assister, which is how the split below is made; the exact rule is not stated.
    """
    average = rule(f"HeroKillGoldShareFrac[{players - 1}]")
    team = average * players * bounty
    ratio = rule("convar citadel_player_gold_killer_to_assist_ratio")
    assister = team / (ratio + players - 1)
    killer = team - assister * (players - 1)
    return {"killer": killer, "assister": assister if players > 1 else 0.0, "team_total": team}


def objective_split(bounty: float, nearby: int) -> dict:
    """Objective bounty: 25% to nearby players, the rest split among all six (Settled).

    Inferred: the nearby share is split evenly among nearby players.
    """
    near_pct = rule("ObjectiveParams.NearPlayerSplitPct") / 100
    rest_each = bounty * (1 - near_pct) / 6
    return {"each_nearby": bounty * near_pct / nearby + rest_each, "each_other": rest_each, "team_total": bounty}


def hero_kill_bounty(minute: float) -> float:
    """Base hero kill bounty at a game minute (Settled endpoints; straight line between is Inferred)."""
    lo = rule("convar citadel_player_gold_reward_min")
    hi = rule("convar citadel_player_gold_reward_max")
    full = rule("convar citadel_player_gold_reward_time") / 60
    return lo + (hi - lo) * min(minute, full) / full


def trooper_bounty(minute: float) -> float:
    """Trooper bounty at a game minute: 100 + 2 per minute (Settled; per trooper or per wave is Open)."""
    return rule("convar citadel_trooper_gold_reward") + rule("convar citadel_trooper_gold_reward_bonus_per_minute") * minute


def neutral_souls_per_health(minute: float) -> float:
    """Souls per point of creep health relative to minute 0.

    Data: health grows 2.1%/min, souls 1.08%/min. Assumption: both grow in a straight line.
    """
    health_growth = rule("convar citadel_neutral_health_growth_pct_per_min") / 100
    creep = next(r for r in table("units") if r["key"] == "neutral_trooper_normal")
    soul_growth = float(creep["soul_reward_growth_pct_per_minute"]) / 100
    return (1 + soul_growth * minute) / (1 + health_growth * minute)


def respawn_time(minute: float) -> float:
    """Respawn seconds at a game minute, before penalties (Settled points; straight lines between Inferred)."""
    points = [(0, rule("convar citadel_player_spawn_time_min_ramp_1")),
              (5, rule("convar citadel_player_spawn_time_min_ramp_1")),
              (20, rule("convar citadel_player_spawn_time_min_ramp_2")),
              (30, rule("convar citadel_player_spawn_time_min_ramp_3")),
              (40, rule("convar citadel_player_spawn_time_max_ramp_3"))]
    cap = rule("convar citadel_player_spawn_time_max_respawn_time")
    for (m0, t0), (m1, t1) in zip(points, points[1:]):
        if minute <= m1:
            return t0 + (t1 - t0) * (minute - m0) / (m1 - m0)
    return min(points[-1][1], cap)


if __name__ == "__main__":
    # Print the worked examples used in formulas.md.
    print("Battle Vest + Bullet Resilience:", round(total_resist([0.18, 0.35]) * 100, 1), "%")
    print("Shredder + Crippling Headshot:", round(total_reduction([0.10, 0.16]) * 100, 1), "%")
    print("Final:", round(final_resist([0.18, 0.35], [0.10, 0.16]) * 100, 1), "%")
    for n in range(5):
        r = total_resist([0.18] * n)
        print(f"{n} x 18%: resist {r * 100:.1f}%, effective health x{effective_health(1, r):.2f}")
    for r in (0, 0.3, 0.5, 0.7):
        print(f"-10% shred vs {r * 100:.0f}%: +{shred_damage_gain(r, 0.10) * 100:.0f}%")
    for n in (1, 2, 3, 4, 6):
        s = hero_kill_split(200, n)
        print(f"hero kill 200, {n} players:", {k: round(v) for k, v in s.items()}, "trooper", trooper_share(n))
    for n in (1, 2, 3):
        print("Guardian", n, {k: round(v) for k, v in objective_split(rule("ObjectiveParams.Tier1GoldKill"), n).items()})
    for m in (0, 10, 20, 30, 40):
        print(m, "min: kill", round(hero_kill_bounty(m)), "trooper", trooper_bounty(m),
              "camp souls/health", round(neutral_souls_per_health(m), 2), "respawn", round(respawn_time(m)))
    for b, w, v, s in ((9, 4800, 0, 0), (9, 0, 4800, 0), (9, 0, 0, 4800), (29, 9600, 9600, 9600)):
        print("Abrams", b, "boons", (w, v, s), "gun", round(gun_dps("Abrams", b, investment_bonus("Weapon", w))),
              "hp", round(health_with_vitality("Abrams", b, v)), "sp",
              round(spirit_power_from_boons("Abrams", b) + investment_bonus("Spirit", s), 1))
