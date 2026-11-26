# Case study: "Jamlex Tank Graves"

- **Source:** deadlocklabs.gg build 872212, "Jamlex Tank Graves" by Jamlex. Version 275, updated 2026-11-24. The author says it was tested and played in Ascendant.
- **How it got here:** the page text was pasted in by hand; the site blocks automated access.
- **Labels:** the author's claims are labelled **Author**. Checks against the sheet use the usual labels from `analysis/formulas.md`.

## The build

| Stage (author's soul total) | Items |
|---|---|
| Early (21.6k) | Restorative Shot, Grit, Extra Spirit, Tesla Bullets, Extra Stamina, Mystic Shot, Weapon Shielding, Torment Pulse, Improved Spirit, Stamina Mastery, Toxic Bullets, Enchanter's Emblem |
| Mid (28.8k) | Mystic Vulnerability, Spirit Lifesteal, Escalating Exposure |
| Late (48k) | Capacitor, Spiritual Overflow, Siphon Bullets, Inhibitor |
| Optional late | Ricochet, Boundless Spirit, Leech, Scourge |

Plus counter options (Titanic Magazine, Dispel Magic, Counterspell, Metal Skin, Spellbreaker, Plated Armor, Divine Barrier, Phantom Strike, Silencer) and anti-crowd-control options (Reactive Barrier, Indomitable, Unstoppable).

The author's notes: sell Restorative Shot "when slot locked"; Weapon Shielding and Essence Theft are the early resists.

## The author's idea

**Author:** stack resist and health for high effective health. Also stack as many separate sources of item damage as possible (Torment Pulse, Tesla or Capacitor, Toxic Bullets, Escalating Exposure, Scourge, Siphon Bullets, Mystic Shot), so Graves deals damage "by simply existing" instead of relying on ability cooldowns. Escalating Exposure then amplifies every spirit source.

**Author:** "~4 stacks of EE ≈ having Boundless". Graves with this build matches about 86 to 89% of Celeste's Torment Pulse damage (author's measurement).

## Checks against the data

### Resists use the multiplicative rule

| Author's figure | Items | Multiplicative | Additive |
|---|---|---|---|
| Mid: 18% bullet | Weapon Shielding 18% | 18% ✓ | 18% |
| Late: 26% bullet | Weapon Shielding 18% + Siphon Bullets 10% | **26.2% ✓** | 28% |
| Mid: 42%+ spirit | Enchanter's Emblem 18% + Escalating Exposure 17% + 15% stolen by Essence Theft (10% + 5% at tier 1) | **42.1% ✓** | 50% |
| Late: 84% spirit | none of the late items add spirit resist | not reproduced | – |

- Mystic Vulnerability's own 8% is left out of the mid figure, because Escalating Exposure is built from it and consumes it.
- The 84% couldn't be matched. Even adding Scourge's 40% (an active, 10 s) gives 65.3%.
- The sheet files Weapon Shielding's 18% as **conditional**: it comes with a barrier that triggers on heavy damage, with a 35 s cooldown.

An independent player's numbers agree with the wiki's multiplicative rule.

### The damage comes from item triggers fed by a fast gun

Graves fires **9.8 shots per second** at 3.6 damage per shot (Data). On-hit items trigger per shot. Rough figures at 130 spirit power (Inferred trigger model, `formulas.md` §5):

| Source | Damage per second |
|---|---|
| Capacitor | ~133 |
| Tesla Bullets (replaced by Capacitor late) | ~85 |
| Torment Pulse (9 m radius) | ~39 |
| Mystic Shot | ~20 |
| Her gun at 35 boons with +86% weapon damage (Assumption on weapon damage) | ~99 |

Capacitor alone may out-damage her gun. Toxic Bullets, Siphon Bullets and Scourge deal shares of the target's health, so they don't depend on Graves' damage stats.

The 130 spirit power is a rough total:
- about 38 from boons
- 59 from spirit investment
- about 33 always-on from Improved Spirit, Mystic Shot and Spiritual Overflow
- 45 more is available from conditional effects (Enchanter's Emblem's passive, Spiritual Overflow's stacks), not counted

### Where the souls go

Final late items, with components consumed and Restorative Shot sold:

| Tab | Spent | Investment bonus |
|---|---|---|
| Weapon | 17,600 (Mystic Shot, Toxic Bullets, Capacitor, Spiritual Overflow) | +86% weapon damage |
| Vitality | 19,200 (Weapon Shielding, Stamina Mastery, Enchanter's Emblem, Siphon Bullets, Inhibitor) | +54% health |
| Spirit | 11,200 (Torment Pulse, Improved Spirit, Escalating Exposure) | +59 spirit power |

A tank build spends more than a third of its souls in the Weapon tab, because its damage-source items are Weapon items.

### Slots

- Early holds 9 items after consumed components, which is all 9 base slots. That's why the author sells Restorative Shot.
- Late holds 12, the maximum, which needs all three enemy Walkers destroyed.

The author's stage totals (21.6k / 28.8k / 48k) are roughly consistent with the items. They don't settle whether an upgrade costs the full price or the difference.

### Other agreement

- **Ability point costs:** the page shows 1 / 2 / 5 points per tier, matching the inferred costs.
- **Torment Pulse:** +100 health and 22% melee resist (Data). The author's "50% resist = 2× effective health" matches the effective health formula.

## Why it works, in framework terms

- **Self-sufficient damage:** stolen weapon damage and spirit resist (Essence Theft), summons whose health grows with boons, and damage based on the target's health.
- **Low cost of skipping weapon items:** her gun gains little from weapon investment (+18 damage per second for 4,800 souls at 9 boons, against +54 for Vyper).
- **A trigger carrier:** a fast gun with weak bullets feeds on-hit items.
- **One amplifier × many sources:** Escalating Exposure over about seven spirit damage sources.
- **Health × resist:** low base health is offset because resist multiplies whatever health she has.
