# Stock Recognition → Price Response Bridge

Status: **RECOGNITION REPRESENTATION RETAINED / C1 BINARY ACTION MAPPING CLOSED**
Date: **2026-09-22**
Parent evidence:
- RC1 final aggregate audit (consumed holdout);
- Recognition V1 minimum-sample release audit, 25 fresh cases (consumed validation).

## Recognition V1 minimum-sample decision

Recognition V1 tested a shadow binary mapping:

```text
recognition assessment
        ↓
ACTIVE / CASH
```

Across 25 fresh cases, C1 did **not** beat either Quality-only or the preregistered simple-recognition baseline at the primary 60-session horizon.

Primary aggregate:
- Quality-only: +58.70%;
- B3 simple recognition: +58.16%;
- C1 binary Recognition: +58.03%.

C1 chose the numerically better action in 5 of 7 frozen action disagreements, but its two false exclusions (CAVA and CRSP) were larger than the combined capital benefit of its correct disagreements.

Release verdict:

> **FAIL / SIMPLIFY C1 BINARY ACTION MAPPING.**

This verdict closes the C1 ACTIVE/CASH capital-filter implementation. It does **not** reject Recognition as a state representation.

All 25 Recognition V1 cases are consumed evidence. They may train/generate hypotheses for a successor but may not validate it.

## Purpose

RC1 showed that Xyool can classify economic and causal state correctly while still making an inferior capital decision. The bridge therefore separates:

```
WHAT HAPPENED ECONOMICALLY
        ↓
WHAT INFORMATION THE MARKET RECEIVED
        ↓
HOW LIKELY THAT INFORMATION IS TO CAUSE MATERIAL REPRICING
        ↓
EXPECTED PAYOFF / DOWNSIDE
        ↓
CAPITAL PRIORITY
```

Economic state is an input to recognition, not an automatic veto.

## Authority

The Recognition Bridge sits after Quality and economic/causal state, and before capital priority.

Quality remains the normal-capital eligibility gate.

CE/CQ, contract decomposition, FES, breadcrumbs, causal timers and TTC remain evidence/state systems. None may directly force CASH merely because the state is weak, early, optioned, decelerating, or non-terminal.

Recognition estimates stock response. It must not rewrite the underlying economic state.

## Required recognition record

For each candidate event preserve:

- event identity and timestamp;
- Quality state;
- economic state / CE-CQ where applicable;
- causal frontier and unresolved dependencies;
- TTC distribution/window;
- surprise versus prior public expectation;
- company-relative scale;
- equity-denominator / repricing burden;
- uncertainty removed by the event;
- credibility / source strength;
- shareholder-capture friction;
- financing/dilution burden;
- prior recognition / priced-in state;
- same-company analogs;
- mechanism / peer analogs;
- market and sector context;
- attention/liquidity state where evidence exists;
- expected upside range if recognized;
- failure / contradiction / delay downside;
- recognition confidence.

Missing evidence remains UNKNOWN, not zero.

## Recognition hypotheses

The bridge may learn conditional relationships such as:

- weak committed economics can still reprice a stock when the headline is surprising, salient, strategically validating, or large relative to the equity denominator;
- economically strong events can fail to reprice when expected, already recognized, immaterial relative to company scale, or offset by capture/friction;
- a negative forward-state change is not automatically a negative price event if expectations were already lower or another uncertainty was removed;
- causal progress can matter before terminal economics when it changes the distribution of reachable downstream states.

These are hypotheses, not promoted coefficients.

## Output

The bridge produces ranges, not false precision:

```
P(material move | event, current state)
conditional upside range
conditional downside range
recognition confidence
recognition basis
key contradiction
expected-payoff range
```

A provisional transparent calculation is:

```
Recognition EV ≈
P(material upside recognition) × upside magnitude
- P(material adverse recognition) × downside magnitude
- delay/opportunity cost
```

Probabilities and magnitudes should be ranges when calibration is weak.

## Action firewall

Recognition remains **ANALYSIS_ONLY / SHADOW** until a successor earns fresh authority.

1. Recognition may not bypass Quality.
2. Recognition may not convert UNKNOWN evidence into negative evidence.
3. Recognition may not transfer numeric calibration across domains.
4. RC1 and Recognition V1 outcomes are consumed and cannot certify a successor.
5. The failed C1 ACTIVE/CASH mapping is closed and must not be used as a production or shadow default.
6. A Recognition state must not hard-zero an otherwise Quality-eligible opportunity merely because it appears expected, crowded, early, weakly committed, or technically extended unless a **separately preregistered exclusion rule** earns fresh capital evidence.
7. The default successor path is:
   ```text
   RECOGNITION STATE
          ↓
   CONDITIONAL PAYOFF DISTRIBUTION
          ↓
   CAPITAL PRIORITY / RANK
   ```
8. Any later conversion from payoff rank to position size is a separate experiment and authority decision.

## RLE learning job

Domain: `stock-market`
Job: `market-recognition`

Primary prediction targets:
- material positive move by horizon;
- material adverse move by horizon;
- close-to-close abnormal return where benchmark evidence is available;
- magnitude bucket / return distribution;
- profitable-exclusion error: production CASH while recognition challenger would be active and outcome is materially positive;
- false-positive error: recognition challenger active and outcome materially adverse.

Every resolved case must first receive a miss class:

```
DATA_MISS
FRESHNESS_MISS
STATE_MISS
QUESTION_MISS
DEPENDENCY_MISS
CALIBRATION_MISS
CORRESPONDENCE_MISS
EXECUTION_MISS
UNKNOWABLE
```

Only CALIBRATION_MISS can directly generate a bounded parameter challenger. Other miss classes generate the corresponding question/process/state/correspondence work.

## Training / validation firewall

RC1's 30 events are consumed evidence. They may:
- seed features;
- generate hypotheses;
- test code mechanics;
- train an initial challenger.

They may not:
- certify the successor;
- count as untouched holdout;
- support a release claim.

A successor release requires:
1. new method/version identity;
2. preregistered trial family;
3. frozen primary endpoint/horizon and comparator;
4. chronological untouched validation;
5. holdout-consumption record;
6. multiple-testing disclosure;
7. outlier and class/regime robustness;
8. shadow before authority increase.

## Correspondence / cross-dimensional representation

Recognition may use the seven cross-dimensional principles as structural search grammar without granting them trading authority.

Examples:
- Representation: market belief is not the economic event itself.
- Correspondence: analogous information structures may suggest target-domain questions.
- Dynamics: recognition depends on change/velocity, not only state.
- Polarity: support/contradiction and upside/downside are paired state spaces.
- Rhythm: attention, evidence and realization can unfold as sequence/cadence/regime.
- Causality: information must connect through a plausible repricing path.
- Generation/Selection: generate competing recognition explanations, then falsify/select.

The locally useful manifestation must be tested. Structural correspondence can transfer questions; calibration and actions remain local.

## Successor direction — C2 continuous payoff

The next method/version must not reuse C1's binary eligibility mapping.

C2 should forecast/rank the **distribution and magnitude** of post-event payoff using Recognition state as evidence.

Preferred shadow outputs:

```text
P(material upside | horizon)
P(material downside | horizon)
conditional upside magnitude / range
conditional downside magnitude / range
expected-return / payoff range
uncertainty / confidence
capital-priority rank
```

Primary design principle:

> **Classification accuracy is not the capital objective. Expected magnitude and opportunity cost matter.**

A candidate that correctly avoids several -5% to -10% outcomes but excludes a +30% to +50% winner can be inferior for compounded capital despite a high disagreement hit rate.

C2 should therefore be evaluated first as a **continuous forecast / ranking system**, not as a BUY/CASH rule.

Only after continuous prediction/ranking earns fresh out-of-sample value may Xyool preregister a bounded capital-scaling experiment.

## Success criterion

A Recognition successor earns additional authority only if fresh evidence shows incremental value versus Quality-only and preregistered simple recognition/payoff baselines, with:
- magnitude-aware scoring;
- ranking/order quality;
- material-up/down calibration;
- class/regime breadth;
- outlier robustness;
- opportunity-cost accounting;
- realistic costs where applicable.

The objective is not a more elegant score. The objective is better compounded-capital priority without recreating an over-selective veto layer.


## Recognition phase state

Fresh evidence from Recognition V1 Cohorts B-D supports separating price recognition into distinct phases rather than treating "TA confirmation" as one undifferentiated signal.

Shadow representation:

```text
PRE-EVENT RECOGNITION
        ↓
EVENT-DAY ABSORPTION
        ↓
POST-EVENT DIFFUSION
```

Required contextual dimensions:

```text
EVENT CLOCK:
SCHEDULED / UNSCHEDULED / UNKNOWN

SURPRISE STATE:
LOW / MODERATE / HIGH / UNKNOWN

PRE-EVENT RECOGNITION:
weak / mixed / strong / unknown

EVENT-DAY ABSORPTION:
material positive / material negative / non-material / unknown

POST-EVENT DIFFUSION:
material positive / material negative / non-material / unknown
```

Interpretation rule:

> The same technical state may mean different things at different points on the TTC/event clock.

Examples supported as hypotheses, not capital rules:

- strong pre-event momentum immediately before a highly anticipated scheduled event may represent recognition already consumed;
- strong pre-event momentum does not automatically imply "priced in" when a genuinely new unscheduled information shock arrives;
- a large event-day reaction may absorb much of the immediate repricing, but it does not by itself determine later continuation;
- short-horizon and medium-horizon technical states may conflict and must remain separate.

The implementation lives inside `agent/stock_recognition_learning.py` rather than a new module.

Authority: **SHADOW_ONLY**.

No Recognition Phase label may directly create BUY/CASH authority until fresh sequential validation demonstrates incremental value over simpler recognition and market-structure baselines.
