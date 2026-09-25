# Xyool Astrology — Benchmark Ladder

Status: **EXPERIMENTAL DOMAIN CANONICAL / READINESS BENCHMARKS**

Purpose: define increasingly difficult benchmarks so the domain improves by passing concrete tests rather than by accumulating more interpretive material.

---

## Benchmark 0 — Repository integrity

Goal: domain can be reconstructed by a future run.

Pass conditions:

```text
[ ] domain registered
[ ] first-class astrology node exists
[ ] system registry exists
[ ] rule registry exists
[ ] data contracts exist
[ ] run sequence exists
[ ] validation/scoring protocol exists
[ ] preregistration protocol exists
```

---

## Benchmark 1 — Deterministic infrastructure

Goal: generic non-astrological mechanics are executable and tested.

Required:

```text
canonical hashing
forecast freeze verification
atomic window compiler
dependency grouping
Brier/log-loss utilities
categorical score summary
```

These mechanics should work independently of whether astrology itself is valid.

---

## Benchmark 2 — Calculation agreement

Goal: reproduce system-native calculations/conversions.

Separate suites:

```text
Western tropical
Western sidereal
Jyotish
fixed stars/parans
MAYA.TRAD
DREAMSPELL.ARGUELLES
```

Pass criteria must be technique-specific and declared before testing.

Material calculation disagreement blocks interpretive validation for that test case.

---

## Benchmark 3 — Rule reproducibility

Goal: a frozen rule produces the same output regardless of known outcome.

Tests:

```text
same input + same settings + same rule version → same trigger state
same rule version → same native interpretation object
same capability translation version → same capability mapping
```

Human-language rendering may vary; the structured claim must not.

---

## Benchmark 4 — Blinded descriptive discrimination

Goal: determine whether a system can distinguish targets from decoys.

Examples:

```text
chart-to-profile matching
Maya-date meaning to target/decoy matching
fixed-star configuration classification
capability-state matching
```

Require predeclared scoring and decoy construction.

---

## Benchmark 5 — Frozen historical timing

Goal: generate predictions from only information available before known outcomes.

Requirements:

```text
blinded/hidden outcomes where practical
frozen rule set
finite windows
matched controls
all windows closed
```

Historical success is still weaker than prospective success because leakage is difficult to eliminate completely.

---

## Benchmark 6 — Prospective single-system forecasting

Goal: each major system proves its own performance before fusion.

Run separate forecast ledgers for:

```text
Western
Jyotish
Maya traditional
Dreamspell
stellar/fixed-star if operational
```

Do not change system definitions mid-benchmark without beginning a new rule/version cohort.

---

## Benchmark 7 — Capability translation

Goal: determine whether native symbolic outputs can be converted into the shared 10-capability vector reproducibly and usefully.

Compare:

```text
source-native only
capability translation
control translation
```

The translation should improve operational interpretability without making claims so broad that false positives rise materially.

---

## Benchmark 8 — Atomic timing advantage

Goal: determine whether high-resolution boundary splitting improves timing.

Compare:

```text
atomic windows
coarser predefined windows
random/matched windows
```

Measure improvement relative to calendar coverage. Finer segmentation is rejected if it mainly multiplies chances to find retrospective matches.

---

## Benchmark 9 — Cross-system fusion

Goal: determine whether convergence adds independent signal.

Required:

```text
individual baselines
frozen fusion rule
dependency metadata
system ablations
dependency-group ablations
prospective/untouched comparison
```

Fusion must beat the strongest individual contributor by more than ordinary sampling uncertainty to justify extra authority.

---

## Benchmark 10 — Tuner compression

Goal: determine whether 5-signal compression retains enough validated information from the 10-capability vector.

Test:

```text
predictive retention
contradiction retention
action usefulness
complexity reduction
```

If the compression loses material signal, the system should expose the full vector instead.

---

## Benchmark 11 — Stability across populations / contexts

Goal: identify boundary conditions.

Stratify only where data allows:

```text
subject-specific versus pooled
location
observation type
calendar/time horizon
life/capability category
system configuration variant
```

Do not call a rule universal if it only works in one narrow cohort.

---

## Benchmark 12 — Robustness to analyst freedom

Goal: measure how much performance depends on interpretive discretion.

Tests:

```text
independent analysts using same frozen rules
structured engine versus free-form reading
alternative wording while holding structured claims fixed
blind scoring by independent scorer
```

High sensitivity to analyst discretion lowers confidence that the rule itself carries the signal.

---

## Benchmark 13 — Adversarial controls

Challenge the system with:

```text
shuffled dates
wrong-but-plausible birth times
matched placebo windows
decoy charts
synthetic random signals
source-label swaps
hidden contradictory signals
```

A robust system should fail or lower confidence when its defining inputs are disrupted.

---

## Benchmark 14 — External replication

Goal: another implementation can reproduce the structured calculation/rule outputs and scoring from the same frozen records.

This is a strong maturity threshold.

---

# Promotion states

```text
ARCHITECTURE_DEFINED
INFRASTRUCTURE_TESTED
CALCULATION_VALIDATED
RULE_TESTING
PROSPECTIVE_TESTING
PARTIALLY_SUPPORTED
SUPPORTED_WITH_BOUNDARIES
ACTIVE
```

The domain should advance only when the underlying benchmark has actually been executed.

---

# Improvement bottleneck definition

The architecture has reached a meaningful bottleneck when additional internal documentation/code would add less value than obtaining one of:

```text
1. validated astronomical/calendar calculation adapters;
2. a sourced/versioned rule corpus for each selected tradition;
3. representative frozen historical cases;
4. prospective forecast/outcome data;
5. independent scorers/replicators;
6. enough observations to calibrate probabilities and convergence weights.
```

At that point, adding more theory risks complexity without evidence.

Final rule:

> **When the next improvement requires new evidence rather than new architecture, stop architecting and collect evidence.**