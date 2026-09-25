# Xyool — Cross-Domain Gauntlet Learning Loop

Status: **CANONICAL CORE SYSTEM-LEARNING ARCHITECTURE**

## Immutable doctrine

> **Cases are probes. Xyool is the object under test.**

> **Evidence/history is the memory. The current snapshot is Xyool's latest interpretation of that memory.**

> **A case-specific fix is not learning. A transferable rule that survives controls and later cases is learning.**

This doctrine applies to every Xyool domain unless a domain contract adds a stricter rule.

## Canonical loop

The Gauntlet now operates inside the evidence-directed RLE:

RESEARCH EXISTING METHODS / FAILURES
→ ASSESS EXISTING EVIDENCE
→ AUDIT XYOOL AGAINST THAT EVIDENCE
→ FORM COMPETING EXPLANATIONS
→ SELECT THE MOST-INFORMATIVE CASE / TEST
→ FREEZE CASE + METHOD + ENDPOINT
→ RUN CURRENT XYOOL / CHALLENGER
→ CLASSIFY WHAT WORKED / LOOKED WRONG / STAYED UNKNOWN
→ IF ANOMALOUS: RUN FAILURE DIAGNOSIS (`meta-failure-flow.md`)
→ CONFIRM / EXONERATE / LEAVE UNRESOLVED
→ ONLY CONFIRMED DEFECTS GENERATE REPAIR CANDIDATES
→ UPDATE THE EVIDENCE MAP
→ IDENTIFY THE MINIMUM GENERALIZABLE DEFECT OR PRINCIPLE
→ PLACE IT AT THE CORRECT LAYER
→ RUN POSITIVE + NEGATIVE + REGRESSION CONTROLS
→ PROMOTE / SIMPLIFY / KEEP PROVISIONAL / REJECT / RETIRE
→ PERSIST EVIDENCE + RULE + TEST
→ SELECT THE NEXT MOST-INFORMATIVE CASE

Broad/random batches remain useful for regression and coverage. They are no longer the default learning strategy when a smaller disagreement/anomaly cohort would be more informative.

The next case is automatically a regression test for prior learning.

## What counts as learning

A change qualifies as system learning only when it is:

1. **Generalizable** — not tied to the identity of the case.
2. **Causal or procedural** — it changes what Xyool asks, distinguishes, routes, stores, or updates.
3. **Prospectively available** — historical tests may use only information available at the decision time.
4. **Falsifiable** — negative controls exist.
5. **Layer-correct** — the owning module receives the fix.
6. **Persistent** — evidence, rule, and test are stored durably.
7. **Regression-tested** — later cases can prove whether it generalized.

Do not promote winner-specific patches, hindsight thresholds, or one-case exceptions.

## Three reusable layers

### 1. Domain-neutral gauntlet engine

Owns test-case selection, frozen-information discipline, miss classification, regression tracking, rule extraction, controls, promotion status, and system-learning reports.

### 2. Domain adapter / ontology

Defines what identity, evidence, state, gate, timer, consequence, capture, invalidation, and outcome mean in that domain.

Examples:
- stocks: contract → delivery → revenue → cash → shareholder capture;
- business operations: lead → evaluation → contract → implementation → usage → renewal;
- science: hypothesis → experiment → evidence → replication → mechanism → scale;
- cybersecurity: initial access → persistence → privilege → lateral movement → impact → remediation.

Source-domain learning generates hypotheses for another domain; it does not import calibration automatically.

### 3. Persistent evidence memory

Every domain should preserve:
- stable identity;
- append-only atomic evidence/history;
- dependency/state graph;
- timers;
- invalidations and supersessions;
- unresolved questions;
- outcomes;
- current derived snapshot.

Core invariant:

**APPEND-ONLY EVIDENCE / HISTORY = MEMORY**

**CURRENT SNAPSHOT = DERIVED INTERPRETATION**

If a snapshot cannot be defended or reconstructed from persisted evidence, the memory implementation is incomplete.

## Two separate pass/fail surfaces

### Architecture / representation

Can Xyool represent and persist the correct state once it is discovered?

### Automated intelligence

Can Xyool discover, classify, advance, recombine, and apply the state correctly without manual rescue?

A batch may pass architecture while failing automation. That must be reported honestly.

## Required gauntlet report

Every material batch should record:
- cases and system version;
- prior fixes under regression: held / failed / not exercised;
- new system defects and affected layer;
- generalizable rules proposed and governance status;
- positive and negative controls;
- architecture result;
- automation result and manual-rescue requirement;
- regressions;
- promotions, rejections, and unresolved system work.

A batch does not pass merely because finished case analyses were produced.

## Case-selection and batch-size rule

Increasing batch size is a stress test, not a goal.

When the objective is learning rather than coverage, prefer cases that:
- separate competing explanations;
- create genuine action/model disagreement;
- test a recurring expensive miss;
- exercise an evidence-weak regime;
- provide a clean negative control;
- challenge a canonical assumption.

The best next case is the one with the highest expected learning value, not necessarily the next ticker alphabetically or the largest batch.

Track reasoning quality, evidence granularity, stale-state rate, graph/timer integrity, unresolved-question quality, persistence integrity, regression rate, and manual-rescue rate.

Do not trade correctness for throughput.

## Failure-routing requirement

A failed-looking case is not automatically a system failure.

For every material anomaly:

```text
freeze information set
→ identify expected contract
→ compare expected vs observed
→ test knowability
→ locate first broken layer
→ classify CONFIRMED / EXONERATED / UNRESOLVED
```

Only a **CONFIRMED** defect may proceed to repair generation. An **EXONERATED** case remains useful evidence that the system behaved within its stated contract/uncertainty surface. When the first broken layer is upstream, downstream effects are not independently blamed without separate evidence.

Supporting doctrine:
- `meta-failure-flow.md`

## Relationship to Miss-to-Question

The Miss-to-Question loop remains canonical and is a specialized sub-loop of this architecture.

Gauntlet learning also converts successful recurring patterns, edge cases, source conflicts, stale states, regressions, automation failures, and cross-domain correspondence tests into governed learning.

## Cross-domain transfer rule

DOMAIN A CASES
→ DOMAIN A PATTERN
→ ABSTRACT CORE CANDIDATE
→ DOMAIN B INTERPRETATION
→ DOMAIN B POSITIVE/NEGATIVE TESTS
→ DOMAIN B STATUS

Correspondence is a hypothesis generator, not permission to import a rule untested.

## Promotion governance

Use:
- **CANONICAL CORE**
- **DOMAIN CANONICAL**
- **PROVISIONAL INPUT**
- **RESEARCH ONLY**
- **REJECTED**
- **SUPERSEDED**

## Frontier experimentation

When the normal Gauntlet repeatedly reaches the same performance ceiling or anomaly cluster, it may hand off to RLE Frontier Mode.

Frontier Gauntlets may test novel representations, unconventional methods, reversed assumptions, new feature interactions, or alternative horizons, but begin with RESEARCH_ONLY / SHADOW_ONLY authority.

The purpose is to prevent prior research and prior Xyool success from becoming a closed search space.

See `skills/xyool/00-06-EVIDENCE-DIRECTED-FRONTIER-RLE.md`.

## Success criterion

Xyool is improving when repeated basic misses disappear, prior fixes hold on new cases, newly found defects move to deeper reasoning layers, manual rescue declines, and uncertainty becomes explicit instead of being hidden by false precision.

Final rule:

> **Do not merely analyze more cases. Use cases to make the system that analyzes every future case better.**
