# Guardians and Base Guardians

Generated from the game files at build 6868 and Valve's patch notes. Everything below is quoted from a source, not interpreted. Patch notes describe the game as of their date: read newest first, and treat an older line as history once a newer one changes the same thing.

## What the game itself says

- Base Guardians (`Citadel_Hud_KillFeedEnemyBarracksGuardian`)
- Base Guardians (`Citadel_Hud_KillFeedFriendlyBarracksGuardian`)
- Base Guardians (`Citadel_LaneStats_Guardians`)
- Your Base Guardians have been destroyed (`Citadel_Steamshare_Desc_Allied_ObjectiveDestroyed_BaseGuardians`)
- Your Guardian has been destroyed (`Citadel_Steamshare_Desc_Allied_ObjectiveDestroyed_Guardian`)
- Enemy Base Guardians have been destroyed (`Citadel_Steamshare_Desc_Enemy_ObjectiveDestroyed_BaseGuardians`)
- Enemy Guardian has been destroyed (`Citadel_Steamshare_Desc_Enemy_ObjectiveDestroyed_Guardian`)
- Allied Base Guardians (`Citadel_Steamshare_Title_Allied_ObjectiveDestroyed_BaseGuardians`)
- Allied Guardian (`Citadel_Steamshare_Title_Allied_ObjectiveDestroyed_Guardian`)
- Enemy Base Guardians (`Citadel_Steamshare_Title_Enemy_ObjectiveDestroyed_BaseGuardians`)
- Enemy Guardian (`Citadel_Steamshare_Title_Enemy_ObjectiveDestroyed_Guardian`)
- Guardian Damage (`ReportCard_GuardianDamage`)
- Damage you’ve dealt to enemy objectives (`ReportCard_GuardianDamage_Desc`)
- guardian Damage / guardian Damage Next Goal (`ReportCard_GuardianDamage_Progress`)
- Take Down the Enemy Guardian (`ReportCard_KillGuardian`)
- Take down anyone who stands in your way to victory! (`ReportCard_KillGuardian_Desc`)
- Guardian Destroyed (`Sandbox_Tutorial_Controls_DestroyGuardian`)
- Defeat the Enemy Guardian (`Sandbox_Tutorial_DestroyGuardian`)
- We've loaded you up with some additional Items and Ability Points, now face off against enemy heroes and troopers. Destroy their Guardian while defending your own. (`Sandbox_Tutorial_DestroyGuardian_desc`)
- Guardians are the first line of defense in each lane. Their attacks are very powerful, so it's best to push into them with your troopers. (`guide_the_map_guardians_desc`)
- As you collect souls, you'll also be granted Ability Points (AP). You can spend these points to upgrade your abilities by holding [Scoreboard] (`guide_upgrades_killing_guardians_desc`)
- Ability Points (`guide_upgrades_killing_guardians_header`)

## Current numbers in the game files

`npc_boss_tier1`

| Field | Value |
|---|---|
| BackDoorProtectionRange | 30 |
| BackdoorProtectionModifier.HealthPerSecondRegen | 65 |
| BackdoorProtectionModifier.BackdoorProtectionDamageMitigationFromPlayers | 65 |
| BackdoorProtectionModifier.BackdoorProtectionDamageMitigationFromPlayers_Streetbrawl | 85 |
| BackdoorProtectionModifier.ActivationTime | 10 |
| IntrinsicModifiers[0].BULLET_ARMOR_DAMAGE_RESIST | 10 |
| InvulRange | 24 |
| MaxHealth | 5500 |
| MeleeAttemptRange | 5 |
| MeleeHitRange | 7 |
| MinMeleeAttackTime | 1.5 |
| PlayerDPS | 116 |
| PlayerDamageResistPct | -25 |
| RunSpeed | 7.62 |
| TrooperDPS | 35 |
| TrooperDamageResistPct | 42.5 |
| Weapon.BulletDamage | 16 |
| Weapon.RoundsPerSecond | 5 |
| Weapon.BulletsPerShot | 1 |
| Weapon.DPS | 80 |
| Weapon.SustainedDPS | 80 |

`npc_barrack_boss`

| Field | Value |
|---|---|
| BackDoorProtectionRange | 50.8 |
| BackdoorBulletResistModifier.BulletResist | 40 |
| BackdoorBulletResistModifier.BulletResistReductionPerHero | 20 |
| BackdoorProtectionModifier.HealthPerSecondRegen | 65 |
| BackdoorProtectionModifier.BackdoorProtectionDamageMitigationFromPlayers | 65 |
| BackdoorProtectionModifier.BackdoorProtectionDamageMitigationFromPlayers_Streetbrawl | 85 |
| DeathFadeTimeEnd | 4 |
| DeathFadeTimeStart | 2 |
| EnemyTrooperProtectionRange | 40 |
| IntrinsicModifiers[0].BULLET_ARMOR_DAMAGE_RESIST | 20 |
| InvulRange | 24 |
| MaxHealth | 4000 |
| MeleeAttemptRange | 6.35 |
| MeleeDuration | 0.6 |
| MeleeHitRange | 6.985 |
| MinMeleeAttackTime | 1.5 |
| PlayerAutoAttackRange | 24.13 |
| PlayerDPS | 116 |
| PlayerDamageResistPct | -25 |
| RunSpeed | 7.62 |
| TrooperDPS | 35 |
| TrooperDamageResistPct | 42.5 |
| Weapon.BulletDamage | 8 |
| Weapon.RoundsPerSecond | 5 |
| Weapon.BulletsPerShot | 1 |
| Weapon.DPS | 40 |
| Weapon.SustainedDPS | 40 |

## Patch history (109 lines, newest first)

**2026-09-16** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1844115010490072))

- Guardian bounty increased by 10%

**2026-06-30** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1836506165563227))

- Guardian bounty reduced from 1500 to 1250

**2026-05-22** ([forum post](https://forums.playdeadlock.com/threads/05-22-2026-update.135477/))

- Guardians scaling resistance from +75%->-50% over 12 minutes to +50%->-50% (takes more damage early)
- Shrines are now invulnerable until one pair of Base Guardians are destroyed
- Base Guardian Bullet Resistance increased from 10% to 20%
- [ General ] - Base HP reduced by 10 for all heroes - HP per boon reduced by 3 - Guardians scaling resistance from +75%->-50% over 12 minutes to +50%->-50% (takes more damage early) - Medium neutrals initial spawn time reduced from 6 minutes to 5 minutes - Breakables spawn time increased from 2...

**2026-03-10** ([forum post](https://forums.playdeadlock.com/threads/03-06-2026-update.114328/post-220287))

- Base [[Guardian|Guardians]] HP reduced from 5500 to 4000
- Base Guardians HP reduced from 5500 to 4000

**2026-03-06** ([forum post](https://forums.playdeadlock.com/threads/03-06-2026-update.114328/))

- Killing a pair of base guardians now spawns a zipline boosted trooper wave to reinforce your push
- Guardians bounty increased from 1000 to 1500
- Base Guardians bounty from 750 to 1000

**2025-11-23** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/post-172057))

- Guardians HP increased from 4250 to 5500
- Guardians armor decay peak at 12m instead of 10m
- Fixed Base Guardians HP not matching Lane Guardians (were 1000 less)

**2025-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/))

- Guardians HP increased from 3500 to 4250 HP
- Guardians now start with 75% Damage Resist that decay's to -50% over the first 10 minutes of a match
- Base slot count increased from 8 to 9 and Flex slot count reduced from 4 to 3. One is given for each Walker killed. Previously the 4 were given for: "3 Guardians", "1 Walker", "3 Walkers", and "Set of Base Guardians"

**2025-07-04** ([forum post](https://forums.playdeadlock.com/threads/07-04-2025-update.70156/))

- Zip Line after taking Base Guardians in a lane increased from +120% to +140%
- Zip Line after taking Base Guardians in a lane ramp up time reduced from 4s to 3s
- Guardian base resistance increased from 40% to 60% (decays 10 minutes still, same values as creeps)
- Guardian total bounty reduced from 1650 to 1000

**2025-06-17** ([forum post](https://forums.playdeadlock.com/threads/06-17-2025-update.68401/))

- Mid Lane Rework (between Guardians):
- Flex Slot changed from "Two Guardians" to "Three Guardians"
- Guardian and Walker total bounty is now split with all nearby players (including players that have done damage to it within 20s). Nearby players get 40% and the rest is split evenly with all 6 players (including those nearby).

**2025-05-19** ([forum post](https://forums.playdeadlock.com/threads/05-19-2025-update.65381/))

- Moved outer lane Base Guardians down to the lower landing.

**2025-04-17** ([forum post](https://forums.playdeadlock.com/threads/04-17-2025-update.61382/))

- Guardians attack range reduced from 38.1m to 35m
- Guardians melee attempt range reduced from 6.1m to 5m
- Guardians melee damage range reduced from 8m to 7m
- Troopers will no longer aggro to you when you shoot them while they are attacking a Guardian

**2025-04-04** ([forum post](https://forums.playdeadlock.com/threads/04-04-2025-update.60284/))

- Fixed shotguns doing too much damage to Guardians

**2024-12-06** ([forum post](https://forums.playdeadlock.com/threads/12-06-2024-update.50599/))

- Reverted: - Guardians now deal 25% more damage to troopers
- Reverted: - Guardians now take 25% more damage from troopers/players

**2024-11-29** ([forum post](https://forums.playdeadlock.com/threads/11-29-2024-update.49470/))

- Guardians now deal 25% more damage to troopers
- Guardians now take 25% more damage from troopers/players

**2024-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2024-update.47476/))

- Flex Slot changed from All Shrines to 1 Shrine and 2 Base Guardians
- Moved rooftop neutral camps on Amber Yellow and Sapphire Purple to rooftops closer to the Guardian

**2024-11-13** ([forum post](https://forums.playdeadlock.com/threads/11-13-2024-update.46391/))

- Guardian resistance changed from -35% at 8 minutes to -50% at 10 minutes

**2024-11-07** ([forum post](https://forums.playdeadlock.com/threads/11-07-2024-update.44786/))

- Troopers now take 28% more damage from Guardians
- Guardians will now focus their attack on enemy players if an enemy player shoots a hero and the enemy player is within 15m of the Guardian
- Fixed Troopers resistance against Base Guardians not working properly

**2024-10-24** ([forum post](https://forums.playdeadlock.com/threads/10-24-2024-update.40951/))

- Guardian attack range requirement changed from 20m to requiring you are above the ramp on high ground
- Guardian resist vs troopers changed from starting at 70% and ending at -30% at 10 min to starting at 60% and ending at -35% at 8 minutes
- Guardians now have resist vs players starting at 40% and ending at -35% at 8 minutes
- Base Guardians and Shrines no longer have out-of-combat regen

**2024-10-15** ([forum post](https://forums.playdeadlock.com/threads/10-15-2024-update.38925/))

- First flex slot is now granted after 3 Guardians die instead of 4
- Range to attack lane Guardians increased from 19m to 20m

**2024-10-10** ([forum post](https://forums.playdeadlock.com/threads/10-10-2024-update.36958/))

- Added Guardian and Walker death notification sound for all players
- The patron now will sometimes offer words of encouragement when you level up instead of when you destroy a Guardian or Walker
- Troopers attack range vs Lane Guardians reduced from 13.5m to 12m (they get closer to it)
- Players now need to be within 19m (above the ramp) to attack a Lane Guardian
- Guardians now take 70% less damage from troopers at the start of the game; this reduces by 10% per minute (max at +30% increased damage at 10 min)
- Guardian damage vs players increased by 20%
- Percentage of deniable orbs from objectives for Guardian/Walker/Patron/Shrines rescaled from 54.55/66.67/100/0% to 35%
- Moved Guardians back slightly further from stairs down to the canal

**2024-09-26** ([forum post](https://forums.playdeadlock.com/threads/09-26-2024-update.33015/))

- Fixed Guardian trying to shoot people unsuccessfully behind cover
- Trooper damage reduction from Guardians reduced from 35% to 28% (they die a little faster to Guardians now)
- Troopers no longer give half bounty when base guardians are destroyed for that lane
- Guardians now deal 10% more damage to players
- Redesigned outer lane path (ziplines and trooper nodes) from Walker to Guardian on Amber Yellow and Sapphire Purple

**2024-09-12** ([forum post](https://forums.playdeadlock.com/threads/09-12-2024-update.27974/))

- Fixed Medic Troopers sometimes using their heal on Guardian boss
- amber_green_guardian_arena.png

**2024-08-29** ([forum post](https://forums.playdeadlock.com/threads/08-29-2024-update.22253/))

- Fixed Zipline speed from Base Guardian killing and Zip booster ability not stacking properly
- Fixed Base Guardian boost not properly doing its ramp up and instead instantly being fast
- Added 'Express' state to zipline indicators when speed had increased from defeating Enemy Base Guardians
- Moved a flex slot from "Set of enemy Base Guardians" to "All Enemy Lane Guardians"
- Guardians no longer give 1 AP

**2024-08-22** ([forum post](https://forums.playdeadlock.com/threads/08-22-2024-update.19716/))

- Parrying a Guardian now causes it to stop trying to repeatedly melee (and get parried over and over), and instead causes the boss to start shooting shortly there after

**2024-08-15** ([forum post](https://forums.playdeadlock.com/threads/08-15-2024-update.16378/))

- Base Guardian Health increased by 20%
- Firehouse (building next to Sapphire Yellow Guardian) has been reworked to match the layout of the Chapel
- Low roof buildings beside Amber Purple Guardian and Sapphire Yellow Guardian are now valid play spaces
- Added passage through building and stairs up to a peek spot toward the Guardian
- Removed railing and added stairs in the passage toward the Guardian
- Added interior shaft with Bounce Pad to an upper level balcony from defender side to face the Guardian
- Added a juke spot down the stairs from the Guardian to the left

**2024-08-01** ([forum post](https://forums.playdeadlock.com/threads/08-01-2024-update.13369/))

- Added connection from the underground teleport station to the outer lane Guardian (previously a juke spot)
- Added steam tunnel connection from Amber Blue Guardian and Sapphire Orange Guardian to Mid (one-way)
- Each trooper you shoot at will now consider you a higher priority than Guardians/Walkers; that trooper will stop shooting the Guardians/Walkers and consider you its target for a few seconds
- Parrying a Guardian attack will no longer cause the Guardian to be stunned
- Moved barrel cover barrier to block the Guardian shop opening on Amber Purple and Sapphire Yellow

**2024-07-18** ([forum post](https://forums.playdeadlock.com/threads/07-18-2024-update.11831/))

- Guardians now fade out from the world 10 seconds after dying
- Guardian HP increased by 10%
- Guardian melee no longer does a double instant melee attack sometimes
- Guardian melee attack no longer has a splash range much larger than its visuals

**2024-07-11** ([forum post](https://forums.playdeadlock.com/threads/07-11-2024-update.10871/))

- Guardian health increased by 10%
- Base Guardian health increased by 10%
- Base Guardian and Shrines bullet resist per nearby hero increased from 40/20/0/0% (for 0/1/2/3 people) to 60/40/20/0%

**2024-07-04** ([forum post](https://forums.playdeadlock.com/threads/07-04-2024-update.9652/))

- Base Guardians and Shrines now have +40% Bullet Resistance. They lose 20% for each enemy hero nearby (down to a minimum of 0% bullet resistance). When they haven't taken damage for 60 seconds, they regenerate 4% max hp per second.
- Moved the new cover barrier in front of the inner lane Guardian closer to the Guardian

**2024-06-27** ([forum post](https://forums.playdeadlock.com/threads/06-27-2024-update.8486/))

- Fixed being able to hide inside the Guardian's head
- Opened up Authority Building and Jazz Club to the Guardian side
- Added intermediate cover in front of Amber Orange Guardian and Sapphire Blue Guardian
- Extended cover near Sapphire Orange Guardian to match Amber Blue

**2024-06-23** ([forum post](https://forums.playdeadlock.com/threads/06-23-2024-update.7705/))

- There is no longer a reinforcement trooper wave after Guardians and Walkers die

**2024-06-13** ([forum post](https://forums.playdeadlock.com/threads/06-13-2024-update.5773/))

- Added Patron VO for when allied or enemy base guardians are destroyed

**2024-06-06** ([forum post](https://forums.playdeadlock.com/threads/06-06-2024-update.4096/))

- Added new objective health bars for Guardians and Walkers
- Increased the speed of Guardian's melee attacks
- Changed Guardian's behavior to only attempt melee when a unit is within 6m but still do damage to units in 12m range
- Removed street lamp post that was causing heroes to get stuck near inner lane Guardian
- Moved the middle lane Base Guardians further out slightly

**2024-05-30** ([forum post](https://forums.playdeadlock.com/threads/05-30-2024-update.2514/))

- Lane Guardian HP increased from 3750 to 4600
- Various adjustments to lane layout to give defenders more options for forward positions near their Guardian
- Base Guardians moved a little bit further towards the outside of the base
- Carved out interior of inner lane tower buildings beside the Guardian and connected to the neutral camp in the underground areas

**2024-05-23** ([forum post](https://forums.playdeadlock.com/threads/05-23-2024-update.1245/))

- Fixed getting stuck under stair at inner lanes near Guardian
- Sidelane Veils near Guardians are now one-way visibility (used to be blocked visibility in both directions)
- Zipline base speed boost after Base Guardians are killed increased from 100% to 120%
- Zipline base speed boost's ramp time after Base Guardians are killed reduced from 5s to 4s

**2024-05-13** ([forum post](https://forums.playdeadlock.com/threads/05-13-2024-update.807/))

- Troopers DPS vs Base Guardians from 110 DPS to 80 DPS

**2024-05-03** ([forum post](https://forums.playdeadlock.com/threads/05-03-2024-update.427/))

- Troopers DPS vs Lane Guardians reduced from 44 to 36
