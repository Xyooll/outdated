# FLOW — Question Frontier

FLOW ID: `CORE-QUESTION-FRONTIER`  
STATUS: **ACTIVE / CANONICAL**  
DOMAIN: core  
JOB: improve questions until they become decision-useful or reach a real bottleneck

## GOAL

Prevent Xyool from looping on weak questions.

Core law:

> **A bad answer may be evidence that the question is wrong. Improve the question before adding complexity to the answer.**

## TRIGGER

Run this Flow when:
- an answer is vague, unstable, trivial, contradictory, or non-actionable;
- a test fails to discriminate competing explanations;
- repeated model changes do not improve the result;
- the same problem keeps returning under different implementations;
- the current question is too broad to produce a useful state.

## PROCESS

Before entering a question loop, run:
`direct-resolution.flow.md`

```text
QUESTION
  ↓
DIRECT RESOLUTION
  ↓
WORKABLE?
  ├─ YES → STOP / CONTINUE MAIN FLOW
  └─ NO
       ↓
DIAGNOSE WHY THE QUESTION FAILED
       ↓
GENERATE A MATERIALLY BETTER QUESTION
       ↓
DIRECT RESOLUTION AGAIN
       ↓
REPEAT ONLY IF INFORMATION CHANGES
       ↓
STOP AT WORKABLE RESULT OR REAL BOTTLENECK
```

The Question Frontier is not permission to generate many questions by default.

It exists only after the simple/direct answer path has failed.

## 1. QUESTION-FAILURE DIAGNOSIS

Classify the failure before asking another question.

### TOO BROAD
The question combines multiple jobs.

Example:
`What will this stock do?`

Better:
`What material information states can alter shareholder payoff inside the next 60 sessions?`

### WRONG TARGET
The question measures something adjacent to the actual goal.

Example:
`Was the catalyst good?`

when the goal is:
`Which opportunity should receive capital?`

### WRONG TIME SCALE
The question asks an event-local question for a capital-path outcome, or vice versa.

### WRONG UNIT
The question asks about a stock when the relevant object is:
- event;
- causal process;
- future node;
- shareholder capture;
- capital path;
- dependency.

### NON-DISCRIMINATING
Multiple competing explanations give the same answer.

### UNOBSERVABLE
The answer depends on information unavailable at the decision time.

### UNDER-SPECIFIED
Important variables/constraints are missing.

### OVER-SPECIFIED
The question contains assumptions that force the answer.

### EVIDENCE-STARVED
The question is valid, but the required evidence does not exist or is inaccessible.

### IRREDUCIBLY UNCERTAIN
The remaining uncertainty cannot be reduced enough to improve the decision.

## 2. QUESTION GENERATION

Generate several alternative questions from different structural angles.

Useful transforms:

```text
BROAD → NARROW
OBJECT → PROCESS
STATE → TRANSITION
EVENT → CAPITAL PATH
FEATURE → RELATIONSHIP
OUTCOME → CAUSAL MECHANISM
AVERAGE → CONDITIONAL
STATIC → TIME-AWARE
SINGLE FACTOR → COMPETING EXPLANATIONS
PREDICT → DISCRIMINATE
```

Example:

```text
Weak question:
"Is Recognition good or bad?"

Better questions:
- Recognition of what?
- At what point in the causal clock?
- Relative to what new economic information?
- Does Recognition change direction by path regime?
- Is Recognition measuring consumed payoff or informed confirmation?
- Which cases discriminate those explanations?
```

## 3. QUESTION SELECTION

Do not ask every possible question.

Prefer the question with the highest expected information value.

A strong next question should:

1. distinguish live competing explanations;
2. be answerable with available evidence;
3. materially affect the current decision or architecture;
4. require the least justified work;
5. avoid consuming fresh evidence unnecessarily;
6. avoid adding complexity before the question is resolved.

## 3A. QUESTION COUNT DISCIPLINE

Default to **one best next question**, not a tournament of questions.

Generate several internally only when needed to choose the highest-information one.

Do not execute them all merely because they are available.

A question sequence should be:

```text
BEST CURRENT QUESTION
→ DIRECT ANSWER
→ ONE MATERIAL CONTRADICTION
→ NEXT QUESTION ONLY IF NEEDED
```

not:

```text
QUESTION 1
QUESTION 2
QUESTION 3
QUESTION 4
...
run all
```

## 4. RESULT TEST

A question has produced a **WORKABLE RESULT** when its answer:

- changes a decision, state, or architecture;
- eliminates at least one important competing explanation;
- reduces uncertainty materially;
- identifies a clear next action;
- or establishes that no further action is justified.

A result can be workable even if the answer is:

`UNKNOWN`

when UNKNOWN correctly identifies the decision boundary.

## 5. BOTTLENECKS

Stop reformulating when the frontier reaches a real bottleneck.

Allowed bottlenecks:

```text
EVIDENCE BOTTLENECK
REPRESENTATION BOTTLENECK
MEASUREMENT BOTTLENECK
TIME / LATENCY BOTTLENECK
DOMAIN-KNOWLEDGE BOTTLENECK
HARD CONSTRAINT
IRREDUCIBLE UNCERTAINTY
DIMINISHING INFORMATION VALUE
```

At a bottleneck, output:

```text
BOTTLENECK TYPE:
WHAT IS KNOWN:
WHAT REMAINS UNKNOWN:
WHY BETTER WORDING CANNOT RESOLVE IT:
WHAT NEW EVIDENCE / CAPABILITY WOULD RESOLVE IT:
WHETHER CURRENT DECISION CAN PROCEED ANYWAY:
```

Do not continue generating synonymous questions after a true bottleneck is identified.

## 6. LOOP PREVENTION

A new question must materially differ from the failed one.

Do not allow:

```text
same question
→ different wording
→ same evidence
→ same ambiguity
→ repeat
```

Require at least one meaningful change in:
- target;
- unit;
- time horizon;
- causal boundary;
- comparison set;
- evidence type;
- competing hypothesis;
- decision criterion.

## 7. QUESTION MEMORY

Preserve materially useful questions, especially:

- questions that repeatedly unlock a domain;
- questions that expose a common failure mode;
- questions that replace a bad default question;
- bottleneck-defining questions.

These can become reusable Flow components.

## 8. RELATION TO GOALPOSTS

Question search may change the method.

It may not move the frozen goalpost.

```text
SAME GOAL
→ BETTER QUESTION
→ BETTER STATE
→ BETTER METHOD
```

not:

```text
QUESTION FAILED
→ NEW GOAL
```

## 9. SOFTWARE / HARD-LIMIT BOUNDARY

`NONE — FLOWARE SUFFICIENT`

## CORE STATEMENT

> **Do not keep answering a bad question better. Ask a better question.**

> **Keep improving the question until it yields a workable result or exposes the real bottleneck.**
