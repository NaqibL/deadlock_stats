#!/usr/bin/env python3
"""Build the knowledge base in knowledge/ from the cached source.

    python build.py     # first: updates the source and the sheet
    python kb.py        # then: rebuilds knowledge/
"""
from __future__ import annotations

import sys
from pathlib import Path

from src import kb, source

ROOT = Path(__file__).resolve().parent


def main() -> int:
    repo_dir = ROOT / ".cache" / "deadlock-data"
    try:
        primary = source.load_primary(repo_dir)
    except source.SourceError as exc:
        print(f"ERROR: {exc}. Run `python build.py` first.", file=sys.stderr)
        return 1
    summary = kb.build_knowledge(primary, repo_dir, ROOT / "knowledge")
    print(f"Wrote knowledge/ at game build {primary['version'].get('ClientVersion')}: "
          f"{summary['notes']} patch-note lines ({summary['hero_lines']} about heroes, {summary['item_lines']} about items)")
    for slug, count in summary["topics"].items():
        print(f"  mechanics/{slug}.md  {count} patch lines")
    return 0


if __name__ == "__main__":
    sys.exit(main())
