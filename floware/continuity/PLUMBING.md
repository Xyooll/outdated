# Continuity Plumbing v1

Status: CANDIDATE / OPT-IN / VERIFICATION_PENDING
Parent: [Pipe contract](../PIPE-CONTRACT.md).
Owner: [Pipeline Integrity](../meta/pipeline-integrity.flow.md).
Activation: explicit selection of [Continuity v1](PIPELINE.md), never automatic for every task.

## Shared connection wrapper

Every Pipe below inherits these requirements and adds its row-specific gate.
Source/target contracts are the linked Flow's INPUT STATE / OUTPUT STATE and the named stage below.
Mapping: identity-preserving references and explicit field projection only; any incompatible representation goes to existing Mapping through Pipeline Integrity.
Invariants: retain run/objective identity, source versions, epoch, domain semantics, uncertainty and gate status.
Provenance: resolvable source and output revision pointers; preserve originals when summarizing.
Freshness: use the governing domain/claim requirement at consumption time; no universal invented TTL.
Version: pin Flow/Pipe and evidence revisions to the run; evaluate changes before reuse.
Loss/compression: omit irrelevant prose only; never drop blockers, provenance, uncertainty or authority.
Authority in/out: record/routing/analysis scope only, bounded by current authorization and target contract.
Failure: block the affected connection and propagate the blocker to Pipeline Integrity; no silent skip.
Invalidation: preserve historical outputs, invalidate affected consumers and verification; Sequencing owns re-entry epochs.
Audit status: NOT_INDEPENDENTLY_AUDITED; a local check does not change this.
Live state is a per-run record, not a durable readiness assertion in this file.

## Named Pipes

| Pipe ID | From pointer / source state | To pointer / target input | Condition and sequencing |
|---|---|---|---|
| CONT-01 | [Pipeline Integrity](../meta/pipeline-integrity.flow.md) / material handoff candidate | [Run Record](../core/run-record.flow.md) / checkpoint input | Selected continuity run; record blocked states as well as valid outputs. |
| CONT-02 | [Run Record](../core/run-record.flow.md) / persistence receipt | [Pipeline Integrity](../meta/pipeline-integrity.flow.md) / continuity evidence | Read-back verified; storage success is not Pipeline success. Missing receipt blocks required continuity claim. |
| CONT-03 | [Xyool Execution](../core/xyool-execution.flow.md) / resume objective | [Checkpoint Resume](../core/checkpoint-resume.flow.md) / checkpoint and current scope | Existing checkpoint selected; objective compatibility and current authority checked. |
| CONT-04 | [Checkpoint Resume](../core/checkpoint-resume.flow.md) / detected differences | [Evidence Refresh](../core/evidence-refresh.flow.md) / change set | Material change; checkpoint and current heads both available. |
| CONT-05 | [Checkpoint Resume](../core/checkpoint-resume.flow.md) / reconciled candidate | [Pipeline Integrity](../meta/pipeline-integrity.flow.md) / current manifest | Wait for CONT-04/06 when changed; pending external effects remain blocked. |
| CONT-06 | [Evidence Refresh](../core/evidence-refresh.flow.md) / impact dispositions | [Pipeline Integrity](../meta/pipeline-integrity.flow.md) / invalidation and re-entry inputs | All material dependencies dispositioned or explicitly blocked; existing Sequencing selects epoch and readiness. |
| CONT-07 | [Run Record](../core/run-record.flow.md) / checkpoint revision | [Checkpoint Resume](../core/checkpoint-resume.flow.md) / stored input | Later invocation only; this edge does not create a same-epoch execution cycle. |
| CONT-08 | [Run Record](../core/run-record.flow.md) / frozen run evidence | [Evaluation](../core/evaluation.flow.md) / observed results | Only when evaluation is requested; no evaluation overhead on ordinary answers. |
| CONT-09 | [Evaluation](../core/evaluation.flow.md) / evidence candidate | [Pipeline Integrity](../meta/pipeline-integrity.flow.md) / verification candidate | Existing candidate-to-Audit and Audit-to-Integrity Pipes decide verification; never bypass them. |
| CONT-10 | [Pipeline Integrity](../meta/pipeline-integrity.flow.md) / changed live evidence | [Evidence Refresh](../core/evidence-refresh.flow.md) / changed roots | Supports evidence changes without interruption; pause affected consumers until CONT-06 reconciles them. |

## Live Pipe state template

For each material invocation record:
pipe_id, wrapper_revision, source_revision, target_revision, source_as_of,
validated_at, run_id, execution_epoch, compatibility, readiness, gate_state,
invalidation_state, authority_scope, blocked_reason, evidence_refs.

Initial readiness is UNKNOWN, never PASS by default.
Return paths to Pipeline Integrity carry facts/candidates; existing
[Meta Plumbing](../meta/PLUMBING.md) owns mapping, sequencing, patching and audit calls.
