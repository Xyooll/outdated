# Xyool — Domain Persistent State / Delta Fetch Standard

Status: **CANONICAL INFRASTRUCTURE / DOMAIN-STATE CONTRACT**

## Purpose

Xyool should not repeatedly reconstruct a live object from the full historical internet when it has already verified and stored the relevant evidence.

Each domain therefore maintains its own persistent state layer.

This state is **data, not authority**. It never overrides current evidence, domain rules, source hierarchy, Quality, TTC, Quant, or any other governing module.

Core rule:

> **Load stored domain state first. Fetch only missing, stale, due, or newly changed evidence. Preserve provenance and history so every derived state can be audited.**

This is separate from conversational memory.

Conversational memory stores lessons, preferences, decisions, and session context.

Domain persistent state stores structured live-object facts, breadcrumbs, timers, source cursors, derived state, and outcomes.

---

## 1. Storage model

Every operational domain should expose three logical layers:

```text
CURRENT SNAPSHOT
+ APPEND-ONLY EVIDENCE / STATE-CHANGE LEDGER
+ SOURCE CURSORS / FRESHNESS
```

### Current Snapshot

Compact answer to:

> What does Xyool currently believe about this object?

It should contain only the current state needed to resume work quickly.

Examples:

- identity;
- current state;
- unresolved transitions;
- active breadcrumbs;
- active timers;
- latest Quality / confidence / status;
- current source freshness;
- next required refresh;
- references to the evidence that produced the state.

### Evidence / State-Change Ledger

Append-only history of material observations and state changes.

The ledger exists so Xyool can:

- audit why a state exists;
- distinguish new evidence from already-processed evidence;
- avoid repeatedly re-reading the same source;
- preserve superseded / invalidated facts;
- replay historical state without hindsight;
- aggregate breadcrumbs over time;
- learn timer cadence and transition duration.

Do not silently rewrite the ledger because current interpretation changes.

### Source Cursors / Freshness

For every material source family, store the last processed position.

Examples:

```text
SEC:
  latest accession processed
  latest filing date processed

issuer IR:
  latest item ID / URL / published_at processed

regulator:
  latest decision / docket / update ID processed

market data:
  last decision-anchor timestamp stored
  current-price freshness state

news/discovery:
  latest published_at / provider ID processed
```

A source cursor allows:

```text
FETCH SINCE CURSOR
```

instead of:

```text
FETCH ALL HISTORY AGAIN
```

---

## 2. Domain layout

Recommended logical layout:

```text
domains/<domain>/
├─ DOMAIN.md
├─ STATE.md
└─ state/
   ├─ index.json
   ├─ entities/
   │  └─ <entity_id>.json
   ├─ evidence/
   │  └─ <entity_id>.jsonl
   ├─ timers/
   │  └─ <entity_id>.jsonl
   ├─ outcomes/
   │  └─ <entity_id>.jsonl
   ├─ analyses/
   │  └─ <entity_id>/
   │     └─ <analysis_id>.json
   └─ schemas/
      ├─ entity-state.schema.json
      ├─ evidence-event.schema.json
      ├─ timer.schema.json
      └─ analysis-ingestion-bundle.schema.json
```

The physical backend may later be SQLite, Postgres/Supabase, object storage, or another durable store.

The **contract must stay backend-independent**.

Git-repository files are acceptable for initial development, auditability, and moderate catalog sizes. A database should become the live backend when write volume, query volume, or catalog size makes repository commits inefficient.

---

## 3. Entity identity

Every live object must have a stable domain identity.

Never use display name alone.

Minimum:

```text
domain
entity_id
identity_version
primary external identifiers
aliases
status
```

For stocks, the entity identity should distinguish issuer from security where necessary.

Examples:

```text
issuer_id: SEC_CIK_1515673
security_id: US_XNAS_RARE
ticker: RARE
```

Ticker changes must not create a new issuer history accidentally.

---

## 4. Evidence event

Every material observation stored in the ledger should include:

```text
event_id
domain
entity_id
observed_at
effective_at
source_type
source_id
source_url_or_accession
source_published_at
source_fetched_at
source_hash / fingerprint
evidence_class
structured_fact
native_text_summary
transition_implication
timer_ids affected
confidence
status
supersedes / invalidates
```

Use deterministic fingerprints where practical to deduplicate the same fact retrieved through several paths.

Do not store an entire webpage when a structured fact plus source identity is sufficient.

---

## 5. Derived state

Derived state is reproducible interpretation built from stored evidence.

Examples:

```text
Quality state
FES
PFS
Hazard Heat
causal transition
timer state
recognition state
Profit View
completeness status
```

Each derived field should retain:

```text
value
as_of
computed_at
evidence_ids
rule_version
confidence
freshness
```

When evidence changes, recompute only the affected derived state where practical.

---

## 6. Timers

Timers are first-class persistent objects.

Minimum timer fields:

```text
timer_id
entity_id
event_key
timer_type
state
opened_at
last_confirmed_at
single_date
window_start
window_end
timing_basis
remaining_gates
pfs_state
hazard_heat
recognition_state
quality_state_at_open
next_refresh_at
invalidation
evidence_ids
closed_at
close_reason
```

Timer types may include domain-specific values.

For stocks, preserve at least:

```text
SINGLE_DATE_EXACT
SINGLE_DATE_TARGET
PRE_CATALYST_WINDOW
PROCUREMENT
REGULATORY
DEPLOYMENT
REPEAT_CADENCE
CASCADE_GATE
```

One event may legitimately have both a dated timer and a pre-catalyst window.

---

## 6A. Deep-analysis memory ingestion

A deep stock analysis must not be reduced directly into the compact snapshot.

Use the canonical lossless-to-operational contract in:

- `skills/xyool/stock-analysis-memory-ingestion.md`

Pipeline:

```text
FULL ANALYSIS ARTIFACT
→ enumerate material conclusions
→ assign a persistence disposition to every material conclusion
→ validate identities / references / duplicates
→ archive full analysis
→ append evidence / timer revisions
→ patch operational snapshot
→ completeness audit
```

The archive preserves the finished decision-useful analysis artifact. It must not contain hidden chain-of-thought.

Every material conclusion must map to at least one persistence disposition or explicitly state why it is non-persistent. Missing disposition means **FAIL CLOSED** for memory ingestion.

Runtime support where available:

- `stock_analysis_memory_plan`
- `stock_analysis_memory_ingest`
- `stock_analysis_memory_audit`

This ingestion layer complements, rather than replaces, normal delta state updates.

---

## 7. Fetch decision algorithm

Before any external fetch:

```text
1. LOAD domain state index
2. LOAD entity snapshot
3. IDENTIFY requested fields / decision
4. CHECK provenance + freshness for required fields
5. CHECK source cursors
6. FETCH only missing / stale / due / changed source families
7. DEDUP against stored evidence fingerprints
8. APPEND new evidence
9. RECOMPUTE affected derived state
10. UPDATE snapshot + cursors + next_refresh_at
11. REPORT what changed
```

Do not fetch old data merely because the current chat has not seen it.

Do not skip a current fetch when the stored state is stale for the user's decision.

---

## 8. Freshness

Freshness is field- and source-specific.

Each source cursor should support:

```text
last_checked_at
last_changed_at
fresh_until
next_refresh_at
refresh_priority
status
```

Suggested statuses:

```text
FRESH
DUE
STALE
UNKNOWN
BLOCKED
```

Do not use one global TTL for every source.

A filing-derived incorporation date may remain fresh indefinitely unless corrected.

A market price can become stale in minutes.

A procurement breadcrumb may need faster refresh once its Hazard Heat becomes HOT.

---

## 9. Adaptive refresh priority

Fetching frequency should depend on decision relevance.

Conceptual priority:

```text
ACTIVE / HOT TIMER
> exact/target timer approaching
> WARM causal window
> material unresolved high-Quality object
> ordinary monitored object
> dormant / low-priority catalog object
```

This is a fetch-priority rule, not a capital-ranking rule.

A Q1 exact binary can require a current factual refresh while still being blocked for normal capital.

---

## 10. State compaction

The snapshot must remain compact.

Do not copy the entire evidence ledger into the current snapshot.

Snapshot should preserve:

- current values;
- active timer IDs;
- latest material evidence IDs;
- aggregate breadcrumb state;
- source freshness;
- unresolved questions;
- retrieval keys.

Historical detail belongs in the ledger.

Periodically compact derived summaries, but never erase the append-only evidence needed for audit/replay.

---

## 11. Fetch minimization

A request should use the minimum source work needed to answer correctly.

Examples:

### User asks for current catalyst list

Load stored timers.

Fetch only:
- timers whose source freshness is due;
- entities whose active window requires a refresh;
- entities with an unresolved source cursor gap.

### User asks for historical causal path

Load stored evidence ledger first.

Fetch historical web data only if:
- evidence is missing;
- stored provenance is insufficient;
- a source changed/corrected;
- the user requests independent re-verification.

### User asks for current price-dependent Profit View

Reuse stored causal/economic state.

Fetch current price.

Recompute recognition / Profit View from the current price without re-fetching old company history unless stale evidence requires it.

---

## 12. Cross-domain separation

Each domain owns its own state.

Do not mix stock state, astrology state, numerical-magic state, or future-domain state into one undifferentiated memory file.

Cross-domain correspondence should reference state objects by stable IDs.

Example:

```text
stock entity: US_XNAS_RARE
astrology corporate chart entity: CORP_ULTRAGENYX_2010_04_22
correspondence record: links those identities without merging their evidence ledgers
```

This prevents an experimental domain from silently contaminating an active domain's state.

---

## 13. Authority and invalidation

Stored state is a cache of previously processed evidence.

It is never final authority.

If a current primary source contradicts stored state:

```text
NEW PRIMARY EVIDENCE
-> append correction event
-> invalidate / supersede affected fact
-> recompute derived state
-> preserve old record for audit
```

Never silently overwrite history.

---

## 14. Backend roadmap

### Phase 1 — repository-backed reference implementation

Good for:
- schema development;
- auditability;
- tens to hundreds of entities;
- low/moderate update frequency;
- cross-chat persistence through Git.

### Phase 2 — indexed live store

Move operational state to SQLite or Postgres/Supabase when:
- the catalog reaches hundreds/thousands of entities;
- batch refresh becomes common;
- writes become frequent;
- filtering/sorting across all entities becomes expensive;
- multiple agents/chats may update state concurrently.

Keep schemas, rules, migrations, and periodic checkpoint exports in the repository.

### Phase 3 — scheduled delta ingestion

Add source adapters that implement:

```text
fetch_since(cursor)
normalize()
deduplicate()
append()
recompute()
schedule_next_refresh()
```

Do not build a broad scraper before the state contract is stable.

---

## 15. Core rule

> **Persistent domain state should make Xyool cheaper, faster, and more consistent without making it stale. Load first, refresh selectively, preserve provenance, append changes, preserve deep analyses losslessly, and never confuse cached state with authority.**
