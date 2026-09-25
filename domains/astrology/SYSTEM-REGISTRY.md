# Xyool Astrology — System Registry

Status: **EXPERIMENTAL DOMAIN CANONICAL / SYSTEM IDENTITY AUTHORITY**

Purpose: define the astrology and adjacent symbolic systems that Xyool may use, keep their calculations and interpretive rules separate, and prevent silent cross-system mixing.

Core rule:

> **A system may contribute to synthesis only after it has produced its own independently labeled output.**

No system is allowed to borrow another system's objects, meanings, timing rules, or calibration without an explicit correspondence rule.

---

## 1. Registered system families

### ASTRO.WT.MODERN — Western Tropical / Modern

Typical objects:

```text
planets / luminaries
signs
houses
angles
aspects
transits
progressions
returns
synastry / composite
```

Required identity fields:

```text
tropical zodiac
house system
aspect set
orb policy
node mode if used
planet / point set
calculation engine
interpretive source / ruleset
```

---

### ASTRO.WT.TRAD — Western Tropical / Traditional-Hellenistic

Typical additional objects:

```text
sect
essential / accidental condition
traditional rulership
lots
annual profections
time-lord techniques
traditional aspect doctrine
```

Traditional and modern Western rules must not be silently merged.

---


### ASTRO.WT.XYOOL_STORY_V1 — Western Tropical / Xyool Story Grammar v1

Status:

~~~text
EXPERIMENTAL HYBRID / SOURCE-LABELED / VALIDATION REQUIRED
~~~

Purpose: provide a deliberately small, auditable Western Tropical rule grammar for Core Story Reader/Writer experiments.

Declared components:

~~~text
tropical zodiac
whole-sign houses
classical sign rulers for annual profections
major aspects: conjunction / sextile / square / trine / opposition
transit state: applying → exact → separating
annual profection: one sign per year from Ascendant
broad house/life-area semantics from Astrodienst
broad planetary-function semantics from Astrodienst
Xyool story-branch rules layered separately as DOMAIN HYPOTHESES
~~~

Deliberate exclusions in v1:

~~~text
progressions
solar arcs
solar returns
zodiacal releasing
detailed dignity scoring
minor aspects
fixed stars
asteroids
midpoints
modern outer-planet rulership substitution inside profections
multi-system convergence
precise numeric prediction probabilities
~~~

Canonical rule cohort:
`rules/western_tropical_xyool_story_v1.yaml`

This is not identical to ASTRO.WT.MODERN or ASTRO.WT.TRAD. It is an explicitly named experimental hybrid so components from those families are never silently merged.

### ASTRO.WS — Western Sidereal

Required additional field:

```text
ayanamsha / sidereal reference
```

Do not assume Jyotish rules merely because the zodiac is sidereal.

---

### ASTRO.JYO — Jyotish / Vedic

Potential submodules:

```text
rashi / natal chart
nakshatra
planetary condition
bhava / house interpretation
transits
dashas / antardashas / deeper subperiods
Panchang
muhurta
relationship methods
other named Jyotish techniques
```

Required identity fields include:

```text
ayanamsha
house / bhava convention
node convention
nakshatra scheme
dasha system when used
Panchang source / location when used
interpretive lineage / ruleset when material
```

A prior Xyool-oriented workflow used Jyotish transits, Panchang, nakshatras and dasha hierarchy to generate capability/timing outputs. Those are preserved as candidate domain methods, not assumed validated laws.

---

### ASTRO.STAR — Fixed-Star / Stellar

Purpose: preserve the user's earlier full-resolution-sky concept beyond the 12-sign abstraction.

Potential objects:

```text
individual fixed stars
planet-star conjunctions
angle-star contacts
parans
stellar culmination / rising / setting relationships
constellation context where explicitly used
```

A prior conceptual model treated:

```text
fixed stars = candidate signal sources
planets = receivers / processors / modifiers
angles = activation gates
```

This is retained as an **EXPERIMENTAL MODEL**, not a canonical causal claim.

Parans require exact location and sufficiently precise time because the relation is based on simultaneous angularity. If time precision is inadequate, paran claims fail closed.

---


### ASTRO.STAR.DEGREE.XYOOL_V1 — Star Astrology / Degree Field

Status:

~~~text
RESEARCH / USER-DERIVED FRAMEWORK / VALIDATION REQUIRED
~~~

Purpose: treat exact ecliptic degree position as a first-class astrological object and relate each degree address to its actual stellar neighborhood before larger sign/house/decan compression.

Canonical framework:
`STAR-DEGREE.md`

Primary objects:

~~~text
exact degree address
degree bin/cell if used
stellar neighborhood
fixed-star identity
planet/angle/node/asteroid occupants
zodiacal wrappers
house/angular wrappers
aspect/relationship network
~~~

Required identity fields:

~~~text
coordinate frame
epoch/date
tropical/sidereal reference
star catalogue
star-position calculation source
degree-bin policy if used
stellar-neighborhood/orb policy
object/asteroid set
intrinsic-degree rule set if used
star-interpretation rule set if used
~~~

Core boundary:

~~~text
intrinsic degree meaning
≠
fixed-star meaning
≠
sign/decan meaning
≠
house meaning
~~~

These layers may later converge only through explicit rules and dependency tracking.

### ASTRO.HELIO — Heliocentric / 3D Experimental

Purpose: research whether heliocentric geometry, declination, latitude, or a more complete 3D sky representation adds discriminating information beyond standard geocentric longitude-based methods.

Status:

```text
RESEARCH ONLY / UNVALIDATED
```

Do not treat novelty or apparent physical realism as evidence of predictive value.

---

### MAYA.TRAD — Traditional / Living Maya Calendrical Layer

This namespace is reserved for historically documented or living Maya calendrical traditions such as:

```text
Tzolk'in / Chol Q'ij
Haab
Calendar Round
Long Count
other explicitly sourced Maya cycles
```

This is **not** Western natal astrology and must not be forced into planets, houses, signs, or aspects.

Required identity fields may include:

```text
calendar / count used
language / regional naming convention where relevant
Gregorian-to-Maya correlation method
converter / calculation source
interpretive source or living-tradition source
```

Detailed rules: `domains/astrology/MAYA.md`.

---

### DREAMSPELL.ARGUELLES — Dreamspell / Argüelles Modern System

This is a separate namespace.

It may include:

```text
260 kin
13 Galactic Tones
20 Solar Seals
Wavespells
13 Moon / 28-day framework
other explicitly named Dreamspell constructs
```

It must never be presented as interchangeable with the traditional Tzolk'in / Chol Q'ij count.

Detailed rules: `domains/astrology/MAYA.md`.

---

## 2. Adjacent systems allowed in synthesis

These are **not automatically astrology systems**. They may feed a higher-level Xyool synthesis only when named separately.

### ADJ.WUXING — Wu Xing

Prior user framework:

```text
Wood → Fire → Earth → Metal → Water → Wood
```

The earlier Tuner used ordered actions so one phase supports the next. Preserve this only inside a declared Wu Xing or action-sequencing layer. Do not project Wu Xing correspondences onto planets or signs without an explicit correspondence map.

### ADJ.HD — Human Design

May contribute a separate symbolic/profile output when explicitly requested and sourced. It does not inherit authority from astrology calculations simply because it uses astronomical birth data.

### ADJ.AYURVEDA — Ayurveda / Prakriti-Vikriti

May contribute baseline/imbalance information to the broader Tuner framework. It is not an astrology rule and should remain independent from astrological validation.

---

## 3. System output object

Every participating system should return a standardized object before synthesis:

```text
system_id
system_version
input_version
calculation_settings
source_rules
raw_configuration
native_interpretation
capability_effects_if_defined
timing_boundaries_if_defined
confidence_status
validation_status
known_dependencies
known_conflicts
```

The native interpretation must be preserved even if later translated into shared capability language.

---

## 4. Provenance classes

Each rule or meaning should carry one of:

```text
PRIMARY / FOUNDATIONAL SOURCE
LIVING-TRADITION SOURCE
ESTABLISHED TRADITIONAL SECONDARY SOURCE
MODERN SYSTEM SOURCE
XYOOL HYPOTHESIS
USER-DERIVED FRAMEWORK
FREE-FORM SYNTHESIS
```

Provenance is not the same thing as predictive validity. It tells Xyool what the rule is and where it came from; validation tells Xyool how well it performs.

---

## 5. Cross-system independence rule

Two agreeing outputs are not automatically two independent confirmations.

Track shared dependencies such as:

```text
same birth time
same planetary ephemeris
same aspect geometry
same transit
same underlying calendar conversion
one system derived from another
one interpretation copied from another
```

Cross-system convergence should eventually be weighted by **independent information contribution**, not raw vote count.

---

## 6. Translation rule

Correct order:

```text
SYSTEM-NATIVE CALCULATION
→ SYSTEM-NATIVE INTERPRETATION
→ OPTIONAL CAPABILITY TRANSLATION
→ CROSS-SYSTEM SYNTHESIS
→ TUNER COMPRESSION
```

Incorrect order:

```text
mix all symbols first
→ create one story
→ label it convergence
```

---

## 7. Registration rule

A new astrology or symbolic system may be added only when Xyool can state:

```text
what objects it uses
how those objects are calculated / identified
what rules interpret them
what timing boundaries exist
what data precision it requires
what its provenance is
how it can fail
what validation would distinguish it from flexible storytelling
```

If those are not known, register the system as `RESEARCH ONLY` rather than operational.

---

### ASTRO.WT.XYOOL_STORY_V2_DEGREE_NODE — Western Story v2 / Degree-Node Full Chart

Status:

~~~text
CANDIDATE / PARTIAL / VALIDATION REQUIRED
~~~

Parent:
`ASTRO.WT.XYOOL_STORY_V1`

Degree layer:
`ASTRO.STAR.DEGREE.XYOOL_V1`

Canonical system file:
`systems/ASTRO.WT.XYOOL_STORY_V2_DEGREE_NODE.yaml`

Migration:
`migrations/WT-STORY-V1-TO-DEGREE-NODE-V2.md`

Purpose:
preserve exact degree state and model the full chart as a dependency-aware graph of houses, rulers/dispositors, aspects, stellar neighborhoods, bounded minor bodies, and timing activations.

Core layers:

~~~text
L0 raw astronomical state
L1 categorical wrappers
L2 rulership/governance
L3 geometric relationships
L4 stellar neighborhood
L5 bounded minor bodies
L6 timing activation
L7 historical/outcome evidence
~~~

House policy:
houses remain primary life-area/capture wrappers.

Degree policy:
exact longitude remains the atomic sky address and is never discarded by sign/house/decan compression.

V1 remains immutable; v2 is a domain delta, not a rewrite of prior history.
