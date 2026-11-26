# Crates, golden statues and powerups

Generated from the game files at build 6868 and Valve's patch notes. Everything below is quoted from a source, not interpreted. Patch notes describe the game as of their date: read newest first, and treat an older line as history once a newer one changes the same thing. The patch notes do not record every change, so where a current number below differs from the newest note, the number is right. Questions already worked through are answered in [settled.md](../settled.md).

## What the game itself says

- Melee to pick up Soul Urn (`AbilityButtonHint_MeleeIdolPickup`)
- Heavy Melee to claim souls (`AbilityButtonHint_MeleePickUp`)
- Heavy Melee to claim PowerUp (`AbilityButtonHint_MeleePowerUp`)
- Breakable Pickups (`Citadel_Graph_Souls_Breakables`)
- Hold [Ability Melee] to break with heavy melee (`Citadel_Hideout_HeavyCrate`)
- Golden Statues (`Citadel_ShopStats_GoldenStatues`)
- Fire Rate Per Leech (`FireRatePerLeechPickup_label`)
- Fire Rate Per Leech (`FireRatePerLeechPickup_postvalue_label`)
- Heal On Pickup (`HealPerPickup_label`)
- Heal On Pickup (`HealPerPickup_postvalue_label`)
- Damage Reduction per Drawing (`IncomingDamagePercentReductionPerPickup_postvalue_label`)
- Used to open a treasure (`ItemHistory_Action_UnlockCrate_Remove`)
- Opened a treasure (`ItemHistory_Transaction_UnlockCrate`)
- Damage Bonus per Drawing (`OutgoingDamagePercentPerPickup_postvalue_label`)
- Health Regen Per Leech (`RegenPerLeechPickup_label`)
- Health Regen Per Leech (`RegenPerLeechPickup_postvalue_label`)
- Power Up your Hero (`ReportCard_PowerUp`)
- Ride the Transit Line back to base and spend all your Souls and Ability Points (`ReportCard_PowerUp_Desc`)
- Spirit per Sketch (`SpiritPerPickup_label`)
- Spirit per Sketch (`SpiritPerPickup_postvalue_label`)
- Enemy Reveal (`StatueActivateRange_label`)
- Enemy Reveal (`StatueActivateRange_postvalue_label`)
- Attack Range (`StatueAttackRadius_label`)
- Attack Range (`StatueAttackRadius_postvalue_label`)
- (Normalized) (`StatueHealth_label`)
- (Normalized) (`StatueHealth_postvalue_label`)
- Ava Recalled Regen (`StatueHeldRegen_label`)
- Ava Recalled Regen (`StatueHeldRegen_postvalue_label`)
- Lifesteal Non-Hero (`StatueLifestealNonHero_label`)
- Lifesteal Non-Hero (`StatueLifestealNonHero_postvalue_label`)
- Auto Recall Time (`StatueLifetime_label`)
- Auto Recall Time (`StatueLifetime_postvalue_label`)
- Damage Reduction (`StatueVictimDamageReduction_label`)
- Damage Reduction (`StatueVictimDamageReduction_postvalue_label`)
- +3% Max Ammo (`ammo_permanent_pickup_label`)
- +5% Max Ammo (`ammo_permanent_pickup_label_lv2`)
- +7% Max Ammo (`ammo_permanent_pickup_label_lv3`)
- {amount, plural, one{Soul} other{Souls}} (`big_gold_pickup_label:f`)
- PICKUP MISSING LOC NAME (`breakable_pickup_missing_loc`)
- +0.5% Bullet Resist (`bulletresist_permanent_pickup_label`)
- +0.75% Bullet Resist (`bulletresist_permanent_pickup_label_lv2`)
- +1% Bullet Resist (`bulletresist_permanent_pickup_label_lv3`)
- +0.5% Cooldown Reduction (`cd_permanent_pickup_label`)
- +0.75% Cooldown Reduction (`cd_permanent_pickup_label_lv2`)
- +1% Cooldown Reduction (`cd_permanent_pickup_label_lv3`)
- 3 Large clips (`clip_size_pickup/clip_size`)
- 3 Large clips (`clip_size_pickup_label`)
- Reduced Cooldown (`cooldown_reduction_pickup/cooldown_reduction`)
- Lower Cooldowns (`cooldown_reduction_pickup_label`)
- Double Jump and Zipline Speed (`double_jump_pickup/double_jump`)
- Bonus Bounty Next Hero Kill (`extra_gold_pickup/extra_gold_pickup`)
- Extra Stamina (`extra_stamina_pickup/extra_stamina`)
- Extra Stamina (`extra_stamina_pickup_label`)
- Increased fire rate (`fire_rate_pickup/small_fire_rate`)
- +1.5% Fire Rate (`firerate_permanent_pickup_label`)
- +2% Fire Rate (`firerate_permanent_pickup_label_lv2`)
- +2.5% Fire Rate (`firerate_permanent_pickup_label_lv3`)
- Increased health regen (`health_regen_pickup/small_health_regen`)
- +15 Bonus Health (`hp_permanent_pickup_label`)
- +20 Bonus Health (`hp_permanent_pickup_label_lv2`)
- +30 Bonus Health (`hp_permanent_pickup_label_lv3`)
- Increased Movement Speed (`move_speed_pickup/small_move_speed`)
- Faster Movement (`move_speed_pickup_label`)
- +0.1m Move Speed (`movespeed_permanent_pickup_label`)
- +0.2m Move Speed (`movespeed_permanent_pickup_label_lv2`)
- +0.3m Move Speed (`movespeed_permanent_pickup_label_lv3`)
- Leeches Collected: (`nurse_leech_pickups_stacklabel`)
- +0.25% Ability Range (`range_permanent_pickup_label`)
- +0.5% Ability Range (`range_permanent_pickup_label_lv2`)
- +0.75% Ability Range (`range_permanent_pickup_label_lv3`)
- {amount, plural, one{Soul} other{Souls}} (`small_gold_pickup_label:f`)
- +2 Spirit Power (`spirit_permanent_pickup_label`)
- +3 Spirit Power (`spirit_permanent_pickup_label_lv2`)
- +4 Spirit Power (`spirit_permanent_pickup_label_lv3`)
- +0.5% Spirit Resist (`spiritresist_permanent_pickup_label`)
- +0.75% Spirit Resist (`spiritresist_permanent_pickup_label_lv2`)
- +1% Spirit Resist (`spiritresist_permanent_pickup_label_lv3`)
- +3% Weapon Damage (`wp_permanent_pickup_label`)
- +4% Weapon Damage (`wp_permanent_pickup_label_lv2`)
- +6% Weapon Damage (`wp_permanent_pickup_label_lv3`)
- Increased Zipline Speed (`zipline_speed_pickup/zipline_speed`)
- Zipline Speed (`zipline_speed_pickup_label`)

## Current numbers in the game files

`BreakableSpawnTimeDesc`

| Field | Value |
|---|---|
| [0].InitialSpawnTime | 180 |
| [0].RespawnInterval | 180 |
| [1].InitialSpawnTime | 300 |
| [1].RespawnInterval | 300 |
| [2].InitialSpawnTime | 600 |
| [2].RespawnInterval | 180 |
| [3].InitialSpawnTime | 300 |
| [3].RespawnInterval | 180 |

## Patch history (112 lines, newest first)

**2026-09-16** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1844115010490072))

- Breakables in the underground tunnels initial spawn time increased from 3m to 5m
- Breakables in the underground tunnels respawn rate increased from 3m to 5m

**2026-06-30** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1836506165563227))

- Unstable Rift no longer grants +1 permanent buff to each player (there is also no +3 buffs to the urn runner)
- Urn runner gets +4 permanent buffs on deposit

**2026-06-11** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1835236783562074))

- Breakables health permanent bonus reduced from 15/25/35 to 15/20/30 for level 1/2/3

**2026-05-22** ([forum post](https://forums.playdeadlock.com/threads/05-22-2026-update.135477/))

- Breakables spawn time increased from 2 minutes to 3 minutes
- All rewards are the same. The last person to contest the urn gets the +3 Golden Idol buffs, falling back to the original carrier if nobody contested it.
- [ General ] - Base HP reduced by 10 for all heroes - HP per boon reduced by 3 - Guardians scaling resistance from +75%->-50% over 12 minutes to +50%->-50% (takes more damage early) - Medium neutrals initial spawn time reduced from 6 minutes to 5 minutes - Breakables spawn time increased from 2...

**2026-03-07** ([forum post](https://forums.playdeadlock.com/threads/03-06-2026-update.114328/post-217955))

- Golden Egg Goose: Souls Per Minute increased from 75 to 90
- Golden Egg Goose: Souls Per Minute increased from 75 to 90

**2025-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/))

- Team that kills Mid Boss gets +2 permanent buffs for each player
- Soul Urn now provides 4 Permanent Buffs to the person dropping it off
- Golden Statue: Cooldown Reduction reduced from 0.75/1.0/1.5% to 0.5/0.75/1%

**2025-07-29** ([forum post](https://forums.playdeadlock.com/threads/07-29-2025-update.72760/))

- Breakables souls growth per minute reduced from 2.6 to 2.0

**2025-06-17** ([forum post](https://forums.playdeadlock.com/threads/06-17-2025-update.68401/))

- Adjusted breakables that were spread out in the underground

**2025-05-27** ([forum post](https://forums.playdeadlock.com/threads/05-27-2025-update.66453/))

- Breakable souls rescaled from 28.5 + 2.375/min to 23 + 2.6/min

**2025-05-21** ([forum post](https://forums.playdeadlock.com/threads/05-21-2025-update.65674/))

- Fixed Breakable souls being counted as secured souls rather than unsecured souls (this fix was released yesterday)
- Added Breakable souls to the post game Souls by Source graph (was previously bundled in with Urn)
- Added statues in front of Mid Lane entrances for cover.
- Tweaked trooper nodes to go around new statues.

**2025-03-13** ([forum post](https://forums.playdeadlock.com/threads/03-13-2025-update.58592/))

- Golden Statue Buffs adjustments

**2024-12-06** ([forum post](https://forums.playdeadlock.com/threads/12-06-2024-update.50599/))

- Added text box field to the post-game survey

**2024-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2024-update.47476/))

- Adjusted Powerup Runes' design to look more visually breakable (due to melee change explained later in the gameplay section)
- Gaining Rejuvenator buff now shows what stats have been improved on your hero (like powerups and other buffs)
- Revised Casting bridge buff loop
- Powerups now require a heavy melee to claim (art visuals updated)
- Powerups now start weaker and grow stronger (from 10 minutes to 40  minutes)
- Gun Powerup:
- Survival Powerup:
- Casting Powerup:
- Movement Powerup:

**2024-11-07** ([forum post](https://forums.playdeadlock.com/threads/11-07-2024-update.44786/))

- Fixed the 'x' button in the shop search not clearing the search box
- Added an ambient looping sound for each bridge powerup

**2024-10-24** ([forum post](https://forums.playdeadlock.com/threads/10-24-2024-update.40951/))

- Breakables spawn time increased from 2 minutes to 3 minutes
- Breakables Souls reduced from 35 + 3/min to 30 + 2.5/min

**2024-10-15** ([forum post](https://forums.playdeadlock.com/threads/10-15-2024-update.38925/))

- T3 Golden Statues spawn time moved from 25 min to 30 min

**2024-10-10** ([forum post](https://forums.playdeadlock.com/threads/10-10-2024-update.36958/))

- If you enter a Build ID in the search box of the build browser, it will show all of the builds for the current hero by the author of that build.
- Golden Statues and Breakables spawn time changed from 3 min to 2 min
- Golden Statues bonuses upgrade time changed from 15 min to 10 min
- Golden Statue Health buff increased from 15/20 to 20/30
- Golden Statues now have a tier 3 upgrade at 25 minutes (+2.5% Fire Rate, +8% Ammo, 1.5% CD Reduction, +7% Weapon Damage, 40 Health, +5 Spirit Power)
- Urn delivery now gives each player on your team a Golden Statue permanent buff

**2024-09-26** ([forum post](https://forums.playdeadlock.com/threads/09-26-2024-update.33015/))

- Picking up a powerup will now list all the stats they modify in the HUD instead of a generic name like 'Casting' or 'Gun'
- Fixed Dash not always breaking breakables
- Breakables will now wait to spawn if a player is in the way
- Sinner's Sacrifice now grants a permanent golden statue bonus when it is killed
- Fixed dashing downwards not destroying breakables

**2024-09-12** ([forum post](https://forums.playdeadlock.com/threads/09-12-2024-update.27974/))

- Sand Box orb practice area now displays the time in milliseconds that you hit the orb after spawning
- Fixed multiple heroes getting the power-up bonus by standing on top of it before spawns
- Replaced wall landing in front of the Nursery and the Market with an electrical box
- Fixed breakable items outside the underground tunnel

**2024-08-29** ([forum post](https://forums.playdeadlock.com/threads/08-29-2024-update.22253/))

- Fixed some tooltips not showing golden statue bonuses if it wasn't the direct stat (i.e. you got fire rate but bullets per second didn't show the golden statue)
- Golden Statues drop rate increased by 6%
- Breakable containers have been added to the new playable rooftops
- Lowered the statue pedestals in the inner lanes outside of Mid

**2024-08-15** ([forum post](https://forums.playdeadlock.com/threads/08-15-2024-update.16378/))

- Individual stats can now be hovered over to see a breakdown of all the bonuses contributing to a value, including things like golden statues

**2024-08-01** ([forum post](https://forums.playdeadlock.com/threads/08-01-2024-update.13369/))

- Movement Powerup: Stamina regen increased from 20% to 30%
- Movement Powerup: Sprint speed increased from +2 to +3
- Movement Powerup: Zipline bonus increased from 30% to 50%
- Gun Powerup: Ammo increased from +30% to +40%
- Powerup durations increased from 150s to 160s
- Moved breakable idols from the street level juke spots to other locations

**2024-07-18** ([forum post](https://forums.playdeadlock.com/threads/07-18-2024-update.11831/))

- Powerup spawn locations moved to the bridges
- Powerup buff duration increased from 130s to 150s
- Golden Statues level 2 drops now happen at 15 minutes instead of 20
- Increased golden statue drop chance by 4%

**2024-07-11** ([forum post](https://forums.playdeadlock.com/threads/07-11-2024-update.10871/))

- Added new sound effects to picking up powerups and breakable drops
- Powerup Bonus duration increased from 100s to 130s
- Movement powerup now grants +20% stamina regeneration
- Fixed Movement powerup not replenishing stamina on pickup
- Golden Statues level 2 bonuses spawn time reduced from 25 minutes to 20 minutes
- Golden Statues Weapon Damage bonus increased from 2% to 3% (level 2 from 3% to 4%)
- Golden Statues Ammo bonus increased from 3% to 4% (level 2 from 5% to 6%)
- Capture radius for breakable drops increased very slightly

**2024-07-04** ([forum post](https://forums.playdeadlock.com/threads/07-04-2024-update.9652/))

- Reworked how Powerups work. There are now only 2 locations where they spawn instead of 6 (the two at the strong camps near the middle far edges of the map). The different powerup types are reduced from 6 to 4 and they have been reworked:
- Powerups now always cycle which ones spawn until they have each spawned, and then they are randomly allocated again
- Breakables are no longer pre-placed on the map, they now spawn in when they are able to roll for drops (3 minutes)
- Breakables now use pseudorandom rolls (makes streaks of success or failure less likely)
- Golden Statue bonuses now have some dynamic weighting based on what has already dropped (makes it less likely that you have too many of one specific bonus over the course of the game)
- Golden Statue's CD Reduction bonus increased from 0.5% to 0.75%
- After 25 minutes, the Golden Statue bonuses that drop are slightly stronger:

**2024-06-27** ([forum post](https://forums.playdeadlock.com/threads/06-27-2024-update.8486/))

- Crates now show the amount of souls they have in the tooltip
- Golden Statues no longer drop powerups (time duration buffs). Instead they now drop small permanent bonuses. These stack and do not decay with time or death. Drop rates rebalanced.
- At defined locations around the map, powerups now spawn starting 10 minutes (and every 5 minutes after). There are 6 spots where they spawn and they are indicated on the minimap when they are up.
- Movement powerup duration increased from 30s to 50s
- Fire Rate powerup duration increased from 35s to 45s and +15% Fire Rate to +18%
- Regeneration powerup duration increased from 25s to 45s
- Stamina powerup duration increased from 80s to 120s
- Cooldown powerup is unchanged
- Clip powerup is unchanged
- Breakables initial spawn time increased from 2 min to 3 min
- Breakables souls base value reduced by 30%. Increases to +15% of current values over 30 minutes. (so -30% to +15% from start to 30 min)
- Added connection hallway between outer lane Shop and crate room

**2024-06-06** ([forum post](https://forums.playdeadlock.com/threads/06-06-2024-update.4096/))

- Powerups bonus types are now split between the regular destructibles like crates/vases/etc and the Golden Statues. Regular ones can only roll for souls and Golden Statues can only roll for buffs. Distribution of destructibles and Golden Status around the map has been adjusted a bit.
- Respawn rate for Destructibles/Statues (after initial spawn) slowed from 120s to 180s
- Movement Speed powerup duration increased from 12s to 30s
- Movement Speed powerup movespeed reduced from 2 to 1
- Movement Speed powerup sprint speed increased from 2 to 4
- Fire Rate powerup reduced from +20% to +15%
- Fire Rate powerup duration increased from 25s to 35s
- Health Regen powerup regen reduced from 1.5% to 1%
- Health Regen powerup duration increased from 15s to 25s
- Cooldown Reduction powerup reduced from 25% to 20%
- Extra Clip powerup reduced from 4 clips to 3
- Extra Stamina powerup duration increased from 60s to 80s
- Extra Stamina powerup amount reduced from 2 to 1

**2024-05-30** ([forum post](https://forums.playdeadlock.com/threads/05-30-2024-update.2514/))

- Crate powerups can now only spawn after 2 minutes (when the small neutrals spawn)
- Added breakable crates inside each lane's Cosmic Veil

**2024-05-23** ([forum post](https://forums.playdeadlock.com/threads/05-23-2024-update.1245/))

- Removed stack of cardboard boxes inside connection hallway near bases to prevent cover from Neutrals

**2024-05-13** ([forum post](https://forums.playdeadlock.com/threads/05-13-2024-update.807/))

- Crate Powerups: Removed Zipline buff as a potential drop
- Crate Powerups: Increased Health Regen drop from 1.25% Regen to 1.5%
- Crate Powerups: Added Fire Rate drop, provides +20% Fire Rate for 25s
