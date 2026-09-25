# FLOW — Evaluation

FLOW ID: CORE-EVALUATION
STATUS: CANDIDATE / OPT-IN / INDEPENDENT AUDIT PENDING
DOMAIN: core / domain-neutral
JOB: Evaluation
AUTHORITY: record and route only; existing domain, action, and promotion boundaries apply
PARENT GOALPOST: [Continuity v1](../../research/system-tests/floware-continuity-v1-2026-09-24/GOALPOST.md); individual runs retain their own goalpost
UPSTREAM FLOWS: Development; Pipeline Integrity; Run Record
DOWNSTREAM FLOWS: Audit through Pipeline Integrity; Learning
INBOUND PIPES: CONT-08 in [continuity Plumbing](../continuity/PLUMBING.md)
OUTBOUND PIPES: CONT-09 in [continuity Plumbing](../continuity/PLUMBING.md)
SOFTWARE DEPENDENCIES: existing authorized storage tools for durable writes; no runtime engine introduced

## GOAL

Measure a candidate against frozen criteria without confusing guided examples, blinded tests, and isolated comparisons.

## GOALPOST

A reproducible evidence package reports the declared experiment, all outcomes and exclusions, and the limits of its design.

## INPUT STATE

Candidate/base revisions, frozen task set and rubric, source snapshots, execution context and model settings, permitted tools/budget, baseline protocol, evaluator separation declaration.

## EVIDENCE

Actual responses, tool receipts, recorded timing/token/cost measurements where available, frozen scoring rules and failure artifacts. Missing measurements remain NOT_MEASURED.

## PROCESS

Fill the [evaluation template](../continuity/EVALUATION.template.md) before execution. Separate development cases from a sealed holdout whose answers the executor cannot access. For A/B require separate contexts with identical model/version/settings, task evidence, tool permissions and budget; vary only declared Floware treatment and record total overhead. Counterbalance order and repeat as preregistered. If isolation or blinding is unavailable, mark that component NOT_RUN and allow a clearly labeled guided exercise. Score all runs, including timeouts and blocks, using the frozen rubric. Submit candidate evidence through Pipeline Integrity to independent Audit. Send exposed failures to Learning as development regressions; retire them from untouched holdout.

## GATES

No outcome-dependent rubric change; valid proceed cases prevent block-everything success; failures/exclusions retained; candidate author and evaluator separation documented; no superiority claim without a suitable completed comparison.

## ADAPTATION

Use contract review for Flow definitions, behavioral cases for execution, and focused software checks only for changed deterministic components. A generated fixture is not a completed experiment.

## BOUNDARIES

Does not create its own independent evaluator by renaming a second pass. Does not promote a component or bypass existing release gates. Public answers cannot be called a hidden test.

## FAIL-CLOSED CONDITIONS

Leaked answers invalidate blinding; differing model/evidence/budget confounds invalidate the intended comparison; missing independent evaluator leaves independent Audit BLOCKED.

## OUTPUT STATE

design; protocol revision; raw run references; per-case outcomes; completion/constraint violations/unsupported claims; time/tokens/cost or NOT_MEASURED; exclusions; uncertainty; audit status; next owner. Maturity claims are evidence-linked annotations, separate from canonical Pipeline statuses.

## LEARNING HOOK

Preserve failure evidence before proposing a patch; route regressions to existing Learning/Development and retain the frozen goal.

## SOFTWARE / HARD-LIMIT BOUNDARY

NONE — FLOWARE SUFFICIENT for experiment governance. Isolated model execution, exact scoring, telemetry and sealed access need actual supporting capabilities; absent capabilities stay NOT_RUN.

## COMPLEXITY RULE

Select the smallest experiment that resolves the named uncertainty. Stop at frozen success/failure gates or a documented capability bottleneck.
