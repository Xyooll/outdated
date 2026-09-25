# Xyool — Domain / Correspondence Architecture

Status: **CANONICAL META-ARCHITECTURE / FUTURE-DOMAIN HANDOFF**

## Purpose

Xyool is currently being developed and validated in the **Stock / Market domain**.

That is the current working implementation. It is not the permanent boundary of Xyool.

Xyool is intended to become a more general system for reasoning about changing parts of reality by preserving reusable causal principles, state-transition methods, timing logic, evidence discipline, miss-learning, and decision processes, then applying them to new domains through explicit **correspondence**.

Short form:

> **Core reasoning architecture → domain-specific implementation → validated correspondence to other domains.**

This document exists so a future chat does not mistake current stock-market machinery for the full ontology of Xyool, and does not blindly copy market rules into unrelated domains.

---

# 1. CURRENT SCOPE

Current active domain:

```text
DOMAIN: STOCK / MARKET
STATUS: ACTIVE DEVELOPMENT + VALIDATION
PRIMARY OBJECTIVE: CAPITAL COMPOUNDING
PRIMARY DECISION UNIT: CAPITAL ALLOCATION
PRIMARY OBJECTS: COMPANIES / SECURITIES / CATALYSTS / POSITIONS
PRIMARY OUTCOME: REALIZABLE SHAREHOLDER RETURN
```

Current market-specific concepts include, among others:
- Quality Qualifier;
- Opportunity State Engine;
- Forward Evidence State;
- Time to Catalyst;
- catalyst profitability;
- shareholder capture;
- recognition / stock-price response;
- insider activity / 10b5-1 interpretation;
- new capital vs earned capital;
- rotation / harvest;
- Quant market-risk expression.

These are authoritative inside the current Stock / Market domain according to their validation status.

They are **not automatically universal laws of every future domain**.

---

# 2. XYOOL ABOVE THE MARKET LAYER

At the higher level, Xyool should preserve reusable primitives rather than stock-specific vocabulary.

Candidate cross-domain primitives include:

```text
IDENTITY
OBSERVATION / EVIDENCE
SOURCE QUALITY
FRESHNESS
STATE
STATE DELTA
CAUSAL RELATIONSHIP
TRANSITION
GATE
TIMER / WAITING TIME
PROBABILITY / UNCERTAINTY
MAGNITUDE / CONSEQUENCE
FRICTION / RESISTANCE
CAPTURE / WHO RECEIVES THE CONSEQUENCE
RECOGNITION / OBSERVER RESPONSE
PERSISTENCE
REPETITION / CADENCE
INVALIDATION
DECAY / STALENESS
ACTION
OUTCOME
FEEDBACK
MISS / LEARNING
VALIDATION STATUS
```

These are candidate general primitives because they can describe many processes without assuming the object is a stock.

Example abstraction:

```text
MARKET-SPECIFIC
customer acceptance → procurement → deployment → revenue → stock recognition

ABSTRACT
state A → gated transition → state B → realized consequence → observer/system response
```

The abstraction preserves causal structure while removing market-only assumptions.

---

# 3. THREE-LAYER DESIGN

Xyool should be interpreted through three levels:

```text
LAYER 1 — XYOOL CORE
Domain-independent reasoning primitives and governance

LAYER 2 — META MAPPING + DOMAIN CONFIGURATION
Domain-specific meanings, evidence, objectives, actions, losses, and calibrations bound to Floware through explicit mappings

LAYER 3 — INSTANCE / LIVE OBJECT
The actual company, biological system, technology, institution, event, process, or other object under analysis
```

For the current system:

```text
XYOOL CORE
   ↓
MAPPING + DOMAIN CONFIGURER
   ↓
STOCK / MARKET DOMAIN CONFIGURATION
   ↓
CODA / OESX / ELMT / SPCB / etc.
```

A future extension should look like:

```text
XYOOL CORE
   ↓
MAPPING + DOMAIN CONFIGURER
   ↓
NEW DOMAIN CONFIGURATION
   ↓
LIVE OBJECTS IN THAT DOMAIN
```

Do not force a future domain to pretend that its objects are securities or that its objective is capital return.

---

# 4. DOMAIN CONFIGURATION CONTRACT

Before Xyool is used seriously in a new domain, run the canonical `floware/meta/domain-configurer.flow.md`, using `floware/meta/mapping.flow.md` for material domain-to-Floware bindings, and create/update a domain manifest that answers:

```text
Domain Name:
Domain Status:
Primary Objective:
Decision Maker / User:
Unit of Decision:
Objects / Entities:
Observable Evidence:
Hidden / Latent State:
Important State Transitions:
Relevant Timers:
Actions Available:
Outcome / Payoff Definition:
Failure / Loss Definition:
Capture Definition:
Recognition / Response Definition:
Persistence Definition:
Primary Frictions:
Invalidation Conditions:
Required Freshness Standard:
Source Hierarchy:
Validation Method:
Anti-Lookahead Rule:
Miss-Handling Rule:
Safety / Authority Constraints:
Market-Derived Principles Used:
Market-Derived Principles Explicitly Not Assumed:
Domain-Specific Principles:
Current Calibration Status:
```

A domain is not production-ready merely because several Xyool words can be renamed to fit it.

---

# 4A. FAILURE DIAGNOSIS

Supporting doctrine: `meta-failure-flow.md`.

Before an apparent miss becomes a repair candidate, the active domain must supply enough contract/evidence context to determine:

```text
OBSERVED DIVERGENCE / MISS / BAD OUTCOME
→ freeze relevant information
→ identify expected contract
→ compare expected vs observed
→ test knowability
→ trace upstream → downstream
→ locate first broken layer
→ CONFIRMED / EXONERATED / UNRESOLVED
→ only confirmed defects enter repair/promotion
```

The meta layer must distinguish primary failure from propagated effects, legitimate uncertainty, invalidation, external surprise, and ordinary probabilistic variation.

A bad result is not sufficient evidence of a system failure.

---

# 5. CORRESPONDENCE

## Definition

**Correspondence** is the controlled process of asking whether a causal principle, state relation, timer structure, evidence pattern, or learning rule discovered in one domain has a structurally similar form in another domain.

Correspondence is not analogy by resemblance.

It must preserve the causal or informational relationship that makes the principle useful.

Short form:

> **Do not transfer the surface story. Transfer the invariant relationship, then revalidate it in the target domain.**

---

# 6. CORRESPONDENCE OBJECT

Every proposed cross-domain correspondence should be recorded as:

```text
SOURCE DOMAIN:
SOURCE PRINCIPLE / PATTERN:
SOURCE EVIDENCE / VALIDATION STATUS:

ABSTRACT INVARIANT:
What relationship remains after domain-specific nouns are removed?

TARGET DOMAIN:
TARGET OBJECTS / STATES:
PROPOSED TARGET CORRESPONDENCE:

STRUCTURAL MATCH:
What causal/state/timing relationship is genuinely the same?

IMPORTANT DIFFERENCES:
What changes in mechanism, incentives, observability, timescale, agency, or loss?

TRANSFERRED COMPONENTS:
Which parts may be reused?

NON-TRANSFERRED COMPONENTS:
Which market-specific assumptions, thresholds, probabilities, or actions must stay behind?

TARGET-DOMAIN TEST:
How can this be falsified prospectively or on untouched evidence?

STATUS:
HYPOTHESIS / PROVISIONAL / SUPPORTED / REJECTED / SUPERSEDED
```

---

# 7. CORRESPONDENCE RULES

## Rule 1 — Structure before vocabulary

Two things correspond because their causal/state structure matches, not because they share words.

## Rule 2 — Principle may transfer; calibration does not automatically transfer

A market principle such as:

> missed expected windows should eventually become negative evidence

may have cross-domain value.

But a market-derived 30-day or 90-day threshold does not transfer unless separately validated.

## Rule 3 — Objective functions are domain-specific

The Stock / Market domain optimizes compounded capital.

A future domain may optimize prediction accuracy, reliability, intervention quality, resource allocation, discovery, safety, understanding, or another objective.

Do not preserve the market objective when it no longer fits.

## Rule 4 — Action authority is domain-specific

A correspondence can inform understanding without authorizing an action.

## Rule 5 — Similar outcome does not prove shared mechanism

Correlation or visual resemblance is insufficient.

## Rule 6 — Fail closed on hidden differences

If a transferred principle depends on an unverified mechanism in the target domain, classify the correspondence as provisional or blocked.

## Rule 7 — Negative correspondence is useful

Record cases where a market principle does **not** map cleanly. Knowing the boundary of a principle is part of Xyool knowledge.

## Rule 8 — Miss learning travels better than numeric calibration

General learning rules such as:

```text
freeze pre-outcome evidence
identify the missing question
generalize
test positive + negative controls
promote only if transferable
```

are more likely to be domain-general than market-specific return or timing coefficients.

---

# 8. EXAMPLE OF CORRESPONDENCE

Illustrative only — not a promoted non-market rule.

Stock / Market pattern:

```text
weak causal breadcrumb
→ timer becomes armed
→ stronger evidence advances state
→ expected conversion window becomes relevant
→ missed window eventually decays confidence
```

Abstract invariant:

```text
early observable precursor
→ conditional future transition becomes trackable
→ confirming evidence raises transition confidence
→ time becomes evidence
→ persistent non-occurrence can eventually contradict the hypothesis
```

Potential future-domain correspondence:

A new domain may contain precursor signals, state transitions, and expected windows. The abstract logic may apply, but the evidence types, waiting-time distribution, and invalidation threshold must be learned inside that domain.

The correspondence does **not** permit importing stock-market FES levels, TTC rankings, or market timing thresholds unchanged.

---

# 9. KNOWLEDGE FLOW

Xyool knowledge should be allowed to move in both directions:

```text
STOCK / MARKET EXPERIENCE
        ↓
ABSTRACT PRINCIPLE LIBRARY
        ↓
CORRESPONDENCE TEST
        ↓
NEW DOMAIN
        ↓
NEW DOMAIN EVIDENCE / MISSES
        ↓
REFINE ABSTRACT PRINCIPLE
        ↓
OPTIONALLY IMPROVE MARKET DOMAIN TOO
```

A future domain can therefore teach the market implementation something new.

The Stock / Market layer is the first laboratory, not the permanent center of reality.

---

# 10. REPOSITORY HANDOFF RULE

A future chat loading this repository should be able to answer immediately:

1. **What is Xyool at the highest level?**
2. **Which domain is active now?**
3. **What objective is active in that domain?**
4. **Which principles are domain-general candidates?**
5. **Which rules are market-specific?**
6. **How are principles transferred to a new domain?**
7. **What must be revalidated rather than copied?**
8. **Where are current domain instructions located?**

If those questions cannot be answered from repository documents, the architecture handoff is incomplete.

---

# 11. CURRENT DOMAIN REGISTRY

Current registry:

```text
stock-market
  status: ACTIVE
  maturity: PRIMARY DEVELOPMENT / VALIDATION DOMAIN
  objective: compounded capital
  manifest: domains/stock-market/DOMAIN.md
```

Future domains should be registered under `domains/<domain-name>/DOMAIN.md`.

Do not silently activate a new domain. Its manifest must declare its status and validation level.

---

# 12. FUTURE DOMAIN LIFECYCLE

Use:

```text
IDEA
→ DOMAIN MANIFEST
→ CORRESPONDENCE HYPOTHESES
→ DOMAIN-SPECIFIC EVIDENCE MODEL
→ PROVISIONAL TESTS
→ NEGATIVE CONTROLS
→ UNTOUCHED / PROSPECTIVE VALIDATION
→ SUPPORTED DOMAIN PRINCIPLES
→ OPERATIONAL USE
→ CONTINUOUS MISS LEARNING
```

A new domain must not inherit production status from the Stock / Market domain.

---

# 13. CURRENT AUTHORITY BOUNDARY

As of this architecture version:

- Xyool's operationally developed decision system is the **Stock / Market domain**.
- Future reality domains are architectural extensions, not current validated production systems.
- Correspondence is a **knowledge-transfer method**, not proof that a principle applies elsewhere.
- Market-derived numeric calibrations remain inside the market domain unless explicitly revalidated.
- Domain-general candidates may be promoted only after evidence across domains supports them.

---

# 14. FUTURE-CHAT INSTRUCTION

When a future chat receives this repo:

```text
READ XYOOL-START-HERE.md
→ READ 00-00-START-HERE-XYOOL-PRIMER.md
→ READ THIS DOMAIN / CORRESPONDENCE ARCHITECTURE
→ IDENTIFY ACTIVE DOMAIN
→ LOAD THAT DOMAIN'S MANIFEST
→ LOAD ONLY THE MODULES REQUIRED FOR THE TASK
```

For current work, the active domain is `stock-market`.

For future-domain work, do not begin by copying stock-market instructions. Begin by creating/loading the target domain manifest and an explicit correspondence map.

---

# 15. FINAL PRINCIPLE

> **XYOOL SHOULD ACCUMULATE KNOWLEDGE WITHOUT CONFUSING WHERE THE KNOWLEDGE CAME FROM, WHERE IT IS VALID, OR WHY IT SHOULD TRANSFER.**

The market layer teaches Xyool principles. Correspondence determines what may survive beyond the market layer. Target-domain evidence decides what actually belongs there.