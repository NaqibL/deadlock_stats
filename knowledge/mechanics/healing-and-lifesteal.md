# Healing, regen, lifesteal and heal reduction

Generated from the game files at build 6868 and Valve's patch notes. Everything below is quoted from a source, not interpreted. Patch notes describe the game as of their date: read newest first, and treat an older line as history once a newer one changes the same thing.

## What the game itself says

- Ability Lifesteal Duration (`AbilityLifestealDuration_label`)
- Ability Lifesteal Duration (`AbilityLifestealDuration_postvalue_label`)
- Spirit Lifesteal (`AbilityLifestealPercentHeroPassive_label`)
- Spirit Lifesteal (`AbilityLifestealPercentHeroPassive_postvalue_label`)
- Spirit Lifesteal (`AbilityLifestealPercentHero_label`)
- Spirit Lifesteal (`AbilityLifestealPercentHero_postvalue_label`)
- Spirit Lifesteal on Non Heroes (`AbilityLifestealPercentNonHero_label`)
- Spirit Lifesteal on Non Heroes (`AbilityLifestealPercentNonHero_postvalue_label`)
- Spirit Lifesteal (`AbilityLifestealPercent_label`)
- Spirit Lifesteal (`AbilityLifestealPercent_postvalue_label`)
- above health threshold (`AboveHealthThreshold_conditional`)
- Bullet Lifesteal (`ActiveBonusLifesteal_label`)
- Bullet Lifesteal (`ActiveBonusLifesteal_postvalue_label`)
- Active Shield Health (`ActiveBulletShieldHealth_label`)
- Bullet Shield Health (`ActiveBulletShieldMaxHealth_label`)
- Bullet Shield Health (`ActiveBulletShieldMaxHealth_postvalue_label`)
- Health Steal (`ActiveHealthChange_label`)
- Health Regen (`ActiveHealthRegenBoost_label`)
- Health Regen (`ActiveHealthRegenBoost_postvalue_label`)
- Health Regen (`ActiveHealthRegen_label`)
- Health Regen (`ActiveHealthRegen_postvalue_label`)
- Bullet Shield Health (`ActiveMODIFIER_VALUE_BULLET_SHIELD_HEALTH_MAX_label`)
- Bullet Shield Health (`ActiveMODIFIER_VALUE_BULLET_SHIELD_HEALTH_MAX_postvalue_label`)
- Health Threshold to Auto-Cast (`AutoActivateHealthThreshold_postvalue_label`)
- Heal Per Headshot (`BaseHealOnHeadshot_label`)
- Heal Per Headshot (`BaseHealOnHeadshot_postvalue_label`)
- below health threshold (`BelowHealthThreshold_conditional`)
- Bonus Current Health as Damage (`BonusCurrentHealthDamagePercentage_label`)
- Bonus Current Health as Damage (`BonusCurrentHealthDamagePercentage_postvalue_label`)
- Bonus Max Health Per Kill (`BonusHealthOnKill_label`)
- Bonus Max Health Per Kill (`BonusHealthOnKill_postvalue_label`)
- Health Regen Out of Combat (`BonusHealthRegenOutOfCombat_label`)
- Health Regen (`BonusHealthRegen_label`)
- Health Regen (`BonusHealthRegen_postvalue_label`)
- Bonus Health (`BonusHealth_label`)
- Bonus Health (`BonusHealth_postvalue_label`)
- Max Health Regen (`BonusRegenMaxHealthPercent_label`)
- Max Health Regen (`BonusRegenMaxHealthPercent_postvalue_label`)
- Spirit Lifesteal (`BonusSpiritLifesteal_label`)
- Spirit Lifesteal (`BonusSpiritLifesteal_postvalue_label`)
- Bullet Lifesteal (`BulletLifestealPercentHero_label`)
- Bullet Lifesteal (`BulletLifestealPercentHero_postvalue_label`)
- Bullet Lifesteal (`BulletLifestealPercent_label`)
- Bullet Lifesteal (`BulletLifestealPercent_postvalue_label`)
- Bullet Shield Health (`BulletShieldHealth_label`)
- Bullet Shield Health (`BulletShieldHealth_postvalue_label`)
- Max Health Bullet Shield (`BulletShieldMaxHealthPercentage_label`)
- Max Health Bullet Shield (`BulletShieldMaxHealthPercentage_postvalue_label`)
- Bullet Shield Health (`BulletShieldMaxHealth_label`)
- Bullet Shield Health (`BulletShieldMaxHealth_postvalue_label`)
- Missing Health Bullet Shield (`BulletShieldMissingHealthPercentage_label`)
- Missing Health Bullet Shield (`BulletShieldMissingHealthPercentage_postvalue_label`)
- Anti-Healing (`CitadelComponentGroup_EAntiHealing`)
- Lifestealing (`CitadelComponentGroup_ELifesteal`)
- Health Changes (`Citadel_CombatLog_HealthDeltas`)
- Healing by Type (`Citadel_GraphType_HealingType`)
- Regen by Type (`Citadel_GraphType_RegenBreakdown`)
- Healer Sketches (`Citadel_Graph_PermanentBuff_ArtistHealer`)
- Bonus Health (`Citadel_Graph_PermanentBuff_BonusHealth`)
- Total Bonus to your Base Health gained from buying items in the Vitality tree (`Citadel_Hero_Stats_Tooltip_HealthMult`)
- Healing Needles (`Citadel_Hud_HealingMode`)
- Health Critical (`Citadel_Hud_HealthCritical`)
- Health Warning (`Citadel_Hud_HealthWarning`)
- Most Healing (`Citadel_PostGame_AwardHealing`)
- Second Most Healing (`Citadel_PostGame_AwardHealing_Rank2`)
- Third Most Healing (`Citadel_PostGame_AwardHealing_Rank3`)
- Most Healing (`Citadel_Post_Game_MostHealing`)
- Assistant Health (`CloneHealth_label`)
- Assistant Health (`CloneHealth_postvalue_label`)
- Health Regen in Combat (`CombatRegenPercent_label`)
- Consume Heal Percentage (`ConsumeHealPercentage_label`)
- Consume Heal Percentage (`ConsumeHealPercentage_postvalue_label`)
- Trooper Health (`ConvertedHealth_label`)
- Current Health as Damage (`CurrentHealthDamagePercentage_label`)
- Current Health as Damage (`CurrentHealthDamagePercentage_postvalue_label`)
- Current Health Damage (`CurrentHealthDamage_label`)
- Current Health Damage (`CurrentHealthDamage_postvalue_label`)
- Current Health (`CurrentHealthPercentDamage_label`)
- Current Health (`CurrentHealthPercentDamage_postvalue_label`)
- Current Health (`CurrentHealthPercent_label`)
- Current Health (`CurrentHealthPercent_postvalue_label`)
- Max Health as Damage (`DPSPercentHealth_label`)
- Max Health as Damage (`DPSPercentHealth_postvalue_label`)
- Damage to Heal (`DamageHealMultNonHero_label`)
- Damage to Heal (`DamageHealMultNonHero_postvalue_label`)
- Hero Damage to Heal (`DamageHealMult_label`)
- Hero Damage to Heal (`DamageHealMult_postvalue_label`)
- Damage/Heal Per Target (`DamageHealPerTarget_label`)
- Damage/Heal Per Target (`DamageHealPerTarget_postvalue_label`)
- Max Health as Damage (`DamagePercentHealth_label`)
- Max Health as Damage (`DamagePercentHealth_postvalue_label`)
- Max Health Damage (`DealMaxHealthDamagePct_postvalue_label`)
- Health Per Kill (`DeathTaxHeal_label`)
- Deployable Health (`DeployHealthRegen_label`)
- Dispenser Health (`DispenserHealth_label`)
- Bleed Damage (`DotHealthPercent_label`)
- Bleed Damage (`DotHealthPercent_postvalue_label`)
- Health Regen (`DroneHealthRegen_label`)
- Health Regen (`DroneHealthRegen_postvalue_label`)
- Drone Health (`DroneHealth_label`)
- Anti-Healing (`EShopFilterAntiHeal`)
- Out of Combat Regen (`EShopFilterOutOfCombatRegen`)
- Enemy above health threshold (`EnemyAboveHealthThreshold_conditional`)
- Enemy health threshold (`EnemyHealthPercent_label`)
- Enemy Health Threshold (`EnemyHealthPercent_postvalue_label`)
- Enemy Min Health (`EnemyMinHealthPct_label`)
- Enemy Min Health (`EnemyMinHealthPct_postvalue_label`)
- Health Regen (`ExternalBonusHealthRegen_label`)
- Health Regen (`ExternalBonusHealthRegen_postvalue_label`)
- Healing Amount (`FlatHealthHealing_label`)
- Healing Amount (`FlatHealthHealing_postvalue_label`)
- Current Health Damage (`FullRageCurrentHealthDamagePct_label`)
- Current Health Damage (`FullRageCurrentHealthDamagePct_postvalue_label`)
- Ghoul Health (`GhoulHealth_label`)
- Ghoul Health (`GhoulHealth_postvalue_label`)
- Gravestone Health (`GravestoneHealth_label`)
- Gravestone Health (`GravestoneHealth_postvalue_label`)
- Deadhead Health (`HauntingSkullHealth_postvalue_label`)
- Headshot Heal Bonus (`HeadshotHealBonusPercent_label`)
- Headshot Heal Bonus (`HeadshotHealBonusPercent_postvalue_label`)
- Outgoing Healing (`HealAmpCastPercent_label`)
- Outgoing Healing (`HealAmpCastPercent_postvalue_label`)
- Incoming Healing (`HealAmpReceivePenaltyPercent_label`)
- Incoming Healing (`HealAmpReceivePenaltyPercent_postvalue_label`)
- Healing Received Boost (`HealAmpReceivePercent_label`)
- Healing Received Boost (`HealAmpReceivePercent_postvalue_label`)
- Health Regen Multiplier (`HealAmpRegenMultiplierOutOfCombat_label`)
- Incoming Healing (`HealAmpRegenPenaltyPercent_label`)
- Incoming Healing (`HealAmpRegenPenaltyPercent_postvalue_label`)
- Health Regen Boost (`HealAmpRegenPercent_label`)
- Heal Cooldown (`HealCooldown_postvalue_label`)
- Heal on hero hit (`HealFixedHealth_label`)
- Heal on hero hit (`HealFixedHealth_postvalue_label`)
- Friendly Heal Radius (`HealFriendRadius_label`)
- Friendly Heal Radius (`HealFriendRadius_postvalue_label`)
- Healing From Heroes (`HealFromHero_label`)
- Healing From Heroes (`HealFromHero_postvalue_label`)
- Healing From NPCs / Orbs (`HealFromNPC_label`)
- Healing From NPCs / Orbs (`HealFromNPC_postvalue_label`)
- Heal Interval (`HealInterval_label`)
- Heal Interval (`HealInterval_postvalue_label`)
- Max Health Regen (`HealLifePercentOutOfCombat_label`)
- Max Health Regen (`HealLifePercentOutOfCombat_postvalue_label`)
- Max Health Heal / Shot (`HealMaxHealthPercentPerShot_label`)
- Max Health Heal / Shot (`HealMaxHealthPercentPerShot_postvalue_label`)
- Max Health Restored (`HealMaxHealthPercent_label`)
- Max Health Restored (`HealMaxHealthPercent_postvalue_label`)
- Heal on hero hit (`HealMaxHealth_label`)
- % of Max Health (`HealMaxHealth_postfix`)
- Heal on hero hit (`HealMaxHealth_postvalue_label`)
- Missing Health as Healing (`HealOnKillPct_label`)
- Missing Health as Healing (`HealOnKillPct_postvalue_label`)
- Heal On Hero Kill (`HealOnKill_label`)
- Heal On Hero Kill (`HealOnKill_postvalue_label`)
- Heal vs heroes (`HealPctVsHeroes_label`)
- Heal vs heroes (`HealPctVsHeroes_postvalue_label`)
- Heal vs non-heroes (`HealPctVsNonHeroes_label`)
- Heal vs non-heroes (`HealPctVsNonHeroes_postvalue_label`)
- Heal Increase Per Minute (`HealPerMinute_label`)
- Heal On Pickup (`HealPerPickup_label`)
- Heal On Pickup (`HealPerPickup_postvalue_label`)
- Healing / Stack (`HealPerSecondPerStack_label`)
- Healing / Stack (`HealPerSecondPerStack_postvalue_label`)
- Heal Per Second (`HealPerSecond_label`)
- Heal Per Second (`HealPerSecond_postvalue_label`)
- Heal Per Stack (`HealPerStack_label`)
- Heal Per Stack (`HealPerStack_postvalue_label`)
- Heal Per Headshot (`HealPercentPerHeadshot_label`)
- Heal Per Headshot (`HealPercentPerHeadshot_postvalue_label`)
- Heal Reduction Duration (`HealReductionDuration_label`)
- Heal Reduction Duration (`HealReductionDuration_postvalue_label`)
- Heal Per Shot (`HealRegen_label`)
- Heal Per Shot (`HealRegen_postvalue_label`)
- Incoming Healing (`HealingEffectivenessPercent_label`)
- Incoming Healing (`HealingEffectivenessPercent_postvalue_label`)
- Healing Effectiveness (`HealingEffectiveness_label`)
- Healing Effectiveness (`HealingEffectiveness_postvalue_label`)
- Buff Duration (`HealingNeedlesAmpDuration_label`)
- Buff Duration (`HealingNeedlesAmpDuration_postvalue_label`)
- Healing on Ability Cast (`HealingPerCast_Label`)
- Healing on Ability Cast (`HealingPerCast_postvalue_label`)
- Health Restored (`HealingPerSecond_label`)
- Health Restored (`HealingPerSecond_postvalue_label`)
- Heal Percent (`HealingPercent_label`)
- Heal Percent (`HealingPercent_postvalue_label`)
- %s1 to any health and health regen bonuses (`HealthAttribute_Desc`)
- no additional health and health regen bonuses (`HealthAttribute_Desc_0`)
- Health Boost Duration (`HealthBoostDuration_postvalue_label`)
- Health Drain (`HealthDrainedPerSecond_label`)
- Health Drain (`HealthDrainedPerSecond_postvalue_label`)
- Current Health Damage (`HealthPctDamage_label`)
- Current Health Damage (`HealthPctDamage_postvalue_label`)
- Health Percent (`HealthPercent_label`)
- Health Percent (`HealthPercent_postvalue_label`)
- Regen Duration (`HealthRegenDuration_label`)
- Regen Duration (`HealthRegenDuration_postvalue_label`)
- Health Regen (`HealthRegenPerTrooper_label`)
- per nearby trooper (`HealthRegenPerTrooper_postfix`)
- Health Regen (`HealthRegenPerTrooper_postvalue_label`)
- Health Regen (`HealthRegen_label`)
- Health Regen (`HealthRegen_postvalue_label`)
- Hero Lifesteal (`HealthStealPctHero_label`)
- Hero Lifesteal (`HealthStealPctHero_postvalue_label`)
- Non-Hero Lifesteal (`HealthStealPct_label`)
- Non-Hero Lifesteal (`HealthStealPct_postvalue_label`)
- Max HP Steal Per Bullet (`HealthSteal_label`)
- Max HP Steal Per Bullet (`HealthSteal_postvalue_label`)
- Buff Duration (`HealthSwapBuffDuration_label`)
- Buff Duration (`HealthSwapBuffDuration_postvalue_label`)
- Health Threshold for Blood Trail (`HungerLowHealthThreshold_label`)
- Health Threshold for Blood Trail (`HungerLowHealthThreshold_postvalue_label`)
- Imbued Lifesteal (`ImbueAbilityLifesteal_label`)
- Imbued Lifesteal (`ImbueAbilityLifesteal_postvalue_label`)
- Heal Interval (`InfestHealInterval_postvalue_label`)
- Trooper Heal (`InfestHeal_label`)
- Max HP Heal On Cast (`InfinitySlashHealOnCast_label`)
- Max HP Heal On Cast (`InfinitySlashHealOnCast_postvalue_label`)
- Max HP Heal On Kill (`InfinitySlashHealOnKill_label`)
- Max HP Heal On Kill (`InfinitySlashHealOnKill_postvalue_label`)
- regeneration (`InlineAttribute_Regen`)
- stamina recovery (`InlineAttribute_StaminaRegenPerSecond`)
- Invis Max Health Regen (`InvisRegen_Label`)
- Max HP Heal On Kill (`LeechHealOnKill_label`)
- Max HP Heal On Kill (`LeechHealOnKill_postvalue_label`)
- Damage to Heal (`LifeDrainHealthMult_label`)
- Damage to Heal (`LifeDrainHealthMult_postvalue_label`)
- Lifesteal Duration (`LifestealDuration_label`)
- Lifesteal Duration (`LifestealDuration_postvalue_label`)
- Melee Hit Heal (`LifestealHealPercent_label`)
- Melee Hit Heal (`LifestealHealPercent_postvalue_label`)
- Heal on Melee Hit (`LifestealHeal_label`)
- Heal on Melee Hit (`LifestealHeal_postvalue_label`)
- Lifesteal on Non Heroes (`LifestealPercentNonHero_label`)
- Lifesteal on Non Heroes (`LifestealPercentNonHero_postvalue_label`)
- Heal on Melee Hit (`LifestrikeHeal_label`)
- Heal on Melee Hit (`LifestrikeHeal_postvalue_label`)
- Max Bonus Damage (`LowHealthEnemyDamageBonus_label`)
- Max Bonus Damage (`LowHealthEnemyDamageBonus_postvalue_label`)
- Low Health Threshold (`LowHealthEnemyThresholdPct_label`)
- Low Health Threshold (`LowHealthEnemyThresholdPct_postvalue_label`)
- Spirit Resist (`LowHealthTechResist_label`)
- Spirit Resist (`LowHealthTechResist_postvalue_label`)
- Health Threshold (`LowHealthThreshold_label`)
- Health Threshold (`LowHealthThreshold_postvalue_label`)
- Health Percentage for Max Damage (`MaxDamageHealthPercentage_label`)
- Health Percentage for Max Damage (`MaxDamageHealthPercentage_postvalue_label`)
- Max Leech Damage As Healing (`MaxHealPercentOfLeechDamage_label`)
- Max Leech Damage As Healing (`MaxHealPercentOfLeechDamage_postvalue_label`)
- Max Health Damage (`MaxHealthDamage_label`)
- Max Health Damage (`MaxHealthDamage_postvalue_label`)
- Melee Bonus Health (`MaxHealthMelee_label`)
- Melee Bonus Health (`MaxHealthMelee_postvalue_label`)
- Max Health as Barrier (`MaxHealthPct_label`)
- Max Health as Barrier (`MaxHealthPct_postvalue_label`)
- Max Health per second (`MaxHealthPercentAsDPS_label`)
- Max Health per second (`MaxHealthPercentAsDPS_postvalue_label`)
- Max Health Regen (`MaxHealthRegenPct_label`)
- Max Health Regen (`MaxHealthRegenPct_postvalue_label`)
- Max Health Heal (`MaxHealthRegen_label`)
- Max Health Heal (`MaxHealthRegen_postvalue_label`)
- % Max Health (`MaxHealthSelfDamagePercent_postfix`)
- Melee Lifesteal (`MeleeLifestealPercent_label`)
- Melee Lifesteal (`MeleeLifestealPercent_postvalue_label`)
- Melee Lifesteal (`MeleeLifesteal_label`)
- Melee Lifesteal (`MeleeLifesteal_postvalue_label`)
- Low Health Threshold (`MinHealthFractionToTrack_postvalue_label`)
- Min Health Received (`MinHealthTakenPct_label`)
- Min Health Received (`MinHealthTakenPct_postvalue_label`)
- Extra Health given to units (`MindControlHealthBonus_label`)
- Health Steal Per Sec (`MirageFireScarabsHealthSteal_label`)
- Health Steal Per Sec (`MirageFireScarabsHealthSteal_postvalue_label`)
- Missing HP Heal (`MissingHPHeal_label`)
- Missing HP Heal (`MissingHPHeal_postvalue_label`)
- Missing Health Burst (`MissingHealthBurstPct_label`)
- Missing Health Burst (`MissingHealthBurstPct_postvalue_label`)
- Missing Health as Damage (`MissingHealthDamagePercentage_postvalue_label`)
- Missing Health Heal (`MissingHealthHealPct_postvalue_label`)
- Missing Health as Healing (`MissingHealthPercentHeal_label`)
- Missing Health as Healing (`MissingHealthPercentHeal_postvalue_label`)
- Mobile Resupply Regen Multiplier (`MobileResupplyRegenMultiplier_label`)
- Lifesteal vs Non-Heroes (`NonHeroHealingFactor_label`)
- Lifesteal vs Non-Heroes (`NonHeroHealingFactor_postvalue_label`)
- Max Health Regen (`NotSeenByEnemiesRegen_label`)
- Max Health Regen (`NotSeenByEnemiesRegen_postvalue_label`)
- Out of Combat Regen (`OutOfCombatHealthRegen_label`)
- Out of Combat Regen (`OutOfCombatHealthRegen_postvalue_label`)
- Barrier Duration (`OverhealBarrierDuration_label`)
- Barrier Duration (`OverhealBarrierDuration_postvalue_label`)
- Ichor per Leech (`PainRegenPerLeech_label`)
- Ichor per Leech (`PainRegenPerLeech_postvalue_label`)
- Damage Parried as Heal (`ParrySuccessHealPercentage_label`)
- Damage Parried as Heal (`ParrySuccessHealPercentage_postvalue_label`)
- Health Healed (`PercentHealthHealing_label`)
- Health Healed (`PercentHealthHealing_postvalue_label`)
- Health Threshold (`ProcHealth_label`)
- Health Threshold (`ProcHealth_postvalue_label`)
- Heal Per Kill (`RakeHealPerKill_label`)
- Heal Per Kill (`RakeHealPerKill_postvalue_label`)
- Regen Duration (`RegenDuration_label`)
- Regen Duration (`RegenDuration_postvalue_label`)
- Regeneration Time (`RegenIncomingDamageDuration_label`)
- Regeneration Time (`RegenIncomingDamageDuration_postvalue_label`)
- Damage Regenerated (`RegenIncomingDamagePercent_label`)
- Damage Regenerated (`RegenIncomingDamagePercent_postvalue_label`)
- Health Regen Per Leech (`RegenPerLeechPickup_label`)
- Health Regen Per Leech (`RegenPerLeechPickup_postvalue_label`)
- Health Regen while Invisible (`RegenWhileInvisible_label`)
- Health Regen while Invisible (`RegenWhileInvisible_postvalue_label`)
- Regeneration Duration (`RegenerationDuration_label`)
- Regeneration Duration (`RegenerationDuration_postvalue_label`)
- Restore Time (`RegenerationRate_label`)
- Regeneration (`Regeneration_label`)
- Regeneration (`Regeneration_postvalue_label`)
- Respawn Bonus Health Duration (`RespawnBonusHealthDuration_label`)
- Respawn Bonus Health (`RespawnBonusHealth_label`)
- Rebirth Health (`RespawnHealthPercent_label`)
- Rebirth Health (`RespawnHealthPercent_postvalue_label`)
- Shield Health (`ShieldHealth_label`)
- Shield Health (`ShieldHealth_postvalue_label`)
- Shot Regen Time (`ShotRegenTime_label`)
- Max HP Steal (`SiphonBullets_HealthStealPctHero_label`)
- Max HP Steal (`SiphonBullets_HealthStealPctHero_postvalue_label`)
- Stamina Heal (`StaminaHeal_label`)
- Stamina Heal (`StaminaHeal_postvalue_label`)
- Stamina Regen (`StaminaRegenPercent_label`)
- Stamina Regen (`StaminaRegenPercent_postvalue_label`)
- Health Regen (`StatDesc_BaseHealthRegen`)
- Health Regen (`StatDesc_BaseHealthRegen_postvalue_label`)
- Bullet Lifesteal (`StatDesc_BulletLifesteal`)
- Bullet Lifesteal (`StatDesc_BulletLifesteal_postvalue_label`)
- Damage Shield (`StatDesc_BulletShieldHealth`)
- Damage Shield (`StatDesc_BulletShieldHealth_postvalue_label`)
- Energy Regen Time (`StatDesc_EnergyRegenTime`)
- External Health Regen (`StatDesc_ExternalHealthRegen`)
- Incoming Healing - Percentage modification of healing received (`StatDesc_HealingAmpDesc`)
- Outgoing Healing - Percentage modification to the output of your healing abilities (`StatDesc_HealingBoostDesc`)
- Outgoing Healing (`StatDesc_HealingOutput`)
- Outgoing Healing (`StatDesc_HealingOutput_postvalue_label`)
- Health Per Level (`StatDesc_HealthPerLevel`)
- Health Regen (`StatDesc_HealthRegen`)
- Health Regen Per Level (`StatDesc_HealthRegenPerLevel`)
- Health Regen (`StatDesc_HealthRegen_postvalue_label`)
- Energy Regen Per Level (`StatDesc_ManaRegenPerLevel`)
- Non-Combat Regen (`StatDesc_OutOfCombatHealthRegen`)
- Non-Combat Regen (`StatDesc_OutOfCombatHealthRegen_postvalue_label`)
- Health Regen - Amount of health you regen per second (`StatDesc_RegenDesc`)
- Spirit Lifesteal - Amount of health you regain from dealing Spirit Damage (`StatDesc_SpiritLifestealDesc`)
- Lifesteal Effectiveness (`StatDesc_SpiritLifestealEffectiveness`)
- Lifesteal Effectiveness (`StatDesc_SpiritLifestealEffectiveness_postvalue_label`)
- Stamina Recovery (`StatDesc_StaminaRegenIncrease`)
- Stamina Recovery (`StatDesc_StaminaRegenIncrease_postvalue_label`)
- Stamina Recovery (`StatDesc_StaminaRegenPerSecond`)
- Stamina Recovery (`StatDesc_StaminaRegenPerSecond_postvalue_label`)
- Stamina Recovery (`StatDesc_StaminaRegenPercent`)
- Stamina Recovery (`StatDesc_StaminaRegenPercent_postvalue_label`)
- Spirit Lifesteal (`StatDesc_TechLifesteal`)
- Spirit Lifesteal on Non Heroes (`StatDesc_TechLifestealNonHero`)
- Spirit Lifesteal on Non Heroes (`StatDesc_TechLifestealNonHero_postvalue_label`)
- Spirit Lifesteal (`StatDesc_TechLifesteal_postvalue_label`)
- Spirit Shield (`StatDesc_TechShieldHealth`)
- Weapon Lifesteal - Amount of health you regain from dealing Weapon Damage (`StatDesc_WeaponLifestealDesc`)
- (Normalized) (`StatueHealth_label`)
- (Normalized) (`StatueHealth_postvalue_label`)
- Ava Recalled Regen (`StatueHeldRegen_label`)
- Ava Recalled Regen (`StatueHeldRegen_postvalue_label`)
- Lifesteal Non-Hero (`StatueLifestealNonHero_label`)
- Lifesteal Non-Hero (`StatueLifestealNonHero_postvalue_label`)
- to Gangster Health (`SummonCasterHealthPct_label`)
- % of The Boss' health (`SummonCasterHealthPct_postfix`)
- Gangster Health (`SummonCasterHealthPct_prefix`)
- Summon Health (`SummonHealth_label`)
- Summon Health (`SummonHealth_postvalue_label`)
- Lifesteal Duration (`TargetLifestealDuration_label`)
- Lifesteal Duration (`TargetLifestealDuration_postvalue_label`)
- Bullet & Spirit Lifesteal vs Target (`TargetLifesteal_label`)
- Lifesteal vs Target (`TargetLifesteal_postvalue_label`)
- Spirit Lifesteal (`TechLifestealPercent_label`)
- Spirit Lifesteal (`TechLifestealPercent_postvalue_label`)
- Spirit Shield Health (`TechShieldHealth_label`)
- Spirit Shield Health (`TechShieldHealth_postvalue_label`)
- Spirit Shield Health (`TechShieldMaxHealth_label`)
- Spirit Shield Health (`TechShieldMaxHealth_postvalue_label`)
- Temp Bullet Shield Health (`TempBulletShieldHealth_label`)
- Temp Spirit Shield Health (`TempTechShieldHealth_label`)
- Temporary Health (`TemporaryHealth_postvalue_label`)
- Tesla Coil Health (`TeslaCoilHealth_label`)
- Replicated Healing (`TetherSharedHealPct_label`)
- Replicated Healing (`TetherSharedHealPct_postvalue_label`)
- Bonus Health Regen (`TetheredBonusHealthRegen_label`)
- Total HP Regen (`TotalHealthRegen_label`)
- Total HP Regen (`TotalHealthRegen_postvalue_label`)
- Turret Health (`TurretBaseHealth_label`)
- Turret Health (`TurretBaseHealth_postvalue_label`)
- Turret Health (`TurretHealthScaling_label`)
- Turret Health (`TurretHealthScaling_postvalue_label`)
- Health for Max Damage (`VenomMaxDamageHealthPercentage_label`)
- Health for Max Damage (`VenomMaxDamageHealthPercentage_postvalue_label`)
- Missing Health Damage (`VenomMissingHealthDamagePercentage_label`)
- Missing Health Damage (`VenomMissingHealthDamagePercentage_postvalue_label`)
- Healer Sketch (`artist_drawing_healer`)
- Hero Base Regen (`base_stat_regen`)
- %s1 was healed for %s2. (`citadel_combat_log_healed`)
- %s1 was healed %s3x for %s2. (`citadel_combat_log_healed_n`)
- %s1 heals %s2 for %s3 health%s4. (`citadel_combat_log_heals`)
- %s1 heals %s2 %s5x for %s3 health%s4. (`citadel_combat_log_heals_n`)
- %s1's %s2 heals %s3 for %s4 health%s5. (`citadel_combat_log_minion_heals`)
- %s1's %s2 heals %s3 %s6x for %s4 health%s5. (`citadel_combat_log_minion_heals_n`)
- Health Regen (`fathom_lurkers_ambush/regen`)
- Reefdweller Harpoon Regen (`fathom_reefdweller_harpoon/regen`)
- Increased health regen (`health_regen_pickup/small_health_regen`)

## Current numbers in the game files

- No dedicated block for this in the files the sheet reads; see the sheet's tables.

## Patch history (214 lines, newest first)

**2026-08-12** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1840944183775204))

- Doorman: Similar to the Walker change above, the turrets in the healing area in base now also wait on considering valid targets

**2026-06-30** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1836506165563227))

- Rift Troopers spawn with 100% extra health and damage (they also look larger and have custom VFX). Their bonus health and damage grow slightly per event (first one is 100%, then 120%, 140%, etc)
- Health per boon reduced by 5%

**2026-06-11** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1835236783562074))

- Breakables health permanent bonus reduced from 15/25/35 to 15/20/30 for level 1/2/3

**2026-05-25** ([forum post](https://forums.playdeadlock.com/threads/05-22-2026-update.135477/post-259788))

- Urn runner now gains +2m Sprint, +1 Stamina, +10% Dash Distance and +15% Stamina Regen

**2026-05-22** ([forum post](https://forums.playdeadlock.com/threads/05-22-2026-update.135477/))

- Stamina Regeneration is reduced by 25% for 5s after using a Wall Jump. This does not trigger when out of combat or when mantling soon after.
- Medic trooper heal duration increased from 2s to 4s (same overall heal amount)
- When receiving multiple of the Medic trooper orb the duration will now be added ontop rather than stacking directly (so picking up 4 in a row will give the regen over 16s instead of over 4s, overall heal is the same just slower)
- Medic Trooper heal increased from 12% missing hp to 13%
- Fixed the following abilities taking you out of zoom temporarily when cast: Blasted, Gloom Bombs, Shining Wonder, Call Bell, Luggage Cart, Stalker's Mark, Rejuvenating Aurora, Charged Shot, Powder Keg, Bounce Pad, Spirit Lasso, Napalm, Ice Path, Flog, Spectral Wall, Rake, Fire Scarabs, Scorn, Sand Blast, Time Wall, Paradoxical Swap, Barrage, Flying Cloak, Pillow Toss, Lightning Ball, Entangling Bola, Go For The Throat, Vexing Bolt, Consecrating Grenade, Gut Shot, Snap Trap, Ira Domini, Pain Battery, Jumpstart, Flight, Crow Familiar, Lethal Venom, Petrifying Bola, Alchemical Flask, Card Trick, Capacitor, Restorative Locket, Healing Nova, Silence Wave, Magic Carpet, Refresher
- Fixed the following items and abilities not working through veils: Heroic Aura, Healing Rite, Healing Nova, Rescue Beam, Divine Barrier, Kudzu Connection, Cube, Tag Along, Lil Helpers, Guardian Ward, Scourge, Plot Armor
- Added a new T1 Vitality Item, Grit. Active grants you 200 Barrier for 4s duration. Innate grants 1 Out of Combat Regen. Cooldown: 60s. Upgrades to Weapon Shielding, Spirit Shielding, Reactive Barrier (these do not inherit the manual cast active) and Guardian Ward.
- Fixed the following Enhanced Items not maintaining their stats from components: Opening Rounds, Tankbuster, Kinetic Dash, Radiant Regeneration, Burst Fire, Veil Walker, Arcane Surge, Fury Trance, Leech

**2026-04-30** ([forum post](https://forums.playdeadlock.com/threads/04-30-2026-update.129989/))

- [ General ] - Base health per boon reduced by 7 - Vitality Investment bonus increased from 8/10/13/17/34/39/44/48/52/56% to 9/12/15/20/38/42/46/50/56/62% - Weapon Investments bonus rescaled from 7/9/13/20/49/60/80/95/115/135% to 9/12/15/18/46/55/70/85/100/115% - Reduced bullet damage growth by...

**2026-04-10** ([forum post](https://forums.playdeadlock.com/threads/04-10-2026-update.125825/))

- Medic Trooper missing health percent heal reduced from 16% to 14%
- Medic Trooper fixed regen growth per minute reduced from 4 to 3
- Medic Trooper missing health percent heal reduced from 16% to 14%
- Medic Trooper fixed regen growth per minute reduced from 4 to 3

**2026-03-21** ([forum post](https://forums.playdeadlock.com/threads/03-06-2026-update.114328/post-226950))

- Hero health growth increased by +3 and 4%
- Improved the following Enhanced Items: Blood Tribute, Shadow Weave, Cultist Sacrifice, Magic Carpet, Healing Rite, Majestic Leap, Metal Skin, Monster Rounds, Veil Walker, Fury Trance, Return Fire, Restorative Locket, Rebuttal, Disarming Hex, Split Shot, Rescue Beam, Spirit Sap, Cursed Relic, Heroic Aura, Rusted Barrel, Weapon Shielding, Nullification Burst|l1=Nullification Blast{{sic}}, Cloak of Opportunity
- Hero health growth increased by +3 and 4%
- Improved the following Enhanced Items: Blood Tribute, Shadow Weave, Cultist Sacrifice, Magic Carpet, Healing Rite, Majestic Leap, Metal Skin, Monster Rounds, Veil Walker, Fury Trance, Return Fire, Restorative Locket, Rebuttal, Disarming Hex, Split Shot, Rescue Beam, Spirit Sap, Cursed Relic, Heroic Aura, Rusted Barrel, Weapon Shielding, Nullification Blast, Cloak of Opportunity

**2026-03-10** ([forum post](https://forums.playdeadlock.com/threads/03-06-2026-update.114328/post-220287))

- Hero base health increased by 40
- Hero health increased growth by +4 and 8%
- Hero base health increased by 40
- Hero health increased growth by +4 and 8%

**2026-03-06** ([forum post](https://forums.playdeadlock.com/threads/03-06-2026-update.114328/))

- Troopers now gain 7 HP regen when out of combat
- Walkers Health rescaled from 6800/9350/11900 to 6000/9000/12000
- Mid Boss global announcement health threshold reduced from 70% to 50%
- Spirit Shredder Bullets: Spirit Lifesteal increased from 8% to 12%
- Hearts: Heals you for 75 HP (1.25 spirit scaling, half heal no non-heroes)

**2026-02-04** ([forum post](https://forums.playdeadlock.com/threads/01-30-2026-update.102822/post-198653))

- Street Brawl: Healing in base is now 2x faster

**2026-01-30** ([forum post](https://forums.playdeadlock.com/threads/01-30-2026-update.102822/))

- Removed global 40% healing reduction (balance note: it didn't actually work on many things that it was supposed to work on. We'll be adjusting specific things that need healing reductions directly instead.)
- Enhanced Unstable Concoction: Now increases Bonus Health, Weapon Damage, Spirit Power and Stun Duration

**2026-01-20** ([forum post](https://forums.playdeadlock.com/threads/12-29-2025-update.95233/post-185824))

- Stamina Regen in the healing zone is now dramatically increased

**2025-12-17** ([forum post](https://forums.playdeadlock.com/threads/12-16-2025-update.93983/post-178389))

- Stamina now regenerates faster (from 5s to 4.5s for 1 stamina)

**2025-12-16** ([forum post](https://forums.playdeadlock.com/threads/12-16-2025-update.93983/))

- Bonus Health on all Weapon and Spirit items is reduced by ~25
- Vitality investment tree bonuses changed from a % of base health to a fixed amount (from +8/10/13/17/34/39/44/48/52/56% to +75/125/200/275/525/625/750/1000/1200/1400)
- Shrines health increased from 3000 to 7000
- Medic orbs now heals allied troopers 30% more
- Medic orbs regen on allied troopers is now applied over 8s instead of 2s

**2025-12-03** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/post-174987))

- Sprint/Out of Combat regen timer against neutrals increased from 2.5s to 4s (takes longer to start sprinting/regening)

**2025-11-27** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/post-173347))

- Medic Pack now heal amounts increased by 2x
- Medic Pack heal now splits its value evenly based on the number of nearby heroes (so 1 hero is 100%, 2 heroes is 50%, 3 heroes is 33%, etc. Other nearby units also get the reduced values.)
- Medic Pack regen applied over 2s instead of 1s
- Walkers now have escalating health after each one dies. From a constant 12880 to 8000/11000/14000 (model scale slightly smaller for 1st and slightly bigger for last)

**2025-11-23** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/post-172057))

- Hero base health increased by 50

**2025-11-22** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/post-171913))

- Medic Pack missing health % reduced from 10% to 8%
- Stamina regen returned from 5.25s to 5s

**2025-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/))

- Medic troopers no longer have a passive healing pulse ability
- Medic troopers now drop a medic pack when you kill them. Has same pickup range/duration mechanics as the soul orbs on the ground. Heals everyone in a 30m radius for 10% of their missing health as well as 75 plus 2 per minute game time.
- Sprint/Out of Combat regen timer against neutrals increased from 0.5s to 2.5s (takes longer to start sprinting/regening)
- Vitality Investment Bonuses: Now grants an additional +12% Bonus Health at 4800 souls spent
- Stamina regen rate reduced by 5% (5s to 5.25s)
- Mid Boss base health increased from 13000 to 14000
- Mid Boss health growth per minute increased from 200 to 230
- Survival Buff hp regen changed from 0.5->1.5% Max HP to 4->40 Fixed Regen
- Doorman: Base regen from 2 to 1

**2025-10-02** ([forum post](https://forums.playdeadlock.com/threads/10-02-2025-update.84332/))

- Soul Urn: Damage taken when holding too long increased from 1% to 1.5% Max Health per second

**2025-09-04** ([forum post](https://forums.playdeadlock.com/threads/09-04-2025-update.80693/))

- Rejuv only heals the person hitting the crystal

**2025-07-29** ([forum post](https://forums.playdeadlock.com/threads/07-29-2025-update.72760/))

- Reworked Rejuv reward from Mid Boss. No longer buffs troopers, reduces respawn time and buffs various stats. Upon death, 3 rejuv crystals fall to the ground (4 for subsequent midboss kills). Claiming one now grants you in place revive after 3s. If you already claimed one and claim another, it'll go to an ally (priority is closest allies first, then most recent dead allies). Dying with Rejuv no longer counts as a kill/death nor gives out bounties. While you have the Rejuv buff, you gain the following: +20% Max HP, +20% Fire Rate, and +15% Spirit Damage. Gaining the buff heals you to full and lasts up to 7 minutes.
- Added new UI indicator on HP for showing pending heal (affects things like Abram's passive)
- Debuff Remover: Bonus Health reduced from 125 to 100

**2025-07-04** ([forum post](https://forums.playdeadlock.com/threads/07-04-2025-update.70156/))

- Rejuv trooper health bonus reduced from 200/230/260% to 170/200/230%
- Mid Boss shield regeneration changed from 100 + 8/min to 50 + 7/min
- Bullet Lifesteal vs creeps increased from 50% to 60%
- Spirit Lifesteal vs creeps increased from 33% to 40%
- Veilwalker: Heal now scales with boons (+3)

**2025-06-17** ([forum post](https://forums.playdeadlock.com/threads/06-17-2025-update.68401/))

- Time holding Urn before taking damage reduced from 90s to 45s (1% max health damage per second)

**2025-05-21** ([forum post](https://forums.playdeadlock.com/threads/05-21-2025-update.65674/))

- Cultists Sacrifice: Bonus health reduced from 275 to 250

**2025-05-11** ([forum post](https://forums.playdeadlock.com/threads/05-11-2025-update.64113/))

- Mystic Regen: Duration reduced from 6s to 5s
- Mystic Regen: Spirit Power scaling reduced from 0.06 to 0.05

**2025-04-17** ([forum post](https://forums.playdeadlock.com/threads/04-17-2025-update.61382/))

- Medic Trooper: Heal no longer has charges (was 3)
- Medic Trooper: Fixed healing sometimes not functioning on bounce when there are walls nearby

**2025-04-04** ([forum post](https://forums.playdeadlock.com/threads/04-04-2025-update.60284/))

- Lifesteal provided by things like Soul Shredder bullets now properly diminishes in stacking with other sources of lifesteal

**2025-01-12** ([forum post](https://forums.playdeadlock.com/threads/01-12-2025-update.53389/))

- Unstoppable state no longer blocks anti-heal effects

**2024-12-21** ([forum post](https://forums.playdeadlock.com/threads/12-21-2024-update.52206/))

- Shield duration to not take damage before regenerating increased from 18s to 30s

**2024-12-06** ([forum post](https://forums.playdeadlock.com/threads/12-06-2024-update.50599/))

- Return Fire now has +3 HP Regen
- Debuff Remover: Heal on active increased from 10% Max HP to 300 HP

**2024-11-26_HeroLab**

- Reduce health per boon from 35 to 30

**2024-11-21_HeroLab**

- Consume: Reduced T1 upgrade from +75% to +25% heal percentage

**2024-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2024-update.47476/))

- The through-wall ally silhouette health bars are now more accurate
- Mid Boss trooper health for first spawn reduced from 95% to 70%
- Medic Trooper now has 3 charges of heal rather than 2
- Previously was +400 Health and +1% Max Health Regen for 160s.
- Now starts at "+250 Health and 1% Max Health Regen" and ends at "+700 Health and 1.5% Max Health Regen"
- Previously was +2 Stamina, +3 Sprint, +30% Stamina Regen and +50% Zipline Boost for 160s.
- Now starts at "+1 Stamina, +2 Sprint, +20% Stamina Regen and +40% Zipline Boost" and ends at "+4 Stamina, +4 Sprint, +50% Stamina Regen and +80% Zipline Boost"
- Below is a group of changes bundled together that pairs reducing sustain abilities/items as well as anti-heal mechanics by some percentage (some things less than others depending on the specific circumstances of the ability)
- Soul Shredder Bullets: Spirit Lifesteal reduced from 20% to 18%
- New T3 Weapon Item, Spellslinger Headshots: Requires Soul Shredder Bullets. Landing a headshot on enemy heroes increases your total Spirit Power by 3% for 12s. Cooldown 1.5s. Max stacks 12. Grants +12% Weapon Damage, +8% Spirit Amp/18% Spirit Lifesteal (component passive), and +150 Health.
- Debuff Remover: Purging a debuff now also heals you for 10% Max HP
- Superior Stamina: Now grants +75 Health
- New T3 Spirit Item, Spirit Snatch: Requires Spirit Strike. Causes your melee attacks to steal 12% Spirit Resist and 26 Spirit Power for 16s. Cooldown 6s. Buff you receive stacks if you hit different heroes. Grants +15% Melee Damage, +8% Spirit Resist,  +125 Health  and +1 Sprint. (Thanks to https://forums.playdeadlock.com/threads/spirt-snatch-3k-soul-spirit-strike-upgrade.46932/ )
- New T3 Spirit Item, Arcane Surge: Requires Kinetic Dash. After successful Dash Jump, the next ability you use will also have +20% Range, +20% Duration and +20 Spirit Power. Grants +100 Health, +1 Stamina and +15% Slow Resist.

**2024-11-08_HeroLab**

- Reefdweller Harpoon: No longer has passive regen

**2024-11-07** ([forum post](https://forums.playdeadlock.com/threads/11-07-2024-update.44786/))

- Added "Frenzied" text when you own Frenzy and go below 50% health
- Fixed being able to briefly gain regen when crossing the Veil of the enemy fountain
- Fixed a rare bug where shields would never regenerate
- Fixed issues where health regen effect will begin popping on and off if player is at max health
- Mid Boss Rejuv Trooper Health increased by 30%

**2024-11-01_HeroLab**

- Health per boon reduced from 41 to 36

**2024-10-24** ([forum post](https://forums.playdeadlock.com/threads/10-24-2024-update.40951/))

- Added Healing Rite end sound
- If the Urn hasn't been delivered within 90 seconds of pickup time, it now drains your health for 1% of Max HP per second (the timer is per team). Your regen is disabled during this.
- Base Guardians and Shrines no longer have out-of-combat regen
- Medic Trooper heal now has 2 charges; time between casts is 6s [does not consume a charge when healing other troopers, mainly affects waves pushing on their own]
- Medic Trooper heal cooldown increased from 6s to 35s
- High-Velocity Mag: Bullet Shield Health increased from 50 to 65

**2024-10-10** ([forum post](https://forums.playdeadlock.com/threads/10-10-2024-update.36958/))

- Updated the way status effects are shown above the healthbar
- Rescue beam now shows heal indicator if you heal someone with it
- Added Healing Rite cast sound
- Added Rescue Beam heal and pull loop sounds
- Added Health Nova cast sound
- Fixed a bunch of bugs that were impacting how VO was playing in a match.  Now a bunch of hero VO that was previously getting squashed/cut off should play properly (for instance certain lines where allies commented on ability usage, the patrons giving compliments for assists/team healing, etc).
- Golden Statue Health buff increased from 15/20 to 20/30
- Golden Statues now have a tier 3 upgrade at 25 minutes (+2.5% Fire Rate, +8% Ammo, 1.5% CD Reduction, +7% Weapon Damage, 40 Health, +5 Spirit Power)
- Mid Boss now has 15 regen
- Bullet and Spirit Lifesteal now stack diminishingly
- Health Nova: Spirit Power increased from +4 to +6
- Withering Whip: No longer grants +50 Health
- Improved Burst: Max Health damage reduced from 9% to 7%

**2024-09-29** ([forum post](https://forums.playdeadlock.com/threads/09-29-2024-update.34541/))

- Fixed Wraith Cards, Shiv Rage and lifesteal from increasing by shooting the shop

**2024-09-26** ([forum post](https://forums.playdeadlock.com/threads/09-26-2024-update.33015/))

- Non-Health boon bonuses rescaled over the 14 levels (same total as before)
- Health Nova: Weapon Damage increased from 10% to 12%

**2024-09-12** ([forum post](https://forums.playdeadlock.com/threads/09-12-2024-update.27974/))

- Adjusted Midboss low health roar sound to be more distinct from spawn sound
- Updated medic healing beam colors to be consistent with other heals
- Shield regeneration time reduced from 60s to 50s
- Fixed Medic Troopers sometimes using their heal on Guardian boss
- Health Nova: Now requires Healing Rite
- Health Nova: Now grants +4 Spirit Power
- Health Nova: Range reduced from 18m to 15m

**2024-08-29** ([forum post](https://forums.playdeadlock.com/threads/08-29-2024-update.22253/))

- Added a new Profile page that displays a breakdown of recent matches and all-time player and hero statistics (Note: the newly added stats 'Souls Collected' and 'Healing' are starting at 0 for all players)
- Added Heal Amp and Debuff Resist to the Vitality stats in the shop
- Player's low health screen effect more visible for longer if you're below 20% of your max HP
- Added new T3 Weapon Item, Headhunter: Requires High-Velocity Mag. Grants +50% Bullet Velocity, +15% Weapon Damage and +150 Bullet Shield. Passive cooldown: Landing a headshot on heroes deals bonus +140 Damage, heals you for +8% Max HP and grants +2 m/s for 3 seconds. Cooldown: 6 seconds.

**2024-08-15** ([forum post](https://forums.playdeadlock.com/threads/08-15-2024-update.16378/))

- Walker Health increased by 15%
- Base Guardian Health increased by 20%
- Weakened Patron Health increased by 15%
- Health Nova: Health increased from +75 to +100
- Added a new T4 Spirit item, Magic Carpet: Active - After a 1.3s delay, a magic carpet arrives to pick you up. You gain full flight controls and have +6 m/s movement speed. Lasts 7 seconds. If you cast abilities or use your gun, the carpet disappears. While on the Magic Carpet you gain +400 Bullet and +400 Spirit Shields. Passively grants +150 Health, +10% Ability Duration, and +15 Spirit Power. Cooldown: 40s

**2024-08-01** ([forum post](https://forums.playdeadlock.com/threads/08-01-2024-update.13369/))

- Improved visibility of low health state on troopers about to die
- Weakened Patron HP regen increased from 80 to 120
- Mid Boss health gained per minute increased from 350 to 425
- Movement Powerup: Stamina regen increased from 20% to 30%
- Health Nova: Bonus HP increased from +50 to +75

**2024-07-23** ([forum post](https://forums.playdeadlock.com/threads/07-23-2024-update.12505/))

- Mid Boss starting health increased from 5000 to 6000
- Mid Boss health gained per minute increased from 275 to 350

**2024-07-18** ([forum post](https://forums.playdeadlock.com/threads/07-18-2024-update.11831/))

- Added Midboss arrive, low health, and death sound effects
- Walker in mid lanes health increased by 12%
- Weakened Patron health increased by 20%
- Mid Boss starting health increased from 4500 to 5000
- Mid Boss health gained per minute increased from 200 to 275
- Vitality base health bonus increased from 8/12/16/20% to 11/14/17/20%
- Health Nova: Cooldown reduced from 65s to 60s
- Health Nova: Now heals over 2s instead of 3s
- Soul Rebirth (new T4 Vitality item): After you die, you will respawn in 4 seconds where you died with 40% of your Max Health. Cooldown: 220s. Also innately grants +20% Weapon Damage and +10% Cooldown Reduction.

**2024-07-11** ([forum post](https://forums.playdeadlock.com/threads/07-11-2024-update.10871/))

- Updated Restorative Shot impact and heal effects
- Redesigned exit from the base's regeneration area to the rest of the base
- Increased Weakened Patron's out of combat (30s) regeneration from 40 to 80
- Removed platform blocking line of sight from regeneration area exit to the center
- Guardian health increased by 10%
- Base Guardian health increased by 10%
- Movement powerup now grants +20% stamina regeneration
- The spawn area's regeneration buff now lingers for 1s
- Fixed ability-based lifesteals not granting life from damage caused to shields (affects things like Hyperbeam T3, Siphon, Scorn, Life Drain, Flog and Concussive Combustion T3)
- Health Nova: Now grants +10% weapon damage
- Debuff Remover: T3 Vitality Item that upgrades from Debuff Reducer. Removes debuffs fully on cast again. Grants +3 m/s for 3s if any debuff is removed. Grants +40% debuff resist, +125 health, +20% weapon damage. Cooldown: 45
- Silence Glyph: No longer has +75 health

**2024-07-04** ([forum post](https://forums.playdeadlock.com/threads/07-04-2024-update.9652/))

- Survival: +400 Max HP and +1% HP Regen for 100s
- Base Guardians and Shrines now have +40% Bullet Resistance. They lose 20% for each enemy hero nearby (down to a minimum of 0% bullet resistance). When they haven't taken damage for 60 seconds, they regenerate 4% max hp per second.
- Withering Whip: Now grants +50 Health
- Improved Burst: Now grants +100 Spirit Shield Health

**2024-06-27** ([forum post](https://forums.playdeadlock.com/threads/06-27-2024-update.8486/))

- Regeneration powerup duration increased from 25s to 45s
- Medic Trooper heal now bounces to up to one other allied hero within 25m from the hero

**2024-06-20** ([forum post](https://forums.playdeadlock.com/threads/06-20-2024-update.7003/))

- Added search functionality to the shop. You can now search by item name or by individual stat such as 'Ammo', 'Lifesteal', or 'Spirit Power'.
- Active: Gain 12 Spirit and 20% Spirit Lifesteal for 6 seconds. Cooldown: 35s
- +50 Health
- Passive: Pressing the reload key during the halfway point of a reload will cause you to instantly regain your magazine and grant you +30% Bullet Lifesteal and +15% Fire Rate for 6s. The reload UI has an indicator for the trigger window. Cooldown: 25s
- Passive: Walking through a Cosmic Veil causes you to become invisible with +3 m/s for 4 seconds and grants you +30% Fire Rate for your next magazine. Cosmic Veils regenerate any shields you have. Cooldown: 20s
- +75 Health

**2024-06-13** ([forum post](https://forums.playdeadlock.com/threads/06-13-2024-update.5773/))

- Added heal and kill events to the contextual ping wheel slot
- Post lane medic troopers will heal other troopers if a hero within range is full hp
- Post lane medic troopers' hero heal increased from 40 to 80
- Healing/Spawn area in the base now has its defense damage go up over time
- Base side doors near the healing area now open a lot faster
- Medic Bullets: Healing from heroes increased from 25 to 30

**2024-06-06** ([forum post](https://forums.playdeadlock.com/threads/06-06-2024-update.4096/))

- Added new objective health bars for Guardians and Walkers
- Candle trooper health bars now stick around at 1% when they are in self destruct mode to make it more clear they can still be shot
- Visual effects updates for melee lifesteal items
- Fixed training Ivy's True Form causing you to get healed
- Rejuv now causes all your candle troopers to have double health for 3 minutes
- Health Regen powerup regen reduced from 1.5% to 1%
- Health Regen powerup duration increased from 15s to 25s
- Decay changed from 2.2% of Max Health to 2.4% Current Health (less damage when the target is low, and non-lethal now)
- Healbane moved from Spirit tree to Vitality tree
- Healbane now gives +50 Health
- Improved Cooldown: HP Regen reduced from 2 to 1.5

**2024-05-30** ([forum post](https://forums.playdeadlock.com/threads/05-30-2024-update.2514/))

- Adjusted the health bar on Walkers to be easier to see
- Added option to give fast stamina regen in Hero Sandbox

**2024-05-23** ([forum post](https://forums.playdeadlock.com/threads/05-23-2024-update.1245/))

- Ally player glow-through-world silhouette now communicates their current health
- Fixed upgrading McGinnis’s Medicinal Specter to T3 while active causing it to heal everyone to full instantly
- Starting at 15 minutes, one melee Trooper per wave will spawn with 1.75x health
- Medic Trooper health increased from 240 to 260
- Silence Glyph: Health increased from 50 to 75

**2024-05-16** ([forum post](https://forums.playdeadlock.com/threads/05-16-2024-update.902/))

- Medic Trooper health increased from 200 to 240
- Health Nova: Now provides +50 Health

**2024-05-13** ([forum post](https://forums.playdeadlock.com/threads/05-13-2024-update.807/))

- Fixed Stamina not appearing to regenerate while spectating
- Fortitude now starts on cooldown to prevent purchasing and selling in the field for significant regen
- Sprint is now always considered active as long as you are out of combat (haven’t taken or dealt damage for 5s, healthbar is now a little transparent when out of combat).
- Patron (Weakened) now has 40hp/s regen when it has not taken damage for 30s
- Medic Troopers no longer use their heal on troopers if there is a hero within 30m
- Adjusted how the Anti Backdoor system works. It does a little less % damage reduction now, but it regens “backdoor damage” dealt to it over time. Backdoor damage is defined as any damage taken with no candle troopers within 50m in the last 20 seconds.
- Crate Powerups: Increased Health Regen drop from 1.25% Regen to 1.5%

**2024-05-10** ([forum post](https://forums.playdeadlock.com/threads/05-10-2024-update.689/))

- We fixed a bug when combining shields and resistance that caused you to take too much damage. Previously there was a bug where if you take a high amount of damage, the remaining damage after shield reduction would pass through as pure damage instead of being reduced by resist. An example of this is someone dealing 800 spirit damage to you and you having 80 Spirit Shield and 45% Spirit Resistance. With the bug, the 800 would be reduced to 720 from the shield, and then you would lose 720 health. With the fix, the shield now reduces the damage to 720 as usual, but the remaining amount then gets reduced by 45% to 396 health lost instead of 720.​
