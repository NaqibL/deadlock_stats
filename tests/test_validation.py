"""The validation rules themselves, the cross-check, and the changelog."""
import copy

from src import changelog, crosscheck, output, validate
from src.validate import ERROR, WARNING


def levels(findings, rule=None):
    return [f.level for f in findings if rule is None or f.rule == rule]


BASE = dict(validate.BASELINE, alternate_form_abilities=3)


# --- counts ----------------------------------------------------------------

def test_counts_at_baseline_pass():
    assert validate.check_counts(BASE) == []


def test_count_growth_is_reported_not_fatal():
    counts = dict(BASE, heroes=45, abilities=180)
    findings = validate.check_counts(counts)
    assert levels(findings) == [WARNING, WARNING]
    assert "heroes: 45 rows, was 44" in findings[0].message


def test_large_drop_is_an_error():
    counts = dict(BASE, items=120, Weapon=17)
    findings = validate.check_counts(counts)
    assert ERROR in levels(findings) and any("large drop" in f.message for f in findings)


def test_small_drop_is_a_warning():
    assert levels(validate.check_counts(dict(BASE, items=155, Spirit=48))) == [WARNING, WARNING]


def test_counts_compare_with_previous_output_when_given():
    previous = dict(validate.BASELINE, heroes=45, abilities=180)
    assert validate.check_counts(dict(BASE, heroes=45, abilities=180), previous) == []


def test_empty_table_and_wrong_abilities_per_hero_are_errors():
    assert ERROR in levels(validate.check_counts(dict(BASE, heroes=0)))
    findings = validate.check_counts(dict(BASE, abilities=175))
    assert any("four per hero" in f.message and f.level == ERROR for f in findings)


def test_table_counts(tables):
    counts = validate.table_counts(*tables)
    assert counts["heroes"] == 2 and counts["abilities"] == 8 and counts["alternate_form_abilities"] == 3
    assert counts["items"] == 3 and counts["Vitality"] == 2 and counts["Weapon"] == 1 and counts["Spirit"] == 0


# --- completeness ----------------------------------------------------------

def test_complete_tables_pass(tables):
    assert validate.check_completeness(*tables, abilities_with_cooldown={"ability_drain"}) == []


def test_blank_key_columns_are_errors(tables):
    hero_rows, ability_rows, item_rows = tables
    hero_rows[0]["base_health"] = None
    hero_rows[1]["bullet_damage"] = ""
    item_rows[0]["tier"] = None
    item_rows[1]["cost"] = None
    findings = validate.check_completeness(hero_rows, ability_rows, item_rows)
    assert levels(findings) == [ERROR] * 4
    assert "has no base_health" in findings[0].message


def test_missing_cooldown_is_an_error_only_when_the_source_has_one(tables):
    hero_rows, ability_rows, item_rows = tables
    for row in ability_rows:
        row["cooldown"] = None
    assert validate.check_completeness(hero_rows, ability_rows, item_rows) == []  # passives may be blank
    findings = validate.check_completeness(hero_rows, ability_rows, item_rows, {"ability_drain"})
    assert levels(findings) == [ERROR, ERROR] and "cooldown in the source" in findings[0].message


def test_duplicate_rows_are_errors(tables):
    hero_rows, ability_rows, item_rows = tables
    findings = validate.check_completeness(hero_rows + [hero_rows[0]], ability_rows, item_rows)
    assert any("duplicate" in f.message for f in findings)


# --- prices ----------------------------------------------------------------

def test_prices(tables):
    item_rows = tables[2]
    assert validate.check_prices(item_rows) == []
    item_rows[0]["cost"] = 900
    findings = validate.check_prices(item_rows)
    assert levels(findings) == [WARNING] and "900 souls" in findings[0].message
    item_rows[0]["tier"] = 5
    assert levels(validate.check_prices(item_rows)) == [ERROR]


# --- sanity ----------------------------------------------------------------

REFERENCE = [
    ("heroes", "One", "base_health", 800, None),
    ("items", "Extra Health", "bonus_health", 210, None),
    ("abilities", "Drain", "dps_spirit_scale", 0.6, ("hero", "One")),
    ("items", "Hollow Point", "conditional_effects", "contains:Weapon Damage: 35%", None),
]


def test_sanity_passes_and_flags_differences(tables):
    assert validate.check_sanity(*tables, reference=REFERENCE) == []
    tables[0][1]["base_health"] = 790
    findings = validate.check_sanity(*tables, reference=REFERENCE)
    assert levels(findings) == [WARNING] and "patch notes" in findings[0].message


def test_sanity_reports_missing_reference_entity(tables):
    findings = validate.check_sanity(*tables, reference=[("items", "Nope", "tier", 1, None)])
    assert levels(findings) == [WARNING] and "not found" in findings[0].message


def test_default_reference_covers_every_value_in_the_brief():
    names = {(table, name, column) for table, name, column, _, _ in validate.SANITY}
    for expected in [("heroes", "Abrams", "base_health"), ("heroes", "Haze", "clip_size"),
                     ("items", "Extra Health", "bonus_health"), ("items", "Leech", "bullet_lifesteal_pct"),
                     ("abilities", "Siphon Life", "dps_spirit_scale"), ("abilities", "Kinetic Pulse", "damage")]:
        assert expected in names


# --- cross-check -----------------------------------------------------------

def run_check(primary, raw, tables):
    return crosscheck.cross_check(primary, raw, *tables)


def test_cross_check_agrees_including_unit_conversion(primary, raw, tables):
    result = run_check(primary, raw, tables)
    assert result.disagreements == []  # Reach is 14 m in the sheet, 551.18 inches in the raw files
    assert result.compared["hero base_health"] == 2 and result.compared["item cost"] == 3
    assert result.compared["ability properties (spirit scaling)"] == 4  # DPS and Reach, on both heroes
    assert validate.check_crosscheck(result) == []


def test_cross_check_reports_value_disagreements(primary, raw, tables):
    raw["heroes"]["hero_one"]["m_mapStartingStats"]["EMaxHealth"] = 820.0
    raw["abilities"]["ability_drain"]["m_mapAbilityProperties"]["DPS"]["m_subclassScaleFunction"]["m_flStatScale"] = 0.7
    raw["abilities"]["upgrade_health"]["m_iItemTier"] = "EModTier_2"
    raw["abilities"]["upgrade_hollow"]["m_mapAbilityProperties"]["BaseAttackDamagePercent"]["m_strValue"] = "30"
    found = {(e, f): (s, r) for e, f, s, r in run_check(primary, raw, tables).disagreements}
    assert found[("One", "base_health")] == (800, 820)
    assert found[("One / Drain", "DPS spirit scaling")] == (0.6, 0.7)
    assert found[("Extra Health", "tier")] == (1, 2)
    assert found[("Extra Health", "cost")] == (800, 1600)
    assert found[("Hollow Point", "BaseAttackDamagePercent")] == (35, 30)


def test_cross_check_reports_roster_differences(primary, raw, tables):
    raw["heroes"]["hero_dummy"]["m_eHeroDevelopmentState"] = "EHeroDevState_Release"
    raw["heroes"]["hero_live_dev"]["m_bDisabled"] = True
    found = {(e, s) for e, f, s, r in run_check(primary, raw, tables).disagreements if f == "playable"}
    assert found == {("hero_dummy", "not in sheet"), ("hero_live_dev", "in sheet")}


def test_cross_check_findings_are_warnings_and_note_build_mismatch(primary, raw, tables):
    raw["version"]["ClientVersion"] = "6870"
    raw["heroes"]["hero_one"]["m_mapStartingStats"]["EMaxHealth"] = 820.0
    findings = validate.check_crosscheck(run_check(primary, raw, tables))
    assert levels(findings) == [WARNING, WARNING]
    assert "different game builds" in findings[0].message
    assert not validate.has_errors(findings)


def test_scale_function_without_a_named_stat_counts_as_spirit():
    def prop(scale):
        return {"m_mapAbilityProperties": {"Damage": {"m_strValue": "60", "m_subclassScaleFunction": scale}}}
    assert crosscheck.raw_property(prop({"m_flStatScale": 1.1}), "Damage") == (60, 1.1)
    assert crosscheck.raw_property(prop({"_class": "scale_function_tech_damage", "m_eSpecificStatScaleType": "EStatsCount", "m_flStatScale": 1.0}), "Damage") == (60, 1)
    assert crosscheck.raw_property(prop({"_class": "scale_function_single_stat", "m_eSpecificStatScaleType": "ELevelUpBoons", "m_flStatScale": 2}), "Damage") == (60, None)
    assert crosscheck.raw_property(prop({"_class": "scale_function_tech_duration", "m_flStatScale": 1}), "Damage") == (60, None)


def test_skipped_cross_check_is_reported_loudly():
    findings = validate.check_crosscheck(crosscheck.CrossCheck(available=False, note="could not download"))
    assert levels(findings) == [WARNING] and findings[0].message.startswith("NOT RUN")


# --- changelog -------------------------------------------------------------

def snapshot(tmp_path, name, tables, build="6865"):
    from src import abilities, heroes, items
    hero_rows, ability_rows, item_rows = tables
    meta = [{"field": "game_build", "value": build}, {"field": "game_build_date", "value": "2026-11-23"},
            {"field": "generated_at", "value": "now"}, {"field": "rows_heroes", "value": len(hero_rows)},
            {"field": "rows_abilities", "value": 8}, {"field": "rows_items", "value": len(item_rows)}]
    out = tmp_path / name
    output.write_outputs(out, {"heroes": (heroes.COLUMNS, hero_rows), "abilities": (abilities.COLUMNS, ability_rows),
                               "items": (items.COLUMNS, item_rows), "meta": (["field", "value"], meta)})
    return changelog.load_snapshot(out)


def test_outputs_are_written_with_numbers_as_numbers(tmp_path, tables):
    from openpyxl import load_workbook
    snapshot(tmp_path, "a", tables)
    assert {p.name for p in (tmp_path / "a").iterdir()} == {"heroes.csv", "abilities.csv", "items.csv", "meta.csv", "deadlock.xlsx"}
    workbook = load_workbook(tmp_path / "a" / "deadlock.xlsx")
    assert workbook.sheetnames == ["Heroes", "Abilities", "Items", "Meta"]
    header = [c.value for c in workbook["Heroes"][1]]
    row = dict(zip(header, [c.value for c in workbook["Heroes"][2]]))
    assert row["base_health"] == 800 and isinstance(row["base_health"], int)
    assert row["base_bullet_resist"] is None
    csv_row = output.read_csv(tmp_path / "a" / "heroes.csv")[0]
    assert csv_row["base_health"] == "800" and csv_row["base_bullet_resist"] == ""


def test_diff_finds_changed_added_and_removed(tmp_path, tables):
    old = snapshot(tmp_path, "old", tables)
    new_tables = copy.deepcopy(tables)
    new_tables[0][1]["base_health"] = 820          # One
    new_tables[2][0]["bonus_health"] = 150         # Hollow Point (Weapon sorts first)
    removed = new_tables[2].pop()                  # an item disappears
    new_tables[0].append(dict(new_tables[0][0], key="hero_new", name="Newcomer"))
    new = snapshot(tmp_path, "new", new_tables, build="6870")
    diff = changelog.diff_snapshots(old, new)
    assert diff["heroes"]["changed"] == [("One", "base_health", "800", "820")]
    assert diff["heroes"]["added"] == ["Newcomer"]
    assert diff["items"]["removed"] == [removed["name"]]
    assert ("Hollow Point", "bonus_health", "125", "150") in diff["items"]["changed"]
    assert changelog.has_changes(diff)
    entry = changelog.render_entry(diff, new["meta"], old["meta"])
    assert entry.startswith("## Build 6870 (2026-11-23)")
    assert "previous snapshot was build 6865" in entry
    assert "- **One** base_health: 800 -> 820" in entry
    assert "- New: **Newcomer**" in entry and f"- Removed: **{removed['name']}**" in entry


def test_identical_snapshots_have_no_changes(tmp_path, tables):
    old, new = snapshot(tmp_path, "old", tables), snapshot(tmp_path, "new", copy.deepcopy(tables))
    assert not changelog.has_changes(changelog.diff_snapshots(old, new))


def test_changelog_entries_are_added_newest_first(tmp_path):
    path = tmp_path / "CHANGELOG.md"
    changelog.append_entry(path, "## Build 1 (a)\n\nfirst\n")
    changelog.append_entry(path, "## Build 2 (b)\n\nsecond\n")
    content = path.read_text()
    assert content.startswith("# Changelog")
    assert content.index("## Build 2") < content.index("## Build 1")
    assert content.count("## Build") == 2
