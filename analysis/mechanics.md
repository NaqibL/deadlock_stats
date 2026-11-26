# Damage, control and ways to kill

An extensive view of where damage comes from in Deadlock, what reduces it, how control and sustain change a fight, and every way the sheet shows of eliminating an opponent. It builds on `analysis/formulas.md` (the rules), `analysis/catalogues/` (every damage, control and defence entry, counted) and `analysis/heroes/` (one card per hero).

Status labels are as in `formulas.md`: **Data**, **Settled**, **Community**, **Inferred**, **Assumption**. Patch notes are quoted with their date; a newer line replaces an older one. Counts come from the catalogues, which are a keyword reading of the sheet (`catalogues/README.md`). Build 6868.

---

## 1. Where damage comes from

### 1.1 Damage types and what reduces them

| Type | Comes from | Reduced by | Status |
|---|---|---|---|
| Bullet (weapon) | Guns; abilities that deal weapon damage | Bullet resist | Community |
| Melee | Light and heavy melee; melee-scaling abilities | Bullet resist and melee resist | Community; how the two combine is an Assumption (multiplied) |
| Spirit | Most abilities and items | Spirit resist | Community |
| Pure | Venator's Ira Domini final stake (bonus pure damage) | Pure damage resist only (Rat King's Rule, Ratannia!) | Community; Data for the ability text |
| Share of target health | Toxic Bullets, Siphon Bullets, Scourge, Decay, Tankbuster, and 10 heroes' abilities | Probably spirit resist; it scales with the target's health | Inferred |

Two effects get around resist:
- **Armor Piercer:** 60% of bullets ignore bullet resist and pierce through enemies (Data).
- **Tankbuster:** extra damage on abilities that deal over 165 damage, ignoring spirit resist, including 7.5% of current health (Data).

### 1.2 The sources, one by one

**1. The gun** (Data, `heroes.csv`):
- Damage per shot × shots per second, growing per boon.
- Falls off with range: most guns keep 10% at `falloff_end`.
- Headshots are 1.65× (Settled, as of 2025-11-21). 11 heroes gain less from them; Paige and Deadman Danny can't headshot.
- Gun DPS at 29 boons without items ranges from 50 (Graves) to 168 (Vyper).

**2. Damage added per bullet.** Some abilities add damage to every bullet:

| Ability | Added per bullet |
|---|---|
| Baba, Threadsap | 8 + 0.26 × spirit power |
| Mina, Love Bites | 4 + 0.09 × spirit power |
| Vindicta, Flight | 10 + 0.18 × spirit power |
| Wraith, Full Auto | 2 + 0.045 × spirit power |
| Victor, Shocking Reanimation tier 1 | 6 + 0.06 × spirit power |
| Haze, Bullet Dance | +7 bullet damage |

These grow with **shots per second**, like on-hit items, so they suit fast guns.

**3. Weapon-damage abilities:** Deadman Danny, Haze, Holliday, Paradox, Rat King, Venator. Their damage scales with weapon damage % (for example Ira Domini: +1.5 per weapon damage %), so weapon investment powers them. Bullet resist counters them.

**4. Melee:**
- Light and heavy melee grow per boon (Data).
- Weapon damage % applies to melee, at an unstated rate (Settled that it does).
- **A parried enemy takes 25% more damage of all types** (Settled, 2025-08-01).
- Eight kits have abilities that scale with light or heavy melee damage: Bebop, Billy, Calico, Drifter, Silver (and his transformed form), Viscous, Yamato.

**5. Spirit abilities:** base + coefficient × spirit power (Settled). Basic abilities gain a median +155% to +221% from 100 spirit power; ultimates about +103%. The top gainers are in `catalogues/damage-sources.md`, for example:

| Ability | Gain per 100 spirit power |
|---|---|
| Silver, Boot Kick | +800% |
| Billy, Rising Ram | +475% |
| Abrams, Shoulder Charge | +467% |
| Haze, Sleep Dagger | +338% |

**6. Item procs and timed item effects** (formulas.md §5):
- **On-hit chance:** Tesla Bullets, Capacitor. Lucky Shot: 25% of bullets deal +100% weapon damage.
- **Build-up per shot:** Toxic Bullets, Inhibitor, Spiritual Overflow, Silencer.
- **On a timer:** Torment Pulse, Mystic Shot, Spirit Strike, Mystic Burst, Spirit Burn.

These favour fast guns (Vyper 14.3 shots per second, Ivy 13.6, Bebop 11.9, McGinnis 11.9, Billy 11.8).

**7. Item actives:**

| Item | Damage | Effect |
|---|---|---|
| Arctic Blast | 175 + 0.70 × spirit power | 1 s freeze |
| Cold Front | 95 + 0.465 × spirit power | 48% slow |
| Silence Wave | 75 + 0.7 × spirit power | 3 s silence |
| Phantom Strike | 75 + 0.93 × spirit power | disarm and slow |
| Capacitor active | 100 | movement silence |
| Alchemical Fire | 45 + 0.2 × spirit power per second, rising to 95 + 0.4 × spirit power | |
| Decay | 1.95% of health per second | −55% healing |

**8. Damage based on the target's health:**
- **Heroes:** Drifter, Dynamo, Graves (Borrowed Decree tier 3: 5% of current health), Mina (Rake: 6% of missing health), Paradox, Shiv (Serrated Knives: 4% of current health), Silver (Go For The Throat), Vindicta, Vyper (Lethal Venom grows with missing health).
- **Items:** Toxic Bullets 1.9% per second, Siphon Bullets 2.5% of max health stolen, Scourge 2.3% of max health per second.
- **Decay's damage is non-lethal** and doesn't apply item procs (Data, effect text): it can't finish a kill.

**9. Summons:** Graves (Deadheads, Ghouls, Borrowed Decree gravestone), McGinnis (Mini Turret: health +10 per boon), Rem's Lil Helpers, Vindicta's Crow Familiar and others. Summon health often grows per boon (Data `other_scaling`), not with items.

**10. Reflection:** Return Fire returns 65% of bullet damage and 25% of spirit damage for 6.5 s (Data).

### 1.3 What multiplies damage

**Resist reduction (shred)** is subtracted from the target's resist (Community). There are 35 entries in the catalogue (16 from abilities and upgrades, 19 from items), from abilities (Grey Talon's Spirit Snare −15%, Dynamo's Kinetic Pulse −15%, Holliday's Crackshot) and items (Crippling Headshot −16% bullet and spirit, Disarming Hex −13%, Weakening Headshot −12%, Bullet Resist Shredder −10%).

Timing: since 2026-01-30, on-bullet-hit resist reductions "apply increased damage for subsequent hits rather than initial hit". The hit that applies the shred doesn't benefit; the next ones do. (This replaces the 2025-10-02 line that applied proc debuffs before proc damage.)

**Damage amplification on the target:**

| Source | Amplification |
|---|---|
| Nurse Harrow, Wretched Vapors | +30% damage taken |
| Venator, Hex-Lined Snap Trap tier 3 | +30% |
| Infernus, Napalm | +16%, +17% more at tier 3 |
| Victor, Aura of Suffering tier 3 | +16% |
| Drifter, Bloodscent (against low-health targets) | +15%, +12% more at tier 3 |
| Lady Geist, Malice | +7% per stack |
| Celeste, Radiant Daggers | +6% spirit damage per stack |
| Paradox, Pulse Grenade | +4% per stack |
| Billy, Blasted | +10% bullet damage |
| Escalating Exposure (item) | +4.5% spirit damage per stack, up to 12 |
| Parry | +25% all damage |

How several amplifiers combine (add or multiply) isn't stated anywhere: **Open**.

**Why one amplifier is worth more with many sources:** an amplifier applies to every hit of its type. The more separate damage sources a build has, the more one amplifier returns (the Graves case study).

---

## 2. Control

### 2.1 Kinds of control

| Kind | Effects | What it takes away |
|---|---|---|
| **Hard control** | stun, sleep, immobilize, petrify, freeze, time stop, hex, fear, tether, lift, displacement (pull, knockup, knockback), curse | Movement, or movement and actions |
| **Action denial** | silence (abilities; the files tag it `[EMP]`), disarm (gun), movement silence (movement abilities and items), curse (silence + disarm + no items) | One kind of action |
| **Soft control** | move slow, fire-rate slow, dash reduction, accuracy and vision, reveal | Speed, fire rate, information |

Some control protects the target as well (Data, ability descriptions):
- **Sleep** breaks on damage. Rem's Naptime has a "Sleep Damage Threshold" of 100 + 3.1 per boon. Sleep sets up a burst or an escape, not free damage.
- **Petrify** (Vyper's Petrifying Bola): "Petrified units block all damage, but cannot take actions". It removes the target from the fight for both sides.
- **Time stop** (Apollo's Itani Lo Sahn): struck enemies "cannot take action or heal", but "enemies take reduced damage" (Time Slow Damage Reduction 70%) until the effect expires.

**Walls add control:** Abrams' Shoulder Charge stuns when it pushes a hero into a wall; The Doorman's Luggage Cart deals bonus damage when it hits a wall.

### 2.2 Rules

- **Diminishing returns (Settled, 2025-10-02):** "Each previously applied CC reduces the duration by 7% up to a max of 21% over the past 7 seconds." It applies to the set of effects Reactive Barrier responds to (stun, sleep, immobilize, tether and similar). An ability that applies several effects counts as one.
- **Debuff resist** shortens negative effects (Inferred). How it stacks is **Open**. Exceptions:
  - Parry stuns are not shortened (Settled, 2025-07-29).
  - Knockups are shortened, since 2026-05-22.
  - The Mid Boss has 35% debuff resist.
- **Unstoppable** suppresses negative effects and gives immunity to stun, silence, sleep, root and disarm for 5.5 s. It "no longer blocks anti-heal effects" (2025-01-12).
- **Smaller rules:**
  - Being stunned pauses reloading instead of restarting it (2026-09-16).
  - Silence deselects an ability you had open (2024-09-26).
  - Being disarmed doesn't prevent reloading (2024-05-23).

**Control after resist and repeats** (Settled rule; combining the two multiplicatively is an Assumption):

> duration = base × (1 − debuff resist) × (1 − min(0.07 × recent controls, 0.21))

(`formulas.control_duration`, `chain_control`.)

Worked example, Abrams fully upgraded: Shoulder Charge's stun is 0.3 + 0.8 = 1.1 s, Seismic Impact's 1.6 + 0.8 = 2.4 s.
- Back to back: 1.1 + 2.4 × 0.93 = **3.33 s**.
- Against 25% debuff resist (one Debuff Reducer): **2.50 s**.

### 2.3 What control is worth

During hard control lasting *t* seconds, the target deals no damage, but you keep dealing yours. So control is worth:

- **your damage × t**, dealt without reply, plus
- **their damage × t**, which they don't deal to you.

Action denial is worth that for one source only. A silence on a spirit hero removes most of their damage; a disarm on a gun hero removes theirs.

In the duel model (`formulas.duel`), your control delays the opponent's time to kill you by that long.

Worked example (generic numbers):
- Side A: 2,000 effective health, 600 burst, 150 damage per second, 1.5 s of control.
- Side B: 2,400 effective health, 300 burst, 180 damage per second.
- A kills in 12.0 s; B kills in 9.4 s + 1.5 s of A's control = 10.9 s. **B wins.**
- If A adds 15% shred against B's 30% resist, B's effective health drops to 1,976 and A kills in **9.2 s. A wins.**

Shred was worth more here than the stun. Comparisons like this are what the model is for.

### 2.4 The landscape

- **33 of 44 heroes** have at least one hard-control ability. **13** have action denial (`catalogues/crowd-control.md`).
- **Most hard-control seconds** in a kit, counting each ability once, base form: Rem (4.4 s: Naptime sleep, Pillow Toss), Dynamo (3.75 s: Singularity), Mo & Krill (3.4 s: Combo stun, Burrow), Grey Talon (3 s), Haze (2.75 s: Sleep Dagger).
- **Upgrades add the most to:** Abrams (+1.6 s), Paige (+1.5 s) and Victor (+1.5 s).
- **Action denial:**
  - Grey Talon's Spirit Snare curse (silence, disarm, no items)
  - silences from Baba, Ivy's Air Drop tier 3, Lady Geist, Mina, Violet, Warden's Binding Word tier 3 and Celeste's Dazzling Trick
  - disarms from Apollo's Riposte, Mo & Krill's Sand Blast and Silver (transformed)
  - movement silence from Billy's Chain Gang and Rem's Naptime

**Items that control** (Data):

| Item | Effect |
|---|---|
| Knockdown | 0.5 s stun |
| Lightning Scroll | 0.75 s stun after 3 s |
| Crushing Fists | 0.75 s stun at max stacks |
| Arctic Blast | 1 s freeze |
| Vortex Web | 0.5 s immobilize and tether |
| Silence Wave | 3 s silence |
| Focus Lens | 4.5 s silence, then 35% of the damage dealt during it applied again |
| Silencer | builds up to a 2.5 s silence |
| Cursed Relic | 3.25 s curse |
| Disarming Hex | 4.25 s disarm |
| Phantom Strike | 3 s disarm |
| Slowing Hex, Capacitor | movement silence |

Plus slows and fire-rate slows: Juggernaut slows the fire rate of anyone who shoots you by 40%.

### 2.5 Defending against control

| Defence | What it does |
|---|---|
| Debuff Reducer, Spellbreaker, Unstoppable | 25% debuff resist, always on |
| Weighted Shots | 22% debuff resist |
| Blood Tribute | 8% always, 35% when active |
| Frenzy | 40% below half health |
| Scourge | 20% while active |
| Slow resist (Juggernaut 50%, Fleetfoot 40% active, Enduring Speed 25%) | slows only |
| Unstoppable (active) | immunity for 5.5 s |
| Indomitable | automatically cleanses the next stun, chain, immobilize, sleep, silence or fear; gives a barrier and −20% cooldowns |
| Reactive Barrier | 325 + 1.8 × spirit power barrier when controlled |
| Dispel Magic | purge, plus a 250 heal. Not usable while stunned or slept |
| Divine Barrier | removes non-stun debuffs, 600 barrier, can target an ally |
| Counterspell | a parry that blocks an ability |
| Plated Armor | 50% chance to prevent each bullet's on-hit effects |

---

## 3. Healing, barriers and sustain

- **Healing in the kit:** 18 heroes have it at base (19 entries counting Silver's transformed form; `catalogues/defence-sustain.md`). They include Abrams' Siphon Life (70% lifesteal), Dynamo, Ivy, Kelvin, Lady Geist, Mo & Krill, Rem, Silver, Victor, Warden and Yamato.
- **Barriers in the kit:** 13 abilities, including Paige's Plot Armor, Warden's Willpower, Solomon's Kingside Knight and Wraith's Project Mind.
- **Barrier items:**

  | Item | Barrier |
  |---|---|
  | Grit | 200 (active) |
  | Weapon Shielding / Spirit Shielding | 300 + 5 per boon, triggered by 250 / 225 damage in a short window |
  | Reactive Barrier | 325 + 1.8 × spirit power |
  | Majestic Leap | 200 + 12 per boon |
  | Divine Barrier | 600 |
  | Diviner's Kevlar | 1,000 every 40 s |

- **Lifesteal:**
  - Bullet and spirit lifesteal stack with diminishing returns (2024-10-10).
  - Lifesteal is weaker against creeps: 60% for bullet and 40% for spirit (2025-07-04).
  - Rat King's lifesteal is ×0.75 (Data).
- **Out-of-combat regen** works only with no damage dealt or taken for a few seconds (Inferred).
- **Healing Rite** is dispelled by damage from heroes or objectives (Data).

**Anti-heal** (Data, magnitudes):

| Source | Healing reduction |
|---|---|
| Spirit Burn | −70% |
| Decay | −55% |
| Toxic Bullets | −40% |
| Inhibitor | −40% |
| Crippling Headshot | −40% (healing from regen only) |
| Healbane | −35% |
| Drifter's Stalker's Mark tier 3 | −40% |
| Vyper's Lethal Venom tier 2 | −40% |
| Vindicta's Crow Familiar tier 1 | −35% |
| Infernus's Napalm tier 3 | −33% |
| Venator's Consecrating Grenade | −30% |

Open questions about anti-heal: how several sources stack, whether it reduces lifesteal, and how much Leech's "reduces the effect of enemy applied healing reduction" removes. None of these has a number in the sources.

**Attrition:**

> net damage per second = your damage per second − their healing per second × (1 − anti-heal)

(`formulas.net_dps`; using the strongest single anti-heal is an Assumption.)

Example: 120 damage per second against 60 healing per second leaves **60**. With −40% anti-heal it's **84**; with −70% it's **102**. Against a healer, anti-heal can be worth more than more damage.

---

## 4. Defence against burst

These effects blunt one big moment rather than raise health:

- **Barriers that trigger on damage:** Weapon Shielding and Spirit Shielding. Their thresholds (250 and 225 damage in a few seconds) mean that **burst sets them off**, absorbing the first 300 + 5 per boon.
- **Spellbreaker:** the next instance of spirit damage over 175 is reduced by 65% (9 s cooldown). It works directly against single big spirit hits.
- **Metal Skin:** immune to bullets for 5 s, but slower.
- **Ethereal Shift:** invulnerable for 4 s, then buffs.
- **Cheat Death:** immune to death for 4.5 s once lethal damage lands, but with −60% damage and healing.
- **Evasion:** 30% bullet evasion on Grey Talon's Rain of Arrows, Haze's Bullet Dance and Mirage's Dust Devil. Plated Armor deflects 30% of bullets.
- **Deferred damage:** Shiv's Bloodletting defers 25% of damage taken.
- **Return Fire** punishes the attacker.

---

## 5. Ways to kill

Each path has a formula, the heroes and items that walk it, and its counters.

| # | Path | The idea | Formula (`formulas.py`) | Who walks it | Counters |
|---|---|---|---|---|---|
| 1 | **Damage race** | Out-damage them over the fight | time to kill = (effective health − burst) ÷ damage per second | Strong guns (Vyper, Calico, McGinnis, Venator); trigger carriers with on-hit items | Resist of the right type; healing; Return Fire |
| 2 | **Burst** | Kill before they react | burst ≥ effective health | Spirit-scaling kits (Abrams, Haze, Victor, Warden, Paige, The Doorman); item actives (Arctic Blast, Silence Wave, Phantom Strike) | Triggered barriers, Spellbreaker, Metal Skin, Ethereal Shift, Cheat Death, spirit resist |
| 3 | **Control, then damage** | Remove their actions while you hit | duel(): your control delays their damage; chain_control() | Rem, Dynamo, Mo & Krill, Grey Talon, Lash, Abrams, Paige, Vyper; items Knockdown, Lightning Scroll, Cursed Relic | Debuff resist, Unstoppable, Indomitable, Reactive Barrier; Dispel Magic (not while stunned) |
| 4 | **Deny their damage** | Silence the spirit hero, disarm the gun hero | their damage × denial time | Silences (Baba, Lady Geist, Mina, Violet, Warden, Silence Wave, Focus Lens, Silencer); disarms (Apollo, Mo & Krill, Disarming Hex, Phantom Strike); curse (Grey Talon, Cursed Relic) | As for control; build damage of both types |
| 5 | **Attrition** | Outlast their healing | net_dps() | Damage over time (Shiv's bleed, Infernus, Toxic Bullets, Decay); anti-heal | Burst healing, barriers, cleanses; Leech |
| 6 | **Execute** | Finish them early | execute_effective_health(): effective health × (1 − threshold) | Shiv's Killing Blow (executes below 18%), Venator's Ira Domini (final stake executes below 8%), Apollo's Itani Lo Sahn (bonus damage below 50%), Solomon's Develop Queen (Checkmate threshold 100 + 5 per boon); missing-health damage (Mina's Rake, Silver's Go For The Throat, Vyper's Lethal Venom); Drifter's Bloodscent (amp against low health) | Staying above the threshold: barriers, burst healing |
| 7 | **Bypass defences** | Damage their resist doesn't stop | resist doesn't apply | Pure damage (Venator); Armor Piercer; Tankbuster; damage based on health | Health (not resist); pure damage resist (Rat King only) |
| 8 | **Amplify** | Make every hit count more | shred subtracts from resist; amplifiers | Shredders, Escalating Exposure, Nurse Harrow, Venator's trap, Infernus, Lady Geist, parry (+25%) | Stacking resist (shred is weaker against low resist); spreading out |
| 9 | **Remove them from the map** | Win without a kill, or make a kill count | respawn_time(); hero_kill_split() | Displacement into walls (Abrams, The Doorman); picks on isolated targets (Drifter's Bloodscent; a solo kill pays 1.25×); reveal (Mirage's Djinn's Mark, Venator's trap); vision reduction (Drifter's Eternal Night) | Grouping; vision; mobility |

Execute example: against 2,500 effective health, Shiv's 18% threshold means only **2,050** has to be removed before the execute can finish; Venator's 8% means **2,300**. This assumes the threshold applies to the health bar and resist doesn't change it.

Paths combine. Control (3) plus burst (2) is the classic pick. Amplify (8) multiplies every other path. Attrition (5) is the answer to a healer. Execute (6) shortens any path that gets the target low.

---

## 6. What this means for building

1. **Choose one or two kill paths that fit the hero's card,** and build into them. The card's theory flags point to the natural ones: a trigger carrier walks the damage race with on-hit items; a spirit-scaling kit walks burst.
2. **Check the opponent's counter to your path before you buy into it.** Burst into Spellbreaker and Weapon/Spirit Shielding loses its first 300 to 650 damage. Control into Unstoppable or Indomitable loses its first chain.
3. **Use the paths their build ignores.** A build stacking resist leaves amplify and bypass open; a build stacking health leaves resist-ignoring damage weaker but shred stronger; a healer leaves attrition-with-anti-heal open.
4. **Many damage sources plus one amplifier** beats a few big sources when the amplifier applies to all of them.
5. **Control trades with damage.** In the worked duel, 15% shred was worth more than 1.5 s of stun. Compute both before choosing.

## 7. Open questions this raises

- How several amplifiers combine (add or multiply), and with parry's +25%.
- How anti-heal sources stack, and whether anti-heal reduces lifesteal.
- How debuff resist sources stack, and how debuff resist combines with diminishing returns.
- Whether item proc damage is all spirit damage (and so amplified by spirit amps and reduced by spirit resist). The files don't label it.
- Whether an execute checks health before or after barriers.
- Whether Armor Piercer's ignored resist also ignores shred and amplification.

Each would need a sandbox test in the style of `formulas.md`.
