# FLOW — Recursive Learning

FLOW ID: `CORE-LEARNING`  
STATUS: **ACTIVE / CANONICAL**  
DOMAIN: core  
JOB: bounded recursive system learning  
AUTHORITY: lesson/candidate generation and learning-state update only; no self-promotion, patch completion, or external/action authority  
PARENT GOALPOST: supplied by the active learning/development objective  
UPSTREAM FLOWS: resolved outcomes, Meta Failure, domain/core owning Flows  
DOWNSTREAM FLOWS: Direct Resolution, Question Frontier, Development, Correspondence, Pipeline Integrity  
INBOUND PIPES: `../meta/PLUMBING.md#pipe-meta-failure-learning`  
OUTBOUND PIPES: `../meta/PLUMBING.md#pipe-meta-learning-integrity`  
SOFTWARE DEPENDENCIES: none by default; exact repeated scoring may be software-supported only after Software Escalation

## GOAL

Improve Xyool from outcomes without moving goalposts, overfitting, or accumulating unnecessary complexity.

## PROCESS

```text
OUTCOME
→ RECONSTRUCT WHAT WAS KNOWABLE
→ COMPARE EXPECTED vs ACTUAL
→ CLASSIFY MISS / SUCCESS
→ IDENTIFY SYSTEM-LEVEL QUESTION
→ RUN `direct-resolution.flow.md`
→ IF DIRECT ANSWER FAILS: AUDIT QUESTION QUALITY
→ IF NON-DISCRIMINATING: RUN `question-frontier.flow.md`
→ CHECK EXISTING EVIDENCE
→ KEEP ONLY MATERIAL COMPETING EXPLANATIONS
→ RUN THE LOWEST SUFFICIENT RESOLUTION LEVEL
→ SIMPLIFY / MODIFY FLOW
→ REGRESS KNOWN HARD CASES
→ VALIDATE WITH UNTOUCHED EVIDENCE ONLY WHEN MATURE
→ IF A CANDIDATE SEEKS SYSTEM/DOMAIN AUTHORITY:
      ROUTE THROUGH PIPELINE INTEGRITY
      → EVALUATION / AUDIT AS REQUIRED
      → PROMOTION / LIFECYCLE
```

## GATES

- no lookahead;
- current goalpost preserved;
- failure preserved;
- development vs holdout separated;
- added complexity earns incremental value.

## OUTPUT STATE

- lesson;
- affected Flow;
- modification status;
- regression implications;
- authority status.

## SOFTWARE / HARD-LIMIT BOUNDARY

Software may support exact scoring or large repeated calculations only when the Software Escalation Flow justifies it.


## Question failure

A repeated weak answer may be a question failure rather than a model failure.

Do not improve the answer indefinitely when the question is the bottleneck.


## Discovery versus validation

Discovery and validation are different jobs.

Use cheap reasoning to discover a candidate answer.

Use broader evidence only when the authority of the conclusion requires it.

Do not make every learning step pay the cost of release-grade validation.


## Promotion boundary

Learning may propose a change and assemble its evidence. It may not promote itself. Candidate authority transitions route through `../meta/pipeline-integrity.flow.md` and `../meta/promotion-lifecycle.flow.md`; material contract changes route through Patching.
