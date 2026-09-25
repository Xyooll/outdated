# Xyool — Domain & Correspondence How-To

Status: **CANONICAL OPERATING PLAYBOOK FOR MULTI-DOMAIN EXTENSION**

## Purpose

This document teaches a future chat or analyst how to use the Xyool meta-architecture in practice.

It answers four operational questions:

1. How do I create a new domain?
2. How do I decide whether a market principle is actually reusable?
3. How do I build and test a correspondence?
4. How do lessons from another domain flow back into Xyool without corrupting the source domain?

Short form:

> **Do not copy rules across domains. Extract structure, map carefully, test locally, and preserve failures.**

---

# 1. START BY IDENTIFYING THE ACTIVE LAYER

Before doing anything, answer:

```text
Am I working on:
A. a live instance inside an existing domain?
B. a domain rule/calibration?
C. a possible core principle?
D. a cross-domain correspondence?
E. a new domain definition?
```

Do not solve a Level A problem by changing Level C architecture unless the evidence actually justifies it.

---

# 2. HOW TO CREATE A NEW DOMAIN

Create:

```text
domains/<domain-name>/DOMAIN.md
```

Start from the domain contract, not from market terminology.

Required domain questions:

```text
1. What is the objective?
2. What is the decision unit?
3. What entities/objects exist?
4. What can be observed directly?
5. What important state is latent/hidden?
6. What state transitions matter?
7. What are the gates?
8. What timers/waiting processes exist?
9. What actions are available?
10. What counts as success/payoff?
11. What counts as failure/loss in the domain?
11A. What testable contracts distinguish Xyool system failure from adverse outcome, uncertainty, invalidation, or external surprise?
12. Who/what captures the consequence?
13. What observers/systems recognize/respond to change?
14. What evidence sources are strongest?
15. What is the freshness standard?
16. What are the invalidation conditions?
17. How will misses be handled?
18. How will anti-lookahead be enforced?
19. What imported principles are being considered?
20. Which calibrations are explicitly local?
```

A domain is not ready just because its nouns are listed. It must define how Xyool's primitives operate there.

---

# 3. DOMAIN-READINESS CHECK

Before a domain can be ACTIVE, require:

```text
[ ] objective defined
[ ] entities defined
[ ] evidence hierarchy defined
[ ] state model defined
[ ] transition model defined
[ ] timers/gates defined where relevant
[ ] action authority defined
[ ] success/failure defined
[ ] material layer contracts defined for Meta Failure Flow
[ ] first-broken-layer attribution is possible
[ ] freshness rule defined
[ ] invalidation rule defined
[ ] miss loop defined
[ ] imported principles labeled by status
[ ] local calibrations separated from core principles
[ ] at least one live or historical worked example
[ ] at least one negative/control example
```

If these are incomplete, mark the domain:

```text
DRAFT
EXPERIMENTAL
or
BLOCKED
```

Do not call it ACTIVE prematurely.

---

# 4. HOW TO EXTRACT A PRINCIPLE FROM THE STOCK DOMAIN

Use this ladder:

```text
CONCRETE MARKET CASE
→ MARKET PATTERN
→ STRIP MARKET-SPECIFIC NOUNS
→ ABSTRACT RELATIONSHIP
→ TEST WHETHER THE RELATIONSHIP DEPENDS ON MARKET MECHANICS
→ CORE CANDIDATE OR MARKET-LOCAL RULE
```

Forced questions:

```text
What exactly repeated across cases?
What causal mechanism made it work?
Which parts depend on securities/markets/accounting/regulation?
Could the relationship be expressed without market nouns?
What would falsify the abstraction?
Does a negative control break it?
```

Example:

```text
Market observation:
A customer-specific testing disclosure often precedes acceptance/procurement.

Do NOT export:
"testing means buy the stock."

Possible abstraction:
Observable costly/committed action by a relevant agent can increase confidence that a gated transition is underway.
```

The abstraction is a hypothesis until independently supported.

---

# 5. HOW TO BUILD A CORRESPONDENCE

Create a file using:

```text
correspondence/TEMPLATE.md
```

Then complete this sequence.

## Step 1 — Source integrity

Record:
- source domain;
- exact source principle;
- source validation status;
- source evidence/tests;
- known failure modes.

Do not begin with a vague remembered principle.

## Step 2 — Abstract invariant

Write the principle without domain-specific nouns.

Bad:

```text
A Navy SAT often leads to procurement.
```

Better:

```text
Successful completion of a required acceptance gate can reduce uncertainty before a later commitment/procurement transition.
```

## Step 3 — Target interpretation

Define:
- target objects;
- target states;
- target gate;
- target actors;
- target observable evidence;
- target stop event;
- target failure mode.

## Step 4 — Structural match

Explain why the mapping may be causal rather than metaphorical.

Ask:

```text
same direction of causality?
same kind of dependency?
same type of gate?
same information timing?
same consequence structure?
similar confounders?
```

## Step 5 — Differences

List differences explicitly.

A correspondence with no differences section is incomplete.

## Step 6 — Transfer boundary

Write two lists:

```text
TRANSFERS
DOES NOT TRANSFER
```

This is mandatory.

## Step 7 — Target-domain test

Define evidence that would support or reject the mapping.

Use prospective evidence or frozen historical information where possible.

## Step 8 — Status

Use:

```text
HYPOTHESIS
PROVISIONAL
SUPPORTED
REJECTED
SUPERSEDED
```

Do not skip directly to SUPPORTED.

---

# 6. HOW TO TELL CORRESPONDENCE FROM FALSE ANALOGY

Use the correspondence stress test:

```text
1. Is the same causal relationship present?
2. Are the relevant actors actually analogous in function?
3. Does the same state transition exist?
4. Is the gate structurally necessary in both domains?
5. Does timing carry comparable information?
6. Are the important confounders named?
7. Can the target mapping fail in a measurable way?
8. Is there target-domain evidence, not just source-domain success?
```

If most answers are no/unknown, keep it as inspiration only.

---

# 7. HOW TO USE A CORRESPONDENCE IN LIVE ANALYSIS

A correspondence should normally change **questions before actions**.

Correct pattern:

```text
SUPPORTED SOURCE PRINCIPLE
→ correspondence suggests a target-domain question
→ inspect target evidence
→ update target state if warranted
→ target-domain authority decides action
```

Incorrect pattern:

```text
market principle worked before
→ assume target outcome
→ take target action
```

Example:

```text
Source lesson:
Overdue expected transitions should decay in confidence.

Target use:
Ask whether the target system has an evidence-backed expected transition window and whether non-occurrence is informative.

Do NOT automatically import the stock-domain overdue threshold.
```

---

# 8. HOW TO HANDLE CALIBRATIONS

Every numeric value should answer:

> **Is this core, domain-local, or correspondence-derived?**

Examples likely local to markets:
- event-return windows;
- volatility limits;
- trading thresholds;
- FDA historical priors;
- SEC filing timing;
- capital rotation rules.

When entering a new domain:

```text
retain structure
reset calibration
re-estimate locally
```

Never carry a numeric threshold merely because the abstract principle transferred.

---

# 9. HOW TO FEED TARGET-DOMAIN LEARNING BACK INTO XYOOL

Before treating a target-domain miss or bad outcome as a reusable lesson, run the canonical `meta-failure-flow.md`.

```text
target-domain anomaly
→ freeze information
→ identify target-domain contract
→ test knowability
→ locate first broken layer
→ confirm / exonerate / leave unresolved
→ only confirmed defects feed repair/correspondence learning
```

After a confirmed target-domain defect or a valid correspondence test result, ask:

```text
Did the correspondence hold?
Did it hold only under extra conditions?
Did it fail because the source principle was too narrow?
Did it fail because the target mapping was wrong?
Did the target reveal a better abstraction?
Does the source domain need a new question too?
```

Possible outcomes:

```text
A. target support strengthens the abstract principle
B. target support reveals boundary conditions
C. target failure narrows the principle
D. target failure rejects the correspondence only
E. target evidence generates a new core candidate
```

Do not rewrite source-domain history to make the transfer look successful.

---

# 10. HOW MISSES WORK ACROSS DOMAINS

When a miss occurs, classify it additionally as:

```text
DOMAIN-LOCAL MISS
CORE-QUESTION MISS
CORRESPONDENCE MISS
CALIBRATION-TRANSFER MISS
DOMAIN-BOUNDARY MISS
PROCESS-OMISSION MISS
UNKNOWABLE OUTCOME
```

Then run the normal miss loop.

For a correspondence miss, specifically ask:

```text
Was the invariant wrong?
Was the target mapping wrong?
Did we transfer something that should have stayed local?
Did we fail to name a structural difference?
Was target evidence too weak?
```

Every material correspondence miss should end with one of:

```text
mapping retained
mapping narrowed
mapping demoted
mapping rejected
core abstraction refined
no change — outcome genuinely unknowable
```

---

# 11. HOW TO ADD A NEW DOMAIN TO THE REGISTRY

Update:

```text
domains/registry.yaml
```

Required registry fields should include at least:

```text
name
status
manifest
objective
notes
```

Only mark a domain ACTIVE when its readiness checks pass.

Current active domain remains:

```text
stock-market
```

until a future domain is explicitly added and validated.

---

# 12. FUTURE-CHAT HANDOFF PROCEDURE

When a future chat is asked to work with Xyool beyond markets, it should say internally:

```text
1. What domain am I in?
2. Is that domain already registered?
3. If yes, load its manifest.
4. If no, draft a domain manifest before importing market rules.
5. Which Xyool core principles are relevant?
6. Which are only market implementations?
7. Is there an existing correspondence file?
8. If not, create/test one rather than assuming transfer.
9. What target-domain evidence validates the mapping?
10. What remains provisional or blocked?
```

---

# 13. WORKED MINI-EXAMPLE

Source-domain principle:

```text
A precursor is useful when it changes the probability/timing of a specific falsifiable transition.
```

Source implementation:

```text
customer testing → acceptance/procurement timer
```

Target-domain correspondence process:

```text
Target object: TBD
Target precursor: TBD
Target transition: TBD
Target gate: TBD
Target evidence: TBD
Target invalidation: TBD
Target waiting-time calibration: must be learned locally
```

What transfers:

```text
look for action-linked precursors tied to a specific future state
```

What does not transfer:

```text
customer semantics
procurement semantics
market return assumptions
market timing windows
capital actions
```

That is correct correspondence discipline.

---

# 14. COMPLETION CHECKLIST

Before declaring a new correspondence or domain usable:

```text
[ ] correct layer identified
[ ] source principle fetched from current repo
[ ] source status known
[ ] abstraction written without source nouns
[ ] target mapping defined
[ ] structural differences named
[ ] transfer/non-transfer boundary written
[ ] target falsification defined
[ ] target evidence collected
[ ] negative/control case considered
[ ] status assigned
[ ] local calibrations separated
[ ] miss path defined
[ ] registry/docs updated if needed
```

Blank means incomplete.

---

# 15. FINAL OPERATING RULE

> **Xyool should transfer questions, structures, and tested causal relationships before it transfers conclusions.**

That rule is the safest way to grow from the Stock / Market layer into broader parts of reality without turning analogy into false knowledge.
