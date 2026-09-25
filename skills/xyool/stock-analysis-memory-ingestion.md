# Xyool — Stock Analysis Memory Ingestion

Status: **CANONICAL PERSISTENCE / LOSSLESS-TO-OPERATIONAL MEMORY CONTRACT**

## Purpose

A deep stock analysis contains more information than the compact live snapshot should carry.

Xyool therefore persists two linked layers:

```text
LOSSLESS ANALYSIS ARCHIVE
        ↓ audited extraction
OPERATIONAL STOCK STATE
```

The archive preserves the complete decision-useful analysis artifact. The operational layer remains compact and structured for fast future retrieval.

This prevents analysis intelligence from disappearing merely because it does not fit a current-state field.

## Core pipeline

```text
DEEP STOCK ANALYSIS
→ build ingestion bundle
→ enumerate material conclusions
→ assign a persistence disposition to every material conclusion
→ validate references / identities / duplicate evidence
→ archive the complete analysis text
→ append new evidence
→ append timer revisions
→ patch current snapshot
→ recompute active timer IDs from latest timer revisions
→ update index pointer
→ write completeness audit
```

The deterministic ingestor does **not** infer investment meaning from prose. The analysis layer creates the structured bundle; code verifies and persists it.

## Lossless archive

Path:

```text
domains/stock-market/state/analyses/<entity_id>/<analysis_id>.json
```

The archive stores:
- stable entity identity;
- analysis ID and as-of time;
- complete `analysis_text`;
- source list;
- every material conclusion;
- every declared persistence disposition;
- evidence events;
- timer records;
- snapshot patch;
- before/after state version;
- operational files written;
- completeness audit;
- deterministic source-bundle hash.

Do not store hidden chain-of-thought. Preserve the finished analysis artifact, evidence, calculations, conclusions, rationale needed for audit, rejected hypotheses, and unresolved questions.

## Archive provenance

Every analysis archive must distinguish **native lossless capture** from **historical reconstruction**.

### Native archive

```text
archive_origin = NATIVE_LOSSLESS
lossless_original = true
```

Use this for analyses created after the ingestion pipeline is active. The complete finished analysis artifact is captured at the time of analysis and then extracted into operational state.

### Reconstructed historical archive

```text
archive_origin = RECONSTRUCTED_EXISTING_GIT_STATE
lossless_original = false
```

Use this only to migrate pre-existing Git-backed stock memory.

A reconstructed archive may preserve:
- the pre-migration snapshot;
- evidence ledger;
- timer history;
- already-persisted dependency/repricing objects;
- material conclusions that can be recovered from those stored objects.

It must also carry:
- `reconstructed_at`;
- `historical_limitations[]`;
- an explicit statement that unstored original analysis detail cannot be recovered.

Do **not** infer or manufacture missing historical research merely to make an old archive look lossless.

A later genuine deep analysis may replace the snapshot's latest-analysis pointer with a `NATIVE_LOSSLESS` archive while the reconstructed archive remains in history.

Historical migration must preserve the factual `as_of` date of the stock state. The migration timestamp is metadata, not new company evidence.

Unchanged evidence and timer ledgers must remain byte-for-byte untouched. Referencing old ledger records from a reconstructed archive does not justify reformatting or re-appending them.

---

## Material-conclusion completeness rule

Every conclusion marked `material: true` must have at least one declared disposition.

Allowed disposition types:

```text
EVIDENCE
SNAPSHOT_FIELD
DEPENDENCY_NODE
DEPENDENCY_EDGE
TIMER
UNRESOLVED_QUESTION
REJECTED_HYPOTHESIS
NON_PERSISTENT
```

`NON_PERSISTENT` requires an explicit reason.

A material conclusion with no disposition causes ingestion to **FAIL CLOSED**.

The point is not to force every sentence into operational state. The point is to make every deliberate omission visible and auditable.

## Story-memory extraction

A completed Narrative Thesis / Story Flow is a first-class durable memory object.

After a material story build:

```text
LOSSLESS FINISHED STORY
→ preserve inside the analysis archive
→ extract a compact story_memory head
→ point back to the lossless story artifact
→ future runs load story_memory before research
→ refresh only stale/due character branches
```

The story-memory head should preserve:
- compressed current story;
- thesis;
- source authority / gaps;
- story closure;
- four-degree depth budget;
- key characters and their degree/remaining budget;
- primary conflict/bottleneck;
- likely next state / conditional window;
- invalidation;
- next refresh targets.

The operational story is not allowed to sever provenance from the lossless archive/evidence.

Rule:

> **Do not rebuild a known story from zero when an audited story memory exists. Load it first and update deltas.**

## Operational extraction

The ingestor may update only approved stock-memory roots:

```text
current_state
dependency_graph
repricing_sensitivity
research_shadow_state
research_trial_context
active_timer_ids
latest_material_evidence_ids
unresolved_questions
source_cursors
story_memory
completeness_status
```

Stable identity, schema identity and unrelated top-level state cannot be silently rewritten through the ingestion bundle.

## Evidence behavior

Evidence remains append-only.

Incoming evidence must preserve:
- stable `event_id`;
- stable fingerprint;
- domain/entity identity.

Rules:
- identical already-stored evidence is idempotent;
- the same event ID with different content is rejected;
- the same fingerprint under a different event ID is rejected;
- corrections should use a new evidence event and explicit supersession/invalidation.

## Timer behavior

Timer history is append-only.

A later record with the same `timer_id` is a timer revision. Readers resolve the latest revision by default while `history=True` exposes the full sequence.

This allows:

```text
ACTIVE
→ DELAYED
→ ACTIVE RESET
→ REALIZED / CLOSED
```

without deleting the historical timer state.

## Snapshot behavior

After successful ingestion:
- `state_version` increments;
- `as_of` advances;
- active timer IDs are derived from latest timer revisions;
- new material evidence IDs are linked;
- `analysis_memory` points to the latest analysis archive and records whether it is native-lossless or reconstructed;
- the catalog index stores the latest analysis ID/path and PASS state;
- if the ingestion materially changes a rank-driving field, any prior derived `research_rank` is marked `STALE` until the applicable rerank is recomputed.

Rank-driving fields include at least Quality/capital eligibility, TTC/date-window state, primary gate/frontier, recognition, repricing sensitivity, profitability transmission, normalized earnings bridge, sector regime, return-failure state, profit view, and shareholder-capture/dilution state. Rank freshness must preserve the analysis/state basis used to compute the rank.

### Shadow-state rank firewall

`research_shadow_state` is persistent but **not rank-driving** while its method status remains experimental/shadow.

Changes in:
- analyst revisions / PEAD state;
- residual or sector-relative momentum;
- execution/capacity diagnostics;
- short-borrow feasibility;
- factor-exposure diagnostics;

must not mark `research_rank` stale and must not alter canonical TTC output unless the current analysis belongs to a pre-registered augmented trial arm that explicitly grants those fields decision authority.

A later canonical promotion must first update the method contract and method version; only then can the promoted fields enter rank invalidation.

## Runtime tools

`stock_analysis_memory_plan`
- validates the bundle;
- verifies material-conclusion coverage;
- performs no writes.

`stock_analysis_memory_ingest`
- persists the archive and operational extraction;
- modification action;
- idempotent for the exact same bundle/analysis ID.

`stock_analysis_memory_audit`
- verifies latest/specified archive status;
- checks completeness status and snapshot pointer.

## Required use

Use this pipeline when:
- a new stock receives a full/deep Xyool analysis;
- a refresh materially changes the thesis, dependency graph, shareholder-capture state, or catalyst architecture;
- a substantial research pass produces conclusions that would be expensive to reconstruct later.

A tiny factual refresh that creates no material analytical change may update evidence/state directly under the normal domain-state delta process.

## Failure conditions

Fail closed if:
- stable entity identity does not match;
- lossless analysis text is absent;
- a material conclusion is unmapped;
- a disposition points to a nonexistent evidence/timer/dependency target;
- evidence IDs/fingerprints conflict;
- the snapshot patch attempts to mutate forbidden roots;
- the same analysis ID already exists with different content.

## Core rule

> **Deep analysis must be preserved twice: once losslessly for future understanding, and once structurally for fast operational use. No material conclusion may disappear between those layers without an explicit disposition.**
