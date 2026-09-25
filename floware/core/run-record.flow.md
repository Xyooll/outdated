# FLOW — Run Record

FLOW ID: CORE-RUN-RECORD
STATUS: CANDIDATE / OPT-IN / INDEPENDENT AUDIT PENDING
DOMAIN: core / domain-neutral
JOB: Run Record
AUTHORITY: record and route only; existing domain, action, and promotion boundaries apply
PARENT GOALPOST: [Continuity v1](../../research/system-tests/floware-continuity-v1-2026-09-24/GOALPOST.md); individual runs retain their own goalpost
UPSTREAM FLOWS: Pipeline Integrity; owning execution context
DOWNSTREAM FLOWS: Pipeline Integrity; Checkpoint Resume; Evaluation
INBOUND PIPES: CONT-01 in [continuity Plumbing](../continuity/PLUMBING.md)
OUTBOUND PIPES: CONT-02, CONT-07, CONT-08 in [continuity Plumbing](../continuity/PLUMBING.md)
SOFTWARE DEPENDENCIES: existing authorized storage tools for durable writes; no runtime engine introduced

## GOAL

Preserve a reconstructable account of a material run without making a new source of domain truth.

## GOALPOST

The declared checkpoint is recoverable by read-back, identifies the exact consumed versions and unresolved gates, and retains prior records.

## INPUT STATE

Run ID, objective/goalpost, Pipeline manifest, repository commit, execution epoch, stage outputs, evidence pointers, authority scope, and expected prior record head.

## EVIDENCE

Use observed tool results and source revisions. An intended write is not evidence of persistence. Source as-of, observation time, and record-write time remain separate.

## PROCESS

Use the [record template](../continuity/RUN-RECORD.template.md). Capture a checkpoint at a material handoff, interruption, evidence change, or terminal candidate. Preserve references to canonical domain state instead of copying it into a competing store. Read the expected prior head; append a uniquely identified record through the authorized persistence tool; read it back and compare contents. Report the location/revision and any failure. Only an actual compare-and-swap or transaction can establish atomic concurrent safety.

## GATES

Run, epoch, objective, contract versions and evidence versions resolve; required Pipe live states are recorded; no success inferred from a blocked stage; persistence receipt and read-back agree.

## ADAPTATION

Single short answers may omit durable records. Use this Flow when continuity or reproducibility matters. Record failures as well as successes. Omit secrets; preserve a recoverable authorized reference instead.

## BOUNDARIES

A checkpoint neither grants authority nor verifies a Pipeline. Do not overwrite historical records or label an uncommitted local file durably saved. Do not serialize independent tasks solely for logging; serialize competing writes to the same head.

## FAIL-CLOSED CONDITIONS

Unknown prior head, collision, conflicting writer, missing required provenance, or failed read-back: return BLOCKED for durable checkpoint acceptance. Preserve the attempted record separately; the last accepted head remains authoritative.

## OUTPUT STATE

record_id; run_id; epoch; storage_status (RECORDED / BLOCKED); expected_parent; persisted_revision; readback_result; per-stage/Pipe status; blockers. Pipeline status is separately owned by Pipeline Integrity.

## LEARNING HOOK

Lost provenance, falsely reported persistence, and overwritten history route through the existing Learning Flow.

## SOFTWARE / HARD-LIMIT BOUNDARY

Durable storage and atomic concurrent writes require deterministic tools. This Flow specifies their use; it does not implement crash-safe transactions. If unavailable, leave the corresponding guarantee BLOCKED.

## COMPLEXITY RULE

Capture the minimum material state once and reference it. Do not log every reasoning token.
