# Changelog

Changes to the generated sheet, newest first under each game build.

## Build 6868 (2026-11-24)

Generated 2026-11-25T04:32:04+00:00; previous snapshot was build 6868.

### Heroes

- New columns in the sheet: fire_rate_max_spin, can_headshot, headshot_bonus_scale_pct, headshot_damage_taken_reduction_pct, bullet_resist_per_boon, spirit_resist_per_boon, debuff_resist, innate_bullet_lifesteal_pct, bullet_lifesteal_effectiveness, spirit_lifesteal_effectiveness
- **Baba** damage_per_shot: 26.4 -> 8.8
- **Drifter** damage_per_shot: 60.3 -> 20.1
- **Grey Talon** spirit_scaling: Max Movement Speed: 0.0084; Bullet Damage: 0.08; Damage Per Second: 0.1333; Sustained DPS: 0.1084 -> Max Movement Speed: 0.0084; Bullet Damage: 0.08
- **Haze** spirit_scaling: Clip Size: 0.5; Sustained DPS: 0.2471 -> Clip Size: 0.5
- **Solomon** spirit_scaling: Bullet Damage: 0.14; Damage Per Second: 0.28; Sustained DPS: 0.16 -> Bullet Damage: 0.14
- **Vindicta** spirit_scaling: Bullet Damage: 0.022; Damage Per Second: 0.0952; Sustained DPS: 0.0572 -> Bullet Damage: 0.022
- **Warden** spirit_scaling: Rounds Per Second: 0.008; Fire Rate: 0.21; Damage Per Second: 0.1387; Sustained DPS: 0.0507 -> Fire Rate: 0.21
- **Yamato** spirit_scaling: Clip Size: 0.15; Sustained DPS: 0.1723 -> Clip Size: 0.15

### Abilities

- **Apollo / Riposte** slow_percent: 40 -> (blank)
- **Apollo / Riposte** slow_duration: 4 -> (blank)
- **Apollo / Riposte** other_scaling: Damage Threshold: 4 per boon -> (blank)
- **Apollo / Riposte** internal_properties: AbilityLifestealPercentHero=50; CounterattackAntiMashDelay=0.2; DamageThreshold=60 (+4 x boon); DampingFactor=0.5; DashGraceWindow=1.3; DashRadius=2.2; DashRange=35; DashSpeed=76.2; LiftHeight=240; MoveSpeedMax=4; SideMoveSpeed=-100; SlashConeAngle=90; SlashHalfWidth=1; SlashRadius=6; TurnRateMax=10 -> AbilityLifestealPercentHero=50; CounterattackAntiMashDelay=0.2; DamageThreshold=60 (+4 x boon); DampingFactor=0.5; DashGraceWindow=1.3; DashRadius=2.2; DashRange=35; DashSpeed=76.2; LiftHeight=240; MoveSpeedMax=4; SideMoveSpeed=-100; SlashConeAngle=90; SlashHalfWidth=1; SlashRadius=6; SlowDuration=4; SlowPercent=40; TurnRateMax=10
- **Apollo / Itani Lo Sahn** spirit_scaling: Delayed Damage: 2.6; Impact Damage: 0.77 -> Delayed Damage: 2.6
- **Bebop / Exploding Uppercut** other_properties: Uppercut Damage: 0.01 (+1 x melee damage); Duration [Displacement]: 0.5s; Area Damage: 75 (+0.6 x spirit power); Fire Rate: -14% (+-0.186 x spirit power); Landing Radius: 14m -> Uppercut Damage: 0.01 (+1 x light melee damage); Duration [Displacement]: 0.5s; Area Damage: 75 (+0.6 x spirit power); Fire Rate: -14% (+-0.186 x spirit power); Landing Radius: 14m
- **Bebop / Exploding Uppercut** other_scaling: Uppercut Damage: 1 per melee damage -> Uppercut Damage: 1 per light melee damage
- **Bebop / Grapple Arm** slow_percent: 72 -> (blank)
- **Bebop / Grapple Arm** other_scaling: Damage: 0.7 per melee damage -> Damage: 0.7 per light melee damage
- **Bebop / Grapple Arm** internal_properties: AbilityPostCastDuration=0.2; CancelHookDuration=0.2; FriendlyHookIgnoreRange=8; HookImpactDelay=0.5; HookingSlowSpeedLimit=5; RestrictionDuration=0.5 -> AbilityPostCastDuration=0.2; CancelHookDuration=0.2; FriendlyHookIgnoreRange=8; HookImpactDelay=0.5; HookingSlowSpeedLimit=5; RestrictionDuration=0.5; SlowPercent=72
- **Billy / Bashdown** other_properties: Channel Duration: 0.3s; Wave End Radius: 8m; Melee Damage: 0 (+0.9 x melee damage); Duration [Displacement]: 0.4s -> Channel Duration: 0.3s; Wave End Radius: 8m; Melee Damage: 0 (+0.9 x light melee damage); Duration [Displacement]: 0.4s
- **Billy / Bashdown** other_scaling: Melee Damage: 0.9 per melee damage -> Melee Damage: 0.9 per light melee damage
- **Billy / Chain Gang** dps: 45 -> (blank)
- **Billy / Chain Gang** dps_spirit_scale: 0.9 -> (blank)
- **Billy / Chain Gang** spirit_scaling: Damage Per Second: 0.9; Damage: 0.7 -> Damage: 0.7
- **Billy / Chain Gang** internal_properties: AbilityPostCastDuration=0.2; MoveSpeedSlowMinPct=25; PullDistance=4; PullDuration=0.8; PullForceMax=2000; PullTrackCasterDuration=0.5; RopeLength=2; RopeSnapDistance=45; RopeSnapNoLOSDuration=0.5; RopeSoftEdgeLength=4.5; TickRate=0.25 -> AbilityPostCastDuration=0.2; DPS=45 (+0.9 x spirit power); MoveSpeedSlowMinPct=25; PullDistance=4; PullDuration=0.8; PullForceMax=2000; PullTrackCasterDuration=0.5; RopeLength=2; RopeSnapDistance=45; RopeSnapNoLOSDuration=0.5; RopeSoftEdgeLength=4.5; TickRate=0.25
- **Calico / Leaping Slash** other_properties: Cast Delay: 0.1s; Slash Radius: 4m; Impact Damage: 10 (+0.8 x melee damage) -> Cast Delay: 0.1s; Slash Radius: 4m; Impact Damage: 10 (+0.8 x light melee damage)
- **Calico / Leaping Slash** other_scaling: Impact Damage: 0.8 per melee damage -> Impact Damage: 0.8 per light melee damage
- **Deadman Danny / Jettison Fuel** upgrade_3: Bullet Resist -10%; Burst Mark Stacks +1 \| -10% Bullet Resist Shred On Backblast Hit: Apply a Mark -> Bullet Resist Reduction -10%; Burst Mark Stacks +1 \| -10% Bullet Resist Shred On Backblast Hit: Apply a Mark
- **Drifter / Rend** other_scaling: Damage: 1.2 per melee damage -> Damage: 1.2 per light melee damage
- **Drifter / Stalker's Mark** upgrade_1: Bullet Resist -8% \| -8% Bullet Resist -> Bullet Resist Reduction -8% \| -8% Bullet Resist
- **Drifter / Stalker's Mark** upgrade_3: Bleed Damage +1.5% DPS; Incoming Healing -40%; Incoming Healing -40% \| +1.5% Bleed and -40% Incoming Healing -> Bleed Damage +1.5% DPS; Incoming Healing -40%; Healing From Regen -40% \| +1.5% Bleed and -40% Incoming Healing
- **Dynamo / Kinetic Pulse** upgrade_2: Bullet Resist -15%; Move Speed Slow +24%; Slow Duration +4s \| On Hit: -15% Bullet Resist and -24% Move Speed for 4s -> Bullet Resist Reduction -15%; Move Speed Slow +24%; Slow Duration +4s \| On Hit: -15% Bullet Resist and -24% Move Speed for 4s
- **Graves / Jar of Dead** other_scaling: Skull Kill Gold: 0.5 per boon; Summon Health: 1.3 per boon -> (blank)
- **Graves / Grasping Hands** slow_percent: 40 -> (blank)
- **Graves / Grasping Hands** internal_properties: AuraRadius=0.75; DebuffDuration=0.5; GrabHeight=1.75; GroundAuraPopDelay=1.1; GroundAuraSpacing=1; TetherDuration=1; TetherRadius=0.1; TickRate=0.1; ZombieWallDeployTime=0.8; ZombieWallHeight=2.5 -> AuraRadius=0.75; DebuffDuration=0.5; GrabHeight=1.75; GroundAuraPopDelay=1.1; GroundAuraSpacing=1; SlowPercent=40; TetherDuration=1; TetherRadius=0.1; TickRate=0.1; ZombieWallDeployTime=0.8; ZombieWallHeight=2.5
- **Graves / Borrowed Decree** other_scaling: Summon Health: 8 per boon; Spirit Power: 1 per boon -> Summon Health: 8 per boon
- **Grey Talon / Spirit Snare** upgrade_2: Bullet Resist -15%; Debuff Duration +10s \| Applies -15% Bullet Resist for 10s -> Bullet Resist Reduction -15%; Debuff Duration +10s \| Applies -15% Bullet Resist for 10s
- **Haze / Sleep Dagger** upgrade_1: Bullet Resist -10%; Bullet Resist Reduction Duration +6 \| -10% Bullet Resist Reduction for 6s on wake-up -> Bullet Resist Reduction -10%; Bullet Resist Reduction Duration +6 \| -10% Bullet Resist Reduction for 6s on wake-up
- **Haze / Fixation** upgrade_3: Weapon Damage +0.11/stack and +0.0003 x weapon damage % scaling \| +0.11/ per Stack Scales with Weapon Damage -> Weapon Damage +0.11/stack and +0.00035 x weapon damage % scaling \| +0.11/ per Stack Scales with Weapon Damage
- **Holliday / Crackshot** upgrade_2: Damage +49.5; Bullet Resist -6%; Bullet Resist Reduction Duration +5 \| +49.5 Damage and -6% Bullet Resist for 5s -> Damage +49.5; Bullet Resist Reduction -6%; Bullet Resist Reduction Duration +5 \| +49.5 Damage and -6% Bullet Resist for 5s
- **Infernus / Napalm** upgrade_3: Damage Taken +17%; Incoming Healing -33%; Incoming Healing -33% \| Napalm Effect: +17% Damage Taken and -33% Healing -> Damage Taken +17%; Incoming Healing -33%; Healing From Regen -33% \| Napalm Effect: +17% Damage Taken and -33% Healing
- **Kelvin / Frost Grenade** spirit_scaling: Aura HPS: 0.8; Damage: 0.6; Heal Amount: 0.8 -> Damage: 0.6; Heal Amount: 0.8
- **Kelvin / Ice Path** spirit_scaling: Explode Damage: 0.8 -> (blank)
- **Kelvin / Arctic Beam** slow_duration: 0.6 -> (blank)
- **Kelvin / Arctic Beam** spirit_scaling: Beam Heal Per Second: 0.6; Damage Per Second: 0.38 -> Damage Per Second: 0.38
- **Kelvin / Arctic Beam** internal_properties: BeamHealPerSecond=0 (+0.6 x spirit power); ChannelSlowPercent=8; MinSlowPercent=24; PathWidth=1.1; TickRate=0.1 -> BeamHealPerSecond=0 (+0.6 x spirit power); ChannelSlowPercent=8; MinSlowPercent=24; PathWidth=1.1; SlowDuration=0.6; TickRate=0.1
- **Kelvin / Frozen Shelter** upgrade_2: Duration +1.5s; Fire Rate +20% \| +1.5s Duration Applies -20% Fire Rate -> Duration +1.5s; Fire Rate Slow +20% \| +1.5s Duration Applies -20% Fire Rate
- **Lash / Ground Strike** spirit_scaling: Stomp Damage: 0.7905; Damage Per Meter: 0.04; Damage Per Meter (25m+): 0.0081 -> Stomp Damage: 0.7905; Damage Per Meter: 0.04
- **Lash / Ground Strike** internal_properties: AbilityPostCastDuration=0.4; MinAimAngle=60; StompDamagePerMeterSecondary=4.2 (+0.0081 x spirit power); StompDamagePrimaryRange=25; StompVerticalThreshold=118; StrikeVelocity=50 -> AbilityPostCastDuration=0.4; MinAimAngle=60; StompDamagePerMeterSecondary=4.2 (+0.00814 x spirit power); StompDamagePrimaryRange=25; StompVerticalThreshold=118; StrikeVelocity=50
- **Lash / Ground Strike** upgrade_3: Damage Per Meter +2.2 and +0.04 x spirit power scaling; Damage Per Meter (25m+) +2.2 and +0.0081 x spirit power scaling \| Damage Per Meter +120% and improved scaling -> Damage Per Meter +2.2 and +0.04 x spirit power scaling; Damage Per Meter (25m+) +2.2 and +0.00814 x spirit power scaling \| Damage Per Meter +120% and improved scaling
- **Lash / Flog** upgrade_2: Cooldown -16s; Fire Rate +30% \| Apply -30% Fire Rate -16s Cooldown -> Cooldown -16s; Fire Rate Slow +30% \| Apply -30% Fire Rate -16s Cooldown
- **Nurse Harrow / Leech Therapy** other_scaling: Leech Crawl Range: 1.3 per boon; Leech Move Speed: 0.05 per boon; Health Regen Per Leech: 0.13 per boon -> Leech Crawl Range: 1.3 per boon; Health Regen Per Leech: 0.13 per boon
- **Nurse Harrow / Lurking Terrors** upgrade_2: Move Speed Slow +20%; Fire Rate +20%; Damage Per Second +30 \| -20% Move Speed and Fire Rate +30 DPS -> Move Speed Slow +20%; Fire Rate Slow +20%; Damage Per Second +30 \| -20% Move Speed and Fire Rate +30 DPS
- **Paige / Captivating Read** upgrade_3: Tech Armor Damage Reduction -18%; Debuff Duration +6s; Radius +2m \| +2m Radius On Hit: Reduce Spirit Resist by -18% for 6s -> Spirit Resist Reduction -18%; Debuff Duration +6s; Radius +2m \| +2m Radius On Hit: Reduce Spirit Resist by -18% for 6s
- **Pocket / Enchanter's Satchel** upgrade_3: Fire Rate +40%; Move Slow Percent +32; Debuff Duration +4s; Channel Duration +1.5s; Radius +4m \| +1.5s Duration +4m Radius -32% Move Speed and Fire Rate for 4s -> Fire Rate Slow +40%; Move Slow Percent +32; Debuff Duration +4s; Channel Duration +1.5s; Radius +4m \| +1.5s Duration +4m Radius -32% Move Speed and Fire Rate for 4s
- **Rem / Pillow Toss** upgrade_2: Fire Rate +35%; Radius +2m \| +2m Radius and applies -35% Fire Rate -> Fire Rate Slow +35%; Radius +2m \| +2m Radius and applies -35% Fire Rate
- **Rem / Lil Helpers** damage: 20 -> (blank)
- **Rem / Lil Helpers** internal_properties: ArmTime=0.1; AuraAttackHeight=10; AuraRadius=10; AuraSoftRadius=10; DPSPerSprite=1; HelperChoreCooldownDuration=5; HelperCount=1; HelperDowntimeDuration=15.1; HelpersPerPatrol=4; InfestBurstHealthPercent=75; InfestHealInterval=2; PatrolDamageCooldown=10; TickRate=0.2 -> ArmTime=0.1; AuraAttackHeight=10; AuraRadius=10; AuraSoftRadius=10; DPSPerSprite=1; Damage=20; HelperChoreCooldownDuration=5; HelperCount=1; HelperDowntimeDuration=15.1; HelpersPerPatrol=4; InfestBurstHealthPercent=75; InfestHealInterval=2; PatrolDamageCooldown=10; TickRate=0.2
- **Seven / Power Surge** spirit_scaling: Damage on Jump: 0.32; Shock Damage: 0.14 -> Shock Damage: 0.14
- **Shiv / Slice and Dice** upgrade_2: Tech Armor Damage Reduction -4%; Time Window +2s \| -4% Spirit Resist +2m Dash Range -> Spirit Resist Reduction -4%; Time Window +2s \| -4% Spirit Resist +2m Dash Range
- **Silver / Slam Fire** damage: 40 -> (blank)
- **Silver / Slam Fire** internal_properties: BulletEffectiveness=0.1; BulletRadiusOverride=7; BulletSpread=-1; DebuffDuration=3; LingerDuration=0.1; ProcChance=100; RecoilDelayFactor=0.05; RecoilRecoverySpeed=0.1; RecoilSpeed=12; RecoilStrength=12; SpreadPenaltyPerShot=0.5 -> BulletEffectiveness=0.1; BulletRadiusOverride=7; BulletSpread=-1; Damage=40; DebuffDuration=3; LingerDuration=0.1; ProcChance=100; RecoilDelayFactor=0.05; RecoilRecoverySpeed=0.1; RecoilSpeed=12; RecoilStrength=12; SpreadPenaltyPerShot=0.5
- **Silver / Boot Kick** slow_duration: 0.1 -> (blank)
- **Silver / Boot Kick** other_scaling: Damage: 0.9 per melee damage -> Damage: 0.9 per light melee damage
- **Silver / Boot Kick** internal_properties: AbilityPostCastDuration=0.25; AirDrag=0.8; EnemyPushForceAway=300; EnemyPushForceUp=300; FallSpeedMax=20; LeapForwardOffset=2.5; LeapRadius=1.7; SelfPushForceUp=200; SuccessInputWindow=0.3; TimeScaleDebuff=95 -> AbilityPostCastDuration=0.25; AirDrag=0.8; EnemyPushForceAway=300; EnemyPushForceUp=300; FallSpeedMax=20; LeapForwardOffset=2.5; LeapRadius=1.7; SelfPushForceUp=200; SlowDuration=0.1; SuccessInputWindow=0.3; TimeScaleDebuff=95
- **Silver / Lycan Curse** other_scaling: Bonus Health: 15 per boon; Heal Amount: 1 per boon; Low Health Rage Bonus: 1.8 per boon; Max Rage: 9.4 per boon -> Bonus Health: 15 per boon; Heal Amount: 1 per boon
- **Silver / Silver (Transformed) / Go For The Throat** other_scaling: Damage: 1.5 per melee damage -> Damage: 1.5 per light melee damage
- **Silver / Silver (Transformed) / Mauling Leap** other_scaling: Damage: 1.5 per melee damage -> Damage: 1.5 per light melee damage
- **Silver / Silver (Transformed) / Mauling Leap** upgrade_3: Bullet Resist -12% -> Bullet Resist Reduction -12%
- **Silver / Silver (Transformed) / Tail Whack** slow_duration: 2 -> (blank)
- **Silver / Silver (Transformed) / Tail Whack** internal_properties: AbilityPostCastDuration=0.2; LeftForce=400; PushForce=300; SlashHeight=3 -> AbilityPostCastDuration=0.2; LeftForce=400; PushForce=300; SlashHeight=3; SlowDuration=2
- **Sinclair / Vexing Bolt** upgrade_1: Fire Rate +25%; Debuff Duration +5s \| Bolts apply -25% Fire Rate for 5s. -> Fire Rate Slow +25%; Debuff Duration +5s \| Bolts apply -25% Fire Rate for 5s.
- **Solomon / Setup Bishop** dps: 30 -> (blank)
- **Solomon / Setup Bishop** dps_spirit_scale: 0.7 -> (blank)
- **Solomon / Setup Bishop** spirit_scaling: Damage Per Second: 0.7; Damage: 0.85; Impact Damage: 2; Pulse Damage: 0.8 -> Damage: 0.85; Impact Damage: 2
- **Solomon / Setup Bishop** internal_properties: AuraHeight=50; BishopTimemBetweenShots=0.05; BossDamageScale=0.5; BulletResist=25; CurrentCooldownRefundPercent=50; DPSTickInterval=0.25; DashSlowPercent=-25; ExpireDistance=80; GroundAuraHeight=1; ImpactRadius=2.5; MaxPieces=1; MultiHitPenaltyPercentage=25; PulseDamage=0 (+0.8 x spirit power); TechResist=50; TickInterval=0.15 -> AuraHeight=50; BishopTimemBetweenShots=0.05; BossDamageScale=0.5; BulletResist=25; CurrentCooldownRefundPercent=50; DPS=30 (+0.7 x spirit power); DPSTickInterval=0.25; DashSlowPercent=-25; ExpireDistance=80; GroundAuraHeight=1; ImpactRadius=2.5; MaxPieces=1; MultiHitPenaltyPercentage=25; PulseDamage=0 (+0.8 x spirit power); TechResist=50; TickInterval=0.15
- **Solomon / Kingside Knight** other_scaling: Move Distance: 0.23 per boon; King Move Distance: 0.14 per boon; Spirit Resist: 0.5 per boon -> Move Distance: 0.23 per boon; King Move Distance: 0.14 per boon
- **Solomon / Rook Battery** barrier: 100 -> (blank)
- **Solomon / Rook Battery** spirit_scaling: Move Speed: 0.1; Damage: 0.9 -> Damage: 0.9
- **Solomon / Rook Battery** other_scaling: Move Distance: 0.23 per boon -> (blank)
- **Solomon / Rook Battery** internal_properties: AirDrag=0.3; AirSpeedMax=100; BonusMoveSpeedPercent=0 (+0.1 x spirit power); DetonationDelay=0.25; FallSpeedMax=10; GroundAuraHeight=2; GroundAuraLingerDuration=0.5; GroundAuraRadius=0; GroundAuraSpacing=3; MaxTriggers=1; MoveDistance=12 (+0.23 x boon); SlideScale=100; SummonHealth=100; TossBackSpeed=300; TossDuration=1; TossUpSpeed=220 -> AirDrag=0.3; AirSpeedMax=100; BonusMoveSpeedPercent=0 (+0.1 x spirit power); CombatBarrier=100; DetonationDelay=0.25; FallSpeedMax=10; GroundAuraHeight=2; GroundAuraLingerDuration=0.5; GroundAuraRadius=0; GroundAuraSpacing=3; MaxTriggers=1; MoveDistance=12 (+0.23 x boon); SlideScale=100; SummonHealth=100; TossBackSpeed=300; TossDuration=1; TossUpSpeed=220
- **Solomon / Rook Battery** upgrade_1: Fire Rate +25%; Debuff Duration +5s \| On Hit: Reduce 25% Fire Rate for 5s -> Fire Rate Slow +25%; Debuff Duration +5s \| On Hit: Reduce 25% Fire Rate for 5s
- **Solomon / Develop Queen** dps: 50 -> (blank)
- **Solomon / Develop Queen** dps_spirit_scale: 0.7 -> (blank)
- **Solomon / Develop Queen** spirit_scaling: Damage Per Second: 0.7; Damage: 1.6 -> Damage: 1.6
- **Solomon / Develop Queen** internal_properties: AuraHeight=8; AuraLingerDuration=0.15; DPSTickInterval=0.5; ExpireDistance=80; GroundAuraHeight=1; Height=10; LiftHeight=4; MaxPieces=1; MaxStacks=3; TossUpSpeed=600 -> AuraHeight=8; AuraLingerDuration=0.15; DPS=50 (+0.7 x spirit power); DPSTickInterval=0.5; ExpireDistance=80; GroundAuraHeight=1; Height=10; LiftHeight=4; MaxPieces=1; MaxStacks=3; TossUpSpeed=600
- **Venator / Consecrating Grenade** upgrade_3: Incoming Healing -20%; Incoming Healing -20%; Charges +1; Charge Delay +3s \| -20% Incoming Healing and allow Charges -> Incoming Healing -20%; Healing From Regen -20%; Charges +1; Charge Delay +3s \| -20% Incoming Healing and allow Charges
- **Victor / Aura of Suffering** damage_spirit_scale: 1.1 -> (blank)
- **Victor / Aura of Suffering** spirit_scaling: Damage: 1.1; Max DPS: 0.72; Minimum DPS: 0.15 -> Max DPS: 0.72; Minimum DPS: 0.15
- **Victor / Aura of Suffering** internal_properties: BossDamageScale=0.5; DebuffDuration=0.5; SelfDPS=15; TickRate=0.25 -> BossDamageScale=0.5; Damage=0 (+1.1 x spirit power); DebuffDuration=0.5; SelfDPS=15; TickRate=0.25
- **Vindicta / Crow Familiar** upgrade_1: Incoming Healing -35%; Incoming Healing -35% \| Reduces Incoming Healing by -35% -> Incoming Healing -35%; Healing From Regen -35% \| Reduces Incoming Healing by -35%
- **Vindicta / Crow Familiar** upgrade_3: Bullet Resist -8%; Tech Armor Damage Reduction -8%; Debuff Duration +2s \| +2s Duration -8% Bullet Resist -8% Spirit Resist -> Bullet Resist Reduction -8%; Spirit Resist Reduction -8%; Debuff Duration +2s \| +2s Duration -8% Bullet Resist -8% Spirit Resist
- **Viscous / Puddle Punch** other_scaling: Damage: 0.6 per melee damage -> Damage: 0.6 per light melee damage
- **Vyper / Screwjab Dagger** slow_duration: 2 -> (blank)
- **Vyper / Screwjab Dagger** internal_properties: (blank) -> SlowDuration=2
- **Vyper / Screwjab Dagger** upgrade_2: Bullet Resist -8%; Bullet Resist per Stack -6% \| On Hit: -8% Bullet Resist and -6% Bullet Resist per Stack -> Bullet Resist Reduction -8%; Bullet Resist per Stack -6% \| On Hit: -8% Bullet Resist and -6% Bullet Resist per Stack
- **Vyper / Lethal Venom** upgrade_2: Incoming Healing -40%; Incoming Healing -40%; Cooldown -12s \| -40% Incoming Healing and -12s Cooldown -> Healing From Regen -40%; Incoming Healing -40%; Cooldown -12s \| -40% Incoming Healing and -12s Cooldown
- **Warden / Alchemical Flask** upgrade_3: Fire Rate +30%; Cooldown -7s; Radius +2m \| -7s Cooldown and +2m Radius Applies -30% Fire Rate -> Fire Rate Slow +30%; Cooldown -7s; Radius +2m \| -7s Cooldown and +2m Radius Applies -30% Fire Rate
- **Warden / Binding Word** upgrade_1: Bullet Resist +20%; Duration +5s \| Warden deals +20% more Bullet Damage to trapped Heroes for 5s -> Bullet Resist Reduction +20%; Duration +5s \| Warden deals +20% more Bullet Damage to trapped Heroes for 5s
- **Yamato / Flying Slash** other_scaling: Damage: 1.2 per melee damage -> Damage: 1.2 per light melee damage

### Items

- New columns in the sheet: ability_cooldown_reduction_pct
- **Fleetfoot** other_innate_stats: Slide Distance: 35%; move speed penalty while shooting reduction: 100; Move While Zoomed Speed Penalty Reduction Percent: 100 -> Slide Distance: 35%
- **Fleetfoot** stats_not_on_tooltip: move speed penalty while shooting reduction: 100; Move While Zoomed Speed Penalty Reduction Percent: 100 -> Move Speed Penalty While Shooting Removed: 100; Move Speed Penalty While Zoomed Removed: 100
- **Intensifying Magazine** other_innate_stats: Weapon Damage: % -> (blank)
- **Spirit Shredder** enemy_effects: [Passive] Tech Armor Damage Reduction: -8%; Debuff Duration: 8s -> [Passive] Spirit Resist Reduction: -8%; Debuff Duration: 8s
- **Stalker** enemy_effects: [Effect, 6s cooldown] Damage Per Second: 17; Bullet Resist: -6%; Debuff Duration: 5s -> [Effect, 6s cooldown] Damage Per Second: 17; Bullet Resist Reduction: -6%; Debuff Duration: 5s
- **Weakening Headshot** enemy_effects: [Passive] Bullet Resist: -12%; Debuff Duration: 12s -> [Passive] Bullet Resist Reduction: -12%; Debuff Duration: 12s
- **Alchemical Fire** enemy_effects: [Active, 30s cooldown] Damage Per Second: 45 (+0.2 x spirit power); Bullet Resist: -7% (+-0.055 x spirit power); Max DPS: 95 (+0.4 x spirit power) -> [Active, 30s cooldown] Damage Per Second: 45 (+0.2 x spirit power); Bullet Resist Reduction: -7% (+-0.055 x spirit power); Max DPS: 95 (+0.4 x spirit power)
- **Ballistic Enchantment** other_innate_stats: Radius: 22% -> (blank)
- **Ballistic Enchantment** stats_not_on_tooltip: Radius: 22% -> (blank)
- **Cultist Sacrifice** stats_not_on_tooltip: (blank) -> Bonus Ability Charges: 1 (flagged conditional)
- **Cultist Sacrifice** conditional_effects: [Active, 270s cooldown] Weapon Damage: 10% (+0.8 x boon); Bonus Health: 50 (+4 x boon); Ability Range: 12%; Duration: 160s \| [Not on tooltip] Bonus Ability Charges: 1; Radius: 12% -> [Active, 270s cooldown] Weapon Damage: 10% (+0.8 x boon); Bonus Health: 50 (+4 x boon); Ability Range: 12%; Duration: 160s
- **Hollow Point** enemy_effects: [Passive] Bullet Resist: -10%; Debuff Duration: 8s -> [Passive] Bullet Resist Reduction: -10%; Debuff Duration: 8s
- **Hunter's Aura** enemy_effects: [Passive] Bullet Resist: -10%; Fire Rate: 15% -> [Passive] Bullet Resist Reduction: -10%; Fire Rate Slow: 15%
- **Shadow Weave** conditional_effects: [Active, 37s cooldown] Status Effect Invisible: None; Stealth Duration: 13s; Spot Radius: 20m; Invis Sprint Speed: 5m \| [Active] Ambush Weapon Damage: 50%; Ambush Spirit Power: 25; Ambush Duration: 5s; Time to Full Ambush: 6s -> [Active, 37s cooldown] Stealth Duration: 13s; Spot Radius: 20m; Invis Sprint Speed: 5m \| [Active] Ambush Weapon Damage: 50%; Ambush Spirit Power: 25; Ambush Duration: 5s; Time to Full Ambush: 6s
- **Spirit Rend** enemy_effects: [Effect] Tech Armor Damage Reduction: -8% \| [Passive, 2s cooldown] Spirit Resist on Headshot: -7%; Debuff Duration: 8s -> [Effect] Spirit Resist Reduction: -8% \| [Passive, 2s cooldown] Spirit Resist Reduction: -7%; Debuff Duration: 8s
- **Toxic Bullets** stats_not_on_tooltip: (blank) -> Healing From Regen: -40% (flagged conditional)
- **Toxic Bullets** enemy_effects: [Effect] Bleed Damage: 1.9% DPS (+0.006 x spirit power); Incoming Healing: -40%; Dot Duration: 4 \| [Not on tooltip] Incoming Healing: -40% -> [Effect] Bleed Damage: 1.9% DPS (+0.006 x spirit power); Incoming Healing: -40%; Dot Duration: 4
- **Crippling Headshot** stats_not_on_tooltip: (blank) -> Incoming Healing: -40% (flagged conditional)
- **Crippling Headshot** enemy_effects: [Passive] Bullet Resist: -16%; Spirit Resist: -16%; Incoming Healing: -40%; Debuff Duration: 12s \| [Not on tooltip] Incoming Healing: -40% -> [Passive] Bullet Resist Reduction: -16%; Spirit Resist Reduction: -16%; Healing From Regen: -40%; Debuff Duration: 12s
- **Crushing Fists** enemy_effects: [Passive] Bullet Resist: -5%; Stun Duration: 0.75s; Debuff Duration: 8s -> [Passive] Bullet Resist Reduction: -5%; Stun Duration: 0.75s; Debuff Duration: 8s
- **Glass Cannon** stats_not_on_tooltip: (blank) -> Bullet Slow Proc: 30% (flagged conditional)
- **Glass Cannon** enemy_effects: [Not on tooltip] Bullet Slow Proc: 30% -> (blank)
- **Silencer** conditional_effects: [Passive] Spirit Damage Reduction: -25% \| [Passive] Immunity Duration: 10s; Build Up Per Shot: 1.04 -> [Passive] Immunity Duration: 10s; Build Up Per Shot: 1.04
- **Silencer** enemy_effects: [Passive] Debuff Duration: 6s \| [Passive] Silence Duration: 2.5s [EMP] -> [Passive] Spirit Damage Reduction: -25%; Debuff Duration: 6s \| [Passive] Silence Duration: 2.5s [EMP]
- **Spellslinger** fire_rate_pct: 11 -> (blank)
- **Spellslinger** other_innate_stats: Reload Time: -10% -> (blank)
- **Spellslinger** conditional_effects: [Passive] Max Stacks: 6; Buff Duration: 18s -> [Passive] Fire Rate: 11%; Reload Time: -10%; Max Stacks: 6; Buff Duration: 18s
- **Spiritual Overflow** fire_rate_pct: 25 -> (blank)
- **Spiritual Overflow** other_innate_stats: Ability Duration: 13%; Spirit Power: 30; Spirit Lifesteal: 10% -> Ability Duration: 13%
- **Spiritual Overflow** conditional_effects: [Passive] Build Up Per Shot: 1.08; Duration: 15s -> [Passive] Fire Rate: 25%; Spirit Power: 30; Spirit Lifesteal: 10%; Build Up Per Shot: 1.08; Duration: 15s
- **Rebuttal** other_innate_stats: Parry Cooldown: 1.25s; Melee Resist: 18% -> Parry Cooldown Reduction: 1.25s; Melee Resist: 18%
- **Debuff Reducer** other_innate_stats: (blank) -> Debuff Resist: 25%
- **Debuff Reducer** conditional_effects: [Passive] Debuff Resist: 25% -> (blank)
- **Enchanter's Emblem** spirit_power: 15 -> (blank)
- **Enchanter's Emblem** conditional_effects: (blank) -> [Passive] Spirit Power: 15; Ability Cooldown Reduction: 5%
- **Enduring Speed** other_innate_stats: (blank) -> Slow Resist: 25%
- **Enduring Speed** conditional_effects: [Passive] Slow Resist: 25% -> (blank)
- **Guardian Ward** other_innate_stats: Ability Range: 8%; Radius: 8% -> Ability Range: 8%
- **Guardian Ward** stats_not_on_tooltip: Radius: 8% -> (blank)
- **Healbane** stats_not_on_tooltip: (blank) -> Healing From Regen: -35% (flagged conditional)
- **Healbane** enemy_effects: [Passive] Incoming Healing: -35% \| [Not on tooltip] Incoming Healing: -35% -> [Passive] Incoming Healing: -35%
- **Healing Booster** other_innate_stats: Health Regen Boost: 20% -> Outgoing Healing: 20%
- **Healing Booster** conditional_effects: [Passive] Outgoing Healing: 20% -> (blank)
- **Trophy Collector** unlisted_properties: StackingTechRadiusMultiplier=0.75; ThinkRate=3 -> ThinkRate=3
- **Fury Trance** stats_not_on_tooltip: (blank) -> Move Speed Penalty While Shooting Removed: 100 (flagged conditional)
- **Fury Trance** conditional_effects: [Active, 18s cooldown] Fire Rate: 32%; Move Speed: 1.5m; Spirit Resist: 40%; Duration: 6.5s \| [Not on tooltip] move speed penalty while shooting reduction: 100 -> [Active, 18s cooldown] Fire Rate: 32%; Move Speed: 1.5m; Spirit Resist: 40%; Duration: 6.5s
- **Healing Nova** other_innate_stats: Ability Range: 5%; Radius: 5% -> Ability Range: 5%
- **Healing Nova** stats_not_on_tooltip: Radius: 5% -> (blank)
- **Majestic Leap** stats_not_on_tooltip: (blank) -> Air Control: 100% (flagged conditional); Move Speed Slow: 32% (flagged conditional)
- **Majestic Leap** conditional_effects: [Active, 45s cooldown] Barrier: 200 (+12 x boon); Interrupt Cooldown: 5s; Barrier Duration: 8s; Air Control: 50% \| [Not on tooltip] Air Control: 100% -> [Active, 45s cooldown] Barrier: 200 (+12 x boon); Interrupt Cooldown: 5s; Barrier Duration: 8s; Air Control: 50%
- **Majestic Leap** enemy_effects: [Not on tooltip] Move Speed Slow: 32% -> (blank)
- **Metal Skin** conditional_effects: [Active, 24s cooldown] Active Movespeed Penalty: -1.5m; Duration: 5s -> [Active, 24s cooldown] Active Movespeed Penalty: -1.5m; Gravity Scale: 20%; Dash Distance: -20%; Duration: 5s
- **Metal Skin** enemy_effects: [Active, 24s cooldown] Gravity Scale: 20%; Dash Distance: -20% -> (blank)
- **Rescue Beam** other_innate_stats: Ability Range: 6%; Radius: 6% -> Ability Range: 6%
- **Rescue Beam** stats_not_on_tooltip: Radius: 6% -> (blank)
- **Veil Walker** conditional_effects: [Passive, 15s cooldown] Status Effect Invisible: None; Invis Move Speed: 3.5m; Heal: 85 (+8 x boon); Invisibility Duration: 8s -> [Passive, 15s cooldown] Invis Move Speed: 3.5m; Heal: 85 (+8 x boon); Invisibility Duration: 8s
- **Veil Walker** unlisted_properties: AbilityDuration=16; InvisAlertWhenFading=1; InvisFadeToDuration=0.25; SpottedRadius=20m; RevealOnDamageDuration=0.5; RevealOnSpottedDuration=1.25; BonusSprintSpeed=0m -> AbilityDuration=16; InvisAlertWhenFading=1; InvisFadeToDuration=0.25; SpottedRadius=20m; RevealOnDamageDuration=0.5; RevealOnSpottedDuration=1.25
- **Cheat Death** stats_not_on_tooltip: (blank) -> Healing From Regen: -60% (flagged conditional)
- **Cheat Death** conditional_effects: [Passive, 90s cooldown] Death Immunity Duration: 4.5s; Damage Reduction: -60% -> [Passive, 90s cooldown] Death Immunity Duration: 4.5s; Damage Reduction: -60%; Incoming Healing: -60%
- **Cheat Death** enemy_effects: [Passive, 90s cooldown] Incoming Healing: -60% \| [Not on tooltip] Incoming Healing: -60% -> (blank)
- **Cheat Death** unlisted_properties: BonusMoveSpeed=0m -> (blank)
- **Colossus** stats_not_on_tooltip: (blank) -> Dash Distance: -22% (flagged conditional)
- **Colossus** conditional_effects: [Active, 37s cooldown] Bullet Resist: 35%; Spirit Resist: 35%; Melee Damage: 30%; Radius: 14m; Duration: 7s; Model Scale: 20% \| [Not on tooltip] Dash Distance: -22% -> [Active, 37s cooldown] Bullet Resist: 35%; Spirit Resist: 35%; Melee Damage: 30%; Radius: 14m; Duration: 7s; Model Scale: 20%
- **Divine Barrier** other_innate_stats: Ability Range: 10%; Radius: 10% -> Ability Range: 10%
- **Divine Barrier** stats_not_on_tooltip: Radius: 10% -> (blank)
- **Healing Tempo** other_innate_stats: Outgoing Healing: 25%; Health Regen Boost: 25% -> Outgoing Healing: 25%
- **Inhibitor** stats_not_on_tooltip: (blank) -> Healing From Regen: -40% (flagged conditional)
- **Inhibitor** conditional_effects: [Passive] Damage Penalty: -30%; Build Up Per Shot: 0.77 -> [Passive] Build Up Per Shot: 0.77
- **Inhibitor** enemy_effects: [Passive] Incoming Healing: -40%; Debuff Duration: 5s \| [Not on tooltip] Incoming Healing: -40% -> [Passive] Damage Penalty: -30%; Incoming Healing: -40%; Debuff Duration: 5s
- **Juggernaut** enemy_effects: [Effect] Fire Rate: 40%; Duration: 4s -> [Effect] Fire Rate Slow: 40%; Duration: 4s
- **Phantom Strike** conditional_effects: [Active, 35s cooldown] Status Effect Disarmed: None; Cast Range: 25m -> [Active, 35s cooldown] Cast Range: 25m
- **Mystic Expansion** other_innate_stats: Radius: 20% -> (blank)
- **Mystic Expansion** stats_not_on_tooltip: Radius: 20% -> (blank)
- **Rusted Barrel** enemy_effects: [Active, 16s cooldown] Fire Rate: 32%; Bullet Resist: -8% -> [Active, 16s cooldown] Fire Rate Slow: 32%; Bullet Resist Reduction: -8%
- **Spirit Strike** enemy_effects: [Passive, 8s cooldown] Spirit Damage: 40 (+0.372 x spirit power); Tech Armor Damage Reduction: -6% -> [Passive, 8s cooldown] Spirit Damage: 40 (+0.372 x spirit power); Spirit Resist Reduction: -6%
- **Arcane Surge** conditional_effects: [Passive] Ability Range: 12%; Ability Duration: 15%; Spirit Power: 20; Cast Window: 7s \| [Not on tooltip] Radius: 12% -> [Passive] Ability Range: 12%; Ability Duration: 15%; Spirit Power: 20; Cast Window: 7s
- **Bullet Resist Shredder** enemy_effects: [Passive] Bullet Resist: -10% -> [Passive] Bullet Resist Reduction: -10%
- **Improved Spirit** bonus_health: 75 -> (blank)
- **Improved Spirit** sprint_speed: 1 -> (blank)
- **Mystic Vulnerability** enemy_effects: [Passive] Tech Armor Damage Reduction: -8% -> [Passive] Spirit Resist Reduction: -8%
- **Spirit Sap** enemy_effects: [Active, 22s cooldown] Spirit Resist: -9%; Spirit Power: -30 -> [Active, 22s cooldown] Spirit Resist Reduction: -9%; Spirit Power: -30
- **Suppressor** enemy_effects: [Passive] Fire Rate: 28% -> [Passive] Fire Rate Slow: 28%
- **Decay** stats_not_on_tooltip: (blank) -> Healing From Regen: -55% (flagged conditional)
- **Decay** enemy_effects: [Active, 30s cooldown] Bleed Damage: 1.95% DPS (+0.003 x spirit power); Incoming Healing: -55% \| [Not on tooltip] Incoming Healing: -55% -> [Active, 30s cooldown] Bleed Damage: 1.95% DPS (+0.003 x spirit power); Incoming Healing: -55%
- **Disarming Hex** enemy_effects: [Active, 16s cooldown] Duration: 4.25s [Disarmed]; Bullet Resist: -13% -> [Active, 16s cooldown] Duration: 4.25s [Disarmed]; Bullet Resist Reduction: -13%
- **Greater Expansion** other_innate_stats: Radius: 30% -> Ability Range: 30%
- **Greater Expansion** stats_not_on_tooltip: Radius: 30% -> (blank)
- **Greater Expansion** conditional_effects: [Passive] Ability Range: 30% -> (blank)
- **Knockdown** other_innate_stats: Ability Range: 5%; Radius: 5% -> Ability Range: 5%
- **Knockdown** stats_not_on_tooltip: Radius: 5% -> (blank)
- **Radiant Regeneration** move_speed: 1.75 -> (blank)
- **Radiant Regeneration** conditional_effects: [Passive] Regeneration: 4HP/s (+0.025 x spirit power); Regeneration Duration: 7s \| [Effect, 6s cooldown] Healing Per Cast: 40 (+1.4 x boon); Duration: 3s -> [Passive] Regeneration: 4HP/s (+0.025 x spirit power); Regeneration Duration: 7s \| [Effect, 6s cooldown] Healing Per Cast: 40 (+1.4 x boon); Move Speed: 1.75m; Duration: 3s
- **Spirit Snatch** stats_not_on_tooltip: (blank) -> Spirit Resist Reduction: -12% (flagged conditional); Spirit Power: -25 (flagged conditional)
- **Spirit Snatch** enemy_effects: [Passive, 6s cooldown] Spirit Damage: 50 (+0.84 x spirit power) \| [Not on tooltip] Tech Armor Damage Reduction: -12%; Spirit Power: -25 -> [Passive, 6s cooldown] Spirit Damage: 50 (+0.84 x spirit power)
- **Superior Cooldown** conditional_effects: [Passive] Ability Cooldown Reduction: 20% -> (blank)
- **Superior Duration** other_innate_stats: (blank) -> Ability Duration: 28%
- **Superior Duration** conditional_effects: [Passive] Ability Duration: 28% -> (blank)
- **Surge of Power** stats_not_on_tooltip: (blank) -> Move Speed Penalty While Shooting Removed: 100 (flagged conditional); Move Speed Penalty While Zoomed Removed: 100 (flagged conditional)
- **Surge of Power** conditional_effects: [Passive, 14s cooldown] Imbued Ability Spirit Power: 28; Fire Rate Bonus: 20%; Move Speed: 1.75m; Move Speed Duration: 8s \| [Not on tooltip] move speed penalty while shooting reduction: 100; Move While Zoomed Speed Penalty Reduction Percent: 100 -> [Passive, 14s cooldown] Imbued Ability Spirit Power: 28; Fire Rate Bonus: 20%; Move Speed: 1.75m; Move Speed Duration: 8s
- **Arctic Blast** stats_not_on_tooltip: (blank) -> Move Speed Slow: 48% (flagged conditional)
- **Arctic Blast** enemy_effects: [Active, 24s cooldown] Damage: 175 (+0.6975 x spirit power); Freeze Duration: 1s \| [Not on tooltip] Move Speed Slow: 48% -> [Active, 24s cooldown] Damage: 175 (+0.6975 x spirit power); Freeze Duration: 1s
- **Cursed Relic** stats_not_on_tooltip: (blank) -> Skip Frames: 6 (flagged conditional)
- **Cursed Relic** conditional_effects: [Active, 55s cooldown] Status Effect EMP: None; Status Effect Disarmed: None; Duration: 3.25s; Cast Range: 20m; Damage Penalty: -25% \| [Not on tooltip] Skip Frames: 6 -> [Active, 55s cooldown] Duration: 3.25s; Cast Range: 20m; Damage Penalty: -25%
- **Escalating Exposure** enemy_effects: [Innate] Spirit Resist On Spirit Damage: -8% \| [Passive, 0.7s cooldown] Spirit Amp per Stack: 4.5% -> [Innate] Spirit Resist Reduction: -8% \| [Passive, 0.7s cooldown] Spirit Amp per Stack: 4.5%
- **Ethereal Shift** stats_not_on_tooltip: (blank) -> Float Speed: 2.5m (flagged conditional)
- **Ethereal Shift** enemy_effects: [Not on tooltip] Float Speed: 2.5m -> (blank)
- **Focus Lens** enemy_effects: [Active, 40s cooldown] Duration: 4.5s [EMP]; Damage On Expire: 35%; Spirit Resist: -9%; Resist Reduction Duration: 12s; Spirit Power: -30 -> [Active, 40s cooldown] Duration: 4.5s [EMP]; Damage On Expire: 35%; Spirit Resist Reduction: -9%; Resist Reduction Duration: 12s; Spirit Power: -30
- **Lightning Scroll** stats_not_on_tooltip: (blank) -> Move Speed Slow: 64%; Dash Distance: -12% (flagged conditional)
- **Lightning Scroll** enemy_effects: [Innate] Move Speed on Spirit Damage Slow: 24% \| [Passive] Stun Duration: 0.75s [Stun]; Damage: 150 (+0.35 x spirit power) \| [Not on tooltip] Move Speed Slow: 64%; Dash Distance: -12% -> [Innate] Move Speed on Spirit Damage Slow: 24% \| [Passive] Stun Duration: 0.75s [Stun]; Damage: 150 (+0.35 x spirit power)
- **Refresher** bullet_resist_pct: 15 -> (blank)
- **Refresher** spirit_resist_pct: 14 -> (blank)
- **Spirit Burn** other_innate_stats: Ability Range: 6%; Radius: 6% -> Ability Range: 6%
- **Spirit Burn** stats_not_on_tooltip: Radius: 6% -> Healing From Regen: -70% (flagged conditional)
- **Spirit Burn** enemy_effects: [Passive] Explosion Damage: 50; Damage Per Second: 24 (+0.06 x spirit power); Debuff Duration: 8s; Incoming Healing: -70% \| [Not on tooltip] Incoming Healing: -70% -> [Passive] Explosion Damage: 50; Damage Per Second: 24 (+0.06 x spirit power); Debuff Duration: 8s; Incoming Healing: -70%
- **Transcendent Cooldown** other_innate_stats: (blank) -> Item Cooldown Reduction: 25%
- **Transcendent Cooldown** conditional_effects: [Passive] Ability Cooldown Reduction: 25%; Item Cooldown Reduction: 25% -> (blank)
- **Vortex Web** other_innate_stats: Ability Range: 8%; Radius: 8% -> Ability Range: 8%
- **Vortex Web** stats_not_on_tooltip: Radius: 8% -> (blank)

### Units

- New columns in the sheet: health_second, health_third, health_growth_pct_per_minute, damage_absorbed_per_second, damage_growth_pct_per_minute, respawn_change_per_kill_seconds, respawn_min_seconds, note
- New: **Shrine**
- **Guardian** weapon_dps: 80 -> (blank)
- **Base Guardian** weapon_dps: 40 -> (blank)
- **Patron** health_gain_per_minute: (blank) -> 250
- **Trooper** weapon_dps: 34.951 -> (blank)
- **Trooper** dps_vs_players: (blank) -> 28
- **Trooper** dps_vs_troopers: (blank) -> 35
- **Melee Trooper** weapon_dps: 60 -> (blank)
- **Melee Trooper** dps_vs_players: (blank) -> 28
- **Melee Trooper** dps_vs_troopers: (blank) -> 35
- **Medic Trooper** weapon_dps: 34.951 -> (blank)
- **Medic Trooper** dps_vs_players: (blank) -> 28
- **Medic Trooper** dps_vs_troopers: (blank) -> 45
- **Sinner's Sacrifice** weapon_dps: 0 -> (blank)

### Rules

- New: **Guardian kill bounty, team total (souls)**
- New: **Walker kill bounty, team total (souls)**
- New: **Base Guardian kill bounty, team total (souls)**
- New: **Shrine kill bounty, team total (souls)**
- New: **Objective bounty: share to nearby players (%), rest split among all six**
- New: **Hero kill: average share of the bounty per participant, 1 in the kill**
- New: **Hero kill: average share of the bounty per participant, 2 in the kill**
- New: **Hero kill: average share of the bounty per participant, 3 in the kill**
- New: **Hero kill: average share of the bounty per participant, 4 in the kill**
- New: **Hero kill: average share of the bounty per participant, 5 in the kill**
- New: **Hero kill: average share of the bounty per participant, 6 in the kill**
- New: **Trooper kill: share of the bounty each player gets, 1 nearby**
- New: **Trooper kill: share of the bounty each player gets, 2 nearby**
- New: **Trooper kill: share of the bounty each player gets, 3 nearby**
- New: **Trooper kill: share of the bounty each player gets, 4 nearby**
- New: **Trooper kill: share of the bounty each player gets, 5 nearby**
- New: **Trooper kill: share of the bounty each player gets, 6 nearby**
- New: **Starting souls**
- New: **Item sell value (fraction of price)**
- New: **Hero kill bounty at 0:00 (souls)**
- New: **Hero kill bounty at full ramp (souls)**
- New: **Hero kill bounty reaches full ramp at (s)**
- New: **Bonus for each player's first kill (souls)**
- New: **Assist window (s)**
- New: **Killer's share relative to an assister's**
- New: **Trooper bounty at 0:00 (souls)**
- New: **Trooper bounty growth per minute (souls)**
- New: **Super trooper bounty multiplier**
- New: **First trooper wave at (s)**
- New: **Trooper wave interval, early (s)**
- New: **Trooper wave interval, late (s)**
- New: **Late wave interval starts at (min)**
- New: **Trooper wave interval, very late (s)**
- New: **Very late wave interval starts at (min)**
- New: **Trooper health multiplier, late game**
- New: **Trooper late-game health starts at (min)**
- New: **Neutral creep health growth per minute (%)**
- New: **Respawn time until 5 min (s)**
- New: **Respawn time at 20 min (s)**
- New: **Respawn time at 30 min (s)**
- New: **Respawn time at 40 min (s)**
- New: **Respawn time cap (s)**
- New: **Extra respawn time when not killed by a hero (s)**
- New: **Extra respawn time when richer than enemy average, minimum (s)**
- New: **Extra respawn time when richer than enemy average, maximum (s)**
- New: **Respawn time cut for the losing team when a Patron first falls (s)**
- New: **Soul Urn first spawn (s)**
- New: **Soul Urn spawn interval (s)**
- New: **Soul Urn reward at 0:00 (souls)**
- New: **Soul Urn reward growth per minute (souls)**
- New: **Soul Urn permanent buffs for the runner**
- New: **Soul Urn reward starts decaying after (s)**
- New: **Soul Urn reward decays over (s)**
- New: **Unstable Rift first spawn (s, plus or minus the window)**
- New: **Unstable Rift spawn window (s)**
- New: **Unstable Rift spawn interval (s)**
- New: **Unstable Rift warning before spawn (s)**
- New: **Unstable Rift reward at 0:00 (souls)**
- New: **Unstable Rift reward growth per minute (souls)**
- New: **Souls per level after the last boon**
- Removed: **Guardian kill bounty (souls)**
- Removed: **Walker kill bounty (souls)**
- Removed: **Base Guardian kill bounty (souls)**
- Removed: **Shrine kill bounty (souls)**
- Removed: **Objective bounty share for nearby players (%)**
- Removed: **Hero kill soul share, 1 player(s) sharing**
- Removed: **Hero kill soul share, 2 player(s) sharing**
- Removed: **Hero kill soul share, 3 player(s) sharing**
- Removed: **Hero kill soul share, 4 player(s) sharing**
- Removed: **Hero kill soul share, 5 player(s) sharing**
- Removed: **Hero kill soul share, 6 player(s) sharing**
- Removed: **Trooper kill soul share, 1 player(s) sharing**
- Removed: **Trooper kill soul share, 2 player(s) sharing**
- Removed: **Trooper kill soul share, 3 player(s) sharing**
- Removed: **Trooper kill soul share, 4 player(s) sharing**
- Removed: **Trooper kill soul share, 5 player(s) sharing**
- Removed: **Trooper kill soul share, 6 player(s) sharing**

### Powerups

- New table in the sheet (10 rows)

### Permanent_buffs

- New table in the sheet (11 rows)

## Build 6868 (2026-11-24)

Generated 2026-11-25T04:16:16+00:00; previous snapshot was build 6868.

### Investment

- New columns in the sheet: bonus_unit

## Build 6868 (2026-11-24)

Generated 2026-11-25T03:08:06+00:00; previous snapshot was build 6868.

### Rules

- New: **Rejuvenator duration (s)**
- New: **Rejuvenator drop count**
- New: **Rejuvenator time to drop (s)**
- New: **Rejuvenator revive delay (s)**
- New: **Rejuvenator revive health (%)**
- Removed: **Rejuvenator buff duration (s)**
- Removed: **Rejuvenator trooper health multiplier, level 1**
- Removed: **Rejuvenator trooper health multiplier, level 2**
- Removed: **Rejuvenator trooper health multiplier, level 3**
- Removed: **Rejuvenator respawn time multiplier, level 1**
- Removed: **Rejuvenator respawn time multiplier, level 2**
- Removed: **Rejuvenator respawn time multiplier, level 3**

## Build 6868 (2026-11-24)

Generated 2026-11-25T02:22:15+00:00; previous snapshot was build 6865.

### Heroes

- New columns in the sheet: bullets_per_burst, sustained_dps_level_1, dps_per_boon, reloads_single_bullets, falloff_end_damage_scale, crit_bonus_pct, move_speed_while_shooting_scale, dash_distance, air_dash_distance, base_melee_resist, spirit_scaling

### Abilities

- **Abrams / Shoulder Charge** internal_properties: CameraTurnRateMax=200; ChargeDragVerticalOffset=30; ChargeRadius=2.2; ChargeSpeedMax=30; CollidePlayersStopTime=0.3; SideMoveSpeedReduction=-65; SpeedInitial=18.75; TossUpMagnitude=0.5; TurnRateMax=140 -> ChargeDragVerticalOffset=30; ChargeRadius=2.2; ChargeSpeedMax=30; CollidePlayersStopTime=0.3; SideMoveSpeedReduction=-65; SpeedInitial=18.75; TossUpMagnitude=0.5; TurnRateMax=140
- **Apollo / Itani Lo Sahn** internal_properties: AbilityPostCastDuration=0.2; AirSpeedMax=70; CameraDistance=250; CasterLockDuration=1.8; DashAngleThreshold=89; DashRadius=7; DashSpeed=254; FallSpeedMax=1; GapDistanceToWall=180; GroundDashReductionPercent=-26; ImpactDamage=70 (+0.77 x spirit power); MoveSpeedPenaltyMaxSpeed=200; SideMoveSpeedReduction=-100; TechCleaveExpireTime=0.35; TimeScaleDebuff=70; TimerSoundDuration=1; TravelDistPctBeforeWallGapCheck=70; TurnRateMaxDuringCast=999; VacuumSpeed=10.16 -> AbilityPostCastDuration=0.2; AirSpeedMax=70; CasterLockDuration=1.8; DashAngleThreshold=89; DashRadius=7; DashSpeed=254; FallSpeedMax=1; GapDistanceToWall=180; GroundDashReductionPercent=-26; ImpactDamage=70 (+0.77 x spirit power); MoveSpeedPenaltyMaxSpeed=200; SideMoveSpeedReduction=-100; TechCleaveExpireTime=0.35; TimeScaleDebuff=70; TravelDistPctBeforeWallGapCheck=70; TurnRateMaxDuringCast=999; VacuumSpeed=10.16
- **Baba / Granny Long Legs** internal_properties: AirDashDistancePercent=20; BonusMeleeRange=2; ChargedJumpForwardForce=300; CrouchMoveSpeedBonus=3.5; DashDistancePercent=20; EndLaunchMaxLingerTime=3; GravityScalePercent=80; GroundPoundFallTimeReductionPercent=30; GroundPoundKnockUpDuration=0.3; GroundPoundKnockUpHeight=2.54; HeavyMeleeDashSlowPercent=-25; JumpSoundLayerVolumeMax=-4; JumpSoundLayerVolumeMin=-60; KickKnockbackDuration=0.45; LightKickKnockbackHeight=0.75; MaxJumpHeight=250; MeleeLifestealNonHeroPct=60; MinJumpHeight=75; MoveWhileShootingSpeedPenaltyReductionPercent=100; RisingGravityScalePercent=50 -> AirDashDistancePercent=20; BonusMeleeRange=2; ChargedJumpForwardForce=300; CrouchMoveSpeedBonus=3.5; DashDistancePercent=20; EndLaunchMaxLingerTime=3; GravityScalePercent=80; GroundPoundFallTimeReductionPercent=30; GroundPoundKnockUpDuration=0.3; GroundPoundKnockUpHeight=2.54; HeavyMeleeDashSlowPercent=-25; KickKnockbackDuration=0.45; LightKickKnockbackHeight=0.75; MaxJumpHeight=250; MeleeLifestealNonHeroPct=60; MinJumpHeight=75; MoveWhileShootingSpeedPenaltyReductionPercent=100; RisingGravityScalePercent=50
- **Billy / Bashdown** internal_properties: AbilityPostCastDuration=0.3; CameraTurnRateMax=2000; CountsAsLightMelee=1; ExplodeDelay=0.5; PlaceDistanceInFrontOfCaster=6.2; PullDownDuration=0.75; PullDownRange=3; TossForce=350; WaveStartRadius=0.5; WaveThickness=1 -> AbilityPostCastDuration=0.3; CountsAsLightMelee=1; ExplodeDelay=0.5; PlaceDistanceInFrontOfCaster=6.2; PullDownDuration=0.75; PullDownRange=3; TossForce=350; WaveStartRadius=0.5; WaveThickness=1
- **Billy / Rising Ram** internal_properties: AirControlAccelPercent=50; AirControlDashReductionPct=-70; AirControlDebuffDuration=1.5; AirControlPercent=50; AllowRamMultiple=1; CameraTurnRateMax=188; ChargeMultiHitRadius=1.5; ChargeRadius=2.54; ChargeSpeed=1200; ChargeStrikeDistance=165; GoingBackAwaySpeed=-100; GoingUpDistance=3.1; GoingUpEnemyDistancePercent=95; GoingUpSpeed=430; HoverGravityScale=0.75; KnockAwaySpeed=170; NearbyHeroKillDistance=10; ReduceCooldownOnHitPct=50; TimeBeforeGoUpForLagComp=0.1; TimeGoingUpEnemy=0.2; WorldImpactRadius=25 -> AirControlAccelPercent=50; AirControlDashReductionPct=-70; AirControlDebuffDuration=1.5; AirControlPercent=50; AllowRamMultiple=1; ChargeMultiHitRadius=1.5; ChargeRadius=2.54; ChargeSpeed=1200; ChargeStrikeDistance=165; GoingBackAwaySpeed=-100; GoingUpDistance=3.1; GoingUpEnemyDistancePercent=95; GoingUpSpeed=430; HoverGravityScale=0.75; KnockAwaySpeed=170; NearbyHeroKillDistance=10; ReduceCooldownOnHitPct=50; TimeBeforeGoUpForLagComp=0.1; TimeGoingUpEnemy=0.2; WorldImpactRadius=25
- **Calico / Leaping Slash** internal_properties: CameraDistance=550; DashAngleThreshold=89; DashRadius=2; DashSpeed=60.96; MoveSpeedPenaltyMaxSpeed=200; PostDashMaintainedVelocityRatio=0.15; SideMoveSpeedReduction=-90; SlashForwardOffset=1.5; SlashHeight=2.5 -> DashAngleThreshold=89; DashRadius=2; DashSpeed=60.96; MoveSpeedPenaltyMaxSpeed=200; PostDashMaintainedVelocityRatio=0.15; SideMoveSpeedReduction=-90; SlashForwardOffset=1.5; SlashHeight=2.5
- **Drifter / Eternal Night** internal_properties: AuraLingerDuration=0.001; BonusFireRate=0; BonusSprintAcceleration=12; DarkFactor=1; DistanceForMaxProjSpeed=200; DrifterNearbyRangeCheck=40; MaxProjectileSpeed=3000; MinProjectileSpeed=3000; PostProcessFadeInTime=0.2; PostProcessFadeOutTime=1; RevealDuration=3 -> AuraLingerDuration=0.001; BonusFireRate=0; BonusSprintAcceleration=12; DarkFactor=1; DistanceForMaxProjSpeed=200; DrifterNearbyRangeCheck=40; MaxProjectileSpeed=3000; MinProjectileSpeed=3000; RevealDuration=3
- **Dynamo / Singularity** internal_properties: CameraDistance=400; Speed=5.08; TickRate=0.25; TossAngle=45; TossSpeed=8.89 -> Speed=5.08; TickRate=0.25; TossAngle=45; TossSpeed=8.89
- **Grey Talon / Charged Shot** internal_properties: AirSpeedMax=4.1; CameraHeightOffset=20; CameraHorizontalOffset=15; FallSpeedMax=1.524; TechCleaveExpireTime=0.2 -> AirSpeedMax=4.1; FallSpeedMax=1.524; TechCleaveExpireTime=0.2
- **Holliday / Spirit Lasso** internal_properties: CameraPreviewDistance=200; CameraPreviewOffset=25; CameraPreviewSpeed=0.6; ExtraTargetConeAngle=60; ExtraTargetHorizontalOffset=30; FollowDistance=60; GrabExtraTargetsRadiusMult=2; LiftHeight=7; LiftHorizontal=-30; LiftInitialDelay=0.5; LiftInitialRisingSpeed=100; LiftInitialVelocityStart=500 -> ExtraTargetConeAngle=60; ExtraTargetHorizontalOffset=30; FollowDistance=60; GrabExtraTargetsRadiusMult=2; LiftHeight=7; LiftHorizontal=-30; LiftInitialDelay=0.5; LiftInitialRisingSpeed=100; LiftInitialVelocityStart=500
- **Infernus / Napalm** internal_properties: GrowthPerMeter=0.5; HeightOffGround=50; InitialWidth=1; ParticleRadiusMultiplier=1.15; TickRate=0.5 -> GrowthPerMeter=0.5; HeightOffGround=50; InitialWidth=1; TickRate=0.5
- **Kelvin / Ice Path** internal_properties: CameraDistance=250; ExplodeDamage=0 (+0.8 x spirit power); ExplodeInterval=0.15; ExplodeRadius=5; IcePathEdgeWidth=0.7; IcePathInterval=0.5; IcePathPullInStrength=20; IcePathShardRadius=1.2; MinHeight=20; ModifierRadius=5; MoveWhileShootingSpeedPenaltyReductionPercent=100; MoveWhileZoomedSpeedPenaltyReductionPercent=100; PopupForce=30; SlideScale=50; SlowResistancePercent=60 -> ExplodeDamage=0 (+0.8 x spirit power); ExplodeInterval=0.15; ExplodeRadius=5; IcePathEdgeWidth=0.7; IcePathInterval=0.5; IcePathPullInStrength=20; IcePathShardRadius=1.2; MinHeight=20; ModifierRadius=5; MoveWhileShootingSpeedPenaltyReductionPercent=100; MoveWhileZoomedSpeedPenaltyReductionPercent=100; PopupForce=30; SlideScale=50; SlowResistancePercent=60
- **Kelvin / Arctic Beam** internal_properties: BeamHealPerSecond=0 (+0.6 x spirit power); CameraDistance=250; ChannelSlowPercent=8; MinSlowPercent=24; PathWidth=1.1; TickRate=0.1 -> BeamHealPerSecond=0 (+0.6 x spirit power); ChannelSlowPercent=8; MinSlowPercent=24; PathWidth=1.1; TickRate=0.1
- **Lady Geist / Essence Bomb** internal_properties: BeepSoundBuildupCount=4; BeepSoundIntervalBias=0.55; BeepSoundMaxFrequency=0.1 -> (blank)
- **McGinnis / Mini Turret** internal_properties: AttackConeAngle=10; AttackSpeedMult=100; BossDamagePercentIncoming=50; BossDamagePercentOutgoing=30; MeleeResist=35; ModelScale=0.8; NonHeroDamagePercentOutgoing=65; TechResist=35; TickRate=0.5; TrackingSpeed=430; TurretAttackDelay=0.2; TurretAttackFalloffEnd=30; TurretAttackFalloffStart=20; TurretDeployTime=0.25 -> AttackConeAngle=10; AttackSpeedMult=100; BossDamagePercentIncoming=50; BossDamagePercentOutgoing=30; MeleeResist=35; NonHeroDamagePercentOutgoing=65; TechResist=35; TickRate=0.5; TrackingSpeed=430; TurretAttackDelay=0.2; TurretAttackFalloffEnd=30; TurretAttackFalloffStart=20; TurretDeployTime=0.25
- **Nurse Harrow / Lurking Terrors** internal_properties: AirControlAccelPercent=-50; AirDrag=3; BuildupDecayTime=10; BuildupLookAngle=80; BuildupLookAngleFull=55; BuildupLookAngleVertical=65; BuildupTickRate=0.075; CameraTurnRateMax=15; ConeAngle=180; ExtraSweepConeAngle=40; ExtraSweepOffsetBehindCaster=40; ExtraSweepRange=4; FacingAwayDamagePercent=50; FallSpeedMax=1; GazeLingerDuration=0.3; LaunchHeight=7.8; LookBuildupScalePercent=35; PitchScaleMax=1.3; PitchScaleMin=1; SlowLingerDuration=0.5; TargetMantleAttemptInterval=0.5; TickRate=0.15; VolScaleMax=1; VolScaleMin=0.35 -> AirControlAccelPercent=-50; AirDrag=3; BuildupDecayTime=10; BuildupLookAngle=80; BuildupLookAngleFull=55; BuildupLookAngleVertical=65; BuildupTickRate=0.075; ConeAngle=180; ExtraSweepConeAngle=40; ExtraSweepOffsetBehindCaster=40; ExtraSweepRange=4; FacingAwayDamagePercent=50; FallSpeedMax=1; GazeLingerDuration=0.3; LaunchHeight=7.8; LookBuildupScalePercent=35; PitchScaleMax=1.3; PitchScaleMin=1; SlowLingerDuration=0.5; TargetMantleAttemptInterval=0.5; TickRate=0.15; VolScaleMax=1; VolScaleMin=0.35
- **Paradox / Time Wall** internal_properties: AuraEffectDuration=2; TimeWallDepth=0.5; TimeWallDepthVisualScale=0.16; TimeWallFormationTime=0.5; TimeWallTimeScale=0.0001 -> AuraEffectDuration=2; TimeWallDepth=0.5; TimeWallFormationTime=0.5; TimeWallTimeScale=0.0001
- **Seven / Storm Cloud** internal_properties: BossDamageScale=0.5; CameraDistance=600; CloudHeight=120; DamageInterval=0.3; EndingSoonTime=2; ExpandTime=3.5; LightningStrikeDelay=0.25; LightningStrikeKnockBackForce=500; LightningStrikes=1 -> BossDamageScale=0.5; CloudHeight=120; DamageInterval=0.3; EndingSoonTime=2; ExpandTime=3.5; LightningStrikeDelay=0.25; LightningStrikeKnockBackForce=500; LightningStrikes=1
- **Shiv / Slice and Dice** internal_properties: AbilityPostCastDuration=0.2; CameraDistance=250; DashAngleThreshold=89; DashRadius=2.5; DashSpeed=60.96; MoveSpeedPenaltyMaxSpeed=200; SideMoveSpeedReduction=-100; TechCleaveExpireTime=0.35 -> AbilityPostCastDuration=0.2; DashAngleThreshold=89; DashRadius=2.5; DashSpeed=60.96; MoveSpeedPenaltyMaxSpeed=200; SideMoveSpeedReduction=-100; TechCleaveExpireTime=0.35
- **Shiv / Killing Blow** internal_properties: AbilityPostCastDuration=0.15; BonusAbilityResource=10; CameraDistance=400; EnemyHealthPercentBuffer=3; FailedExecuteCooldownPenalty=30; MinTimeToTarget=0.5; MoveSpeedToTarget=30; RageDrainDelayDuration=12; RageDrainRate=0.25; RagePerHeavyMelee=2.8538; RagePerLightMelee=1.5566; RagePerSpiritDamage=0.0145; RagePerWeaponDamage=0.0159; RecastWindow=12; SlashRange=90 -> AbilityPostCastDuration=0.15; BonusAbilityResource=10; EnemyHealthPercentBuffer=3; FailedExecuteCooldownPenalty=30; MinTimeToTarget=0.5; MoveSpeedToTarget=30; RageDrainDelayDuration=12; RageDrainRate=0.25; RagePerHeavyMelee=2.8538; RagePerLightMelee=1.5566; RagePerSpiritDamage=0.0145; RagePerWeaponDamage=0.0159; RecastWindow=12; SlashRange=90
- **Silver / Boot Kick** internal_properties: AbilityPostCastDuration=0.25; AirDrag=0.8; CameraTurnRateMax=188; EnemyPushForceAway=300; EnemyPushForceUp=300; FallSpeedMax=20; LeapForwardOffset=2.5; LeapRadius=1.7; SelfPushForceCameraAway=600; SelfPushForceUp=200; SuccessInputWindow=0.3; TimeScaleDebuff=95 -> AbilityPostCastDuration=0.25; AirDrag=0.8; EnemyPushForceAway=300; EnemyPushForceUp=300; FallSpeedMax=20; LeapForwardOffset=2.5; LeapRadius=1.7; SelfPushForceUp=200; SuccessInputWindow=0.3; TimeScaleDebuff=95
- **Silver / Lycan Curse** internal_properties: AbilityChargesConditionally=1; AbilityPostCastDuration=0.5; AutoActivateHealthThreshold=20; BonusDurationOnBullet=0.15; BonusDurationOnHeavyMelee=1.5; BonusDurationOnLightMelee=0.5; BonusDurationPerHealthPercentLost=0.1; CameraTurnRateMax=188; EndingWarningSoundDuration=3; HeadshotResist=-20; LowHealthFraction=30; LowHealthRageBonus=40 (+1.8 x boon); MaxRage=100 (+9.4 x boon); MaxStacks=15; RagePerDamage=0.255; RagePercentagePerSecondInCombat=1; RagePercentagePerSecondOutOfCombat=-3; ReadyDuration=3; StackDuration=5 -> AbilityChargesConditionally=1; AbilityPostCastDuration=0.5; AutoActivateHealthThreshold=20; BonusDurationOnBullet=0.15; BonusDurationOnHeavyMelee=1.5; BonusDurationOnLightMelee=0.5; BonusDurationPerHealthPercentLost=0.1; HeadshotResist=-20; LowHealthFraction=30; LowHealthRageBonus=40 (+1.8 x boon); MaxRage=100 (+9.4 x boon); MaxStacks=15; RagePerDamage=0.255; RagePercentagePerSecondInCombat=1; RagePercentagePerSecondOutOfCombat=-3; ReadyDuration=3; StackDuration=5
- **Silver / Silver (Transformed) / Mauling Leap** internal_properties: AbilityPostCastDuration=0.1; AllowRamMultiple=1; CameraTurnRateMax=188; LeapForwardOffset=0.3; LeapMultiHitRadius=1.5; LeapRadius=2.8; TickRate=0.5; WorldImpactRadius=25 -> AbilityPostCastDuration=0.1; AllowRamMultiple=1; LeapForwardOffset=0.3; LeapMultiHitRadius=1.5; LeapRadius=2.8; TickRate=0.5; WorldImpactRadius=25
- **Venator / Consecrating Grenade** internal_properties: AbilityPostCastDuration=0.15; BounceGrenadeSpeed=1100; BounceLifetime=0.5; BurnLingerDuration=0.15; CameraTurnRateMax=15; HealAmpRegenPenaltyPercent=-30; PreBounceLifetime=15; TickRate=0.2 -> AbilityPostCastDuration=0.15; BounceGrenadeSpeed=1100; BounceLifetime=0.5; BurnLingerDuration=0.15; HealAmpRegenPenaltyPercent=-30; PreBounceLifetime=15; TickRate=0.2
- **Vindicta / Crow Familiar** internal_properties: AbilityPostCastDuration=0.2; TickRate=1; VisualSplashRadius=4 -> AbilityPostCastDuration=0.2; TickRate=1
- **Vindicta / Assassinate** internal_properties: BonusGoldOnKill=250; LowHealthEnemyThresholdPct=50; MaxSoundDistance=2000; MoveSpeed=4; Range=1000; ShotRadius=4; ViewPunch=2.5 -> BonusGoldOnKill=250; LowHealthEnemyThresholdPct=50; MoveSpeed=4; Range=1000; ShotRadius=4; ViewPunch=2.5
- **Viscous / Goo Ball** internal_properties: AccelerationPercentage=-60; AirJumpForce=500; BallHitRadius=1.8; BallOffset=50; BreakablePropDamageRadius=75; CastWhileRolling=1; FrictionPercentage=-85; JumpForce=500; KnockForce=400; MoveSpeedMax=7; ParticleRadiusMultiplier=1.2; TickRate=0.25 -> AccelerationPercentage=-60; AirJumpForce=500; BallHitRadius=1.8; BallOffset=50; BreakablePropDamageRadius=75; CastWhileRolling=1; FrictionPercentage=-85; JumpForce=500; KnockForce=400; MoveSpeedMax=7; TickRate=0.25
- **Wraith / Project Mind** internal_properties: CameraDistance=250; TrailInterval=0.1 -> TrailInterval=0.1

## Build 6865 (2026-11-23)

Initial snapshot, generated 2026-11-24T09:16:59+00:00: 44 heroes, 176 abilities, 156 items.
