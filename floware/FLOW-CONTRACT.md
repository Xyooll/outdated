# Flow Contract

Status: **CANONICAL**

Every Xyool Flow should use this structure.

## Identity

```text
FLOW ID:
STATUS:
DOMAIN:
JOB:
AUTHORITY:
PARENT GOALPOST:
UPSTREAM FLOWS:
DOWNSTREAM FLOWS:
INBOUND PIPES: optional pointers to canonical Pipe contracts
OUTBOUND PIPES: optional pointers to canonical Pipe contracts
SOFTWARE DEPENDENCIES:
```

## Pipe / composition note

Canonical Pipe contract:
`PIPE-CONTRACT.md`

For material reusable connections, prefer explicit inbound/outbound Pipe pointers over repeatedly reconstructing the connection from prose.

`UPSTREAM FLOWS` and `DOWNSTREAM FLOWS` remain useful routing/discovery metadata and may be derived from the Plumbing. They do not replace the Pipe contract.

A Flow owns its reasoning contract.
A Pipe owns its connection contract.

## Composition / sequencing note

`UPSTREAM FLOWS`, `DOWNSTREAM FLOWS`, `PROCESS`, and `GATES` are inputs to:
`meta/sequencing.flow.md`

They do not imply that every Flow must execute as one rigid linear list.

When multiple Flows compose, Sequencing may derive:
- hard prerequisites;
- parallel branches;
- barriers;
- shared-state mutexes;
- re-entry/invalidation epochs.

A Flow should declare a hard ordering constraint only when correctness, authority, state integrity, or a domain contract requires it.

When a Flow participates in a material multi-Flow pipeline, its declared inputs, outputs, authority, version/state assumptions, and gates are also inputs to:
`meta/pipeline-integrity.flow.md`

The individual Flow may pass locally while the pipeline still fails at a Pipe.

## GOAL
State the capability or outcome this Flow is responsible for.

## GOALPOST
State what constitutes sufficient completion. Link the frozen goalpost when one exists.

## INPUT STATE
State what must already be known.

## EVIDENCE
Define authoritative evidence and freshness requirements.

## PROCESS
Describe the adaptive reasoning sequence. Use questions and state transitions rather than unnecessary fixed branching.

## GATES
Name the conditions that must be satisfied before advancing.

## ADAPTATION
Explain how the route may change when the state changes.

## BOUNDARIES
State what the Flow may not decide or alter.

## FAIL-CLOSED CONDITIONS
State when the Flow must stop, return UNKNOWN/BLOCKED, or request evidence.

## OUTPUT STATE
Define the minimum auditable output.

## LEARNING HOOK
Define what later evidence evaluates this Flow and what type of miss should feed recursive learning.

## SOFTWARE / HARD-LIMIT BOUNDARY
List only the parts that truly require deterministic enforcement, exact computation, persistence, transactions, security, or physical limits.

If none are required, write:

`NONE — FLOWARE SUFFICIENT`

## COMPLEXITY RULE

> **If a simpler Flow reaches the frozen effectiveness gate with materially similar reliability, prefer the simpler Flow.**
