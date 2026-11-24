"""Parsing: KV3, text clean-up, and the three table builders."""
import pytest

from src import abilities, heroes, items, kv3, source, text


# --- KV3 -------------------------------------------------------------------

def test_kv3_parses_values_flags_and_comments():
    doc = kv3.loads('''<!-- kv3 encoding:text -->
    {
        // comment
        name = "Abrams \\"the\\" bull"
        m_flHealth = 800.0
        count = -3
        on = true
        nothing = null
        m_eType = EHeroDevState_Release
        res = resource_name:"scripts/x.vdata_inc"
        sub = subclass:
        {
            m_flStatScale = 0.6
        }
        list = [ 0, 800, 1600, "a", ]
        bits = "A | B"
    }''')
    assert doc["name"] == 'Abrams "the" bull'
    assert doc["m_flHealth"] == 800.0 and isinstance(doc["m_flHealth"], float)
    assert doc["count"] == -3 and doc["on"] is True and doc["nothing"] is None
    assert doc["m_eType"] == "EHeroDevState_Release"
    assert doc["res"] == "scripts/x.vdata_inc"
    assert doc["sub"] == {"m_flStatScale": 0.6}
    assert doc["list"] == [0, 800, 1600, "a"]
    assert doc["bits"] == "A | B"


@pytest.mark.parametrize("bad", ["{ a = ", "{ a 1 }", "{ a = [1, 2 }", "{ a = 1 } extra"])
def test_kv3_rejects_malformed_input(bad):
    with pytest.raises(kv3.KV3Error):
        kv3.loads(bad)


# --- text ------------------------------------------------------------------

@pytest.mark.parametrize("value,expected", [
    (800.0, (800, None)), (3.78, (3.78, None)), ("3.0m", (3, "m")), ("-12", (-12, None)),
    ("2m", (2, "m")), (4.5000045000045, (4.5, None)), (True, (None, None)), ("abc", (None, None)), (None, (None, None)),
])
def test_number_splits_value_and_unit(value, expected):
    assert text.number(value) == expected


def test_clean_strips_markup_and_resolves_templates():
    loc = {"InlineAttribute_SpiritDPS": "spirit damage over time"}
    raw = "Deal {g:citadel_inline_attribute:'SpiritDPS'}<br>for <span class=\"highlight\">{s:Dur}s</span> &amp; press {g:citadel_binding:'Ability1'}"
    assert text.clean(raw, loc, {"Dur": 4.0}) == "Deal spirit damage over time for 4s & press [Ability1]"
    assert text.clean("{s:Missing}", {}, {}) == "[Missing]"
    assert text.clean(None) == ""


def test_label_falls_back_to_humanised_key_and_marks_slows():
    loc = {"SlowPercent_label": "Move Speed", "X_label": "Named"}
    assert text.label(loc, "X") == "Named"
    assert text.label(loc, "BonusClipSize") == "Bonus Clip Size"
    assert text.label(loc, "SlowPercent") == "Move Speed Slow"
    assert text.label(loc, "Whatever", "#X") == "Named"


def test_version_parsing():
    version = source.parse_version("ClientVersion=6865\nVersionDate=Nov 23 2026\n")
    assert version["ClientVersion"] == "6865"
    assert source.build_date(version) == "2026-11-23"


# --- heroes ----------------------------------------------------------------

def test_hero_filter_keeps_live_heroes_only(primary):
    rows, excluded = heroes.build_heroes(primary)
    assert [r["name"] for r in rows] == ["LiveDev", "One"]  # InDevelopment alone does not exclude
    reasons = {key: reason for key, _, reason in excluded}
    assert "disabled" in reasons["hero_disabled"]
    assert "alternate form" in reasons["hero_one_transformed"]
    assert "no hero type" in reasons["hero_dummy"]


def test_hero_row_reads_the_right_fields(primary):
    row = heroes.hero_row("hero_one", primary["heroes"]["hero_one"], primary["loc"])
    assert row["base_health"] == 800 and isinstance(row["base_health"], int)
    assert row["health_per_boon"] == 49
    assert row["bullet_damage"] == 3.78 and row["pellets_per_shot"] == 9
    assert row["damage_per_shot"] == pytest.approx(34.02)
    assert row["clip_size"] == 9 and row["fire_rate"] == 1.5873 and row["weapon_dps_level_1"] == 54
    assert row["spirit_power_per_boon"] == 1.1
    assert row["stamina_recovery_seconds"] == 4.5
    assert row["role"] == "Charges in" and row["weapon_tags"] == "Close Range"
    assert row["base_bullet_resist"] is None  # blank, not an invented zero
    assert row["ability_1"] == "One 1" and row["ability_4"] == "One 4"
    assert set(row) == set(heroes.COLUMNS)


# --- abilities -------------------------------------------------------------

def test_split_value_handles_scalars_dicts_and_scale_lists():
    assert abilities.split_value(0.25) == (0.25, None, {})
    assert abilities.split_value({"Value": 22, "Scale": {"Value": 0.6, "Type": "spirit"}}) == (22, None, {"spirit": 0.6})
    value, unit, scales = abilities.split_value({"Value": "14m", "Scale": [{"Value": 0.14, "Type": "spirit"}, {"Value": 1, "Type": "range"}]})
    assert (value, unit, scales) == (14, "m", {"spirit": 0.14, "range": 1})
    assert abilities.split_value({"Class": "Modifier"}) == (None, None, {})
    assert abilities.split_value({"Value": 0, "Scale": {"Value": 0, "Type": "spirit"}})[2] == {}


def test_ability_rows_four_per_hero_plus_alternate_form(primary):
    rows, problems = abilities.build_abilities(primary)
    assert problems == []
    base = [r for r in rows if r["form"] is None]
    assert len(base) == 8 and {r["hero"] for r in base} == {"One", "LiveDev"}
    forms = [r for r in rows if r["form"]]
    # only the form's own abilities, not the one it shares with the base hero
    assert [(r["hero"], r["form"], r["slot"]) for r in forms if r["key"] == "ability_drain"] == []
    assert ("One", "One (Transformed)", 2) in [(r["hero"], r["form"], r["slot"]) for r in forms]


def test_ability_row_numbers_spirit_scaling_and_upgrades(primary):
    rows, _ = abilities.build_abilities(primary)
    row = next(r for r in rows if r["hero"] == "One" and r["slot"] == 1)
    assert row["cooldown"] == 42 and row["dps"] == 22 and row["radius"] == 8
    assert row["dps_spirit_scale"] == 0.6
    assert row["charge_cooldown"] is None  # -1 in the files means "not applicable"
    assert row["damage"] is None and row["damage_spirit_scale"] is None
    assert row["description"] == "Drain health, dealing spirit damage over time. Lasts a while."
    assert row["spirit_scaling"] == "Damage Per Second: 0.6; Reach: 0.14"
    assert row["other_properties"] == "Reach: 14m (+0.14 x spirit power)"  # zero-valued props are left out
    assert row["internal_properties"] == "TickRate=0.25"
    assert row["upgrade_1"] == "Cooldown -20s"
    assert row["upgrade_2"] == "Move Speed Slow +24%"
    assert row["upgrade_3"] == "Damage Per Second +22 and +0.12 x spirit power scaling; Radius +2m | +22 DPS & more"


def test_missing_ability_is_reported(primary):
    del primary["abilities"]["ability_1_2"]
    _, problems = abilities.build_abilities(primary)
    assert any("ability_1_2" in p for p in problems)


# --- items -----------------------------------------------------------------

def test_item_filter(primary):
    rows, excluded = items.build_items(primary)
    assert {r["name"] for r in rows} == {"Extra Health", "Fortitude", "Hollow Point"}
    reasons = {key: reason for key, _, reason in excluded}
    assert "no English name" in reasons["armor_upgrade_t1"]
    assert "Street Brawl" in reasons["upgrade_brawl"]
    assert "disabled" in reasons["upgrade_off"]
    assert "not a shop tier" in reasons["upgrade_t5"]


def test_item_category_names_come_from_localisation(primary):
    rows, _ = items.build_items(primary)
    assert {r["name"]: r["category"] for r in rows} == {
        "Extra Health": "Vitality", "Fortitude": "Vitality", "Hollow Point": "Weapon"}


def test_item_components_and_upgrades(primary):
    rows = {r["name"]: r for r in items.build_items(primary)[0]}
    assert rows["Fortitude"]["builds_from"] == "Extra Health"
    assert rows["Extra Health"]["upgrades_into"] == "Fortitude"
    assert rows["Extra Health"]["builds_from"] is None


def test_conditional_and_enemy_effects_stay_out_of_innate_stats(primary):
    row = next(r for r in items.build_items(primary)[0] if r["name"] == "Hollow Point")
    assert row["bonus_health"] == 125
    assert row["weapon_damage_pct"] is None  # +35% is conditional, not a flat stat
    assert row["bullet_resist_pct"] is None
    assert "Weapon Damage: 35%" in row["conditional_effects"]
    assert "Move Speed" not in (row["enemy_effects"] or "")
    assert row["enemy_effects"] == "[Passive] Bullet Resist: -10%"
    assert "3m" in row["conditional_effects"] and "16s cooldown" in row["conditional_effects"]
    assert row["activation"] == "Active" and row["cooldown"] == 16
    assert row["unlisted_properties"] == "LifeThreshold=65; TechResist=14; SlowPercent=30; EnhancedOnly=75"
    assert row["effect_text"] == "[Passive] Above 65% health, deal more damage."


@pytest.mark.parametrize("section,prop,expected", [
    ("Innate", {"Key": "BonusHealth", "Type": "health"}, "innate"),
    ("Innate", {"Key": "X", "UsageFlags": "ConditionallyApplied"}, "conditional"),
    ("Passive", {"Key": "BulletResist", "UsageFlags": "IntrinsicallyProvidedInAbility"}, "innate"),
    ("Passive", {"Key": "BonusFireRate", "Type": "fire_rate"}, "conditional"),
    ("Passive", {"Key": "FireRateSlow", "UsageFlags": "ConditionallyEnemyApplied"}, "enemy"),
    ("Active", {"Key": "SlowPercent", "Type": "slow"}, "enemy"),
    ("Active", {"Key": "AbilityDuration", "Type": "duration", "StatusEffect": "Stun"}, "enemy"),
    ("Passive", {"Key": "Damage", "Type": "tech_damage"}, "enemy"),
    (None, {"Key": "WeaponPowerPerStack", "Type": "bullet_damage"}, "conditional"),
    ("Innate", {"Key": "TechArmorDamageReduction", "Type": "tech_armor_down", "UsageFlags": "ConditionallyApplied"}, "enemy"),
])
def test_bucket_rules(section, prop, expected):
    assert items.bucket(section, prop) == expected


def test_raw_files_settle_stats_that_are_on_no_tooltip_section(primary, raw):
    row = next(r for r in items.build_items(primary, raw)[0] if r["name"] == "Hollow Point")
    assert row["spirit_resist_pct"] == 14                      # provided by the game, no usage flag: innate
    assert row["stats_not_on_tooltip"] == "Spirit Resist: 14%"
    assert "[Not on tooltip] Move Speed Slow: 30%" in row["enemy_effects"]   # flagged conditional, slows enemies
    assert row["unlisted_properties"] == "LifeThreshold=65; EnhancedOnly=75"  # not stats the game provides


def test_raw_files_supply_hero_tags_and_gun_tag(primary, raw):
    rows = {r["name"]: r for r in heroes.build_heroes(primary, raw)[0]}
    assert rows["One"]["hero_tags"] == "Tank; Brawler" and rows["One"]["gun_tag"] == "Shotgun"
    assert rows["LiveDev"]["hero_tags"] is None and rows["LiveDev"]["gun_tag"] is None
    assert heroes.build_heroes(primary)[0][0]["gun_tag"] is None  # without the raw files: blank
