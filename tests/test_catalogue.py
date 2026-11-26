"""Spot checks of the keyword catalogues and hero cards against rows read by hand from the sheet."""

import importlib.util
import sys
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parent.parent / "analysis"
sys.path.insert(0, str(ANALYSIS))


def _load(name):
    spec = importlib.util.spec_from_file_location(name, ANALYSIS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


cat = _load("catalogue")
DMG_A, CC_A, DEF_A = cat.ability_rows(cat.read("abilities"))
DMG_I, CC_I, DEF_I = cat.item_rows(cat.read("items"))
CC = CC_A + CC_I


def find(rows, **kw):
    return [r for r in rows if all(r.get(k) == v for k, v in kw.items())]


def test_field_control_is_read():
    assert find(CC, owner="Haze", name="Sleep Dagger", cc_type="sleep", tier=0)[0]["value"] == 2.75
    assert find(CC, owner="Graves", name="Grasping Hands", cc_type="immobilize", tier=0)[0]["value"] == 1
    assert find(CC, name="Silence Wave", cc_type="silence")[0]["value"] == 3
    assert find(CC, name="Silencer", cc_type="silence")[0]["value"] == 2.5


def test_text_and_description_control():
    assert find(CC, name="Cursed Relic", cc_type="curse")
    assert find(CC, owner="Mo & Krill", name="Combo", cc_type="stun")[0]["value"] == 2.4
    assert not find(CC, name="Air Drop", cc_type="lift")  # lifts an ally, not control
    assert not find(CC, name="Unstoppable")  # protection, not control


def test_damage_kinds():
    tesla = find(DMG_I, name="Tesla Bullets")[0]
    assert tesla["other_scaling"] == "on-hit chance" and tesla["spirit_coef"] == 0.19
    assert find(DMG_I, name="Toxic Bullets")[0]["kind"] == "target health %"
    chimera = find(DMG_A, owner="Deadman Danny", name="Chimera Mk1", tier=0, property="Explosion Damage")
    assert chimera and chimera[0]["damage_type"] == "weapon"
    assert find(DMG_A, owner="Bebop", name="Grapple Arm")[0]["damage_type"] == "melee"
    assert not [r for r in DMG_A if r["property"] in ("Damage Cap", "Uninterruptible By Damage")]


def test_summon_health_is_not_healing():
    assert not [r for r in DEF_A if r["name"] == "Borrowed Decree" and r["effect"] == "heal" and not r["tier"]]


def test_spirit_gain_is_a_percentage():
    hands = find(DMG_A, owner="Graves", name="Grasping Hands", tier=0, property="Damage")[0]
    assert round(hands["gain_per_100_sp"]) == 178
