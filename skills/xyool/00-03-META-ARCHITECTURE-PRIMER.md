# Xyool — Meta-Architecture Primer

Status: **CANONICAL ORIENTATION FOR MULTI-DOMAIN XYOOL**

## Purpose

This document teaches what Xyool is **above any one domain** and how to think about the relationship between the Xyool core, a domain implementation, concrete observations, and cross-domain correspondence.

Read this before extending Xyool beyond the Stock / Market domain.

Short form:

> **Xyool learns structures of reality in one domain, maps and configures that domain into Floware through the Meta layer, and transfers only validated structural invariants to another domain through correspondence.**

The Stock / Market system is the first major working implementation and validation laboratory. It is not the permanent ontology of Xyool.

---

# 1. FOUR LEVELS OF XYOOL

Think in four levels:

```text
LEVEL 1 — XYOOL CORE
Reusable reasoning primitives and learning discipline.

LEVEL 2 — META MAPPING + DOMAIN CONFIGURATION
How domain-native semantics are mapped and bound to reusable Floware contracts.

LEVEL 3 — LIVE INSTANCES
Actual companies, people, systems, events, objects, states, observations, decisions.

LEVEL 4 — CORRESPONDENCE
Controlled mapping of a structural principle from one domain to another.
```

These levels must not be silently collapsed.

## Level 1 — Xyool Core

Core concepts should be expressible without stock-specific nouns. Examples:

```text
identity
evidence
source quality
freshness
state
state delta
causal relation
transition
gate
timer / waiting time
probability / uncertainty
magnitude / consequence
friction / resistance
capture / beneficiary
recognition / response
persistence
repetition / cadence
invalidation
decay / staleness
action
outcome
feedback
miss
learning
```

The core asks questions like:

- What state is this object in?
- What changed?
- What caused the change?
- What transition could happen next?
- What evidence would support or kill that transition?
- What gate must be crossed first?
- How long does that gate normally take?
- What consequence follows if it resolves?
- Who captures the consequence?
- Who observes/reacts to it?
- Does the effect persist or decay?
- What did the system fail to notice?

These questions can survive a change of domain.

## Level 2 — Mapping + Domain Configurer

A domain gives the core concepts concrete meaning through explicit mappings and a validated domain configuration.

Canonical composite Meta Flow:
- `floware/meta/pipeline-integrity.flow.md`

Primitive Meta Flows:
- `floware/meta/mapping.flow.md`
- `floware/meta/domain-configurer.flow.md`
- `floware/meta/sequencing.flow.md`
- `floware/meta/patching.flow.md`
- `floware/meta/audit.flow.md`

Specific adapters may still exist below this layer for native calculations, APIs, formats, or system-specific normalization.

Pipeline Integrity is the default end-to-end integrity layer for material multi-Flow work.

```text
MULTI-FLOW OBJECTIVE
→ PIPELINE MANIFEST
→ primitive Meta Flows as needed
→ handoff / state / authority continuity
→ independent Audit
→ VERIFIED / BLOCKED
```

Sequencing is the primitive Meta order-of-operations layer:

```text
SELECTED OPERATIONS
→ prerequisites / gates / shared-state conflicts
→ partial order
→ ready frontier
→ parallel branches + barriers
→ re-entry on invalidation
```

Patching is the Meta change-propagation layer. It is invoked when a core/domain/meta change affects multiple dependent representations:

```text
AUTHORIZED CHANGE
→ PATCH IMPACT GRAPH
→ ALL MATERIAL DEPENDENCIES
→ UPDATE / MIGRATE / VERIFY
→ META AUDIT
```

Patching does not decide what the architecture should become; it prevents an authorized change from being applied incompletely.

Current example — Stock / Market:

```text
capture     → shareholder capture
recognition → market-price recognition
payoff      → realizable capital return
action      → initiate / hold / rotate / harvest / cash
timer       → procurement / deployment / regulatory / revenue clocks
```

A future domain must define its own meanings rather than inherit these automatically.

## Level 3 — Live Instances

These are the actual objects being analyzed.

In markets:
- CODA;
- a Navy procurement path;
- a specific FDA program;
- a Form 4 sale;
- a contract;
- a stock-price response.

Live facts belong to the domain/instance level, not the universal core.

## Level 4 — Correspondence

Correspondence asks:

> **Does a structural relationship learned in one domain have a real counterpart in another domain?**

It does not ask whether two stories merely sound similar.

---

# 2. WHAT MAY BE UNIVERSAL VS LOCAL

Every important principle should be mentally tagged as one of three types.

## A. Core candidate

Potentially domain-independent structure.

Example:

```text
A weak precursor can become useful when it implies a specific falsifiable transition and starts a trackable timer.
```

This may generalize.

## B. Domain implementation

A domain-specific realization of a more general idea.

Example:

```text
customer testing → acceptance → procurement
```

This is a market/business implementation of a more abstract gated-transition chain.

## C. Local calibration

Values or rules that depend heavily on the domain.

Examples:
- 10b5-1 interpretation;
- PDUFA mechanics;
- SEC filing hierarchy;
- stock abnormal-return windows;
- portfolio replacement hurdles;
- quant volatility ceilings;
- a 30–120 day repeat-order window.

Local calibrations do **not** travel by correspondence unless separately validated.

---

# 3. THE ABSTRACTION LADDER

When learning from a concrete case, move upward carefully:

```text
CASE
→ DOMAIN PATTERN
→ ABSTRACT RELATIONSHIP
→ CORE CANDIDATE
```

Example:

```text
CASE:
Customer begins testing a product before a later procurement order.

DOMAIN PATTERN:
Operational testing can precede acceptance/procurement.

ABSTRACT RELATIONSHIP:
Observable commitment/action can be a precursor to a gated state transition.

CORE CANDIDATE:
A precursor that changes transition probability and implies a falsifiable next state can arm a timer.
```

Do not jump directly from one case to a universal law.

---

# 4. THE DESCENT INTO A NEW DOMAIN

When applying a core candidate to another domain, move downward:

```text
CORE CANDIDATE
→ TARGET-DOMAIN INTERPRETATION
→ TARGET OBJECTS / STATES
→ TARGET EVIDENCE
→ TARGET TEST
→ TARGET CALIBRATION
```

Example structure:

```text
Core candidate:
precursor → trackable transition

Target domain asks:
- what counts as a precursor here?
- what is the actual transition?
- what observable action is meaningful?
- what is the stop event?
- what invalidates it?
- how long does it normally take here?
```

The source domain supplies a hypothesis and reasoning pattern, not the answer.

---

# 5. CORRESPONDENCE IS NOT ANALOGY

Analogy says:

> "These things look alike."

Correspondence requires:

```text
same structural relationship?
same causal direction?
same relevant state variables?
same kind of gate or constraint?
same falsifiable consequence?
important differences explicitly named?
target-domain evidence available?
```

A metaphor may inspire correspondence research, but it is not validation.

---

# 6. KNOWLEDGE FLOW

Xyool should learn in both directions.

```text
DOMAIN A OBSERVATION
→ ABSTRACT PRINCIPLE
→ CORRESPONDENCE HYPOTHESIS
→ DOMAIN B TEST
→ DOMAIN B RESULT
→ REFINE ABSTRACTION
→ UPDATE A AND/OR B IF WARRANTED
```

A target-domain failure can teach that the supposed invariant was actually local to the source domain.

That is useful information.

---

# 6A. FAILURE DIAGNOSIS

Supporting doctrine: `meta-failure-flow.md`.

Before an apparent miss is converted into a repair or new principle, Xyool must determine whether a genuine system failure occurred.

```text
OBSERVED DIVERGENCE / MISS / BAD OUTCOME
→ freeze the relevant information set
→ identify the expected contract
→ compare expected vs observed
→ test knowability
→ locate the first broken layer
→ classify primary failure vs propagated effects
→ CONFIRMED / EXONERATED / UNRESOLVED
→ only confirmed defects may generate repair candidates
```

Core distinction:

> **Bad outcome ≠ system failure.**

Exoneration is a valid result. Xyool must not rewrite itself around randomness, hindsight, external surprise, or uncertainty already represented by the governing contract.

---

# 7. MISS LEARNING AT THE META LEVEL

The existing miss rule applies only after failure diagnosis has established a defect or a genuine missing question:

```text
APPARENT MISS
→ failure diagnosis
→ CONFIRMED DEFECT / ESTABLISHED MISSING QUESTION
→ freeze what was knowable
→ identify missing question
→ generalize minimally
→ test controls
→ promote only if transferable
```

But multi-domain Xyool adds two additional questions:

1. **Was the miss caused by using a domain-local assumption as if it were universal?**
2. **Does another domain contain a tested principle that could have generated the missing question here?**

A correspondence-generated fix still requires validation in the target domain.

---

# 8. AUTHORITY AND VALIDATION

A principle can have different statuses in different places.

Example:

```text
Source domain: SUPPORTED
Abstract invariant: PROVISIONAL CORE CANDIDATE
Target domain correspondence: HYPOTHESIS
Target-domain implementation: UNVALIDATED
```

Do not let source confidence leak into target confidence.

Recommended statuses:

```text
CORE CANDIDATE
CORE SUPPORTED
DOMAIN CANONICAL
DOMAIN PROVISIONAL
CORRESPONDENCE HYPOTHESIS
CORRESPONDENCE PROVISIONAL
CORRESPONDENCE SUPPORTED
REJECTED
SUPERSEDED
```

Existing module-specific statuses remain valid; these labels describe the cross-domain layer.

---

# 9. CURRENT REALITY OF THE REPO

Current active development domain:

```text
stock-market
```

Current domain objective:

```text
compound capital
```

The mature operational machinery currently lives mostly under:

```text
skills/xyool/
domains/stock-market/
research/system-tests/
```

Future domains should not be forced to use market vocabulary. They should live under:

```text
domains/<domain-name>/
```

and declare their own contract.

---

# 10. WHAT FUTURE CHATS MUST DO

Before working beyond the current market domain:

1. Read `XYOOL-START-HERE.md`.
2. Read `00-00-START-HERE-XYOOL-PRIMER.md`.
3. Read this document.
4. Read `00-04-DOMAIN-CORRESPONDENCE-HOWTO.md`.
5. Read `domains/README.md` and the active domain manifest.
6. Read `correspondence/README.md` before transferring knowledge.
7. Distinguish core principle, domain implementation, and local calibration.
8. State what transfers and what does not.
9. Validate in the target domain.
10. Preserve failed mappings.

---

# 10A. AI-NATIVE EXECUTION SUBSTRATE — FLOWARE

Canonical module:
`00-08-FLOWARE-AI-NATIVE-ARCHITECTURE.md`

Xyool's reasoning architecture should not be confused with conventional software implementation.

The preferred AI-era execution stack is:

```text
GOAL
  ↓
FLOWARE
state-aware / evidence-sensitive / adaptive reasoning
  ↓
SOFTWARE
deterministic computation / persistence / permissions / hard limits
  ↓
HARDWARE
compute / sensors / actuators / physical execution
```

This means:
- a canonical reasoning flow may itself be executable architecture;
- code is added where exactness, scale, persistence, security, transactions, or hard limits justify it;
- domain intelligence should not be forced into fixed software branches merely because software is familiar.

Robotics is a useful correspondence example:

```text
robot goal
→ perceive state
→ interpret environment
→ select/adapt flow
→ act
→ observe
→ update state
```

while deterministic software continues to enforce motor control, collision limits, torque limits, emergency stops, drivers, and other non-negotiable constraints.

The transferable structural principle is:

> **Adaptive goal pursuit belongs in Floware; non-negotiable guarantees belong in software.**

Target-domain implementations must still define their own hard limits and evidence semantics.

# 11. ONE-SCREEN MODEL

```text
XYOOL CORE
state / causality / transitions / evidence / timing / consequence / learning
        ↓
MAPPING META FLOW
how domain-native representations align with Floware contracts
        ↓
DOMAIN CONFIGURER META FLOW
how the domain composes and binds those contracts
        ↓
VALIDATED DOMAIN CONFIGURATION
what those ideas mean in this part of reality
        ↓
LIVE INSTANCES
actual objects, events, evidence and decisions
        ↓
OUTCOMES / MISSES
what worked, failed, or remained unknown
        ↓
ABSTRACTION
what relationship may be reusable
        ↓
CORRESPONDENCE
controlled mapping into another domain
        ↓
TARGET-DOMAIN VALIDATION
        ↓
REFINED XYOOL KNOWLEDGE
```

Final principle:

> **Xyool should accumulate transferable understanding without erasing the boundaries that make that understanding valid.**

# 12. GAUNTLET LEARNING IS A CORE CROSS-DOMAIN METHOD

Canonical module: `gauntlet-learning-loop.md`.

The stock-market gauntlets established a reusable system-learning discipline:

CASE → RUN XYOOL → FIND SYSTEM FAILURE/SUCCESS PATTERN → GENERALIZE MINIMALLY → TEST CONTROLS → PERSIST → NEXT CASE REGRESSES THE FIX.

The case is not the primary object of learning. **Xyool is.**

This extends the Miss-to-Question loop beyond explicit misses. Successful cases, source conflicts, edge cases, stale-state transitions, branch-recombination problems, and automation gaps can also produce reusable principles.

Permanent memory rule: **Evidence/history is the memory. The current snapshot is Xyool's latest interpretation of that memory.**

Future domains inherit the gauntlet-learning discipline but define their own ontology, evidence classes, states, timers, consequence/capture semantics, and calibration. A rule discovered in one domain is only a core candidate for another until target-domain tests support it.
