# Xyool Astrology — Signal & Output Model

Status: **EXPERIMENTAL DOMAIN CANONICAL / OUTPUT TRANSLATION LAYER**

Purpose: preserve rich system-native astrology while translating useful outputs into a practical shared capability language and, when desired, compressing that into the user's earlier Tuner framework.

Core rule:

> **Do not simplify before the source system has produced its own labeled result. Compression happens last.**

---

## 1. Output stack

```text
RAW CALCULATION / CALENDAR STATE
→ SYSTEM-NATIVE INTERPRETATION
→ CAPABILITY TRANSLATION
→ CROSS-SYSTEM CONVERGENCE / CONFLICT
→ ATOMIC TIME WINDOWS
→ TUNER COMPRESSION
→ OPTIONAL ACTION LEVERS
```

Each layer must remain inspectable.

---

## 2. Capability vector

The prior capability-optimization framework is preserved as the common output vocabulary.

```text
1. Mental Capacity
2. Focus
3. Action
4. Opportunity
5. Communication
6. Creation
7. Investigation
8. Connection
9. Recovery
10. Friction / Impulsiveness
```

These are not moral labels and should not be rendered as "good" versus "bad" days.

Preferred language:

```text
stronger / weaker
more available / less available
favorable / mixed / less favorable
likely / uncertain / less likely
supportive / frictional
```

The system should explain *what capability is emphasized and for what kind of action*, not simply call a period positive or negative.

---

## 3. Capability signal object

Each system may emit zero or more capability effects:

```text
system_id
rule_id
capability
polarity / direction
strength_band
confidence_band
start
end
peak_if_defined
native_interpretation_reference
translation_rule_id
dependencies
```

A capability translation is distinct from the native rule. If the translation is Xyool-created, mark it as a `DOMAIN HYPOTHESIS` until validated.

---

## 4. Probability discipline

The user prefers probability-based outputs.

Before numerical calibration exists, use ordered probability language rather than invented percentages:

```text
LESS FAVORABLE
MIXED / UNCERTAIN
FAVORABLE
LIKELY
```

Once prospective validation is large enough, the domain may map those bands to empirical hit frequencies.

Do not assign a number such as `73%` merely because multiple symbolic systems agree.

---

## 5. Atomic timing windows — no phase smoothing

The prior timing framework explicitly rejected broad phases.

Xyool must therefore construct **atomic windows**:

1. Gather every material start, exact/peak, boundary, and end time from every selected system.
2. Sort all boundaries chronologically.
3. Split the day / forecast horizon at every boundary.
4. Treat each unique interval as its own window.
5. Recompute the active capability vector for that interval.
6. If several influences overlap, the overlap is a new interval with its own output.

Example:

```text
09:00–10:17  signal set A
10:17–11:42  A + B
11:42–13:05  B
13:05–13:31  B + C + Maya day-boundary-derived rule if applicable
```

Do not merge these into "morning phase" or "afternoon phase" if the actual signal set changes inside them.

---

## 6. Cross-system convergence object

After each system produces its independent output, calculate convergence metadata:

```text
capability
supporting_systems
contradicting_systems
neutral_systems
raw_agreement_count
independence_adjusted_count
shared_dependencies
strongest_native_evidence
contradiction_type
combined_status
```

Do not use simple majority voting as authority.

Two methods driven by the same transit may represent one underlying information source. A Maya day count and a Western transit may be more independent than two Western techniques derived from the same planetary geometry.

The value of independence-adjusted convergence must be learned empirically.

---

## 7. Contradiction handling

Contradiction is information, not an error to hide.

Possible states:

```text
CONVERGENT
PARTIALLY CONVERGENT
ORTHOGONAL — systems speak to different capabilities
CONTRADICTORY
INSUFFICIENTLY COMPARABLE
```

When systems contradict, preserve both native outputs and lower synthesis confidence unless a prevalidated conflict-resolution rule exists.

---

# PART B — TUNER COMPRESSION

## 8. Five Tuner signals

The user's earlier Tuner framework compresses complexity into five foreground signals:

```text
ENERGY     — available level / charge
DIRECTION  — whether effort has a clear channel or vector
STABILITY  — grounding / consistency / ability to hold state
INTENSITY  — heat / pressure / activation amplitude
CLARITY    — signal quality / discernment / mental or perceptual cleanliness
```

These are **output-compression variables**, not astrology primitives.

Astrology, Maya systems, Wu Xing, Human Design, Ayurveda, or other declared systems may contribute upstream evidence, but the Tuner cannot retroactively change what those systems said.

---

## 9. Tuner mapping object

```text
source_capabilities
source_systems
Energy
Direction
Stability
Intensity
Clarity
compression_rule_version
confidence
```

Initially, mappings from the 10-capability vector to the five Tuner signals are hypotheses and should be versioned.

Example conceptual relationships may include:

```text
Action + Recovery → Energy balance information
Focus + Opportunity → Direction information
Recovery + low Friction → Stability information
Action + Friction → Intensity information
Mental Capacity + Focus + Investigation → Clarity information
```

These are starting hypotheses, not fixed equations.

---

## 10. Fast Tuner use

Prior operating logic:

```text
SCAN 5 SIGNALS
→ IDENTIFY THE LARGEST IMBALANCE
→ APPLY THE SMALLEST COHERENT CORRECTION
→ RESCAN
```

Earlier shorthand:

```text
1–2 signals off → minor adjustment
3+ signals off → question the broader cycle / sequence rather than stacking more force
```

This remains a user-derived heuristic and should be labeled accordingly until validated.

---

## 11. Desired output modes

The earlier framework used three broad desired outcomes:

```text
HIGH PERFORMANCE
RECOVERY
TRANSFORMATION
```

The same astrology window can be useful for different goals. Therefore Xyool should not output a single universal recommendation.

Instead:

```text
CURRENT CAPABILITY VECTOR
+ USER GOAL
→ BEST-FIT ACTION CLASS
```

---

## 12. Four controllable levers

The earlier Tuner used:

```text
Breath
Body
Fuel
Attention
```

These are optional self-regulation/action levers after the astrology output, not proof that the astrology signal is true.

Any health-related interpretation of these levers must follow ordinary health/safety standards rather than astrology authority.

---

## 13. Wu Xing sequencing

The user's prior sequencing rule was:

```text
Wood → Fire → Earth → Metal → Water → Wood
```

with actions stacked toward one outcome so each step prepares the next.

Preserve this only when `ADJ.WUXING` is explicitly active. Astrology itself does not inherit the sequence.

Potential synthesis order:

```text
astrology / Maya / other systems identify current capabilities
→ Tuner identifies imbalance or objective
→ Wu Xing may organize the order of chosen actions
```

This preserves correspondence without pretending the systems are the same.

---

## 14. Output template

A compact user-facing output may eventually look like:

```text
WINDOW: 10:17–11:42

CAPABILITIES
Focus: favorable
Action: likely
Communication: mixed
Creation: favorable
Recovery: less favorable
Friction: elevated

CONVERGENCE
Jyotish: supports Focus / Action
Western: supports Creation
Maya traditional: supports declared day-theme translation
Dreamspell: neutral
Contradiction: Communication

TUNER
Energy: high
Direction: strong
Stability: medium
Intensity: high
Clarity: medium

BEST USE
focused execution / creation

WATCH
impulsive communication
```

Actual wording and probability bands must come from declared rules and validation, not this example.

---

## 15. Validation requirement

The domain must test three separate questions:

```text
A. Does the source system itself discriminate?
B. Does the capability translation improve practical usefulness without increasing false positives?
C. Does cross-system convergence outperform the strongest individual system on untouched/prospective data?
```

Only C can justify giving convergence extra authority.

Final rule:

> **Preserve full-resolution sources, compare them independently, split time at every real boundary, and compress only after the evidence has been kept intact.**

---

## 15. Delivery modes

Canonical presentation contract:
`DELIVERY.md`

The internal signal/output stack remains rich and inspectable.

User-facing delivery uses progressive disclosure:

~~~text
QUICK
→ headline + 3–5 windows + strongest call + status

STANDARD — default
→ headline + short timeline + 2–3 strongest calls + hit/miss + short why

AUDIT / DEEP
→ exact degrees, houses, rulers, stars, asteroids, rule IDs, dependencies, nulls, scoring
~~~

Default rule:

> **Do not expose the full reasoning graph when a smaller explanation preserves the forecast.**

## 16. Signal selection for presentation

Before user-facing delivery:
1. rank active signals by timing relevance, capture relevance, and independent contribution;
2. collapse duplicate/shared-dependency signals;
3. select only signals that materially change the prediction;
4. treat degree/star/minor-body layers as modifiers unless they change the outcome/window;
5. keep the complete internal record for audit.

STANDARD mode normally exposes:
- no more than 5 windows;
- no more than 3 primary predictions;
- no more than 2 technical drivers per prediction.

## 17. User-facing forecast object

Recommended compact object:

~~~text
OVERALL STORY:
WINDOWS[]:
  date
  prediction
  strength
PRIMARY CALLS[]:
HIT:
MISS:
WHY[]:
STATUS:
~~~

This is a presentation object only. It does not replace the frozen validation forecast record.


## 17A. Continuous horizon requirement

Atomic-window construction already partitions the full horizon.

User-facing compression must preserve that continuity.

For every interval, compute:
- active signals;
- dominant capability/story;
- signal density;
- conflict state;
- build/peak/separate/transition state where meaningful.

Do not discard intervals merely because no rule crosses a promotion threshold.

Instead emit:

~~~text
LOW-SIGNAL / BACKGROUND-DOMINANT
~~~

with the best-supported active background state.

The absence of a high-amplitude signal is itself part of the state.

Validation may separately designate matched control intervals, but delivery should not present those as empty gaps.
