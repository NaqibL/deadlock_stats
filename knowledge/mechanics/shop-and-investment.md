# Shop, item slots and investment bonuses

Generated from the game files at build 6868 and Valve's patch notes. Everything below is quoted from a source, not interpreted. Patch notes describe the game as of their date: read newest first, and treat an older line as history once a newer one changes the same thing.

## What the game itself says

- Additional Protection (`CitadelComponentGroup_EAdditionalProtection`)
- Anti-Healing (`CitadelComponentGroup_EAntiHealing`)
- Bullet Protection (`CitadelComponentGroup_EBulletProtection`)
- Bullet Velocity (`CitadelComponentGroup_EBulletVelocity`)
- Burst Damage (`CitadelComponentGroup_EBurstDamage`)
- Ability Charges (`CitadelComponentGroup_ECharges`)
- Crowd Control (`CitadelComponentGroup_ECrownControl`)
- Ability Duration (`CitadelComponentGroup_EDuration`)
- Headshot Enthusiasts (`CitadelComponentGroup_EHeadshotEnthusiasts`)
- Lifestealing (`CitadelComponentGroup_ELifesteal`)
- Magic Vulnerability (`CitadelComponentGroup_EMagicVulnerability`)
- Melee Lifesteal (`CitadelComponentGroup_EMelee`)
- Melee Spirit (`CitadelComponentGroup_EMeleeSpirit`)
- Misc Passive (`CitadelComponentGroup_EMisc`)
- Movement & Agility (`CitadelComponentGroup_EMovementAndAgility`)
- Rate of Fire (`CitadelComponentGroup_ERateOfFire`)
- Revitalization (`CitadelComponentGroup_ERevitalization`)
- Slowing Bullets (`CitadelComponentGroup_ESlowingBullets`)
- Slowing Magic (`CitadelComponentGroup_ESlowingMagic`)
- Spirit Protection (`CitadelComponentGroup_ESpiritProtection`)
- Ability Range (`CitadelComponentGroup_ESpiritRange`)
- Spirit Slinger (`CitadelComponentGroup_ESpiritSlinger`)
- Bruisers & Brawlers (`CitadelComponentGroup_ETankingBullets`)
- Assassin's Toolkit (`CitadelComponentGroup_EWeaponRange`)
- Ability Improvements (`CitadelShopFilterCategory_AbilityImprovements`)
- Additional Damage (`CitadelShopFilterCategory_AdditionalDamage`)
- Gun Improvements (`CitadelShopFilterCategory_GunImprovements`)
- Gun Reductions (`CitadelShopFilterCategory_GunReductions`)
- Popular Items (`CitadelShopFilterCategory_Popular`)
- Status Effects (`CitadelShopFilterCategory_StatusEffects`)
- Vulnerability (`CitadelShopFilterCategory_Vulnerability`)
- Items shown must match ALL filters (`CitadelShopFilter_AndTooltip`)
- Active Filters: (`CitadelShopFilter_FiltersActive`)
- Items shown can match ANY filter (`CitadelShopFilter_OrTooltip`)
- Backspace to Search (`CitadelShopFilter_SearchPlaceholder`)
- Popular Items (`CitadelShopFilter_ShowPopularItems`)
- Popular Items (`CitadelShopFiltered_PopularItems`)
- Item Filters: (`CitadelShopFiltered_Title`)
- Search Items (`CitadelShopSearch`)
- Generated from match data (`CitadelShop_PopularItemGenerated`)
- Try searching by Item Name or by stat such as Ammo, Lifesteal or Spirit Power (`CitadelShop_SearchExampleAlt`)
- Search Examples: (`CitadelShop_SearchExampleLine1`)
- Name: Phantom Strike (`CitadelShop_SearchExampleLine2`)
- Property: Bullet Resist (`CitadelShop_SearchExampleLine3`)
- Upgrades From: (`Citadel_ComponentRequired`)
- Currently Used in: (`Citadel_ComponentUseIn`)
- [Open Hero Sheet]Shop & Upgrade (`Citadel_Dead_ShopReminder`)
- You've unlocked an extra slot for killing one of the Enemy Walkers (`Citadel_FlexSlotUnlockedSlot02`)
- You've unlocked an extra slot for killing two of the Enemy Walkers (`Citadel_FlexSlotUnlockedSlot03`)
- You've unlocked an extra slot for killing all of the Enemy Walkers (`Citadel_FlexSlotUnlockedSlot04`)
- Vanguard arriving soon to {Lane Color} Lane (`Citadel_FlexSlotVanguard`)
- Extra Slot Unlocked (`Citadel_FlexSlot_Title`)
- The Broker Has Restocked... (`Citadel_HUD_CorruptedItemShopRestock`)
- You may corrupt another item (`Citadel_HUD_CorruptedItemShopRestock_Desc`)
- The Broker has opened shop... (`Citadel_HUD_CorruptedItemShopSpawn`)
- Increase the power of your items... if you dare (`Citadel_HUD_CorruptedItemShopSpawn_Desc`)
- [Default.Open Hero Sheet]to Open Shop (`Citadel_Hud_Autobuy_HudHint_ShopKey`)
- Press [Open Hero Sheet] to Corrupt Items (`Citadel_Hud_OpenCorruptedShop`)
- Press [Open Hero Sheet] to Shop (`Citadel_Hud_OpenShop`)
- queue size {queue_size, plural, one{Item} other{Items}} (`Citadel_Hud_Quickbuy_ShopSummaryItemsInQueue:f`)
- items ready {items_ready, plural, one{Item} other{Items}} (`Citadel_Hud_Quickbuy_ShopSummaryItemsReady:f`)
- Round Begins in: (`Citadel_Hud_StreetBrawlShopCountdown`)
- Upgrades To: (`Citadel_IsComponentOf`)
- Required Extra Slots: required flex slots (`Citadel_Item_Build_RequiredFlexSlots`)
- Return to Shop to purchase (`Citadel_Item_Tooltip_ReturnToShop`)
- Vitality Investment (`Citadel_ModBonus_ArmorInvestment`)
- Health Increases (`Citadel_ModBonus_ArmorInvestmentDesc`)
- Spirit Investment (`Citadel_ModBonus_TechInvestment`)
- Spirit Power Increases (`Citadel_ModBonus_TechInvestmentDesc`)
- Weapon Investment (`Citadel_ModBonus_WeaponInvestment`)
- Weapon Damage Increases (`Citadel_ModBonus_WeaponInvestmentDesc`)
- Broker Arrival Time - minutesm (`Citadel_PrivateLobby_CorruptedItemShopSpawnTime`)
- Spirit Damage (`Citadel_ShopFilter_MagicDamage`)
- Weapon Damage (`Citadel_ShopFilter_WeaponDamage`)
- Golden Statues (`Citadel_ShopStats_GoldenStatues`)
- Shop Bonuses (`Citadel_ShopStats_ShopBonuses`)
- Imbued by [imbuing_ability_name] (`Citadel_Shop_AbilityIsImbued`)
- Imbued upon [imbued_ability_name] (`Citadel_Shop_AbilityIsImbuing`)
- Drag and drop to reassign current activated abilities (`Citadel_Shop_ActivePlacementTooltip_Drag`)
- Choose an ability slot to complete purchase (`Citadel_Shop_ActivePlacementTooltip_Title`)
- Corrupt an Item (`Citadel_Shop_CorruptItem_Button`)
- The Broker is skipping town in countdown time... (`Citadel_Shop_CorruptItem_Countdown`)
- Are you sure you want to sell item [item_name] for item sell amount souls (half the purchase price)? (`Citadel_Shop_Destroy_Item_Confirm`)
- to purchase [enter_purchase_item] (`Citadel_Shop_EnterPurchase_Purchase`)
- to sell [enter_purchase_item] (`Citadel_Shop_EnterPurchase_Sell`)
- Hold[Scoreboard] (`Citadel_Shop_HoldAlt`)
- Choose an ability to imbue (`Citadel_Shop_ImbueTooltip_Title`)
- Damage Warning (`Citadel_Shop_InCombat_Alert`)
- Popular Items (`Citadel_Shop_NavTab_Recommended`)
- Spirit Items (`Citadel_Shop_NavTab_SpiritItems`)
- Vitality Items (`Citadel_Shop_NavTab_VitalityItems`)
- Weapon Items (`Citadel_Shop_NavTab_WeaponItems`)
- Select a high-tier item you own to corrupt it. Corrupted items are powerful, but buyer beware - every item also carries a randomized downside. Each game, The Broker will decide where the stats will land. (`Citadel_Shop_PickCorruptItem_Desc`)
- None of the items you own can be corrupted. (`Citadel_Shop_PickCorruptItem_None`)
- Corrupt one of your non-enhanced items for free. Corrupted items are permanently stronger, but every item carries a downside. (`Citadel_Shop_PickCorruptItem_StreetBrawlDesc`)
- Corrupt an Item (`Citadel_Shop_PickCorruptItem_Title`)
- Pick which item you'd like to enhance (`Citadel_Shop_PickEnhanceItem_Desc`)
- Enhance an item (`Citadel_Shop_PickEnhanceItem_Title`)
- Player Level: total player level (`Citadel_Shop_Player_Level_Label`)
- [selected_build_name] (`Citadel_Shop_SelectedBuildHeader`)
- Active Slots Full (`Citadel_Shop_SellMaxItemsActive_Title`)
- Select an item to replace (`Citadel_Shop_SellMaxItems_Desc`)
- Item Slots Full (`Citadel_Shop_SellMaxItems_Title`)
- Shop Settings (`Citadel_Shop_SettingsTooltip`)
- Sort Items by Category (`Citadel_Shop_Sort_Tooltip_Categories`)
- Sort Items by Price (`Citadel_Shop_Sort_Tooltip_Tier`)
- Spirit Power (`Citadel_Shop_TierBonus_Tech`)
- Weapon Damage (`Citadel_Shop_TierBonus_Weapon`)
- Lvl unlock Level Required (`Citadel_Shop_Upgrade_Locked_Label`)
- Active Items (`EShopFilterActive`)
- Anti-Healing (`EShopFilterAntiHeal`)
- Bullet Damage Reduction (`EShopFilterBulletDamageReduction`)
- Physical Vulnerability (`EShopFilterBulletVuln`)
- Debuff Resistance (`EShopFilterDebuffResist`)
- Fire Rate Reduction (`EShopFilterFireRateReduction`)
- Invulnerability (`EShopFilterInvulnerability`)
- Spirit Items (`EShopFilterItemSpirit`)
- Vitality Items (`EShopFilterItemVitality`)
- Weapon Items (`EShopFilterItemWeapon`)
- Jump/Dash/Slide (`EShopFilterJumpAndDash`)
- Melee Resistance (`EShopFilterMeleeResist`)
- Out of Combat Regen (`EShopFilterOutOfCombatRegen`)
- Additional Physical Damage (`EShopFilterPhysicalAdditionalDamage`)
- Physical Resistance (`EShopFilterPhysicalResist`)
- Popular (Early Game) (`EShopFilterPopularEarlyGame`)
- Popular (Late Game) (`EShopFilterPopularLateGame`)
- Popular (Mid Game) (`EShopFilterPopularMidGame`)
- Slow Resistance (`EShopFilterSlowResist`)
- Spirit Damage (`EShopFilterSpiritAdditionalDamage`)
- Health % Damage (`EShopFilterSpiritAdditionalDamagePct`)
- Cooldown & Charges (`EShopFilterSpiritCooldownAndCharges`)
- Spirit Power (`EShopFilterSpiritDamage`)
- Spirit Damage Reduction (`EShopFilterSpiritDamageReduction`)
- Spirit Resistance (`EShopFilterSpiritResist`)
- Spirit Vulnerability (`EShopFilterSpiritVuln`)
- Bullet Velocity (`EShopFilterWeaponBulletVelocity`)
- Weapon Damage (`EShopFilterWeaponDamage`)
- Earned by being a Steam Workshop contributor (`ItemHistory_Action_SteamWorkshopContributor`)
- Press MOUSE1 to select a single filter. Press MOUSE2 to select multiple filters (`ShopFilter_HintSecondary`)
- Press [Open Hero Sheet] to open up the shop and set test options. (`citadel_hint_hero_testing_shop`)
- Switch to the All Items tab and start typing in the shop search box. (`citadel_hotkeys_tooltip_shop_focus_search`)
- When your shop search has narrowed the results to a single item, buy it, or sell it if you already own it. Works while typing in the search box. (`citadel_hotkeys_tooltip_shop_purchase_search_match`)
- Switch to the All Items tab of the shop. (`citadel_hotkeys_tooltip_shop_tab_all_items`)
- Switch to the Builds tab of the shop. (`citadel_hotkeys_tooltip_shop_tab_build`)
- Switch to the Popular Items tab of the shop. (`citadel_hotkeys_tooltip_shop_tab_recommended`)
- Switch to the Spirit Items tab of the shop. (`citadel_hotkeys_tooltip_shop_tab_spirit`)
- Switch to the Vitality Items tab of the shop. (`citadel_hotkeys_tooltip_shop_tab_vitality`)
- Switch to the Weapon Items tab of the shop. (`citadel_hotkeys_tooltip_shop_tab_weapon`)
- Scroll the shop down one price tier. If you have disabled the Snap Scrolling to Price Tiers option, this scrolls a small amount instead. (`citadel_hotkeys_tooltip_shop_tier_down`)
- Scroll the shop up one price tier. If you have disabled the Snap Scrolling to Price Tiers option, this scrolls a small amount instead. (`citadel_hotkeys_tooltip_shop_tier_up`)
- Search items (`citadel_keybind_shop_focus_search`)
- Buy/sell search result (`citadel_keybind_shop_purchase_search_match`)
- All Items tab (`citadel_keybind_shop_tab_all_items`)
- Popular Items tab (`citadel_keybind_shop_tab_recommended`)
- Vitality tab (`citadel_keybind_shop_tab_vitality`)
- Used as Component (`item_info_component_locked`)
- Requires Component [component_required] (`item_info_component_required`)
- No Nearby Shop (`item_info_no_shop`)
- Curiosity Dealer (`npc_shopkeeper`)

## Current numbers in the game files

`ItemPricePerTier`

| Field | Value |
|---|---|
| ItemPricePerTier | 0 / 800 / 1600 / 3200 / 6400 / 9999 |

## Patch history (101 lines, newest first)

**2026-06-30** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1836506165563227))

- Urn bounty when deposited is worth 250 + 70/min for just the urn runner. Still has the comeback bounty component. Upon deposit all of the souls are released as orbs into the air (if another ally secures the orbs, they share the bounty with the urn runner).
- Hovering an item in the shop now shows you a preview for your investment bars
- Street Brawl: Fixed Enhanced Sharpshooter and Enhanced Spiritual Overflow not maintaining the bonuses from their enhanced components

**2026-05-22** ([forum post](https://forums.playdeadlock.com/threads/05-22-2026-update.135477/))

- Weapon Investment Bonus now has a 6.4k line, changed from 4.8k/7.2k/9.6k/16k to 4.8k/6.4k/8k/11.2k/16k with bonuses from 46/55/70/85 to 46/54/62/74/86
- Vitality Investment Bonus now has a 6.4k line, changed from 4.8k/7.2k/9.6k/16k to 4.8k/6.4k/8k/11.2k/16k with bonuses from 38/42/46/50 to 38/42/46/50 (final two tiers shifted up by +4)
- Spirit Investment Bonus now has a 6.4k line, changed from 4.8k/7.2k/9.6k/16k to 4.8k/6.4k/8k/11.2k/16k with bonuses from 38/48/57/66 to 38/45/52/59/66
- Fixed the following Enhanced Items not maintaining their stats from components: Opening Rounds, Tankbuster, Kinetic Dash, Radiant Regeneration, Burst Fire, Veil Walker, Arcane Surge, Fury Trance, Leech

**2026-04-30** ([forum post](https://forums.playdeadlock.com/threads/04-30-2026-update.129989/))

- [ General ] - Base health per boon reduced by 7 - Vitality Investment bonus increased from 8/10/13/17/34/39/44/48/52/56% to 9/12/15/20/38/42/46/50/56/62% - Weapon Investments bonus rescaled from 7/9/13/20/49/60/80/95/115/135% to 9/12/15/18/46/55/70/85/100/115% - Reduced bullet damage growth by...

**2026-03-21** ([forum post](https://forums.playdeadlock.com/threads/03-06-2026-update.114328/post-226950))

- Vitality investment tree bonus reverted back to % base hp increase rather than raw constant bonus (back to how it was set up in december)
- Spirit investment rescaled from 7/11/15/19/38/52/64/76/89/101 to 7/11/15/19/38/48/57/66/75/100
- Vitality investment tree bonus reverted back to % base hp increase rather than raw constant bonus (back to how it was set up in december)
- Spirit investment rescaled from 7/11/15/19/38/52/64/76/89/101 to 7/11/15/19/38/48/57/66/75/100

**2026-03-10** ([forum post](https://forums.playdeadlock.com/threads/03-06-2026-update.114328/post-220287))

- Vitality investment bonuses increased by 12%
- Doorman: Call Bell now has Impact Damage (40+1) and Explosion Damage (55+1.7) as separate components again (previous values for impact/explosion)
- Vitality investment bonuses increased by 12%
- Doorman: Call Bell now has Impact Damage (40+1) and Explosion Damage (55+1.7) as separate components again (previous values for impact/explosion)

**2026-03-06** ([forum post](https://forums.playdeadlock.com/threads/03-06-2026-update.114328/))

- Street Brawl: Removed item slot limit (don't need to sell items in the final round sometimes)

**2025-12-16** ([forum post](https://forums.playdeadlock.com/threads/12-16-2025-update.93983/))

- Vitality investment tree bonuses changed from a % of base health to a fixed amount (from +8/10/13/17/34/39/44/48/52/56% to +75/125/200/275/525/625/750/1000/1200/1400)
- Spirit investment tree 4.8k bonus reduced from 45 to 38

**2025-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/))

- Weapon Investment Bonuses: Now grants an additional +20% Weapon Damage at 4800 souls spent
- Vitality Investment Bonuses: Now grants an additional +12% Bonus Health at 4800 souls spent
- Spirit Investment Bonuses: Now grants an additional +20 Spirit Power at 4800 souls spent
- Added a UI highlight to 4800 reward row of the investment bonuses
- Base slot count increased from 8 to 9 and Flex slot count reduced from 4 to 3. One is given for each Walker killed. Previously the 4 were given for: "3 Guardians", "1 Walker", "3 Walkers", and "Set of Base Guardians"

**2025-10-03** ([forum post](https://forums.playdeadlock.com/threads/10-02-2025-update.84332/post-159495))

- Fixed Wall Jumps not refunding stamina if a mantle or zipline occurs within the refund window (similar to how we treat other stamina refunds)

**2025-10-02** ([forum post](https://forums.playdeadlock.com/threads/10-02-2025-update.84332/))

- Weapon Investment bonus increased from 7/9/13/20/29/40/58/72/83/93% to 7/9/13/20/29/40/60/75/95/115 (for 0.8/1.6/2.4/3.2/4.8/7.2/9.6/16/22.4/28.8k spent)
- Neutral Shop no longer gets disabled if an enemy is nearby

**2025-06-17** ([forum post](https://forums.playdeadlock.com/threads/06-17-2025-update.68401/))

- Flex Slot changed from "Two Guardians" to "Three Guardians"
- Flex Slot changed from "Two Walker" to "Three Walkers"

**2025-05-27** ([forum post](https://forums.playdeadlock.com/threads/05-27-2025-update.66453/))

- Armor Piercing Rounds: Bullet Velocity increased from 30% to 35% (to match the component)

**2025-05-21** ([forum post](https://forums.playdeadlock.com/threads/05-21-2025-update.65674/))

- Removed a misplaced Curiosity Shop sign.

**2025-05-11** ([forum post](https://forums.playdeadlock.com/threads/05-11-2025-update.64113/))

- Weapon tree investment bonus increased by 6-12% (from 6/8/12/18/26/36/52/68/78/88% to 7/9/13/20/29/40/58/72/83/93)

**2025-05-08** ([forum post](https://forums.playdeadlock.com/threads/05-08-2025-update.63133/))

- Deadlock - Shop Rework Update - Steam News
- Full shop rework including many new items, build authoring, quickbuy redesign and several other game updates

**2024-12-06** ([forum post](https://forums.playdeadlock.com/threads/12-06-2024-update.50599/))

- Fixed shop search not working in the shop when opened from Resources
- Fixed the Damage Report UI clipping into the shop in Sandbox mode
- Fixed shop showing with a broken build tab if you had previously navigated to the hero builds, then opened it from Resources
- Fixed Grey Talon's spirit power growth from his ult not being reflected in the shop

**2024-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2024-update.47476/))

- Items in the shop that imbue abilities are tagged with a label with a similar styling to active items
- Purchase Log in the shop now shows enemy and ally purchases with different colors
- Fixed a bug where you would be prompted to sell an item if the component wasn't in the same category as the component you were buying (i.e. you go to buy slowing hex with your item slots full and you already own the component)
- Fixed respawn music cue failing to play with shop menu open
- Fixed right-clicking on an item in the shop in build editing mode causing it to be added to your Quickbuy queue
- Flex Slot changed from All Shrines to 1 Shrine and 2 Base Guardians
- Added a street gate structure between the Garage and the Record Shop
- New T3 Weapon Item, Spellslinger Headshots: Requires Soul Shredder Bullets. Landing a headshot on enemy heroes increases your total Spirit Power by 3% for 12s. Cooldown 1.5s. Max stacks 12. Grants +12% Weapon Damage, +8% Spirit Amp/18% Spirit Lifesteal (component passive), and +150 Health.

**2024-11-07** ([forum post](https://forums.playdeadlock.com/threads/11-07-2024-update.44786/))

- Added Quickbuy - You can now right-click items in the shop to add them to your Quickbuy queue. When you return to the shop, you will automatically purchase the items you can afford in your set order. An indicator on the hud will light up when you can afford the next item on your list. In Settings you may change the purchase mode to use a hotkey while in range of the shop rather than auto-purchase.
- Added a Recent Purchases log to the Shop that displays all items bought by players during a match, ordered by most recent
- Fixed the 'x' button in the shop search not clearing the search box

**2024-10-24** ([forum post](https://forums.playdeadlock.com/threads/10-24-2024-update.40951/))

- Added quick-selection for favorite builds. Clicking on the name of your currently active build in the shop will bring up a dropdown that lets you switch between favorited builds for that hero without opening the build browser.
- Fixed pregame countdown drawing over the shop UI
- Shrine Flex Slot moved to "All Shrines"

**2024-10-18** ([forum post](https://forums.playdeadlock.com/threads/10-18-2024-update.39630/))

- We have adjusted the matchmaking schedule to not be split across many different hours throughout the day, primarily to help address queue times. There will now be a wider continuous, but more concentrated, set of hours that it is enabled in. The schedule is now more simplified as well, as there is no more user selection component.

**2024-10-15** ([forum post](https://forums.playdeadlock.com/threads/10-15-2024-update.38925/))

- First flex slot is now granted after 3 Guardians die instead of 4

**2024-10-10** ([forum post](https://forums.playdeadlock.com/threads/10-10-2024-update.36958/))

- Added Crit Bonus Scale tooltip to the Weapon stats in the shop

**2024-09-29** ([forum post](https://forums.playdeadlock.com/threads/09-29-2024-update.34541/))

- Fixed Wraith Cards, Shiv Rage and lifesteal from increasing by shooting the shop

**2024-09-26** ([forum post](https://forums.playdeadlock.com/threads/09-26-2024-update.33015/))

- Fixed Flex Slot unlock order not matching the usual order of unlocks

**2024-09-12** ([forum post](https://forums.playdeadlock.com/threads/09-12-2024-update.27974/))

- Flex Slot moved from "First Walker" to "Two Walkers"
- Added connections from the Shop to the front of the Department Store and the New York Oracle buildings

**2024-08-29** ([forum post](https://forums.playdeadlock.com/threads/08-29-2024-update.22253/))

- Added Heal Amp and Debuff Resist to the Vitality stats in the shop
- Added alternate shop music which plays in the neutral shop
- Fixed selling an item not removing charges correctly. Now you can't buy Extra Charge and immediately sell it and keep that readied charge.
- Fixed a bug that caused items in the build page to not be dimmed when the shop was out of range
- Moved a flex slot from "Set of enemy Base Guardians" to "All Enemy Lane Guardians"
- Removed the archway leading to the underground shop

**2024-08-16** ([forum post](https://forums.playdeadlock.com/threads/08-16-2024-update.17251/))

- Changed default shop music back to original

**2024-08-15** ([forum post](https://forums.playdeadlock.com/threads/08-15-2024-update.16378/))

- Hovering items in the shop will now highlight their components, or which item they are components of
- Reworked the Hero Stats UI in the shop
- Hero Stats in the shop have been expanded and are now broken up by Weapon, Vitality, and Spirit. Various additional stats that were previously hidden have been added here.
- Improved lighting performance around shop
- Added alternate shop music
- Widened hallway above Underground Shop
- Courtyard floor opening to the Underground Shop moved closer to above the shop
- Bounce Pad added to allow easier navigation from the Underground Shop to the upper courtyard. Replaces a juke spot.

**2024-08-01** ([forum post](https://forums.playdeadlock.com/threads/08-01-2024-update.13369/))

- Reworked the Hero Builds system. Browsing and editing builds now happens within the Shop UI (accessible via Sandbox or during a normal game). You can create custom categories for items with unique names and descriptions that can be independently resized and positioned. The interface for browsing builds has also been improved, public builds will now be sorted by popularity (number of favorites). Old builds are incompatible with this system, so they won't be visible in this UI, but we'll have a console command we'll release soon that you can use to print out your older guides if you need them for reference.
- Fixed dead player minimap icons showing over enemy players who are below street level and over shop icons
- Fixed shop close sounds playing whenever the player enters the radius of a closed shop
- Moved delivery truck out from the street curb near the underground shop
- Moved barrel cover barrier to block the Guardian shop opening on Amber Purple and Sapphire Yellow

**2024-07-18** ([forum post](https://forums.playdeadlock.com/threads/07-18-2024-update.11831/))

- Opening the shop now always minimizes the Damage Report

**2024-07-11** ([forum post](https://forums.playdeadlock.com/threads/07-11-2024-update.10871/))

- Shop search now highlights the relevant sections of the item tooltip that match the search string you've put in
- Fixed the Shop search not finding all the types of bonuses an item has
- Shortened connection to the underground tunnel from the shop side

**2024-07-04** ([forum post](https://forums.playdeadlock.com/threads/07-04-2024-update.9652/))

- Added a new Damage Report feature. You can now open a flyout panel within the shop to view a breakdown of your hero's incoming and outgoing damage throughout the course of a match. You can also hover an enemy hero to view a quick breakdown of their key stats and items. The data can be filtered by last respawn, 10 minutes, 5 minutes, 3 minutes, 1 minute, or 30 seconds.
- Fixed position of the "All Walkers Destroyed" Flex slot to be the 2nd slot rather than the 4th

**2024-06-27** ([forum post](https://forums.playdeadlock.com/threads/06-27-2024-update.8486/))

- Flex slot removed from killing the Patron and added to killing all Walkers
- Added connection hallway between outer lane Shop and crate room
- Extended alcove on outer lane cover position in front of the Shop

**2024-06-20** ([forum post](https://forums.playdeadlock.com/threads/06-20-2024-update.7003/))

- Added search functionality to the shop. You can now search by item name or by individual stat such as 'Ammo', 'Lifesteal', or 'Spirit Power'.

**2024-06-13** ([forum post](https://forums.playdeadlock.com/threads/06-13-2024-update.5773/))

- Added two new underground tunnels, one on each side of the map. The tunnels connect the underground shop to the Bodega area on Amber and the Theater area on Sapphire.
- Urn reward now has a comeback component where it gives extra gold for the team that is behind based on the magnitude

**2024-06-06** ([forum post](https://forums.playdeadlock.com/threads/06-06-2024-update.4096/))

- You can now move active item slots on the HUD while holding alt/tab
- Fixed moving active item slots causing the player to say "[ITEM] is on cooldown"

**2024-05-23** ([forum post](https://forums.playdeadlock.com/threads/05-23-2024-update.1245/))

- Fixed the bottom most shop items having part of their icon be unclickable

**2024-05-16** ([forum post](https://forums.playdeadlock.com/threads/05-16-2024-update.902/))

- Added a wall between the T1 shop and the hallway on the outer lanes by the Fire House and the Chapel to prevent attackers from shooting the T1 without taking damage
- Replaced news stand that was close to the T1 with different cover kiosk building to avoid shop confusion

**2024-05-13** ([forum post](https://forums.playdeadlock.com/threads/05-13-2024-update.807/))

- Visual and Audio updates to the shop
- Fortitude now starts on cooldown to prevent purchasing and selling in the field for significant regen
- Fixed items not updating in the UI when purchased from the shop while spectating a teammate

**2024-05-03** ([forum post](https://forums.playdeadlock.com/threads/05-03-2024-update.427/))

- Added a Resources page to the dashboard which contains a browsable item shop
- Shop music will now only play for shops players can access
