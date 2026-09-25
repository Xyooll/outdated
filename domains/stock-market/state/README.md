# Stock-Market Persistent State Store

Status: **REFERENCE BACKEND / INITIAL CATALOG LAYOUT**

Canonical contract:
- `../STATE.md`
- `../../../skills/xyool/domain-state-persistence.md`

## Goal

Persist enough structured state that future Xyool runs can resume a stock from the latest verified snapshot and fetch only deltas.

## Catalog depth

Not every stock should receive the same research cost.

```text
L0 — IDENTITY
ticker / exchange / issuer / stable IDs only

L1 — BASELINE
identity + latest primary financial/capital facts + source cursors
no material active timer required

L2 — ACTIVE RESEARCH
current causal state + breadcrumbs + unresolved material timer(s)
Quality / recognition / Profit View fields populated as applicable

L3 — FULL TRACKING
material active/approaching catalyst, position relevance, or high research priority
fast refresh schedule + complete timer/evidence/outcome state
```

Promotion is evidence-driven.

A stock can be demoted after timers close or evidence decays without deleting its history.

## Index entry

Recommended `index.json` entity entry:

```json
{
  "US_XNAS_EXAMPLE": {
    "ticker": "EXAMPLE",
    "issuer_id": "SEC_CIK_...",
    "tracking_level": "L2",
    "snapshot_path": "entities/US_XNAS_EXAMPLE.json",
    "refresh_priority": "P1",
    "next_refresh_at": "2026-10-01T12:00:00Z",
    "state_status": "ACTIVE"
  }
}
```

The index exists to answer:

- which entities are cataloged?
- which are due for refresh?
- which have active timers?
- which file/record contains the compact snapshot?

Do not put the full evidence history in the index.

## Entity files

Repository reference paths:

```text
entities/<entity_id>.json
evidence/<entity_id>.jsonl
timers/<entity_id>.jsonl
outcomes/<entity_id>.jsonl
analyses/<entity_id>/<analysis_id>.json
stories/<entity_id>/<story_id>.json
characters/<character_id>.json
```

The directories materialize when the first entity is written.

## Deep-analysis archives

When Xyool performs a full/deep stock analysis, preserve the complete finished analysis artifact under:

```text
analyses/<entity_id>/<analysis_id>.json
```

Then extract operational memory into evidence, timers, dependency state and the compact entity snapshot.

Canonical contract:
- `../../../skills/xyool/stock-analysis-memory-ingestion.md`

The archive is the lossless research layer. The snapshot remains the compact operational layer.

---

## Historical memory migration

Pre-ingestion stock records may be wrapped in reconstructed analysis archives so future Xyool runs can traverse one consistent memory structure.

Reconstruction is explicitly provenance-limited:

```text
archive_origin = RECONSTRUCTED_EXISTING_GIT_STATE
lossless_original = false
```

Migration must not invent missing old research. It preserves the old snapshot/evidence/timer state, records the historical limitations, and leaves existing evidence/timer ledgers byte-for-byte unchanged.

The current catalog migration utility is:
- `../../../scripts/migrate_stock_analysis_memory.py`

A subsequent genuine deep analysis should create a native-lossless archive and become the entity's latest analysis pointer.

---

## Refresh queue

A future batch updater should query the index and process only entities whose:

```text
next_refresh_at <= now
OR required field freshness is STALE/UNKNOWN
OR a user explicitly requests a current refresh
OR an external source signals a new item
```

Order refresh work by:

```text
P0 active exact/HOT
P1 active WARM window
P2 high-Quality unresolved
P3 ordinary catalog
P4 dormant/archive
```

This queue is about data-fetch urgency, not capital rank.

## Backend migration

Git files are the initial auditable implementation.

When live catalog size/update frequency becomes expensive, use an indexed database for operational records and keep:

- schemas;
- migrations;
- state contracts;
- periodic checkpoint exports

in Git.

Do not change the state semantics merely because the storage backend changes.

---

## Canonical atomic-memory transition rules

Promoted from the completed Top-50 gauntlet on 2026-09-19.

These rules are **DOMAIN CANONICAL** for stock-market state unless a stricter stock-specific contract applies.

### 1. Intermediate progress cannot satisfy a downstream gate

Operational, regulatory, qualification or clinical-process progress may advance state maturity without satisfying certification, approval, qualification, delivery or revenue.

Examples of distinct states:

```text
test / review / inspection / launch preparation
-> terminal gate
-> economic conversion
```

Never promote a process milestone to a terminal outcome without primary evidence that the terminal gate itself is satisfied.

### 2. Financing has a typed lifecycle

Represent financing as distinct states rather than one generic "capital" fact:

```text
AVAILABLE_CAPACITY
-> DRAWN_OR_ISSUED
-> COMPLETED_OR_TERMINATED
-> REPAYMENT_OR_CASH_CLAIM
```

A new facility may supersede an old one. Do not sum superseded facilities, count unused capacity as realized cash, or count a completed financing as remaining future capacity.

### 3. Operating and capital branches recombine at shareholder capture

When liquidity, debt, dilution, listing status, financing or repayment obligations can materially affect common-shareholder economics, preserve them as explicit parallel graph branches.

Do not hide a capital-survival dependency inside narrative risk text while allowing the operating branch to reach shareholder value independently.

### 4. Regulatory approval is not commercialization

Preserve the causal chain:

```text
REGULATORY_APPROVAL
-> ACCESS / DISTRIBUTION
-> LAUNCH
-> ADOPTION
-> REVENUE / CASH
-> SHAREHOLDER CAPTURE
```

Approval closes the regulatory gate. It does not automatically satisfy distribution, payer access, launch execution, adoption or cash economics.

### 5. Route evidence by program before company-level recombination

Clinical and product evidence must first map to the correct:

```text
asset
program
trial
indication
population
geography
```

Evidence from another branch is contextual unless a valid dependency edge connects it. Positive and negative program events may coexist and must recombine only at the appropriate company-level node.

### 6. Corporate actions are normalized separately from economic value

Stock splits and reverse splits change share-count and per-share presentation but do not create enterprise value by themselves.

When a split is scheduled:
- create the exact corporate-action timer;
- normalize share counts and per-share historical comparisons;
- preserve pre/post-split denominator lineage;
- route any listing or financing consequence through a separate edge.

### 7. Timer state is event-driven

A newly filed primary event can supersede an approximate timer immediately.

Do not wait for the old window to expire before advancing state. A materially stale timer is a state defect even when its original date range remains open.

### 8. Definitive M&A agreement is not acquisition close

Preserve:

```text
SIGNED_AGREEMENT
-> CONDITIONS / APPROVALS
-> CLOSE
-> CAPITALIZATION RESET
-> ACCOUNTING / INTEGRATION
-> ECONOMIC CONTRIBUTION
```

Target-company forecasts are not acquirer revenue. Share consideration or other capitalization changes at close require a denominator rebase before repricing or Profit View is reused.

Canonical regression report:
- `research/system-tests/2026-09-19-top50-closing-atomic-company-memory-gauntlet-v5.md`



### 9. Material state transitions invalidate derived research rank

Research rank is derived from the live snapshot. It is not permanent company memory.

If a material event changes Quality/capital eligibility, TTC, the primary gate, timer/frontier state, recognition, repricing burden, profit view, or shareholder-capture economics:

```text
LATEST MATERIAL ANALYSIS CHANGES
-> PRIOR RESEARCH RANK BECOMES STALE
-> AFFECTED FIELDS RECOMPUTE
-> CATALOG RERANK RUNS
-> NEW RESEARCH RANK BECOMES FRESH
```

Persist the rank basis so Xyool can detect drift:

```text
research_rank
rank_status
rank_analysis_id
ranked_at
rank_basis_analysis_id
rank_stale_reason
```

`top50_rank` is the cohort/catalog anchor. `research_rank` is the current derived research order.

A realized date is retained in evidence/history, but the live timeline must advance to the next unresolved chronological/economic gate. Rank freshness and timer/frontier freshness therefore share the same invalidation trigger.


### 10. Company success is not stock profitability

Promoted from the 2026-09-19 ten-stock profitability gauntlet.

A favorable operating/catalyst outcome must not be treated as a profitable stock thesis until the full transmission path is checked:

```text
CATALYST / OPERATING SUCCESS
-> INCREMENTAL ECONOMICS
-> NORMALIZED EARNINGS / CASH
-> VALUATION / REPRICING DENOMINATOR
-> RECOGNITION / SECTOR REGIME
-> SHAREHOLDER CAPTURE
-> REMAINING PRICE UPSIDE
```

Canonical consequences:

1. **Normalized earnings bridge is mandatory when accounting is distorted.**
   One-time tax benefits, fair-value marks, unusual credits, acquisition accounting and other nonrecurring items cannot substitute for durable earnings/cash power.

2. **A correct company thesis can still be a profitability miss.**
   If the stock loses money over the decision horizon, validation records a profitability miss even when backlog, revenue, EBITDA or operational execution improved.

3. **Return failure is a separate state from thesis failure.**
   Use RF0-RF4. RF2+ requires a full profitability-transmission audit; RF3 can justify REDUCE/ROTATE/CASH while the operating thesis remains intact.

4. **NO TRADE is scored as cash.**
   Validation may not remove blocked/no-trade names from the portfolio denominator.

5. **Adverse catalysts get event-driven harvest review.**
   After a negative event realizes, recompute remaining downside and mean-reversion/squeeze risk rather than forcing a fixed holding period.

6. **Loss severity is a first-class validation metric.**
   Report hit rate, average winner, average loser and drawdown/loss severity alongside aggregate return.

Canonical regression source:
- `research/system-tests/2026-09-19-ten-stock-point-in-time-profitability-gauntlet-v1.md`


### 11. New alpha signals enter as shadow state before they can alter capital decisions

External research may justify measuring a candidate signal, but literature support alone does not prove incremental value inside Xyool.

Required path:

```text
EXTERNAL METHOD
-> POINT-IN-TIME SHADOW FIELD
-> PRE-OUTCOME FREEZE
-> PARALLEL BASELINE vs AUGMENTED TEST
-> MULTIPLE-TESTING ACCOUNTING
-> INDEPENDENT VALIDATION
-> PROSPECTIVE SHADOW
-> CANONICAL CAPITAL LOGIC ONLY IF PROVEN
```

Examples currently in shadow status:
- earnings / guidance expectation diffusion;
- analyst estimate revisions and dispersion;
- residual / factor-neutral momentum;
- execution / liquidity capacity;
- short borrow feasibility.

Process safeguards such as trial registration, transaction-cost accounting, borrow-feasibility accounting, and multiple-testing disclosure may be canonical immediately because they reduce research bias without asserting alpha.

Canonical references:
- `../../../skills/xyool/research-validation-governance.md`
- `../../../skills/xyool/market-expectations-execution-sidecar.md`


## Story Memory

Canonical Flow:
- `../flows/story-memory.flow.md`

Completed stock stories are persisted as versioned story-memory objects:

```text
stories/<entity_id>/<story_id>.json
```

The catalog index may point to:

```text
latest_story_id
latest_story_path
latest_story_as_of
story_status
story_closure_status
```

Runtime behavior:

```text
resolve entity
→ load latest story
→ load snapshot / timers / evidence as needed
→ inspect source freshness
→ refresh only changed/stale character branches
→ propagate deltas
→ write a new story version only when material
```

Story memory is an operational cache of the evidence-backed narrative, not a substitute for primary evidence.

Default character horizon:

```text
Degree 0: 4 remaining
Degree 1: 3 remaining
Degree 2: 2 remaining
Degree 3: 1 remaining
Degree 4: boundary
```


## Canonical Character Memory

Canonical Flow:
- `../flows/character-memory-reroot.flow.md`

Material companies/entities discovered during story-building may be persisted independently of the root story:

```text
characters/<character_id>.json
```

Character Memory stores reusable:
- stable identity;
- local relationship web;
- relationship edges;
- source cursors;
- evidence pointers;
- prior story roles;
- story pointers.

A Story Memory is a **root-relative view** over these characters.

When a nested character becomes the new research root:
1. load its Character Memory;
2. set it to Degree 0;
3. give it a new four-degree horizon;
4. reuse known evidence/edges;
5. refresh stale branches;
6. expand branches newly in scope.

Do not duplicate evidence merely because the root changes.
