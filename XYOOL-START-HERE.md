# Xyool — START HERE

Status: **FLOWARE-FIRST ENTRYPOINT**

## Canonical system and current focus

**Canonical integrated branch: `main`.**

Resolve repository authority through:
`SYSTEM-LINEAGE.md`

Feature/domain/fix/experiment branches are not independent current systems. They remain proposals, mirrors, or historical branches until reconciled into `main`.

The current focus is **Floware architecture**. Stock-domain goals below remain saved domain goals for when stock work resumes.

Start with the [canonical Floware glossary](floware/GLOSSARY.md), then follow the load order below and the [Floware overview](floware/README.md). Glossary definitions are semantic contracts; short summaries do not replace them.

Xyool is an AI-native, goal-directed reasoning system.

The repository is operated **Floware-first**:

```text
GOAL
  ↓
FLOWARE
adaptive reasoning / routing / evidence / learning
  ↓
DOMAIN FLOWS
domain-specific interpretation and decisions
  ↓
SKILLS + RESEARCH + STATE
methods, evidence, history, current state
  ↓
SOFTWARE
only where deterministic guarantees are justified
```

Core law:

> **Use Floware for intelligence. Use software for certainty.**

## Mandatory load order

For material Xyool work, first read the [canonical glossary](floware/GLOSSARY.md) to preserve the meanings of Flow, Pipe, Pipeline, and Plumbing.

1. Read `floware/README.md`.
2. Read `floware/REGISTRY.md`.
3. Read `floware/core/xyool-execution.flow.md`.
4. For material multi-Flow/Pipeline work, load `floware/PIPE-CONTRACT.md` so connections are treated as first-class governed Pipes.
5. If this is development work, load `floware/core/goalpost.flow.md` and the active frozen goalpost.
6. Identify the domain from `domains/README.md` / `domains/registry.yaml`.
7. If the domain is new, materially changed, or lacks a validated Floware binding, load `floware/meta/domain-configurer.flow.md` and `floware/meta/mapping.flow.md`.
8. Load the domain manifest and its `flows/` directory.
9. Load only the skills, evidence, state, and correspondence needed by the active Flow.
10. For material multi-Flow or cross-layer work, load `floware/meta/pipeline-integrity.flow.md`; it coordinates Mapping, Domain Configurer, Sequencing, Patching, Audit, and—on this candidate branch—Failure classification and Promotion/Lifecycle when applicable.
11. Use primitive Meta Flows directly only when the task is narrowly scoped to mapping, configuration, sequencing, patching, failure classification, lifecycle promotion/demotion, or independent audit.
12. Use `floware/core/software-escalation.flow.md` before creating or materially expanding software.

Repository authority map:
`floware/REPOSITORY-MAP.md`

Software exception policy:
`floware/SOFTWARE-BOUNDARY.md`

## Registered stock domain and saved goal

Current focus is Floware architecture. The stock domain retains its existing registry status and the following saved goal for when stock work resumes.

Registered development and validation domain:

`domains/stock-market/DOMAIN.md`

Active stock flows:

- `domains/stock-market/flows/company-analysis.flow.md`
- `domains/stock-market/flows/payoff-ranking.flow.md`

Current frozen stock-development goal:

> **Finish payoff ranking before moving to capital sizing.**

Goalpost:
`research/system-tests/stock-payoff-ranking-goalpost-v1-2026-09-22.md`

## Multi-domain architecture

Xyool remains larger than markets.

```text
XYOOL CORE FLOWARE
        ↓
META MAPPING + DOMAIN CONFIGURER
        ↓
PATCHING WHEN ARCHITECTURE / BINDINGS CHANGE
        ↓
VALIDATED DOMAIN CONFIGURATION + SPECIALIZED ADAPTERS AS NEEDED
        ↓
DOMAIN FLOWS
        ↓
LIVE OBJECTS / STATE / EVIDENCE
        ↓
OUTCOME / MISS
        ↓
LEARNING
        ↓
CORRESPONDENCE
        ↓
TARGET-DOMAIN FLOW + LOCAL VALIDATION
```

Cross-domain work also loads:

- `skills/xyool/00-03-META-ARCHITECTURE-PRIMER.md`
- `skills/xyool/00-04-DOMAIN-CORRESPONDENCE-HOWTO.md`
- `floware/meta/pipeline-integrity.flow.md` for end-to-end multi-Flow integrity
- primitive Meta Flows (`mapping`, `domain-configurer`, `sequencing`, `patching`, `audit`) as called by Pipeline Integrity or for narrowly scoped Meta work
- `floware/core/correspondence.flow.md`
- `correspondence/README.md`

Transfer structures and questions before conclusions. Do not transfer local thresholds, coefficients, actions, or calibrations without target-domain evidence.

## Experimental domains

Registered experimental domains currently include:

- astrology → `domains/astrology/flows/astrology-analysis.flow.md`
- numerical-magic → `domains/numerical-magic/flows/numerical-analysis.flow.md`

Their existing domain procedures remain valid supporting specifications, but the Floware wrapper is now the operating entrypoint.

Experimental status limits claim authority; it does not create a separate execution architecture.

## Skills

`skills/` contains methodologies and domain knowledge.

Skills are loaded **by Flows** when they materially improve the current objective.

They are not a competing execution architecture.

For stock-market work, the detailed mandatory gate specification remains:
`skills/xyool/00-mandatory-run-sequence.md`

Its Floware wrapper is:
`domains/stock-market/flows/company-analysis.flow.md`

## User concept memory

Material user-originated ideas, rationale, philosophies, naming choices, and design intuitions use the scoped canonical lineage:

`lineage/user-concepts` → `memory/user-concepts/`

Canonical lineage contract:
`memory/user-concepts/LINEAGE.md`

Canonical capture Flow:
`floware/core/user-concept-memory.flow.md`

Copies of User Concept Memory on `main` or proposal branches are mirrors/snapshots. Current concept history resolves from `lineage/user-concepts`; a reproducible run should pin the exact canonical memory commit it consumed.

Preserve the user's stated thought separately from assistant interpretation.

## Research and state

`research/` contains frozen evidence, experiments, outcomes, audits, development pools, regressions, and validation history.

`domains/*/state/` and state contracts hold persistent domain state.

Evidence and state constrain Floware. They do not silently create authority.

## Software

Existing:
- `agent/`
- `scripts/`
- `tests/`
- `main.py`
- `.github/`

are retained/parked supporting software/infrastructure, not the current reasoning architecture.

Do not expand or reactivate them by default. See `docs/retained-software.md`.

Before new software:

```text
CAN FLOWARE HANDLE IT?
        ↓
YES → KEEP IT AS FLOWARE

NO / HARD LIMIT / EXACTNESS / SCALE NEED
        ↓
SOFTWARE ESCALATION FLOW
        ↓
MINIMUM JUSTIFIED SOFTWARE
```

Do not rewrite stable existing software merely for architectural purity.

## Nodes

`nodes/` is retained only as a compatibility dependency of the parked runtime.

Do not add new nodes or use them as reasoning authority.

Canonical replacements live under `floware/`.

## Goalpost discipline

For major development:

```text
FREEZE GOAL
→ TRY METHOD
→ METHOD FAILS? CHANGE METHOD
→ SAME GOAL
→ CLEAR SUCCESS GATES
→ CLOSE GOAL
→ ONLY THEN OPEN NEXT GOAL
```

Xyool seeks **effectiveness within reason, not perfection**.

Canonical governance:
`skills/xyool/00-07-GOALPOST-EFFECTIVENESS-GOVERNANCE.md`

## Final operating rule

> **The Flow is the program.**

> **The repository should expose the reasoning path before the implementation machinery.**

> **Software must justify why Floware is insufficient.**


## Observation, attention, failure and lifecycle

When work is event-driven or Xyool has competing work:
- `floware/core/observation-trigger.flow.md` decides whether a new observation should wake/queue work;
- `floware/core/resource-allocation.flow.md` chooses the bounded active set;
- `floware/meta/sequencing.flow.md` still owns dependency-safe order after selection.

Material pipeline failures route to `floware/meta/failure.flow.md`. Candidate authority transitions route to `floware/meta/promotion-lifecycle.flow.md` after the required evidence/Audit path.
