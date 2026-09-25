# FLOW — User Concept Memory

FLOW ID: `CORE-USER-CONCEPT-MEMORY`  
STATUS: **ACTIVE / CANONICAL**  
DOMAIN: core  
JOB: preserve human-originated concepts and rationale  
AUTHORITY: memory/continuity only

## GOAL

Preserve material ideas expressed by the user so they can be:
- retrieved later;
- understood in their original context;
- connected to later architectural decisions;
- read by another person without access to the original conversation.

## TRIGGER

Consider capture when the user expresses a material:
- concept;
- philosophy;
- design principle;
- future thesis;
- naming decision;
- rationale;
- goal/finish definition;
- correction to how Xyool should think;
- worldview that materially affects the project;
- explanation of why a system should operate a certain way.

Do not capture every casual statement.

## INPUT STATE

- current user statement;
- surrounding conversational context;
- canonical lineage contract: `memory/user-concepts/LINEAGE.md`;
- canonical branch head: `lineage/user-concepts`;
- canonical `memory/user-concepts/LEDGER.md` from that branch;
- related canonical concept entries if they exist;
- active working branch only as context, never as independent memory authority.

## PROCESS

```text
RESOLVE CANONICAL USER-CONCEPT LINEAGE
→ IDENTIFY MATERIAL CONCEPT
→ CHECK CANONICAL LEDGER FOR EXISTING RELATED CONCEPT
→ DETECT UNRECONCILED BRANCH-LOCAL DIVERGENCE
→ PRESERVE USER WORDING
→ EXTRACT CONCEPT MINIMALLY
→ SEPARATE USER STATEMENT FROM INTERPRETATION
→ RECORD RATIONALE ONLY WHEN SUPPORTED
→ RECORD SYSTEM CONSEQUENCE
→ LINK RELATED CONCEPTS
→ APPEND / REFINE ON `lineage/user-concepts` WITHOUT ERASING HISTORY
→ RECORD CANONICAL COMMIT FOR REPRODUCIBLE CONSUMERS WHEN MATERIAL
→ UPDATE SYNTHESIS ONLY IF MATERIAL
→ DOWNSTREAM BRANCHES CONSUME / MIRROR AFTER CANONICAL WRITE
```

## GATES

Before capture:
- Has `memory/user-concepts/LINEAGE.md` been resolved?
- Is the write target the canonical `lineage/user-concepts` branch?
- Is there any unreconciled branch-local concept that would make the current history ambiguous?
- Is this materially reusable or meaningful?
- Is authorship clear?
- Is the rationale supported by what the user said?
- Would a future reader understand the entry without the original chat?
- Is this a refinement of an existing concept rather than a new concept?

## AUTHORSHIP LABELS

Use:
- `USER-STATED`
- `ASSISTANT INTERPRETATION`
- `SYSTEM CONSEQUENCE`
- `OPEN QUESTION`

Never convert assistant inference into a user belief.

## PRIVACY BOUNDARY

Do not infer sensitive personal attributes from ordinary discussion.

Do not construct diagnoses, private relationship narratives, political profiles, or other speculative personal characterizations.

The purpose is intellectual continuity, not surveillance or psychological profiling.

## ADAPTATION

If the new thought:
- extends an old idea → add a refinement/link;
- contradicts an old idea → preserve both and mark the evolution;
- replaces an old term → mark the terminology transition;
- is uncertain → store as QUESTION / EVOLVING rather than fact.

## OUTPUT STATE

At minimum:
- canonical dated entry or refinement;
- canonical ledger index update;
- canonical commit/reference;
- status;
- relationship to prior concepts.

Branch-local copies are mirrors/snapshots only. They may lag without changing authority.

When enough material accumulates, update:
`memory/user-concepts/CURRENT-SYNTHESIS.md`

## LEARNING HOOK

Later user corrections are authoritative evidence about whether the stored interpretation was accurate.

Corrections should update interpretation while preserving the original historical record.

## CANONICAL LINEAGE / BRANCH RULE

Canonical contract:
`memory/user-concepts/LINEAGE.md`

Canonical branch:
`lineage/user-concepts`

Core law:

> **There is one thought history. Working branches inherit it; they do not fork it.**

If a valid concept is discovered only on a downstream branch, treat that as a reconciliation event:

```text
DISCOVER DIVERGENCE
→ preserve source branch / commit provenance
→ reconcile into canonical lineage
→ deduplicate without erasing history
→ mark local copy non-authoritative
```

Do not let the active feature/domain branch silently become memory authority.

## FAIL-CLOSED CONDITIONS

Return BLOCKED / RECONCILIATION_REQUIRED when:
- the canonical lineage cannot be resolved;
- the intended write target is not `lineage/user-concepts`;
- a branch-local ledger conflicts with canonical and the difference has not been reconciled;
- a referenced canonical concept entry is missing;
- authorship or historical wording cannot be preserved safely.

## SOFTWARE / HARD-LIMIT BOUNDARY

`NONE — FLOWARE SUFFICIENT`

Repository writes are persistence, not reasoning software.