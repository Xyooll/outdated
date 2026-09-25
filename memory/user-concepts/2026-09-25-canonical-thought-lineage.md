# User Concept — One Canonical Thought Lineage

Date: **2026-09-25**  
Status: **ACTIVE / CORE MEMORY ARCHITECTURE**

## USER-STATED

> "Architecturally, I think we should eventually eliminate that ambiguity. Your thought ledger should have one canonical lineage, with downstream branches inheriting it rather than each branch quietly drifting into its own memory version. I think we need to handle that now"

## CONCEPT

User Concept Memory must have one authoritative history.

A feature, domain, experiment, backup, or working branch may carry a local copy for convenience, but that copy must never become a competing source of truth.

Canonical shape:

~~~text
USER THOUGHT
→ CANONICAL USER-CONCEPT LINEAGE
→ APPEND / REFINE
→ CANONICAL COMMIT
→ DOWNSTREAM BRANCHES CONSUME / MIRROR
~~~

Not:

~~~text
BRANCH A LEDGER
BRANCH B LEDGER
BRANCH C LEDGER
→ silently diverging histories
~~~

## SYSTEM CONSEQUENCE

Xyool establishes:

- canonical branch: `lineage/user-concepts`;
- canonical root: `memory/user-concepts/`;
- canonical index: `memory/user-concepts/LEDGER.md`;
- canonical lineage contract: `memory/user-concepts/LINEAGE.md`;
- branch-local memory copies as non-authoritative mirrors/snapshots;
- canonical-first read/write behavior in the User Concept Memory Flow;
- explicit reconciliation when historical branch drift is discovered;
- exact canonical commit capture when a reproducible run needs a frozen memory view.

## INHERITANCE RULE

Downstream branches inherit concept memory by reference to the canonical lineage.

They may merge/cherry-pick/synchronize canonical memory for local readability, but new user-concept history must originate in the canonical lineage rather than on a feature branch.

## RECOVERY RULE

If a valid user concept was previously written only on a downstream branch:

~~~text
DISCOVER DIVERGENCE
→ PRESERVE ORIGINAL BRANCH / COMMIT PROVENANCE
→ RECONCILE INTO CANONICAL LINEAGE
→ DEDUPLICATE WITHOUT ERASING HISTORY
→ MARK LOCAL COPY NON-AUTHORITATIVE
~~~

## WHY IT MATTERS

The thought ledger is meant to preserve intellectual continuity across the whole Xyool project.

If branch topology can fork that memory silently, then the repository can no longer answer a basic question reliably:

> What did the user actually think, and how did that thought evolve?

One canonical lineage restores that answer.
