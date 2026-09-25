# Xyool Floware

Status: **PRIMARY OPERATING SUBSTRATE**

Floware is the default execution architecture for Xyool.

## Canonical system resolution

Repository authority is defined by `../SYSTEM-LINEAGE.md`.

Current integrated Floware is resolved from `main`. Floware files on feature/domain/fix branches are proposals or historical snapshots until reconciled into `main`.

The scoped `lineage/user-concepts` branch is canonical only for User Concept Memory and does not redefine Floware.

> **Use Floware for intelligence. Use software for certainty.**

Repository roles:

```text
floware/
  core AI-executable flows, routing, contracts, governance

floware/meta/
  meta-layer pipeline integrity plus primitive mapping, domain configuration, sequencing, patching, failure, promotion/lifecycle, and audit

domains/<domain>/flows/
  domain-specific Floware

skills/
  methods, evidence models, domain knowledge, and supporting doctrine used by flows

research/
  evidence, experiments, outcomes, regression history

correspondence/
  controlled cross-domain transfer

agent/ scripts/ tests/ main.py
  retained/parked supporting software; not reasoning authority
```

A Flow is an executable reasoning contract, not merely documentation.

Every material Flow defines:
- goal;
- goalpost;
- input state;
- authoritative evidence;
- process;
- gates;
- adaptation;
- boundaries;
- fail-closed conditions;
- output state;
- learning hook;
- software/hard-limit boundary.

Start with:
1. `GLOSSARY.md`
2. `FLOW-CONTRACT.md`
3. `DOMAIN-CONTRACT.md` when creating or materially expanding a domain
4. `DOMAIN-LIBRARY-CONTRACT.md` for reusable domain knowledge/memory
5. `REGISTRY.md`
5. `core/xyool-execution.flow.md`
6. `core/domain-establishment.flow.md` for new/expanded domain scope
7. `meta/pipeline-integrity.flow.md` when material multi-Flow end-to-end integrity is required; use primitive Meta Flows directly only when the task is specifically mapping, configuration, sequencing, patching, failure classification, lifecycle promotion, or audit.
6. the active domain's `flows/` directory.

Software may support a Flow, but it may not silently become the architecture.

Material architecture/system changes should use:
`meta/patching.flow.md`

so the source change, dependent surfaces, migrations, verification, and audit are tracked as one patch set.


## CI / software verification policy

Floware, research, and ordinary Markdown changes do not automatically run the software test suite.

Software CI is reserved for:
- software/runtime changes that match focused workflow paths;
- explicit manual verification when warranted.

This is intentional.

> **Verification effort should scale with the kind of thing that changed. A Flow change should be evaluated as a Flow before invoking software infrastructure.**


## Human concept memory

Material user-originated concepts route through:
`core/user-concept-memory.flow.md`

Durable archive:
`../memory/user-concepts/`


## Future Flow products

Flow productization is an explicit future research direction:

`FLOW-PRODUCT-MODEL.md`

Core thesis:

> **Better Flows may produce better use of AI capability, making validated Flows valuable digital products.**

This future direction does not supersede active domain goalposts.


## Relational Story architecture

Reusable cross-domain story/relationship architecture:

`core/relational-story.flow.md`

This architecture now composes:
- `core/character-system.flow.md` — reusable character identity, traits, archetypes, behavior and transformations;
- `core/story-reader.flow.md` — evidence-backed past → present reconstruction;
- `core/story-writer.flow.md` — conditional present → possible-future branches;
- `core/relational-story.flow.md` — the umbrella relational story orchestration.

The Relational Story core defines:
- selectable root/main character;
- reusable character memory;
- first-class relationship edges;
- local character webs;
- wrappers/pointers;
- root-relative story memory;
- re-rooting;
- evidence/source authority;
- bounded exploration under finite resources;
- change/miss audit.

Domains specialize the semantics rather than reimplementing the architecture.

## Optional continuity and evaluation

The [continuity walkthrough](continuity/START-HERE.md) introduces four candidate Flows for recorded execution, recovery, evidence changes and evaluation. They compose through existing Meta governance and remain opt-in pending independent audit. They add no runtime engine or automatic overhead to simple tasks.


## Attention and autonomy preparation

Two candidate core Flows define the reasoning side of future autonomy without requiring runtime software:
- `core/observation-trigger.flow.md` — decide whether a new observation/due condition should wake, queue, or be ignored;
- `core/resource-allocation.flow.md` — choose the bounded active work set before Sequencing determines dependency-safe order.

Connections are defined in `core/PLUMBING.md`.

Existing software is preserved under its current paths and governed by `../docs/retained-software.md`; it is not used as the architecture authority.


## Domain establishment

Domain work now has an explicit two-layer boundary:

~~~text
CORE DOMAIN ESTABLISHMENT
→ establishes native objects, rules, functions, evidence, state, outcomes, and per-function readiness

META DOMAIN CONFIGURER
→ binds only an established scope to reusable Floware contracts
~~~

A configured domain is not automatically established for every possible function.

Canonical contracts:
- `DOMAIN-CONTRACT.md`
- `core/domain-establishment.flow.md`
- `meta/domain-configurer.flow.md`


## Domain library / memory

Reusable domain knowledge is governed by:
- `DOMAIN-LIBRARY-CONTRACT.md`
- `core/domain-library.flow.md`

The intended research loop is:

~~~text
DOMAIN QUESTION
→ DOMAIN LIBRARY FIRST
→ reuse current source-traceable knowledge
→ research only missing / stale / contested parts
→ update canonical rules / evidence
→ write distilled reusable knowledge back
~~~

This is separate from:
- `memory/user-concepts/` — human-originated concepts/rationale;
- `domains/*/state/` — live/current domain state;
- `research/` — experiment/evidence history.

The Domain Library should improve Xyool's starting knowledge over time without disconnecting it from provenance or fresh external evidence.
