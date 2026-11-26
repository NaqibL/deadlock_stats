"""Catalogue every damage source, crowd-control effect and defensive or sustain effect in the sheet.

Reads ``output/abilities.csv`` and ``output/items.csv`` and writes three CSVs to
``analysis/catalogues/``:

- ``damage_sources.csv``: one row per damage property of an ability, upgrade or item.
- ``crowd_control.csv``: one row per control effect (stun, sleep, silence, slow, ...).
- ``defence_sustain.csv``: heals, barriers, lifesteal, own resists, evasion, invulnerability,
  debuff resist, and the effects that work against them (anti-heal, resist reduction, amps).

The classification is a keyword reading of property names and tooltip text, not a game rule.
Every row keeps the raw text it came from (``raw``) so it can be checked. Method and limits:
``analysis/catalogues/README.md``.

    python analysis/catalogue.py
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "output"
OUT = Path(__file__).resolve().parent / "catalogues"

# Abilities that deal weapon damage (deadlock.wiki, Damage Resistance page, read 2026-11-26).
WEAPON_DAMAGE_ABILITIES = {
    ("Deadman Danny", "Chimera Mk1"), ("Deadman Danny", "Jettison Fuel"), ("Haze", "Fixation"),
    ("Holliday", "Crackshot"), ("Rat King", "Scrap Grenade"), ("Rat King", "Royal Pestments"),
    ("Rat King", "Rule, Ratannia!"), ("Venator", "Consecrating Grenade"), ("Venator", "Gutshot"),
    ("Venator", "Ira Domini"),
}

# Item control effects that the effect text states but the number columns do not (durations from the
# item's own Duration / Debuff Duration fields). Read from items.csv effect_text, build 6868.
ITEM_TEXT_CC = {
    "Capacitor": [("movement silence", 3.0)],
    "Slowing Hex": [("movement silence", 3.5)],
    "Phantom Strike": [("disarm", 3.0)],
    "Cursed Relic": [("curse", 3.25), ("silence", 3.25), ("disarm", 3.25)],
}
# Items whose effect text protects against or removes control.
ITEM_PROTECTION = {
    "Unstoppable": "control immunity (active)",
    "Indomitable": "control cleanse (automatic)",
    "Reactive Barrier": "barrier when controlled",
    "Dispel Magic": "cleanse (active)",
    "Divine Barrier": "cleanse non-stun (active, ally)",
    "Cheat Death": "death immunity",
    "Metal Skin": "bullet immunity (active)",
    "Ethereal Shift": "invulnerability (active)",
}

# Words in an ability description that name a control effect (checked against descriptions, build 6868).
DESCRIPTION_CC = [
    ("stun", ("applying stun", "stunning", "and stunned", "stuns ", "applies stun", "hold the target in place")),
    ("displacement", ("pulling", "pulls ", "reeling them", "knockup", "knockback", "knock up", "slammed",
                      "slam them", "swaps your position", "launches you and nearby enemies")),
    ("fire rate slow", ("slowing their fire rate", "reduced fire rate")),
    ("lift", ("lift an enemy", "lifted",)),
    ("time stop", ("cannot take action",)),
    ("sleep", ("fall asleep", "puts them to sleep", "sleep ")),
    ("movement silence", ("cannot use movement abilities",)),
    ("silence", ("silenc",)),
    ("disarm", ("disarm",)),
    ("immobilize", ("immobiliz", "root")),
    ("move slow", ("slows", "slowed", "slowing", " slow ")),
]

# Description matches that are not control on an enemy (self effects, allies, interruptions), read one by one.
DESCRIPTION_NOT_CC = {
    ("Air Drop", "lift"), ("Traveler", "sleep"), ("Traveler", "silence"), ("Traveler", "immobilize"),
    ("Traveler", "stun"), ("Lightning Ball", "move slow"), ("Heavy Barrage", "move slow"),
    ("Flame Dash", "move slow"), ("Ice Path", "move slow"), ("Chimera Mk1", "move slow"),
    ("Chimera Mk1", "stun"), ("Petrifying Bola", "time stop"), ("Crimson Slash", "move slow"),
}

PROP = re.compile(
    r"^(?P<name>[^:]+?)(?:\s*\[(?P<tag>[^\]]+)\])?:\s*(?P<val>-?[\d.]+)?\s*(?P<unit>%|s|m|x)?"
    r"(?P<rest>.*)$")
COEF = re.compile(r"\(\+?(-?[\d.]+) x ([a-z %]+?)\)")
SEG = re.compile(r"^\[(?P<tags>[^\]]+)\]\s*(?P<body>.*)$")

# ---------------------------------------------------------------- reading text


def read(name):
    with open(OUTPUT / f"{name}.csv", newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def props(text):
    """Split "A: 1s; B: 40 (+0.9 x spirit power)" into dicts."""
    out = []
    for part in (p.strip() for p in (text or "").split(";")):
        m = PROP.match(part)
        if not m or not m.group("name"):
            continue
        trailing = re.search(r"\[([^\]]+)\]\s*$", part)
        coefs = {}
        for v, k in COEF.findall(part):
            coefs[k.strip()] = coefs.get(k.strip(), 0) + float(v)
        tag = m.group("tag") or (trailing.group(1) if trailing else "")
        out.append({"name": m.group("name").strip(), "tag": tag, "value": num(m.group("val")),
                    "unit": m.group("unit") or "", "pct_dps": "% DPS" in part,
                    "spirit": coefs.get("spirit power"), "boon": coefs.get("boon"),
                    "weapon": coefs.get("weapon damage %"), "raw": part})
    return out


def segments(text):
    """Split an item effect column into (tags, properties) per tooltip section."""
    out = []
    for seg in (s.strip() for s in (text or "").split(" | ")):
        m = SEG.match(seg)
        tags, body = (m.group("tags"), m.group("body")) if m else ("", seg)
        out.append((tags, props(body)))
    return out


def upgrade_props(text):
    """'Stun Duration +0.8s; Damage +90 | prose' -> properties of the stat half."""
    stat = (text or "").split(" | ")[0]
    out = []
    for part in (p.strip() for p in stat.split(";")):
        m = re.match(r"^(?P<name>.+?)\s+(?P<val>[+-]?[\d.]+)\s*(?P<unit>%|s|m)?(?P<rest>.*)$", part)
        if m:
            coef = re.search(r"\+?(-?[\d.]+) x spirit power", part)
            value = float(m.group("val"))
            if m.group("rest").lstrip().startswith("x "):
                value = 0.0  # the upgrade only adds scaling (spirit power, melee damage, ...)
            out.append({"name": m.group("name").strip(), "tag": "", "value": value,
                        "unit": m.group("unit") or "", "pct_dps": "% DPS" in part,
                        "spirit": float(coef.group(1)) if coef else None, "boon": None, "weapon": None,
                        "raw": part})
    return out


# ---------------------------------------------------------------- classification

NOT_DAMAGE = ("threshold", "reduction", "taken", "amp", "penalty", "resist", "to heal", "deferred", "regenerated",
              "self damage", "returned", "as healing", "per stack", "bonus scale", "time for max", "range",
              "radius", "duration", "interval", "delay", "count", "cooldown", "heal", "stolen", "steal",
              "vs. npcs", "weapon damage per kill", "permanent weapon damage", "per kill", "multishot",
              "uninterruptible", "additional", "damage cap", "damage bonus")

GUN_BUFFS = ("weapon damage", "bullet damage")  # flat per-bullet additions to the hero's own gun

CC_RULES = [  # (type, test on lower-case name, needs a duration)
    ("stun", lambda n: "stun" in n and not any(x in n for x in ("self stun", "delay before", "range", "cooldown"))),
    ("sleep", lambda n: n.startswith("sleep duration")),
    ("immobilize", lambda n: "immobilize" in n),
    ("silence", lambda n: "silence" in n),
    ("disarm", lambda n: "disarm" in n),
    ("petrify", lambda n: "petrify duration" in n),
    ("freeze", lambda n: "freeze duration" in n),
    ("fear", lambda n: n == "fear duration"),
    ("time stop", lambda n: "time stop duration" in n or "time-stop" in n),
    ("hex", lambda n: n == "hex duration"),
    ("curse", lambda n: n == "curse duration"),
    ("tether", lambda n: "tether duration" in n),
    ("lift", lambda n: "lift duration" in n),
    ("displacement", lambda n: False),  # matched by the [Displacement] tag
    ("fire rate slow", lambda n: "fire rate slow" in n),
    ("move slow", lambda n: ("slow" in n and "fire rate" not in n and "duration" not in n
                             and "resist" not in n and "velocity" not in n) or n in ("dash distance",)),
    ("accuracy / vision", lambda n: "weapon accuracy" in n or "reduced vision" in n),
    ("reveal", lambda n: "reveal duration" in n),
]

DEFENCE_RULES = [
    ("heal", lambda n: (re.search(r"heal(?!th)", n) or "health restored" in n or "regen" in n or "lifesteal" in n
                        or "life steal" in n)
     and "reduction" not in n and "healing from regen" not in n and "incoming healing" not in n
     and "as damage" not in n),
    ("barrier", lambda n: "barrier" in n and "damage" not in n),
    ("own resist", lambda n: n in ("bullet resist", "spirit resist", "melee resist", "damage reduction",
                                    "channel damage resist", "time slow damage reduction")),
    ("evasion", lambda n: "evasion" in n),
    ("invulnerability", lambda n: "invulnerab" in n),
    ("debuff resist", lambda n: "debuff resist" in n or "slow resist" in n),
    ("damage deferred", lambda n: "deferred" in n),
    ("anti-heal", lambda n: "incoming healing" in n or "healing from regen" in n),  # negative values only, see classify
    ("resist reduction", lambda n: "resist reduction" in n and "duration" not in n),
    ("damage amp on target", lambda n: n in ("damage taken", "extra damage taken", "spirit amp per stack",
                                             "damage amp per stack", "amplified damage", "wrecked bullet amp",
                                             "damage amplification", "damage amp", "amp per stack")),
]


def damage_kind(p):
    """'flat', 'per second', 'target health %' or None when the property is not damage."""
    n = p["name"].lower()
    if not ("damage" in n or "dps" in n or n.endswith(" bite")):
        return None
    if any(x in n for x in NOT_DAMAGE) and not ("health" in n and "damage" in n):
        return None
    if p["value"] is None:
        return None
    if n in GUN_BUFFS:
        return "gun buff per bullet" if p["unit"] != "%" else None
    if "per bullet" in n:
        return "per bullet"
    if p["pct_dps"] or ("health" in n and p["unit"] == "%"):
        return "target health %"
    if p["unit"] == "%":
        return None  # a % on damage is a buff or amp, not a damage number
    if "per second" in n or "dps" in n:
        return "per second"
    return "flat"


def classify(p, rules):
    n = re.sub(r"\s*\[.*?\]", "", p["name"]).lower()
    tag = p["tag"].lower().replace("emp", "silence").replace("disarmed", "disarm")
    if rules is CC_RULES and p["unit"] == "m" and "vision" not in n:
        return None  # a range or radius, not a control effect
    for kind, test in rules:
        if test(n) or (rules is CC_RULES and tag and kind in tag):
            if kind == "anti-heal" and (p["value"] or 0) >= 0:
                return None  # a positive "Incoming Healing" is a healing boost
            return kind
    return None


# ---------------------------------------------------------------- building rows


def ability_rows(abilities):
    dmg, cc, dfn = [], [], []
    for a in abilities:
        owner = a["form"] or a["hero"]
        base = {"source": "ability", "owner": owner, "name": a["name"], "slot": a["slot"],
                "cooldown": a["cooldown"], "charges": a["charges"], "radius": a["radius"]}
        os_ = a["other_scaling"] or ""
        if (a["hero"], a["name"]) in WEAPON_DAMAGE_ABILITIES or "weapon damage" in os_ or "weapon power" in os_:
            dtype = "weapon"
        elif "melee damage" in os_:
            dtype = "melee"
        else:
            dtype = "spirit"
        found = []
        if num(a["damage"]) is not None:
            found.append({"name": "Damage", "value": num(a["damage"]), "spirit": num(a["damage_spirit_scale"]),
                          "kind": "flat", "raw": f"damage {a['damage']}"})
        if num(a["dps"]) is not None:
            found.append({"name": "Damage Per Second", "value": num(a["dps"]), "spirit": num(a["dps_spirit_scale"]),
                          "kind": "per second", "raw": f"dps {a['dps']}"})
        for p in props(a["other_properties"]):
            k = damage_kind(p)
            if k:
                found.append({**p, "kind": k})
        # Damage that exists only as scaling with melee damage, weapon damage % or boons.
        for part in (x.strip() for x in os_.split(";") if x.strip()):
            m = re.match(r"^(?P<prop>.+?): (?P<coef>-?[\d.]+) per (?P<stat>.+)$", part)
            if not m or not damage_kind({"name": m.group("prop"), "value": 1.0, "unit": "", "pct_dps": False}):
                continue
            prop, coef, stat = m.group("prop"), float(m.group("coef")), m.group("stat")
            hit = next((x for x in found if x["name"] == prop), None)
            key = ("melee" if "melee" in stat else "weapon" if "weapon" in stat else "boon" if stat == "boon" else None)
            if not key:
                continue
            if hit is None:
                hit = {"name": prop, "value": 0.0, "spirit": None, "kind": "flat", "raw": f"other_scaling {part}"}
                found.append(hit)
            hit[f"{key}_coef"] = coef
        for f in found:
            gain = f["spirit"] * 100 / f["value"] * 100 if f.get("spirit") and f["value"] else None
            dmg.append({**base, "tier": 0, "property": f["name"], "kind": f["kind"],
                        "damage_type": ("target health %" if f["kind"] == "target health %"
                                        else "bullet" if f["kind"] == "gun buff per bullet" else dtype),
                        "base": f["value"], "spirit_coef": f.get("spirit"),
                        "weapon_pct_coef": f.get("weapon") or f.get("weapon_coef"),
                        "melee_coef": f.get("melee_coef"), "boon_coef": f.get("boon_coef") or f.get("boon"),
                        "gain_per_100_sp": gain, "other_scaling": os_, "raw": f["raw"]})
        if num(a["stun_duration"]):
            cc.append({**base, "tier": 0, "cc_type": "stun", "value": num(a["stun_duration"]), "unit": "s",
                       "raw": f"stun_duration {a['stun_duration']}"})
        if num(a["slow_percent"]):
            cc.append({**base, "tier": 0, "cc_type": "move slow", "value": num(a["slow_percent"]), "unit": "%",
                       "duration": a["slow_duration"], "raw": f"slow_percent {a['slow_percent']}"})
        for p in props(a["other_properties"]):
            kind = classify(p, CC_RULES)
            if kind:
                cc.append({**base, "tier": 0, "cc_type": kind, "value": p["value"], "unit": p["unit"], "raw": p["raw"]})
            d = classify(p, DEFENCE_RULES)
            if d:
                dfn.append({**base, "tier": 0, "effect": d, "value": p["value"], "unit": p["unit"],
                            "spirit_coef": p["spirit"], "raw": p["raw"]})
        # Control the description names but no field holds (inferred; duration from the ability's
        # duration or channel time where it has one).
        desc = (a["description"] or "").lower()
        have = {r["cc_type"] for r in cc if r["owner"] == owner and r["name"] == a["name"]}
        chan = next((p["value"] for p in props(a["other_properties"]) if p["name"] == "Channel Duration"), None)
        for kind, words in DESCRIPTION_CC:
            if (a["name"], kind) in DESCRIPTION_NOT_CC:
                continue
            if kind not in have and any(w in desc for w in words):
                dur = num(a["stun_duration"]) if kind == "stun" else None
                if kind in ("stun", "lift"):
                    dur = dur or (chan if chan and chan < 60 else None)
                cc.append({**base, "tier": 0, "cc_type": kind, "value": dur, "unit": "s" if dur else "",
                           "basis": "description", "raw": f"description: {a['description'][:180]}"})
                have.add(kind)
        for t in (1, 2, 3):
            for p in upgrade_props(a[f"upgrade_{t}"]):
                kind = classify(p, CC_RULES)
                if kind and (p["value"] or 0) > 0:
                    cc.append({**base, "tier": t, "cc_type": kind, "value": p["value"], "unit": p["unit"],
                               "raw": p["raw"]})
                d = classify(p, DEFENCE_RULES)
                if d:
                    dfn.append({**base, "tier": t, "effect": d, "value": p["value"], "unit": p["unit"],
                                "spirit_coef": p["spirit"], "raw": p["raw"]})
                k = damage_kind(p)
                if k:
                    dmg.append({**base, "tier": t, "property": p["name"], "kind": k,
                                "damage_type": ("target health %" if k == "target health %"
                                                else "bullet" if k == "gun buff per bullet" else dtype),
                                "base": p["value"], "spirit_coef": p["spirit"], "gain_per_100_sp": None,
                                "other_scaling": os_, "raw": p["raw"]})
    return dmg, cc, dfn


def delivery(tags, prop_names):
    t = tags.lower()
    if "active" in t:
        return "active"
    if "proc chance" in prop_names:
        return "on-hit chance"
    if "build up per shot" in prop_names:
        return "build-up"
    if "cooldown" in t:
        return "passive, on cooldown"
    return "passive"


def item_rows(items):
    dmg, cc, dfn = [], [], []
    for it in items:
        base = {"source": "item", "owner": f"{it['category']} T{it['tier']}", "name": it["name"],
                "slot": "", "cooldown": it["cooldown"], "charges": "", "radius": "", "tier": it["tier"]}
        cond = segments(it["conditional_effects"])
        cond_names = {p["name"].lower() for _, ps in cond for p in ps}
        for col, on_enemy in (("enemy_effects", True), ("conditional_effects", False)):
            for tags, ps in segments(it[col]):
                if "not on tooltip" in tags.lower():
                    continue
                names = {p["name"].lower() for p in ps} | cond_names
                how = delivery(tags, names)
                for p in ps:
                    k = damage_kind(p) if on_enemy or "damage" in p["name"].lower() else None
                    if k and on_enemy:
                        dmg.append({**base, "property": p["name"], "kind": k,
                                    "damage_type": "target health %" if k == "target health %" else "spirit (assumed)",
                                    "base": p["value"], "spirit_coef": p["spirit"],
                                    "gain_per_100_sp": p["spirit"] * 100 / p["value"] * 100 if p["spirit"] and p["value"] else None,
                                    "other_scaling": how, "raw": f"[{tags}] {p['raw']}"})
                    kind = classify(p, CC_RULES) if on_enemy else None
                    if kind:
                        cc.append({**base, "cc_type": kind, "value": p["value"], "unit": p["unit"],
                                   "raw": f"[{tags}] {p['raw']}"})
                    d = classify(p, DEFENCE_RULES)
                    if d and (on_enemy == (d in ("anti-heal", "resist reduction", "damage amp on target"))):
                        dfn.append({**base, "effect": d, "value": p["value"], "unit": p["unit"],
                                    "spirit_coef": p["spirit"], "raw": f"[{tags}] {p['raw']}"})
        # Always-on defensive stats.
        for col, eff in (("bullet_resist_pct", "own resist"), ("spirit_resist_pct", "own resist"),
                         ("bullet_lifesteal_pct", "heal"), ("spirit_lifesteal_pct", "heal"),
                         ("health_regen", "heal"), ("bonus_health", "health")):
            if num(it[col]):
                dfn.append({**base, "effect": eff, "value": num(it[col]), "unit": "", "spirit_coef": None,
                            "raw": f"always-on {col} {it[col]}"})
        for p in props(it["other_innate_stats"]):
            d = classify(p, DEFENCE_RULES)
            if d:
                dfn.append({**base, "effect": d, "value": p["value"], "unit": p["unit"], "spirit_coef": None,
                            "raw": f"always-on {p['raw']}"})
        # Control or protection stated only in the effect text (read item by item, see README).
        if it["name"] in ITEM_TEXT_CC:
            for kind, dur in ITEM_TEXT_CC[it["name"]]:
                if not any(r["name"] == it["name"] and r["cc_type"] == kind for r in cc):
                    cc.append({**base, "cc_type": kind, "value": dur, "unit": "s" if dur else "",
                               "raw": f"effect text: {it['effect_text'][:180]}"})
        if it["name"] in ITEM_PROTECTION:
            dfn.append({**base, "effect": ITEM_PROTECTION[it["name"]], "value": None, "unit": "", "spirit_coef": None,
                        "raw": f"effect text: {it['effect_text'][:180]}"})
    return dmg, cc, dfn


def merge_damage(rows):
    """One row per (owner, ability, tier, property, base): the files list some properties twice,
    once per scaling stat."""
    out, seen = [], {}
    for r in rows:
        key = (r["owner"], r["name"], r.get("tier"), r["property"], r["base"])
        if key in seen:
            prev = seen[key]
            for k in ("spirit_coef", "weapon_pct_coef", "gain_per_100_sp"):
                if prev.get(k) is None and r.get(k) is not None:
                    prev[k] = r[k]
            prev["raw"] += " || " + r["raw"]
        else:
            seen[key] = r
            out.append(r)
    return out


def dedupe(rows, keys):
    out, seen = [], set()
    for r in rows:
        k = tuple(r.get(x) for x in keys)
        if k not in seen:
            seen.add(k)
            out.append(r)
    return out


def write(name, rows):
    OUT.mkdir(exist_ok=True)
    fields = []
    for r in rows:
        fields += [k for k in r if k not in fields]
    with open(OUT / f"{name}.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k: ("" if v is None else (round(v, 4) if isinstance(v, float) else v)) for k, v in r.items()})


HARD_CC = ("stun", "sleep", "immobilize", "petrify", "freeze", "time stop", "hex", "fear", "tether", "lift",
           "displacement", "curse")
ACTION_DENIAL = ("silence", "disarm", "movement silence", "curse")


def fmt(v, digits=2):
    if v in (None, ""):
        return ""
    try:
        f = float(v)
    except (TypeError, ValueError):
        return str(v)
    if f != f:
        return ""
    return f"{f:.{digits}f}".rstrip("0").rstrip(".")


def md_table(rows, cols, heads):
    out = ["| " + " | ".join(heads) + " |", "|" + "---|" * len(heads)]
    for r in rows:
        out.append("| " + " | ".join(fmt(r.get(c)) if isinstance(r.get(c), float) else str(r.get(c) or "")
                                     for c in cols) + " |")
    return "\n".join(out)


def write_markdown(dmg, cc, dfn):
    head = ("Generated by `python analysis/catalogue.py` from `output/` (build {build}). Keyword classification of "
            "property names and tooltip text: check `raw` in the CSV before relying on a row. Method and limits: "
            "[README.md](README.md).\n\n")
    build_no = next(r["value"] for r in read("meta") if r["field"] == "game_build")
    head = head.format(build=build_no)

    # Damage sources.
    t0 = [r for r in dmg if r["source"] == "ability" and not r.get("tier")]
    lines = ["# Damage sources", "", head]
    lines += ["## Counts", "", md_table(
        [{"group": f"{s} / {d} / {k}", "n": n} for (s, d, k), n in sorted(
            __import__("collections").Counter((r["source"], r["damage_type"], r["kind"]) for r in dmg).items())],
        ["group", "n"], ["source / damage type / kind", "rows"]), ""]
    scal = sorted([r for r in t0 if r["kind"] == "flat" and r.get("gain_per_100_sp") and (r["base"] or 0) >= 20],
                  key=lambda r: -r["gain_per_100_sp"])
    lines += ["## Abilities that gain most from spirit power", "",
              "Extra damage from 100 spirit power as a share of base (coefficient x 100 / base, in %), flat damage of "
              "at least 20, base form, no upgrades.", "",
              md_table([{**r, "gain": f"+{r['gain_per_100_sp']:.0f}%"} for r in scal[:30]],
                       ["owner", "name", "slot", "property", "base", "spirit_coef", "gain", "cooldown"],
                       ["hero", "ability", "slot", "property", "base", "x spirit power", "gain per 100 SP", "cooldown"]), ""]
    for title, keep, note in (
        ("Damage based on the target's health", lambda r: r["kind"] == "target health %",
         "Grows with the target's health, so it does not need the attacker's damage stats."),
        ("Weapon-damage abilities", lambda r: r["damage_type"] == "weapon" and r["kind"] != "gun buff per bullet",
         "Reduced by bullet resist, not spirit resist (community: deadlock.wiki)."),
        ("Melee-scaling abilities", lambda r: r["damage_type"] == "melee",
         "Reduced by bullet resist and melee resist (community)."),
        ("Damage added per bullet", lambda r: r["kind"] in ("per bullet", "gun buff per bullet"),
         "Scales with shots per second; see formulas.md section 5.")):
        rows = [r for r in dmg if r["source"] == "ability" and keep(r)]
        lines += [f"## {title}", "", note, "", md_table(
            rows, ["owner", "name", "tier", "property", "base", "spirit_coef", "weapon_pct_coef", "other_scaling"],
            ["hero", "ability", "tier", "property", "base", "x spirit power", "x weapon damage %", "other scaling"]), ""]
    items = [r for r in dmg if r["source"] == "item"]
    lines += ["## Item damage sources", "", "Delivery: active, on-hit chance, build-up (per shot), or passive. "
              "Damage type is assumed spirit unless it is a share of health; the files do not label it.", "",
              md_table(items, ["name", "owner", "property", "kind", "base", "spirit_coef", "other_scaling", "cooldown"],
                       ["item", "tab / tier", "property", "kind", "base", "x spirit power", "delivery", "cooldown"]), ""]
    amp = [r for r in dfn if r["effect"] in ("damage amp on target", "resist reduction")]
    lines += ["## Amplifiers and resist reduction", "", "Effects that raise the damage a target takes from everything "
              "of a type. Resist reduction is subtracted from resist (community rule, formulas.md section 4).", "",
              md_table(amp, ["source", "owner", "name", "tier", "effect", "raw"],
                       ["source", "hero / tab", "name", "tier", "effect", "text"]), ""]
    (OUT / "damage-sources.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Crowd control.
    lines = ["# Crowd control", "", head,
             "Hard control removes the target's movement or actions; action denial removes one kind of action "
             "(abilities, gun, items, movement abilities); slows reduce speed or fire rate.", ""]
    heroes = sorted({r["owner"] for r in cc if r["source"] == "ability"})
    summary = []
    for h in heroes:
        rs = [r for r in cc if r["owner"] == h]
        hard0 = [r for r in rs if r["cc_type"] in HARD_CC and not r.get("tier") and r["unit"] == "s"]
        hardu = [r for r in rs if r["cc_type"] in HARD_CC and r.get("tier") and r["unit"] == "s"]
        def per_ability(rows):
            best = {}
            for r in rows:
                best[r["name"]] = max(best.get(r["name"], 0), r["value"] or 0)
            return sum(best.values())
        summary.append({"hero": h,
                        "hard": ", ".join(sorted({f"{r['cc_type']} ({r['name']})" for r in rs if r["cc_type"] in HARD_CC})),
                        "hard_s": per_ability(hard0), "hard_up": per_ability(hardu),
                        "deny": ", ".join(sorted({r["cc_type"] for r in rs if r["cc_type"] in ACTION_DENIAL})),
                        "slows": len({r["name"] for r in rs if "slow" in r["cc_type"]})})
    summary.sort(key=lambda r: -(r["hard_s"] + r["hard_up"]))
    lines += ["## By hero", "", "Seconds of hard control summed over the kit (each ability counted once, at its longest hard-control "
              "duration), base form, and the seconds upgrades add. Abilities whose control is named only in the "
              "description often have no duration, so they count as 0 here. A sum over abilities with different cooldowns, so a rough measure of how much control a kit "
              "carries, not of control per fight.", "",
              md_table(summary, ["hero", "hard_s", "hard_up", "hard", "deny", "slows"],
                       ["hero", "hard control (s)", "+ from upgrades (s)", "hard control", "action denial",
                        "abilities or upgrades that slow"]), ""]
    order = list(HARD_CC) + ["silence", "disarm", "movement silence", "fire rate slow", "move slow",
                             "accuracy / vision", "reveal"]
    for kind in order:
        rs = [r for r in cc if r["cc_type"] == kind]
        if rs:
            lines += [f"## {kind}", "", md_table(rs, ["source", "owner", "name", "tier", "value", "unit", "cooldown"],
                                                 ["source", "hero / tab", "name", "tier", "value", "unit", "cooldown"]), ""]
    (OUT / "crowd-control.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Defence and sustain.
    lines = ["# Defence and sustain", "", head]
    for kind in sorted({r["effect"] for r in dfn}):
        rs = [r for r in dfn if r["effect"] == kind]
        lines += [f"## {kind}", "", md_table(rs, ["source", "owner", "name", "tier", "value", "unit", "spirit_coef", "raw"],
                                             ["source", "hero / tab", "name", "tier", "value", "unit",
                                              "x spirit power", "text"]), ""]
    (OUT / "defence-sustain.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build():
    ad, ac, af = ability_rows(read("abilities"))
    idm, ic, idf = item_rows(read("items"))
    write("damage_sources", merge_damage(ad + idm))
    cc = dedupe(ac + ic, ("owner", "name", "tier", "cc_type", "value"))
    write("crowd_control", cc)
    write("defence_sustain", af + idf)
    write_markdown(merge_damage(ad + idm), cc, af + idf)
    return {"damage_sources": len(merge_damage(ad + idm)), "crowd_control": len(cc), "defence_sustain": len(af + idf)}


if __name__ == "__main__":
    print(build())
