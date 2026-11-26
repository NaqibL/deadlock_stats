# Catalogues

Every damage source, crowd-control effect and defensive or sustain effect in the sheet, in one place, so builds and matchups can be reasoned about across all heroes and items at once.

```bash
python analysis/catalogue.py
```

rebuilds everything here from `output/abilities.csv` and `output/items.csv`. Run it after `build.py`.

| File | Contents |
|---|---|
| `damage-sources.md`, `damage_sources.csv` | One row per damage property of an ability, ability upgrade or item. Includes damage type, kind (flat, per second, per bullet, share of target health), base, spirit and weapon-damage coefficients, and delivery (for items). |
| `crowd-control.md`, `crowd_control.csv` | One row per control effect: stun, sleep, immobilize, petrify, freeze, time stop, hex, fear, tether, lift, displacement, curse, silence, disarm, movement silence, fire-rate and move slows, accuracy, reveal. Includes a per-hero summary. |
| `defence-sustain.md`, `defence_sustain.csv` | Heals, regen and lifesteal; barriers; own resists; evasion; invulnerability; debuff resist; deferred damage; control protection and cleanses. Also the effects that work against defence: anti-heal, resist reduction, damage amplification on the target. |

## Method

This is a **keyword reading** of the sheet. It is not a game rule.

- **Property names** (for example "Stun Duration", "Bleed Damage", "Incoming Healing") decide the category. The rules are in `CC_RULES`, `DEFENCE_RULES` and `damage_kind()` in `catalogue.py`.
- **Tags** the files attach to values count too: `[Stun]`, `[Immobilize]`, `[Displacement]`, `[Disarmed]`, and `[EMP]`, which is the files' silence tag.
- **Ability descriptions** add control that no field holds, for example Mo & Krill's Combo ("Hold the target in place, stunning them"). These rows have `basis = description`.
  - A duration is filled in only for stuns and lifts, from the ability's stun field or channel time. That is inferred.
  - Description matches that turned out to be self, ally or interruption effects were read one by one and excluded (`DESCRIPTION_NOT_CC`).
- **Items whose control appears only in the effect text** (Capacitor, Slowing Hex, Phantom Strike, Cursed Relic) and items that protect against control (Unstoppable, Indomitable, Reactive Barrier, Dispel Magic, Divine Barrier, Cheat Death, Metal Skin, Ethereal Shift) are listed explicitly: `ITEM_TEXT_CC` and `ITEM_PROTECTION`.
- **Damage type for abilities:**
  - *weapon* when the ability is on deadlock.wiki's weapon-damage list or scales with weapon damage
  - *melee* when it scales with melee damage
  - *spirit* otherwise
  - *target health %* when the value is a share of health
- **Damage type for items:** assumed spirit unless it is a share of health. The files don't label it.
- **A % on a damage-named property** (for example "Weapon Damage: 20%") is a buff or amplifier, not a damage number, and is left out of damage sources.
- **Flat per-bullet additions to the hero's own gun** ("Bullet Damage: 7" on Haze's Bullet Dance) are kind *gun buff per bullet*.
- **Values not shown on the tooltip** (`[Not on tooltip]`) are skipped.

## Limits

- **Check before relying on a row.** Every row keeps the text it came from in `raw`.
- **Damage under unusual names can be missed,** and a damage-named property that isn't damage can slip in.
- **The per-hero control summary is rough.** It adds up seconds across abilities with different cooldowns, so it measures how much control a kit carries, not control per fight. Control named only in a description usually has no duration and counts as 0.
- **Who an ability property applies to isn't always clear.** A positive resist on an ability is listed as a buff on the caster or allies; a negative resist is listed as resist reduction on enemies.
- **Upgrade rows (`tier` 1 to 3) are what the upgrade adds**, not the total.
- **Alternate forms** (Silver (Transformed)) are listed under the form's name.
