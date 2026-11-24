"""Fetching and loading the source data.

Primary: deadlock-wiki/deadlock-data (Deadbot's parsed game files), kept as a
shallow git clone in the cache directory.
Cross-check: the raw game files from SteamDatabase/GameTracking-Deadlock,
downloaded file by file.
"""
from __future__ import annotations

import json
import subprocess
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

PRIMARY_URL = "https://github.com/deadlock-wiki/deadlock-data"
PRIMARY_BRANCH = "master"
RAW_BASE = "https://raw.githubusercontent.com/SteamDatabase/GameTracking-Deadlock/master/game/citadel/"
RAW_FILES = {
    "steam.inf": "steam.inf",
    "heroes.vdata": "pak01_dir/scripts/heroes.vdata",
    "abilities.vdata": "pak01_dir/scripts/abilities.vdata",
    "generic_data.vdata": "pak01_dir/scripts/generic_data.vdata",
}
PRIMARY_JSON = {
    "heroes": "data/json/hero-data.json",
    "abilities": "data/json/ability-data.json",
    "ability_cards": "data/json/ability-cards.json",
    "items": "data/json/item-data.json",
    "item_cards": "data/json/item-cards.json",
    "loc": "data/localizations/english.json",
}


class SourceError(RuntimeError):
    pass


def _git(args, cwd=None) -> str:
    result = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        raise SourceError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


def update_primary(repo_dir: Path) -> None:
    """Clone the primary repository, or bring an existing clone up to date."""
    repo_dir = Path(repo_dir)
    if not (repo_dir / ".git").exists():
        repo_dir.parent.mkdir(parents=True, exist_ok=True)
        _git(["clone", "--depth", "1", "--branch", PRIMARY_BRANCH, PRIMARY_URL, str(repo_dir)])
        return
    _git(["fetch", "--depth", "1", "origin", PRIMARY_BRANCH], cwd=repo_dir)
    _git(["reset", "--hard", "FETCH_HEAD"], cwd=repo_dir)


def parse_version(text: str) -> dict:
    """Parse ``version.txt`` / ``steam.inf`` (``Key=Value`` lines)."""
    out = {}
    for line in text.splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            out[key.strip()] = value.strip()
    return out


def build_date(version: dict) -> str:
    """ISO date of the game build (``Nov 23 2026`` -> ``2026-11-23``)."""
    raw = version.get("VersionDate", "")
    try:
        return datetime.strptime(raw, "%b %d %Y").date().isoformat()
    except ValueError:
        return raw


def load_primary(repo_dir: Path) -> dict:
    """Load the primary source into one dict: the JSON tables, version and git commit."""
    repo_dir = Path(repo_dir)
    data = {}
    for name, rel in PRIMARY_JSON.items():
        path = repo_dir / rel
        if not path.exists():
            raise SourceError(f"primary source is missing {rel}; its layout may have changed")
        with open(path, encoding="utf-8") as fh:
            data[name] = json.load(fh)
    version_path = repo_dir / "data" / "version.txt"
    if not version_path.exists():
        raise SourceError("primary source is missing data/version.txt")
    data["version"] = parse_version(version_path.read_text(encoding="utf-8"))
    data["commit"] = {"hash": "", "date": ""}
    if (repo_dir / ".git").exists():
        data["commit"] = {
            "hash": _git(["rev-parse", "HEAD"], cwd=repo_dir),
            "date": _git(["log", "-1", "--format=%cI"], cwd=repo_dir),
        }
    return data


def fetch_raw(raw_dir: Path, timeout: int = 120) -> None:
    """Download the raw game files used for the cross-check."""
    raw_dir = Path(raw_dir)
    raw_dir.mkdir(parents=True, exist_ok=True)
    for name, rel in RAW_FILES.items():
        try:
            with urllib.request.urlopen(RAW_BASE + rel, timeout=timeout) as response:
                payload = response.read()
        except OSError as exc:
            raise SourceError(f"could not download cross-check file {rel}: {exc}") from exc
        (raw_dir / name).write_bytes(payload)


def load_raw(raw_dir: Path) -> dict:
    """Parse the downloaded raw game files."""
    from . import kv3

    raw_dir = Path(raw_dir)
    missing = [name for name in RAW_FILES if not (raw_dir / name).exists()]
    if missing:
        raise SourceError(f"cross-check files not downloaded: {', '.join(missing)}")
    return {
        "version": parse_version((raw_dir / "steam.inf").read_text(encoding="utf-8")),
        "heroes": kv3.load(raw_dir / "heroes.vdata"),
        "abilities": kv3.load(raw_dir / "abilities.vdata"),
        "generic": kv3.load(raw_dir / "generic_data.vdata"),
    }


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
