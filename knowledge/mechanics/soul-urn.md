# Soul Urn

Generated from the game files at build 6868 and Valve's patch notes. Everything below is quoted from a source, not interpreted. Patch notes describe the game as of their date: read newest first, and treat an older line as history once a newer one changes the same thing. The patch notes do not record every change, so where a current number below differs from the newest note, the number is right. Questions already worked through are answered in [settled.md](../settled.md).

## What the game itself says

- Heavy Melee to contest Soul Urn (`AbilityButtonHint_MeleeIdolCashIn`)
- Melee to pick up Soul Urn (`AbilityButtonHint_MeleeIdolPickup`)
- +35% Extra Souls (`golden_idol_bonus_01`)
- +1 Ability Point (`golden_idol_bonus_02`)

## Current numbers in the game files

Server settings (`convars.json`)

| Setting | Value |
|---|---|
| citadel_crate_respawn_interval | 300 |
| citadel_crate_reward_base | 250 |
| citadel_crate_reward_time_multiplier | 70 |
| citadel_crate_spawn_initial_delay | 600 |
| citadel_idol_cashin_buff_count | 4 |
| citadel_idol_decay_duration | 45 |
| citadel_idol_duration_until_decay | 45 |

## Patch history (163 lines, newest first)

**2026-07-09** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1836506165584438))

- Urn Runner sprint bonus reduced from +2m to 0 (trailing bonus reduced from +7m to +5m)
- Urn Runner move speed bonus reduced from +3.5m to +2m
- Urn Runner Stamina Recovery increased from +15% to +25%
- Urn talking frequency increased from every 8s to every 6s
- Urn talking sound distance increased (easier to hear a nearby Urn Runner)

**2026-06-30** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1836506165563227))

- Unstable Rift no longer requires an Urn delivery to trigger the start of the event. It now has a variable start time of +/- 1 minute. There is a global announcement 25s before it spawns. 60s before that there is also an in-world only visual effect to let you know which lane it'll randomly spawn in.
- Unstable Rift bounty increased by 35% (to account for the 35% loss with no urn runner bounty, overall objective bounty is unchanged)
- Unstable Rift no longer grants +1 permanent buff to each player (there is also no +3 buffs to the urn runner)
- Urn running is now its own objective. Spawns on either end of the map (where the previous neutral pickup locations were), and gets delivered to the opposite end. Spawns at 10/15/20/25/etc.
- Urn runner is no longer revealed and is not disarmed or silenced (going through a doorway or mirage teleport still drops it)
- Urn cannot be manually dropped. It gets dropped when you get hit with a light or heavy melee, are stunned or are killed. It stays where it drops and does not walk back home.
- Urn runner can no longer parry
- Urn bounty value starts decaying after 45s from being picked up. It drains gradually over another 45s and then the urn is removed when the bounty is empty.
- Urn is deposited immediately at the drop off point.
- Urn bounty when deposited is worth 250 + 70/min for just the urn runner. Still has the comeback bounty component. Upon deposit all of the souls are released as orbs into the air (if another ally secures the orbs, they share the bounty with the urn runner).
- Urn runner gets +4 permanent buffs on deposit
- Urn is now louder when it talks and is easier to hear by nearby enemies
- After 3 Minutes from spawn the Urn will start walking very slowly on his own towards the deposit location
- Urn runner's passive bonuses while holding it now scales based on how behind you are, rather than being on or off (same as the Unstable Rift 0%-15% NW linear scaling). Bonuses are the same as the previous urn runner bonuses.
- citadel_force_spawn_idol - This spawns the Urn

**2026-06-11** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1835236783562074))

- Urn give up time reduced from 75s to 60s
- Urn bounty reduced by 10% (unreduced for trailing team)

**2026-06-04** ([forum post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1834602721188293))

- Urn mechanics have been reworked.
- Delivering the urn now starts a king of the hill style capture point, rather than using melee to flip the urn back and forth.
- Both teams can progress at the same time, but the urn will only be fully claimed once there is only one team in the circle.
- The Urn runner now gets their normal 35% bonus bounty and stats immediately on initial deposit (rather than on deposit conclusion only if your team won it)
- Urn overall bounty reduced by 20% (unreduced for trailing team)
- If Urn has been in progress for over 75s, it will give up and throw all the souls as orbs into the sky (they will float for a long time)
- Increased time allowed to run the urn before taking damage by 10s
- Urn comeback resistance now also grants +35% Debuff Resistance ontop of the 35% Bullet and Spirit Resistance
- Urn comeback resistance aura reduced from 60m to match the 20m progress radius

**2026-05-28** ([forum post](https://forums.playdeadlock.com/threads/05-22-2026-update.135477/post-261657))

- {{EntityIcon|Soul Urn|l1=Urn}} spawn time and interval changed from 10/15/20/25/etc to 12/18/24/30/etc
- Urn timer now gets frozen with Frozen Shelter
- Urn no longer provides the +35% Bullet and Spirit Resist aura for the behind team when it is being carried or dropped. The aura is now only active when it is being deposited.
- Urn runner when behind now gains +35% Bullet and Spirit Resist for themselves only
- Fixed the trailing team Urn runner's extra sprint bonus not working properly
- Urn will do damage to the runner after a team has held it for 30s (was 50s before), however, this timer will freeze while there are enemies within a 40m radius of the urn runner.
- Urn will now always add at least 2s to the team 30s held timer limit anytime it is picked up, even if it is instantly dropped
- You are no longer prevented from picking up the urn for 12s after it is dropped after the previous 50s team held timer
- The conditions for when the Urn decides to run back home have been reworked. The Urn will now stay in place on the ground as long as there are enemies in a 40m radius (enemies of the last person to have dropped or fumbled the Urn). If there are no enemies, then the Urn will wait up to 13s if there is a friendly player in a 40m radius.
- If the Urn held timer is over 45s (keeping in mind this timer is frozen if there are nearby enemies), the next time it is dropped it will immediately run back home if there are no nearby enemies.
- Urn spawn time and interval changed from 10/15/20/25/etc to 12/18/24/30/etc - Urn timer now gets frozen with Frozen Shelter - Urn no longer provides the +35% Bullet and Spirit Resist aura for the behind team when it is being carried or dropped. The aura is now only active when it is being...

**2026-05-25** ([forum post](https://forums.playdeadlock.com/threads/05-22-2026-update.135477/post-259788))

- Urn drop off point is moved from the above bridge in the mid lane to under the bridge in the side lane
- Urn timer extension when contested increased from 1.25s to 3s
- Urn deposit timers for favored/neutral/unfavored increased from 3/5/10s to 5/10/15s
- Urn comeback bullet and spirit resist auras reduced from 50% to 35%
- Urn pickup spot is now where the old comeback drop off spots were for when your team is behind
- Urn runner no longer has sprint disabled
- Urn runner now has max sprint acceleration
- Urn runner now gains +2m Sprint, +1 Stamina, +10% Dash Distance and +15% Stamina Regen
- Urn runner for the team that is behind now gains an extra +4m Sprint
- Urn collision radius increased by 20%
- Various smaller urn holding timers and variables adjusted to account for the new location
- Please continue to give feedback on the Urn as we work through iterations on it.

**2026-05-22** ([forum post](https://forums.playdeadlock.com/threads/05-22-2026-update.135477/))

- We are experimenting with an alternate set of Urn mechanics. Please give us your thoughts on this after you've played with it some.
- To pickup the Urn, rather than standing in place to channel, you now light or heavy melee the Urn to pick it up.
- The Urn is now always dropped off on top of the bridge on the middle of the map.
- Once dropped off, the Urn will go into a "Depositing" phase for a set amount of time, depending on which team the urn favors (3s/5s/10s for Favored/Neutral/Unfavored).
- While in the Depositing phase, the enemy team can Heavy Melee the urn to have their team claim it and cause it to switch sides. This adds +1.25s to that team's timer.
- If the urn is Favored or Unfavored (in a comeback state), then the Favored team will get +50% Bullet and Spirit Resist in a 60m radius around the urn while it is being carried, dropped or deposited.
- Urn damage is lethal
- Like before, when the Urn is fumbled, it will wait 13s if there is a player within 25m. However afterwards, with this new version, it can no longer be picked up anymore and will very quickly run back to its spawn position.
- Area around deposting the urn is revealed (urn runner is also revealed as usual)
- The rules for Favored/Unfavored remain the same (+15% soul difference for the first urn at 10:00, +10% for all future urns)
- All rewards are the same. The last person to contest the urn gets the +3 Golden Idol buffs, falling back to the original carrier if nobody contested it.

**2026-03-06** ([forum post](https://forums.playdeadlock.com/threads/03-06-2026-update.114328/))

- Minimap now indicates if the Urn is a favored, neutral or unfavored

**2026-01-20** ([forum post](https://forums.playdeadlock.com/threads/12-29-2025-update.95233/post-185824))

- Urn no longer requires a drop off channel time
- Urn is now knocked out of your hands with a light melee (instead of only with a heavy melee)
- Urn pickup channel time is reset if you get hit with a light or heavy melee
- Can no longer parry while channeling to pickup the urn
- Urn carrier resist reduced from 50% to 30%
- Urn now drops if it travels through doorman portals

**2025-12-16** ([forum post](https://forums.playdeadlock.com/threads/12-16-2025-update.93983/))

- Urn: Bounty increased from 700 + 230/min to 1300 + 230/min
- Urn: Comeback bounty now gives more souls
- Urn: Bullet and Spirit resist for carrier increased from 30% to 50%
- Urn: Bonus bounty for carrier increased from 25% to 35%

**2025-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2025-update.90383/))

- Dropping / Throwing the Urn now causes Parry to go on CD
- Soul Urn no longer grants +1 AP to the person dropping it off
- Soul Urn now provides 4 Permanent Buffs to the person dropping it off

**2025-10-02** ([forum post](https://forums.playdeadlock.com/threads/10-02-2025-update.84332/))

- Soul Urn: Carriers now have +30% bullet and +30% spirit Resist
- Soul Urn: Movespeed bonus reduced from +7m to +3.5m
- Soul Urn: Damage taken when holding too long increased from 1% to 1.5% Max Health per second

**2025-06-17** ([forum post](https://forums.playdeadlock.com/threads/06-17-2025-update.68401/))

- Time holding Urn before taking damage reduced from 90s to 45s (1% max health damage per second)
- Time Urn will Autorun back to Home regardless of nearby players reduced from 75s to 45s
- Time an Urn will wait for a nearby player to pick it up reduced from 20s to 12s

**2025-05-27** ([forum post](https://forums.playdeadlock.com/threads/05-27-2025-update.66453/))

- Fixed a bug where Urn can be invisibly carried on the hero by throwing it in certain areas like the air vents

**2025-05-21** ([forum post](https://forums.playdeadlock.com/threads/05-21-2025-update.65674/))

- Added Breakable souls to the post game Souls by Source graph (was previously bundled in with Urn)

**2025-04-17** ([forum post](https://forums.playdeadlock.com/threads/04-17-2025-update.61382/))

- Urn now reveals you immediately
- First urn is now considered for comeback mechanics (15% NW delta)
- Urn now has a visual indication on the model to indicate if its a side favored pickup
- Urn will no longer wait indefinitely for someone nearby to pick him up. He'll ignore loiterers after 20 seconds in aggregate and start running back home
- Fixed Debuff Resistance affecting Urn pickup time

**2025-04-04** ([forum post](https://forums.playdeadlock.com/threads/04-04-2025-update.60284/))

- Fixed Ivy, Viscous and Magic Carpet moving faster than desired when holding the soul urn
- Urn reveal time reduced from 25s to 15s
- Urn speed limit increased from 13 m/s to 15 m/s

**2025-01-19** ([forum post](https://forums.playdeadlock.com/threads/01-19-2025-update.53961/))

- The Magnificent Sinclair: Teleporting now drops the Urn

**2024-12-06** ([forum post](https://forums.playdeadlock.com/threads/12-06-2024-update.50599/))

- Carrying Urn now sets and limits your movespeed to a fixed 13 (this includes things like Ivy Air Drop). It no longer provides sprint. The speed cannot be reduced or increased.
- Urn spawn point now alternates left and right starting with left, rather than being random

**2024-11-21** ([forum post](https://forums.playdeadlock.com/threads/11-21-2024-update.47476/))

- Urn time to reveal increased from 20s to 25s
- Initial Urn bounty reduced from 4050 to 3000 (changed from 1750 + 230*Min to 700 + 230*Min)
- Adding an alternate Urn mechanic as an experiment for 2 days. This will be enabled this weekend only and Monday will be back to normal. Urn pickup location is the same, but drop-off location is now always at the top of mid temple. The bonus souls the team gets is reduced by 60% (the delivering player reward is unchanged). The reveal time is now 40s.

**2024-11-13** ([forum post](https://forums.playdeadlock.com/threads/11-13-2024-update.46391/))

- First Urn is now always neutral regardless of NW lead

**2024-11-07** ([forum post](https://forums.playdeadlock.com/threads/11-07-2024-update.44786/))

- Biased Urn delivery locations moved slightly closer to neutral positions
- Moved the stairs from the warehouse interior to the underground tunnel further from the Urn delivery location

**2024-10-27** ([forum post](https://forums.playdeadlock.com/threads/10-27-2024-update.42492/))

- Urn NW lead requirement increased from 8% to 10%

**2024-10-24** ([forum post](https://forums.playdeadlock.com/threads/10-24-2024-update.40951/))

- Urn comeback properties now require an 8% net worth lead to kick in
- Urn pickup locations are the same as before, however now the drop-off locations will be variable based on which team is leading. If there isn't a lead over 8% net worth, then the drop-off location is the same as before. If there is, then the drop-off location will be closer to the losing team's side. The minimap will show where the drop-off location is as usual, as well as an indicator in the world that helps show you where it is.
- If the Urn hasn't been delivered within 90 seconds of pickup time, it now drains your health for 1% of Max HP per second (the timer is per team). Your regen is disabled during this.
- Whenever the Urn is dropped after 90 seconds of pickup time, it starts moving back to its spawn point immediately and cannot be picked up by the same team for 12 seconds.
- Increased speed Urn walks back
- Redesigned stairs from central canal to the outer lanes (near Urn spawn)

**2024-10-15** ([forum post](https://forums.playdeadlock.com/threads/10-15-2024-update.38925/))

- Urn now reveals you after 20s from initial pickup
- Urn sprint changed from +3/5 for winning/losing team to +2/6

**2024-10-10** ([forum post](https://forums.playdeadlock.com/threads/10-10-2024-update.36958/))

- Fixed a bug where the bot that would pick up the Urn was not the closest one, just the one that was in the highest player slot
- Increased the time you need to carry the urn before the urn nags about not being delivered
- Urn now causes the runner to be revealed on the minimap
- Heavy Melee against the urn runner now causes them to drop the urn
- Urn delivery now gives each player on your team a Golden Statue permanent buff
- Urn bounty increased by 15%
- Urn now falls down from the sky a little bit faster

**2024-09-29** ([forum post](https://forums.playdeadlock.com/threads/09-29-2024-update.34541/))

- Urn now drops when teleporting with Mirage's Traveler

**2024-09-26** ([forum post](https://forums.playdeadlock.com/threads/09-26-2024-update.33015/))

- Added connection from canal near the urn platforms through the Radio Station and Apartment buildings

**2024-09-12** ([forum post](https://forums.playdeadlock.com/threads/09-12-2024-update.27974/))

- Added little spirit frog legs to the Soul Urn

**2024-08-29** ([forum post](https://forums.playdeadlock.com/threads/08-29-2024-update.22253/))

- Urn delivery sprint bonus increased from +2 to +3

**2024-08-15** ([forum post](https://forums.playdeadlock.com/threads/08-15-2024-update.16378/))

- Replaced the Urn drop parachute with new effects
- Fixed a bug that allowed teleporters to be used while carrying the Soul Urn

**2024-08-01** ([forum post](https://forums.playdeadlock.com/threads/08-01-2024-update.13369/))

- Fixed a bug with Urn that could cause you to be permanently silenced
- Urn now gives the team that is behind +2 more sprint when carrying it

**2024-07-23** ([forum post](https://forums.playdeadlock.com/threads/07-23-2024-update.12505/))

- Fixed bot behavior with the new Urn locations

**2024-07-18** ([forum post](https://forums.playdeadlock.com/threads/07-18-2024-update.11831/))

- Removed voice lines / fixed text that referenced the urn being delivered to the temple
- Can no longer use the Teleporter while carrying the Urn

**2024-07-11** ([forum post](https://forums.playdeadlock.com/threads/07-11-2024-update.10871/))

- Added HUD Notifications on Soul Urn drop off to let depositor know they gained +25% Souls and +1 AP
- Fixed Soul Urn walking back while the game is paused
- Urn now grants the Urn Runner +1 AP
- Urn Runner now gains +2 sprint and is disarmed while carrying the Urn
- Urn bounty increased from 900 + 200/min to 1500 + 200/min (10 min spawn goes from 2900 to 3500)
- Urn display on the minimap is now pulsing a green rectangle showing where the destination is if an ally is carrying the urn, and a red rectangle at the destination if an enemy is carrying it

**2024-07-04** ([forum post](https://forums.playdeadlock.com/threads/07-04-2024-update.9652/))

- Fixed the HUD cooldown state thrashing while picking up the Soul Urn
- Minimap now highlights Soul Urn dropoff location
- Urn count changed from 2 to 1 (previous souls value restored)
- Urn pickup location moved to closer to the outer lanes (on the opposite side of the lane pillar, facing towards the bridge)
- Urn drop-off location now move to the same spot as the pickup (opposite end of the map, depending on which location the Urn spawns in)
- Urn pickup time reduced from 4s to 2s
- Urn now has a 2s drop-off time
- Urn no longer applies a 15% slow
- Urn now prevents you from using the zipline while carrying it
- The person delivering the urn now gets +25% soul bonus

**2024-06-27** ([forum post](https://forums.playdeadlock.com/threads/06-27-2024-update.8486/))

- Urn now spawns on both sides of the map. Bounty for each is reduced by 40%

**2024-06-16** ([forum post](https://forums.playdeadlock.com/threads/06-16-2024-update.6424/))

- Carrying the Soul Urn no longer causes your hero to be revealed to enemies

**2024-06-13** ([forum post](https://forums.playdeadlock.com/threads/06-13-2024-update.5773/))

- The Patrons no longer care about the well being of the Urn Runner, and so they will stop asking you to protect them (patrons will no longer call out the urn being picked up)
- Urn reward now has a comeback component where it gives extra gold for the team that is behind based on the magnitude
- If the Soul Urn is dropped it goes back to its original spot a little bit faster
- Carrying the Soul Urn no longer causes you to get slowed briefly by 50% when you get shot
- Carrying the Soul Urn now always slows you by 15%
- Carrying the Soul Urn now also silences your items
- The silence effect for Soul Urn now applies as you start channeling to pick it up (0.5s after touching it, to prevent accidental walk overs)

**2024-05-30** ([forum post](https://forums.playdeadlock.com/threads/05-30-2024-update.2514/))

- Extended inner lane urn bridge buildings toward the T1 and added a doorway to allow defenders to shoot down into the canal
- Removed 3 bush trees on each inner lane near the urn bridge buildings

**2024-05-23** ([forum post](https://forums.playdeadlock.com/threads/05-23-2024-update.1245/))

- Sped up select Amber Hand VO that related to game state (shrines being under attack, protecting the urn runner etc)
- Fixed the Idol falling during pause

**2024-05-13** ([forum post](https://forums.playdeadlock.com/threads/05-13-2024-update.807/))

- Fixed visual bug on Spirit Urn when dropping on the ground

**2024-05-03** ([forum post](https://forums.playdeadlock.com/threads/05-03-2024-update.427/))

- You are now silenced while carrying the Urn
- Urn bounty increased from 900 + 160/minute to 900 + 200/minute
