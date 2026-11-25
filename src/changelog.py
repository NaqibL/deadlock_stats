"""Compare two output snapshots (directories of CSVs) and render a changelog entry."""
from __future__ import annotations

from pathlib import Path

from .output import read_csv

# table -> (columns that identify a row, function giving its display name)
TABLE_KEYS = {
    "heroes": (("key",), lambda r: r.get("name") or r.get("key")),
    "abilities": (("hero", "form", "key"), lambda r: " / ".join(x for x in (r.get("hero"), r.get("form"), r.get("name")) if x)),
    "items": (("key",), lambda r: r.get("name") or r.get("key")),
    "investment": (("category", "souls_spent"), lambda r: f"{r.get('category')} investment at {r.get('souls_spent')} souls"),
    "progression": (("level",), lambda r: f"Level {r.get('level')}"),
    "units": (("key",), lambda r: r.get("name") or r.get("key")),
    "rules": (("rule",), lambda r: r.get("rule")),
    "powerups": (("key", "stat"), lambda r: f"{r.get('name')} powerup, {r.get('stat')}"),
    "permanent_buffs": (("key", "stat"), lambda r: f"Permanent buff, {r.get('stat')}"),
}
CORE_TABLES = ("heroes", "abilities", "items")
HEADER = "# Changelog\n\nChanges to the generated sheet, newest first under each game build.\n"


def load_snapshot(directory: Path) -> dict:
    """Read the data tables of an output directory. Missing files give empty tables."""
    directory = Path(directory)
    snapshot = {}
    for table in TABLE_KEYS:
        path = directory / f"{table}.csv"
        snapshot[table] = read_csv(path) if path.exists() else []
    path = directory / "meta.csv"
    snapshot["meta"] = {row["field"]: row["value"] for row in read_csv(path)} if path.exists() else {}
    return snapshot


def diff_table(table: str, old_rows: list, new_rows: list) -> dict:
    key_columns, name_of = TABLE_KEYS[table]
    index = lambda rows: {tuple(row.get(c, "") for c in key_columns): row for row in rows}
    old, new = index(old_rows), index(new_rows)
    if not old_rows:  # a table the previous snapshot did not have: one line, not one per row
        return {"added": [], "removed": [], "changed": [], "new_columns": [], "new_table": len(new_rows)}
    old_columns = set(old_rows[0])
    new_columns = [c for c in (new_rows[0] if new_rows else {}) if c not in old_columns]
    changed = []
    for key in new:
        if key not in old:
            continue
        before, after = old[key], new[key]
        for column in after:
            if column in before and before[column] != after[column]:
                changed.append((name_of(after), column, before[column], after[column]))
    return {
        "new_columns": new_columns, "new_table": 0,
        "added": [name_of(new[key]) for key in new if key not in old],
        "removed": [name_of(old[key]) for key in old if key not in new],
        "changed": changed,
    }


def diff_snapshots(old: dict, new: dict) -> dict:
    return {table: diff_table(table, old.get(table, []), new.get(table, [])) for table in TABLE_KEYS}


def has_changes(diff: dict) -> bool:
    return any(d["added"] or d["removed"] or d["changed"] or d["new_columns"] or d["new_table"] for d in diff.values())


def _show(value: str) -> str:
    return "(blank)" if value == "" else str(value).replace("|", "\\|")


def render_entry(diff: dict, new_meta: dict, old_meta: dict | None = None, initial: bool = False) -> str:
    """One changelog section, grouped under the game build of the new snapshot."""
    build = new_meta.get("game_build", "unknown")
    date = new_meta.get("game_build_date", "")
    lines = [f"## Build {build} ({date})", ""]
    previous = (old_meta or {}).get("game_build")
    generated = new_meta.get("generated_at", "")
    if initial:
        counts = ", ".join(f"{new_meta.get('rows_' + t, '?')} {t}" for t in ("heroes", "abilities", "items"))
        lines += [f"Initial snapshot, generated {generated}: {counts}.", ""]
        return "\n".join(lines)
    came_from = f"previous snapshot was build {previous}" if previous else "previous build unknown"
    lines += [f"Generated {generated}; {came_from}.", ""]
    for table, table_diff in diff.items():
        if not any(table_diff.values()):
            continue
        lines += [f"### {table.capitalize()}", ""]
        if table_diff["new_table"]:
            lines.append(f"- New table in the sheet ({table_diff['new_table']} rows)")
        if table_diff["new_columns"]:
            lines.append(f"- New columns in the sheet: {', '.join(table_diff['new_columns'])}")
        lines += [f"- New: **{name}**" for name in table_diff["added"]]
        lines += [f"- Removed: **{name}**" for name in table_diff["removed"]]
        for name, column, before, after in table_diff["changed"]:
            lines.append(f"- **{name}** {column}: {_show(before)} -> {_show(after)}")
        lines.append("")
    return "\n".join(lines)


def append_entry(path: Path, entry: str) -> None:
    """Insert ``entry`` at the top of the changelog, below the file header."""
    path = Path(path)
    existing = path.read_text(encoding="utf-8") if path.exists() else HEADER
    if not existing.startswith("# "):
        existing = HEADER + "\n" + existing
    head, _, rest = existing.partition("\n## ")
    body = head.rstrip("\n") + "\n\n" + entry.rstrip("\n") + "\n"
    if rest:
        body += "\n## " + rest
    path.write_text(body, encoding="utf-8")
