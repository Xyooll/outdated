# Xyool

Xyool is an AI-native, multi-domain reasoning and learning architecture.

## Canonical system and current focus

**`main` is the canonical integrated Xyool.** The default branch and the current system are the same thing.

Repository-wide lineage/branch authority:
`SYSTEM-LINEAGE.md`

Other feature/domain/fix/experiment branches are proposals, mirrors, or historical surfaces until reconciled into `main`. The only current scoped subordinate lineage is `lineage/user-concepts`, authoritative solely for `memory/user-concepts/`.

Start with [System Lineage](SYSTEM-LINEAGE.md), then the [canonical Floware glossary](floware/GLOSSARY.md), [Start Here](XYOOL-START-HERE.md), and the [Floware overview](floware/README.md). Glossary definitions are semantic contracts; short summaries do not replace them.

## Floware-first architecture

Xyool's primary operating substrate is **Floware**: structured, state-aware, goal-directed procedural knowledge executed adaptively by AI.

```text
GOAL
  ↓
FLOWARE
intent / reasoning / planning / routing / audit
  ↓
DOMAIN FLOWS
local evidence / state / decisions
  ↓
SOFTWARE
exact computation / persistence / permissions / hard limits
  ↓
HARDWARE / EXTERNAL SYSTEMS
```

> **Use Floware for intelligence. Use software for certainty.**

Start here:
`XYOOL-START-HERE.md`

Then:
- `floware/README.md`
- `floware/REGISTRY.md`
- `floware/REPOSITORY-MAP.md`
- `floware/FLOW-CONTRACT.md`

## Repository layout

```text
floware/
  canonical AI-executable flows and routing

domains/<domain>/flows/
  domain-specific Floware

skills/
  methods, taxonomies, evidence models, domain doctrine

research/
  experiments, freezes, outcomes, audits, regressions

domains/*/state/
  persistent domain state

correspondence/
  controlled cross-domain transfer

nodes/
  legacy Markdown-node compatibility

agent/ scripts/ tests/ main.py
  retained/parked supporting software; not reasoning authority

.github/
  repository automation, not intelligence
```

## Development philosophy

New capability development follows:

```text
GOALPOST
→ FLOW
→ EVIDENCE
→ EXECUTE
→ OUTCOME
→ LEARN
→ IMPROVE FLOW
```

Not:

```text
IDEA
→ WRITE CODE
→ BUILD INFRASTRUCTURE
→ MAINTAIN INFRASTRUCTURE
```

Code is introduced only when a specific deterministic need earns its cost.

Use:
`floware/core/software-escalation.flow.md`

## Goalposts

Major development goals are frozen before optimization.

A failed approach changes the method, not the goal.

Xyool optimizes for:

> **Evidence-backed effectiveness within reason, using the least justified complexity, research, computation, latency, and maintenance.**

Canonical governance:
`skills/xyool/00-07-GOALPOST-EFFECTIVENESS-GOVERNANCE.md`

## Saved stock-domain goal

The stock market remains a registered development and validation domain. The following frozen goal applies when stock work resumes; current work focuses on Floware architecture.

Saved domain goal:
**finish the payoff-ranking architecture.**

Active Flow:
`domains/stock-market/flows/payoff-ranking.flow.md`

Frozen goalpost:
`research/system-tests/stock-payoff-ranking-goalpost-v1-2026-09-22.md`

Capital sizing is intentionally not the active goal yet.

## Retained software

Existing software is parked in place for recoverability and future justified reuse. It does not define current reasoning behavior.

> **New intelligence goes into Floware. Reactivate software only when a Flow reaches a deterministic/exactness/scale boundary that earns it.**

Retention/revival contract:
`docs/retained-software.md`

Migration policy:
`floware/MIGRATION.md`

## Core principles

- exact identity before inference;
- evidence and freshness before confidence;
- explicit causal state and transitions;
- fail closed on material unknowns;
- preserve failures;
- separate development evidence from untouched validation;
- correspondence transfers structure, not local calibration;
- every added layer must earn its complexity;
- stop when the frozen effectiveness gate is met;
- software is an exception, not the default home of reasoning.

## Security and authority

Floware does not waive permissions, security boundaries, financial controls, or other hard limits.

Adaptive reasoning may choose a path.

It may not override a non-negotiable constraint.

The detailed runtime/security control plane remains in:
`SYSTEM_INSTRUCTIONS.md`


## Current cross-cutting Flow ownership

Candidate consolidation Flows now make four previously scattered jobs explicit:
- Observation / Trigger — when a change deserves Xyool attention;
- Resource Allocation — what competing work receives finite attention;
- Failure — how a material failure is classified/routed without self-repair;
- Promotion / Lifecycle — what evidence-backed lifecycle authority a candidate has earned.

Stock Discovery Visibility is also a first-class domain Flow before Quality capital eligibility.
