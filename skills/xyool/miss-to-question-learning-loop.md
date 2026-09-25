# Xyool — Miss-to-Question Learning Loop

Status: **CANONICAL SYSTEM-IMPROVEMENT PRINCIPLE**

This loop begins **after** failure diagnosis has established a repair-worthy defect or a genuine missing question without hindsight.

Canonical prerequisite:
- `meta-failure-flow.md`

## Core principle

When Xyool materially misses an opportunity, risk, catalyst, timing relationship, or capital-allocation implication, do not patch the system around the specific winner or loser.

Ask instead:

> **What question, check, state field, or evidence requirement would have forced Xyool to notice the relevant information before the outcome was known?**

If that question is generalizable across companies and does not depend on hindsight, add it to the appropriate Xyool process and test it against both successes and failures.

Short form:

> **Convert misses into permanent questions, not case-specific rules.**

## Why this exists

A system can appear to improve while actually memorizing recent winners. The purpose of this loop is to extract the **general causal lesson** from a miss without embedding the identity of the company or the known outcome into future decisions.

The mistake this principle is designed to prevent is:

```text
MISS
→ discover winner afterward
→ invent winner-specific rule
→ historical fit improves
→ live generalization gets worse
```

The desired process is:

```text
APPARENT MISS
→ run failure diagnosis
→ CONFIRMED DEFECT / ESTABLISHED MISSING QUESTION
→ freeze/reconstruct pre-outcome information
→ assess existing external + Xyool evidence
→ audit the evidence → state → decision path
→ keep competing explanations alive
→ identify what next evidence would separate them
→ derive a missing question/state/process change only when supported
→ generalize it
→ test positive + negative cases
→ promote only if transferable
```

A miss is not proof that Xyool failed to ask a question. It may instead expose calibration error, regime change, representation failure, execution friction, noise, or genuinely unknowable uncertainty.

## Required post-miss procedure

For every material miss:

```text
0. RUN FAILURE DIAGNOSIS: expected contract → knowability → first broken layer → CONFIRMED / EXONERATED / UNRESOLVED
1. PROCEED ONLY IF A DEFECT / MISSING QUESTION IS ESTABLISHED; THEN FREEZE / RECONSTRUCT THE PRE-OUTCOME INFORMATION SET
2. IDENTIFY WHAT XYOOL KNEW
3. RESEARCH RELEVANT EXISTING METHODS / EVIDENCE
4. ASSESS SUPPORT, CONTRADICTION, REGIME SCOPE, AND UNKNOWN
5. AUDIT THE XYOOL EVIDENCE → STATE → DECISION PATH
6. ENUMERATE PLAUSIBLE COMPETING EXPLANATIONS
7. IDENTIFY THE MOST-INFORMATIVE DISCRIMINATING TEST
8. ONLY THEN FORMULATE A GENERALIZABLE QUESTION / CHECK IF WARRANTED
9. RUN POSITIVE + ADVERSARIAL / NEGATIVE CONTROLS
10. PROMOTE / SIMPLIFY / REJECT ONLY FROM FRESH VALIDATION
11. RECORD AUTHORITY, VALIDATION STATUS, AND WHAT WOULD INVALIDATE / DEMOTE IT
```

If failure diagnosis returns `EXONERATED`, do not create a repair merely to explain the outcome.

New principles/questions should follow `principle-question-documentation-standard.md`.

## What qualifies as a useful system question

A promoted question should:
- be answerable with information that can exist before the outcome;
- apply to more than one company or event type;
- expose a causal or economic state that matters to Quality or TTC;
- have a clear anti-false-positive condition;
- avoid embedding the identity of the eventual winner;
- improve research coverage, timing interpretation, risk detection, or capital comparison.

## Nameless example

A supplier receives one paid site deployment. Several months later the same customer orders another site using the same product and approval path.

The system correctly recognizes that adoption is repeating but fails to ask whether the spacing between the two sites creates a forward timing hypothesis.

Generalized question:

> **What repeats, and when could it repeat again?**

The lesson is not that another site must arrive on the same date interval. The lesson is that repeat deployments can create timing evidence that TTC should carry forward.

## Counterexample

Two unrelated companies each receive one order three months apart.

That does not establish a repeat cadence. A generalized timing question should require causal comparability, not mere date similarity.

## What not to do

Do not:
- add a rule merely because it would have selected the latest winner;
- optimize a threshold to one recent outcome;
- convert one interval into a guaranteed schedule;
- treat hindsight as evidence that the question was knowable prospectively;
- create duplicate scores when an existing module can absorb the lesson;
- weaken Quality simply because a low-quality stock later rallied;
- override fail-closed behavior to make a historical result look better.

## Principles discovered outside a miss

Not every useful principle originates from a failure.

When Xyool discovers a recurring causal relationship during successful analysis, historical testing, or live research, ask:

> **Is this relationship general enough that a future run should be required to consider it?**

If yes, document it with:
- explanation;
- nameless example where useful;
- authority boundary;
- counterexample / false-positive guard;
- validation status.

Therefore Xyool should accumulate principles **as they are discovered**, but only after generalization and governance.

The objective is a growing library of transferable reasoning, not a growing pile of observations.

## Governance

Every promoted post-miss question or discovered principle must be tagged as one of:
- **CANONICAL PROCESS** — permanently required;
- **PROVISIONAL INPUT** — useful hypothesis, calibration incomplete;
- **REJECTED** — created hindsight fit or false positives;
- **RESEARCH ONLY** — insufficient evidence for live use.

A new question does not automatically create independent capital authority. It feeds the existing Quality, OSE/FES, TTC, or Quant layer according to its job.

## Success criterion

The system is improving when repeated misses increasingly become one of two things:
1. genuinely unknowable outcomes that Xyool correctly treats as uncertainty; or
2. known pre-outcome evidence that an existing mandatory question captures and routes to the correct decision layer.

The objective is not to eliminate all misses. It is to eliminate **avoidable process misses** without overfitting the system to history.

## Relationship to the canonical gauntlet-learning loop

This module is a specialized sub-loop of `skills/xyool/gauntlet-learning-loop.md`.

Miss-to-Question governs material misses. Gauntlet Learning is broader: it also converts successful recurring patterns, edge cases, source conflicts, stale-state discoveries, regressions, automation failures, and cross-domain tests into governed, transferable system learning.

> **A case answer improves knowledge of the case. A validated transferable rule improves Xyool.**
