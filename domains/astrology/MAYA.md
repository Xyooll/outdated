# Xyool Astrology — Maya Calendrical & Dreamspell Adapter

Status: **EXPERIMENTAL DOMAIN MODULE / PROVENANCE-LOCKED**

Purpose: add Maya-related timing systems to Xyool without conflating living/historical Maya calendrics with modern Dreamspell.

Core rule:

> **`MAYA.TRAD` and `DREAMSPELL.ARGUELLES` are different systems. They may be compared, but they may not be silently merged.**

---

## 1. Why this separation exists

The traditional Maya calendrical complex includes multiple interlocking counts. The Smithsonian National Museum of the American Indian's *Living Maya Time* identifies the Tzolk'in / Chol Q'ij, Haab, Calendar Round, and Long Count among the best-understood components and documents continued living calendar traditions.

Dreamspell is a modern system developed by José and Lloydine Argüelles in the late twentieth century. It uses Maya-inspired 13 × 20 structure and its own modern vocabulary and calendar framework. Xyool therefore stores it under a separate namespace.

Neither system is made more or less useful to Xyool by this distinction. The distinction protects identity, source integrity, and validation.

---

# PART A — MAYA.TRAD

## 2. Core calendrical objects

### Tzolk'in / Chol Q'ij

Canonical calculation structure:

```text
13-number cycle × 20 named day signs = 260 unique day combinations
```

The Smithsonian describes this as the sacred 260-day Maya calendar and notes the name `Chol Q'ij` in K'iche' usage.

Xyool fields:

```text
day_number: 1..13
day_sign: named sign from the declared language / naming convention
cycle_position: 1..260
source_naming_system
calculation_source
```

Interpretive meaning must come from a named Maya source, living calendar-keeper tradition, or explicitly labeled secondary source. Do not manufacture Western-style personality meanings from the day sign.

### Haab

Canonical structure:

```text
18 periods × 20 days + 5-day Wayeb = 365 days
```

Xyool fields:

```text
haab_day
haab_month
wayeb_state if relevant
source_naming_system
```

### Calendar Round

The Calendar Round interweaves the 260-day and 365-day counts. A specific Tzolk'in + Haab combination repeats after 18,980 days, approximately 52 Haab years.

Xyool should treat Calendar Round position as a cycle identity, not as a Western transit or return unless an explicit Maya rule says so.

### Long Count

The Long Count provides an extended chronological count using units such as:

```text
k'in
uinal
tun
katun
baktun
```

It is primarily a chronology object. Any divinatory or interpretive use requires an explicit source rule rather than being inferred from scale alone.

### Other Maya cycles

Other cycles may be added only with source provenance. Examples may include Lords of the Night, Venus-related cycles, lunar series, regional ceremonial counts, or other documented calendrical structures.

Do not add a cycle merely because a modern site labels it "Mayan astrology."

---

## 3. Gregorian ↔ Maya correlation lock

Converting ancient Long Count dates to European/Gregorian chronology requires a correlation convention.

The Goodman-Martínez-Thompson family of correlations is widely used and has empirical support from radiocarbon work, but correlation history contains alternative proposals. Therefore Xyool must record the correlation or converter identity whenever it matters.

Required fields:

```text
correlation_id
converter / algorithm
calendar convention
input civil date
resulting Tzolk'in
resulting Haab
resulting Long Count if calculated
```

For current-domain reference work, the Smithsonian *Living Maya Time* converter is an appropriate independent cross-check source.

A day-sign result without a declared conversion method is incomplete for validation-grade work.

---

## 4. Regional / language integrity

Maya is not one monolithic historical or living tradition.

Where meanings or names differ by community, language, region, or lineage, preserve that identity rather than flattening them into a universal dictionary.

Recommended fields:

```text
language / community
region
source person / text
traditional / historical / modern status
translation notes
```

If Xyool cannot identify the provenance of a meaning, label it `SOURCE UNCERTAIN`.

---

## 5. Maya timing state

Maya calendrical states are discrete cyclic states. Xyool may represent them as:

```text
CURRENT DAY COMBINATION
NEXT DAY BOUNDARY
CURRENT HAAB POSITION
CURRENT CALENDAR-ROUND POSITION
CURRENT LONG-COUNT POSITION
REPEATING CYCLE RELATION, if explicitly defined
```

Do not force the Western aspect state machine (`applying → exact → separating`) onto a discrete Maya day count unless a specific Maya technique defines an analogous transition.

---

## 6. Maya interpretive rule object

```text
rule_id
system_id: MAYA.TRAD
community / language / source tradition
source_reference
calendar_object
input_pattern
native_meaning
native_action / ceremonial meaning if the source includes one
capability_translation if Xyool creates one
translation_status
validation_status
version
```

The `native_meaning` must be preserved separately from Xyool's capability translation.

---

# PART B — DREAMSPELL.ARGUELLES

## 7. Identity

Dreamspell is stored as a modern, Maya-inspired symbolic timing system associated with José and Lloydine Argüelles.

Typical objects may include:

```text
260 Kin
13 Galactic Tones
20 Solar Seals
Galactic Signature
Wavespell
Castles, when used
13 Moon / 28-day calendar
Day Out of Time
```

These objects must not be labeled as historical Maya objects unless a source independently establishes that identity.

---

## 8. Dreamspell calculation lock

Required fields:

```text
system_id: DREAMSPELL.ARGUELLES
Dreamspell version / implementation
Gregorian mapping algorithm
leap-day handling
Kin
Tone
Solar Seal
Wavespell / other derived objects if used
source implementation
```

Because modern implementations can differ, calculation rules must be versioned.

---

## 9. Dreamspell interpretation

Interpretive claims should be sourced to Dreamspell literature or clearly labeled modern practitioner synthesis.

Do not use traditional Maya day-keeper meanings as if they automatically describe a Dreamspell Solar Seal, and do not translate Dreamspell Solar Seal meanings backward into the traditional Tzolk'in.

---

# PART C — COMPARATIVE / XYOOL USE

## 10. What can be compared

Xyool may compare:

```text
cycle positions
timing recurrence
symbolic themes
capability translations
self-report or event associations
prospective timing performance
```

But comparison must preserve source identities.

Correct:

```text
MAYA.TRAD signal A
DREAMSPELL.ARGUELLES signal B
→ agreement / disagreement recorded
```

Incorrect:

```text
"the Mayan signal" = A + B blended together
```

---

## 11. Capability translation

A Maya or Dreamspell rule may optionally translate into Xyool's common capability vocabulary:

```text
Mental Capacity
Focus
Action
Opportunity
Communication
Creation
Investigation
Connection
Recovery
Friction / Impulsiveness
```

Translation is a **new Xyool hypothesis** unless the source tradition itself expresses an equivalent concept.

Store both:

```text
native meaning
XYOOL capability translation
```

This lets Xyool test the translation without rewriting the source tradition.

---

## 12. Validation plan

### Calculation validation

Cross-check a sample of Gregorian dates against an independent reference implementation.

### Identity validation

Verify that traditional Maya and Dreamspell calculations are not accidentally sharing the same mapping or names when their algorithms differ.

### Meaning reproducibility

Freeze the source dictionary / rule version before reading outcomes.

### Blinded discrimination

Test whether source-derived day descriptions distinguish target dates/subjects from decoy dates better than flexible matching would predict.

### Prospective timing

Predeclare day/cycle hypotheses before the target day or window and close them afterward.

### Cross-system comparison

Test `MAYA.TRAD` and `DREAMSPELL.ARGUELLES` independently before testing whether their convergence adds signal.

---

## 13. Sources / provenance anchors

Preferred traditional/living Maya reference layer:

```text
Smithsonian National Museum of the American Indian — Living Maya Time
Maya calendar / calendar-system materials
Maya Calendar Converter
living Maya Day Keeper material when clearly attributed
scholarly calendrical research for historical questions
```

Dreamspell reference layer:

```text
José & Lloydine Argüelles primary Dreamspell materials
clearly identified Dreamspell organizations / implementations
comparative scholarship when distinguishing Dreamspell from historical Maya calendrics
```

Final rule:

> **Preserve the living/historical Maya system on its own terms; preserve Dreamspell on its own terms; let Xyool test each before testing convergence.**