# How Deadlock's systems fit together, read from the game's numbers

Data: `main` branch, game build **6868** (2026-11-24), cross-checked against the raw game files with 0 disagreements (`output/REPORT.md`, `output/meta.csv`).

## How to read this

Every claim carries one of these labels:

| Label | Meaning |
|---|---|
| **[Data]** | Read directly from a CSV in `output/`. Find it by the hero, ability or item named. |
| **[Computed]** | Arithmetic I did on the CSVs. I ran all of these in Python against the files. The method is given with each one so you can redo it. |
| **[Game text]** | Valve's own in-game wording, quoted in `knowledge/game_text.md` or `knowledge/mechanics/*.md`. `main` has these files; the older working branch does not. |
| **[Patch notes, date]** | A Valve patch-note line from `knowledge/`. It was true on that date. A later patch can change it, and where it disagrees with the data, the data wins. |
| **[Outside]** | Something I know about Deadlock from outside this repository. It may be out of date. |
| **[Assumption]** | A rule about how stats combine. The game files don't contain these rules, so I state the assumption so the arithmetic can go ahead, and say how to test it. |

Two assumptions come up repeatedly. I name them once here:

- **A1 (resists):** a resist of R% multiplies incoming damage of that type by (1 − R/100), so effective HP = HP / (1 − R/100). *Test:* in the sandbox, shoot a target with and without one resist item and compare the combat-log numbers.
- **A2 (weapon damage):** weapon damage % from investment and from items adds into one bonus. That bonus multiplies the hero's current bullet damage, including what boons have added. *Test:* note one bullet's damage, buy a +8% item, and check whether the number rises by 8% of the current value or of the level-0 value.

---

# Part 1. The systems, one at a time

## 1. The soul economy and how power grows over a match

### Souls are the one currency, and spending them is only half of what they do

Collecting souls grants things on its own, before you spend anything **[Data, `progression.csv`]**. Each of the 35 thresholds grants one **boon**. Most thresholds also grant either an **ability point** or an **ability unlock**:

- 4 ability unlocks, at 0, 500, 1,400 and 3,200 souls. You have all four abilities available by 3,200.
- 32 ability points by the last threshold (48,600 souls).
- 35 boons by 48,600 souls.

Boons get more expensive as the match goes on **[Computed: souls between thresholds]**:

| Boons | Souls range | Average souls per boon |
|---|---|---|
| 1–9 | 0 → 4,600 | 511 |
| 10–19 | 4,600 → 12,800 | 820 |
| 20–29 | 12,800 → 29,400 | 1,660 |
| 30–35 | 29,400 → 48,600 | 3,200 |

Snapshots at the two soul counts you asked about **[Data]**:

| Souls collected | Threshold reached | Boons | Unlocks | Ability points |
|---|---|---|---|---|
| 5,000 | level 9 (4,600) | 9 | 4 | 6 |
| 10,000 | level 15 (9,200) | 15 | 4 | 12 |
| 20,000 | level 24 (18,900) | 24 | 4 | 21 |
| 30,000 | level 29 (29,400) | 29 | 4 | 26 |

**[Outside]** Thresholds count souls *collected* (net worth), not souls spent, so unspent souls still level you.

**A conflict, where the data wins.** The game's own string says "1 Ability Point gained at levels 2, 3, 5, 7, and each level after" **[Game text, `Citadel_Player_Level_AbilityPoints`]**. `progression.csv` gives points at its levels 1, 3, 5, 6, 8, 9, … That doesn't match whichever way you number the levels. The patch notes say the boon reward table was reworked on 2026-06-30 **[Patch notes, 2026-06-30]**, so the string is probably left over from before that. Trust the CSV.

### Where souls come from

**[Data, `rules.csv`, `units.csv`]**

- **Objectives**, in souls: Guardian 1,375, Walker 3,675, Base Guardian 1,000, Shrine 2,000. 25% of each bounty is the "share for nearby players".
  - **[Patch notes, 2026-09-16]** "the remaining gets split between all 6 players".
  - The same patch raised the Guardian bounty by 10% and the Walker bounty by 5%. From the 2026-06-30 values (1,250 and 3,500) that gives exactly 1,375 and 3,675 **[Computed]**. So the data and the patch notes agree here.
- **Neutral camps:**

  | Creep | Souls | First spawn | Respawn |
  |---|---|---|---|
  | Small | 45 | 120 s | 85 s |
  | Medium | 75 | 300 s | 290 s |
  | Large | 199 | 480 s | 335 s |
  | Sinner's Sacrifice | 155 | 480 s | 300 s |

  Each grows by `soul_reward_growth_pct_per_minute` = 1.08. The data doesn't say whether that growth is linear or compounding.
- **Troopers:** `soul_reward` is blank in `units.csv`. The most recent patch line found is "Trooper bounty rescaled from 116 + 1.16/m to 100 + 2/m" **[Patch notes, 2026-06-30]**. Treat it as dated.
- **Hero kills:** the base bounty isn't in the sheet. **[Patch notes, 2026-06-30]** "Base kill bounty reduced from 250 to 200 (max is still 2200 at 40m)". Comeback bounties are layered on top. They were changed several times in 2026 and aren't in the data.

### Sharing: troopers keep their value when shared, hero kills lose it

`rules.csv` lists a per-player fraction for 1 to 6 sharers. Multiply each fraction by the number of sharers to get the total souls the kill creates **[Computed]**:

| Sharers | Trooper: each gets | Trooper: total | Hero kill: each gets | Hero kill: total |
|---|---|---|---|---|
| 1 | 1.00 | 1.00 | 1.25 | **1.25** |
| 2 | 0.54 | 1.08 | 0.575 | 1.15 |
| 3 | 0.36 | 1.08 | 0.283 | 0.85 |
| 4 | 0.25 | 1.00 | 0.175 | 0.70 |
| 5 | 0.20 | 1.00 | 0.11 | 0.55 |
| 6 | 0.16 | 0.96 | 0.083 | **0.50** |

Assuming "share" means the fraction of the bounty each nearby player receives (the README says the wording is an interpretation of the field name):

- Trooper souls are roughly conserved however many people share them, with an 8% bonus for 2 or 3 players.
- A hero kill made alone creates 2.5 times the souls of the same kill shared six ways.

The economy rewards spreading out and getting picks, and charges a soul cost for grouping. That cost is offset by whatever the group's fighting wins. *Check in game:* compare the soul popup for a solo kill with a two-person kill on the same target.

## 2. The three stat families: weapon, vitality, spirit

The shop has three tabs. Each one feeds one **investment bonus** that grows with the souls you have spent in that tab **[Data, `investment.csv`]**:

| Souls spent in the tab | Weapon (weapon damage) | Vitality (health) | Spirit (spirit power) |
|---|---|---|---|
| 800 | 9 | 9 | 7 |
| 1,600 | 12 | 12 | 11 |
| 3,200 | 18 | 20 | 19 |
| **4,800** | **46** | **38** | **38** |
| 8,000 | 62 | 46 | 52 |
| 16,000 | 86 | 54 | 66 |
| 28,800 | 115 | 66 | 100 |

**Units.** The files don't say whether each bonus is a percentage or a flat amount. The game text and patch notes settle most of it:

- **Weapon** is a percentage: "Total Bonus to your Gun and Melee Damage gained from buying items in the Weapon tree" **[Game text]**, and the patch notes write it in % **[Patch notes, 2026-04-30, 2026-05-22]**. It applies to gun and melee damage.
- **Vitality** is a percentage of base health: "Total Bonus to your *Base* Health gained from buying items in the Vitality tree" **[Game text]**. It was switched back "to % base hp increase rather than raw constant bonus" **[Patch notes, 2026-03-21]**. What "base health" means is an open question, covered in §7.
- **Spirit** is flat spirit power. The investment is labelled "Spirit Power Increases" **[Game text]**, and the patch notes always write it as a plain number.

**Marginal rate per 1,000 souls spent** **[Computed: Δbonus / Δsouls between rows]**:

| Segment | Weapon (pts per 1k) | Vitality (pts per 1k) | Spirit (pts per 1k) |
|---|---|---|---|
| 0 → 800 | 11.2 | 11.2 | 8.8 |
| 800 → 3,200 | 3.8 | 3.8–6.2 | 5.0 |
| **3,200 → 4,800** | **17.5** | **11.2** | **11.9** |
| 4,800 → 8,000 | 5.0 | 2.5 | 4.4 |
| 8,000 → 22,400 | 2.2–3.8 | 0.8–1.2 | 1.4–2.2 |
| 22,400 → 28,800 | 2.3 | 0.9 | **3.9** |

The curves aren't smooth. Each one has two steps, at the first 800 and at 4,800, followed by long flat stretches. Spirit also gets a late bump at 28,800 (75 → 100). Vitality flattens hardest after 4,800. The 4,800 row is a designed highlight **[Patch notes, 2025-11-21]**: "Added a UI highlight to 4800 reward row of the investment bonuses".

### What each family buys

Read from the items' always-on columns (`items.csv`) and the game's stat descriptions **[Data, Game text]**:

- **Weapon:**
  - Always-on: weapon damage %, fire rate %, ammo %, bullet velocity, falloff range, plus melee for some items.
  - Effects (procs): bullet procs such as Tesla Bullets' shock (33 + 0.19 × spirit power), Toxic Bullets' bleed with −40% incoming healing, and Headshot Booster (+45 damage, 9 s cooldown).
  - Effects (conditional bonuses): Close Quarters (+20% weapon damage within 15 m) and Intensifying Magazine (up to +45% weapon damage after 2.5 s of firing).
- **Vitality:**
  - Health, regeneration (in combat and out of combat), bullet and spirit resist, lifesteal, debuff resist, stamina and movement.
  - Defensive actives: Colossus (35% bullet and spirit resist for 7 s), Warp Stone, Majestic Leap, Healing Rite and Rescue Beam.
- **Spirit:**
  - Spirit power, cooldown reduction (Compress Cooldown 18%, Superior 20%, Transcendent 25%), ability duration (Duration Extender 22%), radius (Mystic Expansion 20%) and ability charges (Extra Charge +1, Rapid Recharge +2).
  - Spirit procs: Mystic Burst and Spirit Strike (40 + 0.372 × spirit power).
  - Enemy debuffs: Mystic Vulnerability (−8% spirit resist) and Escalating Exposure (+4.5% spirit amp per stack, up to 12).

The shop category doesn't decide which stats an item gives **[Computed: counting non-blank stat columns by category]**:

- Spirit power appears as an always-on stat on 10 Vitality items, 7 Spirit items and 4 Weapon items. Examples are Enchanter's Emblem (Vitality T2, 15 SP) and Witchmail (Vitality T4, 14 SP).
- Bonus health is always-on on 17 Spirit items, 18 Vitality items and 12 Weapon items.

**[Computed]** What the category decides is which investment bar the souls fill. Section 8 comes back to this.

## 3. Heroes: how they differ at baseline and how they scale

A hero's stat at a given number of boons is `base + per_boon × boons` **[README]**. Applied to all 44 heroes **[Computed]**:

| Stat | Min | Median | Max |
|---|---|---|---|
| Base health | 660 (Mina) | 780 | 930 (Mo & Krill) |
| Health per boon | 27 (Mina) | 41.5 | 65 (Mo & Krill) |
| Health at 29 boons | 1,443 (Mina) | 1,967 | 2,815 (Mo & Krill) |
| Gun DPS at 0 boons (`weapon_dps_level_1`) | 28.4 (Baba) | 52.3 | 94.0 (Vyper) |
| Gun DPS gained per boon | 0.51 (Graves) | 1.49 | 2.54 (Vyper) |
| Gun DPS at 29 boons | 50.1 (Graves) | 99.6 | 167.8 (Vyper) |
| Gun DPS growth, 0 → 29 boons | +42% (Graves, Warden) | +79% | +168% (Holliday) |
| Spirit power per boon | 0.5 (Haze) | 1.1 (37 of 44 heroes) | 1.6 (Grey Talon) |

I checked that `weapon_dps_level_1` is the 0-boon value. Abrams: 34.02 damage per shot × 1.5873 shots per second = 54.0, and `dps_per_boon` = 0.1 × 9 pellets × 1.5873 = 1.4286 **[Computed]**.

What this shows:

- **Toughness is one axis.** Base health and health per boon correlate at 0.74, and health at 29 boons is almost entirely health per boon (correlation 0.99) **[Computed]**. A hero that starts tanky grows tanky.
- **Gun power is two separate axes.** Starting DPS and DPS growth correlate at only 0.35 **[Computed]**. Some guns are strong early and grow slowly, others the reverse:

  | Hero | Starting DPS | DPS at 29 boons | Growth |
  |---|---|---|---|
  | Victor | 70.2 | 114.3 | +63% |
  | Billy | 74.1 | 117.5 | +58% |
  | Holliday | 41.7 | 111.9 | +168% |
  | The Doorman | 38.1 | 95.6 | +151% |
  | Lady Geist | 43.8 | 105.2 | +140% |

  Holliday's gun nearly triples over a match without a single item.
- **Hero types line up with gun power** **[Computed: mean by `hero_type`]**:
  - Mystics average 44 starting DPS and 83 at 29 boons, against 55–59 and 96–112 for the other four types.
  - Brawlers have the most health: 2,234 on average at 29 boons, against about 1,890–2,010 for the others.
  - Mystics and Brawlers also move slowest on average (6.7 and 6.8 m/s, against 6.9–7.3).
- **Gun shapes vary a lot** **[Data]**:
  - Shots per second range from 1.18 (Silver) to 14.3 (Vyper).
  - Clip size ranges from 7 to 66 (Bebop, McGinnis).
  - Bullet velocity ranges from 43 (Paige, projectile) to 1,588 (Venator).
  - Sustained DPS, which includes reload time, is a median 0.65 of burst DPS. It drops to 0.47 for Billy and 0.49 for Calico. Reload and ammo items matter most for heroes with a low ratio.
- **Falloff:**
  - **[Data]** Most guns keep 10% of their damage at `falloff_end` (`falloff_end_damage_scale` 0.1), with falloff starting around 20 m and ending around 53 m (medians).
  - **[Data]** The exceptions are Apollo (1.0), Drifter (0.6), Graves (0.5, but falloff starts at 7.6 m) and Sinclair (0.3).
  - **[Game text]** "Gun damage falls off at longer ranges".
  - **[Outside]** I believe falloff is linear between start and end. **[Assumption]** The files don't give the curve. *Test:* shoot a dummy at 20, 35 and 50 m.
- **Headshots:** `crit_bonus_pct` is negative for 11 heroes, for example Drifter −45, Nurse Harrow −40 and The Doorman −30 **[Data]**.
  - **[Outside]** I read "crit" as headshot.
  - **[Assumption]** A negative value lowers that hero's headshot bonus.
  - The baseline headshot multiplier isn't in the sheet.
- **Movement:**
  - Move speed ranges from 6.2 (Celeste) to 8.2 (Haze, Holliday, Yamato) **[Data]**.
  - Stamina is 2–4 charges.
  - Sprint bonus ranges from 1.0 to 4.0 (Bebop, Rem).
  - Dash distance is 10 m for every hero.
- **Built-in hybrid scaling.** 13 heroes have base stats that grow with spirit power (`spirit_scaling`) **[Data]**. Examples:
  - Haze: +0.5 clip size per spirit power.
  - Grey Talon and Solomon: bullet damage (+0.08 and +0.14 per spirit power).
  - Venator: bullet and spirit resist (+0.1218 each per spirit power).
  - Wraith: sprint speed.
  - Victor: health regen.

  For these heroes, spirit items also improve their gun or their body.
- **Small fixed resists** on 5 heroes, for example Baba with −7% bullet and +8% spirit, and Pocket with −15% spirit **[Data]**.

## 4. Abilities

### Cooldowns and charges

**[Computed from `abilities.csv`, base forms only]**

| Slot | Abilities with a cooldown | Median cooldown | Range |
|---|---|---|---|
| 1 | 43 | 25 s | 0.6 s (Wraith Card Trick) – 42 s |
| 2 | 44 | 33 s | 13 – 50 s |
| 3 | 35 | 28 s | 2 – 50 s |
| 4 (ultimate) | 44 | 155 s | 55 – 250 s |

- 10 abilities have more than one charge **[Data]**. Examples are Graves' Jar of Dead (4 charges, 13 s per charge), Shiv's Serrated Knives (2) and Vindicta's Assassinate (2, the only ultimate with charges).
- **[Outside]** `charge_cooldown` is the short wait between using charges. `cooldown` refills them.
- Items can add charges: Extra Charge (+1, plus 7 spirit power for charged abilities) and Rapid Recharge (+2, 30% faster between charges) **[Data]**.

### Spirit scaling

An ability's value is `base + coefficient × spirit power` **[README: the `TechPower` scaling]**.

- 147 of 176 abilities have at least one spirit-scaled property **[Data]**.
- Damage is the most common (65 abilities), then damage per second (23), then a long tail of other properties: barrier, heal, duration, fire rate, and others **[Computed: counting `spirit_scaling` entries]**.

A useful single number is **how much one ability's damage rises per 100 spirit power, as a fraction of its base**: (coefficient × 100) / base damage. Computed for the 63 abilities that have both a `damage` and a `damage_spirit_scale` value:

| Slot | Abilities | Median gain per 100 spirit power |
|---|---|---|
| 1 | 24 | +155% |
| 2 | 8 | +221% |
| 3 | 12 | +175% |
| Ultimate | 19 | **+103%** |

Ultimates have the biggest base numbers (median base damage 117.5) but scale least, relative to that base, with spirit power. Basic abilities roughly double or triple between 0 and 100 spirit power **[Computed]**.

Caveats:

- The samples are small.
- `damage` only covers properties literally named Damage. Many abilities put their damage under other names, such as Impact Damage or Explosion Damage.

### Scaling with things other than spirit power

`other_scaling` holds this for 33 abilities **[Data]**. These hooks are what connect the families:

- **Weapon damage %:**
  - Deadman Danny's Chimera Mk1 (explosion damage 1.4 per weapon damage %).
  - Rat King's Scrap Grenade and Rule, Ratannia!
  - Venator's Gutshot and Ira Domini.
  - Paradox's Kinetic Carbine, which scales with "weapon power".
- **Melee damage:** Bebop's Exploding Uppercut and Grapple Arm, Billy's Bashdown, Calico's Leaping Slash, Drifter's Rend, Silver's Boot Kick and Yamato's Flying Slash.
- **Boons:** Graves' summons, Silver's Lycan Curse (+15 bonus health per boon) and Solomon's move distances.

For these heroes, weapon investment also powers abilities.

### Upgrades (three tiers per ability)

I classified the upgrade text by keyword **[Computed]**:

| Upgrade tier | Most common contents (number of abilities) |
|---|---|
| Tier 1 | cooldown (51), damage (36), duration (30) |
| Tier 2 | duration (61), cooldown (57), damage (43) |
| Tier 3 | damage (81), duration (58), **added spirit scaling (44)** |

Notes:

- 134 abilities have cooldown cuts across their upgrades. The cuts total a median **36%** of the base cooldown. Ivy's Kudzu Connection shows a 37 s cut on a 37 s cooldown, which looks like a special mechanic; worth reading its row.
- Tier 3 often makes the ability scale better with spirit power. Abrams' Siphon Life tier 3 adds +22 DPS *and* +0.12 × spirit power to a base of 22 + 0.6 × spirit power. Tier 3 is therefore where spirit power and ability points multiply each other.
- **[Outside]** The three tiers cost 1, 2 and 5 ability points, so a fully upgraded ability costs 8. The sheet doesn't include these costs.
  - **[Computed]** This fits the data neatly: 4 abilities × 8 = 32, exactly the `total_ability_points` at the last threshold.
  - If the costs are right, then 26 points at 30,000 souls is three abilities maxed plus 2 points spare, and 6 points at 5,000 is one tier-3 upgrade plus one more point, or a spread of tier-1 and tier-2 upgrades.

## 5. The item shop

### Structure

**[Data, `items.csv`, `rules.csv`]**

- There are 156 items: 53 Weapon, 54 Vitality and 49 Spirit.
- Tier prices are fixed at 800 / 1,600 / 3,200 / 6,400. Every item is at its tier's standard price; validation checks this.

| Tier | Spirit | Vitality | Weapon | All |
|---|---|---|---|---|
| 1 (800) | 8 | 8 | 7 | 23 |
| 2 (1,600) | 12 | 15 | 16 | 43 |
| 3 (3,200) | 13 | 14 | 19 | 46 |
| 4 (6,400) | 16 | 17 | 11 | 44 |

- **Components.** 61 items are built from another item (`builds_from`). No tier-1 item is, and about half of tier 2–4 items are. Examples: Extra Health → Fortitude, Extended Magazine → Titanic Magazine / Escalating Resilience, Bullet Lifesteal + Spirit Lifesteal → Leech.
  - **[Outside]** Buying the upgrade consumes the component and you pay only the difference. Check this in the shop.
  - The data doesn't say whether the upgrade keeps the component's stats. Leech (T4) lists its own full stat block (12% weapon damage, 180 health, 12 spirit power, 30% bullet and 30% spirit lifesteal), which suggests each item's numbers stand alone.
- **Active versus passive.** 44 items are active: 18 Spirit, 18 Vitality and only 8 Weapon **[Data]**. Weapon power is overwhelmingly passive. The game caps active items ("Active Slots Full" **[Game text]**), but the cap isn't in the sheet.
- **Imbue items** attach to one of your abilities. There are 9: Mystic Expansion, Compress Cooldown, Duration Extender, Quicksilver Reload, Ballistic Enchantment, Surge of Power, Echo Shard, Mercurial Magnum and Mystic Reverb **[Data]**.
- **Slots.** **[Patch notes, 2025-11-21]** "Base slot count increased from 8 to 9 and Flex slot count reduced from 4 to 3. One is given for each Walker killed." That makes at most 12 slots. It isn't in the CSVs.
- **Selling** returns half: "sell … for … souls (half the purchase price)" **[Game text]**. The data doesn't say whether selling also lowers your investment bar.

### Always-on stats versus effects

Each item's effects are split three ways **[README]**:

- Always-on stats (the stat columns and `other_innate_stats`).
- `conditional_effects`: on 129 items.
- `enemy_effects`: on 55 items, partly inferred from property type and name.

In 23 items the effect itself scales with spirit power (13 Spirit, 5 Vitality, 5 Weapon) **[Computed]**. Examples:

- Tesla Bullets' shock: 33 + 0.19 × spirit power.
- Toxic Bullets' bleed: 1.9% DPS + 0.006 × spirit power.
- Healbane's heal on hero kill: 170 + 3 per boon.

For some actives the sheet's columns are thin. Refresher, for example, shows no numbers, only its `effect_text`: "Reset the cooldown of all your abilities and restore all your charges", with a 300 s cooldown. Read `effect_text` alongside the columns.

### Cost per point of a stat by tier

**[Computed: tier price ÷ median value of that stat among items that have it]**

This deliberately charges the whole price to one stat, so it overstates the cost of every stat that rides along on an item.

| Stat | T1 | T2 | T3 | T4 |
|---|---|---|---|---|
| Bonus health (souls per HP) | 13.3 | 23.7 | 42.7 | 51.2 |
| Weapon damage (souls per %) | 100 | 168 | 320 | 474 |
| Spirit power (souls per point) | 80 | 229 | 400 | 640 |
| Bullet resist (souls per %) | – | 188 | 320 | 640 |
| Spirit resist (souls per %) | – | 200 | 320 | 582 |

The best single-stat buys are cheap items:

- Extra Health gives 210 HP for 800 souls (3.8 souls per HP).
- Extra Spirit gives 10 spirit power for 800 (80 per point).
- Rapid Rounds gives 9% fire rate for 800.
- Battle Vest gives 18% bullet resist for 1,600.

**How much of an item's price is its always-on stats?** **[Computed]** I priced each item's always-on stats at those cheapest rates:

- 3.81 souls per HP, 80 per spirit power, 100 per weapon damage %, 89 per fire rate %, 89 per bullet resist %, 107 per spirit resist % (Spirit Resilience's rate), 27 per ammo %.
- Then I divided by the item's cost.

The median result is 0.13 at tier 3 and 0.17 at tier 4, and only 0.09 for Spirit items. In other words, at tier 3 and 4 almost everything you pay for is the effect, plus the investment that every purchase brings.

Exceptions whose always-on stats are worth more than their price at those rates: Titanic Magazine (2.5×), Extended Magazine (2.0×), Enchanter's Emblem (1.95×) and Glass Cannon (1.33×, but it also costs 13% max health).

## 6. The map: objectives, troopers, neutral camps

**[Data, `units.csv`; effective HP is Computed under A1]**

| Unit | Health | Bullet resist | Spirit resist | Effective HP vs bullets | Bounty (souls) |
|---|---|---|---|---|---|
| Guardian | 5,500 | 10% | 0% | 6,111 | 1,375 |
| Walker | 6,000 | 35% | 0% | 9,231 | 3,675 |
| Base Guardian | 4,000 | 20% | 0% | 5,000 | 1,000 |
| Patron | 12,000 + 12,000 (phase 2) | – | 0% | – | – |
| Mid Boss | 15,600 (+234 per minute) | 15% | 0% | 18,353 at spawn | – |

The resists in that table aren't the whole story. **[Patch notes, 2026-05-22]** "Guardians scaling resistance from +75%→−50% over 12 minutes to +50%→−50%". **[Patch notes, 2026-03-06]** Walkers: "+65% → −65% … over 18min". So objectives start tougher than the table says and become *weaker* than it says as the match goes on.

More objective numbers **[Data]**:

- Guardian: 116 DPS against players and 35 against troopers.
- Walker: 300 melee damage.
- Mid Boss: respawns every 420 s. It drops the Rejuvenator **[Data, `rules.csv`]**:
  - lasts 180 s
  - drop count 3
  - revive delay 3 s
  - revive health 100%

  This matches "The team that kills it will have immediate respawns on their next deaths" **[Game text]**.

**Troopers [Data]:**

| Trooper | Health | Bullet damage | Melee damage |
|---|---|---|---|
| Trooper | 300 | 36 | 50 |
| Melee Trooper | 400 | 61.8 | 80 |
| Medic Trooper | 350 | 36 | 25 |

**[Patch notes, 2026-01-30]** "Troopers now have 20% Spirit Resist." The resist columns are blank in `units.csv`, so check this in game.

**Neutral creeps.** Souls per point of effective HP **[Computed under A1]**:

| Creep | Health | Bullet / spirit resist | Souls | Souls per eHP vs bullets | Souls per eHP vs spirit |
|---|---|---|---|---|---|
| Small | 142 | 50 / 45% | 45 | 0.158 | 0.174 |
| Medium | 354 | 50 / 45% | 75 | 0.106 | 0.117 |
| Large | 1,246 | 60 / 55% | 199 | 0.064 | 0.072 |
| Sinner's Sacrifice | 500 | – | 155 | 0.310 | 0.310 |

- Every camp creep has 5 percentage points less spirit resist than bullet resist, so spirit damage clears camps about 10% more efficiently.
- Small creeps return about 2.5 times the souls per effective HP of large creeps.
- The number of creeps per camp isn't in the sheet.

---

# Part 2. How the systems interact

## 7. Where power comes from at 5,000 souls versus 30,000

Take a median hero (base 780 HP, +41.5 HP per boon, 52.3 starting gun DPS, +1.49 DPS per boon, 1.1 spirit power per boon). Boons alone give **[Computed]**:

| | At 5,000 souls (9 boons) | At 30,000 souls (29 boons) |
|---|---|---|
| Health | +374, ×1.48 | +1,204, ×2.54 |
| Gun DPS | +13, ×1.26 | +43, ×1.83 |
| Spirit power | +9.9 | +31.9 |

The investment you can hold depends on how you split your spending **[Data, `investment.csv`]**:

- At 5,000 you have about 4,800 spent. Put all of it in one tab and you reach that tab's spike (46 / 38 / 38). Split three ways (1,600 each) and you get 12 / 12 / 11.
- At 30,000 you have about 28,800 spent. All in one tab gives 115% / 66% / 100. An even split (9,600 each) gives 62% / 46% / 52.

### Worked example: Abrams

I used Abrams' own rows: base 800 HP + 49 per boon, gun 54.0 DPS + 1.43 per boon, 1.1 spirit power per boon. The abilities are Shoulder Charge (30 + 1.4 × SP), Siphon Life (22 + 0.6 × SP DPS) and Seismic Impact (100 + 2.325 × SP).

The table counts **boons and investment only**. It ignores the items' own stats on purpose, so you can see the free and semi-free layers on their own. It assumes A2, and that boon spirit power and investment spirit power simply add.

The vitality bonus is shown two ways, because "base health" is ambiguous:

- **Reading A:** the % applies to `base_health` only.
- **Reading B:** the % applies to base health plus what boons have added.

**[Computed]**

| Souls | Spend: weapon / vitality / spirit | Gun DPS | HP (A) | HP (B) | Spirit power | Shoulder Charge | Siphon Life DPS | Seismic Impact |
|---|---|---|---|---|---|---|---|---|
| 5k | 4.8k / 0 / 0 | **98** | 1,241 | 1,241 | 9.9 | 44 | 28 | 123 |
| 5k | 0 / 4.8k / 0 | 67 | **1,545** | **1,713** | 9.9 | 44 | 28 | 123 |
| 5k | 0 / 0 / 4.8k | 67 | 1,241 | 1,241 | **47.9** | **97** | **51** | **211** |
| 5k | 1.6k each | 75 | 1,337 | 1,390 | 20.9 | 59 | 35 | 149 |
| 30k | 28.8k / 0 / 0 | **205** | 2,221 | 2,221 | 31.9 | 75 | 41 | 174 |
| 30k | 0 / 28.8k / 0 | 95 | **2,749** | **3,687** | 31.9 | 75 | 41 | 174 |
| 30k | 0 / 0 / 28.8k | 95 | 2,221 | 2,221 | **131.9** | **215** | **101** | **407** |
| 30k | 9.6k each | 155 | 2,589 | 3,243 | 83.9 | 147 | 72 | 295 |
| 30k | 16k / 6.4k / 6.4k | 177 | 2,557 | 3,154 | 76.9 | 138 | 68 | 279 |

What this shows:

1. **At 5,000 souls, the spike decides things.** With about 4,800 to spend, you can only cross the 4,800 line in one tab. All-in gives 38–46 points in that family; spreading gives about 12 in each. **[Computed]** Early, concentrating on one family beats spreading by a factor of about 3–4 in that family.
2. **At 30,000 souls, the curves have flattened, so spreading is cheap.** The even split loses about half of each family's all-in value but gains in the other two. Look at the total: all-in weapon holds 115 points across the three bars, the even split holds 62 + 46 + 52 = 160 **[Computed]**. Concentrating still pays where a curve is steep at the top: spirit's last step is 75 → 100 for 6,400 souls (3.9 points per 1,000, against 2.3 for weapon and 0.9 for vitality).
3. **The vitality reading matters a lot late.** At 30,000 the gap between reading A (2,749) and reading B (3,687) is 938 HP. This is the most important formula to check in game. *Test:* note your max HP at a known boon count, buy items until your Vitality spend crosses 800, and see whether health rose by 9% of `base_health` or 9% of current max health.
4. **Free power makes up a larger share early.** At 5,000 souls, boons give Abrams +441 HP and +13 gun DPS. That's comparable to what one tab's 4,800-soul spike gives: +304 or +472 HP, or +31 DPS. At 30,000, the investment layer alone adds +110 DPS when all-in on weapon, more than the +41 from boons **[Computed]**. Items' own effects come on top of all of this and grow in importance with tier (§5).

## 8. What is free and what is chosen

| Layer | Where it comes from | What you control |
|---|---|---|
| **Boons** | Collecting souls (thresholds in `progression.csv`). Per-hero growth in `heroes.csv`. | Nothing directly. Only how fast you collect souls. |
| **Ability unlocks (4) and points (32)** | Collecting souls | Order and allocation: which ability gets upgraded, and when |
| **Investment** | Spending souls in a tab | Which tab, *by the category label of the item you buy*, not by its stats |
| **Item stats and effects** | Spending souls | Fully chosen, limited by slots (9 + up to 3), active slots, and the component tree |

**[Computed]** The investment layer turns an item's category into a stat in its own right. Some cases:

- Enchanter's Emblem (Vitality T2) gives 15 spirit power, 18% spirit resist and 5% cooldown reduction always-on, but its 1,600 souls go to the *health* bar.
- A Spirit-tab item bought for its health rider still pushes your *spirit* bar.

So you can push a bar you want by choosing items from that tab, even when the stats you need sit in another tab. Conversely, a cross-tab item delays your next spike.

## 9. The real trade-offs when spending souls

1. **Concentrate or spread.** Below about 5k spent per tab, concentrating wins because of the 4,800 spike. After that, every curve is concave, so the second tab's first 4,800 (+38 to +46) is worth more than the first tab's next 4,800 (+8 to +16 weapon) **[Computed]**. One reading: the tab you push early sets your identity, and the second spike is the natural mid-game buy. Spirit's 28,800 step is the one late reason to concentrate again.
2. **Cheap stats or effects.** Low tiers sell stats cheaply; high tiers sell effects (§5). With 12 slots at most, slots, not souls, become the constraint late **[Computed]**:
   - 9 base slots of T3 cost exactly 28,800, the top investment row.
   - 12 slots of T4 cost 76,800, far above the last boon at 48,600.

   Late game, every T1 item is a slot spent on 800 souls of stats.
3. **Health versus resist.** Under A1, effective HP = HP / (1 − R). The two multiply, so each one makes the other worth more, and a balanced mix tends to beat stacking one. Two caveats:
   - **[Patch notes, 2026-05-22]** Some percentage stats stack with diminishing returns: "Total Damage Reduction debuffs now stack diminishingly" and "Bullet Velocity now stacks additively rather than diminishingly". Cooldown reduction and lifesteal are named as diminishing in older notes.
   - Whether bullet resist from several items adds or diminishes isn't in the data. *Test:* buy two bullet-resist items and read the total on your stat sheet.
4. **Hero baseline or build against it.** Heroes with steep gun growth (Holliday, The Doorman, Lady Geist) get a stronger gun for free. Heroes with flat growth but strong starting DPS (Victor, Billy, Warden) start strong. Heroes with spirit-scaling base stats (Haze, Grey Talon, Venator) get double value from spirit power. Heroes with weapon-scaling abilities (Venator, Rat King, Deadman Danny) get double value from weapon investment **[Data]**.
5. **Ability points: breadth or depth.** Tier 1–2 upgrades are mostly cooldown and duration. Tier 3 is where damage and spirit scaling grow (§4). With 6 points at 5,000 souls, choosing *which* ability reaches tier 3 first is a real choice. By 30,000 (26 points) it largely isn't any more.
6. **Spirit power or ultimates.** Basic abilities gain a median +155% to +221% per 100 spirit power, ultimates about +103% (§4). Stacking spirit power mostly strengthens the abilities you cast most often.

---

# Part 3. What the data can't tell you, and what to do next

## Questions the data raises but can't answer

1. Does the vitality investment % apply to `base_health` only, or to health including boons? This is a 938 HP question for Abrams at 30k (§7).
2. Does weapon investment add to or multiply with item weapon damage %, boon bullet growth, and conditional bonuses such as Close Quarters' +20%?
3. How do resists combine across items, and do negative resists (shredders, Escalating Exposure) subtract before or after?
4. What is the falloff curve between `falloff_start` and `falloff_end`, and what is the baseline headshot multiplier that `crit_bonus_pct` modifies?
5. Does cooldown reduction from several items (18% + 20% + 25%) add or diminish? The patch notes say "diminishingly" but don't give the formula.
6. Does selling an item lower your investment bar? Does the component's price count toward investment when you upgrade?
7. What are the ability point costs per upgrade tier? **[Outside]** I believe 1/2/5, and that fits the 32-point total, but it's not in the sheet.
8. How much does a trooper or a base hero kill pay now, and how big are the comeback bounties? These are only in dated patch notes.
9. How many creeps are in each neutral camp, and is the 1.08%/minute soul growth linear or compounding?
10. How many active-item slots are there?
11. Are the 16 items' `stats_not_on_tooltip` real in play? Examples: Refresher's 15% bullet and 14% spirit resist, Witchmail's 7% cooldown reduction, Improved Spirit's 75 bonus health.
12. For the 18 heroes with a blank `role`, what does Valve intend them to do? The `hero_tags` and `hero_type` columns are the only hint.

## Analyses worth doing next

1. **Hero growth curves at every threshold.** Plot health and gun DPS against souls for all 44 heroes from `progression.csv` × per-boon columns, to see which heroes peak early and which late. A small script can do this.
2. **The spike calendar.** For a given purchase order, compute souls spent per tab after each purchase and mark when each 4,800 line is crossed. Compare common opening builds.
3. **Ability value at a spirit-power budget.** For each hero, sum (base + coefficient × SP) over its four abilities, divided by cooldown, at SP = 30, 80, 130. That gives a rough "ability DPS" to compare against gun DPS at the same soul count. Upgrades would need parsing.
4. **Item efficiency with the effect included.** Extend the "stat value ÷ price" calculation to the main number of each effect: proc damage per cooldown, conditional weapon damage %, and so on. That separates items that are good for their stats from items that are good for their effect.
5. **Patch tracking.** `python diff.py` across committed snapshots, plus `output/CHANGELOG.md`, shows which systems Valve tunes most often. The knowledge base shows the investment curves changing in seven patch lines between October 2025 and May 2026.
6. **Sandbox tests for assumptions A1 and A2 and questions 1–5 above.** Each one turns an assumption in this document into data.

---

## What I verified and what I didn't

- **Verified by computing from the CSVs:**
  - every number labelled [Data] or [Computed]: hero stats at 9 and 29 boons, correlations, type averages, ability cooldown and scaling statistics, upgrade keyword counts, item counts and cost per point, the always-on value ratio, investment marginal rates, the sharing totals, the Abrams table, and effective HP for units
  - the patch-note bounty arithmetic (1,250 × 1.1 = 1,375; 3,500 × 1.05 = 3,675)
  - the 32-point total matching 4 × (1 + 2 + 5)
- **Not verified:**
  - anything labelled [Outside]: AP costs, component pricing, collected-versus-spent souls, the meaning of "crit"
  - anything labelled [Assumption]: resist and weapon-damage maths, the falloff shape
  - patch-note claims about slot counts, trooper bounty, objective resist decay and diminishing stacking; they are dated and not in the CSVs
  - the upgrade classification, which is a keyword match on text and can mislabel some upgrades
  - I didn't open `deadlock.xlsx`; it holds the same tables as the CSVs
- **No tool or data files were changed.** I read `main` through a separate checkout; it has the same build 6868 data as the working branch, plus the `knowledge/` folder and corrected Rejuvenator rules.
