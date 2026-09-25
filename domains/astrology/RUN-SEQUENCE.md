# Xyool Astrology — Mandatory Run Sequence

Status: **EXPERIMENTAL DOMAIN PROCESS / CANONICAL FOR ASTROLOGY WORKFLOW**

Purpose: prevent astrology analysis from skipping input integrity, system identity, calculation, uncertainty, provenance, falsifiability, capability translation, cross-system independence, or outcome logging.

Supporting domain files:

- `domains/astrology/SYSTEM-REGISTRY.md`
- `domains/astrology/RULE-REGISTRY.md`
- `domains/astrology/SIGNAL-OUTPUT-MODEL.md`
- `domains/astrology/MAYA.md`
- `domains/astrology/VALIDATION.md`

Use this sequence for material natal readings, timing work, relationship analysis, rectification, historical tests, forecasts, Maya/Dreamspell timing work, stellar work, and cross-system synthesis. Mark each gate:

```text
PASS
NOT APPLICABLE — reason required
BLOCKED — missing evidence named
FAIL
```

Blank is prohibited for material work.

---

## 0. Request / scope lock

Record:

```text
subject(s)
question / requested reading type
natal / transit / synastry / forecast / rectification / electional / calendrical / other
historical vs current vs prospective
interpretive vs validation task
requested output: native interpretation / capability map / Tuner / synthesis
```

Do not silently change the question after seeing the chart or calendar state.

---

## 1. Birth / event / date identity

Verify or label:

```text
date
time if relevant
time precision / uncertainty
location if relevant
historical timezone / UTC offset if relevant
source of birth/event/date data
```

If time is unknown, identify which techniques remain valid and which are blocked.

A Maya or Dreamspell date calculation may not require natal houses/angles, but its civil-date conversion rules must still be locked.

---

## 2. System identity lock

Choose explicit `system_id` values from `SYSTEM-REGISTRY.md` before interpretation.

Examples:

```text
ASTRO.WT.MODERN
ASTRO.WT.TRAD
ASTRO.WS
ASTRO.JYO
ASTRO.STAR
ASTRO.HELIO
MAYA.TRAD
DREAMSPELL.ARGUELLES
```

Record only fields relevant to the chosen system, including where applicable:

```text
zodiac: tropical / sidereal
ayanamsha
house system
node mode
planet / point set
aspect set
orb policy
calculation engine / ephemeris
interpretive tradition
allowed timing techniques
Maya calendar/count identity
Maya correlation / converter identity
Dreamspell implementation / mapping algorithm / leap-day rule
fixed-star catalogue / paran method
```

If hybrid, list every component explicitly. Do not use the label `Mayan astrology` when the actual system can be identified more precisely as `MAYA.TRAD` or `DREAMSPELL.ARGUELLES`.

---

## 3. Calculation integrity

Calculate the relevant state under the locked system.

Check where material:

```text
planetary longitudes
Moon position
angles
house cusps
aspects
planetary speed / direction
stations
ingresses
exact transit times
period / time-lord boundaries
fixed-star positions / parans
Tzolk'in / Chol Q'ij identity
Haab identity
Calendar Round / Long Count identity
Dreamspell Kin / Tone / Solar Seal / derived cycle objects
```

For validation-grade work, cross-check an independent engine or reference when practical.

Do not proceed from an unresolved calculation disagreement to interpretation.

---

## 4. Uncertainty propagation

Ask only the questions relevant to the selected system:

```text
Could birth-time error change Ascendant / MC?
Could it change house placement?
Could it change Moon sign / aspect status?
Could it change a fixed-star paran?
Could timezone uncertainty alter the chart?
Could a Maya correlation/converter choice alter the calendar result?
Could Dreamspell implementation rules alter the Kin/date mapping?
Could historical calendar convention alter the input date?
```

Downgrade or block claims that exceed input or conversion precision.

---

## 5. Baseline / native system state

Identify the configurations relevant to the request under each declared system.

Separate:

```text
CALCULATED / CALENDAR CONFIGURATION
SOURCE-DOCUMENTED NATIVE INTERPRETATION
USER-DERIVED FRAMEWORK
XYOOL DOMAIN HYPOTHESIS
```

Preserve native meanings before translating them into shared capability language.

Do not infer a Western-style natal personality meaning from a Maya day sign unless a named Maya source provides that interpretation.

---

## 6. Dynamic timing inventory

If timing is relevant, inventory each active technique or cycle separately.

Examples:

```text
Western/Jyotish transits
returns
profections
progressions
solar arcs
dashas / subperiods
Panchang / muhurta factors
eclipses / lunations
stations / ingresses
fixed-star contacts / parans
Maya day / cycle boundaries
Dreamspell Kin / Wavespell boundaries
other declared techniques
```

For each material timer record:

```text
system_id
configuration / cycle identity
start / boundary
applying state if the system uses one
exact / peak if defined
separating state if the system uses one
end / next boundary
technique-specific window rule
rule_id
```

Do not force `applying → exact → separating` onto discrete systems that do not use that structure.

Do not keep expired configurations active.

---

## 7. Atomic window construction — no broad phase smoothing

For timing optimization, broad phases are prohibited when the active signal set changes inside them.

Procedure:

1. Gather every material start, exact/peak, boundary, and end time from all selected systems.
2. Sort boundaries chronologically.
3. Split the forecast horizon at every boundary.
4. Treat each unique interval as a separate window.
5. Recalculate the active rule/capability set inside each interval.
6. Treat overlaps as new windows rather than averaging them into a larger phase.

Output:

```text
window_start
window_end
active_systems
active_rule_ids
active_native_signals
```

---

## 8. Exact configuration / rule identity

A material configuration should be uniquely identifiable.

Recommended identity:

```text
SUBJECT / DATE
+ SYSTEM_ID
+ TECHNIQUE / CALENDAR OBJECT
+ MOVING FACTOR / PERIOD / DAY IDENTITY
+ TARGET FACTOR if applicable
+ RELATION / ASPECT / CYCLE RELATION if applicable
+ CONTEXT
+ TIMING STATE
+ EXACT TIME / BOUNDARY
+ ORB / WINDOW / CORRELATION RULE
+ RULE_ID + VERSION
```

Do not transfer evidence from a different planet, aspect, calendar count, day sign, Solar Seal, house, period, star, or technique without explicit correspondence.

---

## 9. Interpretation decomposition

Break the reading into claims small enough to test.

For each claim, record:

```text
system_id
rule_id + version
source / provenance
native symbolic theme
capture / life-domain mapping if defined
expected expression
alternative expression(s)
uncertainty
```

Avoid a single broad statement that can fit any outcome.

---

## 10. Capability translation

If a practical capability output is requested, translate native claims using versioned `CAPABILITY_TRANSLATION_RULE`s.

Shared capability vocabulary:

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

For each translation record:

```text
source system
source rule
capability
expected direction
strength band
confidence band
translation rule version
```

Do not translate every native symbol into every capability.

---

## 11. Convergence / contradiction / independence check

Only after independent system outputs exist, compare them.

Record:

```text
supporting systems
contradicting systems
neutral systems
shared astronomical/data dependencies
shared interpretive lineage
raw agreement count
independence-adjusted assessment
CONVERGENT / PARTIAL / ORTHOGONAL / CONTRADICTORY / NOT COMPARABLE
```

Do not treat several correlated techniques as independent votes.

Do not assume cross-system convergence is stronger than the best individual method until prospective validation shows that it is.

---

## 12. Capture / manifestation mapping

Specify where the effect is hypothesized to appear only when the declared rule supports such a mapping.

Examples may include:

```text
self / identity
body / vitality
resources
communication / learning
home / family
creativity
work / routines
partnership
shared resources
belief / travel / higher study
career / public role
friends / networks
retreat / hidden processes
```

For Maya or Dreamspell work, do not automatically map symbols into Western houses/life areas.

---

## 13. Base-rate / alternative explanation check

Before counting a claim as strong, ask:

```text
How common is the predicted event/capability state anyway?
Could the description fit most people/days?
Could ordinary context explain the result without the symbolic system?
Is the claim specific enough to discriminate?
Would a control chart/date receive the same reading?
```

Mandatory for validation work.

---

## 14. Forecast object

For prospective or frozen historical predictive testing, create the forecast before outcome review.

Minimum fields:

```text
forecast_id
claim
category / capability
predicted capture area if applicable
start
end
peak if applicable
magnitude band if predicted
hit definition
miss definition
confidence band
system_ids
rule_ids + versions
```

A prediction without a miss condition cannot become validation evidence.

---

## 15. Tuner compression — optional

If requested, compress the capability state into:

```text
Energy
Direction
Stability
Intensity
Clarity
```

This happens after system-native interpretation and capability synthesis.

Do not let Tuner compression hide contradictions.

Optional desired-output modes from the earlier framework:

```text
HIGH PERFORMANCE
RECOVERY
TRANSFORMATION
```

Optional controllable levers:

```text
Breath
Body
Fuel
Attention
```

These are action/reflection levers, not evidence that an astrology rule is true.

---

## 16. Output classification

Label statements as one of:

```text
CALCULATED FACT
CALENDAR / CYCLE FACT
INPUT-DEPENDENT CALCULATION
SOURCE-DOCUMENTED INTERPRETATION
USER-DERIVED FRAMEWORK
DOMAIN HYPOTHESIS
CAPABILITY TRANSLATION
CONVERGENCE RESULT
TUNER COMPRESSION
PROSPECTIVE PREDICTION
SUBJECTIVE REFLECTION
VALIDATION RESULT
```

Do not blend these categories into one certainty level.

---

## 17. Outcome closure

After a forecast window ends:

```text
record observed outcome
classify hit / miss / ambiguous / unavailable
close the timing window
preserve the original prediction
record whether evidence was objective or self-reported
record each contributing rule separately
```

Do not rewrite the original forecast.

---

## 18. Miss / learning loop

For misses and ambiguous outcomes:

```text
freeze original inputs + rules
identify failure layer
run controls
ask minimum generalizable missing question
revise only after positive + negative control testing
preserve rejected rules
```

Possible failure layers:

```text
input
calculation / conversion
system identity
source provenance
interpretation
capability translation
capture mapping
timing window
cross-system synthesis
Tuner compression
magnitude
base rate
confounder
validation design
```

---

## 19. Completeness audit

Before calling material astrology-domain work complete:

```text
[ ] scope locked
[ ] identity/data resolved or uncertainty labeled
[ ] system_id declared
[ ] calculation/conversion established
[ ] uncertainty propagated
[ ] native system state preserved
[ ] dynamic timers/cycles mapped if relevant
[ ] atomic windows constructed for optimization work
[ ] exact rule/configuration identity recorded
[ ] interpretation decomposed
[ ] capability translation versioned if used
[ ] convergence/contradictions checked if multiple systems used
[ ] base rates / alternatives considered when testing
[ ] forecast object frozen when predictive
[ ] Tuner compression kept downstream if used
[ ] output types labeled
[ ] outcome closure path defined
```

If a mandatory step is missing:

> **INCOMPLETE / FAIL CLOSED**

Final operating rule:

> **Preserve each system before synthesis; split time at every material boundary; and never let interpretive flexibility substitute for calculation precision or falsifiability.**

---

## 18. Delivery compression

After the analytical/forecast state is complete, choose delivery depth from `DELIVERY.md`.

Default:
`STANDARD`

Do not simplify the internal model before interpretation/forecast formation.

Correct order:

~~~text
FULL INTERNAL ANALYSIS
→ RANK MATERIAL SIGNALS
→ FREEZE FORECAST / VALIDATION RECORD
→ COMPRESS PRESENTATION
→ USER-FACING OUTPUT
~~~

Presentation compression may omit:
- low-value duplicate signals;
- secondary asteroids/stars;
- repeated degree mechanics;
- rule IDs;
- validation methodology details.

It may not omit or alter:
- primary prediction;
- date/window;
- material life area/outcome;
- meaningful contradiction;
- confidence/status;
- hit/miss condition when the forecast is being prospectively tested.

If compression materially changes what the claim means, compression failed.


## 18A. No-gap delivery invariant

The forecast horizon is continuous.

After atomic window construction:
- every atomic interval must survive into the presentation model;
- adjacent equivalent intervals may merge;
- no time may disappear solely because signal strength is low;
- lower-intensity intervals are labeled by their actual state rather than "gap";
- validation control windows remain a separate metadata layer.

This preserves the user's principle:

> **All intervals are data.**
