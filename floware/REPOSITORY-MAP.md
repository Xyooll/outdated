# Xyool Repository Map — Floware-First

Status: **CANONICAL REPOSITORY AUTHORITY MAP**

## Canonical branch authority

Repository-wide authority is defined by:
`../SYSTEM-LINEAGE.md`

~~~text
main
= canonical integrated Xyool

lineage/user-concepts
= subordinate canonical authority only for memory/user-concepts/

all other branches
= proposal / mirror / historical until reconciled
~~~

Directory authority below is interpreted inside the canonical integrated system on `main`. A feature branch containing a newer copy of a directory does not gain canonical authority from recency alone.

## Primary operating architecture

```text
XYOOL-START-HERE.md
        ↓
floware/
        ↓
domains/<domain>/flows/
        ↓
skills/ + research/ + state
        ↓
software only where justified
```

## Directory roles

### `floware/` — PRIMARY EXECUTION AUTHORITY

Contains Xyool's AI-executable reasoning architecture and governed Plumbing:
- routing;
- goalposts;
- evidence-to-state;
- research;
- development;
- learning;
- correspondence;
- software escalation;
- core execution;
- domain establishment and per-function readiness before Meta configuration;
- canonical Pipe contracts and Flow-to-Flow connection semantics;
- observation/trigger routing and finite resource allocation before execution.

New cross-domain behavior belongs here.

### `floware/meta/` — META-LAYER INTEGRITY / COMPOSITION

Contains general Flows whose primary objects are other Flows, mappings, domain configurations, transitions, or architecture-level relationships.

Current canonical Meta architecture:

Composite:
- `pipeline-integrity.flow.md` — end-to-end pipeline integrity coordinator.

Primitive Meta Flows:
- `mapping.flow.md` — explicit structural/representational mapping;
- `domain-configurer.flow.md` — domain-to-Floware configuration and capability binding;
- `audit.flow.md` — independent pipeline/handoff, contract, provenance, boundary, state, mapping, configuration, sequencing, patch, and learning-integrity audit;
- `patching.flow.md` — dependency-aware propagation of authorized changes across contracts, mappings, domains, schemas, state, tests, registries, and compatibility surfaces;
- `sequencing.flow.md` — dependency/order authority for composed operations, including parallel branches, barriers, readiness, and re-entry;
- `failure.flow.md` — candidate failure classification/disposition ownership without repair authority;
- `promotion-lifecycle.flow.md` — candidate evidence-backed lifecycle authority without Evaluation/Audit/Patching duplication.

Meta Flows remain subject to the normal Flow contract. Meta status does not grant superior authority.

### `domains/<domain>/` — DOMAIN-NATIVE AUTHORITY

Contains the native domain meaning, function/rule substrate, validation, reusable domain library, state, and domain Flows.

Before Meta configuration, new/expanded scope must satisfy `floware/DOMAIN-CONTRACT.md` through `core/domain-establishment.flow.md`.

### `domains/<domain>/library/` — REUSABLE DOMAIN KNOWLEDGE MEMORY

Contains distilled, source-traceable, validation-aware domain knowledge and indexes canonical domain artifacts so future work can reuse what Xyool has already established.

It is not live state, user-concept memory, or raw research history.

Canonical contract:
`floware/DOMAIN-LIBRARY-CONTRACT.md`

### `domains/<domain>/flows/` — DOMAIN EXECUTION AUTHORITY

Contains domain-specific executable flows.

New domain reasoning belongs here.

### `skills/` — METHODS / KNOWLEDGE

Skills explain methodologies, taxonomies, evidence rules, and specialized reasoning.

They support Flows.

They are not a separate execution system.

### `memory/` — HUMAN-ORIGINATED CONCEPT MEMORY

Contains:
- user concepts;
- rationale;
- philosophies;
- terminology choices;
- intellectual-development history;
- living synthesis for future recall.

This memory class uses the scoped subordinate lineage:

`lineage/user-concepts` → `memory/user-concepts/`

The copy on `main` is an integration mirror/snapshot. Current User Concept history resolves from the scoped lineage defined in `SYSTEM-LINEAGE.md` and `memory/user-concepts/LINEAGE.md`.

This is distinct from domain state, research evidence, and software/session memory.

Canonical capture Flow:
`floware/core/user-concept-memory.flow.md`

### `research/` — EVIDENCE / EXPERIMENT HISTORY

Contains freezes, outcomes, audits, development pools, validation records, rejected methods, and regressions.

Research constrains Floware. It does not silently become authority.

### `domains/*/state/` and persistent state artifacts — STATE / MEMORY

Contain current and historical domain state with provenance.

State informs Flows. State is not itself authority.

### `correspondence/` — CROSS-DOMAIN TRANSFER

Contains explicit structural mappings and target-domain tests.

### `nodes/` — RETAINED LEGACY RUNTIME COMPATIBILITY

Original Markdown behavioral nodes are retained only because parked software still reads them.

Do not add new nodes and do not treat them as reasoning authority.

Canonical reasoning has moved to Floware.

### `agent/`, `scripts/`, `tests/`, `main.py` — RETAINED SOFTWARE SUPPORT

Existing deterministic/runtime implementation is currently parked in place for recoverability and future justified reuse. It is not active reasoning authority.

Do not add new reasoning here by default and do not delete it merely for architectural purity.

Retention/revival contract:
`../docs/retained-software.md`

New or reactivated software requires:
`floware/core/software-escalation.flow.md`

### `.github/` — REPOSITORY AUTOMATION

Automation is infrastructure, not intelligence.

CI should run only when its evidence value justifies its cost.

### `docs/` — CONTRACTS / CONTINUITY / REFERENCE

Supporting documentation not itself a primary Flow unless registered.

## Precedence

For reasoning/execution behavior:

```text
platform/system authority
→ user-authorized objective
→ Floware core
→ applicable Meta Flow integrity/configuration constraints
→ active domain Flow
→ canonical domain/skill method
→ current evidence/state
→ research hypotheses
→ software implementation detail
```

Software implementation does not override a newer canonical Flow unless a hard safety/permission boundary requires it.

## New capability routing

```text
NEW CAPABILITY
→ define goalpost if material
→ query Domain Library for existing knowledge
→ if new/expanded domain scope: establish native function under Core Domain Establishment
→ create/modify Flow
→ test with evidence
→ register Flow
→ software escalation only if Flow proves insufficient
```

## Core rule

> **The repository should make the adaptive reasoning visible before the implementation machinery.**

## Optional continuity extension

[continuity/](continuity/START-HERE.md) owns the opt-in Pipeline manifest, connection wrappers, templates and synthetic example. New reasoning contracts remain in core/. Per-run records belong in the authorized run store and reference canonical domain state. Existing domain stores and historical research retain their authority. This extension is candidate-only pending independent audit.


### Retired active policy surface

The former `controls/` Markdown policy layer has been absorbed into Floware ownership: natural-language routing remains with Xyool Execution, resource/model/token policy lives in Resource Allocation, and verification policy remains with owning Flow checks + Evaluation/Pipeline Integrity/Audit. The old controls files are removed from the active tree; Git history preserves them.
