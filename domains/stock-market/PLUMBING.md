# Xyool Stock / Market — Plumbing

Status: **ACTIVE / CANONICAL DOMAIN PLUMBING V1**

Parent contracts:
- `../../floware/PIPE-CONTRACT.md`
- `../../floware/FLOW-CONTRACT.md`
- `../../floware/meta/pipeline-integrity.flow.md`

Primary pipeline:
- `flows/company-analysis.flow.md`

## Purpose

Make the material connections inside the stock-analysis Pipeline explicit.

These Pipes do not replace the participating Flows.

They define how outputs/state may safely cross between those Flows/stages.

Core rules:

> **Flow correctness does not imply Pipe correctness.**

> **Quality may block capital without blocking discovery.**

> **Authority may not silently increase through a Pipe.**

> **A stale upstream state invalidates affected downstream results.**

## Representation

Each material Pipe uses:

~~~text
ENDPOINT POINTERS
+
CONNECTION WRAPPER
+
LIVE PIPE STATE when executing
~~~

The definitions below are durable wrappers.

Runtime compatibility/readiness/version belongs to live Pipe state for the current execution epoch.

---

## PIPE-STOCK-ENTRY

Purpose:
enter Company Analysis from the authorized Xyool objective/current stock state.

~~~text
FROM POINTER:
  CORE-XYOOL-EXECUTION / authorized stock objective
  + persistent stock state when available

TO POINTER:
  STOCK-COMPANY-ANALYSIS / INPUT STATE

SEMANTIC INVARIANTS:
  ticker/security identity must resolve
  stored state is prior processed evidence, not automatic current truth
  user objective/goalpost preserved

PROVENANCE:
  preserve state/evidence pointers

FRESHNESS:
  downstream Company Analysis must run freshness/identity checks

AUTHORITY:
  process routing → analysis/orchestration only

FAILURE:
  unresolved identity/material missing state = BLOCKED/INCOMPLETE as applicable
~~~

---

## PIPE-STOCK-EVIDENCE-DISCOVERY

Purpose:
carry source-supported stock evidence into Discovery Visibility without silently applying a Quality-only prefilter.

~~~text
FROM POINTERS:
  STOCK-COMPANY-ANALYSIS / identity + freshness + sourced evidence
  STOCK story-sourcing / claim-specific source state
  persistent stock evidence/state where fresh

TO POINTER:
  STOCK-DISCOVERY-VISIBILITY-V1 / INPUT STATE

SEMANTIC INVARIANTS:
  evidence provenance/freshness preserved
  low current Quality does not erase a material causal breadcrumb
  raw filing/news/price presence does not automatically create hidden-transition status

AUTHORITY:
  sourced stock evidence → research-visibility evaluation only

FAILURE:
  unresolved issuer/security identity or material source provenance = BLOCKED/UNKNOWN
~~~

---

## PIPE-STOCK-DISCOVERY-QUALITY

Purpose:
carry a visible research candidate into Quality without allowing Quality to erase valid discovery.

~~~text
FROM POINTER:
  STOCK-DISCOVERY-VISIBILITY-V1 / OUTPUT STATE

TO POINTER:
  STOCK-QUALITY-CREDENTIALS-V1 / Quality evaluation

SEMANTIC INVARIANTS:
  visibility ≠ capital eligibility
  breadcrumb/hidden-transition evidence remains visible
  discovery evidence retains provenance

WRAPPER RULE:
  Quality may classify FAIL/WATCH while the candidate remains research-visible

AUTHORITY IN:
  discovery visibility only

AUTHORITY OUT:
  Quality qualification / normal-capital eligibility only

FAILURE:
  Quality exclusion may block normal capital
  but may not retroactively delete a causal discovery candidate
~~~

---

## PIPE-STOCK-QUALITY-TTC

Purpose:
enforce the Quality authority gate before normal TTC capital competition while preserving TTC as separate priority authority.

~~~text
FROM POINTER:
  STOCK-QUALITY-CREDENTIALS-V1 / QUALITY + trajectory + unlock + survival

TO POINTER:
  STOCK-COMPANY-ANALYSIS / DEPENDENCY-TTC stage
  + applicable TTC methods

SEMANTIC INVARIANTS:
  Quality is credentials/eligibility
  TTC is causal timing/capital priority
  neither field silently becomes the other

GATE:
  normal capital competition requires the applicable Quality eligibility state

AUTHORITY IN:
  normal-capital eligibility

AUTHORITY OUT:
  TTC may rank/prioritize only within its own authority
  no sizing/execution authority created by this Pipe

FAILURE:
  blocked/failed Quality cannot be silently promoted by catalyst proximity
~~~

---

## PIPE-STOCK-CHARACTER-READER

Purpose:
carry current material Character/relationship state into Story Reader.

~~~text
FROM POINTERS:
  CORE-CHARACTER-SYSTEM / character profiles
  STOCK character-influence / relationship graph
  recursive-character-story / refreshed nested character state

TO POINTER:
  CORE-STORY-READER / INPUT STATE

SEMANTIC INVARIANTS:
  character identity ≠ story role
  archetype ≠ causal proof
  raw traits/evidence remain authoritative
  relationship provenance retained

BARRIER:
  every material required character branch must be:
    complete
    explicitly blocked
    or NOT APPLICABLE with reason

FRESHNESS:
  parent story cannot be fresher than material characters

FAILURE:
  unresolved material character freshness/source gap blocks Reader closure
~~~

---

## PIPE-STOCK-READER-THESIS

Purpose:
carry evidence-backed current causal state into the stock thesis without leaking future branches backward.

~~~text
FROM POINTER:
  CORE-STORY-READER / OUTPUT STATE
  + current economics/payoff/recognition state as separately sourced

TO POINTER:
  STOCK-NARRATIVE-THESIS-V1

SEMANTIC INVARIANTS:
  Reader output describes past → present
  future outcomes are not facts
  thesis must preserve unresolved questions/source gaps
  economic/recognition state must retain its own evidence basis

AUTHORITY:
  descriptive/explanatory → descriptive/explanatory

FAILURE:
  future leakage, stale character state, or unsupported causal compression blocks thesis completion
~~~

---

## PIPE-STOCK-THESIS-WRITER

Purpose:
allow Story Writer to branch forward only from the evidence-backed current state.

~~~text
FROM POINTERS:
  STOCK-NARRATIVE-THESIS-V1 / current thesis
  CORE-STORY-READER / current state
  current character/relationship state
  active timers/processes

TO POINTER:
  CORE-STORY-WRITER / INPUT STATE

SEMANTIC INVARIANTS:
  current facts remain separate from future hypotheses
  archetype resemblance alone cannot create a branch
  branch confidence remains qualitative/ordered unless calibration exists

FORBIDDEN TRANSFORMATION:
  HIGH confidence → numeric probability
  unless explicit calibrated Mapping is present

AUTHORITY:
  explanatory state → conditional hypothesis generation

FAILURE:
  unreliable current state or fictional prerequisites = WRITER_PARTIAL / NO_VALID_BRANCH
~~~

---

## PIPE-STOCK-STORY-STRATEGY

Purpose:
carry the understood stock story/state into Strategy selection without allowing Strategy to manufacture the thesis.

~~~text
FROM POINTERS:
  STOCK-NARRATIVE-THESIS-V1
  CORE-STORY-WRITER / material conditional branches
  current payoff/recognition/capital-path/window state

TO POINTER:
  STOCK-STRATEGY-LAYER-V1 / INPUT STATE

REQUIRED MEANING:
  story/thesis
  likely next state when evidence discriminates
  conditional window
  primary invalidation
  recognition/payoff context
  executable constraints where known

SEMANTIC INVARIANTS:
  Strategy cannot repair an unknown thesis
  TA/Quant do not become fundamental thesis authority
  conditional branch ≠ realized fact

AUTHORITY IN:
  analysis/thesis + domain capital state

AUTHORITY OUT:
  strategy-family selection / conditional expression design only

FAILURE:
  unknown thesis/window when required = WAIT/BLOCK rather than invented strategy certainty
~~~

---

## PIPE-STOCK-STRATEGY-EXPRESSION

Purpose:
prevent Strategy selection from silently becoming production execution authority.

~~~text
FROM POINTER:
  STOCK-STRATEGY-LAYER-V1 / selected strategy card

TO POINTER:
  approved downstream risk/execution layer

SEMANTIC INVARIANTS:
  strategy recommendation/design ≠ executable order
  TTC desired exposure / Quant risk cap / hard execution constraints remain authoritative where applicable

GATE:
  explicit downstream authority must exist

AUTHORITY IN:
  strategy selection only

AUTHORITY OUT:
  never greater than explicitly approved capital/risk/execution authority

FAILURE:
  missing authorization = NO EXECUTION
~~~

---

## PIPE-STOCK-STATE-INVALIDATION

Purpose:
propagate a material upstream state/version change into every affected descendant.

~~~text
FROM POINTER:
  persistent stock state / newly promoted material evidence

TO POINTERS:
  affected Quality / TTC / payoff / recognition / thesis / Writer / Strategy outputs

TRIGGER:
  material state/version/as-of change

WRAPPER:
  identify descendants whose assumptions depend on changed state
  mark them INVALIDATED
  preserve prior outputs historically
  start new execution epoch
  rerun only affected descendants

SEMANTIC INVARIANT:
  old downstream result may not remain current merely because its file/object still exists

FAILURE:
  stale descendant reused as current = Pipeline Integrity failure
~~~

---

## PIPE-STOCK-TERMINAL-STATE

Purpose:
write current stock state only after required pipeline closure.

~~~text
FROM POINTERS:
  STOCK-COMPANY-ANALYSIS / completed applicable stages
  completeness audit
  current pipeline epoch

TO POINTER:
  persistent stock state / STATE DELTA

GATE:
  mandatory applicable stages are PASS / NOT APPLICABLE WITH REASON / BLOCKED / FAIL
  blockers are explicit
  provenance retained

SEMANTIC INVARIANTS:
  current head does not erase history
  blocked/partial analysis is not stored as silently complete
  material rank-driving changes stale/recompute derived state as governed by STATE.md
~~~

---

## Current Plumbing migration status

The Pipes above cover the highest-risk semantic/authority/state transitions in the canonical company-analysis Pipeline.

Other lower-risk adjacent process arrows may remain derived/implicit while:
- their semantics are lossless;
- no authority changes;
- no material mapping exists;
- no independent invalidation behavior is required.

Promote an implicit connection to a named Pipe when repeated audit or Patching work shows that its relationship-specific contract matters.

Do not create a Pipe file/object for every cosmetic adjacency.

## Audit rule

The domain Plumbing is not VERIFIED merely because these wrappers exist.

For a live pipeline execution, Pipeline Integrity must still validate:
- endpoint pointer resolution;
- source/target version;
- current freshness;
- live gate/readiness state;
- invalidation state;
- provenance;
- authority continuity.
