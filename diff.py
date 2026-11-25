#!/usr/bin/env python3
"""Compare two output snapshots and write a changelog of what changed.

    python diff.py                      # last committed output/ (git HEAD) vs output/ on disk
    python diff.py OLD_DIR NEW_DIR      # any two directories holding the CSVs
    python diff.py --append             # also add the entry to output/CHANGELOG.md

build.py already appends to the changelog on every run that changes data;
this script is for comparing arbitrary snapshots, for example two git commits.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

from src import changelog

ROOT = Path(__file__).resolve().parent


def committed_snapshot(rev: str, target: Path) -> None:
    """Extract ``output/*.csv`` as of git revision ``rev`` into ``target``."""
    for name in (*changelog.TABLE_KEYS, "meta"):
        result = subprocess.run(["git", "show", f"{rev}:output/{name}.csv"], cwd=ROOT, capture_output=True)
        if result.returncode == 0:
            (target / f"{name}.csv").write_bytes(result.stdout)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("old", nargs="?", type=Path, help="older snapshot directory (default: output/ at --rev)")
    parser.add_argument("new", nargs="?", type=Path, default=ROOT / "output", help="newer snapshot directory")
    parser.add_argument("--rev", default="HEAD", help="git revision to use as the old snapshot (default HEAD)")
    parser.add_argument("--append", action="store_true", help="append the entry to the changelog")
    parser.add_argument("--changelog", type=Path, default=ROOT / "output" / "CHANGELOG.md")
    args = parser.parse_args(argv)

    with tempfile.TemporaryDirectory() as tmp:
        old_dir = args.old
        if old_dir is None:
            old_dir = Path(tmp)
            committed_snapshot(args.rev, old_dir)
        old, new = changelog.load_snapshot(old_dir), changelog.load_snapshot(args.new)
    if not any(new[t] for t in changelog.CORE_TABLES):
        print(f"ERROR: no output CSVs found in {args.new}", file=sys.stderr)
        return 1
    initial = not any(old[t] for t in changelog.CORE_TABLES)
    diff = changelog.diff_snapshots(old, new)
    if not initial and not changelog.has_changes(diff):
        print("No data changes between the two snapshots.")
        return 0
    entry = changelog.render_entry(diff, new["meta"], old["meta"], initial)
    print(entry)
    if args.append:
        changelog.append_entry(args.changelog, entry)
        print(f"Appended to {args.changelog}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
