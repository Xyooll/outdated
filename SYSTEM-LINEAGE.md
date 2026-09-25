# Xyool System Lineage

Status: **CANONICAL SYSTEM AUTHORITY CONTRACT**  
Effective: **2026-09-25**

## Core rule

> **One integrated system, one canonical answer to "what is Xyool now?"**

The canonical integrated Xyool is the head of:

`main`

A branch being newer, more specialized, more active, or more recently edited does **not** make it current system authority.

## Authority classes

Only these authority states are valid for Git branches:

~~~text
CANONICAL
SUBORDINATE_CANONICAL
PROPOSAL
MIRROR
HISTORICAL
~~~

### CANONICAL

`main`

Authority:
- integrated current Xyool architecture;
- Floware contracts and registry;
- integrated domain contracts/configurations/flows;
- current repository routing;
- current supporting-software state;
- current integrated research/state pointers;
- current system-level policies.

There must be exactly one CANONICAL integrated system branch.

### SUBORDINATE_CANONICAL

A branch may be authoritative only for a narrowly declared persistence class that cannot safely use ordinary feature-branch integration semantics.

Current scoped lineage:

`lineage/user-concepts`

Authority scope:
- `memory/user-concepts/`;
- the canonical User Concept ledger/history;
- direct user-concept refinements and corrections.

It has **no authority** to redefine Floware, domains, software, research status, or the integrated system outside that scope.

A subordinate lineage must declare:
- exact branch;
- exact path/scope;
- read rule;
- write rule;
- reconciliation rule;
- relationship to `main`.

No branch becomes SUBORDINATE_CANONICAL by convention or age.

### PROPOSAL

Feature/domain/fix/experiment branches containing work not yet reconciled into `main`.

Examples:
- `feature/*`;
- `fix/*`;
- `codex/*`;
- `quant-layer-v1`;
- `xyool-*`;
- future task branches.

Their contents may be valid, advanced, tested, or newer than `main`, but they are **candidate changes**, not current integrated system truth.

### MIRROR

A convenience copy of canonical material on another branch.

A mirror may lag.

A mirror never outranks its canonical source.

### HISTORICAL

Backup, superseded, frozen, or recovery branches.

Historical branches preserve provenance and rollback/reconstruction value.

They do not participate in current-state resolution unless explicitly selected for historical reconstruction.

## Canonical resolution

For any question equivalent to:

> What is Xyool now?

resolve in this order:

~~~text
1. main
2. exact commit on main when reproducibility matters
3. applicable scoped subordinate lineage only for its declared scope
4. frozen research/state artifact referenced by canonical contracts
~~~

Do not select a feature/domain branch because it appears newer.

## Specialized-lineage resolution

For User Concept Memory:

~~~text
main
→ discovers scope from this contract / repository map
→ lineage/user-concepts
→ exact canonical memory commit when reproducibility matters
~~~

The branch is authoritative only for the declared memory scope.

Its non-memory files are incidental branch ancestry and have no canonical authority.

## Change promotion rule

A system-affecting change becomes current only after reconciliation into `main`.

~~~text
PROPOSAL BRANCH
→ identify intended change
→ Patching impact graph
→ reconcile canonical contracts / domain bindings / state / tests
→ required verification
→ independent Audit when material
→ integrate into main
→ only then CURRENT SYSTEM
~~~

Local branch success does not equal system promotion.

## Cross-branch conflict rule

If `main` and another branch disagree:

~~~text
MAIN
= current integrated authority

OTHER BRANCH
= proposal / mirror / historical evidence
~~~

The disagreement must be surfaced as a delta.

Do not silently choose whichever file is newer.

If the branch contains a valid missing change:
- preserve its provenance;
- reconcile the change into `main`;
- verify affected surfaces;
- then treat the integrated result as current.

## Scoped-lineage conflict rule

If `main` contains a mirror of a SUBORDINATE_CANONICAL scope and the two differ:

~~~text
SCOPED LINEAGE
= authority inside declared scope

MAIN COPY
= mirror / integration snapshot
~~~

That difference is synchronization state, not competing truth.

For system reasoning outside the scoped lineage, `main` remains authoritative.

## Research and frozen evidence

Research artifacts may be authoritative evidence for the experiment/run they record.

They are not current system contracts merely because they are immutable or later-dated.

Use:

~~~text
CURRENT CONTRACT / ROUTING
→ main

HISTORICAL EXPERIMENT FACT
→ frozen research artifact at its recorded commit

CURRENT USER-CONCEPT HISTORY
→ lineage/user-concepts
~~~

## Domain rule

Domains do not own separate canonical Git branches.

Current integrated domain authority lives under `main:domains/<domain>/...`.

A domain feature branch is a proposal until merged/reconciled into `main`.

A domain may have local state/history contracts, but branch topology must not create a second current Xyool.

## Branch creation rule

New branches must have one of these purposes:

~~~text
PROPOSAL
MIRROR
HISTORICAL / BACKUP
explicitly approved SUBORDINATE_CANONICAL
~~~

Default = PROPOSAL.

Branch names do not grant authority.

## Branch retirement rule

After integration:
- preserve the branch when its provenance/recovery value matters;
- otherwise it may be deleted by normal repository maintenance;
- either way, its unmerged contents do not remain silently authoritative.

## Audit rule

Before a current-state audit or architectural claim:

1. resolve `main`;
2. record the commit being audited;
3. identify any applicable subordinate lineage;
4. verify the target is not being sourced from a proposal/mirror by mistake;
5. surface unreconciled branch deltas when materially relevant.

A current-state claim is BLOCKED when canonical identity cannot be established.

## Patching rule

Patching must classify branch-local deltas explicitly:

~~~text
INTEGRATE
SUPERSEDE
PRESERVE_HISTORICAL
MIRROR_ONLY
REJECT
BLOCKED
~~~

No material delta may disappear merely because another branch was chosen as baseline.

## Relationship to default branch

The GitHub default branch and the canonical integrated system branch must be the same branch.

Current required state:

`default branch = main = canonical integrated Xyool`

The previous pattern:

~~~text
main = landing / older system
feature branch = real current system
~~~

is retired.

## Final invariant

> **Branches may diverge in work. Authority may not diverge in meaning.**
