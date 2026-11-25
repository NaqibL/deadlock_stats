# Souls and the economy

Generated from the game files at build 6868 and Valve's patch notes. Everything below is quoted from a source, not interpreted. Patch notes describe the game as of their date: read newest first, and treat an older line as history once a newer one changes the same thing.

## What the game itself says

- Ammo Per Soul (`AmmoPerSoul_label`)
- Ammo Per Soul (`AmmoPerSoul_postvalue_label`)
- Bounty Duration (`BountyDuration_label`)
- Bounty Duration (`BountyDuration_postvalue_label`)
- Souls Collected (`Citadel_GraphType_NetWorth`)
- Souls Collected Difference (`Citadel_GraphType_NetWorthDelta`)
- Souls per Minute (`Citadel_GraphType_NetWorthPerMin`)
- Souls by Source (`Citadel_GraphType_SoulsBySource`)
- Souls Collected Difference (`Citadel_Graph_NetWorthDeltaLine`)
- Ability Assassinate (`Citadel_Graph_Souls_AbilityAssassinate`)
- Kill Assists (`Citadel_Graph_Souls_Assists`)
- Breakable Pickups (`Citadel_Graph_Souls_Breakables`)
- Cultist Sacrifice (`Citadel_Graph_Souls_ItemCultistSacrifice`)
- Golden Goose Egg (`Citadel_Graph_Souls_ItemGooseEgg`)
- Trophy Collector (`Citadel_Graph_Souls_ItemTrophyCollector`)
- Team Catch-Up (`Citadel_Graph_Souls_TeamBonus`)
- [thousands_gold]k (`Citadel_HUD_LevelReward_NetWorthHigh`)
- Haunted Souls (`Citadel_Hero_Stats_Unsecured`)
- Souls Gathered (`Citadel_Hud_SoulsGathered`)
- thousands goldk (`Citadel_Hud_TopbarPlayerNetworth`)
- thousands goldk (`Citadel_Hud_TopbarPlayerNetworthPlayerHigh`)
- thousands gold.hundred goldk (`Citadel_Hud_TopbarPlayerNetworthPlayerMed`)
- team1 networthk (`Citadel_MatchDetails_Team1NetWorth`)
- team2 networthk (`Citadel_MatchDetails_Team2NetWorth`)
- Second Most Souls (`Citadel_PostGame_AwardSouls_Rank2`)
- Third Most Souls (`Citadel_PostGame_AwardSouls_Rank3`)
- Highest Networth (`Citadel_Post_Game_HighestNetworth`)
- {stat_value, plural, one{Soul} other{Souls}} Collected (`Citadel_Profile_Stats_Networth:f`)
- game networthk (`Citadel_Profile_Stats_Value_Networth_High`)
- game networth (`Citadel_Profile_Stats_Value_Networth_Low`)
- net worth team 0k (`Citadel_Watch_Page_NetWorthTeam0`)
- net worth team 1k (`Citadel_Watch_Page_NetWorthTeam1`)
- Souls Earned (`ReportCard_NetWorth`)
- Souls gained by killing troopers and shooting orbs (`ReportCard_NetWorth_Desc`)
- net Worth / net Worth Next Goal Souls (`ReportCard_NetWorth_Progress`)
- Collect 1000 souls from killing enemy troopers (`ReportCard_SoulsCollected_Desc`)
- Sell Bonus Souls: (`SellBonusSouls_label`)
- Sell Bonus Souls: (`SellBonusSouls_postvalue_label`)
- Projectile Radius (`SoulProjectileRadius_label`)
- Spirit Power Per Soul (`SpiritPowerPerSoul_label`)
- Spirit Power Per Soul (`SpiritPowerPerSoul_postvalue_label`)
- Discharge Soul (`apocalypse_discharge_soul`)
- Tombstone Nearby (`apocalypse_discharge_soul/modifier_tombstone_nearby_aura/modifier_tombstone_nearby`)
- Fires a projectile that damages, EMPs, and slows. Charges do not refresh with time. Collect charges by kneeling next to tombstones that appear near fallen friendly troopers. (`apocalypse_discharge_soul_desc`)

## Current numbers in the game files

`ObjectiveParams`

| Field | Value |
|---|---|
| NearPlayerSplitPct | 25 |
| Tier1GoldKill | 1375 |
| Tier2GoldKill | 3675 |
| BaseGuardiansGoldKill | 1000 |
| ShrinesGoldKill | 2000 |

`HeroKillGoldShareFrac`

| Field | Value |
|---|---|
| HeroKillGoldShareFrac | 1.25 / 0.575 / 0.283 / 0.175 / 0.11 / 0.083 |

`TrooperKillGoldShareFrac`

| Field | Value |
|---|---|
| TrooperKillGoldShareFrac | 1 / 0.54 / 0.36 / 0.25 / 0.2 / 0.16 |

## Patch history (160 lines, newest first)

**2026-09-16** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1844115010490072))

- Unstable Rift comeback resist max values now scale over the course of the game. Previously the max values were 35%. Now it is 10% + 1% per minute (around ~20% for the first one), with an upper limit of 40% at 30 minutes.
- Removed a fixed amount of extra bonus souls you would get for being behind even a very slightly amount in net worth for both hero kill bounties as well as Unstable Rift bounties (this had a larger impact on the early to mid game)
- Slightly reduced comeback bounties in general (this is in addition to the above change)
- A portion of the comeback souls earned by players above enemy teams average net worth is instead distributed via the tick gold system that is given to the lowest 2 players (70% of the extra comeback value goes to them)
- Guardian bounty increased by 10%
- Walker bounty increased by 5%
- Share for objectives bounty to nearby heroes reduced from 30% to 25% (the remaining gets split between all 6 players)

**2026-07-09** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1836506165584438))

- Unstable Rift comeback resist aura radius increased from 20m to 35m
- Rift Troopers max comeback count increased from 12 to 14
- Objectives bounty split for nearby heroes reduced from 40% to 30% (this means slightly more portion of the bounty is split team wide rather than towards an individual player)

**2026-06-30** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1836506165563227))

- Unstable Rift comeback bonuses (resists in the area, extra comeback bounty, and trailing/leading team claiming timer) now all scale linearly based on the amount of NW they are trailing (scales from no bonus at 0% NW behind to full bonus at 15% NW behind)
- The team that secures the Unstable Rift now also has a wave of 5 Rift Troopers sent down from the rift location. When trailing, spawns up to 12 troopers instead (using the same linear ramp from 0% NW to -15% NW)
- Unstable Rift bounty increased by 35% (to account for the 35% loss with no urn runner bounty, overall objective bounty is unchanged)
- Urn bounty value starts decaying after 45s from being picked up. It drains gradually over another 45s and then the urn is removed when the bounty is empty.
- Urn bounty when deposited is worth 250 + 70/min for just the urn runner. Still has the comeback bounty component. Upon deposit all of the souls are released as orbs into the air (if another ally secures the orbs, they share the bounty with the urn runner).
- Guardian bounty reduced from 1500 to 1250
- Walker bounty reduced from 4000 to 3500
- First blood bounty reduced from 150 to 125
- Base kill bounty reduced from 250 to 200 (max is still 2200 at 40m)
- Trooper bounty rescaled from 116 + 1.16/m to 100 + 2/m (less before 20m, more after)
- Trooper bounty ratio in the deniable flying orb increased from 40% to 50%
- Minimum unsecured souls allowed to drop reduced from 150 to 50 + 5/min

**2026-06-11** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1835236783562074))

- Urn bounty reduced by 10% (unreduced for trailing team)
- Kill comeback bounty values increased by 8%

**2026-06-04** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1834602721188293))

- The Urn runner now gets their normal 35% bonus bounty and stats immediately on initial deposit (rather than on deposit conclusion only if your team won it)
- Urn overall bounty reduced by 20% (unreduced for trailing team)
- Urn comeback resistance now also grants +35% Debuff Resistance ontop of the 35% Bullet and Spirit Resistance
- Urn comeback resistance aura reduced from 60m to match the 20m progress radius

**2026-05-25** ([forum post](https://forums.playdeadlock.com/threads/05-22-2026-update.135477/post-259788))

- Urn comeback bullet and spirit resist auras reduced from 50% to 35%
- Urn pickup spot is now where the old comeback drop off spots were for when your team is behind

**2026-05-22** ([forum post](https://forums.playdeadlock.com/threads/05-22-2026-update.135477/))

- If the urn is Favored or Unfavored (in a comeback state), then the Favored team will get +50% Bullet and Spirit Resist in a 60m radius around the urn while it is being carried, dropped or deposited.

**2026-03-10** ([forum post](https://forums.playdeadlock.com/threads/03-06-2026-update.114328/post-220287))

- Super [[Trooper|troopers]] (when a lane [[Shrine|shrine]] is down) now have 15% less bounty
- Super troopers (when a lane shrine is down) now have 15% less bounty

**2026-03-06** ([forum post](https://forums.playdeadlock.com/threads/03-06-2026-update.114328/))

- Guardians bounty increased from 1000 to 1500
- Walkers bounty increased from 3500 to 4000
- Base Guardians bounty from 750 to 1000
- Shrines bounty increased from 0 to 2000
- Mid Boss base bounty increased from 2000 to 3000

**2026-01-20** ([forum post](https://forums.playdeadlock.com/threads/12-29-2025-update.95233/post-185824))

- You now have a longer respawn time if you die and are meaningfully richer than the enemy team's average net worth (scales from +6s to +22s penalty, based on networth being 15 to 30% higher and game time being 10min to 25min, if under 15% NW or 10min, nothing happens)
- Neutral respawn times, hp, and bounty reduced by 30% (sinner's sacrifice unaffected)

**2025-12-16** ([forum post](https://forums.playdeadlock.com/threads/12-16-2025-update.93983/))

- Trooper bounty reduced by 12%
- Urn: Bounty increased from 700 + 230/min to 1300 + 230/min
- Urn: Comeback bounty now gives more souls
- Urn: Bonus bounty for carrier increased from 25% to 35%
- Increased kill bounty for solo kills (1 attacker in the kill) by 25%, and by 15% for duo kills
- Increased portion of the bounty the killer gets relative to the assist portion
- Increased comeback bounties for losing team a bit
- Sinner's Sacrifice bounty reduced by 10%
- Unsecured souls claim period reworked. Previously the way it worked was any unsecured souls you gained were added to a rolling 165s window, where it was divided over that time and given out, with a minimum amount given per second of 1 soul. The new system drains 0.5% (of the remaining souls) + 1.6 (scales with the 8% bounty growth per minute).
- There are a few examples below to show how they compare. Old was 165s (assuming bounty was at least 165s). New is:

**2025-11-23** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/post-172057))

- Hero kill bounty split efficiency for 1/2/3/4/5/6 players changed from 100/100/90/84/65/72% to 100/100/85/70/55/50%

**2025-11-22** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/post-171913))

- Neutrals bounty increased by 5%

**2025-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/))

- Trooper bounty mechanics have been reworked. The first half of the souls still fly out as deniable orb, however rather than the other half being instantly given to nearby players it will fall to the ground as an orb that you need to get near to pick up. It has a 18m capture radius where it'll travel to you once you get within. Only one player needs to claim it, share rules remain the same as before.
- Enemy orbs are visible as faint colorless soul orbs to your team, but cannot be claimed.
- Amount of souls in the flying orb that can be secured/denied reduced from 50% to 40%
- Very small tweaks to the secure/deny lag calculation to improve it
- Medic troopers now drop a medic pack when you kill them. Has same pickup range/duration mechanics as the soul orbs on the ground. Heals everyone in a 30m radius for 10% of their missing health as well as 75 plus 2 per minute game time.
- Trooper bounty values increased by 10%
- Trooper bounty split ratios updated from 1/0.65/0.28/0.15/0.12/0.08 to 1/0.54/0.36/0.25/0.2/0.16
- Neutrals bounty increased by 10%
- Minimum unsecured gold to drop increased from 100 to 150

**2025-10-02** ([forum post](https://forums.playdeadlock.com/threads/10-02-2025-update.84332/))

- Dropped Unsecured soul bags now require a Heavy Melee to secure rather than standing ontop of them

**2025-09-04** ([forum post](https://forums.playdeadlock.com/threads/09-04-2025-update.80693/))

- Dying to a non-player (when there is no bounty/assists) now increases the respawn time for that death by 10 seconds

**2025-07-29** ([forum post](https://forums.playdeadlock.com/threads/07-29-2025-update.72760/))

- Reworked Rejuv reward from Mid Boss. No longer buffs troopers, reduces respawn time and buffs various stats. Upon death, 3 rejuv crystals fall to the ground (4 for subsequent midboss kills). Claiming one now grants you in place revive after 3s. If you already claimed one and claim another, it'll go to an ally (priority is closest allies first, then most recent dead allies). Dying with Rejuv no longer counts as a kill/death nor gives out bounties. While you have the Rejuv buff, you gain the following: +20% Max HP, +20% Fire Rate, and +15% Spirit Damage. Gaining the buff heals you to full and lasts up to 7 minutes.
- Trooper bounty growth reduced from 1.5 to 1.2
- Reduced comeback multipliers a bit
- Neutrals bounty increased by 15% (strong neutrals +25%)
- Hero bounties are now reduced based on the amount of players, similar to the trooper mechanic. (Means kills are less efficient/rewarding when its a big group, 1/2/3/4/5/6 players are 100/100/90/85/80/75% efficient)

**2025-07-04** ([forum post](https://forums.playdeadlock.com/threads/07-04-2025-update.70156/))

- Small neutral camp bounty increased by 15%
- Mid Boss total bounty increased from 500 + 50/min to 2000 + 50/min (evenly split among the team that kills the boss, unrelated to rejuv secure)
- Guardian total bounty reduced from 1650 to 1000
- Walker total bounty reduced from 4500 to 3500
- Comeback values are now roughly 25% stronger (this was released before this patch in a recent update)
- Fixed a bug causing soul orb shots towards the end of the contested window to not register as hits on the server

**2025-06-17** ([forum post](https://forums.playdeadlock.com/threads/06-17-2025-update.68401/))

- Guardian and Walker total bounty is now split with all nearby players (including players that have done damage to it within 20s). Nearby players get 40% and the rest is split evenly with all 6 players (including those nearby).
- Hero Kill bounty increased from 250->1800 to 300->2000 (over 40 minutes, previously over 45 minutes)
- Killing heroes no longer spawns orbs, instead the souls are directly awarded to the killer and assisters
- Trooper base bounty reduced from 132 to 120
- Trooper bounty growth per minute increased from 1 to 1.5
- Soul Orb auto claim radius reduced from 40m to 35m

**2025-05-21** ([forum post](https://forums.playdeadlock.com/threads/05-21-2025-update.65674/))

- Fixed Breakable souls being counted as secured souls rather than unsecured souls (this fix was released yesterday)

**2025-05-19** ([forum post](https://forums.playdeadlock.com/threads/05-19-2025-update.65381/))

- Hero Kill Bounty increased from 175->1600 to 250->1800 (maxes out at 45 min)
- The soul orb securer's advantage over denier has been reduced.
- Add a flash to the start of the soul orb claimability window

**2025-04-17** ([forum post](https://forums.playdeadlock.com/threads/04-17-2025-update.61382/))

- Soul Orbs no longer have special duplication rules before 8 minutes. Soul splitting rules are now the same before 8 minutes as afterwards. Adjusted trooper economy to compensate. There is also no longer a bounty bump that occurs at 8 minutes.
- Wave interval increased from 25s to 30s (bounty values adjusted by the same ratio)
- First urn is now considered for comeback mechanics (15% NW delta)

**2025-04-04** ([forum post](https://forums.playdeadlock.com/threads/04-04-2025-update.60284/))

- Soul orb spawn delay range increased from 0.2-0.7 to 0.4-0.7
- Soul orb size increased by 10%
- Soul orb lag compensation buffer increased from 120ms to 140ms
- Fixed issues with denying melee soul orbs
- Fixed various other timing related bugs with Soul orbs

**2025-03-16** ([forum post](https://forums.playdeadlock.com/threads/03-16-2025-update.58880/))

- Neutral bounty increased by 5%
- Fixed a bug with Neutral bounty later in the game being reduced by more than the initial intended -15% (this fix was released yesterday)

**2025-03-13** ([forum post](https://forums.playdeadlock.com/threads/03-13-2025-update.58592/))

- Increased horizontal soul orb movement a bit
- Soul Orb spawn delay increased a bit and added some variability

**2025-01-19** ([forum post](https://forums.playdeadlock.com/threads/01-19-2025-update.53961/))

- The Magnificent Sinclair: Spectral Assistant base cooldown increased from 30s to 40s
- The Magnificent Sinclair: Spectral Assistant base duration decreased from 8s to 6s

**2024-12-06** ([forum post](https://forums.playdeadlock.com/threads/12-06-2024-update.50599/))

- Added a tick based souls system that gives the bottom two net worth players on the team a small amount of souls per second. The amount of souls available to distribute to the bottom two players is based on the souls gathered by your team (2% and 1%). This occurs after the laning phase.
- Added new limiting function for the soul orb duplication abuses during the laning phase. You shouldn't experience any real difference in normal gameplay:
- Players can only participate in 4 Soul Orb share events per trooper wave, before being declared lower priority. A low priority player is not counted for when deciding how many souls to generate. Example: if a player is near 4 troopers from Wave 1 when they die, then moves to a different lane that has an allied hero still fighting Wave 1 troopers, that player will no longer cause the wave to double the souls generated as is the case now, as they are considered a low priority player for that wave. The generated Souls will then be split as normal.

**2024-11-21_HeroLab**

- Vexing Bolt: Now always casts alongside your Assistant, at reduced damage
- Spectral Assistant: Now fires in a burst of two.
- Spectral Assistant: Tracer now matches weapon tracer
- Spectral Assistant: Fix a bug where sometimes, you couldn't redirect your bolts after the Assistant casts it
- Spectral Assistant: Reduce cast range from 20m to 15m

**2024-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2024-update.47476/))

- Soul Sharing ratios post-lane reduced from 100/70/45/33/25/20% to 100/60/35/25/20/16%  (for 1/2/3/4/5/6 players, original was 100/50/33/25/20/16%)
- Initial Urn bounty reduced from 4050 to 3000 (changed from 1750 + 230*Min to 700 + 230*Min)

**2024-11-13** ([forum post](https://forums.playdeadlock.com/threads/11-13-2024-update.46391/))

- Soul Sharing ratios post-lane reduced from 100/75/50/35/28/22% to 100/70/45/33/25/20% (for 1/2/3/4/5/6 players)
- Team vs Team NW comeback formula toned down

**2024-11-10** ([forum post](https://forums.playdeadlock.com/threads/11-10-2024-update.45689/))

- Soul Sharing ratios post-lane reduced from 100/100/66/50/40/33% to 100/75/50/35/28/22% (for 1/2/3/4/5/6 players)

**2024-11-07_HeroLab**

- Spectral Assistant: Now castable in the air

**2024-11-07** ([forum post](https://forums.playdeadlock.com/threads/11-07-2024-update.44786/))

- Fixed Grey Talon getting assist credit while flying Guided Owl
- Fixed using melee to secure orbs being a little unresponsive
- Troopers no longer change soul sharing rules after laning phase ends (meaning 2 heroes don't split souls)
- Troopers no longer increase their bounty by 20% at 8 minutes

**2024-10-24** ([forum post](https://forums.playdeadlock.com/threads/10-24-2024-update.40951/))

- Fixed issue in several languages where team net worth number shrunk to an unreadable size
- Denied orb sound will no longer play beyond 2500 game units from the player
- Bots will prioritize assisting human allies on offense
- Shrine/Patron no longer have Soul/AP bounties
- Trooper Soul Orbs now have a 90ms buffer to allow the server to do better calculations on who shot the orb first, to minimize latency advantages for denying
- Urn comeback properties now require an 8% net worth lead to kick in
- Urn pickup locations are the same as before, however now the drop-off locations will be variable based on which team is leading. If there isn't a lead over 8% net worth, then the drop-off location is the same as before. If there is, then the drop-off location will be closer to the losing team's side. The minimap will show where the drop-off location is as usual, as well as an indicator in the world that helps show you where it is.

**2024-10-15** ([forum post](https://forums.playdeadlock.com/threads/10-15-2024-update.38925/))

- Base kill bounty reduced from 225 to 150 (still scales to 1400 over time)

**2024-10-10** ([forum post](https://forums.playdeadlock.com/threads/10-10-2024-update.36958/))

- Fixed an Unsecured Souls bug where it gave extra bounty directly to the dying hero carrying unsecured souls
- Fixed a bunch of bugs that were impacting how VO was playing in a match.  Now a bunch of hero VO that was previously getting squashed/cut off should play properly (for instance certain lines where allies commented on ability usage, the patrons giving compliments for assists/team healing, etc).
- Trooper spawn/bounty lane end time changed from 10 min to 8 min
- Urn bounty increased by 15%
- Comeback formula weighted a bit less on team vs team net worth calculation and more on the strength of the dying hero (regardless of lead)

**2024-09-26** ([forum post](https://forums.playdeadlock.com/threads/09-26-2024-update.33015/))

- Added a First Blood bonus bounty for the first kill each player gets. Grants 150 bonus souls.
- Some latency-related calculation improvements that help orbs be a little less deny favored
- Orbs now appear a little smaller to the enemy that is trying to deny them
- Troopers no longer give half bounty when base guardians are destroyed for that lane
- Killer to Assist bounty ratio reduced from 2.0 to 1.7 (slightly more to assists)
- Fixed Sinner's Sacrifice sharing bounty to nearby allies

**2024-09-17** ([forum post](https://forums.playdeadlock.com/threads/09-17-2024-update.30413/))

- Fixed players being able to exploit soul sharing across multiple lanes to earn more souls than intended. The way the fix is implemented is that each player can only be considered for an enemy trooper death event 4 times per wave number during the laning phase.

**2024-08-15** ([forum post](https://forums.playdeadlock.com/threads/08-15-2024-update.16378/))

- Fixed some cases where the comeback souls would be higher than intended in the early game

**2024-08-01** ([forum post](https://forums.playdeadlock.com/threads/08-01-2024-update.13369/))

- Improved distinction between orb collect and orb deny sounds
- Soul Orbs now fly out in different initial directions before floating up. There is a 1/3rd chance it goes left, 1/3rd chance it goes right, and 1/3rd chance it goes up.

**2024-07-18** ([forum post](https://forums.playdeadlock.com/threads/07-18-2024-update.11831/))

- Removed the long fx trail from unsecured souls on your hero so it doesn't give away your position when juking/hiding
- Reworked comeback formula to be less weighted towards team vs team net worth and more towards the net worth of the dying hero compared to the average of your team (regardless if your team is leading or not)

**2024-07-11** ([forum post](https://forums.playdeadlock.com/threads/07-11-2024-update.10871/))

- Added in-world confirmation text when an enemy denies your soul orbs
- Urn bounty increased from 900 + 200/min to 1500 + 200/min (10 min spawn goes from 2900 to 3500)
- Trooper gold sharing radius from the location of the soul orb increased from 50m to 60m
- Fixed dropping unsecured souls not lowering your net worth
- Fixed a bug that caused denies during the laning phase to sometimes be shared with allies and sometimes not
- Some tweaks to how the comeback formula works have been done over the past couple days and we'll continue iterating on it over the coming days

**2024-07-04** ([forum post](https://forums.playdeadlock.com/threads/07-04-2024-update.9652/))

- All instances of collecting souls (whether claiming your own or denying an opponent) will share the same sound. Being denied a soul orb by an enemy will have its own unique sound.

**2024-06-27** ([forum post](https://forums.playdeadlock.com/threads/06-27-2024-update.8486/))

- Urn now spawns on both sides of the map. Bounty for each is reduced by 40%

**2024-06-20** ([forum post](https://forums.playdeadlock.com/threads/06-20-2024-update.7003/))

- Vault bounty increased from 300 to 330
- Passive: Anytime you secure or deny a Soul, you get 2 ammo back and have +20% Fire Rate for 4 seconds.

**2024-06-13** ([forum post](https://forums.playdeadlock.com/threads/06-13-2024-update.5773/))

- Urn reward now has a comeback component where it gives extra gold for the team that is behind based on the magnitude
- A small share of the comeback portion of hero kill bounty is now given to each other player outside of just the kill/assist players. This also makes the amount the killer gets be more consistent, previously the amount could vary significantly based on how many people were involved. The killer and assist players still get the bigger shares.
- Kill assist window increased from 7s to 10s

**2024-06-06** ([forum post](https://forums.playdeadlock.com/threads/06-06-2024-update.4096/))

- Strong neutrals souls bounty reduced by 20%

**2024-05-23** ([forum post](https://forums.playdeadlock.com/threads/05-23-2024-update.1245/))

- Hero kill bounty ratio between Killer and Assister reduced from 2.75x to 2.55x (means slightly more to the Assister)
- Vaults base bounty increased from 220 to 260

**2024-05-13** ([forum post](https://forums.playdeadlock.com/threads/05-13-2024-update.807/))

- Vault base bounty increased from 200 to 225

**2024-05-03** ([forum post](https://forums.playdeadlock.com/threads/05-03-2024-update.427/))

- Urn bounty increased from 900 + 160/minute to 900 + 200/minute
- Vaults base bounty increased from 150 to 200
