# Continuity Pipeline v1

PIPELINE ID: FLOWARE-CONTINUITY-V1
PIPELINE VERSION: 1
STATUS: VERIFICATION_PENDING
ACTIVATION: OPT-IN
MATURITY: CANDIDATE
OBJECTIVE: preserve and recover a material run without lost meaning, stale reuse, duplicated effects, or expanded authority.
GOALPOST: [frozen change scope](../../research/system-tests/floware-continuity-v1-2026-09-24/GOALPOST.md).
DOMAIN / CONFIGURATION: inherit the calling run's validated binding; core repository examples are synthetic, not a new active domain.
ENTRY: explicit selection, authorized objective, known contract/evidence heads, storage capability when persistence is required.
AUTHORITY: inherited and revalidated; no additional external-action authority.
STATE / VERSION HEAD: recorded per run using [Run Record](RUN-RECORD.template.md).
AUDIT: independent review pending; canonical Meta handshake applies.

## Stages and composition

| Stage | Flow contract | Reads / writes | Gate / failure |
|---|---|---|---|
| Route | [Xyool Execution](../core/xyool-execution.flow.md) | objective/current context → selected scope | Objective and permission known, else BLOCKED. |
| Govern | [Pipeline Integrity](../meta/pipeline-integrity.flow.md) | stage/Pipe state → candidate manifest | Owns existing primitive calls and final verification. |
| Record | [Run Record](../core/run-record.flow.md) | accepted outputs and expected head → append-only checkpoint | Read-back and collision check; failed write blocks checkpoint acceptance. |
| Recover | [Checkpoint Resume](../core/checkpoint-resume.flow.md) | checkpoint + current heads → reuse/refresh/block decisions | Conditional on interruption; unresolved effects block retries. |
| Refresh | [Evidence Refresh](../core/evidence-refresh.flow.md) | changed roots/read sets → impact dispositions | Conditional on change; unknown dependencies remain blocked. |
| Evaluate | [Evaluation](../core/evaluation.flow.md) | frozen experiment/observed records → evidence package | Conditional on evaluation objective; missing experiment capabilities remain NOT_RUN. |

Pipes: [CONT-01 through CONT-10](PLUMBING.md).
Stage versions: repository commit plus path; no implicit latest contract during an existing run.
Sequencing: existing Sequencing derives prerequisites from the Pipes; Record writes to the same head are mutually exclusive.
Checkpoint Resume runs on a later invocation. Evidence Refresh may return a changed-state candidate, but Sequencing creates a new epoch before re-execution.
Merges consume only current, compatible inputs; unaffected records retain their original epoch and revision with a compatibility justification.

## Terminal and recovery rules

A locally complete stage does not verify the Pipeline.
For a checkpoint-only objective: durable receipt and matching read-back establish only RECORDED.
For material end-to-end completion: required stage/Pipe gates and existing independent Meta Audit must pass before VERIFIED.
If independent review is unavailable: keep VERIFICATION_PENDING and name the blocker.
Do not require a checkpoint's Pipeline to be VERIFIED before allowing it to be inspected or resumed.
On patch failure retain the previous accepted contract/head; candidate artifacts remain separate.
Rollback disables the opt-in route and supersedes candidate state; it does not erase audit history or reverse external effects.

## Load and complexity budget

One relevant route at a time. Skip Recover, Refresh and Evaluate when their conditions do not apply.
Direct Resolution and existing domain gates remain authoritative.
Freeze task-specific time/tool/expansion limits in the goalpost; reaching them yields a documented bottleneck, not invented completion.
