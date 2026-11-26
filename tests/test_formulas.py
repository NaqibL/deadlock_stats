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


def test_sharing_totals():
    assert f.trooper_share(2)["team_total"] == pytest.approx(1.08)
    split = f.hero_kill_split(200, 2)
    assert split["team_total"] == pytest.approx(230)
    assert split["killer"] == pytest.approx(2.2 * split["assister"])
    guardian = f.objective_split(1375, 1)
    assert guardian["each_nearby"] + 5 * guardian["each_other"] == pytest.approx(1375)
