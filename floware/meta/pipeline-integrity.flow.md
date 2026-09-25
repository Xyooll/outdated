# META FLOW — Pipeline Integrity

FLOW ID: META-PIPELINE-INTEGRITY
STATUS: **ACTIVE / CANONICAL COMPOSITE**
DOMAIN: meta
JOB: govern the end-to-end integrity of a composed Xyool Flow pipeline by coordinating configuration, mapping, sequencing, patch propagation, failure classification, lifecycle promotion where applicable, Pipe validation, state/version continuity, and independent audit
AUTHORITY: pipeline composition/integrity coordination only; no authority to redefine domain truth, invent missing evidence, bypass primitive Meta Flow boundaries, or grant external/action authority
PARENT GOALPOST: supplied by Xyool Execution, Development, Learning, domain execution, or the authorized pipeline objective
UPSTREAM FLOWS: Xyool Execution, Core Domain Establishment, Development, Learning, domain composite Flows, authorized change requests
DOWNSTREAM FLOWS: Mapping, Domain Configurer, Sequencing, Patching, Failure, Promotion/Lifecycle, Audit, owning domain/core Flows
INBOUND PIPES: `../core/PLUMBING.md#pipe-core-domain-establishment-integrity`, `PLUMBING.md#pipe-meta-execution-integrity`, `PLUMBING.md#pipe-meta-learning-integrity`
OUTBOUND PIPES: `PLUMBING.md#pipe-meta-integrity-mapping`, `PLUMBING.md#pipe-meta-integrity-configurer`, `PLUMBING.md#pipe-meta-integrity-patching`, `PLUMBING.md#pipe-meta-integrity-sequencing`, `PLUMBING.md#pipe-meta-integrity-failure`, `PLUMBING.md#pipe-meta-integrity-promotion`, `PLUMBING.md#pipe-meta-candidate-audit`
SOFTWARE DEPENDENCIES: none by default; deterministic graph validation, version checks, schema validation, locks, transactions, and durable manifests may support exact enforcement

## GOAL

Ensure that a multi-Flow pipeline remains coherent from entry to completion.

Pipeline Integrity is the top-level composite Meta Flow.

It does not replace the primitive Meta Flows.

It coordinates them.

Core law:

> **A pipeline is only as valid as its weakest required Pipe.**

Second law:

> **No stage may silently change the meaning, authority, version, or state assumptions of what it receives.**

Third law:

> **Pipeline completion requires end-to-end integrity, not merely successful local stages.**

## GOALPOST

A pipeline is complete only when:
- the pipeline objective and terminal state are explicit;
- all required stages are identified;
- each stage's input/output contract is known;
- every material Pipe is compatible;
- Domain Establishment is `READY_FOR_CONFIGURATION` for any new/expanded claimed domain scope;
- domain/configuration bindings are valid;
- representation mappings are valid where required;
- sequencing/gates/barriers are valid;
- state/version/provenance continuity is preserved;
- required patch propagation is complete where the pipeline itself changed;
- failure and rollback/re-entry behavior are explicit;
- no required stage remains silently skipped;
- independent Meta Audit reports no unresolved material FAIL/BLOCKED;
- the pipeline reaches VERIFIED / COMPLETE for the claimed scope.

## INPUT STATE

At minimum:
- pipeline objective / goalpost;
- pipeline identity / version;
- selected stages / Flows;
- applicable domain configuration;
- current state/version;
- authority boundaries;
- required inputs/evidence;
- terminal output expectations;
- known mappings;
- known change/patch context when applicable.

## EVIDENCE

Use:
- Flow contracts;
- `../PIPE-CONTRACT.md`;
- pipeline/stage manifests;
- Domain Configurer outputs;
- Mapping objects;
- Sequencing operation graphs;
- Patching impact graphs;
- state/schema versions;
- provenance/evidence pointers;
- audit findings;
- migration/compatibility records;
- tests/research proving stage behavior where applicable.

A locally successful stage is not evidence that downstream Pipes are valid.

## PIPELINE MANIFEST

Every material composed pipeline should be representable as:

~~~text
PIPELINE ID:
PIPELINE VERSION:
STATUS:
OBJECTIVE / GOALPOST:
DOMAIN / CONFIGURATION:
ENTRY CONDITIONS:
TERMINAL CONDITIONS:
AUTHORITY BOUNDARY:

STAGES[]
  stage_id
  flow_id
  purpose
  input_contract
  output_contract
  reads
  writes
  prerequisites
  gates
  failure_behavior
  version

PIPES[]
  pipe_id
  from_pointer
  to_pointer
  source_contract
  target_contract
  wrapper
  mapping / transformation
  semantic_invariants
  provenance_requirements
  freshness / version requirements
  uncertainty preservation
  authority constraints
  gate / sequencing behavior
  failure / invalidation / re-entry
  live_pipe_state

SEQUENCING PLAN:
PATCH CONTEXT:
STATE / VERSION HEAD:
ROLLBACK / RE-ENTRY RULE:
AUDIT STATUS:
~~~

## PIPELINE STATUS

Use:

~~~text
DRAFT
CONFIGURING
READY
RUNNING
WAITING
BLOCKED
PARTIAL
VERIFICATION_PENDING
VERIFIED
FAILED
SUPERSEDED
ROLLED_BACK
~~~

Only VERIFIED means end-to-end integrity is established for the claimed scope.

## PRIMITIVE META FLOWS

Pipeline Integrity coordinates five primitive Meta capabilities.

~~~text
MAPPING
= how representations line up

DOMAIN CONFIGURER
= how domain semantics bind into Floware

SEQUENCING
= what is ready, what waits, what can run in parallel

PATCHING
= what must change together when the pipeline/contract changes

AUDIT
= independent verification that the resulting pipeline preserved its contracts
~~~

Do not collapse the primitive contracts merely because Pipeline Integrity invokes them.

## WHEN EACH PRIMITIVE IS REQUIRED

### Mapping

Required when:
- one stage's output is not natively the next stage's input representation;
- domain-native objects cross into general Floware structures;
- a schema/contract translation occurs.

### Domain Configurer

Required when:
- a domain is new/materially changed;
- pipeline semantics depend on domain-local meaning;
- authority/evidence/state/time/archetype/writer rules must be bound.

### Sequencing

Required when:
- more than one operation/stage composes materially;
- prerequisites/gates/barriers exist;
- safe parallelism matters;
- state invalidation/re-entry matters.

### Patching

Required when:
- the pipeline, stage contract, mapping, schema, or domain binding changes across multiple dependent surfaces.

### Audit

Required for:
- material pipeline completion;
- promotion/release;
- cross-layer integrity;
- a repaired or changed pipeline before VERIFIED status.

Audit remains independent.

## PIPE INTEGRITY

A Pipe is valid only when:

~~~text
UPSTREAM OUTPUT
→ identity/version known
→ required fields present
→ semantics compatible
→ provenance retained
→ freshness adequate
→ authority not broadened
→ downstream input contract satisfied
~~~

For every required Pipe, check:

- identity continuity;
- schema/shape compatibility;
- semantic compatibility;
- unit/scale compatibility when relevant;
- temporal/as-of compatibility;
- provenance continuity;
- confidence/uncertainty preservation;
- authority preservation;
- domain-boundary preservation;
- version compatibility.

## SEMANTIC PIPE RULE

Matching field names do not prove compatibility.

Example:

~~~text
upstream "confidence"
≠ automatically
downstream "probability"
~~~

Use Mapping when semantic equivalence is not explicit.

## AUTHORITY PIPE RULE

Authority must never silently increase across a pipeline.

Example:

~~~text
ANALYSIS OUTPUT
→ cannot become
ACTION AUTHORITY
~~~

unless an explicit downstream contract grants that authority.

Every Pipe should satisfy:

~~~text
downstream_authority <= explicitly permitted authority
~~~

## STATE / VERSION CONTINUITY

A pipeline must preserve which state/version each stage consumed.

Minimum:

~~~text
stage
input_state_version
input_as_of
output_state_version
evidence/provenance head
execution_epoch
~~~

If upstream state materially changes:

~~~text
identify affected downstream stages
→ INVALIDATE
→ start new execution epoch
→ rerun only affected descendants
~~~

Do not silently keep downstream conclusions based on superseded state.

## PROCESS

~~~text
IDENTIFY PIPELINE OBJECTIVE
→ LOAD / BUILD PIPELINE MANIFEST
→ IDENTIFY DOMAIN + CONFIGURATION
→ IF NEW / EXPANDED DOMAIN SCOPE:
      REQUIRE CORE DOMAIN ESTABLISHMENT RECORD = READY_FOR_CONFIGURATION
      OTHERWISE RETURN TO CORE DOMAIN ESTABLISHMENT
→ VALIDATE STAGE IDENTITIES / CONTRACTS
→ FOR EACH MATERIAL PIPE:
      VALIDATE DIRECT COMPATIBILITY
      OR CALL MAPPING
→ IF DOMAIN BINDING IS NEW / CHANGED:
      CALL DOMAIN CONFIGURER
→ CALL SEQUENCING
      build prerequisite graph
      identify READY frontier
      parallel groups
      barriers
      mutexes
      re-entry rules
→ EXECUTE / ROUTE STAGES
→ AT EACH PIPE:
      CHECK contract + version + provenance + authority
      FAIL CLOSED ON MATERIAL MISMATCH
→ IF PIPELINE CONTRACT / DEPENDENCIES CHANGE:
      CALL PATCHING
      propagate change completely
→ RECONCILE TERMINAL STATE AGAINST GOALPOST
→ STATUS = VERIFICATION_PENDING
→ CALL INDEPENDENT META AUDIT
→ PASS / PASS_WITH_NOTES:
      IF LIFECYCLE TRANSITION IS PART OF THE OBJECTIVE:
          CALL PROMOTION / LIFECYCLE
          IF REQUESTED TRANSITION IS NOT EARNED / PROMOTION RETURNS BLOCKED:
              STATUS = BLOCKED / PARTIAL
              DO NOT CLAIM PROMOTION
          IF PATCH_REQUIRED: ROUTE THROUGH PATCHING + RE-VERIFY
          ELSE RECORD THE EARNED LIFECYCLE STATE
      STATUS = VERIFIED ONLY WHEN THE CLAIMED PIPELINE/LIFECYCLE OBJECTIVE IS SATISFIED
→ FAIL / BLOCKED:
      STATUS = BLOCKED / PARTIAL / FAILED
      CALL FAILURE FOR CLASSIFICATION + OWNER / RE-ENTRY DISPOSITION
      route remediation through the owning primitive/Flow
~~~

## PIPELINE BARRIERS

A barrier prevents premature downstream finalization.

Common barriers:

### Domain-establishment barrier
For new or materially expanded domain scope, all required native functions/rules for the claimed scope are `READY_FOR_CONFIGURATION` before Mapping/Domain Configurer may finalize bindings.

### Domain-update barrier
For an existing domain update, the establishment delta must identify affected/unaffected functions, invalidated shared dependencies, and the minimum reconfiguration scope before Meta integration begins.

### Evidence barrier
All required evidence branches resolved.

### Character/story barrier
All material required character branches have valid terminal status before Story Reader/thesis closure.

### Patch barrier
All required impact-graph nodes have dispositions before audit.

### Migration barrier
All required compatibility/state migration steps completed before runtime promotion.

### Verification barrier
Candidate pipeline waits in VERIFICATION_PENDING until Audit completes.

## FAILURE PROPAGATION

A stage failure does not always fail the entire pipeline.

Each stage must declare failure behavior:

~~~text
BLOCK_PIPELINE
DEGRADE_WITH_WARNING
SKIP_NOT_APPLICABLE
RETRY / RE-ENTER
ROUTE_ALTERNATE
ROLLBACK
~~~

The disposition must come from the governing Flow/domain contract, not from Pipeline Integrity improvisation.

For a material, repeated, cross-layer, or otherwise ambiguous failure, route through `failure.flow.md`. Failure classifies the incident and returns the owning response/re-entry condition; it does not perform Patching, Sequencing, Audit, or Learning itself.

## LOCAL SUCCESS VS PIPELINE SUCCESS

Example:

~~~text
Mapping PASS
Sequencing PASS
Patch PASS
but
Pipe loses provenance
→ PIPELINE FAIL
~~~

Another:

~~~text
all stages COMPLETE
but
Audit finds stale state
→ PIPELINE NOT VERIFIED
~~~

Core rule:

> **Local PASS states do not add up automatically to pipeline PASS.**

## CHANGE MANAGEMENT COMPOSITE

For architecture/system changes:

~~~text
AUTHORIZED CHANGE
→ PIPELINE INTEGRITY
   → PATCHING: impact graph
   → MAPPING / DOMAIN CONFIGURER as needed
   → SEQUENCING: patch order / parallelism / barriers
   → APPLY
   → VERIFICATION_PENDING
   → AUDIT
→ VERIFIED / BLOCKED
~~~

This is the canonical Change Management composite.

## DOMAIN INTEGRATION COMPOSITE

For new/materially changed domains:

~~~text
DOMAIN OBJECTIVE / REQUESTED FUNCTION
→ CORE DOMAIN ESTABLISHMENT
   → if new domain: establish native foundation + function contracts
   → if existing domain: load prior establishment + establish only the delta
   → READY_FOR_CONFIGURATION for claimed scope
   → emit affected/unaffected + reconfiguration scope
→ PIPELINE INTEGRITY
   → MAPPING
   → DOMAIN CONFIGURER
   → SEQUENCING
   → domain/core binding checks
   → AUDIT
→ VALIDATED DOMAIN PIPELINE
~~~

This is the canonical Domain Integration composite.

## EXECUTION PIPELINE COMPOSITE

For ordinary multi-Flow execution:

~~~text
OBJECTIVE
→ XYOOL EXECUTION selects Flows
→ PIPELINE INTEGRITY
   → SEQUENCING
   → Pipe checks
   → state/version continuity
   → Audit when material
→ terminal output
~~~

Patching is not invoked unless the architecture/contract itself changes.

## GATES

Before READY:
- for new/expanded domain scope, Domain Establishment is READY_FOR_CONFIGURATION;
- pipeline objective known;
- stages known;
- entry conditions satisfied;
- domain configuration valid where required;
- critical Pipes mapped/compatible;
- Sequencing graph not materially ambiguous.

Before VERIFIED:
- required stages have valid terminal status;
- Pipes passed;
- no stale/superseded state contaminates terminal output;
- required patches/migrations complete;
- terminal state satisfies goalpost;
- independent Audit passes.

## ADAPTATION

Pipeline Integrity may:
- omit primitive Meta Flows that are genuinely not applicable;
- insert Mapping when a Pipe mismatch appears;
- insert Patching when the pipeline contract changes;
- rebuild Sequencing after state/structure change;
- create a new execution epoch after invalidation;
- narrow verification to the affected subgraph when safely possible.

It may not:
- skip independent Audit where the governing pipeline requires it;
- declare local success equal to end-to-end success;
- turn every simple single-Flow task into a large pipeline ceremony.

## BOUNDARIES

Pipeline Integrity does not:
- decide domain truth;
- create new action/capital authority;
- rewrite primitive Meta Flow contracts;
- silently coerce incompatible stage outputs;
- invent missing evidence;
- hide failed/blocked stages;
- rewrite historical pipeline runs to match new architecture.

## FAIL-CLOSED CONDITIONS

Return BLOCKED / PARTIAL / FAILED when:
- new/expanded domain scope lacks a READY_FOR_CONFIGURATION establishment record;
- a required stage identity/version is unknown;
- a material Pipe is incompatible;
- required Mapping is unresolved;
- required domain configuration is invalid;
- Sequencing contains unresolved hard cycles/deadlocks;
- a required patch is partial;
- upstream state changed and affected downstream results were not invalidated;
- authority broadens silently across a Pipe;
- provenance is lost at a required Pipe;
- Audit reports material FAIL/BLOCKED;
- a material failure requiring classification has no valid Failure disposition/owner;
- a requested lifecycle promotion exceeds the evidence or governing promotion contract.

## OUTPUT STATE

~~~text
PIPELINE ID:
PIPELINE VERSION:
STATUS:
OBJECTIVE / GOALPOST:
DOMAIN / CONFIGURATION:
STAGE STATUS:
PIPE STATUS:
SEQUENCING STATUS:
PATCH STATUS:
STATE / VERSION CONTINUITY:
PROVENANCE CONTINUITY:
AUTHORITY CONTINUITY:
BLOCKERS:
TERMINAL STATE:
META AUDIT:
FAILURE DISPOSITION:
LIFECYCLE DECISION:
NEXT REMEDIATION OWNER:
~~~

## LEARNING HOOK

A Pipeline Integrity Miss occurs when:
- every stage looked locally correct but the end-to-end result was wrong;
- a stage consumed incompatible/stale input;
- a Pipe lost provenance/uncertainty/authority constraints;
- sequencing allowed premature finalization;
- patching omitted a dependent surface;
- a domain binding changed without reconfiguration;
- a stage version changed without invalidating downstream state;
- Audit found an integrity failure not represented by the pipeline manifest.

Recurring misses should improve:
- pipeline manifests;
- Flow contracts;
- Pipe declarations;
- Mapping objects;
- sequencing dependencies;
- patch-impact discovery;
- deterministic compatibility checks.

## SOFTWARE / HARD-LIMIT BOUNDARY

Floware is sufficient for pipeline integrity reasoning.

Deterministic software may be justified for:
- manifest/version validation;
- schema compatibility;
- DAG/cycle checks;
- transaction boundaries;
- locks;
- durable run IDs / execution epochs;
- provenance hashes;
- exact Pipe validation;
- CI/release promotion.

Software enforces the Pipeline Integrity contract; it does not replace the primitive Meta reasoning.

## OPTIONAL CONTINUITY COMPOSITION

For explicitly selected [Continuity v1](../continuity/PIPELINE.md), use [CONT-01 through CONT-10](../continuity/PLUMBING.md) for checkpoint recording, recovery, changed-evidence impact and evaluation evidence.
Record continuity through Run Record; route changed evidence to Evidence Refresh via CONT-10 or Checkpoint Resume via CONT-04. Consume impact dispositions through CONT-06, then invoke existing Sequencing for new epochs and readiness. Contract changes still invoke Patching; domain changes still invoke Domain Configurer/Mapping. Evaluation returns evidence through CONT-09; the existing candidate/Audit/Integrity handshake remains required. No new Flow may independently mark the Pipeline VERIFIED.
