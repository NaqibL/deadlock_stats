# Formulas and calculations

How the numbers in `output/` combine, for reasoning about builds and matchups. Each rule is implemented in `analysis/formulas.py`, which reads its numbers from the sheet, so the worked examples below can be reproduced:

```bash
python analysis/formulas.py
```

## How far each rule can be trusted

| Status | Meaning |
|---|---|
| **Data** | The number or rule is in the game files the sheet is built from. |
| **Settled** | `knowledge/settled.md` answers it from the files, server settings or patch notes. |
| **Community** | From [deadlock.wiki](https://deadlock.wiki/Damage_Resistance), written by players (CC BY-NC-SA). Not from the files or Valve. Read 2026-11-26; the page was last edited about 2026-11-08, before build 6868. |
| **Inferred** | No source states it; it follows from field names or arithmetic. |
| **Assumption** | Chosen so the arithmetic can go ahead. A sandbox test is given under [Open](#open-formulas-and-sandbox-tests). |

When a measured result disagrees with a rule here, the measurement wins and this file should be updated.

---

## 1. Levels and hero growth

**Level from souls** (Data, `progression.csv`): the last row whose `souls_required` you have collected. Unspent souls count. Whether the 600 starting souls count is open.

| Souls collected | Boons | Ability points |
|---|---|---|
| 5,000 | 9 | 6 |
| 10,000 | 15 | 12 |
| 20,000 | 24 | 21 |
| 30,000 | 29 | 26 |
| 48,600 | 35 | 32 |

**Hero stat at a boon count** (Data, `heroes.csv`):

> stat = base + per-boon growth × boons

This applies to health, bullet damage, light and heavy melee, gun DPS (`weapon_dps_level_1` + `dps_per_boon` × boons) and spirit power (`spirit_power_per_boon` × boons).

Example: Abrams' health at 29 boons = 800 + 49 × 29 = 2,221.

## 2. Investment

**Bonus held** (Data; units Settled): the `bonus` on the last `investment.csv` row at or below the souls spent in that tab. It is a running total, not an increment.

- Weapon: % weapon damage, on gun and melee.
- Vitality: % of base health.
- Spirit: flat spirit power.

**Health with vitality investment** (Inferred):

> health = start + boon health + (start + boon health) × vitality % + item bonus health

The game calls starting plus boon health "Base Health", so the % most likely applies to both, and not to item bonus health. The other reading (the % applies to starting health only) is a function option. Test 3 settles it.

**Gun DPS with a weapon damage bonus** (Assumption):

> gun DPS = (base + boon growth) × (1 + total weapon damage %)

where every weapon damage % source adds into one total. Tests 1a and 1b settle both halves of this.

Worked example, Abrams, boons and investment only (no item stats):

| Boons | Spent (weapon / vitality / spirit) | Gun DPS | Health | Spirit power |
|---|---|---|---|---|
| 9 | 4,800 / 0 / 0 | 98 | 1,241 | 9.9 |
| 9 | 0 / 4,800 / 0 | 67 | 1,713 | 9.9 |
| 9 | 0 / 0 / 4,800 | 67 | 1,241 | 47.9 |
| 29 | 9,600 each | 155 | 3,243 | 83.9 |

## 3. Abilities

**Ability value** (Settled):

> value = base + coefficient × spirit power

Spirit power does nothing by itself. Upgrades add to the base and to the coefficient ("+22 DPS and +0.12 × spirit power scaling" adds 22 to the base and 0.12 to the coefficient).

**Gain from 100 spirit power, relative to base** (computed): coefficient × 100 ÷ base. The medians are +155% for slot 1, +221% for slot 2, +175% for slot 3 and +103% for ultimates. Ultimates gain least relative to their base.

**Ability upgrade costs** (Inferred): 1, 2 and 5 ability points per tier. That totals 8 per ability and 32 for four, exactly the 32 the boon table grants.

## 4. Resists and resist reduction (Community)

### The rules

1. **Resists of one type stack multiplicatively:**

   > total resist = 1 − (1 − R1) × (1 − R2) × …

2. **Resist reductions ("shred") of one type stack the same way among themselves:**

   > total reduction = 1 − (1 − S1) × (1 − S2) × …

3. **Reduction is subtracted from resist:**

   > final resist = total resist − total reduction

   The final resist can go negative.

4. **Damage taken = 1 − final resist.** At −30% you take 130%.

5. **Resist from boons and spirit power adds up within itself** (for example Dynamo's 0.625% per boon). The wiki doesn't say how that total then combines with item resist.

Check against the wiki's own examples: 40% and 20% resist give 52%; 25% and 20% shred give 40%; 52% − 40% = 12%. These are tests in `tests/test_formulas.py`.

**Not a conflict with the patch notes:** the notes say *the same* reduction debuff from several sources halves each time (Crippling Headshot: 24%, 12%, 6%). That is a separate rule for repeats of one debuff. The wiki rule is for different sources.

### What each resist covers (Community)

| Resist | Reduces | Notes |
|---|---|---|
| Bullet | all weapon damage: guns, melee, and abilities that deal weapon damage | Also deals with troopers, Guardians and the Mid Boss, which deal weapon damage |
| Melee | melee only, on top of bullet resist | |
| Spirit | spirit damage | Most abilities and items; also Walkers, Shrines and the Patron |
| Pure damage | everything | Only Rat King's Rule, Ratannia! |
| Crit reduction | headshot damage taken | Innate only: Seven 55%, Mo & Krill 20%, Silver (transformed) 20%, Rem 10% |

**Abilities that deal weapon damage**, so bullet resist counters them, not spirit resist:

- Deadman Danny: Chimera Mk1, Jettison Fuel
- Haze: Fixation
- Holliday: Crackshot
- Rat King: Scrap Grenade, Royal Pestments, Rule, Ratannia!
- Venator: Consecrating Grenade, Gutshot, Ira Domini

**Melee abilities**, reduced by bullet resist and melee resist:

- Bebop: Exploding Uppercut, Grapple Arm
- Billy: Bashdown
- Calico: Leaping Slash
- Drifter: Rend
- Silver: Boot Kick
- Viscous: Puddle Punch
- Yamato: Flying Slash

Standing near your own Walker gives 15% bullet, spirit and melee resist (Community).

**Permanent or temporary:** the wiki's item lists mix always-on resist with resist that only applies for a few seconds (Warp Stone 30% for 6 s, Fury Trance 40% spirit for 6.5 s, Weapon Shielding 18% with its triggered barrier). Take item values from `items.csv`, which keeps always-on stats and conditional effects apart. All 22 item values checked against the wiki matched.

### Effective health

> effective health = health ÷ (1 − final resist)

The rules above imply this. Each resist item multiplies effective health by the same factor, however many you already have, so in effective-health terms resist does not diminish:

| 18% bullet resist items | Total resist | Damage taken | Effective health |
|---|---|---|---|
| 0 | 0% | 100% | ×1.00 |
| 1 | 18.0% | 82% | ×1.22 |
| 2 | 32.8% | 67% | ×1.49 |
| 3 | 44.9% | 55% | ×1.81 |
| 4 | 54.8% | 45% | ×2.21 |

Health and resist multiply each other: item health is worth more with resist, and resist is worth more with more health.

### Damage gained from shred

> gain = (1 − R + S) ÷ (1 − R) − 1

where R is the target's resist and S the shred. Shred is worth more against targets with more resist:

| Target's resist | −10% shred gives |
|---|---|
| 0% | +10% damage |
| 30% | +14% |
| 50% | +20% |
| 70% | +33% |

Example: Battle Vest (18%) + Bullet Resilience (35%) = **46.7%**. Bullet Resist Shredder (10%) + Crippling Headshot (16%) = **24.4%** reduction. The final resist is 22.3%, so the attacker's bullets do 46% more damage.

## 5. Souls

### Hero kills

**Bounty at a game minute** (Settled endpoints; a straight line between them is Inferred): 200 at 0:00 to 2,200 at 40 minutes, so about 50 per minute. Each player's first kill adds 125.

| Minute | 0 | 10 | 20 | 30 | 40 |
|---|---|---|---|---|---|
| Bounty | 200 | 700 | 1,200 | 1,700 | 2,200 |

**Split** (team total Settled; the killer and assister split is Inferred):

- The `HeroKillGoldShareFrac` value is the average share per participant, so team total = players × value × bounty.
- The killer gets 2.2 times an assister (`citadel_player_gold_killer_to_assist_ratio`). How exactly the server applies that ratio isn't stated; the split below assumes killer + assisters = team total.

For a 200-soul kill:

| Players in the kill | Killer | Each assister | Team total |
|---|---|---|---|
| 1 | 250 | – | 250 |
| 2 | 158 | 72 | 230 |
| 3 | 89 | 40 | 170 |
| 4 | 59 | 27 | 140 |
| 6 | 30 | 14 | 100 |

### Troopers

**Bounty** (Settled): 100 + 2 per minute. Whether that is per trooper or per wave is open. Half flies out as an orb the enemy can shoot to deny.

**Split** (Settled): each nearby player gets the `TrooperKillGoldShareFrac` value of the bounty.

| Players nearby | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Each player | 100% | 54% | 36% | 25% | 20% | 16% |
| Team total | 100% | 108% | 108% | 100% | 100% | 96% |

### Objectives

**Split** (Settled): bounties are team totals. 25% goes to nearby players (anyone who damaged it within 20 s counts), and the rest is split among all six. Splitting the 25% evenly among nearby players is Inferred.

Guardian (1,375):

| Players nearby | Each nearby | Each other teammate |
|---|---|---|
| 1 | 516 | 172 |
| 2 | 344 | 172 |
| 3 | 286 | 172 |

### Neutral camps

**Souls per point of creep health, relative to minute 0** (Data growth rates; growth in a straight line is an Assumption):

> (1 + 0.0108 × minute) ÷ (1 + 0.021 × minute)

| Minute | 0 | 10 | 20 | 30 | 40 |
|---|---|---|---|---|---|
| Souls per health | 1.00 | 0.92 | 0.86 | 0.81 | 0.78 |

Against resist, souls per point of damage dealt = souls ÷ (health ÷ (1 − resist)). Small creeps return about 2.5 times what large creeps return, and spirit damage is about 10% more efficient on every creep (5 points lower spirit resist).

### Respawn

**Respawn time** (Settled points; straight lines between them Inferred): 8 s up to 5 minutes, 38 s at 20, 70 s at 30, 85 s at 40, capped at 90 s. Add 10 s when not killed by a hero, and 6 to 22 s when much richer than the enemy average.

---

## Open formulas and sandbox tests

Each test is designed so the possible formulas predict different readings. Record the result here when measured.

**Test 1a: what weapon damage % multiplies.**
- Setup: Holliday at 10 boons (5,300 souls collected). Bullet damage = 19.7 + 1.144 × 10 = 31.14. Buy High-Velocity Rounds (+8% weapon damage). It costs 800 in the Weapon tab, so investment adds +9%, for 17% in all if the two add.
- If the % multiplies base plus boon growth, the shop shows **36.4**.
- If the % multiplies base only, the shop shows **34.5**.

**Test 1b: do weapon damage sources add or multiply?**
- Setup: same Holliday, buy Glass Cannon only (+85% weapon damage; 6,400 spent gives +54% investment).
- If they add, bullet damage reads **74.4** (× 2.39).
- If they multiply, it reads **88.7** (× 1.54 × 1.85).

**Test 2: confirm resist stacking.**
- Setup: buy Battle Vest (18%) and Bullet Resilience (35%), stay above 50% health so Bullet Resilience's extra 15% stays off, and read the stat panel.
- Multiplicative (the wiki): **46.7%**.
- Additive: **53%**.

**Test 3: what the vitality bonus multiplies.**
- Setup: Abrams at 20 boons (13,800 souls; 1,780 health). Buy Extra Regen, a Vitality item with no bonus health, so 800 spent gives +9%.
- If it multiplies starting plus boon health: max health rises by **160**.
- If it multiplies starting health only: it rises by **72**.

**Test 4: how ability cooldown reduction stacks.**
- Patch notes say it stacks with diminishing returns, so it doesn't simply add. Whether it multiplies is unknown.
- Setup: on a 30 s cooldown ability, combine Transcendent Cooldown (25%) with a Casting powerup at 20% (its late-game value).
- Multiplicative: **18 s**.
- Additive (ruled out by the notes): 16.5 s.
- Anything else is a different diminishing formula.

**Test 5: falloff curve.**
- Setup: shoot a dummy at `falloff_start`, halfway to `falloff_end`, and at `falloff_end`.
- With a straight-line falloff and an end scale of 0.1, the halfway shot does **55%** of the close-range damage.

Other open questions (upgrade price with a component, selling and investment, starting souls and boons, and more) are listed in `knowledge/settled.md`.
