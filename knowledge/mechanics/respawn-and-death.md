# Respawn timers and death

Generated from the game files at build 6868 and Valve's patch notes. Everything below is quoted from a source, not interpreted. Patch notes describe the game as of their date: read newest first, and treat an older line as history once a newer one changes the same thing. The patch notes do not record every change, so where a current number below differs from the newest note, the number is right. Questions already worked through are answered in [settled.md](../settled.md).

## What the game itself says

- (Last Death) (`Citadel_HUD_DamageReport_LastRespawn`)
- You are about to respawn... (`Citadel_Notification_About_To_Respawn_Message`)
- Respawn Time (`Citadel_Notification_About_To_Respawn_Title`)
- You respawned (`Citadel_Steamshare_Desc_Respawn_Player`)
- Respawn Bonus Health Duration (`RespawnBonusHealthDuration_label`)
- Respawn Bonus Health (`RespawnBonusHealth_label`)
- Rebirth Health (`RespawnHealthPercent_label`)
- Rebirth Health (`RespawnHealthPercent_postvalue_label`)
- Respawn Time (`RespawnTime_label`)
- Respawn Time (`RespawnTime_postvalue_label`)
- Deadhead Revives (`SkullRevives_label`)
- Deadhead Revives (`SkullRevives_postvalue_label`)

## Current numbers in the game files

Server settings (`convars.json`)

| Setting | Value |
|---|---|
| citadel_player_death_no_heroes_respawn_penalty | 10 |
| citadel_player_spawn_time_in_base_penalty | 10 |
| citadel_player_spawn_time_max_ramp_1 | 38 |
| citadel_player_spawn_time_max_ramp_1_time | 1200 |
| citadel_player_spawn_time_max_ramp_2 | 70 |
| citadel_player_spawn_time_max_ramp_2_time | 1800 |
| citadel_player_spawn_time_max_ramp_3 | 85 |
| citadel_player_spawn_time_max_ramp_3_time | 2400 |
| citadel_player_spawn_time_max_respawn_time | 90 |
| citadel_player_spawn_time_min_ramp_1 | 8 |
| citadel_player_spawn_time_min_ramp_1_time | 300 |
| citadel_player_spawn_time_min_ramp_2 | 38 |
| citadel_player_spawn_time_min_ramp_2_time | 1200 |
| citadel_player_spawn_time_min_ramp_3 | 70 |
| citadel_player_spawn_time_min_ramp_3_time | 1800 |
| citadel_player_spawn_time_rich_nw_penalty_max_ramp_behind_nw_pct | 20 |
| citadel_player_spawn_time_rich_nw_penalty_max_ramp_extratime | 22 |
| citadel_player_spawn_time_rich_nw_penalty_max_ramp_gametime | 1500 |
| citadel_player_spawn_time_rich_nw_penalty_max_ramp_pct | 30 |
| citadel_player_spawn_time_rich_nw_penalty_min_ramp_behind_nw_pct | 5 |
| citadel_player_spawn_time_rich_nw_penalty_min_ramp_extratime | 6 |
| citadel_player_spawn_time_rich_nw_penalty_min_ramp_gametime | 600 |
| citadel_player_spawn_time_rich_nw_penalty_min_ramp_pct | 15 |
| citadel_tier3_phase1_kill_respawn_reduction | 20 |
| citadel_tier3_phase1_kill_respawn_reduction_limit | 10 |

## Patch history (46 lines, newest first)

**2026-09-16** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1844115010490072))

- Respawn Time at 20 minutes increased from 35s to 38s (does not affect the max values later on, just a little higher earlier)
- Breakables in the underground tunnels respawn rate increased from 3m to 5m

**2026-06-30** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1836506165563227))

- Respawn ramp changed from 8-30s from 5-19m to 8-35s from 5-20m

**2026-01-20** ([forum post](https://forums.playdeadlock.com/threads/12-29-2025-update.95233/post-185824))

- Respawn time at 19 minutes reduced from 35s to 30s
- Respawn time at 30 minutes reduced from 75s to 70s
- You now have a longer respawn time if you die and are meaningfully richer than the enemy team's average net worth (scales from +6s to +22s penalty, based on networth being 15 to 30% higher and game time being 10min to 25min, if under 15% NW or 10min, nothing happens)
- Neutral respawn times, hp, and bounty reduced by 30% (sinner's sacrifice unaffected)

**2025-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/))

- Small neutral camps respawn time 180s to 120s

**2025-09-04** ([forum post](https://forums.playdeadlock.com/threads/09-04-2025-update.80693/))

- Dying to a non-player (when there is no bounty/assists) now increases the respawn time for that death by 10 seconds

**2025-08-08** ([forum post](https://forums.playdeadlock.com/threads/07-29-2025-update.72760/post-141214))

- Rejuv now drops 1 crystal again, with each heavy melee hit granting a credit to the team (up to 3 for first midboss, and 4 for subsequent ones). Everyone on the team gains the buff. Whenever an ally dies, they respawn in place, lose the buff and your team rejuv credits get reduced by 1 (an ally can only consume one rejuv credit). The top bar has a UI indicator for how many rejuv credits remain. When all rejuv credits are used, the buff disappears for everyone.

**2025-07-29** ([forum post](https://forums.playdeadlock.com/threads/07-29-2025-update.72760/))

- Reworked Rejuv reward from Mid Boss. No longer buffs troopers, reduces respawn time and buffs various stats. Upon death, 3 rejuv crystals fall to the ground (4 for subsequent midboss kills). Claiming one now grants you in place revive after 3s. If you already claimed one and claim another, it'll go to an ally (priority is closest allies first, then most recent dead allies). Dying with Rejuv no longer counts as a kill/death nor gives out bounties. While you have the Rejuv buff, you gain the following: +20% Max HP, +20% Fire Rate, and +15% Spirit Damage. Gaining the buff heals you to full and lasts up to 7 minutes.
- Medium Neutrals respawn rate increased from 360s to 420s (+17%)
- Strong Neutrals respawn rate increased from 480s to 600s (+25%)
- Minor respawn curve reductions (19 min from 40s to 35s, 30 min from 80s to 75s, 40 min is still 85s)

**2025-03-16** ([forum post](https://forums.playdeadlock.com/threads/03-16-2025-update.58880/))

- Sinner's Sacrifice initial spawn time reduced from 10 min to 8 min (respawn rate is still 5 min)

**2025-03-13** ([forum post](https://forums.playdeadlock.com/threads/03-13-2025-update.58592/))

- Sinner's Sacrifice spawn/respawn time increased from 8/4 minutes to 10/5
- Mid Neutral Camp respawn time increased from 5 minutes to 6 minutes
- Minor respawn curve adjustments

**2024-11-29** ([forum post](https://forums.playdeadlock.com/threads/11-29-2024-update.49470/))

- Respawn time at 40 minutes moved to 35 minutes

**2024-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2024-update.47476/))

- Fixed respawn music cue failing to play with shop menu open
- Respawn time curves changed from happening at 17/30 minutes for 40s/70s respawn to 20/40 minutes
- Killing the first Patron now causes any existing enemy hero respawns to be reduced by 20 seconds. However, it does not reduce remaining respawn time lower than 10s.

**2024-11-07** ([forum post](https://forums.playdeadlock.com/threads/11-07-2024-update.44786/))

- Minor adjustments to respawn curve (40s respawn happening at 20m now happens at 17m)

**2024-10-24** ([forum post](https://forums.playdeadlock.com/threads/10-24-2024-update.40951/))

- Flash Windows Taskbar icon if the game window isn't in focus and you have 3 seconds until you respawn
- Enabled certain music cues like 'respawn' to interrupt base attack music
- Mid Boss respawn timer decreases with subsequent boss kills, from 7 to 7/6/5 minutes
- The 70s respawn time now happens at 30 min instead of 35 min
- There is now a respawn curve that goes from 70s to 75s over 30->40 minutes

**2024-10-15** ([forum post](https://forums.playdeadlock.com/threads/10-15-2024-update.38925/))

- Respawn time at 20 minutes reduced from 45s to 40s

**2024-10-10** ([forum post](https://forums.playdeadlock.com/threads/10-10-2024-update.36958/))

- Fixed respawn music not playing while spectating another player
- Mid Boss rejuv respawn rescaled from 50% to 40/50/60% for the 1/2/3rd mid boss death (further deaths don't increase)

**2024-10-02** ([forum post](https://forums.playdeadlock.com/threads/10-02-2024-update.35439/))

- Respawn time at 20min reduced from 50s to 45s (was 40s previous patch)

**2024-09-29** ([forum post](https://forums.playdeadlock.com/threads/09-29-2024-update.34541/))

- Initial respawn reduced from 12s to 8s

**2024-09-26** ([forum post](https://forums.playdeadlock.com/threads/09-26-2024-update.33015/))

- Added a Soul Generator (like the one in hero sandbox) in the respawn area. Starts spawning orbs at 3 minutes. Each orb is worth 10 souls when shot. (primary purpose for this is cases when you are very close to an item purchase)
- Midgame respawn time increased a bit (reaches 50s at 20 min instead of 40s at 20 min)

**2024-09-12** ([forum post](https://forums.playdeadlock.com/threads/09-12-2024-update.27974/))

- Added Rebirth channel and revive sounds
- Max respawn time now happens at 35 minutes rather than 40 minutes

**2024-08-29** ([forum post](https://forums.playdeadlock.com/threads/08-29-2024-update.22253/))

- Added new respawn countdown music 5 seconds before respawn

**2024-08-01** ([forum post](https://forums.playdeadlock.com/threads/08-01-2024-update.13369/))

- Rejuv bonus reduced from 75% to 50% respawn time reduction

**2024-07-18** ([forum post](https://forums.playdeadlock.com/threads/07-18-2024-update.11831/))

- Soul Rebirth (new T4 Vitality item): After you die, you will respawn in 4 seconds where you died with 40% of your Max Health. Cooldown: 220s. Also innately grants +20% Weapon Damage and +10% Cooldown Reduction.

**2024-07-11** ([forum post](https://forums.playdeadlock.com/threads/07-11-2024-update.10871/))

- Base respawn time increased from 8s to 12s (peak values unchanged)

**2024-07-04** ([forum post](https://forums.playdeadlock.com/threads/07-04-2024-update.9652/))

- Added a new Damage Report feature. You can now open a flyout panel within the shop to view a breakdown of your hero's incoming and outgoing damage throughout the course of a match. You can also hover an enemy hero to view a quick breakdown of their key stats and items. The data can be filtered by last respawn, 10 minutes, 5 minutes, 3 minutes, 1 minute, or 30 seconds.

**2024-06-27** ([forum post](https://forums.playdeadlock.com/threads/06-27-2024-update.8486/))

- Rejuvenator now reduces players' next respawn time by 75% instead of giving a 3s respawn time

**2024-06-20** ([forum post](https://forums.playdeadlock.com/threads/06-20-2024-update.7003/))

- Rejuv buff is now only granted to the players that are alive. Players that are dead will have their respawn times cut in half from their current values.

**2024-06-06** ([forum post](https://forums.playdeadlock.com/threads/06-06-2024-update.4096/))

- Respawn rate for Destructibles/Statues (after initial spawn) slowed from 120s to 180s

**2024-05-16** ([forum post](https://forums.playdeadlock.com/threads/05-16-2024-update.902/))

- Respawn curve adjusted slightly (results in a few seconds of increased respawn time in the mid phase, same overall max respawn time)
