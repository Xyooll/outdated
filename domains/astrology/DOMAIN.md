# Xyool Domain Manifest — Astrology

Floware entrypoint:
`domains/astrology/flows/astrology-analysis.flow.md`

New domain reasoning should route through this Flow. Existing deterministic calculation components remain supporting software where exactness requires them.

Status: **EXPERIMENTAL DOMAIN / VALIDATION REQUIRED**

## 1. Domain identity

```text
Domain Name: astrology
Domain Status: EXPERIMENTAL
Primary Objective: produce precise, system-labeled, uncertainty-aware astrological interpretations and timing hypotheses that are reproducible from stated inputs and progressively calibrated against frozen historical and prospective outcomes
Decision Maker / User: astrologer, analyst, or Xyool operator
Unit of Decision: interpretive proposition, timing hypothesis, comparison, or forecast claim
```

Astrology is implemented as a domain adapter over Xyool's core reasoning architecture.

This domain deliberately separates two layers:

```text
ASTRONOMICAL / CALCULATION LAYER
birth/time/location + ephemeris + coordinate conventions
→ positions / angles / houses / aspects / cycles

ASTROLOGICAL / INTERPRETATION LAYER
calculated configuration + declared tradition/rules
→ symbolic interpretation / timing hypothesis / manifestation claim
```

The first layer is computational and should be reproducible. The second is interpretive and must carry its own evidence, uncertainty, validation status, and falsification conditions.

The existence of a calculated configuration does not by itself establish that an astrological interpretation is causally true.

---

## 2. Objects / entities

Core domain objects may include:

```text
SUBJECT / NATIVE
EVENT
BIRTH EVENT
NATAL CHART
EVENT CHART
TRANSIT CHART
SYNASTRY PAIR
COMPOSITE / RELATIONSHIP CHART
PLANET / LUMINARY
NODE
ANGLE
ECLIPTIC DEGREE ADDRESS
DEGREE BIN / CELL
FIXED STAR
STELLAR NEIGHBORHOOD
HOUSE
SIGN
NAKSHATRA / LUNAR MANSION
ASPECT
DIGNITY / CONDITION
LOT / ARABIC PART
TIME LORD / PERIOD
TRANSIT
PROGRESSION
SOLAR ARC
PROFECTION
RETURN
DASHA / SUBPERIOD
INGRESS
STATION
LUNATION / ECLIPSE
TIMING WINDOW
INTERPRETIVE CLAIM
OBSERVED OUTCOME
```

Not every astrology system uses every object. A chart must declare its system before interpretation.

---

## 3. System identity lock

Before material interpretation, record the calculation and tradition identity.

Minimum identity object:

```text
SUBJECT / EVENT
+ CHART TYPE
+ DATE
+ TIME
+ TIME PRECISION / UNCERTAINTY
+ LOCATION
+ HISTORICAL TIMEZONE / UTC OFFSET
+ ZODIAC TYPE
+ AYANAMSHA IF SIDEREAL
+ HOUSE SYSTEM
+ NODE MODE IF RELEVANT
+ POINT / PLANET SET
+ ASPECT SET
+ ORB POLICY
+ EPHEMERIS / CALCULATION ENGINE
+ INTERPRETIVE TRADITION / RULESET
```

Examples of tradition/ruleset labels:

```text
Western Tropical — modern
Western Tropical — traditional / Hellenistic
Western Sidereal
Jyotish / Vedic
Electional
Horary
Mundane
Synastry / relationship
Experimental hybrid — must name every imported component
```

Silent mixing of systems is prohibited.

---

## 4. Observable evidence

Directly observable or reproducibly calculable evidence includes:

```text
birth/event date
birth/event time
birth/event place
historical timezone / UTC offset
calendar convention where relevant
astronomical ephemeris positions
angular separations
planetary speed and direction
stations / ingresses
house cusps and angles given a declared house system
aspect geometry given a declared aspect/orb policy
cycle boundaries
recorded real-world event dates and descriptions
subject-reported experiences, labeled as self-report
```

A computed planetary position and an interpretation of that position are different evidence types.

---

## 5. Latent / hidden state

Important unknown or partially observable state includes:

```text
birth-time error
whether a symbolic configuration is personally salient
whether a configuration corresponds to a specific external event
which life domain, person, or mechanism expresses a configuration
strength / magnitude of manifestation
interaction among simultaneous configurations
base-rate probability of the predicted event
reporting / memory bias
selection bias
unknown life context
causal mechanism, if any
```

These may not be silently converted into certainty.

---

## 6. State model

Astrological analysis should distinguish at least four state layers.

### A. Input state

```text
VERIFIED
REPORTED
APPROXIMATE
UNKNOWN
CONFLICTED
```

### B. Calculation state

```text
CALCULABLE
PARTIALLY CALCULABLE
TIME-SENSITIVE / UNCERTAIN
BLOCKED
```

### C. Dynamic configuration state

For time-varying factors:

```text
INACTIVE
APPROACHING
APPLYING
EXACT / PEAK
SEPARATING
POST-WINDOW
EXPIRED / CLOSED
```

### D. Interpretation / evidence state

```text
TRADITIONAL INTERPRETATION
DOMAIN HYPOTHESIS
PROSPECTIVE PREDICTION
OBSERVED MATCH
OBSERVED MISS
AMBIGUOUS
UNTESTABLE
REJECTED
```

Do not confuse configuration state with outcome state.

---

## 7. Important transitions

Examples include:

```text
planet outside orb → enters orb → applies → exact → separates → exits orb
planet in sign → ingress → new sign state
planet direct → station → retrograde
retrograde → station → direct
pre-return → exact return → post-return
profection year N → birthday boundary → profection year N+1
dasha / period A → period boundary → period B
progressed body approaching natal contact → exact → separating
unactivated natal configuration → timing-layer activation hypothesis → observed manifestation / miss
uncertain birth time → rectification evidence → narrower time range
prediction open → outcome observed / no outcome → prediction closed
```

Transitions must be framework-specific. A Jyotish dasha transition is not interchangeable with a Western annual profection.

---

## 8. Gates and timers

Potential astrology-domain gates/timers include:

```text
orb entry
exact aspect
orb exit
sign ingress
house ingress
station
return
lunation / eclipse
profection boundary
zodiacal releasing boundary where used
dasha / antardasha boundary where used
progressed exact contact
solar-arc exact contact
synodic-cycle phase change
predeclared forecast-window open / close
```

A timer is useful only when the underlying system defines a reproducible transition or window.

Timing calibration is local to the technique. Do not import timing windows from the Stock / Market domain.

---

## 9. Actions

Permitted domain actions include:

```text
calculate
verify inputs
label uncertainty
select / lock astrology system
interpret
compare
rank themes by declared method
identify active timing windows
form a falsifiable hypothesis
record a prospective forecast
observe outcome
close a forecast window
update confidence
run controls
rectify birth time under an explicit method
reject or revise a rule
```

The astrology domain does not override user agency. Interpretations should not be presented as deterministic commands.

High-stakes medical, legal, financial, or safety decisions require evidence appropriate to those domains; astrology does not substitute for it.

---

## 10. Success / payoff definition

Primary domain success is not "sounding accurate."

Success has multiple layers:

```text
CALCULATION SUCCESS
positions / angles / timing states are reproducible from declared inputs

INTERPRETATION SUCCESS
interpretation follows the declared tradition/rules without hidden rule changes

TIMING SUCCESS
predeclared timing hypotheses resolve within the declared window more often / more specifically than relevant controls or base rates

USEFULNESS SUCCESS
the reading helps the user organize reflection or questions without falsely increasing certainty

LEARNING SUCCESS
hits, misses, ambiguity, and failed mappings improve future domain rules rather than being retrofitted away
```

---

## 11. Failure / loss definition

Failures include:

```text
wrong astronomical calculation
wrong timezone / location handling
unrecorded system mixing
using houses/angles despite birth-time uncertainty too large for the claim
post-hoc interpretation presented as prediction
vague prediction with no falsification condition
moving the forecast window after the outcome
selecting only confirming events
ignoring base rates
using outcome knowledge during historical reconstruction
claiming causality from symbolic correspondence alone
double-counting the same configuration across multiple labels
failing to close expired timing windows
silently changing orb / technique / house system to rescue a miss
```

---

## 12. Capture definition

In this domain, `capture` means:

> **the subject, relationship, institution, or life area to which an interpretation assigns the hypothesized manifestation or consequence.**

Examples:

```text
self / body
partner / relationship
career / public role
home / family
finances / resources
education / travel
creative work
community / groups
```

Capture must be derived from the declared astrology framework, not from market/shareholder semantics.

---

## 13. Recognition / response definition

`Recognition` in astrology means the observable response used to evaluate a claim.

Keep distinct:

```text
OBJECTIVE EVENT
externally datable event or state change

SUBJECTIVE REPORT
felt experience, interpretation, salience, or self-description

BEHAVIORAL RESPONSE
observable action taken by the subject

NO OBSERVED RESPONSE
no qualifying event/report inside the declared window
```

Subjective salience can be useful but must not be treated as equivalent to an externally verified event.

---

## 14. Source hierarchy

Use the strongest source appropriate to the claim.

### Calculation / astronomical state

1. established ephemeris / astronomical calculation engine;
2. authoritative historical timezone database;
3. documented calendar / coordinate conventions;
4. independent calculation engine for cross-checks.

### Birth / event inputs

1. contemporaneous birth record or primary record where available;
2. direct subject report;
3. family/secondary report;
4. approximate/unknown data explicitly labeled.

### Interpretive rules

1. explicitly named source tradition / primary or foundational text;
2. established practitioner literature within the named tradition;
3. modern secondary synthesis;
4. Xyool domain hypothesis;
5. free-form intuition — lowest authority unless separately tested.

### Outcome validation

1. contemporaneous primary event record;
2. timestamped external record;
3. frozen prospective user report;
4. retrospective report;
5. later narrative reconstruction.

---

## 15. Freshness standard

For current forecasts:

```text
calculation timestamp must be explicit
current/future transit positions must be recomputed for the requested period
historical timezone assumptions must be checked
open timing windows must have an end condition
realized windows must be closed
superseded birth data or rectified times must not coexist silently
```

For historical work, "freshness" means using the information and rules available at the frozen decision point.

---

## 16. Invalidation conditions

A material astrology claim is blocked or invalidated when, as relevant:

```text
birth date is unknown
required birth time is unknown or too imprecise for the technique
location / timezone cannot be resolved
astrology system is unspecified
calculation engine disagrees materially and discrepancy is unresolved
claimed aspect / transit does not exist under the declared settings
forecast window was not declared before outcome review
claim is too vague to identify a miss
interpretive rule was changed after the result
required outcome evidence is unavailable
```

Unknown birth time does not block all astrology; it blocks techniques that materially depend on time-sensitive angles/houses or precise Moon placement when uncertainty crosses a relevant boundary.

---

## 17. Validation architecture

Astrology-domain validation has separate tracks.

### Track A — Calculation validation

Cross-check chart outputs against an independent reputable engine.

Test:
- longitude / sign;
- angles;
- houses;
- aspects;
- stations;
- timing of exact contacts;
- timezone handling.

### Track B — Rule reproducibility

Given the same chart, configuration, and declared rules, the interpretation should not change merely because the analyst knows the outcome.

### Track C — Historical frozen-case validation

Freeze:
- birth/event inputs;
- astrology system;
- interpretive rules;
- allowed techniques;
- forecast windows;

Then analyze only information available before the target outcome.

### Track D — Prospective validation

Record predictions before the outcome, including:

```text
claim
category
window
magnitude if predicted
what counts as a hit
what counts as a miss
confidence
techniques used
```

Close every prediction after the window.

### Track E — Controls

Use controls such as:

```text
shuffled event dates
randomized / offset birth times where appropriate
matched non-event windows
placebo transit windows
base-rate comparison
blinded chart-to-description matching
alternative-system comparison
```

Controls must be designed so that a flexible interpretation cannot trivially fit every case.

---

## 18. Anti-lookahead discipline

Historical astrology testing must not use future outcome knowledge to choose:

```text
which transit mattered
which house meaning mattered
which orb was allowed
which timing technique was used
which event category counted
which natal placement became "important"
```

Correct sequence:

```text
FREEZE INPUTS
→ FREEZE SYSTEM
→ FREEZE RULES
→ GENERATE CLAIM
→ FREEZE WINDOW / FALSIFICATION
→ REVEAL / OBSERVE OUTCOME
→ SCORE RESULT
→ RUN MISS LOOP
```

---

## 19. Miss handling

Use the Xyool miss loop:

```text
MISS / AMBIGUOUS RESULT
→ freeze pre-outcome record
→ determine whether calculation, input, interpretation, timing, or validation failed
→ identify the minimum missing question
→ test positive + negative controls
→ revise only if the change generalizes
→ preserve rejected rules / failed mappings
```

Astrology-specific miss categories:

```text
INPUT MISS
CALCULATION MISS
SYSTEM-MIX MISS
INTERPRETATION MISS
TIMING-WINDOW MISS
CAPTURE / LIFE-AREA MISS
MAGNITUDE MISS
BASE-RATE / FALSE-POSITIVE MISS
RETROFIT MISS
UNKNOWABLE / INSUFFICIENT-EVIDENCE
```

---

## 20. Imported Xyool core principles

The following are direct implementations of Xyool core primitives, not imported stock-market calibrations:

```text
exact identity before inference
source quality / freshness
state and state delta
transitions / gates / timers
uncertainty and invalidation
anti-double-counting
persistence / decay
anti-lookahead
miss-to-question learning
positive + negative controls
fail-closed handling of material unknowns
principle vs local calibration separation
```

Current status in this domain:

```text
DOMAIN CANONICAL as process discipline
ASTROLOGICAL predictive/interpretive efficacy remains VALIDATION REQUIRED
```

---

## 21. Explicitly local calibrations

These must be declared and validated locally rather than treated as Xyool-core truths:

```text
zodiac choice
ayanamsha
house system
aspect set
orb widths
applying/separating weights
planet / point inclusion
essential / accidental dignity rules
sect rules
nakshatra rules
time-lord technique
profection rules
dasha system
progression method
solar-arc method
return-chart rules
eclipse windows
retrograde interpretation
benefic / malefic weighting
synastry / composite rules
rectification method
forecast lead / lag windows
event-category mappings
confidence thresholds
```

A calibration supported in one astrology tradition does not automatically transfer to another.

---

## 22. Domain laws

### Law 1 — Calculation before interpretation
Do not interpret a configuration that has not been established under declared inputs and settings.

### Law 2 — System identity before inference
A reading without zodiac/house/technique identity is incomplete when those choices could change the result.

### Law 3 — Do not silently mix traditions
Hybrid methods are allowed only when every imported component is named and its authority is tracked.

### Law 4 — Birth-time precision limits claim precision
Unknown or approximate birth time must propagate into uncertainty about houses, angles, and other time-sensitive factors.

### Law 5 — Geometry is not meaning
A measured conjunction, square, transit, dasha boundary, or return is a calculation state. Its meaning is a separate interpretive claim.

### Law 6 — Dynamic windows must open and close
An applying transit or timing period cannot remain "active" forever. Record entry, peak/exactness where relevant, separation, and closure.

### Law 7 — Predictions must be falsifiable
A forecast needs a defined category/window and a miss condition before it can count as predictive evidence.

### Law 8 — No post-hoc rescue
Do not expand the orb, change houses, add a new technique, or redefine the event after seeing the result unless the original prediction is first recorded as a miss/ambiguous result.

### Law 9 — Correlation is not automatically causation
Observed correspondence can support an association hypothesis. Causal claims require separate evidence.

### Law 10 — Base rates matter
A common life event is weak evidence unless the forecast adds timing, specificity, magnitude, or discrimination beyond the base rate.

### Law 11 — Controls are mandatory for validation
A method that fits real cases must also be tested against cases where it should not fit.

### Law 12 — User agency remains intact
Astrological interpretation describes possible patterns, timing hypotheses, or symbolic frames; it does not make human choices inevitable.

### Law 13 — Preserve exact degree before categorical compression
When degree-level analysis is enabled, preserve exact longitude before mapping a body/point into sign, house, decan, or other larger partitions. Do not discard fine-grained state merely because a categorical wrapper exists.

### Law 14 — Degree meaning and stellar meaning are separate claims
An intrinsic degree interpretation and an interpretation derived from nearby fixed stars must retain separate rule identities, provenance, and validation state.

---

## 23. Worked process example — synthetic

Purpose: demonstrate the domain workflow, not prove astrology.

```text
Subject: Synthetic A
Birth data: exact and verified for test purposes
System: Western Tropical
House system: Whole Sign
Aspect policy: major Ptolemaic aspects, declared orb policy
Technique: natal + transits only

Calculated state:
Transit Saturn is approaching an exact aspect to a declared natal career/public-role indicator.

Pre-outcome hypothesis:
A material increase in responsibility, constraint, restructuring, or formalization connected to career/public role is more likely during the predeclared 30-day window around exactness than during matched control windows.

Hit definition:
A dated, material career/public-role event meeting prewritten criteria occurs inside the window.

Miss definition:
No qualifying event occurs inside the window.

Controls:
Matched 30-day non-contact windows; shuffled event dates; same chart with the target transit removed from the interpretation set.

Status:
PROCEDURAL EXAMPLE ONLY — NOT VALIDATION EVIDENCE
```

---

## 24. Negative / control example — synthetic

```text
Test:
Run an angle/house-specific forecast using an exact-time chart.
Then shift the birth time enough to materially move the angles/houses while keeping date and place fixed.

Expected specificity requirement:
If the method claims houses/angles are causally or predictively important, the interpretation or predicted capture area should change in a principled way.

Negative-control failure:
If both materially different charts produce the same flexible reading and both are counted as hits, the method has poor discrimination and the rule should be demoted or redesigned.
```

Status: **CONTROL DESIGN / NOT YET EXECUTED**

---

## 25. Domain readiness

```text
[x] objective defined
[x] entities defined
[x] evidence hierarchy defined
[x] state model defined
[x] transition model defined
[x] gates/timers defined
[x] action authority defined
[x] success/failure defined
[x] freshness/invalidation rules defined
[x] miss loop defined
[x] imported core principles labeled
[x] local calibrations separated
[x] worked procedural example
[x] negative/control design
[ ] calculation engine validation suite executed
[ ] historical frozen-case set executed
[ ] prospective validation set executed
[ ] control set executed
```

Therefore the domain remains:

```text
EXPERIMENTAL
```

It must not be promoted to ACTIVE solely because the architecture is complete.

---

## 26. Handoff instruction

For astrology work:

1. Read Xyool meta-architecture.
2. Load this manifest.
3. Lock birth/event inputs and astrology system.
4. Separate calculated facts from interpretive claims.
5. Use `domains/astrology/RUN-SEQUENCE.md` for material readings/forecasts.
6. Use `domains/astrology/VALIDATION.md` when testing whether a technique actually performs.
7. Do not import stock-market objectives, scores, timing windows, or capital actions.
8. Preserve misses and negative controls.

Core rule:

> **Measure the sky precisely, label the interpretive system explicitly, predict before observing when testing prediction, and let outcomes refine the astrology domain rather than rewriting the past.**
