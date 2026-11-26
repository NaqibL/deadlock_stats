"""Checks for analysis/formulas.py against worked examples and the committed sheet."""

import importlib.util
from pathlib import Path

import pytest

_spec = importlib.util.spec_from_file_location(
    "formulas", Path(__file__).resolve().parent.parent / "analysis" / "formulas.py")
f = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(f)


def test_resist_stacking_matches_wiki_examples():
    assert f.total_resist([0.40, 0.20]) == pytest.approx(0.52)
    assert f.total_reduction([0.25, 0.20]) == pytest.approx(0.40)
    assert f.final_resist([0.40, 0.20], [0.25, 0.20]) == pytest.approx(0.12)


def test_negative_resist_amplifies():
    assert f.damage_taken(f.final_resist([0.10], [0.40])) == pytest.approx(1.30)


def test_each_resist_item_multiplies_effective_health_equally():
    one = f.effective_health(1000, f.total_resist([0.18]))
    two = f.effective_health(1000, f.total_resist([0.18, 0.18]))
    assert two / one == pytest.approx(one / 1000)


def test_shred_gains_more_against_high_resist():
    assert f.shred_damage_gain(0.0, 0.10) == pytest.approx(0.10)
    assert f.shred_damage_gain(0.5, 0.10) == pytest.approx(0.20)


def test_progression_and_hero_growth():
    assert f.level_at(5000)["total_boons"] == 9
    assert f.level_at(30000)["total_ability_points"] == 26
    assert f.hero_stat("Abrams", "base_health", 29) == pytest.approx(2221)


def test_investment_lookup():
    assert f.investment_bonus("Weapon", 4799) == 18
    assert f.investment_bonus("Weapon", 4800) == 46
    assert f.investment_bonus("Spirit", 0) == 0


def test_procs_scale_with_shots_and_respect_cooldown():
    assert f.shots_per_second("Graves") == pytest.approx(9.8039)
    assert f.shots_per_second("McGinnis") == pytest.approx(11.9048)
    assert f.shots_per_second("McGinnis", spun_up=False) < 11.9048
    assert f.procs_per_second(10, 0.15) == pytest.approx(1.5)
    assert f.procs_per_second(40, 0.5, cooldown=0.2) == pytest.approx(5)
    assert f.periodic_dps(56, 1.4) == pytest.approx(40)


def test_sharing_totals():
    assert f.trooper_share(2)["team_total"] == pytest.approx(1.08)
    split = f.hero_kill_split(200, 2)
    assert split["team_total"] == pytest.approx(230)
    assert split["killer"] == pytest.approx(2.2 * split["assister"])
    guardian = f.objective_split(1375, 1)
    assert guardian["each_nearby"] + 5 * guardian["each_other"] == pytest.approx(1375)


def test_damage_mix_and_effective_health():
    assert f.damage_taken_vs_mix({"bullet": 1.0}, bullet=0.3) == pytest.approx(0.7)
    assert f.damage_taken_vs_mix({"spirit": 1.0}, bullet=0.9) == pytest.approx(1.0)
    assert f.damage_taken_vs_mix({"melee": 1.0}, bullet=0.2, melee=0.5) == pytest.approx(0.4)
    assert f.effective_health_vs_mix(1000, {"bullet": 0.5, "spirit": 0.5}, bullet=0.5) == pytest.approx(1000 / 0.75)


def test_control_diminishing_and_chain():
    assert f.control_duration(1.0, recent_controls=5) == pytest.approx(0.79)
    assert f.control_duration(2.0, debuff_resist=0.25, recent_controls=1) == pytest.approx(2 * 0.75 * 0.93)
    assert f.chain_control([1.1, 2.4]) == pytest.approx(1.1 + 2.4 * 0.93)


def test_kill_paths():
    assert f.time_to_kill(1000, 1200, 100) == 0
    assert f.time_to_kill(1000, 200, 100) == pytest.approx(8)
    assert f.net_dps(100, 50, anti_heal=0.4) == pytest.approx(70)
    assert f.execute_effective_health(1000, 0.18) == pytest.approx(820)
    r = f.duel({"ehp": 2000, "burst": 600, "dps": 150, "control": 1.5}, {"ehp": 2400, "burst": 300, "dps": 180})
    assert r["a_kills_in"] == pytest.approx(12) and r["b_kills_in"] == pytest.approx(1700 / 180 + 1.5)
    assert r["winner"] == "b"
