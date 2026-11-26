# Settled questions

Read this before explaining any mechanic. It records what three audits of the sheet and knowledge base found: what ambiguous numbers mean, which values in the game files are leftovers, where the files and the patch notes disagree, and what only an in-game test can answer.

This file is hand-written. Every line of the form `DATE: "text"` is a quote from Valve's patch notes and is checked against `patch_notes.csv` whenever `python kb.py` runs. Game-text quotes give their string key. "Files" means the game data the sheet is built from; "server settings" means `convars.json` in the same source.

Each entry carries one status:

- **Settled**: the sources answer it.
- **Files and notes differ**: the current files hold one number and the newest patch note another. The sheet shows the files. Patch notes do not record every change (see the first entry), so the files are probably right, but nothing proves it.
- **Inferred**: no source states it; the reading comes from field names or arithmetic and is labelled as such.
- **Open**: nothing in the sources. An in-game test is given.

## How far to trust each source

**Patch notes lag the game files.** Status: Settled. The sheet is built from the files of the current build; the notes end earlier and skip changes. Leech is the clearest case: the files have had 30% lifesteal since build 6826 (30 October 2026), and the newest note says 28.

- 2026-09-16: "Leech: Bullet and Spirit Lifesteal increased from 25% to 28%"

Other current values that differ from the newest note mentioning them include Golden Goose Egg's damage penalty, Cursed Relic's damage penalty, Toxic Bullets' and Decay's healing reduction, Armor Piercing Rounds' proc chance, Radiant Regeneration's spirit scaling, Pocket's bullet damage growth and Frozen Shelter's cooldown. Use notes to learn what a mechanic is; use the sheet for its numbers. A rule number that exists only in a note (the headshot multiplier, parry values) is "as of its date".

**The game's tutorial text is partly out of date.** Status: Settled. These strings describe older versions:

- `Citadel_Player_Level_AbilityPoints` ("1 Ability Point gained at levels 2, 3, 5, 7, and each level after") does not match the current boon table. `Citadel_Player_Level_AP_Rewards_UnlockNote` ("Abilities unlock at Boons 0, 2, 4 and 7") does.
- `guide_advanced_parry_desc` says a parried enemy "will receive increased melee damage"; since 2025 the bonus applies to all damage (see Parry).
- `guide_upgrades_yellow_orbs_desc` describes soul orbs from hero deaths; hero kills no longer spawn orbs (see Hero kills).
- `guide_the_map_midboss_desc` ("immediate respawns on their next deaths") is roughly right for the current Rejuvenator but predates its rework.

**A field in the files is not proof the game uses it.** Status: Settled, by example. `RejuvParams.TrooperHealthMult` and `PlayerRespawnMult` are still in the files after the mechanic they served was removed (see Rejuvenator). The sheet now counts as a stat only what the in-game tooltip shows.

**Street Brawl is a separate mode.** Status: Settled. It has its own balance; its patch lines are tagged in `patch_notes.csv` (`mode`) and left out of the mechanics and history files. Street Brawl-only items are not in the sheet.

## Souls and the economy

**Starting souls.** Status: Settled. 600 (server setting `citadel_player_starting_gold`).

- 2025-11-21: "Starting souls count increased from 400 to 600"

Whether those 600 count toward the boon thresholds in `progression.csv` is **Open**. Test: at match start, before earning anything, read your boon count; 600 souls would be boon 2 if they count.

**Hero kills.** Status: Settled. The bounty is 200 souls at 0:00 rising to 2,200 at 40 minutes, plus 125 for each player's first kill, with a 10-second assist window (server settings, matching the notes). Souls go straight to the killer and assisters.

- 2026-06-30: "Base kill bounty reduced from 250 to 200 (max is still 2200 at 40m)"
- 2026-06-30: "First blood bounty reduced from 150 to 125"
- 2025-06-17: "Killing heroes no longer spawns orbs, instead the souls are directly awarded to the killer and assisters"

**Hero kill share rows in `rules.csv`** (1.25 / 0.575 / 0.283 / 0.175 / 0.11 / 0.083). Status: Settled. The index is the number of players in the kill; the value is the average share of the bounty per participant, so the total paid is N times it: 125%, 115%, 85%, 70%, 55%, 50%. The killer gets more than each assister (server setting `citadel_player_gold_killer_to_assist_ratio` is 2.2; the notes give no current number).

- 2025-11-23: "Hero kill bounty split efficiency for 1/2/3/4/5/6 players changed from 100/100/90/84/65/72% to 100/100/85/70/55/50%"
- 2025-12-16: "Increased kill bounty for solo kills (1 attacker in the kill) by 25%, and by 15% for duo kills"

**Trooper kill share rows** (1 / 0.54 / 0.36 / 0.25 / 0.2 / 0.16). Status: Settled. Each nearby player gets that fraction of the trooper bounty (two players get 54% each). The same rules apply in lane and after. Whether neutral camps use this table is **Open**.

- 2025-11-21: "Trooper bounty split ratios updated from 1/0.65/0.28/0.15/0.12/0.08 to 1/0.54/0.36/0.25/0.2/0.16"
- 2025-04-17: "Soul Orbs no longer have special duplication rules before 8 minutes. Soul splitting rules are now the same before 8 minutes as afterwards."

**Trooper souls.** Status: Settled. 100 souls plus 2 per minute (server settings, matching the notes). Half flies out as an orb the enemy can shoot to deny; the other half drops as a ground orb you collect by coming within 18m. Super troopers give 15% less. Whether "100" is per trooper or per wave is **Open** (nothing states it).

- 2026-06-30: "Trooper bounty rescaled from 116 + 1.16/m to 100 + 2/m (less before 20m, more after)"
- 2026-06-30: "Trooper bounty ratio in the deniable flying orb increased from 40% to 50%"
- 2026-03-10: "Super troopers (when a lane shrine is down) now have 15% less bounty"

**Objective bounties** (Guardian 1,375, Walker 3,675, Base Guardians 1,000, Shrines 2,000). Status: Settled. These are team totals: 25% goes to nearby players (including anyone who damaged it within 20 seconds), and the rest is split among all six. Whether the Base Guardian and Shrine numbers are per unit or per pair is **Open**.

- 2026-09-16: "Share for objectives bounty to nearby heroes reduced from 30% to 25% (the remaining gets split between all 6 players)"
- 2026-09-16: "Guardian bounty increased by 10%"
- 2026-03-06: "Shrines bounty increased from 0 to 2000"

**Comeback mechanics.** Status: Inferred / Open. Bounties in the sheet are base values. Kills on richer heroes pay extra, and part of that extra is redirected to the team's two poorest players. No source gives the formula (a server setting `citadel_player_gold_comeback_multiplier` of 2.268 exists with no explanation).

- 2026-09-16: "Slightly reduced comeback bounties in general (this is in addition to the above change)"

**Unsecured souls** (the game UI calls them "Haunted Souls", `Citadel_Hero_Stats_Unsecured`). Status: Inferred. Some souls arrive unsecured, convert to secured over time, and drop as a bag on death if you hold more than 50 + 5 per minute; the bag is claimed with a heavy melee. The full list of what grants unsecured souls is not in the sources, and the drain rate in the notes (0.5% + 1.6) differs from the server settings (0.375% + 1.2).

- 2026-06-30: "Minimum unsecured souls allowed to drop reduced from 150 to 50 + 5/min"
- 2025-10-02: "Dropped Unsecured soul bags now require a Heavy Melee to secure rather than standing ontop of them"

## Boons, ability points and the shop

**What a boon is.** Status: Settled. `level` in `progression.csv` is the game's "Boon N". Boon 0 is the start: one ability unlock, no stats. Every boon from 1 to 35 gives the hero's per-boon stats plus either an ability point or an ability unlock. Boon 35 is the last. Ability points come only from this table.

- 2026-06-30: "Reworked Boon reward table"
- 2025-11-21: "Soul Urn no longer grants +1 AP to the person dropping it off"

**Ability upgrade costs.** Status: Inferred. The three upgrade tiers cost 1, 2 and 5 ability points. No source states this; it fits exactly, since 4 abilities x (1 + 2 + 5) = 32 and the table grants 32 points. Test: read the cost on the three upgrade pips in the sandbox.

- 2025-11-21: "Added two levels at 47k and 49k to let you get all ability upgrades"

**Ability upgrades are additive.** Status: Settled. Each value in `upgrade_1..3`, including "+N x spirit power scaling", is added to the base value or coefficient.

- 2026-09-16: "Warden: Willpower T3 spirit scaling reduced from +2.7 to +2.1"

**Item slots.** Status: Settled. 9 base slots plus up to 3 flex slots, one per enemy Walker destroyed. Older lines tying flex slots to Guardians, Shrines or the Patron are superseded. A cap of four active items has only a 2024 line behind it.

- 2025-11-21: "Base slot count increased from 8 to 9 and Flex slot count reduced from 4 to 3. One is given for each Walker killed."

**Selling.** Status: Settled. An item sells for half its purchase price (server setting `citadel_item_sell_price_ratio` 0.5; game text `Citadel_Shop_Destroy_Item_Confirm` says "half the purchase price"). A purchase can be undone until the item is used. Whether selling lowers investment totals is **Open**.

- 2024-08-15: "Using an active item or ability removes the undo option for the item/AP"

**Upgrading from a component.** Status: Open. The component is consumed and its slot freed. Whether you pay the full `cost` or the difference is stated nowhere. Test: own a component, hover its upgrade, read the price.

**Investment bonuses.** Status: Settled for units and values. All 33 rows match the notes. Weapon is a percentage of gun and melee damage (`Citadel_Hero_Stats_Tooltip_WeaponPower`: "Total Bonus to your Gun and Melee Damage"); vitality is a percentage of base health; spirit is flat spirit power. `bonus` is the cumulative total held at that threshold, not an increment.

- 2026-03-21: "Vitality investment tree bonus reverted back to % base hp increase rather than raw constant bonus (back to how it was set up in december)"
- 2026-05-22: "Spirit Investment Bonus now has a 6.4k line, changed from 4.8k/7.2k/9.6k/16k to 4.8k/6.4k/8k/11.2k/16k with bonuses from 38/48/57/66 to 38/45/52/59/66"

**What "base health" means for the vitality bonus.** Status: Inferred. The game calls boon health "Base Health" (`Citadel_Player_Level_BaseHealth`) and so do the notes, so the bonus most likely applies to starting health plus boon health, and not to item health ("Bonus Health"). Test at a high boon count: buy 800 souls of Vitality and compare the gain with 9% of starting health versus 9% of starting plus boon health.

- 2026-04-30: "Base health per boon reduced by 7"

**Imbue and active items.** Status: Inferred. An imbue item is applied to one ability chosen at purchase, so its bonus affects that ability only (the sheet files these as conditional). `activation` "Active" items take an active slot. A `cooldown` on a passive item is its proc cooldown.

## Combat rules

**Spirit power.** Status: Settled. It does nothing by itself. It acts only through coefficients: value = base + coefficient x spirit power, on abilities, items and the few hero stats in `spirit_scaling`. "Spirit Amp" is a different stat, a percentage multiplier on spirit damage.

- Game text `StatDesc_SpiritPowerDesc`: "Spirit Power - Increases the effectiveness of your Abilities and Items"

**Headshots.** Status: Settled as of its date. The base headshot multiplier is 1.65x; it is not in the files the sheet reads. `headshot_bonus_scale_pct` on a hero is their outgoing "Crit Bonus Scale": 0 is normal, negative means their headshots gain that much less. `headshot_damage_taken_reduction_pct` is a different stat, damage taken from headshots (Seven 55, Mo & Krill 20). `can_headshot` is FALSE for Paige and Deadman Danny in the files with no patch line. Whether a negative scale reduces only the bonus part or the whole multiplier is **Open**.

- 2025-11-21: "Headshot multiplier reduced from 1.8x to 1.65x"
- 2026-07-09: "Doorman: Crit scaling reduced from -25% to -30%"
- 2026-05-22: "Seven: Crit reduction increased from 35% to 55%"

**Damage falloff.** Status: Inferred. `falloff_start` and `falloff_end` are metres and match the notes. `falloff_end_damage_scale` is the files' FalloffEndScale: read as the fraction of damage left at and beyond the end range (0.1 = 10%). No source states the curve between the two.

- 2026-09-16: "Lash: Gun falloff range reduced from 18m->54m to 16m->48m"

**Weapon damage.** Status: Open on the formula. "Weapon Damage" is a percentage on gun and melee damage (`StatDesc_WeaponDamageDesc`). Whether it multiplies base bullet damage or base plus boon growth, whether several sources add, and whether melee takes all of it, are stated nowhere. Test: with boons and one +X% item, compare the shop's bullet damage with (base + growth) x (1 + X).

**Resists.** Status: Open on stacking of bonuses; Inferred for reductions. No source says how several bullet or spirit resist bonuses combine or whether there is a cap, so do not sum the resist columns as if additive without testing (buy two resist items and compare the stat panel with the sum). Resist can go negative. The same resist-reduction debuff from several sources halves each time; some debuffs do not stack at all.

- 2025-12-16: "Fixed a bug causing AP Rounds to reduce damage on targets with negative resist"
- 2024-12-06: "Crippling Headshot: The headshot debuff will now stack from different sources, diminishingly (24%, 12%, 6%, etc)"
- 2026-05-22: "Total Damage Reduction debuffs now stack diminishingly rather than additively (Inhibitor, Fire Scarabs, etc)"

**Stats that stack with diminishing returns.** Status: Settled that they diminish; the formulas are not published. Ability cooldown reduction, ability range, ability duration, move speed bonuses, lifesteal and fire-rate slows all diminish. Bullet velocity adds.

- 2024-07-18: "Cooldown reduction now stacks diminishingly"
- 2024-12-06: "Ability Range stat now has diminishing stacking"
- 2024-12-06: "Ability Duration stat now has diminishing stacking"
- 2025-12-16: "Move Speed bonuses now stack diminishingly"
- 2024-10-10: "Bullet and Spirit Lifesteal now stack diminishingly"
- 2024-09-26: "Fire Rate slows now stack diminishingly"
- 2026-05-22: "Bullet Velocity now stacks additively rather than diminishingly"

**Cooldown reduction.** Status: Settled. "Ability Cooldown Reduction" affects abilities only; item cooldowns need "Item Cooldown Reduction" (Transcendent Cooldown has both). The sheet column is `ability_cooldown_reduction_pct`.

- 2025-07-04: "Cooldown Reduction stat is now renamed to Ability Cooldown Reduction and no longer affects items (all existing CDR is now Ability Cooldown Reduction)"

**Fire rate.** Status: Settled. `fire_rate` on heroes is bullets per second. Total fire rate cannot go below -50%. McGinnis and Victor spin up: `fire_rate_max_spin` is their top rate and the files' DPS figure uses it.

- 2024-12-06: "Fire Rate now has a minimum final value of -50%"

**Lifesteal and healing reduction.** Status: Inferred. Lifesteal is weaker against creeps. `bullet_lifesteal_effectiveness` below 1 (Rat King 0.75) scales a hero's lifesteal. Whether "Incoming Healing" reduction also cuts lifesteal, and what Leech's "reduces healing reduction" amounts to, are **Open** (the files hold no number for Leech's effect).

- 2025-07-04: "Bullet Lifesteal vs creeps increased from 50% to 60%"
- 2025-07-04: "Spirit Lifesteal vs creeps increased from 33% to 40%"

**Regen.** Status: Inferred. `health_regen` is health per second at all times. `out_of_combat_regen` is extra regen while out of combat, meaning no damage dealt or taken for a few seconds.

- 2025-12-17: "Time delay before sprint starts working after hero/neutral interaction reduced from 4s to 3s"

**Movement.** Status: Settled. Speeds are metres per second. `sprint_speed` is a bonus added to `move_speed` while out of combat. `move_speed_while_shooting_scale` 0.75 means you move at 75% speed while firing. `stamina_recovery_seconds` is seconds per stamina point.

- 2025-07-29: "Movespeed Slow when shooting reduced from -30% to -25%"

**Parry and melee.** Status: Settled as of the dates. A parried enemy takes 25% more damage of all types. Parry cooldown 4.5s, active window 0.75s. Melee damage grows per boon (the hero per-boon columns) and weapon damage affects melee, at an unstated rate.

- 2025-08-01: "Parry bonus damage reduced from 30% to 25%"
- 2025-07-29: "Parry bonus damage is no longer melee specific, now affects all damage types (reduced from 35% to 30%)"
- 2024-10-24: "Parry cooldown reduced from 5s to 4.5s"

**Debuff resist.** Status: Inferred. It shortens the duration of negative effects on you, with exceptions (a parry stun is not shortened). How it stacks is **Open**.

- 2025-07-29: "Parried stun duration is no longer reduced by debuff resistance"

## Reading the hero, ability and item tables

**`damage_per_shot` for multi-pellet guns.** Status: Inferred. Baba and Drifter fire three pellets but the files flag them as hitting a target once per shot, and their DPS figure uses one pellet; the sheet's `damage_per_shot` follows that. Test: shoot a dummy point blank and read the damage number.

**Hero `spirit_scaling`.** Status: Settled for most; two differ from the notes. Values are per point of spirit power (Haze's clip, Grey Talon's bullet damage, Yamato, Paige match the notes). Wraith's sprint (files 0.05) and Baba's spirit resist (files 0.05) are a tenth of the figure the notes use, so the notes may quote them in different units.

- 2025-12-16: "Wraith: Sprint speed spirit power scaling reduced from 0.6 to 0.5"
- 2025-09-04: "Grey Talon: Bullet damage growth based on Spirit Power increased from 0.07 to 0.08"

**Ability `other_scaling` types.** Status: Inferred. "per light melee damage" and "per heavy melee damage" multiply the hero's melee damage. "per boon" is added per boon held. "per weapon power" on Paradox's Kinetic Carbine is a percentage of bullet damage (125 means 125%). "per weapon damage %" is presumably per 1% of bonus weapon damage; no source states the unit.

- 2026-04-10: "Bebop: Grapple Arm now deals light melee damage (0.7 scaling)"
- 2026-03-06: "Paradox: Kinetic Carbine base damage scale increased from 100% to 125%"

**Ability numbers come from the tooltip card.** Status: Settled as sheet policy. The main columns and `spirit_scaling` hold only what the in-game card shows. Values the files hold but the card does not (Billy's Chain Gang DPS, Kelvin's Arctic Beam heal) are in `internal_properties`: some are tuning, some unlock with upgrades, some are leftovers. Do not treat them as live without checking.

**Item effect buckets.** Status: Settled as sheet policy. Innate columns hold what the buyer always has. `conditional_effects` holds procs, stacks, thresholds, on-use effects and imbue bonuses. `enemy_effects` holds what is applied to enemies. The split is by tooltip section and flags, corrected by tooltip wording for the items where that was wrong (Cheat Death and Metal Skin penalties are on the user; Inhibitor and Silencer reductions are on the target).

**Signs in item effects.** Status: Settled. A "Slow" label carries a positive magnitude ("Move Speed Slow: 24%", "Fire Rate Slow: 15%"). Resist reductions, healing reductions and damage penalties are negative.

**`stats_not_on_tooltip`.** Status: Open, item by item. These values are in the files and marked as stats the game provides, but no tooltip section shows them (Refresher's 14% spirit and 15% bullet resist, Witchmail's 7% cooldown reduction, Glass Cannon's slow). They are not counted in the stat columns. The patch history suggests some are leftovers: Glass Cannon's slow came from a component it no longer has.

- 2024-11-21: "Glass Cannon: Now requires Slowing Bullets and grants the slow passive"

**"Ability Range" and radius.** Status: Settled. One stat covers both (`StatDesc_AbilityRangeDesc`: "Increases range and radius of your Abilities and Items"). The files store the radius half as a second property with the same number; the sheet lists it once.

## The map

**Mid Boss.** Status: Settled for structure; files and notes differ on numbers. It is present from 0:00 and respawns 7 minutes after the first kill, 6 after the second, 5 thereafter. Its health is fixed when it spawns: base plus gain per minute of game time. It soaks a flat 35 damage per second, growing 5 per minute, has 15% bullet resist, no spirit resist and 35% debuff resist. Files say 15,600 health and 234 per minute; the newest notes say 13,000 and 230.

- 2026-05-22: "Midboss now starts spawned at the beginning of the game"
- 2024-10-24: "Mid Boss respawn timer decreases with subsequent boss kills, from 7 to 7/6/5 minutes"
- 2025-10-02: "Mid Boss damage resistance per second reduced from 50 + 7/min to 35 + 5/min"
- 2026-03-06: "Mid Boss base HP increased from 11900 to 13000"
- 2025-07-29: "Objectives no longer have 20-25% Spirit Resistance"

**Mid Boss bounty.** Status: Files and notes differ. The notes say 3,000 + 50 per minute split across the team, plus 2 permanent buffs per player. The server settings say 1,500 + 25 per minute. Not in the sheet for that reason. Test: kill it at a known minute and add up the team's soul gain.

- 2026-03-06: "Mid Boss base bounty increased from 2000 to 3000"
- 2025-11-21: "Team that kills Mid Boss gets +2 permanent buffs for each player"

**Rejuvenator.** Status: Settled. Killing the Mid Boss drops one crystal. Each heavy melee hit on it gives the team one credit, up to 3. Everyone on the team gets the buff for 180 seconds; when a teammate dies they respawn in place after 3 seconds at full health and one credit is spent. It gives no stat bonuses, does not buff troopers and does not shorten ordinary respawns: `TrooperHealthMult` and `PlayerRespawnMult` in the files are leftovers. "Rejuvenator drop count 3" in `rules.csv` is the credit count. Files say the crystal takes 7.5s to drop; the newest note says 6s.

- 2025-08-08: "Rejuv now drops 1 crystal again, with each heavy melee hit granting a credit to the team (up to 3 for first midboss, and 4 for subsequent ones)."
- 2025-10-02: "2nd Midboss rejuv credits reduced from 4 to 3"
- 2026-06-30: "Rejuv buff duration reduced from 4 minutes to 3"
- 2025-11-21: "Rejuv buff no longer grants +10% Max HP, +15% Fire Rate and +15% Spirit Damage Amp"
- 2026-03-06: "Rejuv drop duration reduced from 7s to 6s"

**Guardians.** Status: Settled for health and bounty; Inferred for damage. Health 5,500. `dps_vs_players` 116 and `dps_vs_troopers` 35 are the live damage figures (both guardian types share them); the generic weapon block is left out. On top of the flat 10% bullet resist there is a resist that decays over the match, from +50% to -50% over 12 minutes, which is in the notes only.

- 2025-11-23: "Guardians HP increased from 4250 to 5500"
- 2026-05-22: "Guardians scaling resistance from +75%->-50% over 12 minutes to +50%->-50% (takes more damage early)"

**Walkers.** Status: Settled for health; files and notes differ on resists. Health is 6,000, then 9,000 and 12,000 for the Walkers that remain as others die. Decaying resist from +65% to -65% over 18 minutes (notes only). They gain resist with more attackers nearby and are immune to bullets from long range. Files say 35% bullet resist; the only note says +15%.

- 2026-03-06: "Walkers Health rescaled from 6800/9350/11900 to 6000/9000/12000"
- 2026-03-06: "Walkers armor decay rescaled from "+75% -> -50%" to "+65% -> -65%", from over 20min to over 18min"

**Shrines.** Status: Settled. 5,000 health for the first, 10,000 for the second once one has died; 20% bullet resist; invulnerable until a pair of Base Guardians is destroyed.

- 2026-03-06: "Shrine is now easier to kill for the first one and harder for the second. HP from 8100 to 5000/10000 (HP updates after the first one dies, like Walkers)"
- 2026-05-22: "Shrines are now invulnerable until one pair of Base Guardians are destroyed"

**Patron.** Status: Files and notes differ on health. Files: 12,000 in each phase, growing 250 per minute from minute 20. The last note giving its health is from 2024 (7,500 and 13,500). The weakened Patron takes 50% less damage with one defender in the pit and none with two or more.

- 2025-12-17: "Weakened Patron now gains 50% damage reduction if one defender is in the pit and 100% if two or more are (defenders must be in pit for at least 2s for reduction to kick in)"

**Backdoor protection.** Status: Inferred. With no friendly troopers near an objective, player damage to it is cut by 65% and it regenerates 65 health per second (Patron 75). Read from field names and a 2024 description.

- 2026-05-22: "Backdoor removal linger duration reduced from 20s to 14s"

**Troopers.** Status: Settled. Health 300 / 400 / 350 (normal, melee, medic), +50% after 35 minutes. Waves every 30 seconds, 25 from minute 20, 20 from minute 35 (server settings, matching the notes). The sheet's `dps_vs_players` 28 and `dps_vs_troopers` 35 are the files' per-target figures. Main-mode troopers' spirit resist is **Open**: the last line is from 2024 and no field holds it.

- 2025-11-21: "After 35 minutes all troopers gain +50% HP."
- 2026-03-06: "Trooper wave interval increased from every 25s to every 20s starting at 35 minutes"
- 2026-03-06: "Medic Troopers DPS grows by 3% per minute"

**Neutral camps.** Status: Settled for timers and resists. First spawns at 2, 5 and 8 minutes for small, medium and large. Listed health, damage and reward are per creep at minute 0; health grows 2.1% per minute and damage 0.5%. Spirit resist 45 / 45 / 55 matches the notes. The large camp's respawn is 335s in the files where the notes imply 420. `soul_reward_growth_pct_per_minute` 1.08 is the files' field; whether it compounds is **Open**. Whether `respawn_seconds` counts from the clear or from the spawn is **Open**.

- 2026-01-20: "Neutral respawn times, hp, and bounty reduced by 30% (sinner's sacrifice unaffected)"
- 2025-12-16: "Neutral HP growth increased from 0.5%/min to 2.1% (less HP before ~15 minutes, more afterwards)"
- 2026-03-21: "Small neutrals spirit resist increased from 35% to 45%"

**Sinner's Sacrifice.** Status: Inferred. Melee only; it returns 80 damage per hit; first spawn 8 minutes, then every 5. Hitting during the flashing lights gives bonuses, and a timed heavy melee finish gives 4 permanent buffs. Whether the 155 soul reward is the total or per stage is **Open**.

- 2025-11-21: "Sinner's Sacrifice: Return damage increased from 60 to 80"
- 2025-03-16: "Sinner's Sacrifice initial spawn time reduced from 10 min to 8 min (respawn rate is still 5 min)"

**Soul Urn.** Status: Settled. Notes and server settings agree. It spawns at 10 minutes and every 5 after, at one end of the map, to be carried to the other. The runner gets 250 + 70 per minute and 4 permanent buffs. The reward starts decaying 45 seconds after pickup and is gone 45 seconds later. Lines from before 2026-06-30 describe older rules.

- 2026-06-30: "Urn bounty when deposited is worth 250 + 70/min for just the urn runner. Still has the comeback bounty component. Upon deposit all of the souls are released as orbs into the air (if another ally secures the orbs, they share the bounty with the urn runner)."
- 2026-06-30: "Urn runner gets +4 permanent buffs on deposit"
- 2026-06-30: "Urn bounty value starts decaying after 45s from being picked up. It drains gradually over another 45s and then the urn is removed when the bounty is empty."

**Unstable Rift.** Status: Settled for timing; Inferred for reward. A separate objective since 2026-06-30. First at about 12 minutes (plus or minus one), then every 7, in a random lane, with a 20-second warning. The securing team gets a wave of Rift Troopers. The soul reward (1,260 + 222 per minute) is in the server settings only.

- 2026-06-30: "Unstable Rift spawn interval increased from every 6 minutes to every 7 minutes"
- 2026-07-09: "Unstable Rift warning time reduced from 25s to 20s"
- 2026-06-30: "Rift Troopers drop no souls when killed"

**Powerups (the bridge buffs).** Status: Files and notes differ on timing. Files: first at 5 minutes and every 5 after, strength growing from minute 5 to minute 40, lasting 160 seconds, claimed with a heavy melee. The notes say 10 minutes, but they are from 2024 and visibly missed later changes. See `powerups.csv`.

- 2024-11-21: "Powerups now require a heavy melee to claim (art visuals updated)"
- 2024-08-01: "Powerup durations increased from 150s to 160s"

**Permanent buffs (golden statues and other sources).** Status: Settled for most. Three levels, changing at 10 and 30 minutes; see `permanent_buffs.csv`. The files' values match the in-game labels. Sources: golden statues, the Mid Boss (2 per player), the Soul Urn (4 to the runner), Sinner's Sacrifice (4 for a timed finish).

- 2026-06-11: "Breakables health permanent bonus reduced from 15/25/35 to 15/20/30 for level 1/2/3"
- 2024-10-15: "T3 Golden Statues spawn time moved from 25 min to 30 min"

**Respawn time.** Status: Settled. 8 seconds until 5 minutes, rising to 38s at 20 minutes, 70s at 30 and 85s at 40 (server settings, matching the notes; straight-line growth between points is inferred). Add 10s when not killed by a hero, and 6 to 22s when you die much richer than the enemy average.

- 2026-09-16: "Respawn Time at 20 minutes increased from 35s to 38s (does not affect the max values later on, just a little higher earlier)"
- 2026-01-20: "Respawn time at 30 minutes reduced from 75s to 70s"
- 2025-09-04: "Dying to a non-player (when there is no bounty/assists) now increases the respawn time for that death by 10 seconds"

## Still open: needs an in-game test

Nothing in the files, server settings, patch notes or game text answers these.

1. **Weapon damage formula.** Does +X% multiply base bullet damage or base plus boon growth; do sources add; how much reaches melee? Test: shop bullet damage readout with and without one item, at a known boon count.
2. **Resist stacking.** Do two resist items add? Is there a cap? Test: stat panel total versus the sum.
3. **Base health for the vitality bonus.** Starting health only, or starting plus boons? Test at a high boon count.
4. **Upgrade price.** Full cost or the difference when you own the component? Test: hover the upgrade.
5. **Starting souls and boons.** Do the 600 starting souls count toward boon thresholds? Test: boon count at 0:00.
6. **Ability upgrade costs.** 1, 2 and 5 points fits the totals but is not stated. Test: read the pips.
7. **Mid Boss bounty.** 3,000 + 50 per minute (notes) or 1,500 + 25 (server settings)? Test: team soul gain on the kill.
8. **Off-tooltip item stats.** Are Refresher's resists, Witchmail's cooldown reduction and the others in `stats_not_on_tooltip` live? Test: stat panel before and after buying.
9. **Hit-once pellets.** Do Baba's and Drifter's three pellets hit one target once? Test: damage number at point blank.
10. **Neutral reward growth.** Does 1.08% per minute compound, and does the trooper share table apply to camps? Test: one creep's reward at minutes 2 and 22.
11. **Headshot scale.** Does a negative hero scale cut the bonus or the whole multiplier? Test: Vyper's headshot against a body shot.
12. **Trooper bounty unit.** Is 100 + 2 per minute per trooper or per wave? Test: souls from one last hit.
13. **Sinner's Sacrifice reward.** Is 155 the total? Test: souls from a full clear.
14. **Selling and investment.** Does selling an item lower the investment total? Test: watch the bar when selling.
