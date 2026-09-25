# Xyool — Meta Failure Flow

Status: **CANONICAL CORE / DOMAIN-AGNOSTIC META FLOW**

## Purpose

Xyool needs one common way to determine whether an apparent miss is actually a system failure, locate the first broken layer, prevent downstream blame from being assigned incorrectly, and route a validated defect into governed learning.

Core rule:

> **A failure is a measurable violation of a previously defined expectation, requirement, state transition, or process contract that was reasonably knowable/testable at the time. An undesirable outcome by itself is not a system failure.**

This flow sits above domain-specific implementations. Domains define their own contracts, evidence, states, actions, calibrations, and consequence measures. The meta layer defines how suspected failures are evaluated and routed.

---

## 1. Canonical meta failure flow

```text
OBSERVED DIVERGENCE / MISS / BAD OUTCOME / PROCESS ANOMALY
        ↓
FREEZE THE RELEVANT INFORMATION SET
        ↓
IDENTIFY THE EXPECTED CONTRACT
        ↓
COMPARE EXPECTED vs OBSERVED
        ↓
IS THERE A MATERIAL DIVERGENCE?
        ├─ NO  → EXONERATED / NORMAL VARIATION / NO FAILURE
        └─ YES
             ↓
WAS THE RELEVANT INFORMATION OR REQUIREMENT KNOWABLE/TESTABLE THEN?
        ├─ NO  → EXTERNAL SURPRISE / UNRESOLVED UNCERTAINTY
        └─ YES / PARTIAL
             ↓
TRACE THE PIPELINE UPSTREAM → DOWNSTREAM
             ↓
LOCATE THE FIRST BROKEN LAYER
             ↓
CLASSIFY FAILURE + PROPAGATION
             ↓
ASSESS PREVENTABILITY + CONSEQUENCE
             ↓
FORMULATE MINIMUM REPAIR CANDIDATE
             ↓
POSITIVE + NEGATIVE + REGRESSION CONTROLS
             ↓
PROMOTE / KEEP PROVISIONAL / REJECT
             ↓
PERSIST FAILURE + REPAIR + TEST RESULT
```

Do not begin by designing a fix. First determine whether a failure actually occurred and where.

---

## 2. Contract principle

Every material Xyool layer should expose a testable contract.

Examples:

```text
SOURCE / DISCOVERY CONTRACT
Did the system acquire evidence it was required and able to acquire?

INGESTION / EXTRACTION CONTRACT
Did the system represent what the source actually said?

VERIFICATION CONTRACT
Did it verify identity, source authority, conditions and superseding evidence?

STATE CONTRACT
Did it map verified evidence to the correct state and dependency structure?

TIMING / PROBABILITY CONTRACT
Were uncertainty and timing represented/calibrated appropriately?

ECONOMIC / CONSEQUENCE CONTRACT
Did it model who captures the consequence and how large/material it is?

RECOGNITION / RESPONSE CONTRACT
Did it distinguish underlying consequence from observer/market response?

DECISION CONTRACT
Did the decision layer follow its stated objective and authority rules?

EXECUTION CONTRACT
Was the approved decision implemented within the required constraints?

MEMORY / STATE-PERSISTENCE CONTRACT
Was prior evidence/learning retained, retrievable, current and applied?

PROCESS CONTRACT
Were mandatory steps completed, blocked explicitly, or marked N/A?

RESEARCH-LEARNING CONTRACT
Was a repair tested without hindsight leakage before promotion?
```

A domain may add stricter or additional contracts.

---

## 3. First-broken-layer rule

Failure attribution belongs to the **earliest material layer whose contract was violated**.

Example:

```text
PUBLIC EVENT EXISTS
→ DISCOVERY MISSES IT
→ INGESTION NEVER RECEIVES IT
→ STATE REMAINS STALE
→ DECISION IS WRONG
```

Canonical attribution:

```text
FIRST BROKEN LAYER = DISCOVERY
DOWNSTREAM STATE / DECISION = PROPAGATED EFFECT
```

Do not blame downstream modules for evidence they never received.

If discovery succeeded but extraction dropped the decisive condition, the first broken layer is extraction, not discovery.

---

## 4. Knowability gate

Before confirming a failure, ask:

> **Could Xyool, using information reasonably available at that time and following its own frozen process/contract, have done materially better?**

Allowed values:

```text
YES
PARTIAL
NO
UNKNOWN
```

Interpretation:

- **YES** — a system/process failure may be confirmed.
- **PARTIAL** — classify the knowable portion and preserve residual uncertainty.
- **NO** — do not manufacture a repair from hindsight; treat as external surprise or ordinary uncertainty.
- **UNKNOWN** — keep the case unresolved until the information set can be reconstructed.

Anti-lookahead applies to failure diagnosis.

---

## 5. Bad outcome is not automatically failure

Probabilistic systems must allow adverse outcomes.

Example:

```text
Prediction: 55% favorable outcome
Observed: unfavorable outcome
```

This single case does not prove model failure.

Evaluate calibration over an appropriate set of comparable predictions.

Conversely:

```text
Contract: check required direct sources before asserting "nothing new"
Observed: a required source contained a material item but was not checked
```

This can be a process failure even before any downstream economic outcome is known.

---

## 6. Core failure families

Use the narrowest applicable family; domains may extend them.

```text
DISCOVERY
INGESTION / EXTRACTION
VERIFICATION
IDENTITY
STATE / REPRESENTATION
DEPENDENCY / CAUSAL MODEL
TIMING / PROBABILITY / CALIBRATION
CONSEQUENCE / ECONOMIC MODEL
RECOGNITION / RESPONSE MODEL
DECISION / AUTHORITY
EXECUTION
MEMORY / RETRIEVAL / STALENESS
PROCESS OMISSION
RESEARCH / LEARNING / PROMOTION
CORRESPONDENCE / TRANSFER
INFRASTRUCTURE / TOOLING
```

A failure may propagate across several layers, but record one primary first-broken layer unless independent failures are demonstrated.

---

## 7. Failure object

Minimum canonical object:

```text
failure_id
domain
entity_or_case_id
observed_at

trigger
expected_contract
expected_state_or_requirement
expected_window_or_boundary

observed_state
divergence

frozen_information_set
knowability: YES / PARTIAL / NO / UNKNOWN

first_broken_layer
failure_family
failure_subclass

severity
consequence
propagated_effects

preventable: YES / NO / UNKNOWN
root_cause

repair_candidate
validation_required
linked_tests
linked_evidence

status:
  SUSPECTED
  CONFIRMED
  EXONERATED
  REPAIR_TESTING
  CLOSED
```

**EXONERATED is mandatory as a possible terminal diagnosis.**

A suspected failure must not be silently converted into a confirmed failure merely because a bad outcome occurred.

---

## 8. Failure vs uncertainty vs invalidation

Keep these separate.

```text
FAILURE
A Xyool contract/process/model was violated.

UNCERTAINTY
The evidence legitimately did not determine the outcome.

INVALIDATION
New evidence changed or killed the underlying state/thesis.

EXTERNAL SURPRISE
A material event was not reasonably knowable under the frozen information set.

NORMAL VARIATION
Observed result falls within the stated uncertainty/error surface.
```

An invalidated thesis can be correctly handled and therefore not be a system failure.

---

## 9. Severity and consequence

Severity must be based on impact, not embarrassment.

At minimum consider:

```text
information consequence
state consequence
decision consequence
economic / domain consequence
repeatability
scope of affected objects
silent-propagation risk
detectability
```

Exact numeric severity scales are domain/local calibration unless separately standardized.

---

## 10. Repair discipline

Confirmed failure does not authorize immediate canonical change.

```text
CONFIRMED FAILURE
→ identify minimum generalizable defect
→ propose minimum repair
→ test original case as a regression case
→ run positive controls
→ run negative controls
→ run fresh / untouched cases where material
→ inspect new failure modes introduced by repair
→ promote / provisional / reject
```

A repair that merely explains the latest winner/loser is not learning.

A process safeguard that prevents an objectively skipped mandatory step may be promoted under the applicable governance rule without claiming alpha or predictive superiority.

---

## 11. Relationship to gauntlet learning

The Meta Failure Flow is a required sub-flow inside the canonical gauntlet loop whenever a case is classified as failed or anomalous.

```text
CASE
→ RUN XYOOL
→ AUDIT
→ SUSPECTED FAILURE?
      ├─ NO → success / unknown analysis
      └─ YES
           ↓
      META FAILURE FLOW
           ↓
      CONFIRMED / EXONERATED / UNRESOLVED
           ↓
      only CONFIRMED defects may generate repair candidates
           ↓
      controls + promotion governance
```

This prevents gauntlet learning from overfitting normal randomness.

---

## 12. Relationship to correspondence

Failure diagnosis is core; failure contracts are domain-specific.

When a correspondence fails, distinguish:

```text
SOURCE PRINCIPLE FAILURE
ABSTRACTION FAILURE
TARGET MAPPING FAILURE
TARGET CALIBRATION FAILURE
TARGET IMPLEMENTATION FAILURE
```

Do not conclude that a source-domain principle is false merely because one target-domain mapping was poor.

---

## 13. Relationship to memory

Persist:

- the frozen information set or references sufficient to reconstruct it;
- expected contract;
- observed divergence;
- first broken layer;
- diagnosis status;
- repair/test lineage;
- final disposition.

The current snapshot may summarize open failures, but historical failure records must not be silently rewritten.

---

## 14. VWAV discovery miss as reference pattern

Reference pattern only; not a stock-specific core rule:

```text
public material event
→ initial current-news result omitted event
→ event was reasonably knowable from a required direct source
→ downstream analysis never received event

first broken layer:
DISCOVERY

propagation:
stale event state / incomplete answer

repair candidate:
direct-source fan-out + freshness/negative-evidence barrier

repair status:
must be validated as a general discovery/process improvement
```

The transferable lesson is not "check VWAV harder."

It is:

> **Before a negative-currentness assertion is promoted to verified, the applicable discovery contract must be satisfied.**

---

## 15. Core invariants

1. **Bad outcome ≠ failure.**
2. **Failure requires a violated contract or materially miscalibrated model.**
3. **Freeze the information set before diagnosis.**
4. **Check knowability before assigning blame.**
5. **Attribute to the first broken layer.**
6. **Separate primary failure from propagated effects.**
7. **Allow exoneration.**
8. **Do not repair before diagnosis.**
9. **Do not promote a repair without controls.**
10. **Persist failures and failed repairs as learning evidence.**

Final rule:

> **Xyool should learn from genuine defects without training itself on randomness, hindsight, or downstream symptoms.**
