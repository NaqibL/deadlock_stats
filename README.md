# Deadlock reference sheet

One spreadsheet of every playable Deadlock hero, hero ability and shop item with
their numbers, generated from the game's own data files. No hand-copied values.

## Refresh

```bash
pip install -r requirements.txt
```

```bash
python build.py
```

```bash
git add output && git commit -m "Refresh sheet"
```

`build.py` updates the local copy of the source, rebuilds every table, runs the
validation and cross-check, and writes `output/`. If validation finds an error
it stops and writes nothing. If nothing changed since the last build it leaves
`output/` untouched. Committing `output/` makes the git history of the outputs
the history of game balance.

Options: `--offline` (reuse the cached source, no network), `--no-crosscheck`,
`--force` (rewrite outputs even if nothing changed).

## Outputs

| File | Contents |
|---|---|
| `output/deadlock.xlsx` | The sheet: Heroes, Abilities, Items, Investment, Progression, Units, Rules, Powerups, Permanent buffs and Meta tabs |
| `output/*.csv` | The same tables as CSV, one file per tab |
| `output/CHANGELOG.md` | What changed in each build: old and new value per entity and field, newest first |
| `output/REPORT.md` | The last build's validation findings, cross-check results and the list of what was filtered out |

Numbers are stored as numbers without units. A blank cell means "not applicable".

## Sources

- **Primary:** [deadlock-wiki/deadlock-data](https://github.com/deadlock-wiki/deadlock-data),
  Deadbot's parse of the game files. Cloned into `.cache/deadlock-data`.
- **Cross-check and gap filler:** the raw game files in
  [SteamDatabase/GameTracking-Deadlock](https://github.com/SteamDatabase/GameTracking-Deadlock)
  (`heroes.vdata`, `abilities.vdata`, `generic_data.vdata`), parsed independently by `src/kv3.py`.

The Deadlock API assets service (`assets.deadlock-api.com`) was the intended
cross-check, but that hostname had no DNS record when this was built, so the raw
game files are used instead.

## Reading the tables

`knowledge/settled.md` answers the questions these tables raise: what ambiguous
numbers mean, which are settled and which still need an in-game test. Read it
alongside this section.

**Heroes.** Speeds are metres per second, distances metres.

- `hero_tags` and `gun_tag` come from the raw game files; `gun_tag` is blank
  where the game sets none. `role` is blank where the game has no role line.
- `damage_per_shot` is `bullet_damage` x `pellets_per_shot`, except for guns
  the files flag as hitting a target once per shot (Baba, Drifter), where it is
  one pellet. `fire_rate` is bullets per second; `fire_rate_max_spin` is the top
  rate of guns that spin up. The DPS columns are the files' own figures.
- `falloff_end_damage_scale` is the fraction of damage left at `falloff_end`.
- `can_headshot`, `headshot_bonus_scale_pct` (0 is normal, negative means this
  hero's headshots gain less) and `headshot_damage_taken_reduction_pct` (damage
  this hero takes from headshots).
- `sprint_speed` is the bonus added to `move_speed` out of combat.
  `stamina_recovery_seconds` is the time to regain one stamina.
  `move_speed_while_shooting_scale` 0.75 means 75% speed while firing.
- `*_per_boon` columns are what each boon adds. `spirit_scaling` lists hero
  stats that grow with spirit power, per point.
- `bullet_lifesteal_effectiveness` and `spirit_lifesteal_effectiveness` scale
  the hero's lifesteal (1 is normal).

**Abilities.** Four rows per hero (`slot` 4 is the ultimate). A hero with an
alternate form has extra rows for that form's own abilities, marked in `form`.

- The numeric columns and `spirit_scaling` hold only what the in-game tooltip
  card shows. A value is `base + coefficient x spirit power`.
- `damage_spirit_scale` and `dps_spirit_scale` are the spirit power coefficients
  for those two properties; `spirit_scaling` lists every coefficient on the card.
- `other_scaling` lists scaling with boons, melee damage and weapon damage.
- `other_properties` holds the remaining tooltip properties.
- `internal_properties` holds values the files have but the card does not show
  (camera, sound and visual values are left out). Some are tuning, some unlock
  with upgrades, some are leftovers of older designs: not confirmed live.
- `upgrade_1..3` are added to the base values and coefficients.

**Items.** `cost` is the list price. Effects are split three ways:

- the stat columns and `other_innate_stats`: what the buyer always has;
- `conditional_effects`: procs, stacks, thresholds, on-use effects, and imbue
  bonuses (which apply to one chosen ability);
- `enemy_effects`: effects applied to enemies.

The split comes from the tooltip sections in the source and their flags, from
whether the raw files provide a passive as a plain stat, and, for the handful
of items where those give the wrong side, from the tooltip wording (the list is
`SIDE_OVERRIDES` in `src/items.py`). The enemy bucket is partly inferred from
property type and name. A "Slow" carries a positive size; resist reductions,
healing reductions and damage penalties are negative.

`stats_not_on_tooltip` lists values the files mark as provided stats but that
no tooltip section shows. They are not counted in the stat columns, because
some are leftovers. `unlisted_properties` holds the rest: tuning constants.

`activation` is Active or Passive; a `cooldown` on a passive item is its proc
cooldown. `ability_cooldown_reduction_pct` affects abilities only.

**Investment.** The cumulative bonus you hold once you have spent that many
souls in a shop category. `bonus_unit` says what the number is: a percentage of
weapon damage (gun and melee), a percentage of base health, or a flat amount of
spirit power. The units come from Valve's patch notes.

**Progression.** `level` is the game's "Boon N". Each row is what that soul
threshold grants (a boon, an ability unlock, an ability point) with running
totals. Multiply a hero's per-boon columns by `total_boons` to get their stats
at a given soul count.

**Units.** Objectives, troopers and neutral camp creeps. Resists are positive
when the unit takes less damage. Objective soul rewards are team totals. Values
for creeps are per creep at minute 0. Read the `note` column: it says what the
row leaves out and where the files and the patch notes disagree. Names the
files do not give (Base Guardian, Mid Boss, the camp sizes) are in `src/world.py`.

**Rules.** Global numbers: prices, bounties and how they are shared, trooper
waves, the respawn curve, Soul Urn, Unstable Rift, Rejuvenator. `source_field`
names the field in the game files or the server setting (`convar ...`); the
wording in `rule` is this tool's reading of it, checked against the patch notes.

**Powerups.** The timed buffs at the bridges: each stat at its starting and
full strength, the minutes between which it grows, and how long it lasts.

**Permanent buffs.** The small permanent stat buffs from golden statues and
other sources, at each of their three levels.

## What is filtered out

Only what a player can pick or buy today is kept. The full list of exclusions,
with the reason for each, is in `output/REPORT.md`.

- Heroes: must be enabled, have a hero id and a hero type. The source's
  `InDevelopment` flag is not used, because it is still set on heroes that are
  live. The cross-check confirms the roster against the raw files'
  release state.
- Items: must have an English name, be enabled, not be Street Brawl only, and
  be tier 1 to 4 in one of the three shop categories.

## Validation

Run on every build (`src/validate.py`):

- **Counts** against the previous output (or the build 6864 baseline). A change
  is a warning; a drop of more than 10% is an error.
- **Completeness**: no blanks in hero health and bullet damage, item tier and
  cost, or ability cooldown where the source has one.
- **Prices**: an item whose cost is not its tier's standard price gets a warning.
- **Reference values**: a short list of known values checks that the parser
  reads the right fields. A balance patch that changes one produces a warning;
  check the patch notes, then update `SANITY` in `src/validate.py`.
- **Cross-check**: hero roster and key stats, item tier, cost and category, and
  every numeric ability and item property with its spirit scaling are compared
  with the raw game files. Disagreements are listed, never resolved silently.

## Knowledge base

```bash
python kb.py
```

writes `knowledge/`, the companion to the sheet: how the mechanics work, in the
words of the game and of Valve's patch notes. Run it after `build.py`.

| Path | Contents |
|---|---|
| `knowledge/README.md` | Index, and which source wins when they disagree |
| `knowledge/settled.md` | Hand-written: what ambiguous numbers mean, known leftovers, where files and patch notes differ, and what still needs an in-game test. Every patch-note quote in it is verified on each run |
| `knowledge/mechanics/*.md` | One file per mechanic (Mid Boss and Rejuvenator, souls, troopers, objectives, neutral camps, urn, shop, melee, movement, damage rules, healing, status effects, respawn). Each has the game's own text, the current numbers in the files, and the patch history newest first |
| `knowledge/history/heroes.md`, `items.md` | Every patch-note line per hero and per item |
| `knowledge/game_text.md` | The game's tutorial pages, stat descriptions and HUD hints |
| `knowledge/patch_notes.csv` | Every patch-note line, for searching |

Apart from `settled.md`, everything in it is quoted from a source, not written
by the tool. It does not include deadlock.wiki: the wiki blocks automated access. Topic files are built
by keyword match, so they can miss a line or include a passing mention.

## Formulas and analysis

```bash
python analysis/formulas.py
```

prints the worked examples from `analysis/formulas.md`, which sets out how the
numbers combine: hero growth, investment, ability scaling, resist stacking and
shred, soul sharing, bounties over time and respawn. Each rule is labelled with
how far it can be trusted (game data, settled, community wiki, inferred or
assumed), and the formulas still open come with sandbox tests that tell the
candidates apart. `analysis/formulas.py` implements the rules against
`output/`; `tests/test_formulas.py` checks them. The resist rules come from
deadlock.wiki, pasted in by hand rather than fetched.

`analysis/framework.md` is the method for theorising builds and matchups from
those formulas (measures of power, event checkpoints, damage mix, theory
types), and `analysis/case-studies/` checks real builds against the sheet.
`analysis/mechanics.md` covers every source of damage, control and sustain and
the ways to eliminate an opponent. `python analysis/catalogue.py` writes
`analysis/catalogues/` (every damage, control and defence entry, counted) and
`python analysis/hero_cards.py` then writes `analysis/heroes/` (a card per hero).
`analysis/deadlock-systems-explainer.md` is a longer read-through of every
system; where it and `formulas.md` differ, `formulas.md` is newer.

## Comparing snapshots

```bash
python diff.py
```

compares the last committed `output/` with the one on disk.
`python diff.py OLD_DIR NEW_DIR` compares any two snapshot directories, and
`--rev <git revision>` picks a different commit as the old side.

## Tests

```bash
python -m pytest -q
```

`tests/test_live.py` checks the real cached source and is skipped until
`build.py` has run once.
