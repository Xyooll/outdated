# Xyool Astrology — Null & Baseline Models

Status: **EXPERIMENTAL DOMAIN CANONICAL / COUNTERFACTUAL AUTHORITY**

Purpose: define what astrology must beat before an apparent pattern can be treated as added information.

Core rule:

> **A forecast is informative only relative to a plausible alternative that did not use the astrology signal.**

---

## 1. Null-model hierarchy

Use the simplest relevant comparator first, then stronger context-aware baselines.

```text
N0 — UNCONDITIONAL BASE RATE
ordinary frequency of the outcome

N1 — PERSONAL BASELINE
subject's own ordinary state/event rate

N2 — CALENDAR BASELINE
time-of-day / day-of-week / season

N3 — RECENT-STATE BASELINE
prior capability/event state

N4 — CONTEXT BASELINE
known schedule/workload/location/context

N5 — PLACEBO SYMBOLIC MODEL
shuffled dates/charts/windows or decoy rules
```

Astrology adds signal only to the extent it improves beyond the relevant baseline.

---

## 2. Capability nulls

For capability outcomes such as Focus or Recovery, initial null predictors may include:

```text
personal mean
clock time
day of week
sleep/rest context
prior measurement
planned workload
```

Do not claim astrological timing if a simple 9-AM-vs-11-PM effect explains the same pattern.

---

## 3. Event nulls

For events, estimate where practical:

```text
ordinary event frequency
seasonality
subject-specific event rate
inter-event interval distribution
exposure/opportunity count
```

Example:

```text
If the subject receives work messages every weekday,
"communication event likely today" is a weak prediction.
```

---

## 4. Window-coverage null

Timing systems must report how much calendar time they flag.

```text
coverage_fraction = flagged_time / observed_time
```

Compare:

```text
fraction of target events captured
versus
fraction of time flagged
```

If a method flags 80% of time and captures 80% of events, it has little discrimination.

---

## 5. Matched placebo windows

Build control windows matched on relevant context but without the target astrology configuration.

Match candidates on:

```text
clock time
day of week
calendar proximity
workday/weekend
subject
measurement type
```

Do not choose controls after seeing outcomes.

---

## 6. Date shuffle

Break the link between astrology timing and outcomes while preserving outcome structure.

Possible shuffles:

```text
permute whole subject-days
circularly shift outcome series
shuffle event dates within declared blocks
shuffle astrology date labels
```

Choose a shuffle that preserves important autocorrelation/context rather than destroying everything trivially.

---

## 7. Birth-time placebo

For time-sensitive techniques:

```text
perturb birth time by a predeclared distribution
recalculate chart-dependent factors
compare target performance with placebo times
```

Do not use this control for techniques genuinely independent of birth time.

---

## 8. Decoy charts/descriptions

For descriptive matching:

```text
true chart + plausible decoy charts
or
true rule-derived description + decoy descriptions
```

Keep length, positivity, detail, and stylistic quality comparable so the target cannot be selected from formatting cues.

---

## 9. Random-signal baseline

Generate synthetic signals with matched frequency/window width.

Purpose:

```text
estimate how many “hits” emerge purely because the framework generates many windows
```

This is especially important for atomic high-resolution timing.

---

## 10. Alternative-system baseline

A system should be compared against materially different systems without assuming either is true.

Example:

```text
Western-only
Jyotish-only
Maya-only
Dreamspell-only
random matched-cycle baseline
```

This helps determine whether one system actually discriminates or whether flexible interpretation makes all systems look similarly accurate.

---

## 11. Simple model before complex model

Before adding fusion, ask whether a simpler model already performs as well.

Complexity ladder:

```text
base rate
→ one system
→ one system + personalization
→ multi-system fusion
→ capability translation
→ Tuner compression/action layer
```

Promote complexity only when it adds out-of-sample value.

---

## 12. Persistence null

For slowly changing capabilities/outcomes, compare against:

```text
predict next state = previous state
```

A timing system that cannot beat state persistence may be tracking persistent real-life conditions rather than astrological transitions.

---

## 13. Opportunity exposure null

Opportunity events depend on exposure.

Examples:

```text
number of applications submitted
number of people contacted
number of meetings attended
number of open channels
```

An increased opportunity rate during a period of dramatically increased outreach should not automatically be credited to astrology.

---

## 14. Null-model preregistration

Every confirmatory benchmark should state:

```yaml
primary_null:
secondary_nulls: []
matching_variables: []
shuffle_method:
random_seed:
performance_metric:
```

Do not replace a strong null with an easier one after results are known.

---

## 15. Improvement threshold

Do not define one permanent universal threshold yet.

At minimum report:

```text
astrology metric
null metric
difference
sample size
uncertainty / resampling interval when available
```

A positive but unstable difference remains provisional.

---

## 16. Null failure is useful

If astrology does not beat a baseline:

```text
preserve result
identify whether the rule adds no information or the experiment lacked power
narrow/reject only after appropriate replication
```

Do not hide null results by switching outcome categories.

Final rule:

> **The question is not “did the astrology match?” but “did it add information that a reasonable non-astrological model did not already contain?”**

---

## 17. Star Astrology nulls

When exact-degree, stellar, or minor-body layers are tested, add nulls that preserve search-space opportunity while destroying the claimed identity.

### Rotated-star catalogue

Preserve approximate star density/magnitude structure while rotating longitudes by a frozen offset.

Question:

~~~text
Do actual star identities/locations outperform a similarly dense false sky?
~~~

### Permuted degree-symbol corpus

Keep the 360-cell structure but permute labels/meanings under a frozen random seed.

Question:

~~~text
Does the claimed degree identity matter, or does any rich 360-symbol dictionary fit similarly well?
~~~

### Minor-body semantic-label shuffle

Keep the selected asteroid positions but permute semantic identities/labels.

Question:

~~~text
Does the declared object identity add signal beyond simply adding more moving points?
~~~

### Star-density / contact-opportunity denominator

Report:
- stars admitted;
- magnitude threshold if any;
- orb/contact threshold;
- fraction of degree space covered by at least one admitted star.

A dense catalogue with broad orbs may make a star contact almost inevitable.

## 18. Ablation baseline

Use the frozen ladder in:
`library/knowledge/ablation-validation-a-e.md`

Do not claim value for B/C/D/E unless the added layer improves beyond its simpler parent model on untouched/prospective data.
