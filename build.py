#!/usr/bin/env python3
"""Build the Deadlock reference sheet: pull source, parse, validate, write outputs.

    python build.py              # update the source, rebuild, validate, write output/
    python build.py --offline    # reuse the cached source, no network
"""
from __future__ import annotations

import argparse
import shutil
import sys
import tempfile
from pathlib import Path

from src import abilities, changelog, crosscheck, heroes, items, output, source, validate
from src.abilities import split_value

ROOT = Path(__file__).resolve().parent


def build_tables(primary: dict, raw: dict | None = None):
    hero_rows, hero_excluded = heroes.build_heroes(primary, raw)
    ability_rows, ability_problems = abilities.build_abilities(primary)
    item_rows, item_excluded = items.build_items(primary, raw)
    return hero_rows, ability_rows, item_rows, hero_excluded, item_excluded, ability_problems


def meta_rows(primary: dict, counts: dict, check, generated_at: str) -> list:
    version = primary["version"]
    compared = sum(check.compared.values()) if check and check.available else 0
    fields = [
        ("game_build", version.get("ClientVersion", "")),
        ("game_build_date", source.build_date(version)),
        ("source_repository", source.PRIMARY_URL),
        ("source_commit", primary["commit"]["hash"]),
        ("source_commit_date", primary["commit"]["date"]),
        ("crosscheck_source", source.RAW_BASE if check and check.available else "not run"),
        ("crosscheck_build", check.raw_build if check and check.available else ""),
        ("crosscheck_values_compared", compared),
        ("crosscheck_disagreements", len(check.disagreements) if check and check.available else ""),
        ("generated_at", generated_at),
        ("rows_heroes", counts["heroes"]),
        ("rows_abilities", counts["abilities"]),
        ("rows_alternate_form_abilities", counts["alternate_form_abilities"]),
        ("rows_items", counts["items"]),
        ("rows_items_weapon", counts["Weapon"]),
        ("rows_items_vitality", counts["Vitality"]),
        ("rows_items_spirit", counts["Spirit"]),
    ]
    return [{"field": name, "value": value} for name, value in fields]


def previous_counts(snapshot: dict) -> dict | None:
    meta = snapshot.get("meta") or {}
    names = {"heroes": "rows_heroes", "abilities": "rows_abilities", "items": "rows_items",
             "Weapon": "rows_items_weapon", "Vitality": "rows_items_vitality", "Spirit": "rows_items_spirit"}
    try:
        return {name: int(meta[field]) for name, field in names.items()}
    except (KeyError, ValueError):
        return None


def render_report(meta, counts, hero_excluded, item_excluded, findings, check) -> str:
    values = {row["field"]: row["value"] for row in meta}
    lines = [
        "# Build report", "",
        f"- Game build: **{values['game_build']}** ({values['game_build_date']})",
        f"- Source: {values['source_repository']} at `{values['source_commit'][:12]}` ({values['source_commit_date']})",
        f"- Generated: {values['generated_at']}",
        f"- Rows: {counts['heroes']} heroes, {counts['abilities']} hero abilities "
        f"(+{counts['alternate_form_abilities']} alternate-form abilities), {counts['items']} items "
        f"({counts['Weapon']} weapon, {counts['Vitality']} vitality, {counts['Spirit']} spirit)",
        "", "## Validation", "",
    ]
    shown = [f for f in findings if f.rule != "cross-check"]
    lines += [f"- {f.level} ({f.rule}): {f.message}" for f in shown] or ["- All rules passed with no warnings."]
    lines += ["", "## Cross-check against the raw game files", ""]
    if check is None or not check.available:
        lines.append(f"- NOT RUN: {check.note if check else 'skipped'}")
    else:
        lines.append(f"- Raw files at game build {check.raw_build}; {sum(check.compared.values())} values compared, "
                     f"{len(check.disagreements)} disagreement(s).")
        if check.note:
            lines.append(f"- Note: {check.note}")
        lines += ["", "| Compared | Values |", "|---|---|"]
        lines += [f"| {name} | {n} |" for name, n in check.compared.items()]
        if check.disagreements:
            lines += ["", "| Entity | Field | Sheet source | Raw game files |", "|---|---|---|---|"]
            lines += [f"| {e} | {f} | {s} | {r} |" for e, f, s, r in check.disagreements]
    for title, excluded in (("heroes", hero_excluded), ("items and item-like entries", item_excluded)):
        lines += ["", f"## Excluded {title}", ""]
        reasons = {}
        for key, name, reason in excluded:
            reasons.setdefault(reason, []).append(name or f"`{key}`")
        for reason, names in reasons.items():
            lines.append(f"- **{reason}** ({len(names)}): {', '.join(sorted(names, key=str.lower))}")
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--offline", action="store_true", help="do not touch the network; reuse the cached source")
    parser.add_argument("--no-crosscheck", action="store_true", help="skip the cross-check against the raw game files")
    parser.add_argument("--force", action="store_true", help="rewrite outputs even if nothing changed")
    parser.add_argument("--cache-dir", type=Path, default=ROOT / ".cache")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "output")
    args = parser.parse_args(argv)

    repo_dir, raw_dir, out_dir = args.cache_dir / "deadlock-data", args.cache_dir / "raw", args.output_dir
    try:
        if not args.offline:
            print(f"Updating source: {source.PRIMARY_URL}")
            source.update_primary(repo_dir)
        primary = source.load_primary(repo_dir)
    except source.SourceError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    version = primary["version"]
    print(f"Source is at game build {version.get('ClientVersion')} ({source.build_date(version)}), "
          f"commit {primary['commit']['hash'][:12]}")

    # The raw game files are the cross-check, and also supply the few fields the
    # primary source lacks (hero tags, gun tag, which off-tooltip item stats are real).
    raw, check = None, None
    if args.no_crosscheck:
        check = crosscheck.CrossCheck(available=False, note="skipped with --no-crosscheck")
    else:
        try:
            if not args.offline:
                print("Downloading raw game files")
                source.fetch_raw(raw_dir)
            raw = source.load_raw(raw_dir)
        except (source.SourceError, ValueError) as exc:
            check = crosscheck.CrossCheck(available=False, note=str(exc))

    hero_rows, ability_rows, item_rows, hero_excluded, item_excluded, problems = build_tables(primary, raw)
    counts = validate.table_counts(hero_rows, ability_rows, item_rows)
    if raw is not None:
        check = crosscheck.cross_check(primary, raw, hero_rows, ability_rows, item_rows)

    old = changelog.load_snapshot(out_dir)
    with_cooldown = {
        key for key, ability in primary["abilities"].items()
        if (split_value(ability.get("AbilityCooldown"))[0] or 0) > 0
    }
    findings = [validate.Finding(validate.ERROR, "parse", problem) for problem in problems]
    findings += validate.check_counts(counts, previous_counts(old))
    findings += validate.check_completeness(hero_rows, ability_rows, item_rows, with_cooldown)
    findings += validate.check_prices(item_rows)
    findings += validate.check_sanity(hero_rows, ability_rows, item_rows)
    findings += validate.check_crosscheck(check)

    print(f"\nRows: {counts['heroes']} heroes, {counts['abilities']} abilities "
          f"(+{counts['alternate_form_abilities']} alternate-form), {counts['items']} items "
          f"({counts['Weapon']} weapon / {counts['Vitality']} vitality / {counts['Spirit']} spirit)")
    for finding in findings:
        print(finding)
    if validate.has_errors(findings):
        print("\nBUILD FAILED: validation errors above. No outputs were written.", file=sys.stderr)
        return 1

    meta = meta_rows(primary, counts, check, source.now_iso())
    tables = {
        "heroes": (heroes.COLUMNS, hero_rows),
        "abilities": (abilities.COLUMNS, ability_rows),
        "items": (items.COLUMNS, item_rows),
        "meta": (["field", "value"], meta),
    }
    with tempfile.TemporaryDirectory() as tmp:
        output.write_outputs(Path(tmp), tables)
        new = changelog.load_snapshot(Path(tmp))
        initial = not any(old[t] for t in changelog.TABLE_KEYS)
        diff = changelog.diff_snapshots(old, new)
        data_changed = initial or changelog.has_changes(diff)
        volatile = {"generated_at"}
        meta_changed = {k: v for k, v in new["meta"].items() if k not in volatile} != \
                       {k: v for k, v in old["meta"].items() if k not in volatile}
        if not (data_changed or meta_changed or args.force):
            print("\nNo changes since the last build; outputs left untouched.")
            return 0
        out_dir.mkdir(parents=True, exist_ok=True)
        for path in Path(tmp).iterdir():
            shutil.copyfile(path, out_dir / path.name)
    (out_dir / "REPORT.md").write_text(
        render_report(meta, counts, hero_excluded, item_excluded, findings, check), encoding="utf-8")
    if data_changed:
        changelog.append_entry(out_dir / "CHANGELOG.md", changelog.render_entry(diff, new["meta"], old["meta"], initial))
        changes = sum(len(d["added"]) + len(d["removed"]) + len(d["changed"]) for d in diff.values())
        print(f"\nWrote {out_dir}/ ({'initial snapshot' if initial else f'{changes} change(s) logged in CHANGELOG.md'})")
    else:
        print(f"\nWrote {out_dir}/ (no data changes; source metadata updated)")
    warnings = sum(1 for f in findings if f.level == validate.WARNING)
    print(f"Validation passed with {warnings} warning(s). See {out_dir}/REPORT.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
