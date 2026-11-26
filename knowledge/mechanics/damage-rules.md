# Damage rules: headshots, falloff, resists, stacking

Generated from the game files at build 6868 and Valve's patch notes. Everything below is quoted from a source, not interpreted. Patch notes describe the game as of their date: read newest first, and treat an older line as history once a newer one changes the same thing. The patch notes do not record every change, so where a current number below differs from the newest note, the number is right. Questions already worked through are answered in [settled.md](../settled.md).

## What the game itself says

- Cooldown Per Headshot NPC (`AbilityCooldownPerHeadshotNPC_label`)
- Cooldown Per Headshot NPC (`AbilityCooldownPerHeadshotNPC_postvalue_label`)
- Cooldown Per Headshot (`AbilityCooldownPerHeadshot_label`)
- Cooldown Per Headshot (`AbilityCooldownPerHeadshot_postvalue_label`)
- Bullet Resist Reduction (`ActiveBulletArmorReduction_label`)
- Bullet Resist Reduction (`ActiveBulletArmorReduction_postvalue_label`)
- Enemy Bullet Resist (`AirDropBulletArmorReduction_label`)
- Enemy Bullet Resist (`AirDropBulletArmorReduction_postvalue_label`)
- Ally Bullet Resist (`AirDropBulletResist_label`)
- Ally Bullet Resist (`AirDropBulletResist_postvalue_label`)
- %s1 to any bullet and spirit armor bonus (`ArmorAttribute_Desc`)
- no additional bullet armor bonuses (`ArmorAttribute_Desc_0`)
- Bullet & Spirit Resistance Per Stack (`ArmorDamageReductionPerStack_postvalue_label`)
- Resist lost per Hit (`ArmorLossPerHit_label`)
- Bullet Resist per Bite (`ArmorReductionPerBite_label`)
- Bullet Resist per Bite (`ArmorReductionPerBite_postvalue_label`)
- Burn Spirit Resist (`BabaBrewBurnSpiritResist_label`)
- Burn Spirit Resist (`BabaBrewBurnSpiritResist_postvalue_label`)
- Heal Per Headshot (`BaseHealOnHeadshot_label`)
- Heal Per Headshot (`BaseHealOnHeadshot_postvalue_label`)
- Spirit Resist (`BleedTechResist_label`)
- Spirit Resist (`BleedTechResist_postvalue_label`)
- Bonus Crit Damage (`BonusCritDamagePercent_label`)
- Increased Damage (`BonusDamageAmp_label`)
- Bonus Headshot Damage (`BonusHeadshotDamage_label`)
- Bonus Headshot Damage (`BonusHeadshotDamage_postvalue_label`)
- Bonus Per Headshot (`BonusPerHeadshot_label`)
- Bullet Resist (`BuffBulletResist_label`)
- Bullet Resist (`BuffBulletResist_postvalue_label`)
- Spirit Resist (`BuffTechResist_label`)
- Spirit Resist (`BuffTechResist_postvalue_label`)
- Bullet Resist per Stack (`BulletArmorDamageReductionPerStack_label`)
- Bullet Resist per Stack (`BulletArmorDamageReductionPerStack_postvalue_label`)
- Bullet Resist (`BulletArmorDamageReduction_label`)
- Bullet Resist (`BulletArmorDamageReduction_postvalue_label`)
- Target Bullet Resist (`BulletArmorPenetration_label`)
- Bullet Damage (`BulletArmorReductionPerStack_label`)
- Bullet Damage (`BulletArmorReductionPerStack_postvalue_label`)
- Bullet Resist (`BulletArmorReduction_label`)
- Bullet Resist (`BulletArmorReduction_postvalue_label`)
- Bullet Armor (`BulletArmor_label`)
- Bullet Armor (`BulletArmor_postvalue_label`)
- Wrecked Duration (`BulletDamageAmpDuration_postvalue_label`)
- Wrecked Bullet Amp (`BulletDamageAmp_postvalue_label`)
- Stack Duration (`BulletResistDuration_label`)
- Stack Duration (`BulletResistDuration_postvalue_label`)
- Bullet Resist (`BulletResistOnActive_label`)
- Bullet Resist (`BulletResistOnActive_postvalue_label`)
- Bullet Resist per Stack (`BulletResistPerStack_label`)
- Bullet Resist per Stack (`BulletResistPerStack_postvalue_label`)
- Bullet Resist per Stack (`BulletResistReductionPerStack_label`)
- Bullet Resist per Stack (`BulletResistReductionPerStack_postvalue_label`)
- Bullet Resist (`BulletResistReduction_label`)
- Bullet Resist (`BulletResistReduction_postvalue_label`)
- Bullet Resist (`BulletResist_label`)
- Bullet Resist (`BulletResist_postvalue_label`)
- HeadShot Bonus (`CarbineHeadshotBonus_label`)
- HeadShot Bonus (`CarbineHeadshotBonus_postvalue_label`)
- Headshot Enthusiasts (`CitadelComponentGroup_EHeadshotEnthusiasts`)
- Falloff Range (`CitadelHeroStats_Weapon_Falloff`)
- Bullet Resist (`Citadel_Graph_PermanentBuff_BulletResist`)
- Spirit Resist (`Citadel_Graph_PermanentBuff_SpiritResist`)
- Gun Damage - Crit (`Citadel_Graph_WeaponDamageCrit`)
- Spirit Damage (`Citadel_HUD_LevelReward_BulletResist`)
- Health Critical (`Citadel_Hud_HealthCritical`)
- Vitality Investment (`Citadel_ModBonus_ArmorInvestment`)
- Health Increases (`Citadel_ModBonus_ArmorInvestmentDesc`)
- Bullet Resist (`Citadel_Player_Level_BulletResist`)
- Spirit Resist (`Citadel_Player_Level_TechResist`)
- Most Headshot Kills (`Citadel_PostGame_AwardHeadshotKills`)
- Second Most Headshot Kills (`Citadel_PostGame_AwardHeadshotKills_Rank2`)
- Third Most Headshot Kills (`Citadel_PostGame_AwardHeadshotKills_Rank3`)
- Headshot Kills (`Citadel_PostGame_AwardHeadshotKills_RankOther`)
- Critical Bug (`Citadel_UserFeedback_eType_CriticalBug`)
- Combo Bullet Resist (`ComboBulletResist_label`)
- Combo Bullet Resist (`ComboBulletResist_postvalue_label`)
- Buildup Per Headshot (`CritBuildup_label`)
- Buildup Per Headshot (`CritBuildup_postvalue_label`)
- Critical Chance (`CritChance_label`)
- Critical Chance (`CritChance_postvalue_label`)
- Crit Coating Crit Bonus (`CritCoatingDamagePercent_label`)
- Bonus Weapon Damage (`CritDamagePercent_label`)
- Bonus Weapon Damage (`CritDamagePercent_postvalue_label`)
- Crit Charge Delay (`CritStackInterval_label`)
- Bonus Damage per Stack (`DamageAmplificationPerStack_label`)
- Bonus Damage per Stack (`DamageAmplificationPerStack_postvalue_label`)
- Channel Damage Resist (`DamageResistPctWhileChanneling_postvalue_label`)
- Bullet and Spirit Resist Reduction (`DiamondResistShred_label`)
- Bullet and Spirit Resist Reduction (`DiamondResistShred_postvalue_label`)
- Debuff Resistance (`EShopFilterDebuffResist`)
- Melee Resistance (`EShopFilterMeleeResist`)
- Physical Resistance (`EShopFilterPhysicalResist`)
- Slow Resistance (`EShopFilterSlowResist`)
- Spirit Resistance (`EShopFilterSpiritResist`)
- Spirit Resist On Spirit Damage (`EscalatingExposureTechArmorDamageReduction_label`)
- Spirit Resist On Spirit Damage (`EscalatingExposureTechArmorDamageReduction_postvalue_label`)
- Bullet Resist (`FervorBulletResist_label`)
- Bullet Resist (`FervorBulletResist_postvalue_label`)
- Enrage Debuff Resistance (`FervorDebuffResistance_label`)
- Debuff Resist (`FervorStatusResistancePercent_label`)
- Debuff Resist (`FervorStatusResistancePercent_postvalue_label`)
- Spirit Resist (`FervorTechResist_label`)
- Spirit Resist (`FervorTechResist_postvalue_label`)
- Bullet Resist (`FlyingBulletResist_label`)
- Bullet Resist (`FlyingBulletResist_postvalue_label`)
- Head Shot Bonus Damage (`HeadShotBonusDamage_label`)
- Head Shot Bonus Damage (`HeadShotBonusDamage_postvalue_label`)
- Headshot Damage (`HeadshotBonus_label`)
- Headshot Damage (`HeadshotBonus_postvalue_label`)
- Headshot Heal Bonus (`HeadshotHealBonusPercent_label`)
- Headshot Heal Bonus (`HeadshotHealBonusPercent_postvalue_label`)
- Heal Per Headshot (`HealPercentPerHeadshot_label`)
- Heal Per Headshot (`HealPercentPerHeadshot_postvalue_label`)
- bullet resist (`InlineAttribute_BulletResist`)
- increased damage (`InlineAttribute_DamageAmp`)
- slow resistance (`InlineAttribute_SlowResistance`)
- spirit resist (`InlineAttribute_SpiritResist`)
- Debuff Resist (`InnateStatusResistancePercent_label`)
- Debuff Resist (`InnateStatusResistancePercent_postvalue_label`)
- Bullet Resist (`LocalBulletArmorReduction_label`)
- Bullet Resist (`LocalBulletArmorReduction_postvalue_label`)
- Magic Resist (`LocalTechArmorReduction_label`)
- Spirit Resist (`LowHealthTechResist_label`)
- Spirit Resist (`LowHealthTechResist_postvalue_label`)
- Spirit Resist (`MagicResistReduction_label`)
- Spirit Resist (`MagicResistReduction_postvalue_label`)
- Max Bullet Resist (`MaxArmorStacks_label`)
- Max Bullet Resist (`MaxArmorStacks_postvalue_label`)
- Max Bullet Resist (`MaxBulletResist_label`)
- Max Bullet Resist (`MaxBulletResist_postvalue_label`)
- Max Spirit Resist Stolen (`MaxStolenSpiritResist_label`)
- Max Spirit Resist Stolen (`MaxStolenSpiritResist_postvalue_label`)
- Melee Resist (`MeleeResistPercent_label`)
- Melee Resist (`MeleeResistPercent_postvalue_label`)
- Melee Resist Reduction Duration (`MeleeResistReductionDuration_label`)
- Debuff Duration (`MeleeResistReductionDuration_postvalue_label`)
- Melee Resist (`MeleeResistReduction_label`)
- Melee Resist (`MeleeResistReduction_postvalue_label`)
- Melee Resist (`MeleeResist_label`)
- Melee Resist (`MeleeResist_postvalue_label`)
- Bullet Resist Duration (`NanoShadowBulletArmorReductionDuration_label`)
- Bullet Resist Duration (`NanoShadowBulletArmorReductionDuration_postvalue_label`)
- Bullet Resist (Heavy) (`NanoShadowBulletArmorReductionHeavy_label`)
- Bullet Resist (Heavy) (`NanoShadowBulletArmorReductionHeavy_postvalue_label`)
- Bullet Resist (Light) (`NanoShadowBulletArmorReductionLight_label`)
- Bullet Resist (Light) (`NanoShadowBulletArmorReductionLight_postvalue_label`)
- against NPCs (`NonPlayerBulletResist_conditional`)
- Bullet Resist vs. NPCs (`NonPlayerBulletResist_label`)
- Bullet Resist vs. NPCs (`NonPlayerBulletResist_postvalue_label`)
- Nearby Defender Resistance (`Objective_Defender_Resistant`)
- Damage Amp per stack (`PulseGrenadeDamageAmplificationPerStack_label`)
- Damage Amp per stack (`PulseGrenadeDamageAmplificationPerStack_postvalue_label`)
- Extend Per Headshot (`RefillDurationCrit_label`)
- Extend Per Headshot (`RefillDurationCrit_postvalue_label`)
- Debuff Duration (`ResistDuration_postvalue_label`)
- Debuff Duration (`ResistDuration_value_label`)
- Resist Reduction Duration (`ResistReductionDuration_label`)
- Resist Reduction Duration (`ResistReductionDuration_postvalue_label`)
- Resist Stolen (`ResistStealAmount_label`)
- Resist Stolen (`ResistStealAmount_postvalue_label`)
- Resist Per Stack (`ResistancePerStack_label`)
- Resist Per Stack (`ResistancePerStack_postvalue_label`)
- Bullet Resist (`ReturnFireBulletResist_label`)
- Bullet Resist (`ReturnFireBulletResist_postvalue_label`)
- Slow Resistance (`SlowResistance_label`)
- Slow Resistance (`SlowResistance_postvalue_label`)
- Spirit Resist on Headshot (`SpellSlingerHeadshots_SpiritShredPerStack_label`)
- Spirit Resist on Headshot (`SpellSlingerHeadshots_SpiritShredPerStack_postvalue_label`)
- Spirit Resist Steal (`SpiritSnatch_TechArmorSteal_label`)
- Spirit Resist Steal (`SpiritSnatch_TechArmorSteal_postvalue_label`)
- Bullet Resist (`StatDesc_BulletArmorDamageReduction`)
- Bullet Resist (`StatDesc_BulletArmorDamageReduction_postvalue_label`)
- Crit Bonus Scale (`StatDesc_CritDamageBonusScale`)
- Crit Bonus Scale (`StatDesc_CritDamageBonusScale_postvalue_label`)
- Crit Reduction (`StatDesc_CritDamageReceivedScale`)
- Crit Reduction (`StatDesc_CritDamageReceivedScale_postvalue_label`)
- Damage Amplification - Percentage modification to any outgoing damage (`StatDesc_DamageAmpDesc`)
- Debuff Resist (`StatDesc_DebuffResist`)
- Debuff Resist (`StatDesc_DebuffResist_postvalue_label`)
- Melee Resist (`StatDesc_MeleeResist`)
- Melee Resist (`StatDesc_MeleeResist_postvalue_label`)
- Spirit Armor - Your resistance to incoming Spirit Damage (`StatDesc_SpiritResistDesc`)
- Spirit Armor (`StatDesc_TechArmor`)
- Spirit Resist (`StatDesc_TechArmorDamageReduction`)
- Spirit Resist (`StatDesc_TechArmorDamageReduction_postvalue_label`)
- Spirit Armor (`StatDesc_TechArmor_postvalue_label`)
- Bullet Armor - Your resistance to incoming Bullet Damage (`StatDesc_WeaponResistDesc`)
- Debuff Resist (`StatusResistancePercent_label`)
- Debuff Resist (`StatusResistancePercent_postvalue_label`)
- Spirit Resistance per Stack (`TechArmorDamageReductionPerStack_label`)
- Spirit Resistance per Stack (`TechArmorDamageReductionPerStack_postvalue_label`)
- Spirit Resist (`TechArmorDamageReduction_Label`)
- Spirit Resist (`TechArmorDamageReduction_postvalue_label`)
- Spirit Resist (`TechArmorGain_postvalue_label`)
- Spirit Armor (`TechArmor_label`)
- Spirit Armor (`TechArmor_postvalue_label`)
- Spirit Amp per Stack (`TechResistPerStack_label`)
- Spirit Amp per Stack (`TechResistPerStack_postvalue_label`)
- Target Spirit Resist (`TechResistReduction_label`)
- Spirit Resist (`TechResist_label`)
- Spirit Resist (`TechResist_postvalue_label`)
- +0.5% Bullet Resist (`bulletresist_permanent_pickup_label`)
- +0.75% Bullet Resist (`bulletresist_permanent_pickup_label_lv2`)
- +1% Bullet Resist (`bulletresist_permanent_pickup_label_lv3`)
- Missing critical keybind (`citadel_bind_key_legend_missing_critical`)
- %s1 headshots %s2 for %s3 damage%s4. (`citadel_combat_log_headshots_with_gun`)
- %s1 headshots %s2 %s5x for %s3 damage%s4. (`citadel_combat_log_headshots_with_gun_n`)
- Ira Domini - Crit (`citadel_weapon_priest_crossbow_crit`)
- +0.5% Spirit Resist (`spiritresist_permanent_pickup_label`)
- +0.75% Spirit Resist (`spiritresist_permanent_pickup_label_lv2`)
- +1% Spirit Resist (`spiritresist_permanent_pickup_label_lv3`)

## Current numbers in the game files

- No dedicated block for this in the files the sheet reads; see the sheet's tables.

## Patch history (215 lines, newest first)

**2026-09-16** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1844115010490072))

- Unstable Rift comeback resist max values now scale over the course of the game. Previously the max values were 35%. Now it is 10% + 1% per minute (around ~20% for the first one), with an upper limit of 40% at 30 minutes.

**2026-07-28** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1839041357039193))

- Doorman: Bullet damage rescaled from 26 + 1.19/boon to 24 + 1.25

**2026-07-09** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1836506165584438))

- Rift Troopers now have Spirit Resist (30/35/40/45%)
- Rift Troopers now have Melee Resistance (25%)
- Unstable Rift comeback resist aura radius increased from 20m to 35m
- Doorman: Bullet damage rescaled from 29.26 + 1.1/boon to 26 + 1.19
- Doorman: Crit scaling reduced from -25% to -30%

**2026-06-30** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1836506165563227))

- Unstable Rift comeback bonuses (resists in the area, extra comeback bounty, and trailing/leading team claiming timer) now all scale linearly based on the amount of NW they are trailing (scales from no bonus at 0% NW behind to full bonus at 15% NW behind)

**2026-06-04** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1834602721188293))

- Urn comeback resistance now also grants +35% Debuff Resistance ontop of the 35% Bullet and Spirit Resistance
- Urn comeback resistance aura reduced from 60m to match the 20m progress radius

**2026-05-28** ([forum post](https://forums.playdeadlock.com/threads/05-22-2026-update.135477/post-261657))

- Urn no longer provides the +35% Bullet and Spirit Resist aura for the behind team when it is being carried or dropped. The aura is now only active when it is being deposited.
- Urn runner when behind now gains +35% Bullet and Spirit Resist for themselves only
- Urn spawn time and interval changed from 10/15/20/25/etc to 12/18/24/30/etc - Urn timer now gets frozen with Frozen Shelter - Urn no longer provides the +35% Bullet and Spirit Resist aura for the behind team when it is being carried or dropped. The aura is now only active when it is being...

**2026-05-25** ([forum post](https://forums.playdeadlock.com/threads/05-22-2026-update.135477/post-259788))

- Urn comeback bullet and spirit resist auras reduced from 50% to 35%

**2026-05-22** ([forum post](https://forums.playdeadlock.com/threads/05-22-2026-update.135477/))

- Guardians scaling resistance from +75%->-50% over 12 minutes to +50%->-50% (takes more damage early)
- Bullet Velocity now stacks additively rather than diminishingly
- When receiving multiple of the Medic trooper orb the duration will now be added ontop rather than stacking directly (so picking up 4 in a row will give the regen over 16s instead of over 4s, overall heal is the same just slower)
- Base Guardian Bullet Resistance increased from 10% to 20%
- Shrine Bullet Resistance increased from 10% to 20%
- Tier 2 Bullet Resistance increased from 25% to 35%
- Total Damage Reduction debuffs now stack diminishingly rather than additively (Inhibitor, Fire Scarabs, etc)
- Movespeed diminish point increased from 11 to 12 (very slightly less aggressive diminishing scaling)
- Fixed the following items and abilities not working through veils: Heroic Aura, Healing Rite, Healing Nova, Rescue Beam, Divine Barrier, Kudzu Connection, Cube, Tag Along, Lil Helpers, Guardian Ward, Scourge, Plot Armor
- If the urn is Favored or Unfavored (in a comeback state), then the Favored team will get +50% Bullet and Spirit Resist in a 60m radius around the urn while it is being carried, dropped or deposited.
- No longer grants +30% Bullet and Spirit Resist while carrying it
- Doorman: Call Bell inaccuracy debuff no longer diminishes from 100% to 0% over 1 second (the rest of the debuff is 4s)
- [ General ] - Base HP reduced by 10 for all heroes - HP per boon reduced by 3 - Guardians scaling resistance from +75%->-50% over 12 minutes to +50%->-50% (takes more damage early) - Medium neutrals initial spawn time reduced from 6 minutes to 5 minutes - Breakables spawn time increased from 2...

**2026-04-30** ([forum post](https://forums.playdeadlock.com/threads/04-30-2026-update.129989/))

- [ General ] - Base health per boon reduced by 7 - Vitality Investment bonus increased from 8/10/13/17/34/39/44/48/52/56% to 9/12/15/20/38/42/46/50/56/62% - Weapon Investments bonus rescaled from 7/9/13/20/49/60/80/95/115/135% to 9/12/15/18/46/55/70/85/100/115% - Reduced bullet damage growth by...

**2026-04-10** ([forum post](https://forums.playdeadlock.com/threads/04-10-2026-update.125825/))

- Armor Piercing Rounds: Chance increased from 50% to 55%
- Armor Piercing Rounds: Chance increased from 50% to 55%

**2026-03-21** ([forum post](https://forums.playdeadlock.com/threads/03-06-2026-update.114328/post-226950))

- Small neutrals spirit resist increased from 35% to 45%
- Small neutrals spirit resist increased from 35% to 45%

**2026-03-06** ([forum post](https://forums.playdeadlock.com/threads/03-06-2026-update.114328/))

- Walkers armor decay rescaled from "+75% -> -50%" to "+65% -> -65%", from over 20min to over 18min
- Mid Boss now has 35% Debuff Resistance
- Move speed diminishing ramp now occurs around 11m rather than 10m
- Diamond: Cuts enemy resistances by -8% for 5s. Does not stack.

**2026-01-30** ([forum post](https://forums.playdeadlock.com/threads/01-30-2026-update.102822/))

- Updated various on bullet hit resistance reduction debuffs to apply increased damage for subsequent hits rather than initial hit (similar to the spirit damage proc cases)
- Curse: No longer grants +15% Weapon Damage

**2026-01-20** ([forum post](https://forums.playdeadlock.com/threads/12-29-2025-update.95233/post-185824))

- Urn carrier resist reduced from 50% to 30%

**2025-12-16** ([forum post](https://forums.playdeadlock.com/threads/12-16-2025-update.93983/))

- Move Speed bonuses now stack diminishingly
- Urn: Bullet and Spirit resist for carrier increased from 30% to 50%
- Neutrals spirit resistance increased by 5%
- Fixed a bug causing AP Rounds to reduce damage on targets with negative resist
- When Armor Piercing Rounds Proc's, Plated Armor can no longer stop the Proc'd Bullet.

**2025-12-03** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/post-174987))

- Walkers and Mid Boss now have +15% Bullet Resistance and -15% HP
- Walker ally aura (grants +15% Bullet and Spirit Resist) range reduced from 32m to 28m

**2025-11-23** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/post-172057))

- Fixed a bug with falloff calculation that was often causing guns to do much more damage than intended. We'll be monitoring to do subsequent adjustments after this.
- Guardians armor decay peak at 12m instead of 10m

**2025-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/))

- Medium neutrals spirit resist from 30% to 40%
- Hard neutrals spirit resist increased from 35% to 50%
- Headshot multiplier reduced from 1.8x to 1.65x
- Weapon Investment Bonuses: Now grants an additional +20% Weapon Damage at 4800 souls spent
- Walker fireballs now reduce bullet and spirit resistance by 10%
- Bullet Damage is no longer reduced by 35% of a Hero's Base Bullet damage against T1's
- Guardians now start with 75% Damage Resist that decay's to -50% over the first 10 minutes of a match
- Walkers now start with 75% Damage Resist that decay's to -50% over the first 20 minutes of a match
- Note: The Walker resistance change used to be in the client a couple months ago, but it got bugged.
- Rejuv buff no longer grants +10% Max HP, +15% Fire Rate and +15% Spirit Damage Amp
- Curse: Weapon Damage reduced from 20% to 15%
- Doorman: Bullet damage falloff and effectiveness now use the actual distance traveled, rather than the distance between the starting position and end position. This fixes shooting through portals not using the right distance for falloff.

**2025-10-24** ([forum post](https://forums.playdeadlock.com/threads/10-24-2025-update.87198/))

- Doorman: Bullet damage growth per boon reduced from 1.15 to 1.0
- Doorman: Outgoing headshot damage multiplier reduced by 25%

**2025-10-02** ([forum post](https://forums.playdeadlock.com/threads/10-02-2025-update.84332/))

- Mid Boss damage resistance per second reduced from 50 + 7/min to 35 + 5/min
- Soul Urn: Carriers now have +30% bullet and +30% spirit Resist
- Fixed ordering issues with various items with Bullet based Procs. Debuffs (ie. negative Bullet Resist) from all procs are now applied before any bonus damage from the procs. Items include Weakening Headshot, Crippling Headshot, Headshot Booster, Headhunter, Hollow Point and Mystic Shot.

**2025-07-29** ([forum post](https://forums.playdeadlock.com/threads/07-29-2025-update.72760/))

- Reworked Rejuv reward from Mid Boss. No longer buffs troopers, reduces respawn time and buffs various stats. Upon death, 3 rejuv crystals fall to the ground (4 for subsequent midboss kills). Claiming one now grants you in place revive after 3s. If you already claimed one and claim another, it'll go to an ally (priority is closest allies first, then most recent dead allies). Dying with Rejuv no longer counts as a kill/death nor gives out bounties. While you have the Rejuv buff, you gain the following: +20% Max HP, +20% Fire Rate, and +15% Spirit Damage. Gaining the buff heals you to full and lasts up to 7 minutes.
- Parried stun duration is no longer reduced by debuff resistance
- Objectives no longer have 20-25% Spirit Resistance
- Spirit Shredder Bullets: Spirit Resist Reduction increased from -7% to -8%
- Armor Piercing Rounds: Chance reduced from 60% to 50%

**2025-07-04** ([forum post](https://forums.playdeadlock.com/threads/07-04-2025-update.70156/))

- Mid Boss Spirit Resistance from abilities reduced from 30% to 20%
- Mid Boss Spirit Resistance from items reduced from 50% to 20%
- Walker Spirit resistance reduced from 30% to 25%
- Guardian base resistance increased from 40% to 60% (decays 10 minutes still, same values as creeps)

**2025-06-17** ([forum post](https://forums.playdeadlock.com/threads/06-17-2025-update.68401/))

- Walker Spirit Resist reduced from 40% to 30%
- Headshot multiplier reduced from 1.9x to 1.8x

**2025-05-27** ([forum post](https://forums.playdeadlock.com/threads/05-27-2025-update.66453/))

- Trooper resistance near base reduced from 40% to 35%
- Fixed Neutrals near the base gaining the "near base" trooper resist
- Armor Piercing Rounds: Bullet Velocity increased from 30% to 35% (to match the component)

**2025-05-21** ([forum post](https://forums.playdeadlock.com/threads/05-21-2025-update.65674/))

- Troopers will now only flinch from player damage if it is a headshot while the trooper is busy running.
- Trooper resistance near base reduced from 50% to 40%

**2025-05-19** ([forum post](https://forums.playdeadlock.com/threads/05-19-2025-update.65381/))

- Troopers now gain 50% resistance when they are in near the base (this has been 30% the past few days)
- Walkers resistance vs troopers reaches -40% at 20 minutes instead of 16 minutes
- Objectives Spirit Resistance reduced from 50% to 40%
- Armor Piercing Rounds: Chance reduced from 65% to 60%

**2025-04-17** ([forum post](https://forums.playdeadlock.com/threads/04-17-2025-update.61382/))

- Fixed Debuff Resistance affecting Urn pickup time
- Hollow Point Ward: Weapon Damage reduced from 20% to 18%

**2025-04-04** ([forum post](https://forums.playdeadlock.com/threads/04-04-2025-update.60284/))

- Lifesteal provided by things like Soul Shredder bullets now properly diminishes in stacking with other sources of lifesteal
- Fixed spellslinger headshots providing more bonuses than intended

**2025-01-27** ([forum post](https://forums.playdeadlock.com/threads/01-27-2025-update.54590/))

- All objectives now take 50% less damage from Spirit Damage (abilities no longer have one off values for this)
- Shrines are no longer vulnerable to Spirit Damage when out of range (rather than only immune to bullet damage)
- Spellslinger Headshots: Amp per headshot increased from 4% to 6%
- Spellslinger Headshots: Max Stacks reduced from 12 to 10

**2024-12-21** ([forum post](https://forums.playdeadlock.com/threads/12-21-2024-update.52206/))

- Spellslinger Headshots: Cooldown is now on a per target basis rather than on the item itself (this is a buff/flexibility improvement)
- Spellslinger Headshots: Spirit Amp per headshot increased from 3% to 4%
- Spellslinger Headshots: Fixed the base Spirit Amp requiring a headshot (this fix was released recently)

**2024-12-06** ([forum post](https://forums.playdeadlock.com/threads/12-06-2024-update.50599/))

- Tweaked falloff range and toned down bass frequencies of hotel music
- Ability Range stat now has diminishing stacking
- Ability Duration stat now has diminishing stacking
- Basic Magazine: Weapon Damage reduced from 15% to 12%
- High-Velocity Mag: Weapon Damage reduced from 13% to 11%
- Hollow Point Ward: Weapon Damage reduced from 22% to 20%
- Spellslinger Headshots: Proc bonus changed from 3% Spirit Power to 3% Spirit Amp
- Withering Whip: Bullet Resist reduced from -11% to -12%

**2024-11-21_HeroLab**

- Weapon: Bullet damage per boon reduced from 0.57 to 0.35

**2024-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2024-update.47476/))

- Walkers now provide nearby allied heroes 25% Bullet and Spirit Resistance
- Walkers now have Resistance based on how many nearby enemies there are (0/8/16/24/32/40% for 1/2/3/4/5/6 players; they are more tanky against a large attacking team)
- Trooper Spirit Resist at 25 minutes reduced from 30% to 20% (still scales to 70% at 50 minutes)
- Falloff min range reduced from 22m to 20m
- Changed entrance to the Armory/Warehouse from the inner lane to be more direct (not a hallway)
- View attachment armory_update.mp4
- New T3 Weapon Item, Spellslinger Headshots: Requires Soul Shredder Bullets. Landing a headshot on enemy heroes increases your total Spirit Power by 3% for 12s. Cooldown 1.5s. Max stacks 12. Grants +12% Weapon Damage, +8% Spirit Amp/18% Spirit Lifesteal (component passive), and +150 Health.
- New T3 Spirit Item, Spirit Snatch: Requires Spirit Strike. Causes your melee attacks to steal 12% Spirit Resist and 26 Spirit Power for 16s. Cooldown 6s. Buff you receive stacks if you hit different heroes. Grants +15% Melee Damage, +8% Spirit Resist,  +125 Health  and +1 Sprint. (Thanks to https://forums.playdeadlock.com/threads/spirt-snatch-3k-soul-spirit-strike-upgrade.46932/ )
- New T3 Spirit Item, Arcane Surge: Requires Kinetic Dash. After successful Dash Jump, the next ability you use will also have +20% Range, +20% Duration and +20 Spirit Power. Grants +100 Health, +1 Stamina and +15% Slow Resist.

**2024-11-13** ([forum post](https://forums.playdeadlock.com/threads/11-13-2024-update.46391/))

- Guardian resistance changed from -35% at 8 minutes to -50% at 10 minutes

**2024-11-07_HeroLab**

- Gun: Reduce Bullet Damage from 25 to 21

**2024-11-07** ([forum post](https://forums.playdeadlock.com/threads/11-07-2024-update.44786/))

- Walker armor loss over time now happens at 16m instead of 14m
- Troopers Spirit resist goes to 30% instead of 40% at 25 minutes
- Fixed Troopers resistance against Base Guardians not working properly
- Debuff Remover: Debuff Resistance increased from 35% to 40%
- Withering Whip: Bullet Resist reduction reduced from -14% to -11%
- Withering Whip: Now deals 50 Spirit Damage

**2024-11-01_HeroLab**

- Shotgun falloff start reduced from 18m to 16m

**2024-10-29_HeroLab**

- Gun: Increased AltFire Bullet Damage from 6 to 7
- Slither: Change T1 upgrade to be +25% Slide distance, T2 to be +2 Stamina, and T3 to be +30% Bullet/Spirit Resistance.

**2024-10-24** ([forum post](https://forums.playdeadlock.com/threads/10-24-2024-update.40951/))

- Added Melee Resistance to Vitality stat screen
- Guardian resist vs troopers changed from starting at 70% and ending at -30% at 10 min to starting at 60% and ending at -35% at 8 minutes
- Guardians now have resist vs players starting at 40% and ending at -35% at 8 minutes
- Walkers now have resist vs troopers starting at 60% and ending at -30% at 14 minutes
- Walkers now have resist vs players starting at 60% and ending at -30% at 14 minutes
- Troopers now gain +40% Spirit Resist gradually over 25 minutes, goes to 70% at 50 minutes
- High-Velocity Mag: Weapon damage increased from 12% to 13%
- Mystic Reach: Bullet Resist increased from 6% to 7%
- Improved Reach: Bullet Resist increased from 12% to 13%

**2024-10-10** ([forum post](https://forums.playdeadlock.com/threads/10-10-2024-update.36958/))

- Added Crit Bonus Scale tooltip to the Weapon stats in the shop
- Golden Statues now have a tier 3 upgrade at 25 minutes (+2.5% Fire Rate, +8% Ammo, 1.5% CD Reduction, +7% Weapon Damage, 40 Health, +5 Spirit Power)
- Bullet and Spirit Lifesteal now stack diminishingly
- Combat Barrier: Weapon Damage reduced from 25% to 22%

**2024-09-26** ([forum post](https://forums.playdeadlock.com/threads/09-26-2024-update.33015/))

- Fixed Magic Reverb not getting increased bonus damage from damage amps
- Fixed min/max falloff range displaying incorrectly on Weapon Stats Tooltip
- Timing critical music and sfx will pause and resume in response to game pause
- Fire Rate slows now stack diminishingly
- Added indicator on the hud to help track your passive cooldown items when they are 1s from ready (headshot Booster, Medic Bullets, etc)
- Combat Barrier: Weapon Damage while shielded reduced from 28% to 25%
- Health Nova: Weapon Damage increased from 10% to 12%
- Improved Bullet Armor: Bullet Resist increased from 45% to 50%
- Mystic Reach: Now provides 6% Bullet Resist instead of 6% Spirit Resist
- Improved Reach: Now provides 12% Bullet Resist instead of 12% Spirit Resist

**2024-09-12** ([forum post](https://forums.playdeadlock.com/threads/09-12-2024-update.27974/))

- Updated effects for the Warp Stone bullet resist buff
- High-Velocity Mag: Weapon Damage reduced from 14% to 12%
- Hollow Point Round: Conditional Weapon Damage increased from 20% to 22%
- Soul Shredder Bullets: Weapon Damage increased from 6% to 7%
- Mystic Reach: Spirit Resist increased from 5% to 6%
- Changed collision on the shelves inside the Armory and Warehouse to improve shooting through them

**2024-08-29** ([forum post](https://forums.playdeadlock.com/threads/08-29-2024-update.22253/))

- Added Heal Amp and Debuff Resist to the Vitality stats in the shop
- Fixed parts of Shiv's coat being considered a headshot
- Fixed Zipline speed from Base Guardian killing and Zip booster ability not stacking properly
- Increased charged melee volume and falloff for victims
- Added new T3 Weapon Item, Headhunter: Requires High-Velocity Mag. Grants +50% Bullet Velocity, +15% Weapon Damage and +150 Bullet Shield. Passive cooldown: Landing a headshot on heroes deals bonus +140 Damage, heals you for +8% Max HP and grants +2 m/s for 3 seconds. Cooldown: 6 seconds.
- Improved Reach: Spirit Resist increased from +10% to +12%

**2024-08-22** ([forum post](https://forums.playdeadlock.com/threads/08-22-2024-update.19716/))

- Silence Glyph: Spirit damage scaling reduced from 1.5 to 1.0
- Dying with Siphon Bullets stacks will now cause you to lose 2 stacks no matter who killed you (rather than returning 1 only if the victim killed you back)
- Fixed Siphon Bullets acting as spirit damage for procs

**2024-08-15** ([forum post](https://forums.playdeadlock.com/threads/08-15-2024-update.16378/))

- Soul Shredder Bullets: Now grants +6% Weapon Damage
- Combat Barrier: Weapon Damage While Shielded increased from +24% to +28%
- Debuff Remover: Debuff resistance reduced from +40% to +35%
- Mystic Reach: Now gives +5% Spirit Resist
- Improved Burst: Reduced Weapon Damage from +12% to +8%
- Improved Reach: Now gives +10% Spirit Resist
- Silence Glyph: No longer reduces Spirit Resist
- Added a new T1 Weapon item. Grants +35% Bullet Projectile Speed, +14% Weapon Damage and +50 Bullet Shield.

**2024-08-01** ([forum post](https://forums.playdeadlock.com/threads/08-01-2024-update.13369/))

- Bullet damage falloff now maxes out at ~60m instead of ~65m
- Added a new T3 Weapon Item, Pristine Emblem: Gives +25% Weapon Damage, +12 Spirit Power, and +12% Spirit Armor. When an enemy is above 50% HP, you deal an additional +25% Weapon Damage.

**2024-07-18** ([forum post](https://forums.playdeadlock.com/threads/07-18-2024-update.11831/))

- Updated bullet resist debuff effects
- Cooldown reduction now stacks diminishingly
- Soul Rebirth (new T4 Vitality item): After you die, you will respawn in 4 seconds where you died with 40% of your Max Health. Cooldown: 220s. Also innately grants +20% Weapon Damage and +10% Cooldown Reduction.
- Silence Glyph: Now reduces Spirit Resist instead of providing Spirit Amplification

**2024-07-11** ([forum post](https://forums.playdeadlock.com/threads/07-11-2024-update.10871/))

- Golden Statues Weapon Damage bonus increased from 2% to 3% (level 2 from 3% to 4%)
- Bullet falloff damage now starts at 22m instead of 25m
- Base Guardian and Shrines bullet resist per nearby hero increased from 40/20/0/0% (for 0/1/2/3 people) to 60/40/20/0%
- Health Nova: Now grants +10% weapon damage
- Debuff Remover: T3 Vitality Item that upgrades from Debuff Reducer. Removes debuffs fully on cast again. Grants +3 m/s for 3s if any debuff is removed. Grants +40% debuff resist, +125 health, +20% weapon damage. Cooldown: 45

**2024-07-04** ([forum post](https://forums.playdeadlock.com/threads/07-04-2024-update.9652/))

- Base Guardians and Shrines now have +40% Bullet Resistance. They lose 20% for each enemy hero nearby (down to a minimum of 0% bullet resistance). When they haven't taken damage for 60 seconds, they regenerate 4% max hp per second.
- Weapon Damage: +2% to +3%
- Bullet falloff damage now starts at 25m instead of 27m
- Improved Burst: Now grants +12% Weapon Damage
- Escalating Exposure now has a base of -12% Spirit Resist reduction

**2024-06-27** ([forum post](https://forums.playdeadlock.com/threads/06-27-2024-update.8486/))

- Updated headshot hit indicator
- Fixed a recent bug with Metal Skin that caused you to do zero bullet damage
- Golden Statues no longer drop powerups (time duration buffs). Instead they now drop small permanent bonuses. These stack and do not decay with time or death. Drop rates rebalanced.
- +2% Weapon Damage

**2024-06-20** ([forum post](https://forums.playdeadlock.com/threads/06-20-2024-update.7003/))

- Fixed various bugs with Headshot Booster and Sharpshooter
- +8% Spirit Resist
- +8% Weapon Damage
- +8% Weapon Damage
- +20% Weapon Damage
- Active: Gain 40% Bullet and Spirit Resist and apply 20% movement slow to enemies within 10m. Your model size grows by 10%. Lasts 7 seconds. Cooldown: 65s

**2024-06-13** ([forum post](https://forums.playdeadlock.com/threads/06-13-2024-update.5773/))

- Added overhead number counter effect for opponents to see the stacks of Berserker

**2024-06-06** ([forum post](https://forums.playdeadlock.com/threads/06-06-2024-update.4096/))

- Changed collision on barrel stand stacks to block bullets
- Bullet damage falloff now maxes out at ~65m instead of ~70m
- Bullet Shields now block damage from melee (similar to resistance)

**2024-05-30** ([forum post](https://forums.playdeadlock.com/threads/05-30-2024-update.2514/))

- Basic Magazine: Weapon Damage reduced from +16% to +15%

**2024-05-24** ([forum post](https://forums.playdeadlock.com/threads/05-24-2024-update.1359/))

- Withering Whip: Bullet Resist Reduction reduced from -20% to -14%

**2024-05-23** ([forum post](https://forums.playdeadlock.com/threads/05-23-2024-update.1245/))

- Removed stack of cardboard boxes inside connection hallway near bases to prevent cover from Neutrals
- Spirit scaling reduced by ~15% (the total effective Spirit damage is reduced by less than this, this is just the Spirit multiplier scaling portion and has largest impact on late game burst)
- Strong Neutrals Spirit Resist increased from 25% to 35%
- Medium Neutrals Spirit Resist increased from 25% to 30%
- Withering Whip: Bullet Resist reduced from 25% to 20%
- Combat Barrier: Weapon Damage while Shielded from 20% to 24%

**2024-05-16** ([forum post](https://forums.playdeadlock.com/threads/05-16-2024-update.902/))

- Neutrals now have 20% Spirit Resist
- Spirit scaling reduced by ~19% (the total effective Spirit damage is reduced by less than this, this is just the Spirit multiplier scaling portion and has largest impact on late game burst)
- Silence Glyph: Now applies 8% Spirit Amp instead of -15% Bullet Resist
- Withering Whip: Now applies -25% Bullet Resist instead of 25% Spirit Amp

**2024-05-13** ([forum post](https://forums.playdeadlock.com/threads/05-13-2024-update.807/))

- Fixed Restorative Locket Spirit Resist not working

**2024-05-10** ([forum post](https://forums.playdeadlock.com/threads/05-10-2024-update.689/))

- We fixed a bug when combining shields and resistance that caused you to take too much damage. Previously there was a bug where if you take a high amount of damage, the remaining damage after shield reduction would pass through as pure damage instead of being reduced by resist. An example of this is someone dealing 800 spirit damage to you and you having 80 Spirit Shield and 45% Spirit Resistance. With the bug, the 800 would be reduced to 720 from the shield, and then you would lose 720 health. With the fix, the shield now reduces the damage to 720 as usual, but the remaining amount then gets reduced by 45% to 396 health lost instead of 720.​
