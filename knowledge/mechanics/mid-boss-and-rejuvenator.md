# Mid Boss and Rejuvenator

Generated from the game files at build 6868 and Valve's patch notes. Everything below is quoted from a source, not interpreted. Patch notes describe the game as of their date: read newest first, and treat an older line as history once a newer one changes the same thing.

## What the game itself says

- Heavy Melee to claim Rejuvenator (`AbilityButtonHint_MeleeRejuvinator`)
- Rejuvenator Already Owned - Will go to Ally (`AbilityButtonHint_RejuvenatorOwned`)
- Temple Guardian (`Citadel_AttackerClass_CLASS_SUPER_NEUTRAL`)
- Captured Rejuvenator (`Citadel_HUD_RejuvCaptured`)
- Stole Rejuvenator! (`Citadel_HUD_RejuvStolen`)
- Haunt MidBoss has been defeated (`Citadel_Steamshare_Desc_Neutral_ObjectiveDestroyed_MidBoss`)
- Haunt MidBoss (`Citadel_Steamshare_Title_Neutral_ObjectiveDestroyed_MidBoss`)
- Out of Range (`Objective_Message_MidBoss_OutOfRange`)
- Time remaining on active rejuvenators, or MidBoss respawn if no rejuvenators are active. (`citadel_rejuvenator_hud_hint`)
- The middle of the map has a powerful neutral boss. The team that kills it will have immediate respawns on their next deaths. (`guide_the_map_midboss_desc`)
- Mid Boss Charge (`super_neutral_charge`)
- Mid Boss Gun (`super_neutral_gun`)

## Current numbers in the game files

`RejuvParams`

| Field | Value |
|---|---|
| RejuvinatorBuffDuration | 180 |
| RejuvinatorDropDuration | 7.5 |
| RejuvinatorDropCount | 3 |
| RejuvinatorBreakGold | 500 |
| RejuvinatorBreakGoldPerMinute | 9 |
| TrooperHealthMult | 1.7 / 2 / 2.3 |
| PlayerRespawnMult | 0.5 / 0.4 / 0.3 |
| RejuvinatorRebirthDuration | 180 / 180 / 180 |

`npc_super_neutral`

| Field | Value |
|---|---|
| BoundAbilities.ESlot_Signature_1.AbilityProperties.AbilityCooldown | 1 |
| BoundAbilities.ESlot_Signature_1.AbilityProperties.ShieldHealth | 10000 |
| BoundAbilities.ESlot_Signature_1.AbilityProperties.ShieldScale | 2.5 |
| BoundAbilities.ESlot_Signature_1.Weapon.BulletsPerShot | 1 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.AbilityCooldown | 10 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.PrepareTime | 0.8 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.TackleDurationMin | 0.5 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.TackleDurationMax | 1 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.TackleSpeed | 25.4 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.Damage | 120 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.StunDuration | 0.5 |
| BoundAbilities.ESlot_Signature_2.Weapon.BulletsPerShot | 1 |
| DyingDuration | 1.4 |
| HealthGainPerMinute | 234 |
| IntrinsicModifiers[0].HEALTH_REGEN_PER_SECOND | 15 |
| IntrinsicModifiers[0].BULLET_ARMOR_DAMAGE_RESIST | 15 |
| IntrinsicModifiers[0].STATUS_RESISTANCE | 35 |
| IntrinsicModifiers[0].RESIST_REDUCTION_RESISTANCE | 50 |
| IntrinsicModifiers[1].DamageResistancePerSecond | 35 |
| IntrinsicModifiers[1].TickInterval | 0.05 |
| IntrinsicModifiers[1].DamageResistanceBonusPerGameMinute | 5 |
| ShieldLogic.BaseAbsorptionPerSecond | 35 |
| ShieldLogic.ScalingAbsorptionPerMinute | 5 |
| SpawnInterval | 420 |
| StartingHealth | 15600 |
| Weapon.BulletDamage | 20 |
| Weapon.RoundsPerSecond | 5 |
| Weapon.BulletsPerShot | 1 |
| Weapon.DPS | 100 |
| Weapon.SustainedDPS | 100 |

`neutral_camp_midboss`

| Field | Value |
|---|---|
| SpawnIntervalChange | -60 |
| SpawnIntervalMin | 300 |
| SpawnIntervalInSeconds | 420 |

`citadel_item_pickup_rejuv`

| Field | Value |
|---|---|
| RebirthModifier.RespawnLifePct | 100 |
| RebirthModifier.RespawnDelay | 3 |
| PunchPickupModifier.NearRejuvAuraModifier.AuraRadius | 300 |
| PunchPickupModifier.ParryCheckModifier.ParryCheckRadius | 80 |

## Patch history (96 lines, newest first)

**2026-06-30** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1836506165563227))

- Rejuv buff duration reduced from 4 minutes to 3

**2026-05-22** ([forum post](https://forums.playdeadlock.com/threads/05-22-2026-update.135477/))

- Midboss now starts spawned at the beginning of the game

**2026-03-06** ([forum post](https://forums.playdeadlock.com/threads/03-06-2026-update.114328/))

- Mid Boss base bounty increased from 2000 to 3000
- Mid Boss base HP increased from 11900 to 13000
- Mid Boss global announcement health threshold reduced from 70% to 50%
- Mid Boss now has 35% Debuff Resistance
- Rejuv drop duration reduced from 7s to 6s
- Rejuv duration no longer refreshes when hitting a crystal later

**2025-12-03** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/post-174987))

- Walkers and Mid Boss now have +15% Bullet Resistance and -15% HP

**2025-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/))

- Rejuv buff no longer grants +10% Max HP, +15% Fire Rate and +15% Spirit Damage Amp
- Mid Boss base health increased from 13000 to 14000
- Mid Boss health growth per minute increased from 200 to 230
- Team that kills Mid Boss gets +2 permanent buffs for each player

**2025-10-02** ([forum post](https://forums.playdeadlock.com/threads/10-02-2025-update.84332/))

- Mid Boss base HP increased from 12500 to 13000
- Mid Boss damage resistance per second reduced from 50 + 7/min to 35 + 5/min
- Rejuv bonus HP reduced from 15% to 10%
- 2nd Midboss rejuv credits reduced from 4 to 3

**2025-09-04** ([forum post](https://forums.playdeadlock.com/threads/09-04-2025-update.80693/))

- Rejuv only heals the person hitting the crystal

**2025-08-08** ([forum post](https://forums.playdeadlock.com/threads/07-29-2025-update.72760/post-141214))

- Rejuv now drops 1 crystal again, with each heavy melee hit granting a credit to the team (up to 3 for first midboss, and 4 for subsequent ones). Everyone on the team gains the buff. Whenever an ally dies, they respawn in place, lose the buff and your team rejuv credits get reduced by 1 (an ally can only consume one rejuv credit). The top bar has a UI indicator for how many rejuv credits remain. When all rejuv credits are used, the buff disappears for everyone.

**2025-08-01** ([forum post](https://forums.playdeadlock.com/threads/07-29-2025-update.72760/post-139997))

- Rejuv buff duration reduced from 7 minutes to 5 minutes

**2025-07-29** ([forum post](https://forums.playdeadlock.com/threads/07-29-2025-update.72760/))

- Mid Boss HP is now fixed at the spawn time. Base HP increased from 6725 to 12500 and growth reduced from 470 to 200.
- Reworked Rejuv reward from Mid Boss. No longer buffs troopers, reduces respawn time and buffs various stats. Upon death, 3 rejuv crystals fall to the ground (4 for subsequent midboss kills). Claiming one now grants you in place revive after 3s. If you already claimed one and claim another, it'll go to an ally (priority is closest allies first, then most recent dead allies). Dying with Rejuv no longer counts as a kill/death nor gives out bounties. While you have the Rejuv buff, you gain the following: +20% Max HP, +20% Fire Rate, and +15% Spirit Damage. Gaining the buff heals you to full and lasts up to 7 minutes.

**2025-07-04** ([forum post](https://forums.playdeadlock.com/threads/07-04-2025-update.70156/))

- Rejuv bonus duration changed from 4 minutes to 3/4/5
- Rejuv trooper health bonus reduced from 200/230/260% to 170/200/230%
- Mid Boss total bounty increased from 500 + 50/min to 2000 + 50/min (evenly split among the team that kills the boss, unrelated to rejuv secure)
- Mid Boss shield regeneration changed from 100 + 8/min to 50 + 7/min
- Mid Boss HP increased by 15%
- Mid Boss warning sound now plays at 70% HP rather than 60%
- Rejuv drop duration reduced from 8s to 7s
- Mid Boss Spirit Resistance from abilities reduced from 30% to 20%
- Mid Boss Spirit Resistance from items reduced from 50% to 20%
- Fixed some AoE abilities not hitting midboss (Kelvin Frost Grenade, Lady Geist Blood Bomb, Holliday Barrel)

**2025-06-17** ([forum post](https://forums.playdeadlock.com/threads/06-17-2025-update.68401/))

- Removed the rope entrances to Mid Boss.
- Added stairway entrance to Mid Boss.
- Veil areas connect to Mid Boss.
- Mid Boss Changes:
- Started Mid Boss Sewer theming.
- Added connection from the rope shafts to upper area of Mid Boss.
- Increase height of entrances to rope shafts from Mid Boss.
- Rejuv drop duration reduced from 9s to 8s

**2025-05-27** ([forum post](https://forums.playdeadlock.com/threads/05-27-2025-update.66453/))

- Improved lighting in Mid Boss area

**2025-05-11** ([forum post](https://forums.playdeadlock.com/threads/05-11-2025-update.64113/))

- Tankbuster: Fixed working on mid boss and objectives

**2025-04-04** ([forum post](https://forums.playdeadlock.com/threads/04-04-2025-update.60284/))

- Fix an edge case where a player can claim the Rejuv but also get parried

**2025-01-12** ([forum post](https://forums.playdeadlock.com/threads/01-12-2025-update.53389/))

- Alchemical Fire: Effectiveness reduction (40%) vs buildings/midboss now affects the Weapon Damage bonus too (instead of just DPS)

**2024-12-06** ([forum post](https://forums.playdeadlock.com/threads/12-06-2024-update.50599/))

- Fixed rejuv collect sound playing from wrong location in hero sandbox
- Lash: Death Slam fixed a rendering issue that could lead to crashes, especially in tight spaces like Mid Boss arena

**2024-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2024-update.47476/))

- Gaining Rejuvenator buff now shows what stats have been improved on your hero (like powerups and other buffs)
- Mid Boss trooper health for first spawn reduced from 95% to 70%

**2024-11-07** ([forum post](https://forums.playdeadlock.com/threads/11-07-2024-update.44786/))

- Mid Boss Rejuv Trooper Health increased by 30%

**2024-10-24** ([forum post](https://forums.playdeadlock.com/threads/10-24-2024-update.40951/))

- Mid Boss respawn timer decreases with subsequent boss kills, from 7 to 7/6/5 minutes

**2024-10-10** ([forum post](https://forums.playdeadlock.com/threads/10-10-2024-update.36958/))

- Mid Boss now has 15 regen
- Mid Boss creep buff rescaled from 70% to 50/70/90% for the 1/2/3rd mid boss death (further deaths don't increase)
- Mid Boss rejuv respawn rescaled from 50% to 40/50/60% for the 1/2/3rd mid boss death (further deaths don't increase)
- Vindicta: Crow Familiar % damage no longer affects Mid Boss

**2024-09-26** ([forum post](https://forums.playdeadlock.com/threads/09-26-2024-update.33015/))

- Added frosted shell effect on the rejuv crystal when Frozen Shelter is active
- Updated Rejuvenator buff effect
- Rejuv bonus creep HP increased from 50% to 70%
- Rejuv bonus is no longer consumed for dead players, they have it on their next life now
- Added Rejuv drop on a loop in the sandbox mode

**2024-09-12** ([forum post](https://forums.playdeadlock.com/threads/09-12-2024-update.27974/))

- Adjusted Midboss low health roar sound to be more distinct from spawn sound
- Mid Boss warning now happens at 60% instead of 50%
- Abrams: Fixed Seismic Impact getting stuck on ceilings like in the mid boss room
- Kelvin: Objectives and Rejuvenator are now frozen and invulnerable when under frozen shelter

**2024-08-01** ([forum post](https://forums.playdeadlock.com/threads/08-01-2024-update.13369/))

- Rejuv bonus reduced from 75% to 50% respawn time reduction
- Mid Boss health gained per minute increased from 350 to 425

**2024-07-23** ([forum post](https://forums.playdeadlock.com/threads/07-23-2024-update.12505/))

- Mid Boss starting health increased from 5000 to 6000
- Mid Boss health gained per minute increased from 275 to 350
- Mid Boss warning sound now plays at 50% HP

**2024-07-18** ([forum post](https://forums.playdeadlock.com/threads/07-18-2024-update.11831/))

- Added Midboss arrive, low health, and death sound effects
- Mid Boss starting health increased from 4500 to 5000
- Mid Boss health gained per minute increased from 200 to 275
- Rejuv drop time reduced from 12.5s to 9s
- Midboss makes a global sound when at 35% hp
- McGinnis: Spectral Wall segments that are touching the Rejuv will be destroyed

**2024-07-11** ([forum post](https://forums.playdeadlock.com/threads/07-11-2024-update.10871/))

- Added a visual effect when the Rejuvenator is attackable

**2024-07-04** ([forum post](https://forums.playdeadlock.com/threads/07-04-2024-update.9652/))

- Added a shatter sound effect for meleeing the mid boss rejuvenator
- Added rejuvenator pickup sound

**2024-06-27** ([forum post](https://forums.playdeadlock.com/threads/06-27-2024-update.8486/))

- Fixed an issue where the Rejuvenator being stolen was firing incorrectly
- Rejuvenator now reduces players' next respawn time by 75% instead of giving a 3s respawn time
- McGinnis: Fixed a bug with Spectral Wall that caused the Rejuvenator to instantly drop

**2024-06-20** ([forum post](https://forums.playdeadlock.com/threads/06-20-2024-update.7003/))

- Rejuv buff is now only granted to the players that are alive. Players that are dead will have their respawn times cut in half from their current values.

**2024-06-13** ([forum post](https://forums.playdeadlock.com/threads/06-13-2024-update.5773/))

- Fixed Dynamo's Singularity moving the Mid Boss
- Rejuvenator is no longer area pick up and now requires someone to heavy melee it to pick it up after it's dropped to the ground
- Rejuvenator will no longer stop dropping if it touches player created geometry (like Ice Dome) and always goes down to the target position

**2024-06-07** ([forum post](https://forums.playdeadlock.com/threads/06-07-2024-update.4443/))

- Rejuv buff to candle troopers reduced from +100% HP to +50%
- Fixed rejuv buff applying to objectives

**2024-06-06** ([forum post](https://forums.playdeadlock.com/threads/06-06-2024-update.4096/))

- Rejuv duration reduced from 4 to 3 minutes
- Rejuv buff no longer increases your ammo
- Rejuv now causes all your candle troopers to have double health for 3 minutes
- Mid Boss can now only be damaged by enemies inside the bottom pit
- Mid Boss Rejuv claim time reduced from 2.5s to 1.5s
- Mid boss area has reduced destructibles

**2024-05-23** ([forum post](https://forums.playdeadlock.com/threads/05-23-2024-update.1245/))

- Fixed the Rejuvenator falling during pause
- Mid-Boss is now invulnerable if there are no enemies it can actually attack

**2024-05-16** ([forum post](https://forums.playdeadlock.com/threads/05-16-2024-update.902/))

- Patrons will now play a voice warning when Rejuvenator time is close to expiring as well as when it's expired

**2024-05-13** ([forum post](https://forums.playdeadlock.com/threads/05-13-2024-update.807/))

- Paradox: Time Wall no longer deals damage to Mid Boss
