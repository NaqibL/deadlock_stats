# Troopers and lanes

Generated from the game files at build 6868 and Valve's patch notes. Everything below is quoted from a source, not interpreted. Patch notes describe the game as of their date: read newest first, and treat an older line as history once a newer one changes the same thing. The patch notes do not record every change, so where a current number below differs from the newest note, the number is right. Questions already worked through are answered in [settled.md](../settled.md).

## What the game itself says

- Zipline Speed Boost [ability_cooldown] (`AbilityButtonHint_ZipLineBoost`)
- Hyperline Speed (`BonusZipLineSpeed_label`)
- Medic Trooper (`Citadel_AttackerClass_CLASS_TROOPER_MEDIC`)
- Melee Trooper (`Citadel_AttackerClass_CLASS_TROOPER_MELEE`)
- Need Troopers (`Citadel_HUD_Damage_NoTroopers`)
- HOLD[Held Item] (`Citadel_Hud_CaptureZipLine`)
- Trooper #unit num (`Citadel_Hud_KillFeedTrooper`)
- HOLD [Zipline] to Ride (`Citadel_Hud_RideZipLine`)
- Unavailable after taking damage (`Citadel_Hud_RideZipLineOnCooldown`)
- cooldown secondss (`Citadel_Hud_RideZipLineOnCooldownValue`)
- Disabled while flying (`Citadel_Hud_RideZipLineUnHoldRequired`)
- Lanes will be assigned based on the skill of all players in the match. (`Citadel_LanePreference_Balanced_Desc`)
- Lane assignments will prioritize keeping your party together. (`Citadel_LanePreference_Party_Desc`)
- Lane preference (`Citadel_LanePreference_Title`)
- Prioritize starting in the same lane as party members when possible. Note this may impact game balance. (`Citadel_LanePreference_Tooltip`)
- Base Guardians (`Citadel_LaneStats_Guardians`)
- Player Damage (`Citadel_LaneStats_PlayerDamage`)
- Specify Lane Assignments (`Citadel_PrivateLobby_RandomLanes_Off`)
- Default Lane Assignments (`Citadel_PrivateLobby_RandomLanes_On`)
- Randomly assign players within teams to different lanes (`Citadel_PrivateLobby_ShuffleLanesTooltip`)
- Click to request swapping lanes. (`Citadel_Scoreboard_LaneSwapAvailable_Tooltip`)
- Click to swap lanes. Right click to reject. (`Citadel_Scoreboard_LaneSwapReceiving_Tooltip`)
- Click to cancel this request. (`Citadel_Scoreboard_LaneSwapRequesting_Tooltip`)
- Zipline Boost (`Citadel_ZiplineBoostDesc`)
- Health Regen (`HealthRegenPerTrooper_label`)
- per nearby trooper (`HealthRegenPerTrooper_postfix`)
- Health Regen (`HealthRegenPerTrooper_postvalue_label`)
- The goal of the early game is to build up enough power to take down objectives. When you complete the goals listed on the right, you'll be ready to take on the Guardian. (`LaneTraining_Intro_Desc`)
- Welcome to Lane Training (`LaneTraining_Intro_Title`)
- Lane Training finished (`LaneTraining_Outro_Title`)
- Learn the early game in Lane Training (`NewPlayer_LaneTraining`)
- Kill Troopers (troopers remaining remaining) (`Sandbox_Tutorial_KillTroopers`)
- There are troopers remaining enemy troopers remaining. (`Sandbox_Tutorial_KillTroopers_desc`)
- Ride the Zipline (`Sandbox_Tutorial_Zipline`)
- Aim at the Zipline, then hold [Default.Mantle] to ride it to your Guardian. (`Sandbox_Tutorial_Zipline_desc`)
- Spawn a melee trooper for each enemy hero trapped in the cage (`SpawnTroopers_label`)
- Hyperline Speed (`StatDesc_ZipLineSpeed`)
- Trooper lifetime (`TrooperLifetime_label`)
- Troopers created (`TroopersToSummon_label`)
- Arrow Flight Time (`ZipLineArrowLifetime_label`)
- Zipline Speed (`ZipLineSpeedPercent_label`)
- Zipline Speed (`ZipLineSpeedPercent_postvalue_label`)
- Jump Off Duration (`ZiplineJumpBonusDuration_label`)
- Jump Off Speed Bonus (`ZiplineJumpBonusMoveSpeed_label`)
- Attacking Lane (`citadel_bot_objective_attack_lane`)
- Defending Lane (`citadel_bot_objective_defend_lane`)
- Defending T1 (`citadel_bot_objective_defend_zipline`)
- Pushing Zipline (`citadel_bot_objective_push_zipline`)
- Hold [Zipline] to jump on the hyperline. (`citadel_hint_zipline`)
- Zipline / rope (`citadel_keybind_zipline`)
- Hold [Zipline] to get on the line. You can jump off by pressing [Mantle] (`guide_movement_zipline_desc`)
- There are three lanes, each with a zipline that players can ride to move quickly. (`guide_the_map_lanes_desc`)
- Troopers periodically spawn in the base and then run down a lane, fighting any enemies they encounter. (`guide_the_map_troopers_desc`)
- Stun Grenade (`trooper_boss_grenade`)
- Zipline Boosted (`zipline_boost`)
- Increased Zipline Speed (`zipline_speed_pickup/zipline_speed`)
- Zipline Speed (`zipline_speed_pickup_label`)

## Current numbers in the game files

`trooper_normal`

| Field | Value |
|---|---|
| BreakableForceScale | 5 |
| EnemyBaseDamageReduction | 35 |
| HitReactClips[0].RandomWeight | 123 |
| HitReactClips[0].Duration | 1.16 |
| HitReactClips[1].RandomWeight | 0.1 |
| HitReactClips[1].Duration | 1.16 |
| HitReactClips[2].RandomWeight | 0.1 |
| HitReactClips[2].Duration | 1.16 |
| HitReactClips[3].RandomWeight | 0.2 |
| HitReactClips[3].Duration | 1 |
| HitReactClips[4].RandomWeight | 0.2 |
| HitReactClips[4].Duration | 1 |
| HitReactClips[5].RandomWeight | 0.3 |
| HitReactClips[5].Duration | 1 |
| JumpUpBaseCostSeconds | 1 |
| MaxHealth | 300 |
| MeleeAttemptRange | 2.54 |
| MeleeDamage | 50 |
| MeleeDuration | 1.5 |
| MeleeHitRange | 2.54 |
| MeleeHitTime | 0.5 |
| NearDeathDuration | 1 |
| NpcOutOfCombatModifier.OOCRegen | 7 |
| RunSpeed | 13 |
| ShrinesDownBuffModifier.HealthScale | 1.4 |
| ShrinesDownBuffModifier.DamageScale | 60 |
| VSGuardian.BaseDPS | 14.4 |
| VSGuardian.EndDPS | 54 |
| VSGuardian.EndDPSTimeInSeconds | 600 |
| VSGuardian.MaxRange | 12 |
| VSPatron.BaseDPS | 50 |
| VSPatron.MaxRange | 25.4 |
| VSPatron.DamageResist | 50 |
| VSPatronPhase2.BaseDPS | 50 |
| VSPatronPhase2.MaxRange | 17.78 |
| VSPatronPhase2.DamageResist | 50 |
| VSPlayer.BaseDPS | 28 |
| VSPlayer.MaxRange | 17.78 |
| VSPlayer.DamageResist | -25 |
| VSShrine.BaseDPS | 50 |
| VSShrine.MaxRange | 8.89 |
| VSTrooper.BaseDPS | 35 |
| VSTrooper.MaxRange | 17.78 |
| VSTrooper.DamageResist | 42.5 |
| VSWalker.BaseDPS | 24 |
| VSWalker.EndDPS | 84 |
| VSWalker.EndDPSTimeInSeconds | 1200 |
| VSWalker.MaxRange | 17.78 |
| VSWalker.DamageResist | 80 |
| VSWatcher.BaseDPS | 80 |
| VSWatcher.DamageResist | 67.5 |
| VSWatcher.MaxRange | 17.78 |
| WalkSpeed | 6.299 |
| Weapon.BulletDamage | 36 |
| Weapon.RoundsPerSecond | 0.9709 |
| Weapon.BulletsPerShot | 1 |
| Weapon.DPS | 34.951 |
| Weapon.SustainedDPS | 34.951 |

`trooper_melee`

| Field | Value |
|---|---|
| BreakableForceScale | 5 |
| EnemyBaseDamageReduction | 35 |
| HitReactClips[0].RandomWeight | 123 |
| HitReactClips[0].Duration | 1.16 |
| HitReactClips[1].RandomWeight | 0.1 |
| HitReactClips[1].Duration | 1.16 |
| HitReactClips[2].RandomWeight | 0.1 |
| HitReactClips[2].Duration | 1.16 |
| HitReactClips[3].RandomWeight | 0.2 |
| HitReactClips[3].Duration | 1 |
| HitReactClips[4].RandomWeight | 0.2 |
| HitReactClips[4].Duration | 1 |
| HitReactClips[5].RandomWeight | 0.3 |
| HitReactClips[5].Duration | 1 |
| JumpUpBaseCostSeconds | 1 |
| MaxHealth | 400 |
| MeleeAttemptRange | 3.048 |
| MeleeChargeRange | 25.4 |
| MeleeDamage | 80 |
| MeleeDuration | 1.333 |
| MeleeHitRange | 3.048 |
| MeleeHitTime | 0.4 |
| NearDeathDuration | 1 |
| NpcOutOfCombatModifier.OOCRegen | 7 |
| RunSpeed | 13 |
| ShrinesDownBuffModifier.HealthScale | 1.4 |
| ShrinesDownBuffModifier.DamageScale | 60 |
| VSGuardian.BaseDPS | 14.4 |
| VSGuardian.EndDPS | 54 |
| VSGuardian.EndDPSTimeInSeconds | 600 |
| VSGuardian.MaxRange | 12 |
| VSPatron.BaseDPS | 50 |
| VSPatron.MaxRange | 25.4 |
| VSPatron.DamageResist | 50 |
| VSPatronPhase2.BaseDPS | 50 |
| VSPatronPhase2.MaxRange | 17.78 |
| VSPatronPhase2.DamageResist | 50 |
| VSPlayer.BaseDPS | 28 |
| VSPlayer.MaxRange | 17.78 |
| VSPlayer.DamageResist | -25 |
| VSShrine.BaseDPS | 50 |
| VSShrine.MaxRange | 8.89 |
| VSTrooper.BaseDPS | 35 |
| VSTrooper.MaxRange | 17.78 |
| VSTrooper.DamageResist | 42.5 |
| VSWalker.BaseDPS | 24 |
| VSWalker.EndDPS | 84 |
| VSWalker.EndDPSTimeInSeconds | 1200 |
| VSWalker.MaxRange | 17.78 |
| VSWalker.DamageResist | 80 |
| VSWatcher.BaseDPS | 80 |
| VSWatcher.DamageResist | 67.5 |
| VSWatcher.MaxRange | 17.78 |
| WalkSpeed | 8.128 |
| Weapon.BulletDamage | 61.8 |
| Weapon.RoundsPerSecond | 0.9709 |
| Weapon.BulletsPerShot | 1 |
| Weapon.DPS | 60 |
| Weapon.SustainedDPS | 60 |

`trooper_medic`

| Field | Value |
|---|---|
| AOEHealthPickup.AOERadius | 35 |
| AOEHealthPickup.PickupRadiusBase | 18.01 |
| AOEHealthPickup.PickupRadiusScaling | 1.499 |
| AOEHealthPickup.PickupRadiusMax | 30 |
| AOEHealthPickup.PickupRadiusStartMinute | 10 |
| AOEHealthPickup.MissingPctRegen | 13 |
| AOEHealthPickup.RegenFixed | 150 |
| AOEHealthPickup.RegenFixedScaling | 2 |
| AOEHealthPickup.RegenDuration | 4 |
| AOEHealthPickup.RegenDurationTroopers | 8 |
| AOEHealthPickup.RegenTrooperMultiplier | 1.3 |
| AOEHealthPickup.PickupExpirationDurationBase | 18 |
| AOEHealthPickup.PickupExpirationDurationScaling | 2 |
| AOEHealthPickup.PickupExpirationDurationMax | 40 |
| AOEHealthPickup.PickupExpirationStartMinute | 10 |
| BreakableForceScale | 5 |
| DPSPctGrowthPerMinute | 3 |
| EnemyBaseDamageReduction | 35 |
| HitReactClips[0].RandomWeight | 123 |
| HitReactClips[0].Duration | 1.16 |
| HitReactClips[1].RandomWeight | 0.1 |
| HitReactClips[1].Duration | 1.16 |
| HitReactClips[2].RandomWeight | 0.1 |
| HitReactClips[2].Duration | 1.16 |
| HitReactClips[3].RandomWeight | 0.2 |
| HitReactClips[3].Duration | 1 |
| HitReactClips[4].RandomWeight | 0.2 |
| HitReactClips[4].Duration | 1 |
| HitReactClips[5].RandomWeight | 0.3 |
| HitReactClips[5].Duration | 1 |
| JumpUpBaseCostSeconds | 1 |
| MaxHealth | 350 |
| MeleeAttemptRange | 2.54 |
| MeleeDamage | 25 |
| MeleeDuration | 1 |
| MeleeHitRange | 2.54 |
| MeleeHitTime | 0.3 |
| NearDeathDuration | 1 |
| NpcOutOfCombatModifier.OOCRegen | 7 |
| RunSpeed | 13 |
| ShrinesDownBuffModifier.HealthScale | 1.4 |
| ShrinesDownBuffModifier.DamageScale | 60 |
| VSGuardian.BaseDPS | 14.4 |
| VSGuardian.EndDPS | 54 |
| VSGuardian.EndDPSTimeInSeconds | 600 |
| VSGuardian.MaxRange | 12 |
| VSPatron.BaseDPS | 50 |
| VSPatron.MaxRange | 25.4 |
| VSPatron.DamageResist | 50 |
| VSPatronPhase2.BaseDPS | 50 |
| VSPatronPhase2.MaxRange | 17.78 |
| VSPatronPhase2.DamageResist | 50 |
| VSPlayer.BaseDPS | 28 |
| VSPlayer.MaxRange | 17.78 |
| VSPlayer.DamageResist | -25 |
| VSShrine.BaseDPS | 50 |
| VSShrine.MaxRange | 8.89 |
| VSTrooper.BaseDPS | 45 |
| VSTrooper.MaxRange | 22.86 |
| VSTrooper.DamageResist | 42.5 |
| VSWalker.BaseDPS | 24 |
| VSWalker.EndDPS | 84 |
| VSWalker.EndDPSTimeInSeconds | 1200 |
| VSWalker.MaxRange | 17.78 |
| VSWalker.DamageResist | 80 |
| VSWatcher.BaseDPS | 80 |
| VSWatcher.DamageResist | 67.5 |
| VSWatcher.MaxRange | 17.78 |
| WalkSpeed | 6.299 |
| Weapon.BulletDamage | 36 |
| Weapon.RoundsPerSecond | 0.9709 |
| Weapon.BulletsPerShot | 1 |
| Weapon.DPS | 34.951 |
| Weapon.SustainedDPS | 34.951 |

Server settings (`convars.json`)

| Setting | Value |
|---|---|
| citadel_player_damage_from_trooper_scale | 0.5 |
| citadel_super_trooper_gold_mult | 0.85 |
| citadel_trooper_gold_reward | 100 |
| citadel_trooper_gold_reward_bonus_per_minute | 2 |
| citadel_trooper_health_mult | 1.5 |
| citadel_trooper_health_mult_gametime | 35 |
| citadel_trooper_spawn_initial | 16 |
| citadel_trooper_spawn_interval_early | 30 |
| citadel_trooper_spawn_interval_late | 25 |
| citadel_trooper_spawn_interval_late_time | 20 |
| citadel_trooper_spawn_interval_very_late | 20 |
| citadel_trooper_spawn_interval_very_late_time | 35 |
| citadel_trooper_squad_size | 4 |
| citadel_zipline_nonbaselane_speed_mult | 1.1 |

## Patch history (322 lines, newest first)

**2026-10-05** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1845383656394833))

- Fixed bugs that were causing troopers to walk too slowly in lane

**2026-07-09** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1836506165584438))

- Rift Troopers now have Spirit Resist (30/35/40/45%)
- Rift Troopers now have Melee Resistance (25%)
- Rift Troopers spawn interval increased from every 0.3s to 0.5s (spawns slightly more staggered)
- Rift Troopers max comeback count increased from 12 to 14

**2026-06-30** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1836506165563227))

- Unstable Rift no longer requires an Urn delivery to trigger the start of the event. It now has a variable start time of +/- 1 minute. There is a global announcement 25s before it spawns. 60s before that there is also an in-world only visual effect to let you know which lane it'll randomly spawn in.
- The team that secures the Unstable Rift now also has a wave of 5 Rift Troopers sent down from the rift location. When trailing, spawns up to 12 troopers instead (using the same linear ramp from 0% NW to -15% NW)
- Rift Troopers drop no souls when killed
- Rift Troopers spawn with 100% extra health and damage (they also look larger and have custom VFX). Their bonus health and damage grow slightly per event (first one is 100%, then 120%, 140%, etc)
- Trooper bounty rescaled from 116 + 1.16/m to 100 + 2/m (less before 20m, more after)
- Trooper bounty ratio in the deniable flying orb increased from 40% to 50%

**2026-06-04** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1834602721188293))

- Drop off location is above the bridges on the side lanes, rather than below.

**2026-05-28** ([forum post](https://forums.playdeadlock.com/threads/05-22-2026-update.135477/post-261657))

- Parrying a [[trooper]] no longer resets your parry cooldown (however it won't end your parry early like a hero hit does)
- Parrying a trooper now stuns the trooper

**2026-05-25** ([forum post](https://forums.playdeadlock.com/threads/05-22-2026-update.135477/post-259788))

- Urn drop off point is moved from the above bridge in the mid lane to under the bridge in the side lane

**2026-05-22** ([forum post](https://forums.playdeadlock.com/threads/05-22-2026-update.135477/))

- Medic trooper heal duration increased from 2s to 4s (same overall heal amount)
- When receiving multiple of the Medic trooper orb the duration will now be added ontop rather than stacking directly (so picking up 4 in a row will give the regen over 16s instead of over 4s, overall heal is the same just slower)
- Medic Trooper heal increased from 12% missing hp to 13%
- Smoothed zipline grabbing to fix some jitter
- Added ropes to zipline binding (so if a player rebinds zipline to something other than SPACE it will also apply to mounting/dismounting ropes)
- Removed delay on ziplines when using alternative key binds

**2026-04-10** ([forum post](https://forums.playdeadlock.com/threads/04-10-2026-update.125825/))

- Medic Trooper missing health percent heal reduced from 16% to 14%
- Medic Trooper fixed regen growth per minute reduced from 4 to 3
- Medic Trooper missing health percent heal reduced from 16% to 14%
- Medic Trooper fixed regen growth per minute reduced from 4 to 3

**2026-03-10** ([forum post](https://forums.playdeadlock.com/threads/03-06-2026-update.114328/post-220287))

- [[Zipline]] can now be captured a little bit more forward towards the enemy base
- The minimum always captured [[Zipline|zipline]] distance in your base is now reduced a little bit inwards
- Super [[Trooper|troopers]] (when a lane [[Shrine|shrine]] is down) now have 15% less bounty
- Zipline can now be captured a little bit more forward towards the enemy base
- The minimum always captured zipline distance in your base is now reduced a little bit inwards
- Super troopers (when a lane shrine is down) now have 15% less bounty

**2026-03-06** ([forum post](https://forums.playdeadlock.com/threads/03-06-2026-update.114328/))

- Super troopers bonus DPS increased from +40% to +60% (the upgraded troopers when Shrine dies)
- Middle Lane troopers now gets upgraded when either of the shrines die, rather than only when both die
- Killing a pair of base guardians now spawns a zipline boosted trooper wave to reinforce your push
- Medic Troopers DPS grows by 3% per minute
- Troopers now gain 7 HP regen when out of combat
- Trooper wave interval increased from every 25s to every 20s starting at 35 minutes
- Moved the mid lane bridge above the Hidden King Base entrance more to the middle of the two edges

**2026-02-12** ([forum post](https://forums.playdeadlock.com/threads/01-30-2026-update.102822/post-204182))

- Troopers now get stronger for the specific lane that the shrine died in, rather than only after both shrines died (when both die, middle lane also gets improved)
- Improved blue zipline attach speed and fixed various bugs

**2025-12-16** ([forum post](https://forums.playdeadlock.com/threads/12-16-2025-update.93983/))

- Trooper bounty reduced by 12%
- Killing both enemy shrines will now make all of your troopers stronger (30% hp and 30% damage)
- Medic orbs now heals allied troopers 30% more
- Medic orbs regen on allied troopers is now applied over 8s instead of 2s
- Medic Trooper HP increased from 260 to 350 (default trooper is 300)
- Medic Trooper DPS vs other troopers increased from 35 to 45 (default trooper is 35)
- Medic Troopers attack range vs troopers and players increased by +5m over the default
- Medic Pack pickup range scales from 18m->26m to 18m->30m (over the same time period, 10min to 18min)

**2025-11-27** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/post-173347))

- Medic Pack now heal amounts increased by 2x
- Medic Pack heal now splits its value evenly based on the number of nearby heroes (so 1 hero is 100%, 2 heroes is 50%, 3 heroes is 33%, etc. Other nearby units also get the reduced values.)
- Medic Pack regen applied over 2s instead of 1s
- Medic Pack ally search radius from 30 to 35
- Medic Pack pickup range scales after 10 minutes (similar to the expiry duration), from 18m at 10 minutes scaling up by 1m per minute up to 26m range.

**2025-11-23** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/post-172057))

- Fixed Base Guardians HP not matching Lane Guardians (were 1000 less)

**2025-11-22** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/post-171913))

- Medic Pack missing health % reduced from 10% to 8%

**2025-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/))

- Trooper bounty mechanics have been reworked. The first half of the souls still fly out as deniable orb, however rather than the other half being instantly given to nearby players it will fall to the ground as an orb that you need to get near to pick up. It has a 18m capture radius where it'll travel to you once you get within. Only one player needs to claim it, share rules remain the same as before.
- Increased trooper range to be considered in range for souls to drop from 35m to 45m
- Medic troopers no longer have a passive healing pulse ability
- Medic troopers now drop a medic pack when you kill them. Has same pickup range/duration mechanics as the soul orbs on the ground. Heals everyone in a 30m radius for 10% of their missing health as well as 75 plus 2 per minute game time.
- Trooper bounty values increased by 10%
- Trooper bounty split ratios updated from 1/0.65/0.28/0.15/0.12/0.08 to 1/0.54/0.36/0.25/0.2/0.16
- After 35 minutes all troopers gain +50% HP.
- Walker on the Side Lanes now have same HP as Midlane (rather than ~37% less)
- Walker area in mid lane adjusted
- Added new trooper anti-stuck behavior to fix some places where you can move a trooper to get them stuck.
- Fixed a bug where troopers could clip into the world while running up stairs and over obstacles

**2025-10-24** ([forum post](https://forums.playdeadlock.com/threads/10-24-2025-update.87198/))

- Getting damaged during the initial launch window (0.6s) after using a Jump Pad will cause you to be stunned (similar to ziplines having an initial knockoff period). When you are stunned, you will lose control and continue towards the landing destination. The stun will wear off 0.2s after landing, and then a 30% slow for 2s will apply. Damage over time does not trigger this (same damage rules as ziplines).

**2025-10-03** ([forum post](https://forums.playdeadlock.com/threads/10-02-2025-update.84332/post-159495))

- Fixed Wall Jumps not refunding stamina if a mantle or zipline occurs within the refund window (similar to how we treat other stamina refunds)

**2025-07-29** ([forum post](https://forums.playdeadlock.com/threads/07-29-2025-update.72760/))

- Reworked Rejuv reward from Mid Boss. No longer buffs troopers, reduces respawn time and buffs various stats. Upon death, 3 rejuv crystals fall to the ground (4 for subsequent midboss kills). Claiming one now grants you in place revive after 3s. If you already claimed one and claim another, it'll go to an ally (priority is closest allies first, then most recent dead allies). Dying with Rejuv no longer counts as a kill/death nor gives out bounties. While you have the Rejuv buff, you gain the following: +20% Max HP, +20% Fire Rate, and +15% Spirit Damage. Gaining the buff heals you to full and lasts up to 7 minutes.
- After 20 minutes, trooper spawn time is reduced from 30s to 25s
- Trooper bounty growth reduced from 1.5 to 1.2
- Trooper ally split updated from 100/65/30/20/15/11% to 100/65/28/15/12/8%
- Hero bounties are now reduced based on the amount of players, similar to the trooper mechanic. (Means kills are less efficient/rewarding when its a big group, 1/2/3/4/5/6 players are 100/100/90/85/80/75% efficient)
- Trooper: Walk speed increased from 6.1 to 6.3
- Trooper: Run speed increased from 11 to 13
- Update the Zipline Knockdown to make the players go straight down and not start the stun timer until they hit the ground
- Zipline knockoff stun duration reduced from 3s to 2.5s

**2025-07-04** ([forum post](https://forums.playdeadlock.com/threads/07-04-2025-update.70156/))

- Zip Line after taking Base Guardians in a lane increased from +120% to +140%
- Zip Line after taking Base Guardians in a lane ramp up time reduced from 4s to 3s
- Rejuv trooper health bonus reduced from 200/230/260% to 170/200/230%

**2025-06-17** ([forum post](https://forums.playdeadlock.com/threads/06-17-2025-update.68401/))

- Trooper damage to Walkers reduced from 80 DPS to 60 DPS
- Trooper base bounty reduced from 132 to 120
- Trooper bounty growth per minute increased from 1 to 1.5
- Fixed some issues with hitting troopers while on ziplines
- Tankbuster only goes on cooldown when it affects players (no longer goes on cooldown if an ability hits a trooper)

**2025-05-27** ([forum post](https://forums.playdeadlock.com/threads/05-27-2025-update.66453/))

- Trooper resistance near base reduced from 40% to 35%
- Fixed Neutrals near the base gaining the "near base" trooper resist
- Added news kiosk structure in between Mid Lane Walker and base entrance
- Added wall partition structures outside of Outer Lane base entrances

**2025-05-21** ([forum post](https://forums.playdeadlock.com/threads/05-21-2025-update.65674/))

- Troopers will now only flinch from player damage if it is a headshot while the trooper is busy running.
- Trooper resistance near base reduced from 50% to 40%
- Added statues in front of Mid Lane entrances for cover.
- Removed a tree in front of the Mid Lane entrance.
- Tweaked trooper nodes to go around new statues.

**2025-05-19** ([forum post](https://forums.playdeadlock.com/threads/05-19-2025-update.65381/))

- Troopers now gain 50% resistance when they are in near the base (this has been 30% the past few days)
- Walkers resistance vs troopers reaches -40% at 20 minutes instead of 16 minutes
- Moved outer lane Base Guardians down to the lower landing.
- Flattened the shape of the outer lane base bridges.

**2025-04-17** ([forum post](https://forums.playdeadlock.com/threads/04-17-2025-update.61382/))

- Soul Orbs no longer have special duplication rules before 8 minutes. Soul splitting rules are now the same before 8 minutes as afterwards. Adjusted trooper economy to compensate. There is also no longer a bounty bump that occurs at 8 minutes.
- Players can no longer Parry troopers
- Medic Trooper: Heal no longer has charges (was 3)
- Medic Trooper: Cooldown reduced from 35s to 6s (this was the previous setup before)
- Medic Trooper: Fixed healing sometimes not functioning on bounce when there are walls nearby
- Troopers will no longer aggro to you when you shoot them while they are attacking a Guardian
- Melee troopers will no longer see and follow players around corners and through veils
- Smoothed out trooper navigation in some spots of the map where they need to drop down
- Troopers that are attacking shrines are no longer distracted from their task by distant enemy troopers
- Troopers now know to cross the base and attack the other shrine once their near one is defeated
- Fixed a bug where troopers would rapidly change targets when multiple enemies are in range
- Fixed a bug where troopers would fidget with their facing direction when walking without a target
- Fixed a bug where troopers would fear really steep stairs
- Fixed a bug where troopers would flash their targeting flare at the targeted player every time they came into camera or line of sight

**2025-04-04** ([forum post](https://forums.playdeadlock.com/threads/04-04-2025-update.60284/))

- Removed the outer lanes teleporters
- When attaching to a zipline, movement direction can override the travel direction

**2025-02-25** ([forum post](https://forums.playdeadlock.com/threads/02-25-2025-update.56683/))

- Today's update introduces a reworked map layout, alongside a variety of improvements and bug fixes. [ Map Rework ] - The map has been redesigned around being 3 lanes rather than 4. This has a large range of accompanying map-wide changes regarding visuals, building layouts, pathways, neutral...

**2024-12-06** ([forum post](https://forums.playdeadlock.com/threads/12-06-2024-update.50599/))

- Added park theming to purple lane
- The new Extra Competitive option, Incoming Chat, and Lane Preference (party only) settings are now collected within a 'Queue Options' button on the dashboard below the profile area
- Shooting a trooper on a zipline now causes other troopers near it on the zipline to dismount as well
- Players can only participate in 4 Soul Orb share events per trooper wave, before being declared lower priority. A low priority player is not counted for when deciding how many souls to generate. Example: if a player is near 4 troopers from Wave 1 when they die, then moves to a different lane that has an allied hero still fighting Wave 1 troopers, that player will no longer cause the wave to double the souls generated as is the case now, as they are considered a low priority player for that wave. The generated Souls will then be split as normal.
- Reverted: - Guardians now deal 25% more damage to troopers
- Reverted: - Guardians now take 25% more damage from troopers/players
- Reverted: - Troopers now do 20% more damage to each other

**2024-11-29** ([forum post](https://forums.playdeadlock.com/threads/11-29-2024-update.49470/))

- Guardians now deal 25% more damage to troopers
- Guardians now take 25% more damage from troopers/players
- Range to be considered for souls reduced by 5m (The way it works now is there are two independent search ranges that gather nearby allied heroes to consider, the first is 50m from the orb itself, and the second is 35m from the hero that killed the trooper. The change reduces it by 5m on both. )

**2024-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2024-update.47476/))

- When queuing as a party, you will have an option to override the default balance oriented lane assignment system and make the system prioritize putting your party members in the same lanes together.
- Added Swap Lanes feature. During the rooftop and zipline phase at the start of the game, you can now request to swap lanes with your teammates by clicking the button below their portrait on the scoreboard. If the other player accepts your request, you will immediately be swapped. You may decline an incoming request by right clicking it.
- Visual update to Medicinal Specter to improve visibility
- Added effect to when the zipline ability first starts
- Related to the above, both patrons will now call out the Greenwich/Green Lane objectives specifically when they are destroyed
- Soul Sharing ratios post-lane reduced from 100/70/45/33/25/20% to 100/60/35/25/20/16%  (for 1/2/3/4/5/6 players, original was 100/50/33/25/20/16%)
- Middle Lane Walkers HP increased from 5800 to 8000 (side walkers HP is 5175)
- Mid Boss trooper health for first spawn reduced from 95% to 70%
- Trooper Spirit Resist at 25 minutes reduced from 30% to 20% (still scales to 70% at 50 minutes)
- Trooper soul changed from 60/40% in the kill/orb to 65/35%
- Medic Trooper now has 3 charges of heal rather than 2
- Air Drag when getting off the zipline increased from 20% to 25% (default in general is 20%)
- Previously was +2 Stamina, +3 Sprint, +30% Stamina Regen and +50% Zipline Boost for 160s.
- Now starts at "+1 Stamina, +2 Sprint, +20% Stamina Regen and +40% Zipline Boost" and ends at "+4 Stamina, +4 Sprint, +50% Stamina Regen and +80% Zipline Boost"
- Moved stairs up from the central canal to the Radio Station interior closer to the inner lanes
- Moved connection corridor between Inner and Outer lanes (Amber Yellow and Sapphire Purple) to be farther from the base entrances
- Changed entrance to the Armory/Warehouse from the inner lane to be more direct (not a hallway)
- Moved the side lane teleporters to the crawl space under the Hard camp
- New building facade art in Amber Blue and Purple lanes

**2024-11-13** ([forum post](https://forums.playdeadlock.com/threads/11-13-2024-update.46391/))

- Troopers now do 20% more damage to each other
- Soul Sharing ratios post-lane reduced from 100/75/50/35/28/22% to 100/70/45/33/25/20% (for 1/2/3/4/5/6 players)

**2024-11-10** ([forum post](https://forums.playdeadlock.com/threads/11-10-2024-update.45689/))

- Soul Sharing ratios post-lane reduced from 100/100/66/50/40/33% to 100/75/50/35/28/22% (for 1/2/3/4/5/6 players)

**2024-11-07** ([forum post](https://forums.playdeadlock.com/threads/11-07-2024-update.44786/))

- Fixed some cases where troopers could get stuck in the base
- Added new zipline animation for Vindicta
- Troopers no longer change soul sharing rules after laning phase ends (meaning 2 heroes don't split souls)
- Troopers no longer increase their bounty by 20% at 8 minutes
- Troopers now take 28% more damage from Guardians
- Moved 8 neutral camps (4 on each side) from outside the outer lanes behind the Walkers to in between inner and outer lanes
- Troopers Spirit resist goes to 30% instead of 40% at 25 minutes
- Mid Boss Rejuv Trooper Health increased by 30%
- Fixed Troopers resistance against Base Guardians not working properly

**2024-10-24** ([forum post](https://forums.playdeadlock.com/threads/10-24-2024-update.40951/))

- Bots are better at coming together to defend and push lanes
- Trooper Soul Orbs now have a 90ms buffer to allow the server to do better calculations on who shot the orb first, to minimize latency advantages for denying
- Trooper soul changed from 50/50% in the kill/orb to 60/40%
- Guardian resist vs troopers changed from starting at 70% and ending at -30% at 10 min to starting at 60% and ending at -35% at 8 minutes
- Walkers now have resist vs troopers starting at 60% and ending at -30% at 14 minutes
- Troopers now gain +40% Spirit Resist gradually over 25 minutes, goes to 70% at 50 minutes
- Backdoor protection detection range for troopers increased (harder to kill troopers approaching the objectives with long range spells to stall making the game think you are backdooring when you aren't)
- Medic Trooper heal now has 2 charges; time between casts is 6s [does not consume a charge when healing other troopers, mainly affects waves pushing on their own]
- Medic Trooper heal cooldown increased from 6s to 35s
- Redesigned stairs from central canal to the outer lanes (near Urn spawn)
- Added more zipline nodes to outer lanes

**2024-10-15** ([forum post](https://forums.playdeadlock.com/threads/10-15-2024-update.38925/))

- Range to attack lane Guardians increased from 19m to 20m

**2024-10-10** ([forum post](https://forums.playdeadlock.com/threads/10-10-2024-update.36958/))

- For private lobbies, added the ability to swap players on both teams with a button press. In addition players can be randomly shuffled across the two teams, and if lanes are being assigned, can be shuffled within the teams.
- Certain heroes now have a higher priority at being in dual lanes (Ivy and Dynamo atm)
- Fixed troopers being unreliable to shoot while on the zipline
- Fixed issues with Bots not using ziplines properly
- Adjusted Trooper tracer and muzzle effects for better alignment and lower visual noise
- Trooper death effects resolve quicker and more cleanly
- Troopers attack range vs Lane Guardians reduced from 13.5m to 12m (they get closer to it)
- Players now need to be within 19m (above the ramp) to attack a Lane Guardian
- Guardians now take 70% less damage from troopers at the start of the game; this reduces by 10% per minute (max at +30% increased damage at 10 min)
- Trooper spawn/bounty lane end time changed from 10 min to 8 min
- Shields no longer reduce damage or get depleted by NPC units (Troopers, Bosses etc, but still takes damage from player summoned units)
- Moved teleporters to travel between outer lane Walkers
- Added bridge and stair to the upper level of the Subway Entrance building from the outer lane Walker arenas

**2024-10-02** ([forum post](https://forums.playdeadlock.com/threads/10-02-2024-update.35439/))

- Zipline Boost cooldown reduced from 340s (5.6min) to 280s (4.6min)

**2024-09-29** ([forum post](https://forums.playdeadlock.com/threads/09-29-2024-update.34541/))

- Outer ziplines hero speed increased by 20% relative to inner lanes (same as troopers on outer lanes zipline being faster)

**2024-09-26** ([forum post](https://forums.playdeadlock.com/threads/09-26-2024-update.33015/))

- Added Zipline hotkey that can be independently bound from space/jump
- Private lobbies now allow picking specific lanes (solo and dual lane colors are displayed)
- Fixed jumping between ziplines consuming stamina
- Side lanes are now a little further apart from the middle lanes
- Lane setup is now always 1-2-2-1
- Zipline Boost now starts on cooldown again
- Trooper damage reduction from Guardians reduced from 35% to 28% (they die a little faster to Guardians now)
- Trooper share radius reduced (from allied hero to allied hero 50m->40m, from orb to allied hero 40m->35m)
- Troopers no longer give half bounty when base guardians are destroyed for that lane
- Added indicator on the hud to help track your passive cooldown items when they are 1s from ready (headshot Booster, Medic Bullets, etc)
- Outer lanes at the middle of the map pushed further away from the inner lanes
- Redesigned outer lane path (ziplines and trooper nodes) from Walker to Guardian on Amber Yellow and Sapphire Purple
- Added interior passage beside Subway Entrance to the outer lanes

**2024-09-19** ([forum post](https://forums.playdeadlock.com/threads/09-19-2024-update.31166/))

- Replaced the recent soul duplication hotfix with new behavior. Pre 10 min, lanes now always split orbs when there are more heroes than the assigned participants for that lane (3+ people in a dual lane, 2+ people in a solo). Previously it only split with 3+ people regardless of the lane, which is what allowed soul abuses when dipping into a solo lane.
- Private lobbies can now assign players to duo and solo lanes

**2024-09-17** ([forum post](https://forums.playdeadlock.com/threads/09-17-2024-update.30413/))

- Fixed players being able to exploit soul sharing across multiple lanes to earn more souls than intended. The way the fix is implemented is that each player can only be considered for an enemy trooper death event 4 times per wave number during the laning phase.
- Fixed troopers sometimes not dying after doing their death flash state

**2024-09-12** ([forum post](https://forums.playdeadlock.com/threads/09-12-2024-update.27974/))

- The Orange Lane (Orchard) is now the Green Lane (Greenwich)​
- The lane allocation of 1-1-2-2- and 2-2-1-1 will no longer be a possible setup
- Orange zipline is now green
- Displays extra information on HUD (ie. Zipline Speed Boost Cooldown) - we plan to expand upon this in future updates​
- Updated medic healing beam colors to be consistent with other heals
- Melee troopers no longer play swipe effect (to reduce some unnecessary noise)
- Melee trooper hitbox improved
- Fixed Medic Troopers sometimes using their heal on Guardian boss
- Angled the walkway connection from the outer lane exits to the inner lane exits

**2024-08-29** ([forum post](https://forums.playdeadlock.com/threads/08-29-2024-update.22253/))

- Added unavailable state to Zipline UI when zipline is on damage cooldown
- Fixed Zipline speed from Base Guardian killing and Zip booster ability not stacking properly
- Some heroes can now comment on being alone in enemy territory, losing sight of an injured enemy, or leaving their teammates alone in a lane
- Added 'Express' state to zipline indicators when speed had increased from defeating Enemy Base Guardians
- Moved a flex slot from "Set of enemy Base Guardians" to "All Enemy Lane Guardians"
- A pair of teleporters has been added to the outer lanes at the midpoint (near the three red neutral creeps)
- The half of the underground tunnel towards the outer lanes has been made wider
- Tunnel walls now have the color of the lane that the exit is closest to
- Lowered the statue pedestals in the inner lanes outside of Mid

**2024-08-15** ([forum post](https://forums.playdeadlock.com/threads/08-15-2024-update.16378/))

- Fixed Candle Troopers sometimes instantly disappearing on death rather than going into their death flash state
- Added one-way defender exits beside each outer lane entrance
- Added billboards to the edge closest to the lane
- Low roof buildings between inner lane Walker arenas are now valid play spaces

**2024-08-01** ([forum post](https://forums.playdeadlock.com/threads/08-01-2024-update.13369/))

- Adjusted Zipline camera positions for various heroes to help with visibility
- Fixed Candle Troopers near-death flash sometimes occurring while moving or doing other active animations
- Candle Trooper behind-wall HUD indicator now also shows near-death state
- Updated Wraith zipline animations
- Improved visibility of low health state on troopers about to die
- Reworked the location of the Walker on Amber Yellow and Sapphire Purple lanes. They are a little further towards the map edges. Nearby terrain has been reworked as well.
- Removed outer lane teleporters
- Added teleporters to areas between lanes (one in each quadrant). Total of 6 teleporters.
- Added connection from the underground teleport station to the outer lane Guardian (previously a juke spot)
- Each trooper you shoot at will now consider you a higher priority than Guardians/Walkers; that trooper will stop shooting the Guardians/Walkers and consider you its target for a few seconds
- Walker laser DPS vs troopers increased from 150 to 190
- Movement Powerup: Zipline bonus increased from 30% to 50%
- Reworked the climb-up exit from the Cosmic Veil space on the outer lanes
- Moved kiosk cover prop in the outer lanes to space out trooper paths

**2024-07-18** ([forum post](https://forums.playdeadlock.com/threads/07-18-2024-update.11831/))

- Reworked building just outside Amber's base in the Yellow lane to match Sapphire Purple
- Walker in mid lanes health increased by 12%
- Teleporter now has the same damage rules as zipline (DoT no longer prevents usage)
- Reduced the momentum coming off of the zipline a bit

**2024-07-11** ([forum post](https://forums.playdeadlock.com/threads/07-11-2024-update.10871/))

- Fixed Majestic Leap buff sticking around after attaching to zipline (caused audio bugs as well)
- Replaced item signs with new poster style and removed item signs on Yellow and Blue lanes
- Zipline Boost duration increased from 25s to 32s
- Trooper gold sharing radius from the location of the soul orb increased from 50m to 60m
- Redesigned interior of new stairwells beside inner lane Walkers

**2024-07-04** ([forum post](https://forums.playdeadlock.com/threads/07-04-2024-update.9652/))

- Parties will now be a little more likely to be in the same lane, if there isn't a wide skill gap or other factors preventing it
- Urn pickup location moved to closer to the outer lanes (on the opposite side of the lane pillar, facing towards the bridge)
- Urn now prevents you from using the zipline while carrying it
- Movement: +2 Stamina, +2 Sprint and +30% zipline boost for 100s
- Troopers now deal 25% less damage to other troopers
- Troopers spawn rate before 10 minutes is now the same as after 10 minutes (30s->25s)
- Inner lane Walker arena (Amber Orange and Sapphire Blue):
- Reworked stairs for defenders to reach the overpass to start near the Walker and exit with line of sight down the lane
- Moved the new cover barrier in front of the inner lane Guardian closer to the Guardian
- Medic Bullets: Renamed to Restorative Shot

**2024-06-27** ([forum post](https://forums.playdeadlock.com/threads/06-27-2024-update.8486/))

- Zipline Boost ability cooldown reduced from 380s to 340s
- Medic Trooper heal now bounces to up to one other allied hero within 25m from the hero
- Trooper gold sharing radius from the location of the allied hero reduced from 50m to 40m
- Creep waves now land at their lane destinations at the same time as each other
- Added connection hallway between outer lane Shop and crate room
- Extended alcove on outer lane cover position in front of the Shop

**2024-06-23** ([forum post](https://forums.playdeadlock.com/threads/06-23-2024-update.7705/))

- There is no longer a reinforcement trooper wave after Guardians and Walkers die

**2024-06-20** ([forum post](https://forums.playdeadlock.com/threads/06-20-2024-update.7003/))

- Updated the entrance to the underground tunnels from the outer lanes to look more like a subway entrance
- Added street names and symbols to the Zipline UI
- Added wind sound when on the Zipline
- 2) Between the exterior Strong Neutral Camps and the outer lane near the T2

**2024-06-13** ([forum post](https://forums.playdeadlock.com/threads/06-13-2024-update.5773/))

- Top bar now highlights your lane partner and lane enemies during the laning phase
- Added two new teleporters, one on each outer lane (behind the Chapel and behind the Firehouse)
- Post lane medic troopers will heal other troopers if a hero within range is full hp
- Post lane medic troopers' hero heal increased from 40 to 80
- Base zipline speed increased by 5%
- Medic Bullets: Healing from heroes increased from 25 to 30

**2024-06-07** ([forum post](https://forums.playdeadlock.com/threads/06-07-2024-update.4443/))

- Rejuv buff to candle troopers reduced from +100% HP to +50%

**2024-06-06** ([forum post](https://forums.playdeadlock.com/threads/06-06-2024-update.4096/))

- Candle trooper health bars now stick around at 1% when they are in self destruct mode to make it more clear they can still be shot
- Removed street lamp post that was causing heroes to get stuck near inner lane Guardian
- Added lights to outer lane Cosmic Veil tunnels
- Rejuv now causes all your candle troopers to have double health for 3 minutes
- Moved the middle lane Base Guardians further out slightly

**2024-05-30** ([forum post](https://forums.playdeadlock.com/threads/05-30-2024-update.2514/))

- Bots will now replace a human player if the player has been disconnected for more than 30 seconds (hero will retreat home first and then after 30 seconds the bot takes over). After 4 minutes it will start using souls to buy items. During laning phase it will go to its assigned lane, afterwards it will aim to stick near where most allies are located. If the player rejoins the bot will leave. We will work on improving the bot behavior as we get feedback.
- Candle Troopers and other NPCS can no longer see or shoot through Cosmic Veils
- Updated Zipline Boost hint to say ACTIVE when it is active and only show the cooldown timer when its done
- Fixed getting stuck going up the ramp on the inner lane street
- Lane Guardian HP increased from 3750 to 4600
- Various adjustments to lane layout to give defenders more options for forward positions near their Guardian
- Added breakable crates inside each lane's Cosmic Veil
- Expanded space in some of the lane's Cosmic Veils
- Base zipline speed increased by 10%
- Extended inner lane urn bridge buildings toward the T1 and added a doorway to allow defenders to shoot down into the canal
- Removed 3 bush trees on each inner lane near the urn bridge buildings
- Carved out interior of inner lane tower buildings beside the Guardian and connected to the neutral camp in the underground areas
- Moved outer lane Walker on Factory and Mansion sides slightly closer to the stairs
- Carved out interior of outer lane wall buildings beside the Walker to allow forward position for defenders

**2024-05-23** ([forum post](https://forums.playdeadlock.com/threads/05-23-2024-update.1245/))

- Updated Trooper and Neutral shooting sound effects
- Fixed upgrading McGinnis’s Medicinal Specter to T3 while active causing it to heal everyone to full instantly
- Fixed getting stuck under stair at inner lanes near Guardian
- Adjusted map around the middle lanes to have an area with Veils for laning
- Starting at 15 minutes, one melee Trooper per wave will spawn with 1.75x health
- Medic Trooper health increased from 240 to 260
- Zipline Boost ability speed increased from 100% to 130%
- Zipline Boost ability ramp time to reach max speed reduced from 2s to 1s
- Zipline base speed boost after Base Guardians are killed increased from 100% to 120%
- Zipline base speed boost's ramp time after Base Guardians are killed reduced from 5s to 4s

**2024-05-16** ([forum post](https://forums.playdeadlock.com/threads/05-16-2024-update.902/))

- Added clips to both sides of the overpass on outer lanes to keep from hitting your head on the ledge when climbing
- Added clips at outer lane T1 stairs where you could get stuck doing a roll slide
- Added a wall between the T1 shop and the hallway on the outer lanes by the Fire House and the Chapel to prevent attackers from shooting the T1 without taking damage
- Zipline Boost ability is now available at the start of the game (used to start on cooldown)
- Troopers run speed increased from 10 m/s to 11 m/s
- Medic Trooper health increased from 200 to 240
- Medic Bullets: Cooldown reduced from 5s to 4s

**2024-05-13** ([forum post](https://forums.playdeadlock.com/threads/05-13-2024-update.807/))

- Sandbox mode now has troopers spawning on the left side
- You can now see an indicator for enemy troopers when near them if they are behind a wall or offscreen (primarly improves tracking their positions during the lane)
- Medic Troopers no longer use their heal on troopers if there is a hero within 30m
- Zipline Speed Boost cooldown reduced from 420s to 380s
- Damage over time no longer prevents zipline usage
- Adjusted how the Anti Backdoor system works. It does a little less % damage reduction now, but it regens “backdoor damage” dealt to it over time. Backdoor damage is defined as any damage taken with no candle troopers within 50m in the last 20 seconds.
- Troopers run speed increased from 9.1 m/s to 10 m/s
- Troopers DPS vs Patrons reduced from 110 DPS to 80 DPS
- Troopers DPS vs Walkers from 110 DPS to 80 DPS
- Troopers DPS vs Base Guardians from 110 DPS to 80 DPS
- Crate Powerups: Removed Zipline buff as a potential drop

**2024-05-03** ([forum post](https://forums.playdeadlock.com/threads/05-03-2024-update.427/))

- Troopers DPS vs Lane Guardians reduced from 44 to 36
- The uncapturable zipline nodes near your base now extend out 2 more nodes (this means attackers can't capture ziplines quite as close to the enemy base)
