# Build report

- Game build: **6868** (2026-11-24)
- Source: https://github.com/deadlock-wiki/deadlock-data at `d82561117154` (2026-11-24T23:48:59+00:00)
- Generated: 2026-11-25T04:16:16+00:00
- Rows: 44 heroes, 176 hero abilities (+3 alternate-form abilities), 156 items (53 weapon, 54 vitality, 49 spirit)

## Validation

- All rules passed with no warnings.

## Cross-check against the raw game files

- Raw files at game build 6868; 5705 values compared, 0 disagreement(s).

| Compared | Values |
|---|---|
| hero roster | 1 |
| hero base_health | 44 |
| hero health_per_boon | 44 |
| hero bullet_damage | 44 |
| hero bullet_damage_per_boon | 44 |
| hero pellets_per_shot | 44 |
| hero clip_size | 44 |
| hero spirit_power_per_boon | 44 |
| hero ability slots | 176 |
| ability properties | 2908 |
| ability properties (spirit scaling) | 202 |
| item tier | 156 |
| item cost | 156 |
| item category | 156 |
| item enabled | 156 |
| item properties | 1456 |
| item properties (spirit scaling) | 30 |

## Excluded heroes

- **disabled in the game files** (21): `hero_testhero`, Boho, Bomber, Cadence, Druid, Fathom, Fortuna, Graf, Gunslinger, Kali, Opera, Raven, Rutger, Shield Guy, Skyrunner, Swan, The Boss, Thumper, Trapper, Vandal, Wrecker
- **no hero type (test or debug hero)** (2): Generic Person, TargetDummy
- **no hero id (alternate form of another hero, not separately pickable)** (1): Silver (Transformed)

## Excluded items and item-like entries

- **no English name (placeholder, base class or non-item ability)** (83): `ability_item_pickup_effects`, `armor_upgrade_base`, `armor_upgrade_t1`, `armor_upgrade_t2`, `armor_upgrade_t3`, `armor_upgrade_t4`, `armor_upgrade_t5`, `cosmetic_ability_emote`, `cosmetic_ability_voting_poster`, `item_projectile_test_01`, `item_projectile_test_02`, `item_projectile_test_03`, `item_projectile_test_04`, `item_projectile_test_05`, `item_projectile_test_06`, `tech_upgrade_base`, `tech_upgrade_t1`, `tech_upgrade_t2`, `tech_upgrade_t3`, `tech_upgrade_t4`, `tech_upgrade_t5`, `upgrade_active_bullet_shield`, `upgrade_aerial_assault`, `upgrade_aoe_silence`, `upgrade_aoe_smoke_bomb`, `upgrade_aoe_tech_shield`, `upgrade_arcane_eater`, `upgrade_arcane_medallion`, `upgrade_attack_speed_1`, `upgrade_attack_speed_2`, `upgrade_base`, `upgrade_belt_fed_magazine`, `upgrade_bonus_ability_charge_3`, `upgrade_bullet_damage_reduction_aura`, `upgrade_burst_fire_actuator`, `upgrade_camouflage`, `upgrade_charge_mastery`, `upgrade_charmed_wraps`, `upgrade_clip_size_2`, `upgrade_clip_size_3`, `upgrade_clip_size_fixed_t3`, `upgrade_clip_size_fixed`, `upgrade_cloaking_device`, `upgrade_disarm`, `upgrade_double_jump`, `upgrade_drum_magazine`, `upgrade_duration_extender`, `upgrade_fire_rate_aura`, `upgrade_frenzy`, `upgrade_full_spectrum`, `upgrade_galvanic_storm`, `upgrade_health_regen_1`, `upgrade_health_regen_aura`, `upgrade_high_impact_armor`, `upgrade_imbued_ability`, `upgrade_long_range_slowing_tech`, `upgrade_magic_clarity`, `upgrade_mod_disruptor`, `upgrade_nearby_enemy_boost`, `upgrade_predator_precision`, `upgrade_proc_disarm`, `upgrade_proc_tech_damage`, `upgrade_quarantine`, `upgrade_regenerative_armor`, `upgrade_reload_speed`, `upgrade_slow_immunity`, `upgrade_slowing_tech`, `upgrade_small_attack_speed`, `upgrade_stabilizer`, `upgrade_stasis_bomb`, `upgrade_tech_cleave`, `upgrade_toughness_3`, `upgrade_weapon_detention_ammo`, `upgrade_weapon_eater`, `upgrade_weapon_instant_reload`, `upgrade_weapon_overdrive_clip`, `upgrade_weapon_power_and_health_drain`, `weapon_upgrade_base`, `weapon_upgrade_t1`, `weapon_upgrade_t2`, `weapon_upgrade_t3`, `weapon_upgrade_t4`, `weapon_upgrade_t5`
- **no shop category** (2): Eat Candy, Snowball
- **disabled in the game files** (22): Aerial Supremacy, Ammo Scavenger, Ancient Shield, Apex Combat, Bullet Armor, Conjure Missiles, Endless Magazine, Enduring Spirit, Glass Cannon v2, Haunting Scream, Hex-Sealed Knuckles, Hexafoil Ward, Majestic Leap - Disabled, Patron's Healing, Rebirth, Shadow Step, Silencer, Soul Explosion, Soul Rebirth, Spirit Armor, Timeless Emblem, Toughness
- **Street Brawl mode only** (17): Celestial Blessing, Cloak of Opportunity, Electric Slippers, Eternal Gift, Frostbite Charm, Haunting Shot, Infinite Rounds, Mystic Conduit, Mystical Piano, Nullification Burst, Omnicharge Signet, Prism Blast, Runed Gauntlets, Seraphim Wings, Shadow Strike, Shrink Ray, Unstable Concoction
