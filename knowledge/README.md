# Knowledge base

Companion to the reference sheet in `output/`. The sheet has the numbers; this explains how the mechanics around them work, in the words of the game and of Valve's patch notes.

- Game build: 6868
- Patch notes: 139 updates, 2024-05-03 to 2026-11-04, 10114 lines
- Source: https://github.com/deadlock-wiki/deadlock-data (game text, game data, patch notes)

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

## Mechanics

| File | Topic | Patch lines |
|---|---|---|
| [mechanics/mid-boss-and-rejuvenator.md](mechanics/mid-boss-and-rejuvenator.md) | Mid Boss and Rejuvenator | 96 |
| [mechanics/souls-and-economy.md](mechanics/souls-and-economy.md) | Souls and the economy | 160 |
| [mechanics/troopers-and-lanes.md](mechanics/troopers-and-lanes.md) | Troopers and lanes | 328 |
| [mechanics/guardians.md](mechanics/guardians.md) | Guardians and Base Guardians | 109 |
| [mechanics/walkers.md](mechanics/walkers.md) | Walkers | 107 |
| [mechanics/shrines-and-patron.md](mechanics/shrines-and-patron.md) | Shrines and the Patron | 67 |
| [mechanics/neutral-camps.md](mechanics/neutral-camps.md) | Neutral camps, vaults and Sinner's Sacrifice | 105 |
| [mechanics/soul-urn.md](mechanics/soul-urn.md) | Soul Urn | 164 |
| [mechanics/breakables-and-powerups.md](mechanics/breakables-and-powerups.md) | Crates, golden statues and powerups | 112 |
| [mechanics/boons-and-ability-points.md](mechanics/boons-and-ability-points.md) | Boons, levels and ability points | 47 |
| [mechanics/shop-and-investment.md](mechanics/shop-and-investment.md) | Shop, item slots and investment bonuses | 101 |
| [mechanics/melee-and-parry.md](mechanics/melee-and-parry.md) | Melee and parry | 102 |
| [mechanics/movement.md](mechanics/movement.md) | Movement and stamina | 169 |
| [mechanics/damage-rules.md](mechanics/damage-rules.md) | Damage rules: headshots, falloff, resists, stacking | 219 |
| [mechanics/healing-and-lifesteal.md](mechanics/healing-and-lifesteal.md) | Healing, regen, lifesteal and heal reduction | 214 |
| [mechanics/status-effects.md](mechanics/status-effects.md) | Status effects and resistance to them | 181 |
| [mechanics/respawn-and-death.md](mechanics/respawn-and-death.md) | Respawn timers and death | 46 |
