# Floware Meta — Plumbing

Status: **ACTIVE / CANONICAL META PLUMBING V1**

Parent contracts:
- `../PIPE-CONTRACT.md`
- `../FLOW-CONTRACT.md`
- `pipeline-integrity.flow.md`

## Purpose

Define the high-risk Pipes connecting Xyool Execution, Pipeline Integrity, primitive Meta Flows, and independent Audit.

The composite coordinates the primitive Meta Flows.

The Pipes below prevent that coordination from becoming an untyped set of calls.

---

## PIPE-META-EXECUTION-INTEGRITY

~~~text
FROM POINTER:
  CORE-XYOOL-EXECUTION / material multi-Flow objective

TO POINTER:
  META-PIPELINE-INTEGRITY / INPUT STATE

WRAPPER:
  preserve user-authorized objective / goalpost
  preserve domain identity and authority boundaries
  supply selected Flows/current state where known

AUTHORITY:
  routing → pipeline integrity coordination only

FAILURE:
  missing objective/domain/authority boundary = BLOCKED
~~~

---

## PIPE-META-INTEGRITY-MAPPING

~~~text
FROM POINTER:
  META-PIPELINE-INTEGRITY / unresolved representation compatibility

TO POINTER:
  META-MAPPING

CONDITION:
  source/target representations are not already natively compatible

WRAPPER:
  Mapping determines representational alignment only
  it does not prove empirical cross-domain transfer
  information loss / incompatibility remains explicit

RETURN:
  Mapping result returns to Pipeline Integrity / owning Pipe wrapper
~~~

---

## PIPE-META-INTEGRITY-CONFIGURER

~~~text
FROM POINTER:
  META-PIPELINE-INTEGRITY / new or materially changed domain binding need

TO POINTER:
  META-DOMAIN-CONFIGURER

CONDITION:
  domain semantics/configuration are new, changed, or unresolved

WRAPPER:
  configure domain to Floware
  do not reshape core Floware into the domain
  explicit Mapping required at material boundaries

RETURN:
  validated / blocked domain configuration returns to Pipeline Integrity
~~~

---

## PIPE-META-INTEGRITY-PATCHING

~~~text
FROM POINTER:
  META-PIPELINE-INTEGRITY / authorized multi-surface change

TO POINTER:
  META-PATCHING

WRAPPER:
  underlying source change must already be authorized
  Patching discovers complete impact graph
  historical immutable records preserved

AUTHORITY:
  change propagation only
  no authority to invent architecture

RETURN:
  patch set / status returns to Pipeline Integrity
~~~

---

## PIPE-META-PATCHING-SEQUENCING

~~~text
FROM POINTER:
  META-PATCHING / non-trivial patch impact graph

TO POINTER:
  META-SEQUENCING

WRAPPER:
  impact graph defines what must change
  Sequencing defines dependency-safe operational order
  independent surfaces may parallelize
  dependent surfaces may not

RETURN:
  operation graph / ready frontier returns to patch execution
~~~

---

## PIPE-META-INTEGRITY-SEQUENCING

~~~text
FROM POINTER:
  META-PIPELINE-INTEGRITY / selected material stages + Pipes

TO POINTER:
  META-SEQUENCING

WRAPPER:
  durable Pipe contracts are ordering truth
  Sequencing derives current readiness/order/barriers from Pipe properties
  domain-mandated gates remain authoritative

RETURN:
  operation graph / ready frontier / barriers / invalidation state
~~~

---

## PIPE-META-CANDIDATE-AUDIT

~~~text
FROM POINTER:
  META-PIPELINE-INTEGRITY / VERIFICATION_PENDING candidate
  or primitive Meta candidate requiring independent validation

TO POINTER:
  META-AUDIT

GATE:
  candidate work applied/composed enough to audit
  final VERIFIED status not yet granted

WRAPPER:
  Audit receives frozen candidate view + governing contracts/evidence
  Audit may inspect but not silently repair/redefine

AUTHORITY:
  candidate status → independent verification only

RETURN:
  PASS / PASS_WITH_NOTES / WARN / FAIL / BLOCKED
~~~

---

## PIPE-META-AUDIT-INTEGRITY

~~~text
FROM POINTER:
  META-AUDIT / audit record

TO POINTER:
  META-PIPELINE-INTEGRITY / terminal verification decision

WRAPPER:
  PASS / PASS_WITH_NOTES may permit VERIFIED if all other terminal gates pass
  FAIL / BLOCKED prevents VERIFIED
  remediation routes to owning Flow/primitive
  Audit does not perform the repair itself

SEMANTIC INVARIANT:
  verification result ≠ repair
~~~

---

## Verification handshake

Canonical Pipe sequence:

~~~text
PIPELINE / PATCH CANDIDATE
→ VERIFICATION_PENDING
→ PIPE-META-CANDIDATE-AUDIT
→ META-AUDIT
→ PIPE-META-AUDIT-INTEGRITY
→ VERIFIED
   or
   BLOCKED / PARTIAL / FAILED
~~~

This prevents the circular dependency:

~~~text
VERIFIED → Audit → VERIFIED
~~~

## Current scope

This manifest covers the high-risk Meta coordination Pipes.

Lower-risk local calls may remain implicit if they are:
- lossless;
- authority-neutral;
- version-insensitive;
- semantically obvious;
- not independently invalidated.

Promote them to named Pipes when those assumptions stop being true.

## Optional continuity connections

[Continuity Plumbing](../continuity/PLUMBING.md) defines opt-in candidate Pipes CONT-01 through CONT-10. They feed the existing Meta Pipes above; they do not replace this manifest or its audit handshake. Per-run live state records activation and readiness; candidate registration alone activates nothing.


---

## PIPE-META-INTEGRITY-FAILURE

~~~text
FROM POINTER:
  META-PIPELINE-INTEGRITY / material FAILED, BLOCKED, or unresolved failure state requiring classification

TO POINTER:
  META-FAILURE / INPUT STATE

WRAPPER:
  preserve objective / goalpost
  preserve failed object + expected contract
  preserve evidence/provenance + execution epoch
  preserve existing authority boundary

AUTHORITY:
  pipeline failure state → classification/disposition only

FAILURE:
  missing failed object/contract/evidence = BLOCKED_UNKNOWN
~~~

---

## PIPE-META-FAILURE-INTEGRITY

~~~text
FROM POINTER:
  META-FAILURE / OUTPUT STATE

TO POINTER:
  META-PIPELINE-INTEGRITY / remediation owner + re-entry decision

SEMANTIC INVARIANTS:
  classification ≠ repair
  disposition ≠ permission to bypass the governing contract
  unresolved cause remains UNKNOWN

AUTHORITY:
  failure classification → pipeline remediation routing only

FAILURE:
  owner/disposition broadens authority or loses failure evidence = BLOCKED
~~~

---

## PIPE-META-FAILURE-LEARNING

~~~text
FROM POINTER:
  META-FAILURE / generalizable learning or regression candidate

TO POINTER:
  CORE-LEARNING / INPUT STATE

GATE:
  failure is material and potentially reusable beyond the single incident

SEMANTIC INVARIANTS:
  historical failure record remains unchanged
  learning candidate is not proof of a system defect until evaluated
  case-specific repair does not become a general rule automatically

AUTHORITY:
  failure evidence → learning candidate only
~~~

---

## PIPE-META-INTEGRITY-PROMOTION

~~~text
FROM POINTER:
  META-PIPELINE-INTEGRITY / lifecycle candidate + evaluation/audit evidence

TO POINTER:
  META-PROMOTION-LIFECYCLE / INPUT STATE

GATE:
  lifecycle transition is part of the authorized objective
  governing promotion criteria are known

SEMANTIC INVARIANTS:
  VERIFIED pipeline/evaluation evidence does not automatically imply PROMOTED
  promotion state does not grant external/action authority
  consumed evidence cannot be relabeled untouched

AUTHORITY:
  verified evidence package → lifecycle decision only

FAILURE:
  missing candidate version/promotion contract/required evidence = BLOCKED
~~~

---

## PIPE-META-PROMOTION-INTEGRITY

~~~text
FROM POINTER:
  META-PROMOTION-LIFECYCLE / lifecycle decision

TO POINTER:
  META-PIPELINE-INTEGRITY / terminal state or patch-required route

SEMANTIC INVARIANTS:
  lifecycle decision preserves evidence history
  PATCH_REQUIRED returns through existing Patching route
  Audit remains independent from Promotion

AUTHORITY:
  earned lifecycle state → pipeline routing only

FAILURE:
  lifecycle decision exceeds governing authority/evidence = BLOCKED
~~~


---

## PIPE-META-LEARNING-INTEGRITY

~~~text
FROM POINTER:
  CORE-LEARNING / validated lesson + candidate change requiring system/domain lifecycle consideration

TO POINTER:
  META-PIPELINE-INTEGRITY / candidate change pipeline

SEMANTIC INVARIANTS:
  lesson/candidate ≠ promoted rule
  source evidence and holdout status preserved
  requested authority remains bounded by the owning domain/core contract

AUTHORITY:
  learning candidate → governed evaluation/patch/promotion routing only

FAILURE:
  candidate lacks evidence/version/authority boundary = BLOCKED
~~~
