# Shrines and the Patron

Generated from the game files at build 6868 and Valve's patch notes. Everything below is quoted from a source, not interpreted. Patch notes describe the game as of their date: read newest first, and treat an older line as history once a newer one changes the same thing. The patch notes do not record every change, so where a current number below differs from the newest note, the number is right. Questions already worked through are answered in [settled.md](../settled.md).

## What the game itself says

- A gift from your Patron... (`Citadel_HUD_PatronBoon`)
- Your Patron has been destroyed (`Citadel_Steamshare_Desc_Allied_ObjectiveDestroyed_Patron`)
- Your Shrine has been destroyed (`Citadel_Steamshare_Desc_Allied_ObjectiveDestroyed_Shrine`)
- Enemy Patron has been destroyed (`Citadel_Steamshare_Desc_Enemy_ObjectiveDestroyed_Patron`)
- Enemy Shrine has been destroyed (`Citadel_Steamshare_Desc_Enemy_ObjectiveDestroyed_Shrine`)
- Allied Patron (`Citadel_Steamshare_Title_Allied_ObjectiveDestroyed_Patron`)
- Allied Shrine (`Citadel_Steamshare_Title_Allied_ObjectiveDestroyed_Shrine`)
- Enemy Patron (`Citadel_Steamshare_Title_Enemy_ObjectiveDestroyed_Patron`)
- Enemy Shrine (`Citadel_Steamshare_Title_Enemy_ObjectiveDestroyed_Shrine`)
- Enemy Patron (`Citadel_TeamMsg_EnemyTitanKilledTitle`)
- The Patron is Transforming... (`Objective_Message_Patron_Transforming`)
- Your team has defeated the enemy Patron (`team_msg_TheirTitanDefeated_Desc`)
- A Patron has been destroyed (`team_msg_TitanDefeated_Desc`)
- Patron destroyed (`team_msg_TitanDefeated_Title`)
- Your Patron has been destroyed (`team_msg_YourTitanDefeated_Desc`)

## Current numbers in the game files

`npc_boss_tier3`

| Field | Value |
|---|---|
| ArmAttackCooldownMax | 10 |
| ArmAttackCooldownMin | 4 |
| ArmAttackRadius | 3.81 |
| BackdoorProtection.HealthPerSecondRegen | 75 |
| BackdoorProtection.BackdoorProtectionDamageMitigationFromPlayers | 65 |
| BackdoorProtection.BackdoorProtectionDamageMitigationFromPlayers_Streetbrawl | 85 |
| BoundAbilities.ESlot_Weapon_Primary.Weapon.BulletDamage | 106 |
| BoundAbilities.ESlot_Weapon_Primary.Weapon.RoundsPerSecond | 1.8868 |
| BoundAbilities.ESlot_Weapon_Primary.Weapon.ClipSize | 16 |
| BoundAbilities.ESlot_Weapon_Primary.Weapon.BulletsPerShot | 1 |
| BoundAbilities.ESlot_Weapon_Primary.Weapon.DPS | 200 |
| BoundAbilities.ESlot_Weapon_Primary.Weapon.SustainedDPS | 178.9 |
| BoundAbilities.ESlot_Weapon_Primary.AbilityPointsCost | 1 |
| BoundAbilities.ESlot_Weapon_Primary.DOFWhileZoomed.DofNearCrisp | 200 |
| BoundAbilities.ESlot_Weapon_Primary.DOFWhileZoomed.DofFarCrisp | 100 |
| BoundAbilities.ESlot_Weapon_Primary.DOFWhileZoomed.DofFarBlurry | 7000 |
| BoundAbilities.ESlot_Signature_1.AbilityProperties.AbilityCastRange | 30.48 |
| BoundAbilities.ESlot_Signature_1.AbilityProperties.PathLength | 2000 |
| BoundAbilities.ESlot_Signature_1.AbilityProperties.PathWidth | 1.016 |
| BoundAbilities.ESlot_Signature_1.AbilityProperties.BulletArmorReduction | -10 |
| BoundAbilities.ESlot_Signature_1.AbilityProperties.TechArmorReduction | -10 |
| BoundAbilities.ESlot_Signature_1.Weapon.BulletsPerShot | 1 |
| BoundAbilities.ESlot_Signature_1.BeamModifier.LaserDPSToPlayers | 440 |
| BoundAbilities.ESlot_Signature_1.BeamModifier.LaserDPSMaxHealth | 5 |
| BoundAbilities.ESlot_Signature_1.BeamModifier.LaserDPSToNPCs | 80 |
| BoundAbilities.ESlot_Signature_1.BeamModifier.AuraDropTickRate | 0.5 |
| BoundAbilities.ESlot_Signature_1.BeamModifier.GroundAuraModifier.ModifierProvidedByAuraDuration | 4 |
| BoundAbilities.ESlot_Signature_1.BeamModifier.GroundAuraModifier.AuraRadius | 4.064 |
| BoundAbilities.ESlot_Signature_1.BeamModifier.GroundAuraModifier.modifierProvidedByAura.Duration | 4 |
| BoundAbilities.ESlot_Signature_1.BeamModifier.GroundAuraModifier.modifierProvidedByAura.TickRate | 0.5 |
| BoundAbilities.ESlot_Signature_1.BeamModifier.GroundAuraModifier.modifierProvidedByAura.NPCDPS | 80 |
| BoundAbilities.ESlot_Signature_1.BeamModifier.GroundAuraModifier.modifierProvidedByAura.PlayerDPS | 100 |
| BoundAbilities.ESlot_Signature_1.BeamModifier.GroundAuraModifier.modifierProvidedByAura.MaxHealthDPS | 4 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.AbilityCooldown | 1 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.AbilityCastRange | 25.4 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.AbilityCastDelay | 3.5 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.Damage | 300 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.DamageNonHero | 500 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.DamageHealthPercent | 20 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.SlowPercent | 24 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.SkipFrames | 6 |
| BoundAbilities.ESlot_Signature_2.Weapon.BulletsPerShot | 1 |
| BoundAbilities.ESlot_Signature_2.PreviewModifier.ShrineChargeOffset | 300 |
| BoundAbilities.ESlot_Signature_2.AoEModifier.modifierProvidedByAura.TossUpStrength | 400 |
| BoundAbilities.ESlot_Signature_2.AoEModifier.modifierProvidedByAura.TossHorizontalMin | 600 |
| BoundAbilities.ESlot_Signature_2.AoEModifier.modifierProvidedByAura.TossHorizontalMax | 1200 |
| BoundAbilities.ESlot_Signature_2.AoEModifier.modifierProvidedByAura.DebuffDuration | 3 |
| BoundAbilities.ESlot_Signature_3.AbilityProperties.AbilityCooldown | 4 |
| BoundAbilities.ESlot_Signature_3.AbilityProperties.SkipFrames | 6 |
| BoundAbilities.ESlot_Signature_3.AbilityProperties.SlowPercent | 24 |
| BoundAbilities.ESlot_Signature_3.Weapon.BulletsPerShot | 1 |
| BoundAbilities.ESlot_Signature_3.ProjectileInfos.primary.Speed | 40.64 |
| BoundAbilities.ESlot_Signature_3.CooldownMax | 12 |
| BoundAbilities.ESlot_Signature_3.CooldownMin | 6 |
| BoundAbilities.ESlot_Signature_3.DetonationTimeMax | 4 |
| BoundAbilities.ESlot_Signature_3.DetonationTimeMin | 4 |
| BoundAbilities.ESlot_Signature_3.BossHealthMax | 1 |
| BoundAbilities.ESlot_Signature_3.BossHealthMin | 0.2 |
| BoundAbilities.ESlot_Signature_3.BombDropDist | 400 |
| BoundAbilities.ESlot_Signature_3.ExplodeRadius | 16.51 |
| BoundAbilities.ESlot_Signature_3.BombOffsets | 300 |
| BoundAbilities.ESlot_Signature_3.BaseDamage | 300 |
| BoundAbilities.ESlot_Signature_3.DamageNonPlayer | 500 |
| BoundAbilities.ESlot_Signature_3.MaxHealthPctDamage | 0.2 |
| BoundAbilities.ESlot_Signature_3.DebuffDuration | 3 |
| BoundAbilities.ESlot_Signature_4.AbilityProperties.AbilityCooldown | 12 |
| BoundAbilities.ESlot_Signature_4.AbilityProperties.AbilityCastRange | 35.56 |
| BoundAbilities.ESlot_Signature_4.AbilityProperties.VolleyInterval | 0.5 |
| BoundAbilities.ESlot_Signature_4.AbilityProperties.GrenadesInVolley | 6 |
| BoundAbilities.ESlot_Signature_4.AbilityProperties.MaxSimultaneousVolley | 1 |
| BoundAbilities.ESlot_Signature_4.AbilityProperties.InitialVolleyInaccuracy | 100 |
| BoundAbilities.ESlot_Signature_4.AbilityProperties.PerVolleyInaccuracy | 25 |
| BoundAbilities.ESlot_Signature_4.AbilityProperties.Damage | 200 |
| BoundAbilities.ESlot_Signature_4.AbilityProperties.DetonateTimer | 10 |
| BoundAbilities.ESlot_Signature_4.AbilityProperties.FireDuration | 5 |
| BoundAbilities.ESlot_Signature_4.AbilityProperties.FireDPS | 25 |
| BoundAbilities.ESlot_Signature_4.AbilityProperties.FireTickInterval | 0.5 |
| BoundAbilities.ESlot_Signature_4.AbilityProperties.BulletArmorReduction | -10 |
| BoundAbilities.ESlot_Signature_4.AbilityProperties.TechArmorReduction | -10 |
| BoundAbilities.ESlot_Signature_4.Weapon.BulletsPerShot | 1 |
| BoundAbilities.ESlot_Signature_4.ProjectileInfos.primary.TrackingDuration | 1 |
| BoundAbilities.ESlot_Signature_4.ProjectileInfos.primary.TrackingStartTime | 1 |
| BoundAbilities.ESlot_Signature_4.ProjectileInfos.primary.TrackingEndTime | 2 |
| BoundAbilities.ESlot_Signature_4.ProjectileInfos.primary.GravityScale | 0.5 |
| BoundAbilities.ESlot_Signature_4.LaunchAngle | 45 |
| BoundAbilities.ESlot_Signature_4.AuraModifier.ModifierProvidedByAuraDuration | 4 |
| CoreRadius | 3.302 |
| CoreVerticalOffset | 350 |
| DefaultMoveSpeed | 5.08 |
| EnemyTrooperProtectionRange | 40 |
| LaserCooldownPhase1 | 10 |
| LaserCooldownPhase2 | 12 |
| LaserDurationPhase1 | 4.5 |
| LaserDurationPhase2 | 3 |
| LaserMoveSpeed | 5.08 |
| MaxHealth | 12000 |
| ObjectiveHealthGrowthPhase1.GrowthPerMinute | 250 |
| ObjectiveHealthGrowthPhase1.TickRate | 60 |
| ObjectiveHealthGrowthPhase1.GrowthStartTimeInMinutes | 20 |
| ObjectiveHealthGrowthPhase2.GrowthPerMinute | 450 |
| ObjectiveHealthGrowthPhase2.TickRate | 60 |
| ObjectiveHealthGrowthPhase2.GrowthStartTimeInMinutes | 1 |
| ObjectiveRegen.OutOfCombatHealthRegen | 120 |
| ObjectiveRegen.OutOfCombatRegenDelay | 20 |
| Phase1BossScale | 1 |
| Phase1DyingBegin | 5 |
| Phase1DyingDrop | 1 |
| Phase1DyingTransformUp | 4.1 |
| Phase1DyingWait | 3.4 |
| Phase1Modifier.PitRadius | 13.97 |
| Phase1ObserverPitch | 55 |
| Phase2BossScale | 1 |
| Phase2DamagePulseModifier.MaxTargets | 3 |
| Phase2DamagePulseModifier.Radius | 19.05 |
| Phase2DamagePulseModifier.DamagePerPulse | 75 |
| Phase2Health | 12000 |
| Phase2ObserverPitch | 50 |
| PostShrineTransition | 2 |
| RangedArmorModifier.BulletResistancePctMax | 100 |
| RangedArmorModifier.RangeMin | 25.4 |
| RangedArmorModifier.RangeMax | 50.8 |
| RotateSpeed | 0.00762 |
| ShrineAttackHealthLossPerAttack | 0.15 |
| ShrineAttackMinTimeBetweenAttacks | 10 |
| vPhase1ObserverOrigin | -600 / 0 / 2000 |
| vPhase2ObserverOrigin | -1000 / 0 / 1500 |

## Patch history (67 lines, newest first)

**2026-05-22** ([forum post](https://forums.playdeadlock.com/threads/05-22-2026-update.135477/))

- Shrines are now invulnerable until one pair of Base Guardians are destroyed
- Shrine Bullet Resistance increased from 10% to 20%

**2026-03-10** ([forum post](https://forums.playdeadlock.com/threads/03-06-2026-update.114328/post-220287))

- Super [[Trooper|troopers]] (when a lane [[Shrine|shrine]] is down) now have 15% less bounty
- Super troopers (when a lane shrine is down) now have 15% less bounty

**2026-03-06** ([forum post](https://forums.playdeadlock.com/threads/03-06-2026-update.114328/))

- Shrine is now easier to kill for the first one and harder for the second. HP from 8100 to 5000/10000 (HP updates after the first one dies, like Walkers)
- Shrines attack no longer hits heroes under the shrine
- Super troopers bonus DPS increased from +40% to +60% (the upgraded troopers when Shrine dies)
- Middle Lane troopers now gets upgraded when either of the shrines die, rather than only when both die
- Shrines bounty increased from 0 to 2000
- Added "0 Way" veils underneath the Shrine platforms in each base
- Moved the mid lane bridge above the Hidden King Base entrance more to the middle of the two edges
- [ General ] - Can now jump during slide - Dash jump grants a very brief period with increased air control (30% for 0.25s) - Shrine is now easier to kill for the first one and harder for the second. HP from 8100 to 5000/10000 (HP updates after the first one dies, like Walkers) - Shrines attack no...

**2026-02-12** ([forum post](https://forums.playdeadlock.com/threads/01-30-2026-update.102822/post-204182))

- Troopers now get stronger for the specific lane that the shrine died in, rather than only after both shrines died (when both die, middle lane also gets improved)
- Shrines HP reduced by 10%

**2025-12-17** ([forum post](https://forums.playdeadlock.com/threads/12-16-2025-update.93983/post-178389))

- Weakened Patron now gains 50% damage reduction if one defender is in the pit and 100% if two or more are (defenders must be in pit for at least 2s for reduction to kick in)

**2025-12-16** ([forum post](https://forums.playdeadlock.com/threads/12-16-2025-update.93983/))

- Shrines health increased from 3000 to 7000
- Killing both enemy shrines will now make all of your troopers stronger (30% hp and 30% damage)

**2025-09-04** ([forum post](https://forums.playdeadlock.com/threads/09-04-2025-update.80693/))

- Patron 1st death time is now a constant 12s instead of being variable between 8 and 15 seconds

**2025-05-27** ([forum post](https://forums.playdeadlock.com/threads/05-27-2025-update.66453/))

- Added news kiosk structure in between Mid Lane Walker and base entrance
- Added wall partition structures outside of Outer Lane base entrances

**2025-05-21** ([forum post](https://forums.playdeadlock.com/threads/05-21-2025-update.65674/))

- Moved Shrines away from the back walls a bit.
- Extended shrine low ground closer to the throne.

**2025-05-19** ([forum post](https://forums.playdeadlock.com/threads/05-19-2025-update.65381/))

- Distance allowed to shoot Shrines increased by 7m

**2025-04-17** ([forum post](https://forums.playdeadlock.com/threads/04-17-2025-update.61382/))

- Troopers that are attacking shrines are no longer distracted from their task by distant enemy troopers
- Troopers now know to cross the base and attack the other shrine once their near one is defeated

**2025-01-27** ([forum post](https://forums.playdeadlock.com/threads/01-27-2025-update.54590/))

- Shrines are no longer vulnerable to Spirit Damage when out of range (rather than only immune to bullet damage)

**2024-12-06** ([forum post](https://forums.playdeadlock.com/threads/12-06-2024-update.50599/))

- Patron HP reduced from 10k to 7.5k
- Downed Patron HP reduced from 18k to 13.5k
- Patron HP grows by 250/Min starting 20 min
- Downed Patron HP grows by 450/Min starting 20 min (overall, these are -25% HP at 20 min, 0% at 30 min, and +25% at 40 min)

**2024-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2024-update.47476/))

- Updated Patron VO to give the Amber Hand more lines that are unique to him as opposed to having the identical script of the Sapphire Flame (for instance, while the Sapphire Flame might praise Haze by saying "you are perfection, Haze", the Amber Hand would say "Haze will dance, and they will fall")
- Steam Game Recording timeline no longer records Shrine objectives as "The World"
- Patron Laser now also deals 3% Max HP DPS
- Flex Slot changed from All Shrines to 1 Shrine and 2 Base Guardians
- Killing the first Patron now causes any existing enemy hero respawns to be reduced by 20 seconds. However, it does not reduce remaining respawn time lower than 10s.
- Moved connection corridor between Inner and Outer lanes (Amber Yellow and Sapphire Purple) to be farther from the base entrances

**2024-11-07** ([forum post](https://forums.playdeadlock.com/threads/11-07-2024-update.44786/))

- Bots will more aggressively attack the Shrines and Patron when pushing into the enemy base

**2024-10-24** ([forum post](https://forums.playdeadlock.com/threads/10-24-2024-update.40951/))

- Shrine/Patron no longer have Soul/AP bounties
- Shrine Flex Slot moved to "All Shrines"
- Base Guardians and Shrines no longer have out-of-combat regen

**2024-10-10** ([forum post](https://forums.playdeadlock.com/threads/10-10-2024-update.36958/))

- The patron once again will warn you when your Walkers are under attack
- The patron now will sometimes offer words of encouragement when you level up instead of when you destroy a Guardian or Walker
- Percentage of deniable orbs from objectives for Guardian/Walker/Patron/Shrines rescaled from 54.55/66.67/100/0% to 35%
- Widened stairs from Shrines back to the player spawn area

**2024-09-12** ([forum post](https://forums.playdeadlock.com/threads/09-12-2024-update.27974/))

- Added an overhang below the Patron position
- Added two juke closets facing the Patron

**2024-08-15** ([forum post](https://forums.playdeadlock.com/threads/08-15-2024-update.16378/))

- Patron damage increased by 30% after it is vulnerable
- Weakened Patron Health increased by 15%
- Weakened Patron now has a Torment Pulse style effect, hitting up to 2 enemies in the pit for 75 damage per second

**2024-08-01** ([forum post](https://forums.playdeadlock.com/threads/08-01-2024-update.13369/))

- Temporarily disabled the audio reminder on being unable to damage the patron while the shrines are alive
- Fixed Shrines not having collision
- When Shrines are destroyed the Patron gets more aggressive, moves faster, and does more damage
- Weakened Patron HP regen increased from 80 to 120
- Weakened Patron out of combat delay reduced from 30s to 20s

**2024-07-18** ([forum post](https://forums.playdeadlock.com/threads/07-18-2024-update.11831/))

- Base entrance window area can no longer be invaded from the outside by double jumping
- Weakened Patron health increased by 20%

**2024-07-11** ([forum post](https://forums.playdeadlock.com/threads/07-11-2024-update.10871/))

- Reworked the core base area where the Weakened Patron goes. It is now in a low terrain pit and requires attackers be inside the pit to do damage to it.
- Base Guardian and Shrines bullet resist per nearby hero increased from 40/20/0/0% (for 0/1/2/3 people) to 60/40/20/0%

**2024-07-04** ([forum post](https://forums.playdeadlock.com/threads/07-04-2024-update.9652/))

- Base Guardians and Shrines now have +40% Bullet Resistance. They lose 20% for each enemy hero nearby (down to a minimum of 0% bullet resistance). When they haven't taken damage for 60 seconds, they regenerate 4% max hp per second.

**2024-06-27** ([forum post](https://forums.playdeadlock.com/threads/06-27-2024-update.8486/))

- Flex slot removed from killing the Patron and added to killing all Walkers

**2024-06-13** ([forum post](https://forums.playdeadlock.com/threads/06-13-2024-update.5773/))

- Fixed TAB/ALT not bringing up your abilities when spectating the Patron
- Added Patron VO for when allied or enemy base guardians are destroyed

**2024-05-23** ([forum post](https://forums.playdeadlock.com/threads/05-23-2024-update.1245/))

- Sped up select Amber Hand VO that related to game state (shrines being under attack, protecting the urn runner etc)

**2024-05-16** ([forum post](https://forums.playdeadlock.com/threads/05-16-2024-update.902/))

- Updated VO for Amber Hand's Patron
- Added a short wall between Shrines level of the base and the Weakened Patron level

**2024-05-13** ([forum post](https://forums.playdeadlock.com/threads/05-13-2024-update.807/))

- Patron (Weakened) now has 40hp/s regen when it has not taken damage for 30s

**2024-05-03** ([forum post](https://forums.playdeadlock.com/threads/05-03-2024-update.427/))

- Added the Patron to the spectate-when-dead cycle if the enemy is in your base or everyone on your team is dead
