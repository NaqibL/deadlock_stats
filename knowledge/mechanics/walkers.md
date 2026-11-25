# Walkers

Generated from the game files at build 6868 and Valve's patch notes. Everything below is quoted from a source, not interpreted. Patch notes describe the game as of their date: read newest first, and treat an older line as history once a newer one changes the same thing.

## What the game itself says

- Your Walker has been destroyed (`Citadel_Steamshare_Desc_Allied_ObjectiveDestroyed_Walker`)
- Enemy Walker has been destroyed (`Citadel_Steamshare_Desc_Enemy_ObjectiveDestroyed_Walker`)
- Allied Walker (`Citadel_Steamshare_Title_Allied_ObjectiveDestroyed_Walker`)
- Enemy Walker (`Citadel_Steamshare_Title_Enemy_ObjectiveDestroyed_Walker`)
- Invis Move Speed (`VeilWalker_MoveSpeed_label`)
- Invis Move Speed (`VeilWalker_MoveSpeed_postvalue_label`)
- Walkers lie deeper in the lanes and have an arsenal of defensive moves. (`guide_the_map_walkers_desc`)

## Current numbers in the game files

`npc_boss_tier2`

| Field | Value |
|---|---|
| AoeWaveHealthThreshold | 0.25 |
| BackDoorProtectionRange | 55 |
| BackdoorProtectionModifier.HealthPerSecondRegen | 65 |
| BackdoorProtectionModifier.BackdoorProtectionDamageMitigationFromPlayers | 65 |
| BackdoorProtectionModifier.BackdoorProtectionDamageMitigationFromPlayers_Streetbrawl | 85 |
| BackdoorProtectionModifier.flShieldImpactDirectionOffset | 50 |
| BoundAbilities.ESlot_Signature_1.AbilityProperties.AbilityCooldown | 10 |
| BoundAbilities.ESlot_Signature_1.AbilityProperties.AbilityCastRange | 35.56 |
| BoundAbilities.ESlot_Signature_1.AbilityProperties.VolleyInterval | 0.5 |
| BoundAbilities.ESlot_Signature_1.AbilityProperties.GrenadesInVolley | 6 |
| BoundAbilities.ESlot_Signature_1.AbilityProperties.MaxSimultaneousVolley | 1 |
| BoundAbilities.ESlot_Signature_1.AbilityProperties.InitialVolleyInaccuracy | 100 |
| BoundAbilities.ESlot_Signature_1.AbilityProperties.PerVolleyInaccuracy | 25 |
| BoundAbilities.ESlot_Signature_1.AbilityProperties.Damage | 200 |
| BoundAbilities.ESlot_Signature_1.AbilityProperties.DetonateTimer | 10 |
| BoundAbilities.ESlot_Signature_1.AbilityProperties.FireDuration | 5 |
| BoundAbilities.ESlot_Signature_1.AbilityProperties.FireDPS | 25 |
| BoundAbilities.ESlot_Signature_1.AbilityProperties.FireDPSTrooperFactor | 0.3 |
| BoundAbilities.ESlot_Signature_1.AbilityProperties.FireTickInterval | 0.5 |
| BoundAbilities.ESlot_Signature_1.AbilityProperties.BulletArmorReduction | -10 |
| BoundAbilities.ESlot_Signature_1.AbilityProperties.TechArmorReduction | -10 |
| BoundAbilities.ESlot_Signature_1.Weapon.BulletsPerShot | 1 |
| BoundAbilities.ESlot_Signature_1.ProjectileInfos.primary.TrackingDuration | 1 |
| BoundAbilities.ESlot_Signature_1.ProjectileInfos.primary.TrackingStartTime | 1 |
| BoundAbilities.ESlot_Signature_1.ProjectileInfos.primary.TrackingEndTime | 2 |
| BoundAbilities.ESlot_Signature_1.ProjectileInfos.primary.GravityScale | 0.5 |
| BoundAbilities.ESlot_Signature_1.LaunchAngle | 45 |
| BoundAbilities.ESlot_Signature_1.AuraModifier.ModifierProvidedByAuraDuration | 4 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.AbilityDuration | 6 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.AbilityCastRange | 34.92 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.AbilityCastDelay | 1 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.PathLength | 1250 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.PathWidth | 0.762 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.MaxHPDPS | 2 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.DPS | 125 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.CreepDPS | 190 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.TrackingSpeed | 0.762 |
| BoundAbilities.ESlot_Signature_2.AbilityProperties.SweepSpeed | 0.0254 |
| BoundAbilities.ESlot_Signature_2.Weapon.BulletsPerShot | 1 |
| BoundAbilities.ESlot_Signature_2.LaserCharge.Duration | 1.5 |
| BoundAbilities.ESlot_Signature_2.LaserLeft.SideSearchAngle | 90 |
| BoundAbilities.ESlot_Signature_2.LaserRight.SideSearchAngle | 90 |
| BoundAbilities.ESlot_Signature_3.AbilityProperties.AbilityCooldown | 6 |
| BoundAbilities.ESlot_Signature_3.AbilityProperties.AbilityCastRange | 12 |
| BoundAbilities.ESlot_Signature_3.AbilityProperties.AbilityCastDelay | 1.43 |
| BoundAbilities.ESlot_Signature_3.AbilityProperties.ActivationDistance | 12 |
| BoundAbilities.ESlot_Signature_3.Weapon.BulletsPerShot | 1 |
| BoundAbilities.ESlot_Signature_4.AbilityProperties.AbilityCooldown | 3 |
| BoundAbilities.ESlot_Signature_4.AbilityProperties.AbilityCastRange | 25.4 |
| BoundAbilities.ESlot_Signature_4.AbilityProperties.AbilityCastDelay | 2.5 |
| BoundAbilities.ESlot_Signature_4.AbilityProperties.Damage | 300 |
| BoundAbilities.ESlot_Signature_4.AbilityProperties.DamageHealthPercent | 20 |
| BoundAbilities.ESlot_Signature_4.AbilityProperties.SlowPercent | 24 |
| BoundAbilities.ESlot_Signature_4.Weapon.BulletsPerShot | 1 |
| BoundAbilities.ESlot_Signature_4.AoEModifier.modifierProvidedByAura.TossUpStrength | 400 |
| BoundAbilities.ESlot_Signature_4.AoEModifier.modifierProvidedByAura.TossHorizontalMin | 300 |
| BoundAbilities.ESlot_Signature_4.AoEModifier.modifierProvidedByAura.TossHorizontalMax | 1200 |
| BoundAbilities.ESlot_Signature_4.AoEModifier.modifierProvidedByAura.DebuffDuration | 3 |
| BurstCooldown | 0.2 |
| BurstDuration | 1 |
| EmpoweredModifierLevel1.MaxHealth | 9000 |
| EmpoweredModifierLevel1.TransitionDuration | 1 |
| EmpoweredModifierLevel2.MaxHealth | 12000 |
| EmpoweredModifierLevel2.TransitionDuration | 1 |
| FriendlyAuraModifier.AuraRadius | 28 |
| FriendlyAuraModifier.modifierProvidedByAura.TECH_RESIST | 15 |
| FriendlyAuraModifier.modifierProvidedByAura.BULLET_ARMOR_DAMAGE_RESIST | 15 |
| IntrinsicModifiers[0].BULLET_ARMOR_DAMAGE_RESIST | 35 |
| InvulModifier.ShieldRadius | 7.62 |
| InvulModifierRange | 22 |
| MaxHealth | 6000 |
| MeleeAttackRadius | 5.08 |
| MeleeAttemptRange | 15.24 |
| MeleeDamage | 300 |
| MeleeDamageHealthPct | 10 |
| MeleeDuration | 0.9 |
| MeleeHitTime | 0.6 |
| MeleeTargetRadius | 5.08 |
| NearbyEnemyResist.NearbyEnemyResistRange | 50.8 |
| NearbyEnemyResist.ResistValues | 0 / 0 / 0 / 20 / 30 / 40 / 50 |
| RangeRingAlpha | 0.0152 |
| RangeRingFadeDistance | 5 |
| RangeRingShowDistance | 7 |
| RangedArmorModifier.BulletResistancePctMax | 100 |
| RangedArmorModifier.RangeMin | 30.48 |
| RangedArmorModifier.RangeMax | 50.8 |
| StaggerWatcherModifier.BuildUpMax | 5 |
| StaggerWatcherModifier.AdditionlPlayerMinContribution | 0.2 |
| StaggerWatcherModifier.BuildUpModifier.BuildUpDecayDelay | 2 |
| StatTrackerAuraModifier.AuraRadius | 32 |
| StompAttemptRadius | 12.57 |
| StompDamage | 350 |
| StompDamageMaxHealthPercent | 15 |
| StompDamageTrooperRate | 0.3 |
| StompImpactRadius | 14.5 |
| StompTossUpMagnitude | 1.25 |
| StunDuration | 2 |
| TossSpeed | 8.89 |

## Patch history (107 lines, newest first)

**2026-09-16** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1844115010490072))

- Walker bounty increased by 5%

**2026-08-12** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1840944183775204))

- Doorman: Walker will no longer consider Luggage Cart dragged enemies as valid targets to trigger the stomp on until soon after they are dropped off
- Doorman: Similar to the Walker change above, the turrets in the healing area in base now also wait on considering valid targets

**2026-06-30** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1836506165563227))

- Walker bounty reduced from 4000 to 3500

**2026-05-22** ([forum post](https://forums.playdeadlock.com/threads/05-22-2026-update.135477/))

- Walkers will interrupt a rocket barrage during the 1s windup if stomp becomes an option.
- Fixed a bug where walkers were spinning while lasering.

**2026-03-06** ([forum post](https://forums.playdeadlock.com/threads/03-06-2026-update.114328/))

- Shrine is now easier to kill for the first one and harder for the second. HP from 8100 to 5000/10000 (HP updates after the first one dies, like Walkers)
- Walkers bounty increased from 3500 to 4000
- Walkers Health rescaled from 6800/9350/11900 to 6000/9000/12000
- Walkers armor decay rescaled from "+75% -> -50%" to "+65% -> -65%", from over 20min to over 18min
- Added a neutral camp (2 Normal, 3 Weak) at Hidden King Park Walker
- Added a neutral camp (2 Normal, 3 Weak) at Archmother York Walker
- [ General ] - Can now jump during slide - Dash jump grants a very brief period with increased air control (30% for 0.25s) - Shrine is now easier to kill for the first one and harder for the second. HP from 8100 to 5000/10000 (HP updates after the first one dies, like Walkers) - Shrines attack no...

**2025-12-16** ([forum post](https://forums.playdeadlock.com/threads/12-16-2025-update.93983/))

- Walker Rocket Barrage radius reduced from 6m to 5m

**2025-12-03** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/post-174987))

- Walkers and Mid Boss now have +15% Bullet Resistance and -15% HP
- Walker ally aura (grants +15% Bullet and Spirit Resist) range reduced from 32m to 28m

**2025-11-27** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/post-173347))

- Walkers now have escalating health after each one dies. From a constant 12880 to 8000/11000/14000 (model scale slightly smaller for 1st and slightly bigger for last)

**2025-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/))

- Walker HP increased by 40%
- Walker on the Side Lanes now have same HP as Midlane (rather than ~37% less)
- Walker engagement ranges reduced (ranges for attacks, being attacked, stomps, etc)
- Walker stomp cooldown reduced from 10s to 6s
- Walker stomp damage increased from 350 + 10% Max HP to 350 + 15% Max HP
- Walker fireballs radius from 5m to 6m
- Walker fireballs debuff now lingers for 4s
- Walker fireballs now reduce bullet and spirit resistance by 10%
- Walker area in mid lane adjusted
- Walkers now start with 75% Damage Resist that decay's to -50% over the first 20 minutes of a match
- Note: The Walker resistance change used to be in the client a couple months ago, but it got bugged.
- Base slot count increased from 8 to 9 and Flex slot count reduced from 4 to 3. One is given for each Walker killed. Previously the 4 were given for: "3 Guardians", "1 Walker", "3 Walkers", and "Set of Base Guardians"

**2025-10-02** ([forum post](https://forums.playdeadlock.com/threads/10-02-2025-update.84332/))

- Distance to attack Walkers reduced from 35m to 34m

**2025-08-01** ([forum post](https://forums.playdeadlock.com/threads/07-29-2025-update.72760/post-139997))

- Side Walkers +16% HP, Mid Walkers +8% HP

**2025-07-29** ([forum post](https://forums.playdeadlock.com/threads/07-29-2025-update.72760/))

- Removed the teleporters behind the Walkers
- Side Walkers HP increased by 10%

**2025-07-04** ([forum post](https://forums.playdeadlock.com/threads/07-04-2025-update.70156/))

- Walker Spirit resistance reduced from 30% to 25%
- Walker total bounty reduced from 4500 to 3500

**2025-06-17** ([forum post](https://forums.playdeadlock.com/threads/06-17-2025-update.68401/))

- Flex Slot changed from "Two Walker" to "Three Walkers"
- Guardian and Walker total bounty is now split with all nearby players (including players that have done damage to it within 20s). Nearby players get 40% and the rest is split evenly with all 6 players (including those nearby).
- Trooper damage to Walkers reduced from 80 DPS to 60 DPS
- Walker HP increased by 10%
- Walker Spirit Resist reduced from 40% to 30%

**2025-05-27** ([forum post](https://forums.playdeadlock.com/threads/05-27-2025-update.66453/))

- Added news kiosk structure in between Mid Lane Walker and base entrance

**2025-05-19** ([forum post](https://forums.playdeadlock.com/threads/05-19-2025-update.65381/))

- Walker HP increased by 10%
- Walkers resistance vs troopers reaches -40% at 20 minutes instead of 16 minutes

**2025-01-27** ([forum post](https://forums.playdeadlock.com/threads/01-27-2025-update.54590/))

- Can no longer stand on top of Walkers

**2024-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2024-update.47476/))

- Walkers Stomp now also deals 10% Max HP as damage
- Walkers Laser now also deals 2% Max HP DPS
- Walkers now provide nearby allied heroes 25% Bullet and Spirit Resistance
- Walkers now have Resistance based on how many nearby enemies there are (0/8/16/24/32/40% for 1/2/3/4/5/6 players; they are more tanky against a large attacking team)
- Middle Lane Walkers HP increased from 5800 to 8000 (side walkers HP is 5175)

**2024-11-07** ([forum post](https://forums.playdeadlock.com/threads/11-07-2024-update.44786/))

- Walkers damage vs players increased by 10%
- Moved 8 neutral camps (4 on each side) from outside the outer lanes behind the Walkers to in between inner and outer lanes
- Walker armor loss over time now happens at 16m instead of 14m

**2024-10-24** ([forum post](https://forums.playdeadlock.com/threads/10-24-2024-update.40951/))

- AP is no longer granted for Walkers
- Walkers now have resist vs troopers starting at 60% and ending at -30% at 14 minutes
- Walkers now have resist vs players starting at 60% and ending at -30% at 14 minutes
- Connection hallways behind the Chapel and Firehouse now has an option to continue inside to the Walker arenas
- Neutral camps beside Amber Purple and Sapphire Yellow Walker arenas moved from the ground floor to the upper floor

**2024-10-10** ([forum post](https://forums.playdeadlock.com/threads/10-10-2024-update.36958/))

- Added Stomp AoE range indication as the Walker is about to use the ability
- Added Guardian and Walker death notification sound for all players
- Walker laser animation updated slightly, raising the forearms to better reveal the eye socket weakpoint to players on the ground
- The patron once again will warn you when your Walkers are under attack
- The patron now will sometimes offer words of encouragement when you level up instead of when you destroy a Guardian or Walker
- Percentage of deniable orbs from objectives for Guardian/Walker/Patron/Shrines rescaled from 54.55/66.67/100/0% to 35%
- Moved teleporters to travel between outer lane Walkers
- Added bridge and stair to the upper level of the Subway Entrance building from the outer lane Walker arenas

**2024-09-26** ([forum post](https://forums.playdeadlock.com/threads/09-26-2024-update.33015/))

- Redesigned outer lane path (ziplines and trooper nodes) from Walker to Guardian on Amber Yellow and Sapphire Purple

**2024-09-12** ([forum post](https://forums.playdeadlock.com/threads/09-12-2024-update.27974/))

- Walker AoE Stomp has new effects
- Flex Slot moved from "First Walker" to "Two Walkers"
- Walker beam max range (the sticky portion after being acquired) reduced by 20% (50m to 40m)

**2024-08-29** ([forum post](https://forums.playdeadlock.com/threads/08-29-2024-update.22253/))

- The minimum range the player must be to attack a walker is increased from 30m to 32m
- Added two bounce pads next to sidelane walkers at cultural center and courthouse
- Added bounce pad from the Amber Orange/Sapphire Blue Walker walkway to the low roofs toward the Walker.
- Stairwell from Amber Orange/Sapphire Blue Walker catwalk to the courtyard now less cramped

**2024-08-15** ([forum post](https://forums.playdeadlock.com/threads/08-15-2024-update.16378/))

- Walkers now require you to be within 30m to deal damage to them
- Walker Health increased by 15%
- Low roof buildings between inner lane Walker arenas are now valid play spaces
- Walker Arena - Amber Yellow/Sapphire Purple:
- Walker Arena - Amber Orange/Sapphire Blue:
- Walker Arena - Amber Blue/Sapphire Orange:
- Walker Arena - Amber Purple/Sapphire Yellow:
- Added an interior corridor through the building between the base and the Walker
- Added a balcony that borders the arena on the back side of the Walker

**2024-08-01** ([forum post](https://forums.playdeadlock.com/threads/08-01-2024-update.13369/))

- Fixed Walkers having a pause at the end of their Rocket Barrage
- Reworked the location of the Walker on Amber Yellow and Sapphire Purple lanes. They are a little further towards the map edges. Nearby terrain has been reworked as well.
- Each trooper you shoot at will now consider you a higher priority than Guardians/Walkers; that trooper will stop shooting the Guardians/Walkers and consider you its target for a few seconds
- Walker laser DPS vs troopers increased from 150 to 190
- Removed the tree in front of the Walkers on Amber Orange and Sapphire Blue

**2024-07-18** ([forum post](https://forums.playdeadlock.com/threads/07-18-2024-update.11831/))

- Walker in mid lanes health increased by 12%
- Walker stomp can no longer be dodged with double jump
- Walker stomp area increased a bit

**2024-07-11** ([forum post](https://forums.playdeadlock.com/threads/07-11-2024-update.10871/))

- Redesigned interior of new stairwells beside inner lane Walkers

**2024-07-04** ([forum post](https://forums.playdeadlock.com/threads/07-04-2024-update.9652/))

- Fixed position of the "All Walkers Destroyed" Flex slot to be the 2nd slot rather than the 4th
- Fixed Walkers not using their stomp properly
- Inner lane Walker arena (Amber Orange and Sapphire Blue):
- Reworked stairs for defenders to reach the overpass to start near the Walker and exit with line of sight down the lane

**2024-06-27** ([forum post](https://forums.playdeadlock.com/threads/06-27-2024-update.8486/))

- Flex slot removed from killing the Patron and added to killing all Walkers

**2024-06-23** ([forum post](https://forums.playdeadlock.com/threads/06-23-2024-update.7705/))

- There is no longer a reinforcement trooper wave after Guardians and Walkers die

**2024-06-06** ([forum post](https://forums.playdeadlock.com/threads/06-06-2024-update.4096/))

- Added new objective health bars for Guardians and Walkers
- Removed roof duct on top of low building besides inner Walker
- Walker bomb damage reduced from 300 to 200

**2024-05-30** ([forum post](https://forums.playdeadlock.com/threads/05-30-2024-update.2514/))

- Adjusted the health bar on Walkers to be easier to see
- Midlane Walkers HP reduced a little bit to match the same HP as the sidelane Walkers
- Moved outer lane Walker on Factory and Mansion sides slightly closer to the stairs
- Carved out interior of outer lane wall buildings beside the Walker to allow forward position for defenders

**2024-05-16** ([forum post](https://forums.playdeadlock.com/threads/05-16-2024-update.902/))

- Redesigned the Walker model and visuals

**2024-05-13** ([forum post](https://forums.playdeadlock.com/threads/05-13-2024-update.807/))

- Fixed Walker boss moving around while the game is paused
- Troopers DPS vs Walkers from 110 DPS to 80 DPS
