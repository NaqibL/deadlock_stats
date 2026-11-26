# Framework for theorising builds and matchups

A method for inventing builds from the game's mechanics rather than from what is popular. No win rates or pick rates: they reflect what is being played, not what is possible. The numbers come from the sheet in `output/`, the rules from `analysis/formulas.md`, and every claim keeps its source label (data, settled, community, inferred, assumption, judgement).

## Principles

- **Mechanics first.** A theory says why a build should work, in numbers, before anyone plays it.
- **Labels stay attached.** A conclusion that rests on an unknown formula says so.
- **The theory loop:**

  > idea → calculate it → does the answer depend on an open formula? → if so, work it out both ways → if the answers differ, run the sandbox test → record the result

  Many conclusions come out the same under every candidate formula. Those don't need a test.
- **Judgement is allowed, but marked.** Positioning, aim, the real value of a stun or of mobility, and teamwork aren't in the numbers.

## 1. How power is measured

Each build at each checkpoint gets two numbers:

- **Burst:** the damage from casting each ability once, plus single-trigger items (Mystic Shot, Capacitor's active).
- **Sustained damage per second:** gun damage including reloads, plus item triggers and timed effects (Tesla, Torment Pulse, bleeds).

A matchup compares how long each side takes to kill the other:

> **time to kill = (opponent's effective health − your burst) ÷ your sustained damage per second**

Effective health is taken against *that* opponent's damage mix (§4), using the resist rules. The length of the fight comes out of the calculation instead of being chosen.

Killing isn't only damage. Crowd control and other ways of removing an opponent from a fight are the next thing to add to this framework.

## 2. Checkpoints: tied to events, not soul counts

Checkpoints are moments when power jumps.

**The same for every hero:**

| Checkpoint | Souls collected |
|---|---|
| Kit complete: all four abilities | 3,200 |
| First ability maxed: 8 points | 6,000 |
| Second ability maxed: 16 points | 12,800 |
| Third ability maxed: 24 points | 24,600 |

The ability-maxed rows assume upgrades cost 1 / 2 / 5 points.

**Set by the build:**

- **First spike:** a tab reaches 4,800 souls spent.
- **Second spike:** a second tab reaches 4,800.
- **Key item:** the item the build is built around.
- **Slots full:** 9 items, so every buy becomes a swap.
- **Flex slots:** 10 to 12 items, which needs enemy Walkers destroyed.

**The same for everyone, by game time:** permanent buffs strengthen at minutes 10 and 30, and respawn time climbs steeply after 20 minutes.

A build is a **purchase order**. Laying it against the soul thresholds shows when each checkpoint arrives, so two builds can be compared by which reaches its spikes first. Boons and ability points follow souls *collected*; investment and items follow souls *spent*.

## 3. Describing a build

### Damage mix

The share of damage from each source:

| Source | Countered by |
|---|---|
| Gun | bullet resist |
| Weapon-damage abilities (Venator, Rat King, Deadman Danny, Haze's Fixation, Holliday's Crackshot) | bullet resist |
| Melee and melee-scaling abilities | bullet resist + melee resist |
| Spirit abilities | spirit resist |
| Item triggers and timed item effects (mostly spirit) | spirit resist, usually |
| Damage based on the target's health (Toxic Bullets, Siphon Bullets, Scourge) | grows with the target's health, so tankiness helps less against it |

A build is a mix, not a category. A mix spread across damage types is harder to counter with one resist.

### Aim

What the build mainly buys: **damage**, **toughness** or **utility** (healing, crowd control, protecting allies).

### Plan

At each stage: souls spent per tab, investment held, slots used, and how many separate damage sources the build has.

**The tab doesn't say what the build is for.** The Graves tank build in `case-studies/` spends about a third of its souls in the Weapon tab, because its damage-source items are Weapon items.

## 4. The four pieces

### 4.1 Hero card: what the hero is

Computed for every hero from the sheet:

- **Body:**
  - health at each checkpoint
  - resist traits
  - speed and stamina
- **Gun:**
  - starting damage per second, and growth per boon
  - burst against sustained
  - range and falloff
  - headshot traits
  - **shots per second**, which drives item triggers and build-up items (`formulas.md` §5)
- **Abilities**, for each one:
  - damage type
  - cooldown and charges
  - what it scales with: spirit power, weapon damage, melee, boons
  - what tier 3 adds
  - crowd control
- **Hooks:** stats that convert one tab into another. Examples: Haze's clip from spirit power, Venator's abilities from weapon damage, Essence Theft stealing weapon damage.
- **Damage sources in the kit:** summons, damage over time, damage based on the target's health. These are things an amplifier can multiply.

### 4.2 Tab value: where this hero's souls go furthest

For each tab, at each checkpoint, two questions:

1. **What does the next 1,000 souls here give this hero**, in damage and in toughness?
2. **What does skipping this tab cost?**

The second question decides how cheap an unusual build is. Spending 4,800 in the Weapon tab at 9 boons adds 18 gun damage per second for Graves and 54 for Vyper. A Graves that skips weapon items gives up a third of what Vyper would.

### 4.3 Threat profile: what an opponent does to you

The hero card read from the other side:

- damage mix, which decides the resist to buy
- healing and lifesteal, which decides whether anti-heal is worth buying
- crowd control
- mobility and range
- timing: strong early or late, from their growth

### 4.4 Counter values: what an item is worth against this opponent

Calculated, not listed:

- **Resist:** the effective health it gives against the opponent's mix. Bullet resist gives none against pure spirit damage.
- **Shred:** the damage gain against the opponent's resist. It's +10% against 0% resist and +33% against 70%.
- **Anti-heal:** weighed against how much the opponent heals.
- **Debuff resist and cleanses:** weighed against the opponent's crowd control.

## 5. Theory types: where new builds come from

1. **Stacked multipliers.** Things that multiply each other beat raw stats: health × resist, spirit power × tier-3 scaling, cooldown reduction × high-scaling abilities. A special case is **one amplifier × many sources**: a spirit amplifier such as Escalating Exposure is worth more the more separate spirit damage sources a build has.
2. **Crossover hooks.** Heroes whose stats convert between tabs, so one tab pays twice. **Trigger carriers** belong here: a fast gun with weak bullets (Vyper 14.3 shots per second, Ivy 13.6, Bebop 11.9, McGinnis 11.9 spun up, Billy 11.8, Wraith 10.6, Graves 9.8) triggers on-hit items far more often than its damage suggests.
3. **Breakpoint timing.** Reaching the 4,800 step, a tier-3 upgrade, an extra charge or a key item earlier than usual creates a power spike.
4. **Mismatches.** An opponent whose damage is mostly one type is weak to stacked resist of that type. Their counter is shred, so the matchup becomes a race between the two.
5. **Self-sufficient damage.** Heroes whose damage doesn't need items can spend on toughness while losing little. Sources: stolen stats (Essence Theft), summons, boon scaling, damage based on the target's health, and item triggers fed by a fast gun. This produces surprise tanks, like the Graves case study.
6. **Surprise burst.** A utility or healer hero whose abilities have high spirit scaling, so the right items turn them into a burst threat.

## 6. Constraints every plan has to respect

- **Item slots:** 9 base plus up to 3 flex, one per enemy Walker. When upgrades consume their components, count only the items held.
- **Active slots:** capped. "4" has only a 2024 patch line behind it.
- **Ability points:** they arrive on the progression table's schedule; tier 3 costs 5.
- **Open formulas:** where a theory depends on one, it carries the matching test from `formulas.md`.

## 7. Next to add

- **Ways to eliminate an opponent other than raw damage:** crowd control (stun, immobilise, silence, disarm, sleep), burst windows, execution thresholds, and damage over time that outlasts healing. How these enter time to kill is still to be designed.
- **Hero cards** for all 44 heroes, generated by a script so they refresh with the data.
