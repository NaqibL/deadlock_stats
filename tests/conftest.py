import copy
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

LOC = {
    "CitadelCategoryWeapon": "Weapon", "CitadelCategoryArmor": "Vitality", "CitadelCategoryTech": "Spirit",
    "hero_one_role": "Charges <span class=\"highlight\">in</span>",
    "Attribute_Close": "Close Range",
    "ability_drain_desc": "Drain health, dealing {g:citadel_inline_attribute:'SpiritDPS'}.<br>Lasts a while.",
    "ability_drain_t3_desc": "<span class=\"highlight\">+22</span> DPS &amp; more",
    "InlineAttribute_SpiritDPS": "spirit damage over time",
    "DPS_label": "Damage Per Second", "AbilityCooldown_label": "Cooldown", "AbilityCooldown_postfix": "s",
    "Radius_label": "Radius", "Radius_postfix": "m", "SlowPercent_label": "Move Speed", "SlowPercent_postfix": "%",
    "BonusHealth_label": "Bonus Health", "BaseAttackDamagePercent_label": "Weapon Damage",
    "BaseAttackDamagePercent_postfix": "%", "BulletArmorReduction_label": "Bullet Resist",
    "BulletArmorReduction_postfix": "%", "GunTag_Shotgun": "Shotgun", "Tag_A": "Tank", "Tag_B": "Brawler",
    "TechResist_label": "Spirit Resist", "guardian_unit": "Guardian",
    "Citadel_ModBonus_WeaponInvestmentDesc": "Weapon Damage Increases", "ClipSize_label": "Clip Size", "TechResist_postfix": "%",
    "item_cond_desc": "Above {s:LifeThreshold}% health, deal more damage.",
}


def _hero(hero_id, name, hero_type="Brawler", **extra):
    hero = {
        "Id": hero_id, "Name": name, "Type": hero_type, "Role": "hero_one_role", "IsDisabled": False,
        "InDevelopment": False, "MaxHealth": 800.0, "BaseHealthRegen": 1.5, "LightMeleeDamage": 50,
        "HeavyMeleeDamage": 116, "MaxMoveSpeed": 6.4, "SprintSpeed": 1.6, "Stamina": 3,
        "StaminaCooldown": 4.5000045, "StaminaRegenPerSecond": 0.222222,
        "LevelScaling": {"BulletDamage": 0.1, "MaxHealth": 49.0, "TechPower": 1.1,
                         "LightMeleeDamage": 1.738, "HeavyMeleeDamage": 4.0322},
        "Weapon": {"BulletDamage": 3.78, "BulletsPerShot": 9, "RoundsPerSecond": 1.5873, "ClipSize": 9,
                   "ReloadTime": 0.3525, "BulletSpeed": 609.6, "FalloffStartRange": 17.0, "FalloffEndRange": 40.0,
                   "DPS": 54.0, "SustainedDPS": 32.069, "BulletsPerBurst": 1, "ReloadSingle": True, "WeaponTypes": ["Attribute_Close"]},
        "CritDamageBonusPercent": 0.0, "GroundDashDistanceInMeters": 10.0, "SpiritScaling": {"ClipSize": 0.5, "Zero": 0},
        "BoundAbilities": {str(n): {"Name": f"{name} {n}", "Key": "ability_drain" if n == 1 else f"ability_{hero_id}_{n}"}
                           for n in (1, 2, 3, 4)},
    }
    hero.update(extra)
    return hero


def _ability(name):
    return {"Key": name, "Name": name, "IsDisabled": False, "AbilityCooldown": 0, "Upgrades": [{}, {}, {}]}


@pytest.fixture
def primary():
    heroes = {
        "hero_one": _hero(1, "One"),
        "hero_live_dev": _hero(2, "LiveDev", InDevelopment=True),
        "hero_one_transformed": _hero(None, "One (Transformed)"),
        "hero_disabled": _hero(3, "Gone", IsDisabled=True),
        "hero_dummy": _hero(4, "Dummy", hero_type=None),
    }
    heroes["hero_one_transformed"]["BoundAbilities"]["2"] = {"Name": "Maul", "Key": "ability_maul"}
    heroes["hero_one_transformed"]["BoundAbilities"]["1"] = heroes["hero_one"]["BoundAbilities"]["1"]
    abilities = {key: _ability(key) for hero in heroes.values() for key in
                 (bound["Key"] for bound in hero["BoundAbilities"].values())}
    abilities["ability_maul"] = _ability("Maul")
    abilities["ability_drain"] = {
        "Key": "ability_drain", "Name": "Drain", "IsDisabled": False,
        "AbilityCooldown": {"Value": 42.0, "Scale": {"Value": 1, "Type": "cooldown"}},
        "AbilityCooldownBetweenCharge": -1.0,
        "DPS": {"Value": 22, "Scale": {"Value": 0.6, "Type": "spirit"}},
        "Radius": {"Value": 8, "Scale": {"Value": 1, "Type": "radius"}},
        "Reach": {"Value": 14, "Scale": [{"Value": 0.14, "Type": "spirit"}, {"Value": 1, "Type": "range"}]},
        "TickRate": 0.25,
        "Upgrades": [{"AbilityCooldown": -20.0}, {"SlowPercent": 24},
                     {"DPS": {"Value": 22, "Scale": {"Value": 0.12, "Type": "spirit"}}, "Radius": "2m"}],
    }
    cards = {"hero_one": {"1": {
        "Key": "ability_drain", "Name": "Drain", "DescKey": "ability_drain_desc",
        "Info1": {"Main": {"Props": [{"Key": "DPS", "Name": "Damage Per Second", "Value": 22,
                                      "Scale": {"Value": 0.6, "Type": "spirit"}, "Type": "tech_damage"},
                                     {"Key": "Reach", "Name": "Reach", "Value": 14, "Type": "distance",
                                      "Scale": [{"Value": 0.14, "Type": "spirit"}, {"Value": 1, "Type": "range"}]}]},
                  "Alt": [{"Key": "Hidden", "Name": "Hidden", "Value": 0, "Type": "healing"}]},
        "Upgrades": [{}, {}, {"DescKey": "ability_drain_t3_desc"}],
        "Headers": {"AbilityCooldown": {"Name": "Cooldown", "Value": 42.0, "Type": "cooldown"}},
    }}}
    items = {
        "upgrade_health": {"Name": "Extra Health", "Cost": 800, "Tier": 1, "Slot": "Armor", "Activation": "Passive",
                           "Components": None, "IsDisabled": False, "StreetBrawl": False, "IsImbue": False,
                           "BonusHealth": 210},
        "upgrade_fort": {"Name": "Fortitude", "Cost": 3200, "Tier": 3, "Slot": "Armor", "Activation": "Passive",
                         "Components": ["upgrade_health"], "IsDisabled": False, "StreetBrawl": False, "IsImbue": False,
                         "BonusHealth": 300},
        "upgrade_hollow": {"Name": "Hollow Point", "Cost": 3200, "Tier": 3, "Slot": "Weapon", "Activation": "Press",
                           "Components": None, "IsDisabled": False, "StreetBrawl": False, "IsImbue": False,
                           "BonusHealth": 125, "BaseAttackDamagePercent": 35, "BulletArmorReduction": -10,
                           "LifeThreshold": 65, "ActiveBonusMoveSpeed": "3.0m", "TechResist": 14,
                           "SlowPercent": 30, "EnhancedOnly": 75},
        "armor_upgrade_t1": {"Name": None, "Cost": 800, "Tier": 1, "Slot": "Armor", "IsDisabled": False, "StreetBrawl": False},
        "upgrade_brawl": {"Name": "Brawl Only", "Cost": 800, "Tier": 1, "Slot": "Tech", "IsDisabled": False, "StreetBrawl": True},
        "upgrade_off": {"Name": "Disabled", "Cost": 800, "Tier": 1, "Slot": "Tech", "IsDisabled": True, "StreetBrawl": False},
        "upgrade_t5": {"Name": "Legendary", "Cost": 9999, "Tier": 5, "Slot": "Tech", "IsDisabled": False, "StreetBrawl": False},
    }
    item_cards = {
        "upgrade_health": {"Info1": {"Type": "Innate", "Main": [{"Key": "BonusHealth", "Value": 210, "Type": "health"}], "Alt": []}, "Other": {}},
        "upgrade_fort": {"Info1": {"Type": "Innate", "Main": [{"Key": "BonusHealth", "Value": 300, "Type": "health"}], "Alt": []}, "Other": {}},
        "upgrade_hollow": {
            "Info1": {"Type": "Innate", "Main": [], "Alt": [{"Key": "BonusHealth", "Value": 125, "Type": "health"}]},
            "Info2": {"Type": "Passive", "DescKey": "#item_cond_desc", "Cooldown": None, "Main": [
                {"Key": "BaseAttackDamagePercent", "Value": 35, "Type": "bullet_damage", "UsageFlags": "ConditionallyApplied"},
                {"Key": "BulletArmorReduction", "Value": -10, "Type": "bullet_armor_down", "UsageFlags": "ConditionallyApplied"}], "Alt": []},
            "Info3": {"Type": "Active", "Cooldown": 16.0, "Main": [
                {"Key": "ActiveBonusMoveSpeed", "Value": "3.0m", "Type": "move_speed", "UsageFlags": "ConditionallyApplied"}], "Alt": []},
            "Other": {"LifeThreshold": {"Key": "LifeThreshold", "Value": 65},
                      "TechResist": {"Key": "TechResist", "Value": 14, "Type": "tech_armor_up"},
                      "SlowPercent": {"Key": "SlowPercent", "Value": 30, "Type": "slow"},
                      "EnhancedOnly": {"Key": "EnhancedOnly", "Value": 75},
                      "ChannelMoveSpeed": {"Key": "ChannelMoveSpeed", "Value": -1}},
        },
    }
    world = {
        "investment": {"ItemInvestments": {
            "Weapon": [{"GoldThreshold": 800, "Bonus": 9}, {"GoldThreshold": 1600, "Bonus": 12}],
            "Vitality": [{"GoldThreshold": 800, "Bonus": 9}], "Spirit": [{"GoldThreshold": 800, "Bonus": 7}]}},
        "soul_unlocks": [{"RequiredSouls": 0, "AbilityUnlocks": 1},
                         {"RequiredSouls": 200, "PowerIncrease": True, "AbilityPoints": 1},
                         {"RequiredSouls": 500, "PowerIncrease": True, "AbilityUnlocks": 1}],
        "npcs": {
            "npc_boss_tier1": {"MaxHealth": 5500, "PlayerDPS": 116.0, "TrooperDPS": 35.0, "LocUnitName": "guardian_unit",
                               "Weapon": {"BulletDamage": 16, "DPS": 80.0},
                               "IntrinsicModifiers": [{"ABILITY_DAMAGE_REDUCTION_PERCENT": 0.0, "BULLET_ARMOR_DAMAGE_RESIST": 10}]},
            "neutral_trooper_weak": {"MaxHealth": 142, "GoldReward": 45, "GoldRewardBonusPercentPerMinute": 1.08,
                                     "IntrinsicModifiers": [{"BULLET_DAMAGE_REDUCTION_PERCENT": 50.0}]},
            "npc_super_neutral": {"StartingHealth": 15600, "HealthGainPerMinute": 234},
        },
        "misc": {"neutral_camp_weak": {"InitialSpawnDelayInSeconds": 120, "SpawnIntervalInSeconds": 85}},
        "generic": {"ItemPricePerTier": [0, 800, 1600, 3200, 6400, 9999],
                    "ObjectiveParams": {"Tier1GoldKill": 1375, "NearPlayerSplitPct": 25.0},
                    "HeroKillGoldShareFrac": [1.25, 0.575], "RejuvParams": {"RejuvinatorBuffDuration": 180}},
    }
    return {
        **world,
        "heroes": heroes, "abilities": abilities, "ability_cards": cards, "items": items, "item_cards": item_cards,
        "loc": dict(LOC), "version": {"ClientVersion": "6865", "VersionDate": "Nov 23 2026"},
        "commit": {"hash": "abc123", "date": "2026-11-23T19:47:32+00:00"},
    }


@pytest.fixture
def raw(primary):
    """Raw game files that agree with the ``primary`` fixture."""
    heroes = {"generic_data_type": "CitadelHeroData_t"}
    abilities = {}
    for key in ("hero_one", "hero_live_dev"):
        hero = primary["heroes"][key]
        heroes[key] = {
            "m_eHeroDevelopmentState": "EHeroDevState_Release", "m_bDisabled": False,
            "m_mapStartingStats": {"EMaxHealth": 800.0},
            "m_mapStandardLevelUpUpgrades": {"MODIFIER_VALUE_BASE_HEALTH_FROM_LEVEL": 49.0,
                                             "MODIFIER_VALUE_BASE_BULLET_DAMAGE_FROM_LEVEL": 0.1,
                                             "MODIFIER_VALUE_TECH_POWER": 1.1},
            "m_mapBoundAbilities": {"ESlot_Weapon_Primary": "weapon_" + key,
                                    **{f"ESlot_Signature_{n}": hero["BoundAbilities"][str(n)]["Key"] for n in (1, 2, 3, 4)}},
        }
        abilities["weapon_" + key] = {"m_mapWeaponInfos": {"primary": {"m_flBulletDamage": 3.78, "m_iBullets": 9, "m_iClipSize": 9}}}
    heroes["hero_dummy"] = {"m_eHeroDevelopmentState": "EHeroDevState_DebugOnly", "m_bDisabled": False}
    for key in primary["abilities"]:
        abilities[key] = {"m_mapAbilityProperties": {}}
    abilities["ability_drain"] = {"m_mapAbilityProperties": {
        "AbilityCooldown": {"m_strValue": 42.0},
        "DPS": {"m_strValue": 22, "m_subclassScaleFunction": {"_class": "scale_function_tech_damage", "m_flStatScale": 0.6}},
        "Radius": {"m_strValue": "8m"},
        "Reach": {"m_strValue": "551.18", "m_subclassScaleFunction": {"m_eSpecificStatScaleType": "ETechPower", "m_flStatScale": 0.14}},
        "TickRate": {"m_strValue": "0.25"},
    }}
    slots = {"Armor": "EItemSlotType_Armor", "Weapon": "EItemSlotType_WeaponMod", "Tech": "EItemSlotType_Tech"}
    for key in ("upgrade_health", "upgrade_fort", "upgrade_hollow"):
        item = primary["items"][key]
        abilities[key] = {
            "m_iItemTier": f"EModTier_{item['Tier']}", "m_eItemSlotType": slots[item["Slot"]],
            "m_mapAbilityProperties": {k: {"m_strValue": str(v)} for k, v in item.items()
                                       if isinstance(v, (int, float, str)) and not isinstance(v, bool)
                                       and k not in ("Name", "Cost", "Tier", "Slot", "Activation", "EnhancedOnly")},
        }
    hollow = abilities["upgrade_hollow"]["m_mapAbilityProperties"]
    hollow["TechResist"].update(m_eProvidedPropertyType="MODIFIER_VALUE_TECH_RESIST", m_eStatsUsageFlags="")
    hollow["SlowPercent"].update(m_eProvidedPropertyType="MODIFIER_VALUE_SLOW", m_strCSSClass="slow",
                                 m_eStatsUsageFlags="ConditionallyApplied")
    heroes["hero_one"].update(m_strGunTag="#GunTag_Shotgun", m_vecHeroTags=["#Tag_A", "#Tag_B"])
    return {"version": {"ClientVersion": "6865"}, "heroes": heroes, "abilities": abilities,
            "generic": {"m_nItemPricePerTier": [0, 800, 1600, 3200, 6400, 9999]}}


@pytest.fixture
def tables(primary):
    from src import abilities, heroes, items
    hero_rows, _ = heroes.build_heroes(primary)
    ability_rows, _ = abilities.build_abilities(primary)
    item_rows, _ = items.build_items(primary)
    return copy.deepcopy((hero_rows, ability_rows, item_rows))
