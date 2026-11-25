# Boons, levels and ability points

Generated from the game files at build 6868 and Valve's patch notes. Everything below is quoted from a source, not interpreted. Patch notes describe the game as of their date: read newest first, and treat an older line as history once a newer one changes the same thing.

## What the game itself says

- Ability Point (`Citadel_HUD_LevelUpAbilityPointAnnouncement`)
- Ability Unlock (`Citadel_HUD_LevelUpAbilityUnlocksAnnouncement`)
- You've Reached (`Citadel_HUD_LevelUpLocalPlayerMessage`)
- [leveled_up_hero_name] has Reached (`Citadel_HUD_LevelUpSpectatingPlayerMessage`)
- Ultimate Unlocked (`Citadel_HUD_LevelUpUltimateAbilityUnlocked`)
- Boon Received (`Citadel_HUD_LevelUp_Title`)
- A gift from your Patron... (`Citadel_HUD_PatronBoon`)
- Boons Received (`Citadel_Hud_BoonsRecieved`)
- 1 Ability Point gained at levels 2, 3, 5, 7, and each level after (`Citadel_Player_Level_AbilityPoints`)
- Melee Damage (`LevelUpBaseMeleeDamage`)
- Bullet Damage (`LevelUpBaseWeaponDamage`)

## Current numbers in the game files

- No dedicated block for this in the files the sheet reads; see the sheet's tables.

## Patch history (47 lines, newest first)

**2026-07-28** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1839041357039193))

- Doorman: Bullet damage rescaled from 26 + 1.19/boon to 24 + 1.25

**2026-07-09** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1836506165584438))

- Doorman: Bullet damage rescaled from 29.26 + 1.1/boon to 26 + 1.19

**2026-06-30** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1836506165563227))

- Reworked Boon reward table
- Health per boon reduced by 5%

**2026-05-22** ([forum post](https://forums.playdeadlock.com/threads/05-22-2026-update.135477/))

- HP per boon reduced by 3
- [ General ] - Base HP reduced by 10 for all heroes - HP per boon reduced by 3 - Guardians scaling resistance from +75%->-50% over 12 minutes to +50%->-50% (takes more damage early) - Medium neutrals initial spawn time reduced from 6 minutes to 5 minutes - Breakables spawn time increased from 2...

**2026-04-30** ([forum post](https://forums.playdeadlock.com/threads/04-30-2026-update.129989/))

- [ General ] - Base health per boon reduced by 7 - Vitality Investment bonus increased from 8/10/13/17/34/39/44/48/52/56% to 9/12/15/20/38/42/46/50/56/62% - Weapon Investments bonus rescaled from 7/9/13/20/49/60/80/95/115/135% to 9/12/15/18/46/55/70/85/100/115% - Reduced bullet damage growth by...

**2026-03-25** ([forum post](https://forums.playdeadlock.com/threads/03-25-2026-update.121766/))

- Street Brawl: You now have all AP unlocked by round 5

**2025-12-16** ([forum post](https://forums.playdeadlock.com/threads/12-16-2025-update.93983/))

- Fixed a bug causing AP Rounds to reduce damage on targets with negative resist

**2025-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/))

- Reduced all AP damage upgrades by 10%
- Soul Urn no longer grants +1 AP to the person dropping it off
- Casting Buff spirit power increased from 15>40 to 15->65

**2025-10-24** ([forum post](https://forums.playdeadlock.com/threads/10-24-2025-update.87198/))

- Doorman: Bullet damage growth per boon reduced from 1.15 to 1.0

**2025-10-02** ([forum post](https://forums.playdeadlock.com/threads/10-02-2025-update.84332/))

- Added an extra boon at 12k (nearby boon levels adjusted slightly, 10.2/11.6/13.2k to 10/11/12/13.2k)
- Cutlist Sacrifice: Fire Rate boon scaling reduced from 0.8 to 0.7
- Diviner’s Kevlar: Spirit Power increased from +25 to +35

**2025-07-04** ([forum post](https://forums.playdeadlock.com/threads/07-04-2025-update.70156/))

- Ability base damage and AP bonus damage reduced by ~8% (spirit power growth unaffected)
- Ultimate cooldowns increased by 10% (affects base and upgrades, so the total CD with AP is 10% longer)
- 300 Souls Boon now gives an AP instead of an Ability Unlock
- 600 Souls Boon now gives an Ability Unlock instead of a AP
- Veilwalker: Heal now scales with boons (+3)

**2025-06-17** ([forum post](https://forums.playdeadlock.com/threads/06-17-2025-update.68401/))

- Cleaned up how boons are distributed. Previously some levels gave stat bonuses and some AP/Unlocks, now every level gives one of each. Power rebalanced on abilities and items to be the same overall as before. Total AP given out reduced from 32 to 29, total stat levels increased from 20 to 32 (but rescaled in value such that they are the same overall as before).

**2025-05-21** ([forum post](https://forums.playdeadlock.com/threads/05-21-2025-update.65674/))

- Melee damage growth per boon reduced by 5%

**2024-11-26_HeroLab**

- Reduce health per boon from 35 to 30

**2024-11-21_HeroLab**

- Weapon: Bullet damage per boon reduced from 0.57 to 0.35

**2024-11-01_HeroLab**

- Health per boon reduced from 41 to 36

**2024-10-24** ([forum post](https://forums.playdeadlock.com/threads/10-24-2024-update.40951/))

- AP is no longer granted for Walkers
- Shrine/Patron no longer have Soul/AP bounties
- Missing AP from above is redistributed along souls reward line at similar soul levels that the objectives previously died on average
- Superior Stamina: Spirit Power increased from 8 to 12

**2024-10-10** ([forum post](https://forums.playdeadlock.com/threads/10-10-2024-update.36958/))

- Updated "getting started" VO for the ability points tab to match the text
- The patron now will sometimes offer words of encouragement when you level up instead of when you destroy a Guardian or Walker
- Health Nova: Spirit Power increased from +4 to +6

**2024-09-26** ([forum post](https://forums.playdeadlock.com/threads/09-26-2024-update.33015/))

- Boon count increased from 11 to 14 (added to 16/18/20k)
- Non-Health boon bonuses rescaled over the 14 levels (same total as before)
- Withering Whip: Spirit Power increased from +4 to +6

**2024-09-12** ([forum post](https://forums.playdeadlock.com/threads/09-12-2024-update.27974/))

- Improved Reach: Spirit Power increased from +6 to +8

**2024-08-29** ([forum post](https://forums.playdeadlock.com/threads/08-29-2024-update.22253/))

- Guardians no longer give 1 AP
- AP is now added to the following Soul levels: 3500, 5200, 8000, 9700

**2024-08-16** ([forum post](https://forums.playdeadlock.com/threads/08-16-2024-update.17251/))

- Fixed the boon level display in the hero pages not working correctly

**2024-08-15** ([forum post](https://forums.playdeadlock.com/threads/08-15-2024-update.16378/))

- Using an active item or ability removes the undo option for the item/AP
- Fixed some abuse cases with undoing AP cooldown reductions

**2024-07-11** ([forum post](https://forums.playdeadlock.com/threads/07-11-2024-update.10871/))

- Added HUD Notifications on Soul Urn drop off to let depositor know they gained +25% Souls and +1 AP
- Urn now grants the Urn Runner +1 AP

**2024-06-13** ([forum post](https://forums.playdeadlock.com/threads/06-13-2024-update.5773/))

- Fixed AP not showing when you have your hero selected
- Heroes HP growth per boon increased by +5 (there are 11 instances of these). This is not done for Abrams or Dynamo.

**2024-05-03** ([forum post](https://forums.playdeadlock.com/threads/05-03-2024-update.427/))

- Fixed AP count not showing if you are dead, spectating a team mate or when holding alt/tab to upgrade your abilities
