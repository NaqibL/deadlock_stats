"""Validation rules run on every build.

Each rule returns a list of :class:`Finding`. Any ``ERROR`` stops the build
before outputs are written; ``WARNING`` findings are reported and recorded.
"""
from __future__ import annotations

from dataclasses import dataclass

ERROR, WARNING, INFO = "ERROR", "WARNING", "INFO"

# Counts at game build 6864 (18 November 2026).
BASELINE = {"heroes": 44, "abilities": 176, "items": 156, "Weapon": 53, "Vitality": 54, "Spirit": 49}
BASELINE_BUILD = "6864"
LARGE_DROP = 0.10  # a table shrinking by more than this is treated as an error
TIER_COST = {1: 800, 2: 1600, 3: 3200, 4: 6400}

# Reference values used to check that the parser reads the right fields.
# They are a parser check, not ground truth: balance patches change them.
# (table, name, column, expected, optional extra match on another column)
SANITY = [
    ("heroes", "Abrams", "base_health", 800, None),
    ("heroes", "Abrams", "health_per_boon", 49, None),
    ("heroes", "Abrams", "bullet_damage", 3.78, None),
    ("heroes", "Abrams", "pellets_per_shot", 9, None),
    ("heroes", "Abrams", "clip_size", 9, None),
    ("heroes", "Haze", "base_health", 730, None),
    ("heroes", "Haze", "clip_size", 25, None),
    ("items", "Extra Health", "bonus_health", 210, None),
    ("items", "Extra Health", "tier", 1, None),
    ("items", "Boundless Spirit", "spirit_power", 30, None),
    ("items", "Boundless Spirit", "other_innate_stats", "contains:Spirit Power: 15%", None),
    ("items", "Boundless Spirit", "tier", 4, None),
    # The brief gave 28% for Leech at build 6864. Both the primary source and the
    # raw game files have carried 30% since build 6826 (30 Oct 2026), so 30 is used.
    ("items", "Leech", "bullet_lifesteal_pct", 30, None),
    ("items", "Leech", "spirit_lifesteal_pct", 30, None),
    ("abilities", "Siphon Life", "cooldown", 42, ("hero", "Abrams")),
    ("abilities", "Siphon Life", "dps", 22, ("hero", "Abrams")),
    ("abilities", "Siphon Life", "dps_spirit_scale", 0.6, ("hero", "Abrams")),
    ("abilities", "Kinetic Pulse", "cooldown", 26, ("hero", "Dynamo")),
    ("abilities", "Kinetic Pulse", "damage", 115, ("hero", "Dynamo")),
    ("abilities", "Kinetic Pulse", "damage_spirit_scale", 1.55, ("hero", "Dynamo")),
]


@dataclass(frozen=True)
class Finding:
    level: str
    rule: str
    message: str

    def __str__(self):
        return f"{self.level:7} [{self.rule}] {self.message}"


def _blank(value) -> bool:
    return value is None or value == ""


def table_counts(hero_rows, ability_rows, item_rows) -> dict:
    counts = {
        "heroes": len(hero_rows),
        "abilities": sum(1 for row in ability_rows if _blank(row.get("form"))),
        "alternate_form_abilities": sum(1 for row in ability_rows if not _blank(row.get("form"))),
        "items": len(item_rows),
    }
    for category in ("Weapon", "Vitality", "Spirit"):
        counts[category] = sum(1 for row in item_rows if row.get("category") == category)
    return counts


def check_counts(counts: dict, previous: dict | None = None) -> list:
    """Report count changes; a large drop is an error.

    ``previous`` is the counts of the last written output if there is one,
    otherwise the build 6864 baseline is the reference.
    """
    reference = previous or BASELINE
    against = "the previous output" if previous else f"build {BASELINE_BUILD}"
    findings = []
    for name, expected in BASELINE.items():
        actual = counts.get(name, 0)
        if actual == 0:
            findings.append(Finding(ERROR, "counts", f"{name}: no rows at all"))
            continue
        ref = reference.get(name, expected)
        if ref and actual < ref * (1 - LARGE_DROP):
            findings.append(Finding(ERROR, "counts", f"{name}: {actual} rows, down from {ref} in {against} (large drop)"))
        elif actual != ref:
            findings.append(Finding(WARNING, "counts", f"{name}: {actual} rows, was {ref} in {against}"))
    for row_count, per_hero in ((counts.get("abilities", 0), counts.get("heroes", 0) * 4),):
        if row_count != per_hero:
            findings.append(Finding(ERROR, "counts", f"abilities: {row_count} rows, expected four per hero ({per_hero})"))
    return findings


def check_completeness(hero_rows, ability_rows, item_rows, abilities_with_cooldown=()) -> list:
    """No blanks in key columns, and no duplicate entities."""
    findings = []

    def require(table, rows, columns, name_of):
        for row in rows:
            for column in columns:
                if _blank(row.get(column)):
                    findings.append(Finding(ERROR, "completeness", f"{table}: {name_of(row)} has no {column}"))

    require("heroes", hero_rows, ("name", "base_health", "bullet_damage"), lambda r: r.get("name") or r.get("key"))
    require("abilities", ability_rows, ("hero", "slot", "name"), lambda r: f"{r.get('hero')} / {r.get('name') or r.get('key')}")
    require("items", item_rows, ("name", "category", "tier", "cost"), lambda r: r.get("name") or r.get("key"))
    need_cooldown = set(abilities_with_cooldown)
    for row in ability_rows:
        if row.get("key") in need_cooldown and _blank(row.get("cooldown")):
            findings.append(Finding(ERROR, "completeness", f"abilities: {row.get('hero')} / {row.get('name')} has a cooldown in the source but none in the sheet"))
    for table, rows, key in (
        ("heroes", hero_rows, lambda r: r.get("key")),
        ("abilities", ability_rows, lambda r: (r.get("hero"), r.get("form"), r.get("slot"))),
        ("items", item_rows, lambda r: r.get("key")),
    ):
        seen = set()
        for row in rows:
            if key(row) in seen:
                findings.append(Finding(ERROR, "completeness", f"{table}: duplicate row for {key(row)}"))
            seen.add(key(row))
    return findings


def check_prices(item_rows) -> list:
    findings = []
    for row in item_rows:
        tier, cost = row.get("tier"), row.get("cost")
        if _blank(tier) or _blank(cost):
            continue  # reported by the completeness rule
        if tier not in TIER_COST:
            findings.append(Finding(ERROR, "prices", f"{row.get('name')}: tier {tier} is not a shop tier"))
        elif cost != TIER_COST[tier]:
            findings.append(Finding(WARNING, "prices", f"{row.get('name')}: costs {cost} souls, tier {tier} items normally cost {TIER_COST[tier]}"))
    return findings


def check_sanity(hero_rows, ability_rows, item_rows, reference=SANITY) -> list:
    """Compare known reference values with the sheet. A difference is a warning."""
    tables = {"heroes": hero_rows, "abilities": ability_rows, "items": item_rows}
    findings = []
    for table, name, column, expected, extra in reference:
        matches = [
            row for row in tables[table]
            if row.get("name") == name and (extra is None or row.get(extra[0]) == extra[1])
        ]
        where = f"{name} ({extra[1]})" if extra else name
        if not matches:
            findings.append(Finding(WARNING, "sanity", f"{table}: reference entity {where} not found (renamed or removed?)"))
            continue
        actual = matches[0].get(column)
        if isinstance(expected, str) and expected.startswith("contains:"):
            ok = isinstance(actual, str) and expected[len("contains:"):] in actual
        elif isinstance(expected, (int, float)) and isinstance(actual, (int, float)):
            ok = abs(actual - expected) < 1e-6
        else:
            ok = actual == expected
        if not ok:
            findings.append(Finding(WARNING, "sanity", f"{table}: {where} {column} is {actual!r}, reference value is {expected!r}; check the patch notes before assuming a parser bug"))
    return findings


def check_crosscheck(result) -> list:
    """Turn a cross-check result into findings. Disagreements are reported, never resolved."""
    if result is None or not result.available:
        note = result.note if result is not None else "cross-check was skipped"
        return [Finding(WARNING, "cross-check", f"NOT RUN: {note}. Columns that come from the raw game files "
                        "(hero_tags, gun_tag, off-tooltip item stats) are incomplete in this build")]
    findings = []
    if result.note:
        findings.append(Finding(WARNING, "cross-check", result.note))
    for entity, fieldname, sheet, raw in result.disagreements:
        findings.append(Finding(WARNING, "cross-check", f"{entity}: {fieldname} is {sheet!r} in the sheet source, {raw!r} in the raw game files"))
    return findings


def has_errors(findings) -> bool:
    return any(f.level == ERROR for f in findings)
