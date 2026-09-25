# User Concept — Degree Limit Is a Resource Bound

Date: **2026-09-23**  
Status: **ACTIVE / CORE ARCHITECTURE PHILOSOPHY**

## USER-STATED CONCEPT

The degrees-of-separation limit is not being used because four degrees is believed to be the best or complete model.

The limit exists because research resources are finite.

Without a boundary, recursive character/story research can continue indefinitely, especially if every discovered entity has its own relationships and if those relationships must be refreshed with real-time data.

Maintaining such a graph would require much greater:
- research capacity;
- storage;
- retrieval;
- source refresh;
- context;
- compute/tool usage;
- provenance management.

## CANONICAL PRINCIPLE

> **The current degree cap is an operational resource horizon, not a natural limit of the story.**

## CURRENT POLICY

```text
CURRENT MAX ABSOLUTE DEGREE = 4
POLICY REASON = RESOURCE_BOUND
```

This can change in the future.

If Xyool gains greater capacity, the same architecture should support:
- larger fixed horizons;
- adaptive horizons;
- continuous graph expansion;
- more real-time relationship maintenance.

## MEMORY CONSEQUENCE

When research stops at the degree boundary, preserve:
- known beyond-boundary pointers;
- unresolved branches;
- reason research stopped;
- provenance;
- expansion-ready state.

Do not encode a boundary as evidence that no further material relationships exist.

## SYSTEM CONSEQUENCE

Updated:
- `recursive-character-story.flow.md`
- `story-memory.flow.md`
- `character-memory-reroot.flow.md`

The architecture is now explicitly **bounded by current capacity and designed for future expansion**.
