# FLOW — Development

FLOW ID: `CORE-DEVELOPMENT`  
STATUS: **ACTIVE / FLOWARE-FIRST**

## GOAL
Improve Xyool or a domain capability while preserving the frozen goalpost and minimizing unnecessary implementation complexity.

## PROCESS
```text
LOAD GOALPOST
→ INSPECT CURRENT FLOW / EVIDENCE
→ DEFINE FAILURE OR OPPORTUNITY
→ RUN `direct-resolution.flow.md`
→ IF WORKABLE: USE THE SIMPLE ANSWER
→ IF NOT WORKABLE: RUN `question-frontier.flow.md`
→ DEFINE THE SMALLEST JUSTIFIED SOURCE CHANGE
→ IF THE CHANGE IS MATERIAL / MULTI-SURFACE: RUN `../meta/pipeline-integrity.flow.md`
→ PIPELINE INTEGRITY INVOKES PATCHING / SEQUENCING / MAPPING / CONFIGURATION / AUDIT AS NEEDED
→ APPLY THE VERIFIED CHANGE PIPELINE
→ VERIFY AT THE LOWEST SUFFICIENT RESOLUTION LEVEL
→ EVALUATE AGAINST GOALPOST
→ ONLY IF NEEDED: ESCALATE EVIDENCE OR SOFTWARE
```

## DEFAULT
Development means improving the Flow, state representation, evidence routing, or boundaries.

Development decides **what should change and why**.

For material multi-surface changes, route through Pipeline Integrity:
`../meta/pipeline-integrity.flow.md`

Within that composite, Patching decides **where the authorized change propagates** and Sequencing decides **in what dependency-safe order**.

It does not mean writing software.

## GATES
- current goalpost remains fixed;
- change addresses evidenced need;
- simpler alternative considered;
- regression implications checked;
- material dependency/patch implications mapped before completion;
- authority unchanged unless earned.

## OUTPUT STATE
Authorized source change + verified patch status where applicable + rationale + evidence + regression status + goalpost progress.

## SOFTWARE / HARD-LIMIT BOUNDARY
Any software change requires:
`core/software-escalation.flow.md`


## Question discipline

Before adding a feature, layer, or model change, ask whether the current question itself is malformed.

Canonical Flow:
`question-frontier.flow.md`


## Proof burden

Do not default to a cohort/tournament.

Use the Direct Resolution ladder:

```text
DIRECT
→ THIN-SLICE
→ CONSUMED REGRESSION
→ TARGETED TOURNAMENT
→ UNTOUCHED VALIDATION
```

Stop at the lowest level sufficient for the current development decision.


## Novelty / challenger generation

Development should still seek the simplest workable answer first.

When the baseline/direct answer exists but the objective explicitly benefits from creative divergence, Development may route to:
`novelty-enhancer.flow.md`

Use novelty to generate challengers, not to bypass proof.

Preferred order:

~~~text
DIRECT / BASELINE
→ if satisfactory: stop
→ if creative divergence is valuable:
     NOVELTY ENHANCER
     → distinct challenger candidates
     → ordinary Development / Evaluation gates
~~~

Novelty never changes the frozen goalpost or hard requirements.
