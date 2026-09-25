# Xyool Astrology — Signal Dependency Graph

Status: **EXPERIMENTAL DOMAIN CANONICAL / ANTI-DOUBLE-COUNTING AUTHORITY**

Purpose: distinguish genuine cross-system corroboration from repeated interpretations of the same underlying information.

Core rule:

> **Agreement is informative only to the extent that the agreeing signals contribute non-duplicated information.**

---

## 1. Dependency layers

Track dependencies at five levels:

```text
L0 — INPUT DEPENDENCY
same birth date/time/location or same civil date

L1 — RAW ASTRONOMICAL / CALENDAR DEPENDENCY
same planetary longitude, same lunation, same Maya conversion, same day index

L2 — DERIVED CONFIGURATION DEPENDENCY
same aspect, same house activation, same nakshatra placement, same cycle position

L3 — INTERPRETIVE LINEAGE DEPENDENCY
one rule copied/translated from another source or tradition

L4 — OUTPUT TRANSLATION DEPENDENCY
multiple native rules mapped through the same capability/Tuner translation rule
```

Two outputs can come from different named systems and still be strongly dependent.

---

## 2. Dependency node

```yaml
dependency_id:
layer: L0 | L1 | L2 | L3 | L4
type:
identifier:
source_system_ids: []
parent_ids: []
description:
```

A signal may reference multiple dependency nodes.

---

## 3. Signal identity

Each signal used in synthesis should record:

```yaml
signal_id:
system_id:
rule_id:
capability:
direction:
strength_band:
dependency_ids: []
```

Signals without dependency metadata are allowed for exploratory readings but should not receive independence-adjusted convergence weight.

---

## 4. Dependency groups

For synthesis, group signals that share a material upstream dependency.

Examples:

### Example A — Same astronomical event

```text
Western: Mars transit square natal Mercury
Modern Western: "communication conflict"
Traditional Western: "Mercury afflicted by Mars"
```

These may be two interpretive traditions but one primary astronomical input.

### Example B — Different derived use of same planet

```text
Jyotish transit of Saturn
Western Saturn transit
```

Depending on zodiac/configuration differences, these may share substantial astronomical dependence even if derived placements differ.

### Example C — More independent source

```text
Western transit signal
MAYA.TRAD Chol Q'ij day rule
```

These may have lower direct computational dependence, though they still share civil-date timing and potentially analyst/output translation dependencies.

---

## 5. Independence states

Use qualitative states until empirically calibrated:

```text
HIGHLY_DEPENDENT
PARTIALLY_DEPENDENT
LOW_DEPENDENCY
DEPENDENCY_UNKNOWN
```

Do not convert these states into fixed numerical weights until validation data supports the mapping.

---

## 6. Effective evidence groups

For an uncalibrated synthesis, report both:

```text
RAW SIGNAL COUNT
e.g. 5 supporting signals

EFFECTIVE INDEPENDENT GROUP COUNT
e.g. 2 distinct upstream information groups + 1 unknown
```

The second is more informative than raw votes but still does not equal probability.

---

## 7. Contradiction matrix

Contradictions should also be dependency-aware.

A contradiction between two highly dependent interpretations may indicate rule disagreement around one input.

A contradiction between low-dependency systems may be stronger evidence of genuine model uncertainty.

Record:

```yaml
signal_a:
signal_b:
relationship: support | conflict | orthogonal
shared_dependencies: []
conflict_level: native_meaning | capability_translation | timing | capture | magnitude
```

---

## 8. Convergence promotion tests

A convergence rule cannot be promoted without:

```text
INDIVIDUAL BASELINES
performance of each constituent system/rule

FUSION
performance of the frozen combination rule

ABLATION
remove one system/group at a time

SHUFFLE
break alignment between one system and outcomes

DEPENDENCY-AWARE ABLATION
remove all signals sharing an upstream dependency group
```

If fusion performance disappears after collapsing duplicates, the original convergence was likely inflated.

---

## 9. Information gain target

The future quantitative target is not `number of agreeing systems`.

It is closer to:

```text
incremental out-of-sample information added by a signal/group
conditional on the signals already known
```

Possible future measures once sample sizes permit:

```text
conditional log-loss improvement
Brier score improvement
mutual information / conditional mutual information
likelihood-ratio improvement
out-of-sample calibration improvement
```

Do not deploy these as authoritative with tiny samples.

---

## 10. Duplicate semantic labels

Do not count semantic paraphrases as independent evidence.

Example:

```text
"communication friction"
"arguments likely"
"verbal tension"
```

If all are generated from one rule/configuration, they are one prediction family.

---

## 11. Dependency graph closure

When a forecast closes, store which dependency groups contributed.

This enables later questions such as:

```text
Which raw configurations actually add signal?
Which systems are redundant?
Which capability translations create false convergence?
Does Maya add information conditional on Western/Jyotish?
Do fixed stars add anything after ordinary planetary configurations are known?
```

Final rule:

> **Count causes of information, not labels of interpretation.**

## Degree-field dependency rule

Star Astrology introduces an important dependency distinction.

Example:

~~~text
planet at exact longitude
→ sign placement
→ decan placement
→ house placement
→ nearby-star projection
→ intrinsic-degree interpretation
~~~

These are not automatically independent signals because they share the same underlying longitude/input.

Track at minimum:
- exact-degree node as the shared L1/L2 dependency;
- sign/decan/house wrappers derived from that node;
- stellar-neighborhood calculations derived from the same coordinate but with additional star-catalogue information;
- intrinsic-degree symbolism as a separate interpretive lineage;
- asteroid/planet occupants as separate objects that may converge on the same degree node.

Do not count:
"planet in 10° Scorpio"
+ "second decan Scorpio"
+ "same point in the 1st house"
+ "degree-10 meaning"

as four independent confirmations merely because four labels exist.

Ablation should test whether degree/star information adds value beyond the categorical wrappers already derived from the same coordinate.
