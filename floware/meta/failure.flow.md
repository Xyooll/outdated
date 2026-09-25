# META FLOW — Failure

FLOW ID: META-FAILURE
STATUS: **CANDIDATE / VERIFICATION_PENDING**
DOMAIN: meta
JOB: classify material failures, assign the correct owning response, preserve failure evidence, and define re-entry/closure conditions without performing the repair itself
AUTHORITY: failure classification and disposition routing only; no authority to repair, patch, waive gates, alter goals, grant permissions, or declare verification
PARENT GOALPOST: ../../research/system-tests/floware-consolidation-v1-2026-09-24/GOALPOST.md
UPSTREAM FLOWS: Pipeline Integrity, Xyool Execution, Audit findings through Pipeline Integrity, owning core/domain Flows
DOWNSTREAM FLOWS: Pipeline Integrity, Learning; Patching/Sequencing/Audit only through their existing governed ownership paths
INBOUND PIPES: PLUMBING.md#pipe-meta-integrity-failure
OUTBOUND PIPES: PLUMBING.md#pipe-meta-failure-integrity, PLUMBING.md#pipe-meta-failure-learning
SOFTWARE DEPENDENCIES: none

## GOAL

Turn an observed failure into an auditable failure state with a correct owner, bounded disposition, and explicit re-entry condition.

Core law:

> **Failure is evidence about the system state, not permission to improvise a repair.**

## GOALPOST

A failure is sufficiently classified when:
- the failed object/stage/Pipe is identified;
- the failed requirement or expected state is explicit;
- observed evidence is preserved;
- scope and blast radius are bounded;
- the failure class is named;
- the owner of the next response is named;
- the allowed disposition is grounded in the governing contract;
- retry/re-entry conditions are explicit;
- learning/regression implications are recorded where material;
- unresolved cause remains UNKNOWN rather than guessed.

## INPUT STATE

At minimum:
- objective / goalpost;
- failing Flow/Pipe/stage/object;
- observed status/output;
- expected contract/gate;
- evidence/provenance;
- execution epoch/version where applicable;
- current authority;
- prior retries/remediations where relevant.

## EVIDENCE

Prefer:
- governing Flow/Pipe contract;
- Pipeline manifest/live Pipe state;
- audit finding;
- run record/checkpoint;
- tool/storage receipt where applicable;
- state/version provenance;
- prior regression/failure records.

Do not classify motive/root cause from symptoms alone.

## PROCESS

~~~text
RECEIVE MATERIAL FAILURE
→ FREEZE FAILURE EVIDENCE
→ IDENTIFY FAILED CONTRACT / EXPECTATION
→ BOUND AFFECTED SCOPE
→ CLASSIFY FAILURE
→ IDENTIFY CURRENT OWNER
→ SELECT ONLY CONTRACT-ALLOWED DISPOSITION
→ DEFINE RE-ENTRY / CLOSURE CONDITION
→ RETURN DISPOSITION TO PIPELINE / OWNER
→ IF FAILURE REVEALS GENERALIZABLE SYSTEM MISS:
      ROUTE LESSON CANDIDATE TO LEARNING
→ AFTER REMEDIATION:
      REQUIRE NORMAL VERIFICATION PATH
~~~

## FAILURE CLASSES

Use the narrowest supported class:

~~~text
EVIDENCE
IDENTITY
FRESHNESS
REPRESENTATION / MAPPING
PIPE / HANDOFF
SEQUENCING / DEPENDENCY
AUTHORITY / PERMISSION
STATE / PERSISTENCE
EXTERNAL EFFECT UNKNOWN
EXECUTION / TOOL
METHOD / QUESTION
CONTRACT / ARCHITECTURE
VALIDATION / AUDIT
RESOURCE / BUDGET
EXTERNAL DEPENDENCY
UNKNOWN
~~~

UNKNOWN is valid when evidence cannot discriminate.

## DISPOSITIONS

Possible dispositions include:

~~~text
BLOCK
RETRY
RE_ENTER
ROUTE_ALTERNATE
DEGRADE_WITH_WARNING
ROLLBACK
PATCH_REQUIRED
LEARNING_REQUIRED
REQUEST_EVIDENCE
ESCALATE_AUTHORITY
SUPERSEDE
ACCEPT_NOT_APPLICABLE
~~~

A disposition is not a universal permission. The governing Flow/Pipe/domain contract decides which are legal.

## GATES

Before returning a disposition:
- failure evidence is preserved;
- owner is explicit;
- no authority increase is implied;
- retry does not risk duplicating an unknown external effect;
- patching is not requested for a merely local transient error unless contract change is actually needed;
- learning is not used as a substitute for immediate remediation;
- Audit remains independent.

## ADAPTATION

If evidence shows several independent failures, emit separate failure records linked to one incident rather than forcing one root cause.

If a failure is downstream fallout, preserve the upstream primary failure and mark descendants as affected/invalidated.

## BOUNDARIES

Failure does not:
- repair the target;
- change the goalpost;
- select patch contents;
- decide sequencing order;
- validate its own remediation;
- grant execution/capital/security authority;
- erase failed evidence after success.

## FAIL-CLOSED CONDITIONS

Return BLOCKED/UNKNOWN when:
- failing object or governing contract cannot be identified;
- external effect status is uncertain and retry could duplicate it;
- owner/disposition would require invented authority;
- evidence cannot distinguish material competing causes.

## OUTPUT STATE

~~~text
FAILURE ID:
OBJECTIVE / GOALPOST:
FAILED OBJECT:
FAILED EXPECTATION:
OBSERVED STATE:
FAILURE CLASS:
SCOPE / AFFECTED OBJECTS:
EVIDENCE / PROVENANCE:
OWNER:
DISPOSITION:
RE-ENTRY CONDITION:
ROLLBACK CONDITION:
LEARNING CANDIDATE:
REGRESSION CANDIDATE:
STATUS:
~~~

## LEARNING HOOK

Repeated, avoidable, or architecture-level failures route a lesson candidate to CORE-LEARNING. The failure record itself remains evidence and may not be rewritten to make the later fix look historically correct.

## SOFTWARE / HARD-LIMIT BOUNDARY

NONE — FLOWARE SUFFICIENT

Future software may persist failure IDs or enforce retry idempotency, but it must not replace semantic failure classification.

## COMPLEXITY RULE

Use local governing failure behavior directly when the failure, owner, and safe disposition are already unambiguous. Invoke this Meta Flow when classification, cross-layer impact, retry safety, ownership, or learning implications are material.
