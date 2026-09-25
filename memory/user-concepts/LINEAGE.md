# User Concept Canonical Lineage

Status: **CANONICAL MEMORY LINEAGE CONTRACT**

## Authority

Canonical branch: `lineage/user-concepts`  
Canonical root: `memory/user-concepts/`  
Canonical index: `memory/user-concepts/LEDGER.md`  
Derived synthesis: `memory/user-concepts/CURRENT-SYNTHESIS.md`

Only the User Concept Memory surfaces named by this contract are authoritative on this branch. Other repository files present because of branch ancestry are incidental and do not gain architectural authority from being on the lineage branch.

## Core rule

> **There is one thought history. Working branches inherit it; they do not fork it.**

A branch-local `memory/user-concepts/` directory may exist for readability or historical reasons, but it is a mirror/snapshot unless the branch is `lineage/user-concepts`.

## Read rule

For current User Concept Memory:

1. resolve `lineage/user-concepts`;
2. read its `LEDGER.md`;
3. load the dated concept entries needed for the task;
4. use `CURRENT-SYNTHESIS.md` only as a derived convenience layer.

Do not infer "current thought memory" from the active feature/domain branch.

For reproducible work, record the exact canonical lineage commit consumed.

## Write rule

New material user concepts, refinements, corrections, and concept-status changes must originate on `lineage/user-concepts`.

Working/domain branches may:
- read the canonical branch;
- pin a canonical commit for a frozen run;
- synchronize/cherry-pick canonical memory for local readability;
- carry historical mirrors.

They must not create an alternate authoritative ledger.

## Reconciliation rule

When historical branch drift is found:

~~~text
DISCOVER BRANCH-LOCAL MEMORY
→ identify entries absent from canonical lineage
→ preserve source branch / commit provenance
→ deduplicate semantically
→ append/refine canonical lineage
→ verify linked concept files exist
→ mark the branch-local copy non-authoritative
~~~

Do not discard a valid concept merely because it was captured on the wrong branch.

Do not allow "newest branch wins" to replace reconciliation.

## Inheritance rule

Downstream branches inherit by **reference first**.

A local mirror is optional and may lag.

Therefore:

~~~text
CANONICAL LINEAGE
= authority

BRANCH MIRROR
= convenience / historical snapshot
~~~

If a branch mirror differs from canonical, canonical wins for current memory unless an unreconciled branch-local concept is discovered. That divergence is a reconciliation event, not a second truth.

## Merge/conflict rule

A merge conflict in User Concept Memory is resolved against the canonical lineage contract:

- preserve both genuinely distinct concepts;
- preserve earlier wording/history;
- treat later corrections as refinements, not erasures;
- never drop a concept only to make branches match;
- update the canonical ledger first;
- downstream copies synchronize afterward.

## Derived synthesis rule

`CURRENT-SYNTHESIS.md` is derived and may be refreshed from canonical entries.

It must never outrank:
1. direct user wording;
2. dated canonical concept entries;
3. canonical ledger history.

## Audit rule

A User Concept Memory write is valid only when:
- target lineage is canonical;
- authorship labels remain clear;
- linked entry exists;
- ledger and entry agree;
- historical wording is not silently rewritten;
- branch-local divergence has been reconciled or explicitly marked unresolved.

## Migration provenance

The one-time branch-drift reconciliation that established this lineage is recorded in:
`memory/user-concepts/RECONCILIATION-2026-09-25.md`

## Relationship to Git branches

Git branches are development topology.

They are not memory authority.

The canonical thought lineage is intentionally independent of whichever feature/domain branch is currently active.
