# Xyool Recursive Learning Architecture

Floware execution:
`floware/core/learning.flow.md`

The Flow is the reasoning authority. Existing RLE software is supporting deterministic machinery and must not become the default location for new learning logic.

Status: **BOUNDED RLE / LEVEL A IMPLEMENTATION + RLE 2.0 GOVERNANCE**

RLE 2.0 extension: `skills/xyool/00-06-EVIDENCE-DIRECTED-FRONTIER-RLE.md`
Goalpost/effectiveness governance: `skills/xyool/00-07-GOALPOST-EFFECTIVENESS-GOVERNANCE.md`

## Purpose

Xyool may improve from resolved outcomes, but learning authority is layered.

```text
XYOOL CORE
  -> DOMAIN LEARNING ADAPTER
  -> JOB-LOCAL LESSON / CHALLENGER
  -> DOMAIN-SPECIFIC EVALUATION
  -> OPTIONAL ABSTRACT INVARIANT
  -> CORRESPONDENCE HYPOTHESIS
  -> TARGET-DOMAIN TEST
  -> TARGET-DOMAIN AUTHORITY
```

A success in one domain or job is **not** copied into another domain or job.

The transfer rule is:

> Extract the invariant, map the structure, reset calibration, test locally.

## 1. What counts as recursive learning

For Xyool, bounded recursive learning is now governed by two nested loops.

The evidence-directed outer loop:

```text
research
-> existing evidence assessment
-> evidence map
-> audit
-> competing explanations
-> most-informative test
-> develop challenger only if needed
-> freeze / preregister
-> test
-> new evidence
-> belief update
-> validate / simplify / reject
-> authority
-> repeat
```

The prediction-resolution inner loop remains:

```text
prediction / decision
-> frozen provenance
-> later outcome
-> scoring
-> diagnosis / lesson
-> challenger generation
-> untouched temporal evaluation
-> bounded promotion recommendation
-> later outcome
-> repeat
```

When the evidence-directed loop plateaus or the representation repeatedly fails, Frontier Experimentation may generate novel hypotheses under lower authority. Frontier novelty never bypasses fresh validation.

Memory alone is not learning. A stored lesson must be able to produce a testable challenger and later evidence must be able to reject it.

## 2. Authority layers

### Core

The RLE core owns:
- prediction registration;
- provenance;
- outcome resolution;
- score/lesson/candidate records;
- append-only learning ledger;
- promotion modes;
- correspondence handoff.

The core does not own domain calibrations.

### Domain adapter

Each domain/job defines:
- target and outcome semantics;
- scoring;
- censoring/unknown handling;
- segmentation/regimes;
- lesson extraction;
- candidate generation;
- temporal evaluation;
- acceptable automatic-change class.

Example implemented now:

```text
stock-market / time-to-catalyst
-> TTCLearningAdapter
```

### Correspondence

Only an explicit `CORE_CANDIDATE` lesson with an abstract invariant may enter correspondence.

A correspondence begins as:

```text
HYPOTHESIS
authority = QUESTION_ONLY
```

It cannot gain domain-rule authority until target-domain evidence exists.

## 3. No blind transfer

Never automatically transfer:
- numeric thresholds;
- timing windows;
- probability bands;
- scoring weights;
- source-domain features;
- objectives;
- actions;
- actor semantics.

Required pattern:

```text
RETAIN STRUCTURE
RESET CALIBRATION
RE-ESTIMATE LOCALLY
```

A stock TTC correction of +18 days therefore remains a stock TTC correction.

A possible transferable invariant might instead be:

> Persistent non-occurrence after an evidence-backed expected transition window can become negative evidence.

Even that invariant does not become a target-domain rule automatically. It becomes a target-domain question and test.

## 4. Correspondence lifecycle

```text
SOURCE LESSON
-> verify source evidence/status
-> strip source nouns and calibration
-> abstract invariant
-> target structural mapping
-> important differences
-> explicit transfer/non-transfer boundary
-> falsifiable target test
-> negative controls
-> anti-lookahead freeze
-> HYPOTHESIS
-> target evidence
-> PROVISIONAL / SUPPORTED / REJECTED
```

Rejected mappings remain in the correspondence ledger so Xyool does not repeatedly relearn the same false analogy.

## 5. Prediction provenance

Every learnable prediction should freeze:
- domain;
- job;
- entity;
- prediction type;
- issue time;
- payload;
- evidence ids;
- producer/model/rule version;
- configuration hash;
- data snapshot hash;
- code ref when available;
- prompt ref when applicable.

An outcome may only be resolved later from explicit evidence.

## 5A. Dual-outcome event attribution

For event-driven domain experiments, a fixed-horizon outcome and a clean causal-attribution outcome must not be silently treated as the same object.

Stock-market Recognition implements:

```text
FROZEN ENTRY
    ↓
CAPITAL TRACK -> full preregistered horizon
    +
ATTRIBUTION TRACK -> last tradable state before next material event
```

If no competing material event arrives before the fixed horizon, the two tracks explicitly match. If one does arrive, the capital track continues while the attribution track stops before the new information state.

A competing-event record must identify the event and time. Missing attribution fails closed for experiments that declare the next-material-event protocol.

Canonical stock protocol:
`research/system-tests/stock-recognition-dual-outcome-attribution-protocol-2026-09-22.md`

This separation is part of outcome semantics and evaluator governance, not a stock-selection signal.

## 6. Candidate classes

Candidate kinds:

```text
PARAMETER
RULE
FEATURE
PROMPT_POLICY
MODEL
CODE
```

Promotion modes:

```text
HUMAN_REVIEW
SHADOW_ONLY
AUTOMATIC_BOUNDED
```

Hard rule:

> CODE, MODEL and PROMPT_POLICY candidates cannot receive automatic promotion authority from the generic RLE core.

A domain adapter may mark a bounded parameter/rule candidate as `AUTOMATIC_BOUNDED`, but the adapter must still prove it on untouched temporal evidence.

## 7. TTC MVP

The first implementation is `agent/stock_ttc_learning.py`.

It supports:
- point TTC error;
- signed error;
- absolute/squared error;
- interval coverage;
- horizon Brier score;
- horizon log loss;
- right-censor-aware horizon scoring;
- gate-type segmentation;
- frozen chronological train/holdout split;
- candidate point-offset correction;
- untouched holdout comparison;
- subperiod robustness check;
- practical-utility threshold;
- explicit local-only authority boundary.

The current candidate is intentionally simple. Simplicity makes the feedback loop auditable before more complex survival models are added.

## 8. Evidence-first and frontier boundaries

Before a new model/rule/feature is developed, the RLE should first distinguish:
- what external evidence already supports or contradicts it;
- what Xyool-local evidence exists;
- what remains unknown;
- whether the proposal duplicates an existing mechanism;
- what observation would falsify it.

Validated knowledge remains challengeable. Evidence is a prior, not a permanent law.

Frontier Mode may be triggered by persistent plateau, anomaly clusters, repeated unexplained misses, models agreeing while reality disagrees, suspected regime change, complexity rising without gain, or a representation limit.

Frontier outputs begin as RESEARCH_ONLY or SHADOW_ONLY.

See `00-06-EVIDENCE-DIRECTED-FRONTIER-RLE.md`.

## 9. Safety boundaries

The current RLE may:
- observe outcomes;
- score itself;
- write lessons;
- propose bounded challengers;
- evaluate challengers;
- recommend promotion;
- create correspondence hypotheses.

The current RLE may not:
- rewrite its evaluator;
- rewrite its safety rules;
- change its own permissions;
- silently alter production Python;
- modify protected holdout outcomes;
- import source calibration into another domain;
- bypass target-domain validation.

## 10. Next phases

### Phase 1 — current PR

- RLE core records
- append-only ledger
- correspondence transfer boundary
- TTC adapter
- train/holdout evaluation
- bounded promotion mode
- tests

### Phase 2

- ledger rehydration across process restarts
- durable candidate registry
- shadow/canary deployment state
- rollback state machine
- live outcome resolvers
- survival-analysis TTC model
- competing-risk catalyst types
- walk-forward evaluation
- multiple-testing controls

### Phase 3

- learning-method performance ledger
- meta-learning over challenger generators
- cross-job core-candidate extraction
- automated correspondence hypothesis generation
- target-domain experiment scheduling
- bidirectional abstraction refinement

## 11. Acceptance criterion

Xyool should only be called recursively learning when this can be demonstrated end-to-end:

```text
frozen prediction
-> independently resolved outcome
-> measurable miss
-> persisted lesson
-> challenger produced from pre-holdout data
-> later untouched evidence evaluates challenger
-> challenger can be rejected or promoted
-> promoted behavior changes later predictions
-> later outcomes re-enter the same loop
```

Cross-domain learning has an additional criterion:

```text
source success
!= target rule

source success
-> invariant
-> correspondence hypothesis
-> target-domain evidence
-> target-local rule/calibration
```

That distinction is permanent.
