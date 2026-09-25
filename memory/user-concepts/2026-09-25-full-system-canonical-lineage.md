# User Concept — Remove Canonical Ambiguity from the Full System

Date: **2026-09-25**  
Status: **ACTIVE / CORE SYSTEM ARCHITECTURE**

## USER-STATED

> "We should get rid of the ambiguity from the full system"

## CONCEPT

Xyool should not require a reader, agent, or future collaborator to infer which branch, subsystem copy, or locally newer artifact represents the current system.

There should be one canonical integrated system state.

Working rule:

~~~text
MAIN
= canonical integrated Xyool

SCOPED CANONICAL LINEAGE
= authority only for an explicitly named data class

FEATURE / DOMAIN / FIX / EXPERIMENT BRANCH
= proposed change, not current system authority

BACKUP / SUPERSEDED BRANCH
= historical recovery surface
~~~

A branch being newer, more specialized, or more recently edited does not make it canonical.

## SYSTEM CONSEQUENCE

Establish a repository-wide System Lineage contract that:
- makes `main` the canonical integrated Xyool;
- removes the old split between landing branch and "real/current" development branch;
- defines explicit branch authority states;
- permits subordinate canonical lineages only when their scope is named and bounded;
- requires all system-affecting changes to reconcile into `main` before they become current system truth;
- treats branch-local differences as proposals or unreconciled deltas rather than competing truths;
- requires audits to resolve canonical branch + commit before making current-state claims;
- preserves historical branches and research without allowing them to silently override current contracts.

## CORE RULE

> **One integrated system, one canonical answer to "what is Xyool now?"**

Specialized lineages may exist for bounded persistence needs, but they must declare their scope and may not compete with the integrated system outside that scope.

## RELATED

- `2026-09-25-canonical-thought-lineage.md`
- repository root `SYSTEM-LINEAGE.md`
- `../../floware/REPOSITORY-MAP.md`
- `../../floware/meta/patching.flow.md`
- `../../floware/meta/audit.flow.md`
