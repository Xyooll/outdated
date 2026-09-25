# FLOW — Stock Company Analysis

FLOW ID: `STOCK-COMPANY-ANALYSIS`  
STATUS: **ACTIVE / CANONICAL**  
DOMAIN: stock-market  
JOB: company / catalyst / capital-state analysis  
AUTHORITY: analysis/orchestration only; capital authority remains Quality → TTC → approved downstream constraints
PARENT GOALPOST: supplied by the active stock objective / frozen development goalpost
UPSTREAM FLOWS: Xyool Execution, persistent stock state, domain configuration, research/evidence-to-state
DOWNSTREAM FLOWS: Discovery Visibility, Quality, Character System, Story Reader/Writer, narrative-thesis, strategy-layer, approved downstream expression, meta audit
INBOUND PIPES: `../PLUMBING.md#pipe-stock-entry`
OUTBOUND PIPES: `../PLUMBING.md#pipe-stock-evidence-discovery`; domain pipeline Plumbing at `../PLUMBING.md`; terminal state via `../PLUMBING.md#pipe-stock-terminal-state`
SOFTWARE DEPENDENCIES: exact denominator arithmetic, current market data, persistent-state integrity, downstream hard risk/execution limits where justified
META SEQUENCING: `../../../floware/meta/sequencing.flow.md`

## GOAL

Produce a complete, evidence-backed stock state without silently skipping a material gate.

## GOALPOST

A live analysis is complete when every applicable mandatory state is:
`PASS / NOT APPLICABLE WITH REASON / BLOCKED / FAIL`

Canonical detail:
`skills/xyool/00-mandatory-run-sequence.md`

## INPUT STATE

- ticker / issuer / security;
- user objective;
- stored domain state if available;
- active timers / unresolved questions;
- current goalpost when part of development work.

## EVIDENCE

Use:
- current primary filings/regulator/issuer evidence where material;
- stored fresh evidence first;
- market data only where needed;
- credible secondary sources for discovery/context;
- explicit inference labels.

## PROCESS

```text
LOAD STATE
→ LOAD STORY MEMORY
→ IDENTIFY STORY DELTAS / STALE CHARACTER BRANCHES
→ FRESHNESS / IDENTITY
→ STORY SOURCING / SOURCE AUTHORITY
→ DISCOVERY VISIBILITY
→ QUALITY CREDENTIALS
→ CHARACTER SYSTEM / QUALITATIVE + QUANTITATIVE PROFILE
→ CHARACTER INFLUENCE / ENTITY GRAPH
→ STORY READER / CURRENT CAUSAL STATE
→ CATALYST INVENTORY
→ EVENT INTEGRITY
→ DEPENDENCY / TTC
→ CORRESPONDENCE RHYTHM WHEN PROCESS-TIMING IS MATERIAL
→ INSIDER CONTEXT
→ ECONOMICS / SHAREHOLDER CAPTURE
→ PAYOFF / REPRICING
→ RECOGNITION
→ DOWNSIDE / INVALIDATION
→ HOLDING / REPLACEMENT HURDLE
→ NARRATIVE THESIS
→ STORY WRITER / CONDITIONAL FUTURE BRANCHES
→ STRATEGY LAYER
→ DOWNSTREAM EXPRESSION ONLY IF AUTHORIZED
→ COMPLETENESS AUDIT
→ STATE DELTA
```

The displayed process is the canonical domain precedence skeleton.

Sequencing interpretation:
- hard gates/order constraints remain mandatory;
- independent evidence/character refresh branches may run in parallel;
- Story Reader/final narrative waits at a barrier for all material required character branches;
- if new evidence invalidates an earlier gate, the affected downstream work is INVALIDATED and rerun in a new execution epoch;
- chronological adjacency in this list does not automatically mean a hard dependency.

The route is adaptive:
- irrelevant branches may be marked NOT APPLICABLE with reason;
- material unknowns may not be skipped;
- a new evidence state may cause earlier gates to be revisited.

## GATES

Discovery Visibility must precede any Quality-only research exclusion.
Quality must precede normal capital competition.
TTC must identify the actual next causal gate.
Payoff must separate economics from recognition.
Current holding must be compared before full rotation.

## BOUNDARIES

This Flow does not:
- create production position sizing;
- bypass Quality;
- treat Quant as thesis authority;
- invent missing dates/probabilities;
- promote shadow research features without validation.

## FAIL-CLOSED CONDITIONS

Any material missing mandatory field that could change the decision results in:
`INCOMPLETE / BLOCKED`

## OUTPUT STATE

- identity/freshness;
- Quality state;
- causal/event state;
- TTC / next gate;
- economic/payoff state;
- recognition state;
- downside/invalidation;
- capital eligibility / priority state;
- blockers;
- provenance;
- what changed.

## LEARNING HOOK

Material misses route to:
`floware/core/learning.flow.md`

## SOFTWARE / HARD-LIMIT BOUNDARY

Software may support:
- exact denominator arithmetic;
- current market-data retrieval;
- persistent state integrity;
- downstream hard risk/execution limits.

Reasoning and routing remain Floware.


## Narrative synthesis

After the detailed state is complete, route through:

`narrative-thesis.flow.md`

The final reasoning object should be a causal story/thesis supported by the detailed ledger.

A material relationship present in evidence but omitted from the thesis is a mapping miss.


## Discovery visibility

Canonical subflow:

`discovery-visibility.flow.md`

Discovery Visibility runs before Quality capital eligibility so a weak current Quality state cannot erase a source-supported hidden transition from research. Visibility grants research attention only; Quality still owns normal-capital eligibility.

## Quality screening

Canonical subflow:

`quality-credentials.flow.md`

Quality should remain a simple credentials/potential screen. It determines whether a stock deserves deeper capital/thesis work and normal capital eligibility. It does not need to tell the entire company story.


## Strategy selection

After the story/thesis and relevant timing window are understood, route through:

`strategy-layer.flow.md`

The Strategy Layer chooses how or whether to express the thesis.

TA and Quant are strategy families inside this layer. They do not create the thesis.


## Recursive character closure

A live company analysis is incomplete if any material character in the story remains unexpanded without an explicit closure reason.

Canonical Flows:
- `character-influence.flow.md`
- `recursive-character-story.flow.md`

This applies to all material characters, not only subsidiaries or investee companies.


## Character-level freshness

The parent freshness lock is insufficient when material characters are public/reporting entities.

Before final narrative/thesis:
1. refresh each material character's current company memory;
2. check new filings, issuer news, and material regulator/exchange disclosures;
3. propagate relevant story deltas back to the parent;
4. fail closed if a material character has an unresolved freshness gap.

Canonical rule:

> **The parent story cannot be fresher than its material characters.**


## Story sourcing

Canonical subflow:

`story-sourcing.flow.md`

This applies to the main company and every material recursive character/subsidiary.

Required principle:

> **Better sources produce a better story.**

For each material claim, use the strongest available evidence that directly supports that claim. Where practical, source both sides of material relationships.

A parent-level filing refresh does not substitute for independently sourcing a material subsidiary or character.


## Story-memory load-first

For a cataloged stock, load:

`story-memory.flow.md`

before broad external research.

Preferred runtime sequence:

```text
domain_state_get
+ domain_state_story
→ determine stale/due story branches
→ refresh only those branches
→ propagate deltas
→ rewrite Story Memory only when material
```

Do not reconstruct a closed/known story from scratch merely because a new chat began.
