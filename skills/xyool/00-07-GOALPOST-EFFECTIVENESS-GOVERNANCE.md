# Xyool — Goalpost + Effectiveness Governance

Status: **CANONICAL / FAIL-CLOSED FOR MAJOR DEVELOPMENT PROGRAMS**
Date: **2026-09-22**

## Core doctrine

Xyool must know what it is trying to finish before it begins optimizing.

> **Freeze the goalpost before the work begins. Do not move it because the evidence is inconvenient, interesting, or points to another research question.**

A failed method does **not** move the goalpost.

```text
FROZEN GOAL
    ↓
METHOD / APPROACH
    ↓
TEST
    ↓
PASS ───────────────→ GOAL ACHIEVED
FAIL
    ↓
LEARN
    ↓
NEW METHOD
    ↓
SAME FROZEN GOAL
```

A new goal may be activated only after:
- the current goal is **ACHIEVED**; or
- the goal itself is formally **INVALIDATED** by evidence showing that the objective is incoherent, impossible, unsafe, obsolete, or no longer relevant.

Method failure is not goal invalidation.

---

## 1. Mandatory goalpost contract

Every major development program must freeze:

```text
GOAL
What exact capability are we trying to finish?

SUCCESS GATES
What evidence is sufficient to call the capability effective?

FAILURE GATES
What evidence means the current method/approach should be rejected or simplified?

BOUNDARIES
What are we explicitly not trying to solve during this goal?

EFFECTIVENESS STANDARD
What is useful/reliable enough to matter in practice?

EFFICIENCY STANDARD
What research, computation, process, and maintenance burden is reasonable?

COMPLEXITY BUDGET
How much complexity may be added before it must prove incremental value?
```

The goalpost is frozen before optimization begins.

Side discoveries enter the backlog unless they materially affect the path to the current goal.

---

## 2. Effectiveness, not perfection

Xyool is not designed to maximize theoretical perfection.

The standard is:

> **Effective within reason, supported by evidence, robust enough for the decision, and no more complex than the evidence justifies.**

Perfection is usually a bad optimization target because it can produce:
- endless research loops;
- overfitting;
- fragile rules;
- excessive latency;
- excessive data requirements;
- unnecessary architecture;
- diminishing returns;
- systems that are harder to audit than the value they add.

A system may be finished enough when:
- it clears the frozen success gates;
- remaining error is acceptable relative to the decision;
- further complexity has weak expected incremental value;
- the simpler architecture is more robust, auditable, maintainable, or efficient.

"Good enough" does not mean arbitrary or careless.

It means the stopping rule is tied to **decision effectiveness**, not an impossible zero-error objective.

---

## 3. Evidence-based streamlining

Optimization includes removal.

For every component ask:

1. Does it measurably improve the target?
2. Does it reduce an important failure mode?
3. Does it improve robustness?
4. Does it improve speed, coverage, auditability, or maintainability?
5. Does another component already capture the same latent phenomenon?
6. What happens if it is removed?

Preferred direction:

```text
MORE EFFECTIVE
+ MORE ROBUST
+ LESS DUPLICATION
+ LOWER LATENCY
+ LOWER RESEARCH BURDEN
+ LOWER MAINTENANCE BURDEN
+ CLEARER AUTHORITY
= BETTER ARCHITECTURE
```

Complexity is not evidence of intelligence.

A more complicated architecture must earn its complexity.

---

## 4. Complexity tax

Every new:
- feature family;
- score;
- model layer;
- rule;
- exception;
- domain mapping;
- data dependency;
- research requirement

creates cost.

Costs include:
- implementation;
- runtime;
- research time;
- data freshness;
- failure surface;
- calibration;
- audit burden;
- interaction effects;
- future maintenance;
- risk of hindsight fit.

Therefore:

> **If a simpler architecture performs similarly within the frozen effectiveness standard, prefer the simpler architecture.**

A feature that adds no repeatable information should be removed, demoted, or retained only as descriptive context.

---

## 5. Efficiency is part of correctness

Xyool should not repeatedly perform expensive work when existing evidence is sufficient.

Evidence-based efficiency includes:
- reusing fresh persistent state;
- using consumed development pools before spending holdouts;
- selecting the most discriminating test instead of the largest test;
- stopping an experiment family when its frozen failure condition is met;
- avoiding duplicate signal families;
- caching provenance-preserving evidence;
- testing cheap/simple models before complex ones;
- using regression suites instead of rediscovering old failures;
- researching externally only when the existing library cannot answer the question.

Efficiency may never bypass a mandatory evidence or safety gate.

The objective is:

> **Minimum justified work for sufficient decision quality.**

Not:
> minimum work regardless of quality.

And not:
> maximum work regardless of incremental value.

---

## 5A. Discovery is cheaper than validation

Do not require release-grade proof to discover a useful answer.

Default escalation:

```text
DIRECT ANSWER
→ CHEAP CONTRADICTION
→ CONSUMED REGRESSION
→ TARGETED TOURNAMENT
→ UNTOUCHED VALIDATION
```

Use the lowest level that is sufficient for the authority of the conclusion.

A tournament is justified only when simpler evidence cannot answer the question or when a broader authority gate requires it.

Canonical Flow:
`floware/core/direct-resolution.flow.md`

## 6. Goalpost movement rule

A goalpost may close as:

### ACHIEVED
The frozen success gates are satisfied with the required evidence.

A successor goal may then be opened.

### INVALIDATED
Evidence shows the goal itself should no longer exist in its frozen form.

Invalidation requires:
- explicit rationale;
- evidence references;
- explanation of why changing the method is insufficient.

### METHOD FAILURE
This does **not** close the goalpost.

It records:

```text
CURRENT METHOD FAILED
→ preserve failure
→ diagnose
→ simplify / redesign
→ same goal
```

Do not relabel a failed method as a new objective.

---

## 7. Side-discovery rule

A useful discovery may:
- improve the evaluator;
- improve the method;
- reveal a missing state;
- change the experiment design;
- create a future research question.

It may not silently replace the frozen goal.

Classify side discoveries:

```text
CURRENT-GOAL RELEVANT
→ integrate if evidence supports it

BACKLOG
→ preserve for later

GOAL INVALIDATION CANDIDATE
→ requires formal evidence review
```

This prevents recursive learning from becoming recursive wandering.

---

## 8. Optimization order

When improving a system, prefer:

```text
1. REMOVE ERROR / OMISSION
2. REMOVE DUPLICATION
3. SIMPLIFY REPRESENTATION
4. IMPROVE EVIDENCE QUALITY
5. IMPROVE TARGET / EVALUATOR
6. IMPROVE CALIBRATION
7. IMPROVE EFFICIENCY
8. ADD COMPLEXITY ONLY IF NEEDED
```

Do not add a new layer before asking whether the current architecture is solving the wrong target or duplicating information.

---

## 9. Recursive-learning integration

Canonical RLE loop becomes:

```text
FREEZE GOALPOST
    ↓
ASSESS EXISTING EVIDENCE
    ↓
AUDIT CURRENT ARCHITECTURE
    ↓
SELECT MOST-INFORMATIVE IMPROVEMENT
    ↓
TEST
    ↓
EFFECTIVE?
  ↙       ↘
NO         YES
↓           ↓
METHOD      CHECK SUCCESS GATES
FAILURE     ↓
↓         NOT YET → SAME GOAL
REDESIGN    ↓
↓         ACHIEVED
SAME GOAL   ↓
          CLOSE GOALPOST
            ↓
          SET NEXT GOAL
```

The RLE implementation stores:
- `GoalpostRecord`;
- `GoalpostAttemptFailureRecord`;
- `GoalpostResolutionRecord`.

A second active goalpost for the same domain/job is rejected while the first remains unresolved.

---

## 10. Relationship to correspondence

Correspondence can suggest a method for the current goal.

It cannot redefine the goal automatically.

A cross-domain mapping should ask:

> **Can this structure help clear the current frozen success gate more effectively or efficiently?**

If not, preserve it as a separate hypothesis/backlog item.

---

## 11. Finish criteria

"Finished" means:
- frozen success gates cleared;
- failure conditions addressed;
- evidence sufficient for the intended authority;
- regressions acceptable;
- complexity justified;
- additional work has low expected incremental value relative to its cost.

It does **not** mean:
- zero errors;
- every edge case solved;
- every interesting hypothesis tested;
- maximum model complexity;
- no future learning.

A finished architecture can continue learning without reopening its completed goal unless evidence later invalidates the assumptions under which it was finished.

---

## 12. Core laws

> **Do not move the goalpost to escape a failed method.**

> **Do not pursue perfection when evidence shows sufficient effectiveness has been reached.**

> **Optimization means improving useful output per unit of complexity, research, computation, and maintenance.**

> **Every added layer must earn its existence.**

> **Finish the current capability before promoting the next objective.**
