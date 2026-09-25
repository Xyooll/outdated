# Xyool — Repository Status and Branch Authority

Last reviewed: **2026-09-25**  
Status: **CANONICAL BRANCH GUIDE**

## Project identity

**Xyool is an AI-native, multi-domain reasoning and learning system. Floware is its reasoning and execution architecture.**

Core rule:

> **Use Floware for intelligence. Use software for certainty.**

System-lineage contract:
`SYSTEM-LINEAGE.md`

## Canonical integrated system

`main` is the single canonical integrated Xyool branch.

After the 2026-09-25 lineage migration:

~~~text
GitHub default branch
= main
= current integrated Xyool
~~~

The former pattern in which `main` was only a landing/legacy branch while a feature branch represented the real current architecture is retired.

## Scoped subordinate lineage

`lineage/user-concepts` is canonical **only** for:

`memory/user-concepts/`

It preserves the user's concept/thought history independently of feature-branch topology.

It has no authority to redefine the integrated system outside that scope.

## All other branches

Unless explicitly added to `SYSTEM-LINEAGE.md` as a scoped canonical lineage, other branches are one of:

- **PROPOSAL** — unmerged candidate work;
- **MIRROR** — convenience copy of canonical material;
- **HISTORICAL** — backup, superseded, frozen, or recovery history.

A branch may contain newer or more specialized work without becoming current system authority.

## Current focus and domain status

Current system architecture is Floware-first.

The stock market remains a registered domain with saved goals and validation history.

Astrology and numerical-magic remain experimental domains; integrated files on `main` define their current Xyool representation, while experimental status still limits claim authority.

## Reading order

1. `SYSTEM-LINEAGE.md` — resolve system authority.
2. `XYOOL-START-HERE.md` — operating entrypoint.
3. `floware/GLOSSARY.md` — canonical Floware semantics.
4. `floware/README.md` — architecture overview.
5. `floware/REPOSITORY-MAP.md` and `floware/REGISTRY.md` — ownership/routing.
6. `floware/FLOW-CONTRACT.md` and `floware/PIPE-CONTRACT.md`.
7. Load the domain, evidence, state, and supporting software required by the objective.

For User Concept Memory, follow the scoped lineage defined by `SYSTEM-LINEAGE.md` and `memory/user-concepts/LINEAGE.md`.

## Review and handoff rules

For current-state work:
- use `main`;
- record the exact `main` commit when reproducibility matters;
- resolve scoped subordinate lineages only for their declared scope;
- never treat a feature/domain branch as current merely because it is newer;
- surface unmerged branch differences as proposals/deltas;
- preserve historical research and frozen evidence at their recorded versions.

For historical reconstruction:
- explicitly select the historical branch/commit/artifact;
- do not present it as current state.

## Integration rule

A system-affecting branch change becomes current only after:

~~~text
PROPOSAL
→ impact mapping / reconciliation
→ verification
→ Audit when material
→ integration into main
→ CURRENT
~~~

## Final rule

> **There is one canonical integrated answer to "what is Xyool now?": `main`.**
