"""Helpers for turning the game's localisation strings and values into plain text and numbers."""
from __future__ import annotations

import html
import re

_TAG = re.compile(r"<[^>]+>")
_BREAK = re.compile(r"</?br\s*/?>", re.I)
_TEMPLATE = re.compile(r"\{(?P<kind>[a-z]):(?P<body>[^}]*)\}")
_NUM_UNIT = re.compile(r"^\s*(-?(?:\d+\.?\d*|\.\d+))\s*([^\d\s].*)?$")
_SLOW_KEY = re.compile(r"SlowPercent$|^MovementSpeedSlow$|^SlowPercent")
_CAMEL = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")


def number(value):
    """Return ``(number, unit)`` for a source value.

    The source mostly stores numbers, but some values are strings with a unit
    glued on (``"3.0m"``). Anything that is not numeric comes back as ``(None, None)``.
    """
    if isinstance(value, bool) or value is None:
        return None, None
    if isinstance(value, (int, float)):
        return tidy(value), None
    if isinstance(value, str):
        m = _NUM_UNIT.match(value)
        if m:
            return tidy(float(m.group(1))), (m.group(2) or "").strip() or None
    return None, None


def tidy(value):
    """Round away float noise and turn whole floats into ints (800.0 -> 800)."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return value
    number_ = float(value)
    # Four decimals removes float noise; tiny coefficients (0.00035) keep their digits.
    rounded = round(number_, 4) if abs(number_) >= 0.01 or number_ == 0 else float(f"{number_:.3g}")
    return int(rounded) if rounded == int(rounded) else rounded


def fmt(value) -> str:
    """Format a number for the readable text columns."""
    value = tidy(value)
    return str(value)


def humanise(key: str) -> str:
    """``BonusClipSizePercent`` -> ``Bonus Clip Size Percent`` (fallback when no label exists)."""
    return _CAMEL.sub(" ", key.lstrip("#")).replace("_", " ").strip()


# The game reuses one label for different things. These keys get a label that
# says which, so two values in one cell cannot be mistaken for each other.
LABEL_OVERRIDES = {
    "TechArmorDamageReduction": "Spirit Resist Reduction",
    "MagicResistReduction": "Spirit Resist Reduction",
    "BulletArmorReduction": "Bullet Resist Reduction",
    "BulletResistReduction": "Bullet Resist Reduction",
    "HealAmpRegenPenaltyPercent": "Healing From Regen",
    "HealAmpReceivePenaltyPercent": "Incoming Healing",
    "FireRateSlow": "Fire Rate Slow",
    "ParryCooldownReduction": "Parry Cooldown Reduction",
    "MoveWhileShootingSpeedPenaltyReductionPercent": "Move Speed Penalty While Shooting Removed",
    "MoveWhileZoomedSpeedPenaltyReductionPercent": "Move Speed Penalty While Zoomed Removed",
}


def label(loc: dict, key: str, override: str | None = None) -> str:
    """English label for a property key, from the localisation data."""
    if key in LABEL_OVERRIDES:
        return LABEL_OVERRIDES[key]
    for candidate in (override, key):
        if not candidate:
            continue
        candidate = candidate.lstrip("#")
        for token in (candidate + "_label", candidate):
            text = loc.get(token)
            if isinstance(text, str) and text.strip():
                text = clean(text, loc)
                # The game labels slows as "Move Speed" and shows them as a negative;
                # the files store the magnitude, so say "Slow" to keep the sign clear.
                if _SLOW_KEY.search(key) and "slow" not in text.lower():
                    text += " Slow"
                return text
    return humanise(key)


def postfix(loc: dict, key: str) -> str:
    text = loc.get(key + "_postfix")
    return text.strip() if isinstance(text, str) else ""


def clean(text, loc: dict | None = None, values: dict | None = None) -> str:
    """Strip markup from a localisation string and resolve its ``{x:...}`` templates."""
    if not text:
        return ""
    loc = loc or {}
    values = values or {}

    def template(m):
        kind, body = m.group("kind"), m.group("body")
        if kind == "s":
            if body in values and values[body] is not None:
                return fmt(values[body])
            return f"[{body}]"
        name = body.split(":")[-1].strip("'\" ")
        if body.startswith("citadel_inline_attribute"):
            return loc.get("InlineAttribute_" + name) or humanise(name).lower()
        if body.startswith("citadel_binding"):
            return f"[{humanise(name)}]"
        return humanise(name)

    text = _BREAK.sub(" ", text)
    text = _TAG.sub("", text)
    text = _TEMPLATE.sub(template, text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()
