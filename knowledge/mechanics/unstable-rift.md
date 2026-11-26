# Unstable Rift

Generated from the game files at build 6868 and Valve's patch notes. Everything below is quoted from a source, not interpreted. Patch notes describe the game as of their date: read newest first, and treat an older line as history once a newer one changes the same thing. The patch notes do not record every change, so where a current number below differs from the newest note, the number is right. Questions already worked through are answered in [settled.md](../settled.md).

## What the game itself says

- Bloodthirsty (`Citadel_Drifter_HeroTag_2`)
- Rift Secured! (`Citadel_HUD_KothCompleted`)
- Rift Has Faded... (`Citadel_HUD_KothExpired`)
- Rift Faded Away... (`Citadel_HUD_KothTimeRanOut`)
- Time's Almost Up... (`Citadel_HUD_Koth_Time_Warning`)
- An Unstable Rift is Opening... (`Citadel_HUD_Koth_Warning`)
- Go to the Rift to claim its power (`Citadel_HUD_Koth_Warning_Desc`)
- Ability Kills (`Citadel_PostGame_AwardAbilityKills_RankOther`)
- Headshot Kills (`Citadel_PostGame_AwardHeadshotKills_RankOther`)
- Weapon Kills (`Citadel_PostGame_AwardWeaponKills_RankOther`)
- Drifter Nearby (`DrifterNearbyRangeCheck_label`)
- Drifter Nearby (`DrifterNearbyRangeCheck_postvalue_label`)
- Drifter Alt Weapon (`citadel_weapon_drifter_alt`)
- Crimson Grasp (`citadel_weapon_drifter_set`)
- Swipe at enemies in a cone ahead of you, dealing spirit damage. If the enemy is in close range, deal bonus melee damage. (`drifter_blood_blast_desc`)
- On Close Range (`drifter_blood_blast_header_on_close_range`)
- -8s Cooldown (`drifter_blood_blast_t2_desc`)
- Deals 55% Heavy Melee Damage Silences enemies for 2s if close range (`drifter_blood_blast_t3_desc`)
- Eternal Night (`drifter_darkness`)
- Surround nearby enemy heroes in darkness, severely limiting their vision of other units. Affected enemies are briefly revealed to you and are considered isolated for the duration. You gain bonus sprint speed. (`drifter_darkness_desc`)
- +2.75s Duration and +1 Max Target. (`drifter_darkness_t3_desc`)
- Shadow Slashes (`drifter_infinity_slash`)
- Deep's Embrace (`drifter_last_breath`)
- Encase yourself in a sphere of water that can absorb damage before bursting. When the sphere dissipates for any reason enemies in range take damage. (`drifter_last_breath_desc`)
- Stalker's Mark (`drifter_shadow_mark`)
- Send out a mark that bleeds the first target it hits, dealing spirit damage over time. While the enemy is bleeding you can re-activate Stalker's Mark to instantly appear behind their back. (`drifter_shadow_mark_desc`)
- -8% Bullet Resist (`drifter_shadow_mark_t1_desc`)
- -10s Cooldown and +3s Duration (`drifter_shadow_mark_t2_desc`)
- +1.5% Bleed and -40% Incoming Healing (`drifter_shadow_mark_t3_desc`)

## Current numbers in the game files

`KothParams`

| Field | Value |
|---|---|
| KothRadius | 20 |

Server settings (`convars.json`)

| Setting | Value |
|---|---|
| citadel_koth_early_warning_time | 60 |
| citadel_koth_respawn_interval | 420 |
| citadel_koth_reward_base | 1260 |
| citadel_koth_reward_buff_count | 0 |
| citadel_koth_reward_time_multiplier | 222 |
| citadel_koth_spawn_initial_delay | 720 |
| citadel_koth_spawn_window | 60 |
| citadel_koth_warning_time | 20 |

## Patch history (21 lines, newest first)

**2026-09-16** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1844115010490072))

- Unstable Rift comeback resist max values now scale over the course of the game. Previously the max values were 35%. Now it is 10% + 1% per minute (around ~20% for the first one), with an upper limit of 40% at 30 minutes.
- Removed a fixed amount of extra bonus souls you would get for being behind even a very slightly amount in net worth for both hero kill bounties as well as Unstable Rift bounties (this had a larger impact on the early to mid game)

**2026-07-09** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1836506165584438))

- Unstable Rift warning time reduced from 25s to 20s
- Rift Troopers now have Spirit Resist (30/35/40/45%)
- Rift Troopers now have Melee Resistance (25%)
- Rift Troopers spawn interval increased from every 0.3s to 0.5s (spawns slightly more staggered)
- Unstable Rift comeback resist aura radius increased from 20m to 35m
- Rift Troopers max comeback count increased from 12 to 14

**2026-06-30** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1836506165563227))

- King of the Hill objective has been rethemed and renamed to "Unstable Rift"
- Unstable Rift no longer requires an Urn delivery to trigger the start of the event. It now has a variable start time of +/- 1 minute. There is a global announcement 25s before it spawns. 60s before that there is also an in-world only visual effect to let you know which lane it'll randomly spawn in.
- Unstable Rift spawn interval increased from every 6 minutes to every 7 minutes
- Unstable Rift comeback bonuses (resists in the area, extra comeback bounty, and trailing/leading team claiming timer) now all scale linearly based on the amount of NW they are trailing (scales from no bonus at 0% NW behind to full bonus at 15% NW behind)
- The team that secures the Unstable Rift now also has a wave of 5 Rift Troopers sent down from the rift location. When trailing, spawns up to 12 troopers instead (using the same linear ramp from 0% NW to -15% NW)
- Rift Troopers drop no souls when killed
- Rift Troopers spawn with 100% extra health and damage (they also look larger and have custom VFX). Their bonus health and damage grow slightly per event (first one is 100%, then 120%, 140%, etc)
- Any players in the Unstable Rift Zone are now revealed on the minimap
- Unstable Rift bounty increased by 35% (to account for the 35% loss with no urn runner bounty, overall objective bounty is unchanged)
- Unstable Rift no longer grants +1 permanent buff to each player (there is also no +3 buffs to the urn runner)
- Urn runner's passive bonuses while holding it now scales based on how behind you are, rather than being on or off (same as the Unstable Rift 0%-15% NW linear scaling). Bonuses are the same as the previous urn runner bonuses.
- citadel_koth_dev_test_spawn - This moves your hero and spawns the Unstable Rift in the early warning state then quickly transitions to the 25s broadcasted timer

**2026-06-04** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1834602721188293))

- Delivering the urn now starts a king of the hill style capture point, rather than using melee to flip the urn back and forth.
