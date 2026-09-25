# Xyool Stock / Market — Persistent State Contract

Status: **CANONICAL DOMAIN IMPLEMENTATION OF DOMAIN-STATE PERSISTENCE**

Parent contract:
- `skills/xyool/domain-state-persistence.md`

## Purpose

The stock domain should be able to resume analysis of a company/security without re-fetching its complete historical evidence every time.

For each cataloged stock, persist:

```text
IDENTITY
+ CURRENT SNAPSHOT
+ AGGREGATED BREADCRUMBS
+ ACTIVE TIMERS
+ SOURCE CURSORS / FRESHNESS
+ APPEND-ONLY EVIDENCE HISTORY
+ OUTCOMES / CLOSED TIMERS
```

The state layer is a cache and audit trail, not an allocator.

Authority remains:

```text
Quality -> eligibility
TTC -> capital priority
Quant -> risk/expression cap
Event Execution -> staging/harvest/re-entry
```

---

## 1. Stock entity identity

Minimum issuer/security identity:

```text
issuer_id
security_id
ticker
exchange
issuer_name
CIK if available
ISIN/CUSIP if available
aliases / prior tickers
security_status
identity_checked_at
```

Prefer stable issuer IDs over ticker strings for historical continuity.

---

## 2. Current snapshot

Each security snapshot should contain at least:

```text
identity
as_of
state_version

quality
capital_status

current_causal_state
next_chronological_event
next_economic_conversion_event
next_profit_producing_event

breadcrumbs_summary
dependency_graph
primary_gating_node
active_timer_ids
closed_timer_head

fes
pfs
hazard_heat
cascade_state
recognition_state
repricing_sensitivity
corporate_action_state
profitability_transmission
normalized_earnings_bridge
recognition_vs_fundamentals
sector_regime
return_failure_state
return_failure_reason
last_profitability_audit_at
profit_view
ttc_state
quant_state
execution_state

research_shadow_state
research_trial_context

story_memory
  latest_story_id
  latest_story_path
  story_as_of
  story_status
  source_authority
  closure_status
  max_degree
  story_reader_head
  compressed_story
  thesis
  primary_conflict
  primary_bottleneck
  likely_next_state
  conditional_window
  primary_invalidation
  story_writer_head
  future_branches[]
  counter_story_branches[]
  next_observable_proofs[]
  writer_freeze_id
  key_characters[]
  character_profile_heads[]
  relationship_graph[]
  relationship_deltas[]
  local_web_heads[]
  newly_entered_characters[]
  ended_relationships[]
  story_policy_status
  material_source_gaps[]
  next_refresh_targets[]

unresolved_questions
completeness_status

source_freshness
source_cursors
latest_material_evidence_ids
```

Not every field must be populated for every stock. Missing required decision fields should remain explicit.

---

## 3. Breadcrumb aggregation

Do not store breadcrumbs only as prose summaries.

Every breadcrumb should have an evidence-ledger record and a current aggregation state.

Suggested breadcrumb object:

```text
breadcrumb_id
transition_key
stage_before
stage_after_candidate
evidence_date
observed_at
materiality
specificity
source_quality
freshness
status
evidence_ids
timer_ids
```

Status:

```text
ACTIVE
CONFIRMED
REALIZED
STALE
INVALIDATED
SUPERSEDED
```

The snapshot should contain only the active/recent breadcrumb summary.

The ledger preserves all historical breadcrumbs.

This allows Xyool to learn:

- how many breadcrumbs normally occur before conversion;
- which breadcrumb types matter;
- time from breadcrumb -> next gate;
- false-positive rates;
- decay/staleness;
- same-company cadence.

---

## 4. Dependency graph persistence

For every material multi-gate catalyst, persist the prerequisite structure rather than leaving the chain only in prose.

Minimum graph object:

```text
dependency_graph:
  graph_version
  as_of
  primary_gate_id
  terminal_node_ids
  nodes[]
  edges[]
  analyst_rationale
```

Minimum node fields:

```text
node_id
label
node_type
state
satisfied
evidence_status
event_key
timer_ids
expected_window
economic_role
materiality
evidence_ids
invalidation
```

Minimum edge fields:

```text
from
to
relationship
required
evidence_ids
```

The graph must be acyclic.

A runtime analysis may derive:

```text
frontier_gate_ids
blocked_node_ids
failed_node_ids
satisfied_node_ids
unsatisfied_node_ids
terminal_node_ids
downstream_node_counts
primary_gate_ready
```

A **frontier gate** is an unresolved node whose required predecessors are satisfied. It is the current dependency frontier, not automatically the highest-TTC capital opportunity.

The analyst may designate one `primary_gate_id` only with an explicit rationale tied to downstream economic materiality. Timer proximity alone is insufficient.

Do not count graph nodes as independent catalysts. A serial chain is one path whose downstream value remains conditional on upstream gates.

Authoritative methodology:
- `skills/xyool/ttc-dependency-chain.md`

---

## 5. Timer persistence

Every unresolved material timer should be stored independently.

Minimum:

```text
timer_id
event_key
event_class
timer_type
state
opened_at
last_confirmed_at

single_date
window_start
window_end
timing_type
timing_basis
timing_confidence

start_gate
stop_gate
remaining_gates

pfs_state
hazard_heat
cascade_dependencies

quality_state_at_open
recognition_state_at_open
profit_view_at_open

next_refresh_at
refresh_priority
invalidation

evidence_ids
closed_at
close_reason
outcome_id
```

For the new dual-timer architecture, the same event may have:

```text
timer A = SINGLE_DATE_TARGET
timer B = PRE_CATALYST_WINDOW
```

They must close together when the underlying event resolves, but timing performance is scored separately.

---

## 6. Source cursor model

### SEC / EDGAR

Persist:

```text
CIK
latest_accession_processed
latest_filing_date_processed
forms_of_interest
last_checked_at
fresh_until
next_refresh_at
```

When refreshing, query only filings newer than the stored accession/date unless an audit requests historical reconstruction.

### Issuer IR / press releases

Persist:

```text
latest_item_id
latest_canonical_url
latest_published_at
last_checked_at
content_hash if available
```

Fetch only newer items plus any current active timer page that requires revalidation.

### Regulatory / agency

Examples:

```text
FDA application / PDUFA / approval record
DoD / procurement record
NRC docket
FAA certification
government award database
```

Persist the domain-specific case/application/docket identity and last processed update.

### Market data

Historical company evidence should not be re-fetched just because a price is stale.

Persist decision anchors:

```text
freeze_price
freeze_timestamp
event_price anchors
recognition reference price
```

For a current price-dependent request, fetch current market data and recompute price-sensitive fields.

Do not treat old stored price as current.

### News / discovery

Use news primarily to discover possible state changes.

Persist:

```text
last_seen_published_at
last_seen_provider_id/url
last_checked_at
```

Then verify material facts against primary sources before state promotion where possible.

---

## 6A. SEC filing company memory

Canonical process:
- `skills/xyool/sec-filing-company-memory.md`

SEC filings feed the existing company memory rather than creating one permanent Xyool object per filing.

```text
SEC filing
→ form-specific extraction
→ append-only evidence
→ compact filing_memory head
→ discovery / confluence update
→ deep-analysis escalation when material
```

Persist in the snapshot:

```text
filing_memory:
  recent_filings
  latest_by_family
  signal_heads
  confluence_state
  deep_analysis_required
  deep_analysis_trigger_reasons
  latest_accession
  latest_form
  last_ingested_at
```

Raw filing bodies are transient parsing inputs by default. Preserve accession/source URL and extracted source context in evidence so the original can be rechecked.

A previously unknown stock may be auto-cataloged from an SEC discovery event with:

```text
Quality = UNASSESSED
Capital = BLOCKED_PENDING_QUALITY
Tracking = L1 / DISCOVERY
```

This creates research visibility only.

The SEC layer cannot promote Quality, TTC, or executable capital by itself.

## 7. Adaptive refresh

Refresh priority should be calculated from operational relevance.

Conceptual states:

```text
P0 — active exact/target event or HOT timer
P1 — active WARM pre-catalyst window / material unresolved gate
P2 — high-Quality monitored stock with unresolved catalyst
P3 — ordinary cataloged stock
P4 — dormant / archived / blocked with no live catalyst
```

These are fetch priorities only.

They do not replace Q1-Q5 or TTC.

Examples:

- RARE after FDA approval: close old regulatory timers; reduce regulator refresh priority; open commercial-launch/adoption timer only if supported.
- OESX PFS4/WARM: issuer/customer/market state gets a nearer refresh schedule.
- dormant company with no unresolved material event: filings/IR checked much less often.

Exact numeric refresh intervals remain infrastructure calibration, not market alpha.

---

## 8. Delta update procedure

For a stock update:

```text
LOAD snapshot
-> identify active timers / unresolved questions
-> inspect source freshness
-> fetch only stale/due sources
-> normalize new evidence
-> for SEC evidence, aggregate into company filing memory / confluence state
-> fingerprint / deduplicate
-> append evidence ledger
-> update breadcrumbs
-> update dependency graph / frontier gates
-> update timers
-> recompute affected Quality/FES/PFS/Hazard/cascade/recognition/repricing/profitability-transmission/return-failure/TTC fields
-> close realized/superseded timers
-> update cursors
-> write new snapshot
-> report delta
```

Default user-facing update should focus on:

```text
WHAT CHANGED?
WHICH STATE CHANGED?
WHICH TIMER OPENED/CLOSED/MOVED?
WHICH DEPENDENCY / GATING NODE CHANGED?
DID THE BASIC / FULLY DILUTED REPRICING BURDEN CHANGE?
DID PROFITABILITY TRANSMISSION OR NORMALIZED EARNINGS CHANGE?
DID RECOGNITION / SECTOR REGIME CREATE RETURN DIVERGENCE?
DID RETURN_FAILURE_STATE CHANGE?
DID A LISTING / REVERSE-SPLIT CORPORATE-ACTION TIMER CHANGE?
DOES QUALITY CHANGE?
DOES TTC PRIORITY CHANGE?
WHAT NEEDS FETCHING NEXT?
```

Not a repeated biography of the company.

---

## 8A. Derived-rank freshness

Research rank is a **derived interpretation of the current stock state**, not durable evidence.

The live rank may depend on:

```text
Quality / capital eligibility
TTC / happens / date window
primary gating node
recognition state
repricing sensitivity
profit view
shareholder-capture / dilution state
```

When a material delta changes any rank-driving field, the prior rank must be marked stale even if the security remains in the same catalog cohort.

Required behavior:

```text
MATERIAL STATE TRANSITION
-> recompute affected stock-state fields
-> rank_status = STALE
-> preserve prior rank as history
-> run the applicable catalog rerank
-> write research_rank + rank_analysis_id + ranked_at
-> rank_status = FRESH
```

Recommended index metadata:

```text
research_rank
rank_status
rank_analysis_id
ranked_at
rank_basis_analysis_id
rank_method_version
rank_stale_reason
```

`top50_rank` may remain the cohort/original catalog anchor. `research_rank` is the current derived research order.

A rank may not remain marked `FRESH` if its `rank_basis_analysis_id` no longer matches the entity's latest material analysis/state basis.

A material ranking-method change must also advance `rank_method_version`. Existing ranks remain historically valid under their recorded method, but they must not be represented as having been computed under the newer method. The next catalog rerank must write the current method version.

This rule also applies to **timer/frontier changes**. A realized catalyst may leave its calendar date in history while the live rank/timeline advances to the next unresolved gate.

---

## 8B. Profitability-state persistence

The stock snapshot must preserve whether company execution is still translating into an attractive stock-return opportunity.

Recommended fields:

```text
profitability_transmission:
  state
  incremental_economics
  normalized_earnings_bridge
  valuation_denominator
  recognition_vs_fundamentals
  sector_regime
  shareholder_capture
  remaining_price_upside
  confidence

return_failure_state: RF0 / RF1 / RF2 / RF3 / RF4
return_failure_reason
last_profitability_audit_at
```

Interpretation:

```text
RF0 = no material return divergence
RF1 = watch
RF2 = active divergence; full profitability audit required
RF3 = capital-priority failure even if operating thesis remains intact
RF4 = thesis / shareholder-capture failure
```

A materially positive operating update can still worsen capital priority if:
- normalized earnings/cash does not improve;
- the current valuation already discounts the improvement;
- recognition has outrun fundamentals;
- sector regime becomes adverse;
- dilution/debt weakens common-share capture;
- another opportunity or cash has superior return velocity.

Conversely, price weakness alone does not create RF3/RF4.

When `return_failure_state` changes or profitability transmission moves between `STRONG / ADEQUATE / FRAGILE / BLOCKED`, the current `research_rank` becomes stale and must be recomputed.

---

## 8C. Research shadow-state persistence

External-method research fields must be persisted separately from canonical rank-driving state until independent validation promotes them.

Recommended object:

```text
research_shadow_state:
  as_of
  method_version
  expectations_diffusion:
    earnings_surprise_state
    guidance_delta
    estimate_revision_direction
    estimate_revision_magnitude
    revision_breadth
    revision_persistence
    estimate_dispersion
    coverage_count
    post_earnings_drift_state
    data_quality
  factor_neutral_recognition:
    total_momentum
    sector_relative_momentum
    residual_momentum
    idiosyncratic_return_trend
    breadth_confirmation
    recognition_acceleration
    factor_model_basis
    data_quality
  execution_capacity:
    bid_ask_spread
    median_dollar_volume
    position_as_pct_adv
    days_to_build
    days_to_exit
    estimated_slippage
    estimated_market_impact
    halt_gap_risk
    execution_state
    data_quality
  short_feasibility:
    borrow_available
    borrow_fee
    borrow_fee_trend
    utilization
    short_interest
    days_to_cover
    float
    ownership_concentration
    locate_stability
    squeeze_risk
    short_feasibility_state
    data_quality
```

Required separation:

```text
SHADOW FIELD CHANGES
-> persist / refresh / audit
-> DO NOT stale research_rank
-> DO NOT alter LONG / SHORT / NO TRADE
-> DO NOT alter TTC desired exposure
```

unless a pre-registered validation arm explicitly grants those fields decision authority.

If an alpha-bearing shadow feature is later promoted, the promotion must:
1. advance the applicable method version;
2. identify which shadow fields become canonical rank-driving fields;
3. stale all ranks whose basis predates the promoted method;
4. rerun the applicable catalog ranking.

This prevents an unvalidated sidecar from influencing capital indirectly through rank invalidation.

### Research trial context

When a stock is used in a formal experiment, snapshot/archive metadata may include:

```text
research_trial_context:
  trial_id
  dataset_role
  freeze_at
  decision_arm
  baseline_method
  augmented_method
  outcome_reveal_status
```

These fields are audit metadata, not company evidence.

Canonical governance:
- `skills/xyool/research-validation-governance.md`
- `skills/xyool/market-expectations-execution-sidecar.md`

---

## 9. Required evidence preservation

Do not throw away old evidence after compaction.

Preserve enough to reconstruct:

- what was known at any historical decision date;
- which breadcrumbs existed;
- which timers were active;
- source freshness at the time;
- Quality/TTC state at the time;
- later outcome.

This is required for anti-lookahead backtesting.

---

## 10. Initial physical layout

Initial repository-backed implementation:

```text
domains/stock-market/state/
├─ index.json
├─ entities/
├─ evidence/
├─ timers/
├─ outcomes/
└─ schemas/
   ├─ entity-state.schema.json
   ├─ evidence-event.schema.json
   └─ timer.schema.json
```

Once catalog/update volume grows, move the operational records to an indexed database while preserving the same object contract.

---

## 11. Catalog workflow

When cataloging a new stock:

```text
1. resolve stable identity
2. ingest only the minimum historical evidence needed to establish current state
3. store source cursors
4. create current snapshot
5. open unresolved timers
6. store active breadcrumbs
7. record unresolved questions
8. schedule next refresh
```

Do not exhaustively fetch the entire corporate history unless the current causal state requires it.

The persistent ledger grows naturally as the company is monitored.

---

## Core rule

> **For cataloged stocks, Xyool should normally resume from persistent state and fetch deltas. Full historical reconstruction becomes an explicit audit action, not the default update path.**


## Character profile memory

Canonical core Flow:
`../../floware/core/character-system.flow.md`

Material stock characters may persist:
- quantitative traits;
- qualitative traits;
- behavior signature;
- resources / constraints / agency;
- non-exclusive archetype hypotheses;
- contradictions;
- transformation state;
- unclassified/emergent features.

Stock-local archetype definitions:
`../CHARACTER-ARCHETYPES.md`

Archetypes are descriptive hypotheses and do not replace Quality, TTC, payoff, or capital authority.

## Story memory

Canonical Flow:
`flows/story-memory.flow.md`

The stock snapshot carries a compact Story Memory head so a future run can resume from the latest evidence-backed narrative rather than reconstructing the full story.

The full finished story remains losslessly archived.

Default recursion horizon:

```text
Degree 0 -> 4 degrees remaining
Degree 1 -> 3
Degree 2 -> 2
Degree 3 -> 1
Degree 4 -> 0 / boundary
```

Refresh procedure:

```text
LOAD STORY MEMORY
→ inspect character/source freshness
→ fetch stale/due branches only
→ propagate story deltas
→ update atomic state
→ write new story-memory version when material
```


### Relationship-web persistence

The Story Memory graph stores both characters and the relationships joining them.

A refresh must compare prior and current edge states:

```text
NEW / SAME / STRENGTHENED / WEAKENED / CHANGED_TYPE / SUSPENDED / ENDED
```

Every material nested character owns a bounded local web under the remaining four-degree budget.

Examples:

```text
main D0 -> local depth 4
D1 character -> local depth 3
D2 character -> local depth 2
D3 character -> local depth 1
D4 character -> local boundary
```

This includes subsidiaries. A subsidiary is a local root, not a flat child record.
