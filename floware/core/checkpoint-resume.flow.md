# FLOW — Checkpoint Resume

FLOW ID: CORE-CHECKPOINT-RESUME
STATUS: CANDIDATE / OPT-IN / INDEPENDENT AUDIT PENDING
DOMAIN: core / domain-neutral
JOB: Checkpoint Resume
AUTHORITY: record and route only; existing domain, action, and promotion boundaries apply
PARENT GOALPOST: [Continuity v1](../../research/system-tests/floware-continuity-v1-2026-09-24/GOALPOST.md); individual runs retain their own goalpost
UPSTREAM FLOWS: Xyool Execution; Run Record
DOWNSTREAM FLOWS: Evidence Refresh; Pipeline Integrity; Run Record
INBOUND PIPES: CONT-03, CONT-07 in [continuity Plumbing](../continuity/PLUMBING.md)
OUTBOUND PIPES: CONT-04, CONT-05 in [continuity Plumbing](../continuity/PLUMBING.md)
SOFTWARE DEPENDENCIES: existing authorized storage tools for durable writes; no runtime engine introduced

## GOAL

Recover interrupted work from a known checkpoint while revalidating current inputs, contracts, and permissions.

## GOALPOST

Produce a justified reuse/refresh/block disposition for each required stage; return control to existing Sequencing without replaying uncertain external effects.

## INPUT STATE

Checkpoint ID/revision, current repository and evidence heads, current time, active user objective/permissions, interrupted operations and receipts.

## EVIDENCE

Read the actual persisted checkpoint and referenced inputs. Saved authority describes history; current session authorization and governing policy determine present permission.

## PROCESS

Resolve the checkpoint and parent chain; compare goalpost, domain binding, Flow/Pipe contracts, source heads, freshness and authority. Classify every relevant difference. Send material changes through Evidence Refresh. Treat interrupted actions with unknown outcomes as BLOCKED pending receipt reconciliation; do not blindly retry. Supply the reconciled candidate to Pipeline Integrity, which invokes Sequencing for readiness and new epochs. Record the resumed checkpoint.

## GATES

No unresolved identity or source-version mismatch; no reused stale gate; all action outcomes reconciled before retry; independent audit still required wherever the governing Pipeline requires it.

## ADAPTATION

If nothing material changed, reuse outputs with explicit provenance. If only one branch changed, refresh that branch and its dependents. Missing permissions may block action while allowing separately authorized analysis.

## BOUNDARIES

Does not own execution order, renew permission, infer successful side effects, or retroactively edit the old checkpoint.

## FAIL-CLOSED CONDITIONS

Missing checkpoint, ambiguous latest head, unsupported schema/contract change, unknown material freshness, or unresolved action outcome blocks affected work.

## OUTPUT STATE

checkpoint reference; current heads; differences; reused/refresh/blocked stage lists with reasons; action reconciliation; candidate manifest for Pipeline Integrity; no independent READY or VERIFIED grant.

## LEARNING HOOK

Resume misses route to Learning with the original and recovered state references.

## SOFTWARE / HARD-LIMIT BOUNDARY

Persistence read-back, revision comparison, transactions, and external action receipts require existing deterministic tooling. Exactly-once external execution is not supplied by this Flow.

## COMPLEXITY RULE

Resume the smallest justified subgraph; an old checkpoint alone is not grounds to rerun everything.
