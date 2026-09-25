# Xyool Astrology — Scoring & Calibration

Status: **EXPERIMENTAL DOMAIN CANONICAL / PERFORMANCE MEASUREMENT AUTHORITY**

Purpose: score forecasts and rules in a way that rewards specificity, calibration, discrimination, and honest misses rather than flexible storytelling.

Core rule:

> **A scoring system must make it possible for astrology to lose.**

---

## 1. Separate scoring dimensions

Never reduce all performance to one master score before the components are understood.

Track:

```text
input_integrity
calculation_accuracy
rule_reproducibility
specificity
category_accuracy
capability_accuracy
capture_accuracy
window_precision
magnitude_accuracy
false_positive_rate
miss_rate
ambiguous_rate
coverage
calibration
discrimination_vs_control
out_of_sample_replication
```

---

## 2. Categorical forecasts

Minimum result states:

```text
HIT
MISS
AMBIGUOUS
UNAVAILABLE
```

`AMBIGUOUS` cannot be used as a convenient substitute for a miss. The protocol should state in advance what creates ambiguity.

Track both:

```text
resolved_accuracy = hits / (hits + misses)
coverage = (hits + misses) / all forecasts
```

A method that appears accurate only by labeling most difficult cases ambiguous should fail the coverage test.

---

## 3. Binary probabilistic forecasts

If numerical probabilities are calibrated and permitted:

### Brier score

```text
BS = mean((p - y)^2)
```

where `y ∈ {0,1}`.

Lower is better.

Always compare against:

```text
base-rate forecast
simple climatology / frequency forecast
relevant control system
```

### Log loss

```text
LL = -mean(y*ln(p) + (1-y)*ln(1-p))
```

Clip only for numerical stability using a declared epsilon. Overconfident wrong forecasts are penalized heavily.

---

## 4. Ordered confidence bands

Before numerical probabilities are justified, use ordered bands:

```text
LOW
MEDIUM
HIGH
```

or:

```text
LESS FAVORABLE
MIXED / UNCERTAIN
FAVORABLE
LIKELY
```

Validation requirement:

```text
observed performance should be monotonic across ordered bands
```

If HIGH does not outperform MEDIUM, the confidence model is not calibrated.

---

## 5. Calibration tables

For each band or probability bin track:

```text
forecast_count
mean_predicted_probability if numeric
observed_frequency
confidence_interval
mean_specificity
mean_window_width
```

Do not claim calibration from tiny cells. Report sample size prominently.

---

## 6. Timing score

A timing method should be rewarded for narrowing useful windows, but not for creating excessive windows.

Track:

```text
window_width
number_of_windows_searched
fraction_of_total_time_flagged
hit_rate_inside_windows
base_rate_inside_matched_control_windows
false_positive_windows
```

A method that flags 90% of the calendar has little timing discrimination even if most events occur inside a flagged window.

Useful derived quantity:

```text
coverage_fraction = total_flagged_time / total_observation_time
```

Evaluate event capture relative to coverage fraction.

---

## 7. Specificity score principles

Specificity increases when a claim narrows:

```text
what
where / capture domain
when
magnitude
direction
```

Do not use an arbitrary universal specificity formula initially. Record these dimensions separately and later learn which dimensions predict meaningful discrimination.

---

## 8. Base rates

Every event/capability category used in forecasting should eventually have a base-rate table.

Possible strata:

```text
subject
age/life-stage where relevant
weekday/time-of-day for behavior/capability outcomes
season
category
observation method
```

Do not over-stratify sparse data.

A prediction of a common event needs substantially more timing/specificity information to be evidentially impressive.

---

## 9. Multiple-comparison correction

Track the search space:

```text
systems inspected
techniques inspected
rules inspected
candidate aspects/configurations
capabilities considered
windows considered
```

For confirmatory statistical tests, support conventional correction methods as appropriate:

```text
Bonferroni / Holm for small confirmatory families
Benjamini-Hochberg FDR for larger exploratory families
permutation tests when analytic assumptions are poor
```

Do not use a correction mechanically; predefine the hypothesis family.

---

## 10. Discovery versus confirmation

Separate:

```text
DISCOVERY SET
VALIDATION SET
PROSPECTIVE SET
```

A rule discovered on a case cannot earn confirmatory credit from that same case.

If data is limited, use cross-validation carefully but preserve a final untouched set whenever possible.

---

## 11. Paired comparison

When comparing systems, use the same cases/windows for both methods when practical.

Compare paired differences in:

```text
accuracy
Brier score
log loss
false-positive rate
window coverage
```

Paired designs reduce noise from case difficulty.

---

## 12. Fusion / convergence score

For combined systems report:

```text
best_single_system
fusion_system
fusion_minus_best_single
ablation_per_system
ablation_per_dependency_group
```

The fusion model is valuable only if its gain survives untouched/prospective cases and is not explained by larger search space.

---

## 13. Translation score

Capability translation is scored against both:

```text
native source interpretation
observed capability outcome
```

A translation can fail even when the source-native reading is preserved correctly.

Measure whether translation adds usefulness without increasing breadth/ambiguity.

---

## 14. Tuner compression score

Compare five-signal Tuner outputs against the full capability vector.

Track:

```text
information retained
prediction performance retained
contradictions lost
user/action utility if measured
```

Compression is successful if it substantially reduces complexity without materially degrading validated signal.

---

## 15. Minimum reporting table

Every validation report should include at least:

```text
N forecasts/cases
N resolved
N ambiguous
N unavailable
hit rate
false-positive rate or control comparison
window coverage if timing work
confidence calibration if used
system/rule versions
whether cases were discovery, validation, or prospective
```

---

## 16. No winner from noise

When differences are small relative to sample uncertainty, report:

```text
NO RESOLVED PERFORMANCE DIFFERENCE
```

Do not force a ranking just because one raw percentage is numerically larger.

---

## 17. Promotion evidence

A rule/system should not be called supported solely because `p < 0.05` or because a hit rate looks high.

Promotion should consider:

```text
effect size
uncertainty
base rate
controls
out-of-sample replication
calibration
false positives
search space
rule stability
practical specificity
```

Final rule:

> **Score the frozen claim against reality, not the story told after reality is known.**

---

## 18. Incremental Star Astrology scoring

Use the A→E model ladder rather than scoring the richest chart alone.

Primary comparisons:

~~~text
A vs B — intrinsic degree increment
A vs C — stellar-neighborhood increment
A vs D — degree + stellar increment
D vs E — bounded minor-body increment
~~~

For probabilistic binary forecasts define:

~~~text
delta_Brier(A,X) = Brier(A) - Brier(X)
~~~

Positive delta means X improved on A.

Also report:
- log-loss difference;
- calibration;
- event prevalence;
- false positives;
- calendar/window coverage;
- effective sample size where overlapping windows create dependence.

## 19. Proper-score boundary

Numeric forecast probabilities are allowed only when a named calibration model/version exists.

Use proper scoring rules so confident wrong forecasts are penalized.

Uncalibrated interpretive confidence remains an ordinal band.

## 20. Complexity penalty by evidence, not arbitrary score

Do not invent an opaque master penalty.

Instead expose:
- number of admitted objects;
- rule families;
- star contacts;
- degree hypotheses;
- asteroid hypotheses;
- windows;
- outcome categories.

A richer model must earn its complexity through out-of-sample incremental performance.
