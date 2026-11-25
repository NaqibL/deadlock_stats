# Knowledge base

Companion to the reference sheet in `output/`. The sheet has the numbers; this explains how the mechanics around them work, in the words of the game and of Valve's patch notes.

- Game build: 6868
- Patch notes: 139 updates, 2024-05-03 to 2026-11-04, 10080 lines
- Source: https://github.com/deadlock-wiki/deadlock-data (game text, game data, patch notes)

## Read this first

[settled.md](settled.md) answers the questions that the numbers alone leave open: what ambiguous fields mean, which values in the files are leftovers, where the files and the patch notes disagree, and what still needs an in-game test. It is hand-written and every patch-note quote in it is checked against `patch_notes.csv` when the knowledge base is built.

## Which source wins

1. The game files (the sheet in `output/`, and the number tables in each mechanics file) are the current build. For any number, they win.
2. Patch notes explain how a mechanic works and what a field means, but they do not record every change: dozens of current values differ from the newest note that mentions them. Use notes for meaning, not for numbers.
3. The game's own tutorial text is the weakest source. Several strings describe older versions of a mechanic.
4. A field in the files is not proof the game uses it. Some are leftovers from retired designs.

## How to use it

- Start with the mechanic's file under `mechanics/`. Each has three parts: what the game's own text says, the current numbers in the files, and the patch history.
- The current numbers are fact for this build. The patch history says how a mechanic works, but only as of each line's date; a later line can replace it. Where the two disagree, the current numbers win.
- Field names in the number tables are the game's own. Their meaning is not always stated anywhere; the patch history is usually what explains them.
- `history/heroes.md` and `history/items.md` hold every patch line per hero and item.
- `patch_notes.csv` is every line, for searching.

## Limits

- Nothing here is from deadlock.wiki. The wiki blocks automated access, so its prose is not included.
- Topic files are built by keyword match on patch-note lines, so a file can miss a relevant line that uses other words, and can include a line that only mentions the word in passing.
- Patch notes do not cover everything. A mechanic that has never changed may have no line at all.
- Street Brawl is a separate mode with its own balance. Its patch lines are in `patch_notes.csv` (column `mode`) but are left out of the mechanics and history files.

## Mechanics

| File | Topic | Patch lines |
|---|---|---|
| [mechanics/mid-boss-and-rejuvenator.md](mechanics/mid-boss-and-rejuvenator.md) | Mid Boss and Rejuvenator | 136 |
| [mechanics/souls-and-economy.md](mechanics/souls-and-economy.md) | Souls and the economy | 160 |
| [mechanics/troopers-and-lanes.md](mechanics/troopers-and-lanes.md) | Troopers and lanes | 322 |
| [mechanics/guardians.md](mechanics/guardians.md) | Guardians and Base Guardians | 130 |
| [mechanics/walkers.md](mechanics/walkers.md) | Walkers | 131 |
| [mechanics/shrines-and-patron.md](mechanics/shrines-and-patron.md) | Shrines and the Patron | 67 |
| [mechanics/neutral-camps.md](mechanics/neutral-camps.md) | Neutral camps, vaults and Sinner's Sacrifice | 105 |
| [mechanics/soul-urn.md](mechanics/soul-urn.md) | Soul Urn | 163 |
| [mechanics/unstable-rift.md](mechanics/unstable-rift.md) | Unstable Rift | 21 |
| [mechanics/breakables-and-powerups.md](mechanics/breakables-and-powerups.md) | Crates, golden statues and powerups | 112 |
| [mechanics/boons-and-ability-points.md](mechanics/boons-and-ability-points.md) | Boons, levels and ability points | 46 |
| [mechanics/shop-and-investment.md](mechanics/shop-and-investment.md) | Shop, item slots and investment bonuses | 98 |
| [mechanics/melee-and-parry.md](mechanics/melee-and-parry.md) | Melee and parry | 101 |
| [mechanics/movement.md](mechanics/movement.md) | Movement and stamina | 168 |
| [mechanics/damage-rules.md](mechanics/damage-rules.md) | Damage rules: headshots, falloff, resists, stacking | 215 |
| [mechanics/healing-and-lifesteal.md](mechanics/healing-and-lifesteal.md) | Healing, regen, lifesteal and heal reduction | 208 |
| [mechanics/status-effects.md](mechanics/status-effects.md) | Status effects and resistance to them | 177 |
| [mechanics/respawn-and-death.md](mechanics/respawn-and-death.md) | Respawn timers and death | 46 |
