# FLOW — Resource Allocation

FLOW ID: CORE-RESOURCE-ALLOCATION
STATUS: **CANDIDATE / VERIFICATION_PENDING**
DOMAIN: core
JOB: choose which competing Xyool work receives finite attention, evidence, reasoning, tool, and model resources before dependency-safe execution ordering
AUTHORITY: work-selection and resource-budget allocation only; no authority to change the goal, waive gates, determine domain truth, or replace Sequencing
PARENT GOALPOST: ../../research/system-tests/floware-consolidation-v1-2026-09-24/GOALPOST.md
UPSTREAM FLOWS: Xyool Execution, Observation/Trigger, Learning, active goalposts
DOWNSTREAM FLOWS: Xyool Execution; selected work may then enter Pipeline Integrity/Sequencing
INBOUND PIPES: PLUMBING.md#pipe-core-execution-resource, PLUMBING.md#pipe-core-observation-resource
OUTBOUND PIPES: PLUMBING.md#pipe-core-resource-execution
SOFTWARE DEPENDENCIES: none

## GOAL

Spend limited Xyool resources on the work most likely to advance the authorized objective without starving important blockers or creating infinite recursive research.

Core law:

> **Priority chooses what enters the active set. Sequencing chooses how the active set may run.**

## GOALPOST

Allocation is sufficient when:
- candidate work is explicit;
- hard must-do items are separated from optional work;
- active resource/complexity constraints are known;
- selected work has a stated reason;
- deferred work is preserved rather than silently discarded;
- selection does not bypass domain/authority gates;
- Direct Resolution/simple paths are preferred when adequate;
- recursive expansion has a stopping rule.

## INPUT STATE

- authorized objective and goalpost;
- candidate work items;
- current blockers/dependencies;
- observation urgency;
- expected information/discrimination value;
- consequence of delay;
- recurrence/reuse;
- cost/latency/tool burden;
- uncertainty/contamination risk;
- available context/model/tool budget where known.

## EVIDENCE

Use the active goalpost, Flow contracts, current pipeline/blocker state, prior learning, domain materiality, and observed cost/benefit evidence.

Do not treat an old software priority formula as universal architecture.

## PROCESS

~~~text
LOAD AUTHORIZED OBJECTIVE / GOALPOST
→ ENUMERATE CANDIDATE WORK
→ MARK HARD REQUIRED / OPTIONAL / DEFERABLE
→ REMOVE DUPLICATES
→ IDENTIFY BLOCKING LEVERAGE
→ ESTIMATE DECISION / INFORMATION VALUE
→ ESTIMATE CONSEQUENCE OF DELAY
→ ESTIMATE COST / COMPLEXITY / CONTAMINATION
→ PREFER SIMPLEST SUFFICIENT PATH
→ SELECT ACTIVE SET
→ ASSIGN BOUNDED RESOURCE ENVELOPES
→ PRESERVE DEFERRED QUEUE + RECONSIDERATION CONDITIONS
→ RETURN ACTIVE SET TO XYOOL EXECUTION
→ SEQUENCING GOVERNS ORDER / PARALLELISM AFTER SELECTION
~~~

## PRIORITY DIMENSIONS

Consider, without requiring one universal weighted score:
- goal relevance;
- hard-gate necessity;
- blocker leverage;
- decision relevance;
- expected information gain/discrimination;
- consequence of delay;
- recurrence/reuse value;
- uncertainty reduction;
- cost/latency/context burden;
- contamination/holdout cost;
- reversibility;
- opportunity to use already-available evidence.

A domain may add stricter dimensions.

## RESOURCE POLICY

Absorbed from the retired declarative controls:

- use the least expensive/capable reasoning path that can satisfy the required result;
- skip broad retrieval for simple self-contained work;
- load context progressively;
- parallelize independent reads only when safe;
- do not impose a token limit that forces an unverified result;
- escalate reasoning/model capability only when difficulty, failures, or proof burden justify it;
- use deterministic software later only for exact enforcement/telemetry after Software Escalation.

These are Floware resource rules, not a second control-plane architecture.

## GATES

- objective preserved;
- hard mandatory work cannot be deferred merely because it is expensive;
- deferred items retain reason/re-entry condition;
- no financial/external action authority is created;
- no validation holdout is consumed merely to gain convenience;
- no infinite recursive branch is allowed without incremental expected value.

## ADAPTATION

If new evidence changes value/cost/urgency, reallocate.

If all candidate work is mandatory, allocation reduces to resource envelopes; Sequencing still decides operational order.

## BOUNDARIES

Resource Allocation does not:
- decide dependency order;
- redefine domain materiality;
- invent new goals;
- declare evidence true;
- terminate required verification due only to token cost;
- select production financial exposure.

## FAIL-CLOSED CONDITIONS

Return BLOCKED when resource limits make the required goal impossible without violating a hard gate. Name the bottleneck instead of silently degrading the claim.

## OUTPUT STATE

~~~text
OBJECTIVE:
CANDIDATE WORK:
HARD REQUIRED:
ACTIVE SET:
DEFERRED SET:
SELECTION RATIONALE:
RESOURCE ENVELOPES:
ESCALATION CONDITIONS:
RECONSIDERATION CONDITIONS:
BLOCKERS:
~~~

## LEARNING HOOK

Repeated wasted work, starvation, excessive research, or systematic under-allocation become Learning inputs.

## SOFTWARE / HARD-LIMIT BOUNDARY

NONE — FLOWARE SUFFICIENT

Future software may enforce quotas, queue fairness, model availability, or telemetry, but only after Software Escalation.

## COMPLEXITY RULE

If one obvious required job fits the current budget, use it directly. Do not build priority scores or queues when selection is already unambiguous.
