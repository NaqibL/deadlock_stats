# Neutral camps, vaults and Sinner's Sacrifice

Generated from the game files at build 6868 and Valve's patch notes. Everything below is quoted from a source, not interpreted. Patch notes describe the game as of their date: read newest first, and treat an older line as history once a newer one changes the same thing.

## What the game itself says

- Temple Guardian (`Citadel_AttackerClass_CLASS_SUPER_NEUTRAL`)
- [Ability Melee] Melee to Collect Souls (`Citadel_Hideout_VaultHint01`)
- [Ability Melee] Melee during flashing lights for bonuses, heavy melee for even more (`Citadel_Hideout_VaultHint02`)
- Haunt #unit num (`Citadel_Hud_KillFeedNeutral`)
- Haunt MidBoss has been defeated (`Citadel_Steamshare_Desc_Neutral_ObjectiveDestroyed_MidBoss`)
- Haunt MidBoss (`Citadel_Steamshare_Title_Neutral_ObjectiveDestroyed_MidBoss`)
- There are many neutral creatures lurking around the map. Defeat them to earn souls. Sometimes, a powerful creature will appear at the center of the map… defeating it will offer your team great power. (`guide_neutrals_desc`)
- Barrel Mimic I (`neutral_barrel_1`)
- Barrel Mimic II (`neutral_barrel_2`)
- Barrel Mimic III (`neutral_barrel_3`)
- Past Dues II (`neutral_books_2`)
- Past Dues III (`neutral_books_3`)
- Festival Spirit I (`neutral_lanterns_1`)
- Festival Spirit II (`neutral_lanterns_2`)
- Festival Spirit III (`neutral_lanterns_3`)
- Slum Shroom I (`neutral_mushrooms_1`)
- Slum Shroom II (`neutral_mushrooms_2`)
- Slum Shroom III (`neutral_mushrooms_3`)
- Overseer III (`neutral_overseer_3`)
- Crabbage Pot I (`neutral_plants_1`)
- Crabbage Pot II (`neutral_plants_2`)
- Crabbage Pot III (`neutral_plants_3`)
- Stage Hand I (`neutral_puppets_1`)
- Stage Hand II (`neutral_puppets_2`)
- Stage Hand III (`neutral_puppets_3`)
- Sinner's Sacrifice (`neutral_sinners`)
- Specimen III (`neutral_specimens_3`)
- Gutter Ghoul I (`neutral_trash_1`)
- Gutter Ghoul II (`neutral_trash_2`)
- Gutter Ghoul III (`neutral_trash_3`)
- Underhand II (`neutral_underhand_2`)
- Underhand III (`neutral_underhand_3`)
- Rat Swarm - Dash to knock off rats (`npc_neutral_bug_rat_swarm/neutral_rat_swarm`)
- Mid Boss Charge (`super_neutral_charge`)
- Mid Boss Gun (`super_neutral_gun`)

## Current numbers in the game files

`neutral_trooper_weak`

| Field | Value |
|---|---|
| AttackRangeTarget | 2.54 |
| GoldReward | 45 |
| GoldRewardBonusPercentPerMinute | 1.08 |
| InitialSpawnDelay | 120 |
| IntrinsicModifiers[0].BULLET_DAMAGE_REDUCTION_PERCENT | 50 |
| IntrinsicModifiers[0].ABILITY_DAMAGE_REDUCTION_PERCENT | 45 |
| MaxHealth | 142 |
| MeleeAttemptRange | 3.81 |
| NeutralDamageGrowth.DamageGrowthPctPerMin | 0.5 |
| NonMoveAttackDuration | 1 |
| RunSpeed | 3.81 |
| ShieldReactivateDelay | 2 |
| SpawnInterval | 85 |
| WalkSpeed | 3.81 |
| Weapon.BulletDamage | 2.657 |
| Weapon.RoundsPerSecond | 2 |
| Weapon.BulletsPerShot | 1 |
| Weapon.DPS | 5.314 |
| Weapon.SustainedDPS | 5.314 |

`neutral_trooper_normal`

| Field | Value |
|---|---|
| AbilityChance01 | 0.1 |
| AbilityChance02 | 0.05 |
| AttackRangeTarget | 10.16 |
| GoldReward | 75 |
| GoldRewardBonusPercentPerMinute | 1.08 |
| InitialSpawnDelay | 300 |
| IntrinsicModifiers[0].BULLET_DAMAGE_REDUCTION_PERCENT | 50 |
| IntrinsicModifiers[0].ABILITY_DAMAGE_REDUCTION_PERCENT | 45 |
| MaxHealth | 354 |
| MeleeAttemptRange | 3.81 |
| NeutralDamageGrowth.DamageGrowthPctPerMin | 0.5 |
| NonMoveAttackDuration | 3 |
| RunSpeed | 3.048 |
| ShieldReactivateDelay | 2 |
| SpawnInterval | 290 |
| WalkSpeed | 3.048 |
| Weapon.BulletDamage | 6.738 |
| Weapon.RoundsPerSecond | 2 |
| Weapon.BulletsPerShot | 1 |
| Weapon.DPS | 13.476 |
| Weapon.SustainedDPS | 13.476 |

`neutral_trooper_strong`

| Field | Value |
|---|---|
| AbilityChance01 | 0.3 |
| AbilityChance02 | 0.2 |
| AbilityChance03 | 0.1 |
| AttackRangeTarget | 15.24 |
| GoldReward | 199 |
| GoldRewardBonusPercentPerMinute | 1.08 |
| InitialSpawnDelay | 480 |
| IntrinsicModifiers[0].BULLET_DAMAGE_REDUCTION_PERCENT | 60 |
| IntrinsicModifiers[0].ABILITY_DAMAGE_REDUCTION_PERCENT | 55 |
| MaxHealth | 1246 |
| MeleeAttemptRange | 3.81 |
| NeutralDamageGrowth.DamageGrowthPctPerMin | 0.5 |
| NonMoveAttackDuration | 3.5 |
| RunSpeed | 2.032 |
| ShieldReactivateDelay | 2 |
| SpawnInterval | 335 |
| WalkSpeed | 2.032 |
| Weapon.BulletDamage | 10.01 |
| Weapon.RoundsPerSecond | 2 |
| Weapon.BulletsPerShot | 1 |
| Weapon.DPS | 20.02 |
| Weapon.SustainedDPS | 20.02 |

`neutral_sinners_sacrifice`

| Field | Value |
|---|---|
| BreakableForceScale | 3 |
| GoldReward | 155 |
| GoldRewardBonusPercentPerMinute | 1.08 |
| InitialSpawnDelay | 480 |
| IntrinsicModifiers[1].ParryCheckRadius | 1.524 |
| MaxHealth | 500 |
| MeleeAttemptRange | 3.81 |
| MiniGameFastChance | 0.4 |
| MiniGameFastSpeed | 0.0419 |
| NeutralDamageGrowth.DamageGrowthPctPerMin | 0.5 |
| RetaliateDamage | 80 |
| ShieldReactivateDelay | 2 |
| SpawnInterval | 300 |
| VaultMiniGameHitWindow | 0.5 |
| VaultMiniGameTime | 3 |
| VaultSuccessDestroyTime | 1.3 |
| Weapon.RoundsPerSecond | 2 |
| Weapon.BulletsPerShot | 1 |

`neutral_camp_weak`

| Field | Value |
|---|---|
| InitialSpawnDelayInSeconds | 120 |
| SpawnIntervalInSeconds | 85 |

`neutral_camp_medium`

| Field | Value |
|---|---|
| InitialSpawnDelayInSeconds | 300 |
| SpawnIntervalInSeconds | 290 |

`neutral_camp_strong`

| Field | Value |
|---|---|
| InitialSpawnDelayInSeconds | 480 |
| SpawnIntervalInSeconds | 335 |

`neutral_camp_vaults`

| Field | Value |
|---|---|
| InitialSpawnDelayInSeconds | 480 |
| SpawnIntervalInSeconds | 300 |

## Patch history (105 lines, newest first)

**2026-06-30** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1836506165563227))

- Urn running is now its own objective. Spawns on either end of the map (where the previous neutral pickup locations were), and gets delivered to the opposite end. Spawns at 10/15/20/25/etc.
- Jump Pads on top of the double sinner buildings have been removed

**2026-06-04** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1834602721188293))

- Progress duration for favored/neutral/unfavored is 6/12/18s

**2026-05-25** ([forum post](https://forums.playdeadlock.com/threads/05-22-2026-update.135477/post-259788))

- Urn deposit timers for favored/neutral/unfavored increased from 3/5/10s to 5/10/15s

**2026-05-22** ([forum post](https://forums.playdeadlock.com/threads/05-22-2026-update.135477/))

- Medium neutrals initial spawn time reduced from 6 minutes to 5 minutes
- Once dropped off, the Urn will go into a "Depositing" phase for a set amount of time, depending on which team the urn favors (3s/5s/10s for Favored/Neutral/Unfavored).
- [ General ] - Base HP reduced by 10 for all heroes - HP per boon reduced by 3 - Guardians scaling resistance from +75%->-50% over 12 minutes to +50%->-50% (takes more damage early) - Medium neutrals initial spawn time reduced from 6 minutes to 5 minutes - Breakables spawn time increased from 2...

**2026-03-21** ([forum post](https://forums.playdeadlock.com/threads/03-06-2026-update.114328/post-226950))

- Small neutrals spirit resist increased from 35% to 45%
- Small neutrals spirit resist increased from 35% to 45%

**2026-03-06** ([forum post](https://forums.playdeadlock.com/threads/03-06-2026-update.114328/))

- Minimap now indicates if the Urn is a favored, neutral or unfavored
- Added a neutral camp (2 Normal, 3 Weak) at Hidden King Park Walker
- Added a neutral camp (2 Normal, 3 Weak) at Archmother York Walker

**2026-01-20** ([forum post](https://forums.playdeadlock.com/threads/12-29-2025-update.95233/post-185824))

- Neutral respawn times, hp, and bounty reduced by 30% (sinner's sacrifice unaffected)

**2025-12-17** ([forum post](https://forums.playdeadlock.com/threads/12-16-2025-update.93983/post-178389))

- Time delay before sprint starts working after hero/neutral interaction reduced from 4s to 3s

**2025-12-16** ([forum post](https://forums.playdeadlock.com/threads/12-16-2025-update.93983/))

- Neutral HP reduced by 20%
- Neutral HP growth increased from 0.5%/min to 2.1% (less HP before ~15 minutes, more afterwards)
- Neutrals spirit resistance increased by 5%
- Sinner's Sacrifice bounty reduced by 10%
- 1x Small Camp: 77s​2x Medium Camps: 163s​1x Hard Camp: 193s​4x Medium Camps: 230s​2x Hard Camps: 263s​1x Hard Camp + 3x Medium Camps: 270s​2x Hard Camp + 6x Medium Camps: 354s​

**2025-12-03** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/post-174987))

- Neutrals HP increases by 0.5% per minute
- Neutrals damage increases by 0.5% per minute
- Neutrals base damage reduced by 30%
- Hard neutrals now take +20% more melee damage
- Sprint/Out of Combat regen timer against neutrals increased from 2.5s to 4s (takes longer to start sprinting/regening)

**2025-11-22** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/post-171913))

- Neutrals bounty increased by 5%

**2025-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/))

- Neutrals bounty increased by 10%
- Neutrals HP increased by +15%
- Small neutrals damage +15%
- Small neutral camps respawn time 180s to 120s
- Medium neutrals spirit resist from 30% to 40%
- Medium neutrals damage increased by 25%
- Hard neutrals spirit resist increased from 35% to 50%
- Hard neutrals damage increased by 30%
- Sinner's Sacrifice: Return damage increased from 60 to 80
- Sprint/Out of Combat regen timer against neutrals increased from 0.5s to 2.5s (takes longer to start sprinting/regening)

**2025-10-02** ([forum post](https://forums.playdeadlock.com/threads/10-02-2025-update.84332/))

- Neutral Shop no longer gets disabled if an enemy is nearby

**2025-07-29** ([forum post](https://forums.playdeadlock.com/threads/07-29-2025-update.72760/))

- Neutrals bounty increased by 15% (strong neutrals +25%)
- Medium Neutrals respawn rate increased from 360s to 420s (+17%)
- Strong Neutrals respawn rate increased from 480s to 600s (+25%)
- Sinner's Sacrifice: Retaliate damage increased from 40 to 60
- Sinner's Sacrifice: Heavy melee end success bonus now grants 4 buffs rather than 3 (these also take a little longer to kill now due to the melee timing changes)

**2025-07-04** ([forum post](https://forums.playdeadlock.com/threads/07-04-2025-update.70156/))

- Small neutral camp bounty increased by 15%
- Fixed an issue where Souls were shared with anyone that punched a Sinner's Sacrifice, regardless of the duration or team

**2025-05-27** ([forum post](https://forums.playdeadlock.com/threads/05-27-2025-update.66453/))

- Fixed Neutrals near the base gaining the "near base" trooper resist

**2025-03-16** ([forum post](https://forums.playdeadlock.com/threads/03-16-2025-update.58880/))

- Neutral bounty increased by 5%
- Sinner's Sacrifice initial spawn time reduced from 10 min to 8 min (respawn rate is still 5 min)
- Fixed a bug with Neutral bounty later in the game being reduced by more than the initial intended -15% (this fix was released yesterday)

**2025-03-13** ([forum post](https://forums.playdeadlock.com/threads/03-13-2025-update.58592/))

- Neutrals soul values reduced by 15%  (including Sinner's Sacrifice)
- Sinner's Sacrifice spawn/respawn time increased from 8/4 minutes to 10/5
- Mid Neutral Camp respawn time increased from 5 minutes to 6 minutes

**2025-02-25** ([forum post](https://forums.playdeadlock.com/threads/02-25-2025-update.56683/))

- Today's update introduces a reworked map layout, alongside a variety of improvements and bug fixes. [ Map Rework ] - The map has been redesigned around being 3 lanes rather than 4. This has a large range of accompanying map-wide changes regarding visuals, building layouts, pathways, neutral...

**2024-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2024-update.47476/))

- Added icon variants for high or low ground for small/medium/large camps
- Moved rooftop neutral camps on Amber Yellow and Sapphire Purple to rooftops closer to the Guardian
- Moved the side lane teleporters to the crawl space under the Hard camp

**2024-11-13** ([forum post](https://forums.playdeadlock.com/threads/11-13-2024-update.46391/))

- First Urn is now always neutral regardless of NW lead

**2024-11-07** ([forum post](https://forums.playdeadlock.com/threads/11-07-2024-update.44786/))

- Sinners Sacrifice now has a final damage state for clear read on final hit
- Fixed Sinner's Sacrifice changing facing direction sometimes
- Neutral Creeps now give 5% less souls
- Moved 8 neutral camps (4 on each side) from outside the outer lanes behind the Walkers to in between inner and outer lanes
- Biased Urn delivery locations moved slightly closer to neutral positions

**2024-10-24** ([forum post](https://forums.playdeadlock.com/threads/10-24-2024-update.40951/))

- Sinner's Sacrifice now shares souls of subsequent hits with everyone that hit it recently (rather than the bigger value from last hit only going to one player)
- Neutral camps beside Amber Purple and Sapphire Yellow Walker arenas moved from the ground floor to the upper floor
- Redesigned traversal from ground floor to upper floor of the Garage and Night Club to get to the Sinner's Sacrifice neutrals

**2024-10-10** ([forum post](https://forums.playdeadlock.com/threads/10-10-2024-update.36958/))

- Medium Camps spawn time changed from 7 min to 5 min
- Hard Camps spawn time changed from 7 min to 8 min
- Vaults spawn time/interval changed from 10/5 to 8/4

**2024-09-26** ([forum post](https://forums.playdeadlock.com/threads/09-26-2024-update.33015/))

- Sinner's Sacrifice now grants a permanent golden statue bonus when it is killed
- Fixed Sinner's Sacrifice sharing bounty to nearby allies

**2024-09-12** ([forum post](https://forums.playdeadlock.com/threads/09-12-2024-update.27974/))

- Neutral Camps are now represented by a highlight glow on the buildings they are located within​

**2024-08-29** ([forum post](https://forums.playdeadlock.com/threads/08-29-2024-update.22253/))

- Added alternate shop music which plays in the neutral shop
- Fixed Sinner's Sacrifice not always correctly animating
- A pair of teleporters has been added to the outer lanes at the midpoint (near the three red neutral creeps)

**2024-07-18** ([forum post](https://forums.playdeadlock.com/threads/07-18-2024-update.11831/))

- Changed the neutrals in the top mid temple area to a strong, a medium and a small creep (2 of these)

**2024-07-04** ([forum post](https://forums.playdeadlock.com/threads/07-04-2024-update.9652/))

- Fixed a bug where bullets could penetrate close range targets and hit 2 targets when not intended (was primarily obvious with neutral farming)
- Reworked how Powerups work. There are now only 2 locations where they spawn instead of 6 (the two at the strong camps near the middle far edges of the map). The different powerup types are reduced from 6 to 4 and they have been reworked:

**2024-06-20** ([forum post](https://forums.playdeadlock.com/threads/06-20-2024-update.7003/))

- Vault bounty increased from 300 to 330
- Enclosed the exterior Medium Neutral Camp with fencing in front of the Theater to match the Amber side Cab Stand
- 2) Between the exterior Strong Neutral Camps and the outer lane near the T2

**2024-06-13** ([forum post](https://forums.playdeadlock.com/threads/06-13-2024-update.5773/))

- Added sandbox option for spawning neutrals

**2024-06-06** ([forum post](https://forums.playdeadlock.com/threads/06-06-2024-update.4096/))

- Replaced the neutral vaults with a new model, the Sinner's Sacrifice
- Added neutrals to Hero Sandbox (the small room in the back on the right)
- Soul Vessel dropped from heroes (after killing neutrals) now scales in size based on how many souls are inside
- Updated sound effects for the Sinner's Sacrifice
- Strong neutrals HP reduced by 20%
- Strong neutrals souls bounty reduced by 20%
- 4 Strong Neutral camps in the corners of the map have been replaced with Medium neutrals
- Vaults souls increased from 260 to 300

**2024-05-30** ([forum post](https://forums.playdeadlock.com/threads/05-30-2024-update.2514/))

- Fixed corner neutral camps not burrowing if they lose line of sight
- Crate powerups can now only spawn after 2 minutes (when the small neutrals spawn)
- Carved out interior of inner lane tower buildings beside the Guardian and connected to the neutral camp in the underground areas

**2024-05-23** ([forum post](https://forums.playdeadlock.com/threads/05-23-2024-update.1245/))

- Updated Trooper and Neutral shooting sound effects
- Fixed Kelvin’s Ice Beam sometimes not hitting Neutrals
- Removed stack of cardboard boxes inside connection hallway near bases to prevent cover from Neutrals
- Vaults base bounty increased from 220 to 260
- Strong Neutrals Spirit Resist increased from 25% to 35%
- Medium Neutrals Spirit Resist increased from 25% to 30%
- Neutrals can now lean side to side to fire when obstructed by map geometry and being attacked

**2024-05-16** ([forum post](https://forums.playdeadlock.com/threads/05-16-2024-update.902/))

- Medium and Hard neutrals now spawn at 7 minutes
- Neutrals now have 20% Spirit Resist
- Basement neutrals now have +2 Medium neutrals and -4 Small neutrals
- Basement neutrals are now classified as a Medium camp instead of a Small camp (for the purposes of spawn time)
- Fixed various abuses where you can shoot neutrals without them being able to shoot back. Neutrals now become invulnerable when they have no line of sight of you for 2 seconds.

**2024-05-13** ([forum post](https://forums.playdeadlock.com/threads/05-13-2024-update.807/))

- Vault base bounty increased from 200 to 225
- Fixed some issues that allowed players to more easily camp players in the spawn area

**2024-05-03** ([forum post](https://forums.playdeadlock.com/threads/05-03-2024-update.427/))

- Vaults base bounty increased from 150 to 200
