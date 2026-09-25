# META FLOW — Promotion / Lifecycle

FLOW ID: META-PROMOTION-LIFECYCLE
STATUS: **CANDIDATE / VERIFICATION_PENDING**
DOMAIN: meta
JOB: govern evidence-backed candidate promotion, demotion, retirement, supersession, and rollback without collapsing Evaluation, Audit, or Patching into lifecycle authority
AUTHORITY: lifecycle-state decision within an already authorized capability scope; no external/action authority and no authority to manufacture validation evidence
PARENT GOALPOST: ../../research/system-tests/floware-consolidation-v1-2026-09-24/GOALPOST.md
UPSTREAM FLOWS: Pipeline Integrity, Evaluation, Learning, Development, Audit through Pipeline Integrity
DOWNSTREAM FLOWS: Pipeline Integrity; Patching through existing Pipeline Integrity route when a lifecycle decision requires current-contract/state changes
INBOUND PIPES: PLUMBING.md#pipe-meta-integrity-promotion
OUTBOUND PIPES: PLUMBING.md#pipe-meta-promotion-integrity
SOFTWARE DEPENDENCIES: none

## GOAL

Assign the highest lifecycle state justified by the candidate's evidence and governing promotion contract, and lower that state when evidence no longer supports it.

Core law:

> **Evidence earns authority; labels do not create evidence.**

## GOALPOST

A lifecycle decision is sufficient when:
- candidate identity/version is frozen;
- governing promotion criteria are known;
- Evaluation evidence is distinguished from Audit findings;
- required independence/holdout/prospective evidence is present or explicitly absent;
- prior lifecycle state is known;
- the proposed transition is legal;
- rollback/demotion evidence is considered;
- external action authority remains separate;
- required Patching is routed rather than silently applied.

## INPUT STATE

- candidate/component identity and version;
- current lifecycle state;
- claimed scope/authority;
- evaluation evidence;
- audit result where required;
- regression/prospective evidence;
- blockers/known failures;
- governing domain/core promotion standard;
- current goalpost.

## EVIDENCE

Use:
- frozen Evaluation records;
- independent Audit result where required;
- repeatability/prospective/holdout evidence;
- regression history;
- operational demonstration evidence;
- failure/rollback records;
- domain-specific release/promotion standards.

A successful local demonstration is not operational verification.

## LIFECYCLE STATES

Default generic states:

~~~text
PROPOSED
RESEARCH
SHADOW
CANARY
PROMOTION_READY
PROMOTED
DEMOTED
ROLLED_BACK
RETIRED
SUPERSEDED
BLOCKED
~~~

Domain contracts may use stricter or mapped states.

These lifecycle states do not replace:
- Pipeline statuses;
- Flow STATUS;
- Continuity maturity annotations;
- external execution authorization.

## PROCESS

~~~text
LOAD CANDIDATE + CURRENT LIFECYCLE
→ LOAD GOVERNING PROMOTION CRITERIA
→ LOAD EVALUATION EVIDENCE
→ LOAD REQUIRED INDEPENDENT AUDIT
→ CHECK REGRESSION / HOLDOUT / OPERATIONAL EVIDENCE
→ CHECK KNOWN FAILURES / INVALIDATION
→ DETERMINE HIGHEST EARNED LEGAL STATE
→ COMPARE TO CURRENT STATE
→ IF TRANSITION CHANGES CURRENT CONTRACT/ROUTING:
      RETURN PATCH_REQUIRED
→ RETURN LIFECYCLE DECISION TO PIPELINE INTEGRITY
→ PRESERVE PRIOR EVIDENCE AND STATE HISTORY
~~~

## GATES

Promotion may not exceed the weakest required evidence gate.

At minimum:
- no promotion from guided demonstration alone when independent evidence is required;
- no promotion after material Audit FAIL/BLOCKED;
- no silent reuse of consumed validation as untouched evidence;
- no automatic CODE/MODEL/PROMPT-policy authority merely because old software supports such statuses;
- no promotion that grants financial/external execution authority.

## ADAPTATION

A candidate may remain useful in SHADOW/RESEARCH while blocked from promotion.

New contradictory evidence may DEMOTE, ROLL_BACK, RETIRE, or SUPERSEDE without deleting prior successful evidence.

## BOUNDARIES

Promotion/Lifecycle does not:
- design experiments;
- score candidate performance;
- perform independent Audit;
- patch implementation/contracts itself;
- choose deployment sequencing;
- grant user/system permissions;
- redefine a domain's success metric.

## FAIL-CLOSED CONDITIONS

Return BLOCKED when:
- candidate/version identity is ambiguous;
- governing promotion criteria are missing;
- required Evaluation/Audit evidence is absent;
- evidence provenance/holdout status is unclear;
- requested transition would broaden authority beyond the candidate's scope.

## OUTPUT STATE

~~~text
CANDIDATE:
VERSION:
PRIOR LIFECYCLE:
EVIDENCE BASIS:
AUDIT BASIS:
BLOCKERS:
EARNED LIFECYCLE:
TRANSITION:
PATCH REQUIRED:
ROLLBACK / DEMOTION CONDITION:
AUTHORITY AFTER TRANSITION:
~~~

## LEARNING HOOK

False promotions, delayed demotions, and lifecycle rules that repeatedly misclassify evidence become Learning inputs. Historical lifecycle decisions remain preserved.

## SOFTWARE / HARD-LIMIT BOUNDARY

NONE — FLOWARE SUFFICIENT

Future deployment systems may enforce lifecycle gates, but the semantic lifecycle decision remains Floware.

## COMPLEXITY RULE

Do not create lifecycle ceremony for an ordinary output that is not seeking durable authority. Use this Flow only when a candidate/component may change promotion, demotion, retirement, supersession, or rollback state.
