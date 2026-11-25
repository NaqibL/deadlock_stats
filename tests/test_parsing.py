"""Parsing: KV3, text clean-up, and the three table builders."""
import pytest

from src import abilities, heroes, items, kb, kv3, source, text, world


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
    assert row["sustained_dps_level_1"] == 32.069 and row["reloads_single_bullets"] is True
    assert row["dash_distance"] == 10 and row["crit_bonus_pct"] == 0
    assert row["spirit_scaling"] == "Clip Size: 0.5"  # how the hero's own stats scale with spirit
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


def test_camera_and_sound_values_are_not_gameplay(primary):
    primary["abilities"]["ability_drain"].update(CameraDistance=250, BeepSoundBuildupCount=4, PullRange=3)
    row = next(r for r in abilities.build_abilities(primary)[0] if r["hero"] == "One" and r["slot"] == 1)
    assert row["internal_properties"] == "TickRate=0.25; PullRange=3"
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


# --- game-wide tables ------------------------------------------------------

def test_investment_table(primary):
    rows = world.build_investment(primary)
    assert rows[0] == {"category": "Weapon", "souls_spent": 800, "bonus": 9, "bonus_stat": "Weapon Damage Increases"}
    assert [r["category"] for r in rows] == ["Weapon", "Weapon", "Vitality", "Spirit"]


def test_progression_table_keeps_running_totals(primary):
    rows = world.build_progression(primary)
    assert rows[0]["boon"] is None and rows[0]["ability_unlock"] == 1
    assert rows[2] == {"level": 2, "souls_required": 500, "boon": 1, "ability_unlock": 1, "ability_point": None,
                       "total_boons": 2, "total_ability_unlocks": 2, "total_ability_points": 1}


def test_units_table(primary):
    rows, missing = world.build_units(primary)
    units = {r["key"]: r for r in rows}
    guardian = units["npc_boss_tier1"]
    assert guardian["name"] == "Guardian" and guardian["health"] == 5500
    assert guardian["bullet_resist_pct"] == 10 and guardian["spirit_resist_pct"] == 0
    assert guardian["soul_reward"] == 1375 and guardian["dps_vs_players"] == 116
    creep = units["neutral_trooper_weak"]
    assert creep["soul_reward"] == 45 and creep["bullet_resist_pct"] == 50
    assert creep["first_spawn_seconds"] == 120 and creep["respawn_seconds"] == 85
    assert units["npc_super_neutral"]["health"] == 15600
    assert "npc_boss_tier2" in missing  # not in the fixture: reported, not fatal


def test_rules_table(primary):
    rules = {r["rule"]: r for r in world.build_rules(primary)}
    assert rules["Item price, tier 4"]["value"] == 6400
    assert rules["Guardian kill bounty (souls)"]["source_field"] == "ObjectiveParams.Tier1GoldKill"
    assert rules["Hero kill soul share, 2 player(s) sharing"]["value"] == 0.575
    assert rules["Rejuvenator drop count"]["value"] == 3 and rules["Rejuvenator revive delay (s)"]["value"] == 3
    assert not any("multiplier" in rule for rule in rules)  # retired by the 2025-07-29 rework


def test_world_tables_survive_a_missing_source_file(primary):
    for name in ("investment", "soul_unlocks", "npcs", "misc", "generic"):
        primary[name] = None
    assert world.build_investment(primary) == [] and world.build_progression(primary) == []
    assert world.build_units(primary)[0] == [] and world.build_rules(primary) == []


# --- knowledge base --------------------------------------------------------

NOTES_NEW = """- Rejuv buff duration reduced from 4 minutes to 3
- One: Drain cooldown reduced from 44s to 42s
- Extra Health: Bonus health increased from 200 to 210
- Dynamo: Rejuvenating Aurora cooldown reduced from 48s to 45s
"""
NOTES_OLD = """General Changes:
==
- Mid Boss respawn rescaled from 50% to 40/50/60% for the 1/2/3rd mid boss death

[ Heroes ]
* One: Now has a hat
"""


@pytest.fixture
def notes_repo(tmp_path):
    raw = tmp_path / "data" / "changelogs" / "raw"
    raw.mkdir(parents=True)
    (raw / "2026-06-30.txt").write_text(NOTES_NEW)
    (raw / "2024-10-10.txt").write_text(NOTES_OLD)
    (tmp_path / "data" / "changelogs" / "changelog_configs.json").write_text('{"2026-06-30": {"link": "https://example.test/1"}}')
    return tmp_path


def test_patch_notes_are_read_with_date_section_and_entity(primary, notes_repo):
    notes = kb.read_patch_notes(notes_repo, kb.entity_names(primary))
    assert len(notes) == 6  # headers are sections, not notes
    by_line = {n["line"]: n for n in notes}
    old = by_line["Mid Boss respawn rescaled from 50% to 40/50/60% for the 1/2/3rd mid boss death"]
    assert (old["date"], old["section"], old["entity"]) == ("2024-10-10", "General Changes", "")
    assert by_line["One: Now has a hat"]["section"] == "Heroes"
    assert by_line["One: Drain cooldown reduced from 44s to 42s"]["entity_kind"] == "hero"
    assert by_line["Extra Health: Bonus health increased from 200 to 210"]["entity"] == "Extra Health"
    assert by_line["Rejuv buff duration reduced from 4 minutes to 3"]["link"] == "https://example.test/1"


def test_topic_picks_matching_lines_newest_first(primary, notes_repo):
    notes = kb.read_patch_notes(notes_repo, kb.entity_names(primary))
    picked = kb.topic_notes(kb.TOPICS["mid-boss-and-rejuvenator"], notes)
    assert [n["date"] for n in picked] == ["2026-06-30", "2024-10-10"]  # the Dynamo ability line is excluded
    general = kb.topic_notes({"notes": "hat|44s", "general_only": True}, notes)
    assert general == []  # lines about one hero belong to the hero history


def test_flatten_keeps_gameplay_numbers_only():
    block = {"RejuvinatorBuffDuration": 180, "RejuvPickupSound": "x", "TrooperHealthMult": [1.7, 2.0, 2.3],
             "Unset": -1, "Zero": 0, "Flag": True, "Nested": {"RespawnDelay": 3.0, "ParticleEffect": 5}}
    assert dict(kb.flatten(block)) == {"RejuvinatorBuffDuration": 180, "TrooperHealthMult": "1.7 / 2 / 2.3",
                                       "Nested.RespawnDelay": 3}


def test_knowledge_base_is_written(primary, notes_repo, tmp_path):
    out = tmp_path / "knowledge"
    summary = kb.build_knowledge(primary, notes_repo, out)
    assert summary["notes"] == 6 and summary["hero_lines"] == 2 and summary["item_lines"] == 1
    page = (out / "mechanics" / "mid-boss-and-rejuvenator.md").read_text()
    assert "immediate respawns on their next deaths. (`guide_the_map_midboss_desc`)" in page  # markup stripped
    assert "| RejuvinatorDropCount | 3 |" in page and "Sound" not in page
    assert page.index("2026-06-30") < page.index("2024-10-10")
    assert "[forum post](https://example.test/1)" in page
    heroes_page = (out / "history" / "heroes.md").read_text()
    assert "## One" in heroes_page and "Now has a hat" in heroes_page
    assert "## Extra Health" in (out / "history" / "items.md").read_text()
    assert (out / "patch_notes.csv").read_text().count("\n") == 7
    assert "mechanics/mid-boss-and-rejuvenator.md" in (out / "README.md").read_text()
