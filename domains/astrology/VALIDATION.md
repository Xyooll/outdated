# Xyool Astrology — Validation Framework

Status: **EXPERIMENTAL / REQUIRED BEFORE DOMAIN PROMOTION**

Purpose: define how Xyool tests calculation accuracy, interpretive consistency, timing specificity, capability translation, cross-system convergence, and failure modes without hindsight fitting.

Supporting files:

- `domains/astrology/SYSTEM-REGISTRY.md`
- `domains/astrology/RULE-REGISTRY.md`
- `domains/astrology/SIGNAL-OUTPUT-MODEL.md`
- `domains/astrology/MAYA.md`

---

## 1. Validation layers

Astrology contains different claim types. They must not share one undifferentiated confidence score.

```text
LAYER A — INPUT INTEGRITY
Are date, time, place, timezone, correlation choices, and uncertainty correct?

LAYER B — CALCULATION / CONVERSION ACCURACY
Are chart positions, calendar identities, aspects, periods, parans, and exact boundaries correct under declared settings?

LAYER C — RULE REPRODUCIBILITY
Does the same declared rule produce the same interpretation before and after outcome knowledge?

LAYER D — DESCRIPTIVE DISCRIMINATION
Does the interpretation distinguish the target chart/date better than controls?

LAYER E — TIMING / FORECAST PERFORMANCE
Do predeclared timing hypotheses resolve with useful specificity against base rates and controls?

LAYER F — CAPABILITY TRANSLATION
Does translation into Mental Capacity / Focus / Action / etc. preserve useful information and improve practical discrimination?

LAYER G — CROSS-SYSTEM CONVERGENCE
Does combining independent systems outperform the strongest individual system on untouched/prospective cases?

LAYER H — CROSS-CASE GENERALIZATION
Does the rule survive untouched cases rather than only the cases that inspired it?
```

A method may pass one layer and fail another.

---

## 2. Calculation / conversion validation suite

For astronomical chart systems compare the chosen calculation source with an independent reputable engine across cases including:

```text
ordinary modern dates
historical dates
DST boundary dates
locations near timezone boundaries
high latitudes
unknown-time charts
Moon-sign boundary cases
Ascendant-sign boundary cases
retrograde stations
ingresses
exact aspect times
sidereal calculations with named ayanamsha
multiple house systems
fixed-star/paran boundary cases
```

For `MAYA.TRAD` include:

```text
Gregorian date → Tzolk'in / Chol Q'ij
Gregorian date → Haab
Calendar Round identity
Long Count where used
correlation/converter version
boundary dates
```

Use an independent reference such as Smithsonian *Living Maya Time* where appropriate.

For `DREAMSPELL.ARGUELLES` include:

```text
Gregorian date → Kin
Tone
Solar Seal
Wavespell / derived objects if used
leap-day handling
implementation/version agreement
```

Do not validate a Dreamspell implementation by assuming it should match `MAYA.TRAD`.

Record tolerances and exact disagreements explicitly.

Calculation failures must be fixed before interpretive testing uses those cases.

---

## 3. Rule registry

Every interpretive, timing, translation, and convergence rule used in validation must have an identity from `RULE-REGISTRY.md`.

Minimum fields:

```text
rule_id
rule_class
system_id
source
version
required inputs
trigger
native interpretation
window / boundary rule if relevant
falsification condition
status
```

Do not silently modify a rule after a result. Create a new version.

---

## 4. Historical frozen-case protocol

For each historical case:

1. Select the case before interpretation.
2. Freeze input data.
3. Hide the target outcome from the interpreter where practical.
4. Lock system IDs and allowed techniques.
5. Lock rule versions.
6. Generate the native reading before any cross-system synthesis.
7. Generate capability translations only from frozen rules.
8. Record category, timing window, magnitude if used, and miss condition.
9. Reveal the outcome.
10. Score using the predeclared rubric.
11. Run the miss loop without rewriting the original result.

Historical biographies can leak outcome knowledge into interpretation. Prefer blinded or partially blinded procedures when possible.

---

## 5. Prospective protocol

Minimum forecast object:

```text
forecast_id
subject_or_date_id
created_at
input_version
system_ids
rule_versions
technique_set
native_claims
capability_claims if used
predicted_category
capture_area if used
start
end
peak_if_relevant
magnitude_band_if_used
confidence_band
hit_definition
miss_definition
```

After the window:

```text
outcome_source
outcome_timestamp
objective_or_self_report
hit / miss / ambiguous / unavailable
per-rule contribution notes
notes written after scoring
```

Never extend the window because nothing happened.

---

## 6. Control architecture

A rule that produces apparently meaningful matches needs controls.

### Date-shuffle control
Shuffle outcome dates while holding rules fixed.

### Birth-time perturbation control
Shift time enough to change angles/houses/parans for techniques that depend on them.

### Placebo-window control
Compare predicted windows with matched windows where the target configuration is absent.

### Chart-description matching
Blindly match chart-derived descriptions to target versus decoy profiles.

### Maya date-description matching
Blindly match source-derived Maya day descriptions to target versus decoy dates/subjects.

### Dreamspell date-description matching
Test Dreamspell meanings under their own system rules, separately from Maya traditional meanings.

### Base-rate control
Compare target outcomes/capabilities in predicted windows against ordinary frequency for the same category.

### Alternative-system control
Compare materially different systems to detect readings so flexible that every system can be made to fit.

### Translation-null control
Compare system-native performance with and without Xyool capability translation.

---

## 7. Atomic-window validation

The timing engine splits at every material boundary rather than smoothing into broad phases.

Track:

```text
number_of_boundaries
number_of_atomic_windows
active_rule_ids_per_window
window_precision
window_hit_rate
false-positive windows
```

Test whether extra segmentation improves timing discrimination or merely creates more opportunities to claim a hit.

If finer windows increase false positives without improving discrimination, the segmentation rule must be revised.

---

## 8. Scoring principles

Do not begin with a single opaque master score.

Track dimensions separately:

```text
calculation_correctness
conversion_correctness
specificity
window_precision
category_accuracy
capability_accuracy
capture_area_accuracy
magnitude_accuracy
discrimination_vs_controls
false_positive_rate
miss_rate
ambiguous_rate
calibration_by_confidence_band
replication_across_untouched_cases
```

A broad statement that could match many outcomes receives less evidentiary weight than a narrow predeclared statement.

Do not count several descriptions of one outcome as several independent hits.

---

## 9. Confidence / probability calibration

The user prefers probability-oriented outputs, but numerical probabilities require empirical calibration.

Initial ordered bands may be:

```text
LESS FAVORABLE
MIXED / UNCERTAIN
FAVORABLE
LIKELY
```

or validation-only confidence labels:

```text
LOW
MEDIUM
HIGH
```

Do not assign precise numerical probabilities until enough target-domain evidence exists to calibrate them.

When sufficient data exists, map each band to observed frequencies and test calibration prospectively.

A `LIKELY` or `HIGH` class that does not resolve more reliably than weaker classes is not informative.

---

## 10. Birth-time uncertainty tests

For uncertain birth times:

1. Define a plausible interval.
2. Identify placements stable across the interval.
3. Identify placements that change.
4. Restrict claims to stable features unless rectification is explicitly being tested.
5. If rectifying, freeze the rectification rule before validation outcomes.
6. Reserve untouched outcomes to test the rectified time.

Do not use the same observations both to fit and validate a rectified birth time.

---

## 11. Multi-technique inflation control

Astrology offers many possible techniques. This creates a multiple-comparisons problem.

Before a test, declare the allowed technique set.

Track:

```text
number_of_systems_searched
number_of_techniques_searched
number_of_candidate_configurations
number_of_capability translations generated
whether technique was predeclared
whether interpretation was selected before outcome reveal
```

Rules discovered after outcome review become hypotheses for future cases, not proof from the discovery case.

---

## 12. Cross-system convergence validation

Convergence is a hypothesis, not a free confidence multiplier.

For every synthesis test record:

```text
participating systems
participating rule IDs
shared data dependencies
shared astronomical dependencies
shared interpretive lineage
raw agreement count
independence-adjusted assessment
combined output
best single-system output
```

Required tests:

### Independent baseline
Measure each system alone first.

### Fusion test
Measure the combined system using a frozen combination rule.

### Ablation test
Remove one system at a time and measure whether performance changes.

### Dependency test
Check whether apparent agreement comes from the same underlying astronomical fact or copied interpretive rule.

### Contradiction test
Measure whether explicit disagreement states improve calibration compared with forcing a consensus.

Convergence earns additional authority only if it adds out-of-sample/prospective discrimination beyond the strongest individual contributor.

---

## 13. Capability-translation validation

Test the user's practical capability layer independently from native astrology meanings.

Capability categories:

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

For each translation rule ask:

```text
Does the capability label preserve source meaning?
Can the capability outcome be observed or self-rated consistently?
Does the translation discriminate predicted windows from controls?
Does it improve action usefulness without broadening the claim until everything fits?
```

The same native symbol may translate differently under different source traditions; do not force universal mapping prematurely.

---

## 14. Tuner validation

Tuner signals:

```text
Energy
Direction
Stability
Intensity
Clarity
```

Validate the Tuner as a **compression layer**, not as an astrology source.

Compare:

```text
full capability vector performance
vs
five-signal Tuner performance
```

The Tuner is useful if it preserves enough information for practical decisions while reducing complexity. If compression hides important contradictions or reduces discrimination materially, keep the richer output.

The earlier heuristic `1–2 signals off = minor adjustment; 3+ off = question the broader cycle/sequence` remains `USER-DERIVED / UNVALIDATED` until tested.

---

## 15. Miss analysis

Every material miss should be classified before proposing a fix.

```text
INPUT MISS
CALCULATION / CONVERSION MISS
SYSTEM IDENTITY MISS
SOURCE / PROVENANCE MISS
RULE MISS
TIMING MISS
CAPABILITY-TRANSLATION MISS
CONVERGENCE MISS
TUNER-COMPRESSION MISS
CAPTURE MISS
MAGNITUDE MISS
BASE-RATE FALSE POSITIVE
MULTIPLE-COMPARISON FALSE POSITIVE
CONTROL FAILURE
OUTCOME-DATA FAILURE
UNKNOWABLE
```

Then ask:

```text
Was the missing information knowable?
Was the rule too broad?
Was the window too flexible?
Was a contradictory signal ignored?
Did outcome knowledge leak into interpretation?
Did correlated systems get double-counted as independent confirmation?
Would the proposed fix improve negative controls or merely rescue this case?
```

A case-specific rescue rule is not promoted.

---

## 16. Promotion discipline

No fixed numeric threshold is canonical yet.

A rule may move from HYPOTHESIS toward SUPPORTED only when it demonstrates, at minimum:

```text
reproducible calculation / conversion
stable rule identity
positive cases
negative/control cases
performance on untouched cases
no material lookahead leakage
specific falsification criteria
documented failure modes
replication beyond the discovery sample
```

A convergence rule additionally requires evidence that combination adds information beyond its strongest constituent.

Numeric thresholds should be added only after enough domain data exists to justify them.

---

## 17. Domain promotion plan

The astrology domain remains EXPERIMENTAL until these are executed, not merely designed:

```text
[ ] astronomical calculation-engine cross-check suite
[ ] timezone edge-case suite
[ ] Maya conversion cross-check suite
[ ] Dreamspell implementation/version suite
[ ] fixed-star/paran precision suite if ASTRO.STAR is operational
[ ] frozen historical-case set
[ ] negative/control set
[ ] untouched validation set
[ ] prospective forecast log
[ ] atomic-window closure process
[ ] machine-readable rule registry with versioning
[ ] capability-translation test set
[ ] cross-system convergence + ablation tests
[ ] Tuner compression tests
[ ] miss log
[ ] evidence showing which rules do or do not discriminate beyond controls
```

If a technique fails controlled validation, preserve that result.

Final rule:

> **Calculate each system correctly, test each system independently, and make convergence earn its weight.**