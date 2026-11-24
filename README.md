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
| `output/deadlock.xlsx` | The sheet: Heroes, Abilities, Items and Meta tabs |
| `output/heroes.csv`, `abilities.csv`, `items.csv`, `meta.csv` | The same tables as CSV |
| `output/CHANGELOG.md` | What changed in each build: old and new value per entity and field, newest first |
| `output/REPORT.md` | The last build's validation findings, cross-check results and the list of what was filtered out |

Numbers are stored as numbers without units. A blank cell means "not applicable".

## Sources

- **Primary:** [deadlock-wiki/deadlock-data](https://github.com/deadlock-wiki/deadlock-data),
  Deadbot's parse of the game files. Cloned into `.cache/deadlock-data`.
- **Cross-check:** the raw game files in
  [SteamDatabase/GameTracking-Deadlock](https://github.com/SteamDatabase/GameTracking-Deadlock)
  (`heroes.vdata`, `abilities.vdata`, `generic_data.vdata`), parsed independently by `src/kv3.py`.

The Deadlock API assets service (`assets.deadlock-api.com`) was the intended
cross-check, but that hostname had no DNS record when this was built, so the raw
game files are used instead.

## Reading the tables

**Heroes.** `sprint_speed` is the bonus added to `move_speed` while sprinting.
`stamina_recovery_seconds` is the time to regain one stamina.
`damage_per_shot` is `bullet_damage` x `pellets_per_shot`. Distances are metres.

**Abilities.** Four rows per hero (`slot` 4 is the ultimate). A hero with an
alternate form has extra rows for that form's own abilities, marked in `form`.
`damage_spirit_scale` and `dps_spirit_scale` are the spirit power coefficients
for those two properties; `spirit_scaling` lists the coefficient for every
property that scales with spirit power (`TechPower` in the files).
`other_scaling` lists scaling with boons, melee damage and weapon damage.
`other_properties` holds the remaining properties shown on the in-game tooltip,
`internal_properties` the ones the files hold but the tooltip does not show.

**Items.** Effects are split three ways:

- the stat columns and `other_innate_stats`: what the buyer always gets;
- `conditional_effects`: conditional, proc and on-use effects on the buyer;
- `enemy_effects`: effects applied to enemies.

The split comes from the tooltip sections in the source (`Innate` versus
`Passive` / `Active`) and its usage flags. The files flag only a handful of
properties as enemy-applied, so that bucket is completed by property type
(resist reduction, slow), status effect, and property name (damage dealt,
debuff durations, healing reduction). It is an approximation; the rule is
`bucket()` in `src/items.py`. `unlisted_properties` holds values that are in
the files but on no tooltip section, so their meaning is not confirmed.

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

## Scheduling

`.github/workflows/refresh.yml` runs the build weekly and commits `output/` if
it changed.
