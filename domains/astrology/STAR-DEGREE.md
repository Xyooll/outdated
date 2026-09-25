# Xyool Astrology — Star Astrology / Degree Field

Status: **RESEARCH / USER-DERIVED FRAMEWORK / VALIDATION REQUIRED**

System candidate:
`ASTRO.STAR.DEGREE.XYOOL_V1`

## Purpose

Treat exact astrological degree position as a first-class domain object before it is compressed into sign, house, decan, or other larger interpretive buckets.

Core idea:

> **The degree is an atomic sky address. Larger astrology structures describe the context around that address.**

## Dual degree identity

Every chart longitude carries two intrinsic degree coordinates:

~~~text
LOCAL30
0°00'–29°59' within the host sign

ABS360
0°00'–359°59' around the complete zodiac
~~~

Canonical representation:
`library/knowledge/degree-coordinate-duality.md`

These must be preserved simultaneously.

A chart object therefore has:
- exact longitude;
- local degree index/ordinal;
- absolute degree index/ordinal.

The local and absolute meanings are separate hypotheses and may both participate in the same degree node.

## Coordinate layers

Keep separate:

~~~text
LAYER 1 — EXACT DEGREE ADDRESS
0°00'00"–359°59'59" ecliptic longitude under a declared coordinate frame

LAYER 2 — DEGREE BIN / CELL
optional bounded degree interval used for testing, e.g. integer degree or smaller subdivision

LAYER 3 — STELLAR NEIGHBORHOOD
actual fixed stars near the longitude, preserving ecliptic latitude, magnitude, epoch/date, catalogue identity

LAYER 4 — ZODIACAL WRAPPERS
sign
decan
bounds/terms if used
nakshatra or other explicitly declared partition

LAYER 5 — HOUSE / ANGULAR WRAPPERS
house
angle proximity
house ruler/dispositor context

LAYER 6 — OCCUPANTS / ACTIVATORS
planets
angles
nodes
asteroids / centaurs
lots / other declared points

LAYER 7 — RELATIONSHIPS
aspects
parans
declination/latitude relations
other declared geometry
~~~

Do not collapse these layers into one meaning.

## Degree object

Minimum degree-state object:

~~~text
degree_id:
longitude_exact:
coordinate_frame:
epoch_or_date:
zodiac_reference:
degree_bin_if_used:
sign:
decan_if_used:
house_if_subject_chart:
house_ruler_if_used:
stellar_neighbors:
occupants:
activators:
aspects:
source_rule_ids:
intrinsic_degree_meaning_if_any:
validation_status:
~~~

## Degree meaning versus star meaning

Two different hypotheses are allowed but must remain separable:

### A. Intrinsic degree hypothesis

~~~text
the degree address itself carries a reusable symbolic/interpretive pattern
~~~

Status:
**USER-DERIVED FRAMEWORK / UNVALIDATED**

### B. Stellar-neighborhood hypothesis

~~~text
part of the apparent degree-level information comes from the actual stars occupying or neighboring that longitude
~~~

Status:
**RESEARCH HYPOTHESIS**

These must be tested independently.

## Astronomical boundary

In tropical astrology, zodiac longitude is measured from the equinox. Fixed-star longitudes change relative to that tropical reference primarily through precession, and stars also have ecliptic latitude and small proper motion.

Therefore:

~~~text
DEGREE ≠ PERMANENT ONE-TO-ONE STAR
~~~

Instead:

~~~text
DEGREE ADDRESS
+ DATE / EPOCH
+ COORDINATE FRAME
→ STELLAR NEIGHBORHOOD
~~~

This is necessary for reproducibility.

## Star field

A stellar-neighborhood record should preserve:

~~~text
star_id / catalogue_id
common_name
ecliptic_longitude
ecliptic_latitude
declination if used
magnitude
proper_motion / epoch when material
angular_distance_from_degree
projected_longitude_distance
source_catalogue
~~~

Do not interpret a star solely because its projected longitude is nearby when its latitude/spatial relationship makes the chosen rule inapplicable.

## Full-chart aggregation correspondence

Star Astrology changes the chart aggregation order.

Preferred candidate:

~~~text
EVERY CHART OBJECT
→ exact degree address
→ local star field
→ sign/decan/house context
→ ruler/dispositor relationships
→ natal aspect network
→ timing activations
→ aggregate degree nodes into Story Reader/Writer
~~~

This prevents house/sign labels from discarding fine-grained coordinate information.

## Signal hierarchy

Degree-level information should not automatically overpower all other layers.

Until validated:

~~~text
CALCULATED DEGREE / STAR STATE
→ exact factual state

INTRINSIC DEGREE MEANING
→ user-derived/domain hypothesis

STAR INTERPRETATION
→ source-documented or domain hypothesis depending on rule

HOUSE / SIGN / ASPECT INTERPRETATION
→ existing declared rule authority
~~~

Aggregation must preserve these different authorities.

## Asteroids

Asteroids fit naturally into this model.

Each selected asteroid:
- receives an exact degree address;
- inherits sign/house/decan wrappers;
- receives its local stellar neighborhood;
- participates in aspects/relationships;
- keeps its own interpretive provenance.

The asteroid set must still be bounded/frozen before a forecast or validation case.

## Predictive use

A future predictive rule may ask whether activation of a degree node changes the story.

Example structure:

~~~text
NATAL DEGREE NODE
contains:
  natal planet/angle/asteroid
  house context
  ruler context
  stellar neighborhood
  intrinsic-degree hypothesis if enabled

FUTURE ACTIVATOR
reaches / aspects / triggers node
→ conditional Story Writer branch
~~~

The exact activation rule and orb must be frozen before outcome review.

## Validation questions

Star Astrology should be tested by ablation.

Compare:

~~~text
BASELINE A
sign + house + planet + major aspects

BASELINE B
A + exact-degree identity

BASELINE C
A + fixed-star neighborhood

MODEL D
A + exact-degree identity + fixed-star neighborhood

MODEL E
D + asteroid degree nodes
~~~

Questions:
- Does exact degree improve descriptive discrimination?
- Does exact degree improve timing specificity?
- Do fixed stars add information after ordinary chart factors are known?
- Does asteroid expansion improve results or only increase match opportunities?
- Are apparent degree effects actually star effects?
- Are apparent star effects only restatements of house/sign/aspect information?

## Failure conditions

Fail/degrade when:
- coordinate frame or epoch is missing;
- star identity/catalogue is unresolved;
- intrinsic degree meaning is presented as sourced tradition without provenance;
- too many stars/asteroids are admitted after seeing the outcome;
- degree bins/orbs are widened after a miss;
- sign/house/star/degree meanings are double-counted as independent evidence.

## Current readiness

~~~text
DEGREE AS FIRST-CLASS CALCULATION OBJECT
→ READY FOR DOMAIN MODELING

INTRINSIC DEGREE SYMBOLISM
→ PARTIAL / USER-DERIVED / NEEDS RULE FOUNDATION

STELLAR-NEIGHBORHOOD CALCULATION
→ PARTIAL / SOURCE + CALCULATION RULES REQUIRED

STAR-ASTROLOGY INTERPRETATION
→ PARTIAL

PREDICTIVE STAR ASTROLOGY
→ BLOCKED / VALIDATION REQUIRED
~~~


## Intrinsic degree research

Canonical research Flow:
`flows/intrinsic-degree-foundation.flow.md`

Initial source corpora:
- `rules/local_degree_30_modern_seed_v1.yaml`;
- `rules/absolute_degree_360_monomoiria_v1.yaml`;
- `rules/degree_intrinsic_synthesis_contract_v1.yaml`.

Current principle:

~~~text
LOCAL30 source meaning
+
ABS360 source meaning
+
XYOOL learned intrinsic candidates
+
stellar neighborhood kept separate
→ degree-node semantic state
~~~

Xyool intrinsic meanings must be learned/versioned rather than silently inherited from one degree-symbol tradition.


## Core meaning architecture

Star Astrology now uses the canonical Core meaning contract:

- `../../floware/MEANING-CONTRACT.md`;
- `../../floware/core/meaning-attribution.flow.md`.

Meaning classification:

~~~text
LOCAL30 intrinsic candidate
→ INTRINSIC

ABS360 intrinsic candidate
→ INTRINSIC

house / sign / decan / bound placement meaning
→ EXTRINSIC

stellar-neighborhood interpretation
→ EXTRINSIC

aspect / ruler / dispositor / timing relation
→ EXTRINSIC

explicit synthesis of the above
→ COMPOSITE
~~~

This classification describes where the meaning is claimed to arise. It does not establish metaphysical or predictive truth.

A Star Astrology degree node should therefore be capable of carrying:

~~~text
intrinsic_meaning_ids[]
extrinsic_meaning_ids[]
composite_meaning_ids[]
~~~

while keeping factual astronomical state separate from all three.
