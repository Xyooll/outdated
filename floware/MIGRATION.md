# Floware Migration Plan

Status: **ACTIVE / INCREMENTAL**

Xyool is moving from Markdown-first + software runtime toward **Floware-first + bounded software**.

This migration should not create unnecessary rewrites.

## Phase 1 — Authority shift — ACTIVE

- make `floware/` canonical;
- add domain `flows/`;
- route Start Here through Floware;
- stop adding new nodes;
- stop defaulting to Python for reasoning;
- require software escalation.

## Phase 2 — Wrap existing intelligence — ACTIVE

Existing canonical methods remain in `skills/`.

Flows reference them instead of duplicating their detail.

Examples:
- stock mandatory sequence → `company-analysis.flow.md`;
- payoff work → `payoff-ranking.flow.md`;
- RLE → `core/learning.flow.md`;
- correspondence → `core/correspondence.flow.md`.

## Phase 3 — Software inventory — DEFERRED UNTIL NEEDED

Do not spend effort rewriting working code solely for architectural cleanliness.

When a Floware contract, domain binding, schema, or software component is materially changed, route the migration through:
`meta/pipeline-integrity.flow.md`

Pipeline Integrity invokes Patching, Sequencing, Mapping, Domain Configurer, and Audit as required so migration implications are discovered instead of handled ad hoc.

When a software component is touched, classify it:

```text
HARD_LIMIT
EXACT_COMPUTATION
PERSISTENCE
INTERFACE
AUTOMATION_WITH_PROVEN_VALUE
LEGACY_COMPATIBILITY
UNJUSTIFIED_REASONING_CODE
```

Only the last category becomes a removal/migration candidate by default.

## Phase 4 — Selective retirement

For any migration patch, preserve historical records and explicitly classify each affected surface as:
- updated;
- migrated;
- verified unchanged;
- historical immutable;
- superseded;
- blocked.

Retire software only when:
- equivalent Floware behavior is stable;
- no hard-limit dependency remains;
- removal does not destroy valuable state/history/interfaces;
- the maintenance benefit is real.

## No big-bang rewrite

Floware adoption must itself follow the effectiveness rule.

> **Do not create a large migration project if leaving a stable software component alone is cheaper and safer.**

The architectural change is primarily about **where new intelligence goes from now on**.
