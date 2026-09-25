# FLOW — Direct Resolution

FLOW ID: `CORE-DIRECT-RESOLUTION`  
STATUS: **ACTIVE / CANONICAL**  
DOMAIN: core  
JOB: find the simplest workable answer before escalating to experiments

## GOAL

Resolve questions with the minimum justified reasoning and evidence burden.

Core law:

> **Do not run a tournament to discover an answer that is already visible.**

Separate:

```text
DISCOVERY
What is probably the answer?

from

VALIDATION
How much proof is required before this answer receives authority?
```

## PROCESS

```text
QUESTION
  ↓
DIRECT SYNTHESIS FROM EXISTING STATE
  ↓
SIMPLEST PLAUSIBLE ANSWER
  ↓
CHEAPEST MATERIAL CONTRADICTION CHECK
  ↓
SURVIVES?
  ├─ NO → QUESTION FRONTIER / ALTERNATIVE ANSWER
  └─ YES
       ↓
IS MORE PROOF REQUIRED FOR THE DECISION?
  ├─ NO → WORKABLE RESULT
  └─ YES → ESCALATE ONE LEVEL ONLY
```

## 1. OBVIOUSNESS PASS

Before designing an experiment, ask:
- Is the answer already explicit in the evidence?
- Is one relationship dominating the cases?
- Are we overcomplicating something that can be stated directly?
- Does the answer follow from a known constraint or definition?
- Are we trying to estimate something whose sign/structure is already obvious?
- Is the remaining uncertainty material to the decision?

If the answer is directly supported, state it.

Do not manufacture uncertainty merely because more testing is possible.

## 2. SIMPLEST PLAUSIBLE ANSWER

Prefer one concise causal/structural explanation.

Examples:

```text
The 60-day miss exists because another material event entered the path.

The report was strong, but the new forward guide reset the growth rate.

The question is asking one score to solve two different jobs.

The next event is already known and dominates this horizon.
```

Do not immediately decompose into ten hypotheses unless the simple answer fails.

## 3. CHEAP CONTRADICTION CHECK

Try to break the answer using the smallest high-information check.

Preferred order:
1. strongest known counterexample;
2. one matched contrast;
3. one hard regression case;
4. existing consumed evidence;
5. only then a new targeted test.

If one counterexample destroys the rule, stop.

If the answer survives, do not automatically expand to a large cohort.

## 4. RESOLUTION LADDER

Use the lowest sufficient level.

### LEVEL 0 — DIRECT
Existing evidence/logic gives a clear answer.

No experiment.

### LEVEL 1 — THIN-SLICE
Check 1–3 high-information cases or contradictions.

Purpose:
- catch obvious failure;
- distinguish two explanations.

### LEVEL 2 — CONSUMED REGRESSION
Run the answer across the relevant existing consumed/hard-case set.

Purpose:
- test whether the local answer survives known failure modes.

### LEVEL 3 — TARGETED COHORT / TOURNAMENT
Use only when:
- important competing explanations remain;
- the claim is intended to generalize;
- the architecture change has broad consequences;
- cheaper levels cannot discriminate.

### LEVEL 4 — UNTOUCHED VALIDATION
Use only when frozen authority/release gates require it.

Do not jump from a question directly to Level 3 or Level 4.

## 5. AUTHORITY MATCHING

The amount of proof should match the authority of the conclusion.

```text
LOCAL WORKING ANSWER
→ direct/thin-slice may be sufficient

DEVELOPMENT ARCHITECTURE CHANGE
→ consumed regression may be sufficient

GENERAL RULE
→ broader discriminating evidence required

PRODUCTION / RELEASE AUTHORITY
→ frozen validation required
```

A provisional answer can be useful before it is validated.

Label its authority correctly instead of withholding it until a tournament finishes.

## 6. ESCALATION RULE

Escalate only when at least one is true:
- a material counterexample survives;
- competing explanations remain decision-relevant;
- the answer changes broad architecture;
- a goalpost gate requires broader evidence;
- consequence of being wrong justifies more work;
- existing evidence cannot resolve the question.

Otherwise stop.

## 7. TOURNAMENT RULE

A tournament is not the default research unit.

Use a tournament only when its comparative structure adds information unavailable from a simpler check.

Bad pattern:

```text
QUESTION
→ BUILD COHORT
→ FREEZE
→ RUN
→ AUDIT
→ NEW QUESTION
→ BUILD ANOTHER COHORT
```

Preferred:

```text
QUESTION
→ DIRECT ANSWER
→ TRY TO BREAK IT CHEAPLY
→ USE IT IF WORKABLE
→ TOURNAMENT ONLY IF NECESSARY
```

## 8. RELATION TO QUESTION FRONTIER

Direct Resolution comes before repeated question search.

If the direct answer is weak or contradictory:
`question-frontier.flow.md`

The Question Frontier changes the question.

Direct Resolution changes the amount of proof.

Together:

```text
CAN WE ANSWER THIS SIMPLY?
  ↓
YES → MINIMUM PROOF
NO  → BETTER QUESTION
```

## 9. BOTTLENECK

If the answer remains unresolved after the minimum useful escalation, return the actual bottleneck.

Do not compensate for a bottleneck with more loops.

## 10. SOFTWARE / HARD-LIMIT BOUNDARY

`NONE — FLOWARE SUFFICIENT`

## CORE STATEMENTS

> **Find the answer first. Prove it only as much as the decision requires.**

> **One strong counterexample can be more useful than fifty routine cases.**

> **Minimum justified proof is better than maximum available proof.**