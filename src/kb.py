"""Knowledge base: what the game and its patch notes say about how things work.

The sheet in ``output/`` holds numbers. This module collects the words that
explain them, from three places in the primary source, all quoted rather than
paraphrased so nothing here is this tool's interpretation:

* the game's own text (tutorial pages, stat descriptions, HUD hints),
* the current numbers in the game files for each mechanic,
* Valve's patch notes, which state how mechanics work when they change.

deadlock.wiki itself is not read: it blocks automated access.
"""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

from .text import clean, tidy

_PRESENTATION = re.compile(
    r"Sound|Particle|Model|Color|Effect|Icon|Image|Material|Anim|Camera|Hud|Css|Outline|Glow|Light|Height$|"
    r"Capsule|Hull|Sight|Physics|Token|Loc|Warning|Clearance|SpreadRadius|DropHeight|TurnRate|BeamWeaponWidth|"
    r"Falloff|BulletGravity|BulletRadius|BulletSpeed|Reload|ShootMoveSpeed|AmmoConsumed|BulletsPerBurst|"
    r"BurstInter|UnitTargetLimit|ChannelMoveSpeed|PostCastDuration|Squad|Strafe|Tether|Acceleration", re.I)
_HEADER_RULE = re.compile(r"^[=\-]{2,}$")
_BULLET = re.compile(r"^\s*[-*•]\s*")

# slug -> topic. ``notes`` matches patch-note lines; ``text`` matches the game's
# own strings; ``data`` lists (file, key) blocks whose numbers are shown;
# ``general_only`` drops lines that are about one hero or item (those live in
# the per-hero and per-item histories instead).
TOPICS = {
    "mid-boss-and-rejuvenator": {
        "title": "Mid Boss and Rejuvenator",
        "notes": r"mid[- ]?boss|rejuv",
        "exclude": r"rejuvenating aurora",
        "text": r"midboss|mid_boss|rejuv|super_neutral",
        "data": [("generic", "RejuvParams"), ("npcs", "npc_super_neutral"), ("misc", "neutral_camp_midboss"),
                 ("misc", "citadel_item_pickup_rejuv")],
    },
    "souls-and-economy": {
        "title": "Souls and the economy",
        "notes": r"soul orb|unsecured|secure|\bden(y|ied|ies|ying)\b|bount|comeback|net ?worth|soul shar|souls? (are|is) (now )?(split|shared)|split among|assist",
        "text": r"soul|bounty|unsecured|networth",
        "data": [("generic", "ObjectiveParams"), ("generic", "HeroKillGoldShareFrac"), ("generic", "TrooperKillGoldShareFrac")],
        "general_only": True,
    },
    "troopers-and-lanes": {
        "title": "Troopers and lanes",
        "notes": r"trooper|\blanes?\b|zipline|creep wave|medic",
        "text": r"trooper|zipline|lane",
        "data": [("npcs", "trooper_normal"), ("npcs", "trooper_melee"), ("npcs", "trooper_medic")],
        "general_only": True,
    },
    "guardians": {
        "title": "Guardians and Base Guardians",
        "notes": r"guardian", "exclude": r"guardian ward",
        "text": r"guardian", "data": [("npcs", "npc_boss_tier1"), ("npcs", "npc_barrack_boss")],
        "general_only": True,
    },
    "walkers": {
        "title": "Walkers",
        "notes": r"\bwalkers?\b", "exclude": r"veil walker",
        "text": r"walker", "data": [("npcs", "npc_boss_tier2")], "general_only": True,
    },
    "shrines-and-patron": {
        "title": "Shrines and the Patron",
        "notes": r"shrine|\bpatron\b|weakened patron|base (defen|entrance)", "exclude": r"patron's",
        "text": r"shrine|patron|titan", "data": [("npcs", "npc_boss_tier3")], "general_only": True,
    },
    "neutral-camps": {
        "title": "Neutral camps, vaults and Sinner's Sacrifice",
        "notes": r"neutral|denizen|jungle|\bcamps?\b|sinner|vault",
        "text": r"neutral|sinner|vault|denizen",
        "data": [("npcs", "neutral_trooper_weak"), ("npcs", "neutral_trooper_normal"), ("npcs", "neutral_trooper_strong"),
                 ("npcs", "neutral_sinners_sacrifice"), ("misc", "neutral_camp_weak"), ("misc", "neutral_camp_medium"),
                 ("misc", "neutral_camp_strong"), ("misc", "neutral_camp_vaults")],
        "general_only": True,
    },
    "soul-urn": {
        "title": "Soul Urn",
        "notes": r"\burn\b|\bidol\b", "exclude": r"spirit snare|ability_tengu",
        "text": r"\burn|idol", "data": [("generic", "IdolParams")], "general_only": True,
    },
    "breakables-and-powerups": {
        "title": "Crates, golden statues and powerups",
        "notes": r"crate|breakable|statue|golden|power-?up|bridge buff|\bbox(es)?\b|permanent (buff|bonus)",
        "exclude": r"golden goose",
        "text": r"breakable|powerup|pickup|statue|crate",
        "data": [("generic", "BreakableSpawnTimeDesc")], "general_only": True,
    },
    "boons-and-ability-points": {
        "title": "Boons, levels and ability points",
        "notes": r"\bboons?\b|ability points?|\bAP\b|level ?up|ability unlock|power increase",
        "text": r"boon|abilitypoint|ability_point|levelup|power_increase",
        "data": [], "general_only": True,
    },
    "shop-and-investment": {
        "title": "Shop, item slots and investment bonuses",
        "notes": r"invest|flex slot|item slot|\bshop\b|sell(ing)? |refund|component|tier \d items?|item (cost|price)s?",
        "text": r"invest|flex|shop|sellitem|component",
        "data": [("generic", "ItemPricePerTier")], "general_only": True,
    },
    "melee-and-parry": {
        "title": "Melee and parry",
        "notes": r"melee|parry|parri", "text": r"melee|parry", "data": [], "general_only": True,
    },
    "movement": {
        "title": "Movement and stamina",
        "notes": r"stamina|\bdash|\bslid(e|ing)|sprint|air ?jump|wall ?jump|mantl|double jump|air ?strafe|bunny|move ?speed",
        "text": r"stamina|dash|slide|sprint|mantle|jump", "data": [], "general_only": True,
    },
    "damage-rules": {
        "title": "Damage rules: headshots, falloff, resists, stacking",
        "notes": r"headshot|\bcrit|falloff|resist|damage amp|diminish|stack(s|ing)? |armor|spirit damage|bullet damage|weapon damage",
        "text": r"headshot|crit|falloff|resist|damageamp|armor", "data": [], "general_only": True,
    },
    "healing-and-lifesteal": {
        "title": "Healing, regen, lifesteal and heal reduction",
        "notes": r"\bheal|lifesteal|regen|anti-?heal", "text": r"heal|lifesteal|regen", "data": [],
        "general_only": True,
    },
    "status-effects": {
        "title": "Status effects and resistance to them",
        "notes": r"\bstun|silenc|disarm|\bslow|\broot|immobil|debuff|status resist|unstoppable|invisib|sleep|interrupt",
        "text": r"stun|silence|disarm|slow|immobil|debuff|statusresist|unstoppable|invis",
        "data": [], "general_only": True,
    },
    "respawn-and-death": {
        "title": "Respawn timers and death",
        "notes": r"respawn|death timer|spawn protect|revive", "text": r"respawn|revive", "data": [],
        "general_only": True,
    },
}

# Game strings that explain something, as opposed to labels and menu text.
_EXPLAINER_KEY = re.compile(r"^(guide_|StatDesc_.*Desc$|Citadel_Hero_Stats_Tooltip|CitadelHeroStats_.*Desc|"
                            r"Objective_|AbilityButtonHint_|citadel_.*hud_hint|ReportCard_.*Desc|Sandbox_Tutorial)", re.I)
_SKIP_TEXT_KEY = re.compile(r"^(ability_|citadel_ability|upgrade_|modifier_|hero_|Steam_|citadel_settings|"
                            r"citadel_chatwheel|HeroTesting|Menu|GameUI|DevMenu|ping_)", re.I)


def read_patch_notes(repo_dir: Path, entity_names: dict) -> list:
    """Every patch-note line as ``{date, section, entity_kind, entity, line, link}``."""
    base = Path(repo_dir) / "data" / "changelogs"
    links = {}
    config = base / "changelog_configs.json"
    if config.exists():
        links = {k: v.get("link", "") for k, v in json.loads(config.read_text(encoding="utf-8")).items()}
    rows = []
    for path in sorted((base / "raw").glob("*.txt")):
        date, section, previous = path.stem, "", ""
        for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            line = raw_line.strip()
            if not line:
                continue
            if _HEADER_RULE.match(line):
                section = previous.rstrip(":").strip("[] ")
                if rows and rows[-1]["line"] == previous and rows[-1]["date"] == date:
                    rows.pop()  # the line above the rule was the header, not a note
                continue
            previous = line
            text = _BULLET.sub("", line)
            if re.fullmatch(r"\[.*\]", text):
                section = text.strip("[] ")
                continue
            prefix = text.split(":", 1)[0].strip().lower() if ":" in text else ""
            kind, entity = entity_names.get(prefix, ("", ""))
            rows.append({"date": date, "section": section, "entity_kind": kind, "entity": entity,
                         "line": text, "link": links.get(date, "")})
    return rows


def entity_names(primary: dict) -> dict:
    """Lower-cased hero and item names -> ``(kind, display name)``, for tagging patch-note lines."""
    names = {}
    for item in primary["items"].values():
        if item.get("Name"):
            names[item["Name"].lower()] = ("item", item["Name"])
    for hero in primary["heroes"].values():
        if hero.get("Name"):
            names[hero["Name"].lower()] = ("hero", hero["Name"])
    return names


def flatten(value, prefix=""):
    """Yield ``(path, number)`` for the gameplay numbers in a block of game data."""
    if isinstance(value, bool):
        return
    if isinstance(value, (int, float)):
        if value not in (0, -1):  # the files' "unset" defaults
            yield prefix, tidy(value)
    elif isinstance(value, dict):
        for key, child in value.items():
            if not _PRESENTATION.search(str(key)):
                yield from flatten(child, f"{prefix}.{key}" if prefix else str(key))
    elif isinstance(value, list):
        if value and all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in value):
            yield prefix, " / ".join(str(tidy(v)) for v in value)
        else:
            for index, child in enumerate(value):
                yield from flatten(child, f"{prefix}[{index}]")


def game_text(loc: dict, pattern: str | None = None) -> list:
    """Explanatory strings from the game, as ``(key, text)``; filtered to a topic when ``pattern`` is given."""
    out = []
    for key, value in loc.items():
        if not isinstance(value, str) or _SKIP_TEXT_KEY.match(key):
            continue
        text = clean(value, loc)
        if pattern is None:
            if _EXPLAINER_KEY.match(key) and len(text) >= 20:
                out.append((key, text))
        elif re.search(pattern, key, re.I) and len(text) >= 12:
            out.append((key, text))
    return out


def topic_notes(topic: dict, notes: list) -> list:
    include, exclude = re.compile(topic["notes"], re.I), re.compile(topic.get("exclude") or r"(?!x)x", re.I)
    picked = []
    for row in notes:
        if topic.get("general_only") and row["entity"]:
            continue
        if include.search(row["line"]) and not exclude.search(row["line"]):
            picked.append(row)
    return sorted(picked, key=lambda r: r["date"], reverse=True)


def _notes_block(rows: list) -> list:
    lines, date = [], None
    for row in rows:
        if row["date"] != date:
            date = row["date"]
            link = f" ([forum post]({row['link']}))" if row["link"] else ""
            lines += ["", f"**{date}**{link}", ""]
        lines.append(f"- {row['line']}")
    return lines


def render_topic(slug: str, topic: dict, primary: dict, notes: list, build: str) -> str:
    lines = [f"# {topic['title']}", "",
             f"Generated from the game files at build {build} and Valve's patch notes. Everything below is quoted "
             "from a source, not interpreted. Patch notes describe the game as of their date: read newest first, "
             "and treat an older line as history once a newer one changes the same thing.", ""]
    texts = game_text(primary["loc"], topic["text"])
    lines += ["## What the game itself says", ""]
    lines += [f"- {text} (`{key}`)" for key, text in texts] or ["- No explanatory text for this in the game's strings."]
    lines += ["", "## Current numbers in the game files", ""]
    any_numbers = False
    for file_key, block_key in topic["data"]:
        block = (primary.get(file_key) or {}).get(block_key)
        numbers = list(flatten(block)) if block is not None else []
        if not numbers:
            continue
        any_numbers = True
        lines += [f"`{block_key}`", "", "| Field | Value |", "|---|---|"]
        lines += [f"| {path or block_key} | {value} |" for path, value in numbers] + [""]
    if not any_numbers:
        lines += ["- No dedicated block for this in the files the sheet reads; see the sheet's tables.", ""]
    picked = topic_notes(topic, notes)
    lines += [f"## Patch history ({len(picked)} lines, newest first)"]
    lines += _notes_block(picked) or ["", "- No patch-note lines matched."]
    return "\n".join(lines) + "\n"


def render_history(kind: str, notes: list) -> str:
    """Patch history for every hero or item, one section each, newest first."""
    by_entity = {}
    for row in notes:
        if row["entity_kind"] == kind:
            by_entity.setdefault(row["entity"], []).append(row)
    title = "Hero" if kind == "hero" else "Item"
    lines = [f"# {title} patch history", "",
             f"Every patch-note line that starts with a {kind}'s name, newest first. Quoted from Valve's patch notes.", ""]
    for entity in sorted(by_entity, key=str.lower):
        rows = sorted(by_entity[entity], key=lambda r: r["date"], reverse=True)
        lines += [f"## {entity}"] + _notes_block(rows) + [""]
    return "\n".join(lines) + "\n"


def render_game_text(loc: dict) -> str:
    lines = ["# What the game says about itself", "",
             "Tutorial pages, stat descriptions and HUD hints from the game's English text, with the string key. "
             "This is Valve's own wording.", ""]
    lines += [f"- {text} (`{key}`)" for key, text in sorted(game_text(loc), key=lambda kv: kv[0].lower())]
    return "\n".join(lines) + "\n"


def render_index(primary: dict, notes: list, build: str, counts: dict) -> str:
    dates = sorted({row["date"] for row in notes})
    lines = [
        "# Knowledge base", "",
        "Companion to the reference sheet in `output/`. The sheet has the numbers; this explains how the "
        "mechanics around them work, in the words of the game and of Valve's patch notes.", "",
        f"- Game build: {build}",
        f"- Patch notes: {len(dates)} updates, {dates[0] if dates else '?'} to {dates[-1] if dates else '?'}, "
        f"{len(notes)} lines",
        "- Source: https://github.com/deadlock-wiki/deadlock-data (game text, game data, patch notes)", "",
        "## How to use it", "",
        "- Start with the mechanic's file under `mechanics/`. Each has three parts: what the game's own text "
        "says, the current numbers in the files, and the patch history.",
        "- The current numbers are fact for this build. The patch history says how a mechanic works, but only "
        "as of each line's date; a later line can replace it. Where the two disagree, the current numbers win.",
        "- Field names in the number tables are the game's own. Their meaning is not always stated anywhere; "
        "the patch history is usually what explains them.",
        "- `history/heroes.md` and `history/items.md` hold every patch line per hero and item.",
        "- `patch_notes.csv` is every line, for searching.", "",
        "## Limits", "",
        "- Nothing here is from deadlock.wiki. The wiki blocks automated access, so its prose is not included.",
        "- Topic files are built by keyword match on patch-note lines, so a file can miss a relevant line that "
        "uses other words, and can include a line that only mentions the word in passing.",
        "- Patch notes do not cover everything. A mechanic that has never changed may have no line at all.", "",
        "## Mechanics", "", "| File | Topic | Patch lines |", "|---|---|---|",
    ]
    for slug, topic in TOPICS.items():
        lines.append(f"| [mechanics/{slug}.md](mechanics/{slug}.md) | {topic['title']} | {counts[slug]} |")
    return "\n".join(lines) + "\n"


def build_knowledge(primary: dict, repo_dir: Path, out_dir: Path) -> dict:
    """Write the knowledge base to ``out_dir`` and return a summary of what was written."""
    out_dir = Path(out_dir)
    (out_dir / "mechanics").mkdir(parents=True, exist_ok=True)
    (out_dir / "history").mkdir(parents=True, exist_ok=True)
    build = primary["version"].get("ClientVersion", "?")
    notes = read_patch_notes(repo_dir, entity_names(primary))
    counts = {}
    for slug, topic in TOPICS.items():
        counts[slug] = len(topic_notes(topic, notes))
        (out_dir / "mechanics" / f"{slug}.md").write_text(render_topic(slug, topic, primary, notes, build), encoding="utf-8")
    (out_dir / "history" / "heroes.md").write_text(render_history("hero", notes), encoding="utf-8")
    (out_dir / "history" / "items.md").write_text(render_history("item", notes), encoding="utf-8")
    (out_dir / "game_text.md").write_text(render_game_text(primary["loc"]), encoding="utf-8")
    with open(out_dir / "patch_notes.csv", "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, ["date", "section", "entity_kind", "entity", "line", "link"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(notes)
    (out_dir / "README.md").write_text(render_index(primary, notes, build, counts), encoding="utf-8")
    return {"notes": len(notes), "topics": counts,
            "hero_lines": sum(1 for r in notes if r["entity_kind"] == "hero"),
            "item_lines": sum(1 for r in notes if r["entity_kind"] == "item")}
