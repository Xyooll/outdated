# FLOW — Xyool Execution

FLOW ID: `CORE-XYOOL-EXECUTION`  
STATUS: **ACTIVE / CANONICAL**  
DOMAIN: core  
JOB: adaptive execution  
AUTHORITY: process routing only
PARENT GOALPOST: current user-authorized objective / active frozen goalpost where required
UPSTREAM FLOWS: Observation / Trigger, Resource Allocation, user-authorized entry context
DOWNSTREAM FLOWS: Domain Establishment, Resource Allocation, Pipeline Integrity, selected core/domain Flows, Failure when directly classifying a non-composite material failure
INBOUND PIPES: `PLUMBING.md#pipe-core-observation-execution`, `PLUMBING.md#pipe-core-resource-execution`
OUTBOUND PIPES: `PLUMBING.md#pipe-core-execution-domain-establishment`, `PLUMBING.md#pipe-core-execution-resource`, `../meta/PLUMBING.md#pipe-meta-execution-integrity`
SOFTWARE DEPENDENCIES: none for reasoning; external tools/runtime only when the selected Flow requires them

## GOAL

Achieve the user's authorized objective using the smallest evidence-backed Flow that can reach a verified result.

## GOALPOST

For major development work, a frozen goalpost must exist before optimization begins.

## INPUT STATE

- user objective;
- applicable domain;
- current repo state;
- current goalpost if development work;
- known evidence/state;
- authority and consequence boundaries.

## PROCESS

```text
UNDERSTAND GOAL
→ IF ENTRY IS A NEW EXTERNAL / TIMER / OUTCOME OBSERVATION: RUN `observation-trigger.flow.md`
→ IDENTIFY DOMAIN + REQUESTED FUNCTION/SCOPE
→ IF DOMAIN IS NEW OR REQUESTED FUNCTION/SCOPE IS NEW / MATERIALLY EXPANDED / ESTABLISHMENT UNKNOWN:
      RUN `domain-establishment.flow.md`
      IF NOT READY_FOR_CONFIGURATION: STOP / RESOLVE LOCAL DOMAIN GAPS
      IF READY_FOR_CONFIGURATION: ROUTE TO `../meta/pipeline-integrity.flow.md` DOMAIN-INTEGRATION COMPOSITE
→ ELSE IF ESTABLISHED DOMAIN BINDING IS MODIFIED / UNCONFIGURED:
      ROUTE TO `../meta/pipeline-integrity.flow.md` DOMAIN-INTEGRATION COMPOSITE
→ LOAD ACTIVE GOALPOST
→ LOAD RELEVANT FLOW(S)
→ IF COMPETING WORK EXCEEDS THE SIMPLE DIRECT PATH: RUN `resource-allocation.flow.md`
→ IF MATERIAL MULTI-FLOW COMPOSITION / CROSS-LAYER INTEGRITY EXISTS: ROUTE THROUGH `../meta/pipeline-integrity.flow.md`
→ LOAD MINIMUM REQUIRED EVIDENCE
→ EXECUTE READY OPERATIONS ADAPTIVELY
→ PASS REQUIRED GATES
→ PRODUCE OUTPUT STATE
→ IF MATERIAL PIPELINE / CROSS-LAYER INTEGRITY APPLIES: REQUIRE `../meta/pipeline-integrity.flow.md` TERMINAL STATUS
→ VERIFY AGAINST GOALPOST
→ PERSIST MATERIAL LEARNING
```

Prefer:
`existing Flow → compose Flows → adapt Flow → create Flow`

Do not begin with:
`write code`.

## GATES

- goal/domain identified;
- required authority known;
- mandatory evidence gates satisfied;
- material unknowns explicit;
- output auditable.

## ADAPTATION

The Flow may route into domain/sub-flows as evidence requires.

### CORE DOMAIN ESTABLISHMENT ROUTING

Use `domain-establishment.flow.md` before Meta configuration when:
- a domain is new;
- a material domain function is new;
- a requested function's native rules/methods are missing or unknown;
- a domain Flow claims capability beyond the established native substrate.

Domain Establishment proves the domain-native foundation and per-function readiness for the claimed scope.

Only `READY_FOR_CONFIGURATION` scopes proceed to Mapping / Domain Configurer through Pipeline Integrity.

A configuration file does not substitute for an establishment record.

### META CONFIGURATION / MAPPING ROUTING

Pipeline Integrity handles integration only after Core Domain Establishment has produced `READY_FOR_CONFIGURATION` for the claimed scope. Use `../meta/domain-configurer.flow.md` directly only when the native domain scope is already established and the task is narrowly scoped to configuration itself.

The Domain Configurer uses `../meta/mapping.flow.md` for explicit representation alignment. Mapping may also be called directly when the task is to align two contracts, schemas, Flow representations, or legacy/new structures without configuring an entire domain.

Do not treat a structural mapping as cross-domain empirical validation. Use `correspondence.flow.md` when the question is whether learned structure genuinely transfers.

### RELATIONAL STORY ROUTING

When the task is naturally organized around:
- a focal/root entity;
- changing relationships;
- nested characters/entities;
- causal propagation;
- reusable memory;
- re-rooting;
- or an evolving multi-actor story,

load:

`relational-story.flow.md`

Then load the applicable validated domain configuration produced or governed by `../meta/domain-configurer.flow.md`.

That configuration must bind the domain to Relational Story through explicit mappings for:
- character/root types;
- relationship semantics;
- event/state-delta semantics where applicable;
- source authority;
- materiality;
- propagation;
- resource horizon;
- memory/pointer rules;
- audit specializations;
- closure/output.

Do not assume the Relational Story Flow is stock-specific.

A side discovery does not become the new goal.

### META PIPELINE INTEGRITY ROUTING

Use `../meta/pipeline-integrity.flow.md` as the default front door when:
- multiple material Flows compose toward one objective;
- cross-layer handoffs matter;
- stage versions/state/provenance must remain continuous;
- order/parallelism/barriers matter;
- an architecture/domain change must propagate safely;
- release/promotion/end-to-end verification matters.

Pipeline Integrity invokes Mapping, Domain Configurer, Sequencing, Patching, and Audit only where applicable.

Use a primitive Meta Flow directly when the task is narrowly scoped to that primitive job.

### META SEQUENCING ROUTING

Pipeline Integrity normally calls `../meta/sequencing.flow.md`. Use Sequencing directly when the task itself is specifically order/readiness control and:

- multiple Flows/operations compose toward one objective;
- prerequisites/gates constrain order;
- independent branches may be parallelized;
- barriers/merge points matter;
- shared mutable state creates ordering conflicts;
- new evidence may invalidate/reopen prior work.

Xyool Execution owns routing. When multiple candidate jobs compete for finite resources, `resource-allocation.flow.md` selects the bounded active set. Sequencing then determines what is READY now, what may run in parallel, and what must wait.

Do not confuse domain causal order with operational order. Xyool may research independent causal branches in parallel even when the real-world events themselves are sequential.

### META PATCHING ROUTING

Pipeline Integrity normally calls `../meta/patching.flow.md`. Use Patching directly only when the task is specifically patch-impact/change propagation and an end-to-end pipeline composite is unnecessary.

Patching must:
- identify the source-of-truth change;
- build an impact graph;
- update or explicitly disposition every material dependent surface;
- preserve historical immutable records;
- remain PARTIAL until required verification is complete.

Do not claim an architectural update is complete merely because the obvious file was edited.

### CORE OBSERVATION / RESOURCE ROUTING

Use `observation-trigger.flow.md` when a new filing/feed item, timer, resolved outcome, changed state, or other observation is the reason Xyool may need to wake/re-enter work.

Use `resource-allocation.flow.md` when more material work is available than should be active at once. Resource Allocation selects/defer jobs; it does not determine dependency order.

Connections:
`PLUMBING.md`

### META FAILURE ROUTING

Inside a material composed pipeline, Pipeline Integrity routes material failures to `../meta/failure.flow.md` for classification, owner, disposition, and re-entry conditions.

Use Failure directly only when the task itself is specifically failure classification and a larger Pipeline Integrity composite is unnecessary. Failure never performs the repair it classifies.

### META PROMOTION / LIFECYCLE ROUTING

A lesson, challenger, domain capability, or other candidate does not become promoted merely because Evaluation or Audit passes. Lifecycle changes route through Pipeline Integrity to `../meta/promotion-lifecycle.flow.md` when promotion/demotion/retirement is part of the authorized objective.

### META AUDIT ROUTING

Pipeline Integrity normally calls `../meta/audit.flow.md` for material end-to-end verification. Use Audit directly when the task itself is specifically independent verification of:
- Flow contract conformance;
- domain-to-core mapping integrity;
- state-transition continuity;
- evidence/provenance integrity;
- architectural boundary preservation;
- learning/promotion integrity;
- or release-level cross-layer checks.

Local self-checks remain inside their owning Flows. Meta Audit does not silently repair or redefine the object it audits.

## BOUNDARIES

This Flow does not grant external action, capital, or transaction authority.

## FAIL-CLOSED CONDITIONS

Return BLOCKED/UNKNOWN rather than inventing evidence or skipping a mandatory gate.

## OUTPUT STATE

- result;
- evidence basis;
- unresolved blockers;
- goalpost status;
- next action only if still inside the same goal.

## LEARNING HOOK

Material misses route to `learning.flow.md`.

## SOFTWARE / HARD-LIMIT BOUNDARY

Use `software-escalation.flow.md` before introducing new software.

## OPTIONAL CONTINUITY ROUTING

When the user selects material run continuity or capability evaluation, load [Continuity v1](../continuity/PIPELINE.md) and its [Pipes](../continuity/PLUMBING.md).
Use CONT-03 for an interrupted checkpoint; existing Pipeline Integrity remains the front door for composition. Run Record, Checkpoint Resume, Evidence Refresh and Evaluation are opt-in candidate Flows. Existing Direct Resolution remains sufficient for simple tasks. Routing into a candidate does not establish independent verification or grant action authority.
