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
| `output/deadlock.xlsx` | The sheet: Heroes, Abilities, Items, Investment, Progression, Units, Rules and Meta tabs |
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

**Heroes.** `hero_tags` and `gun_tag` come from the raw game files (the
primary source does not carry them); `gun_tag` is blank where the game sets
none. `role` is blank for heroes the game has no role line for. `sprint_speed` is the bonus added to `move_speed` while sprinting.
`stamina_recovery_seconds` is the time to regain one stamina.
`damage_per_shot` is `bullet_damage` x `pellets_per_shot`. Distances are metres.

`spirit_scaling` lists hero stats that grow with spirit power (Haze's clip
size, for example), per point of spirit power.

**Abilities.** Four rows per hero (`slot` 4 is the ultimate). A hero with an
alternate form has extra rows for that form's own abilities, marked in `form`.
`damage_spirit_scale` and `dps_spirit_scale` are the spirit power coefficients
for those two properties; `spirit_scaling` lists the coefficient for every
property that scales with spirit power (`TechPower` in the files).
`other_scaling` lists scaling with boons, melee damage and weapon damage.
`other_properties` holds the remaining properties shown on the in-game tooltip,
`internal_properties` the ones the files hold but the tooltip does not show
(camera, sound and visual tuning values are left out).

**Items.** Effects are split three ways:

- the stat columns and `other_innate_stats`: what the buyer always gets;
- `conditional_effects`: conditional, proc and on-use effects on the buyer;
- `enemy_effects`: effects applied to enemies.

The split comes from the tooltip sections in the source (`Innate` versus
`Passive` / `Active`) and its usage flags. The files flag only a handful of
properties as enemy-applied, so that bucket is completed by property type
(resist reduction, slow), status effect, and property name (damage dealt,
debuff durations, healing reduction). It is an approximation; the rule is
`bucket()` in `src/items.py`.

Some stats are on no tooltip section in the primary source. The raw game files
decide those: if the game provides the property as a stat with a non-zero base
value, it goes in the innate columns (and is named in `stats_not_on_tooltip`,
so you can see which numbers the tooltip does not show) or, when flagged
conditional, in the effect columns marked `[Not on tooltip]`. What is left in
`unlisted_properties` is tuning constants and enhanced-variant numbers, not
stats of the shop item.

**Investment.** The bonus you hold once you have spent that many souls in a
shop category: weapon damage %, health %, or spirit power.

**Progression.** What each soul threshold grants (a boon, an ability unlock,
an ability point) with running totals. Multiply a hero's per-boon columns by
`total_boons` to get their stats at a given soul count.

**Units.** Health, resists, damage and soul reward for objectives, troopers and
neutral camp creeps, with camp spawn timers. Names the files do not give (Base
Guardian, Mid Boss, the camp sizes) are written in `src/world.py`.

**Rules.** A few global numbers (objective bounties, how kill souls are shared,
Rejuvenator duration and revive). `source_field` is the name in the game files; the
plain-English reading in `rule` is mine.

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
| `knowledge/README.md` | Index and how to read it |
| `knowledge/mechanics/*.md` | One file per mechanic (Mid Boss and Rejuvenator, souls, troopers, objectives, neutral camps, urn, shop, melee, movement, damage rules, healing, status effects, respawn). Each has the game's own text, the current numbers in the files, and the patch history newest first |
| `knowledge/history/heroes.md`, `items.md` | Every patch-note line per hero and per item |
| `knowledge/game_text.md` | The game's tutorial pages, stat descriptions and HUD hints |
| `knowledge/patch_notes.csv` | Every patch-note line, for searching |

Everything in it is quoted from a source, not written by the tool. It does not
include deadlock.wiki: the wiki blocks automated access. Topic files are built
by keyword match, so they can miss a line or include a passing mention.

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
