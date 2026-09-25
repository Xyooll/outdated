# Future Build Notes — Flow First, Software Later

DATE / CONTEXT: 2026-09-24 — after Floware continuity and consolidation work.

STATUS: **ACTIVE / USER-DIRECTED FUTURE BACKLOG**

## USER WORDING

> "Put all the things that we need to build later into notes."

Related direction already established by the user:

> Xyool should use Flows rather than code for reasoning now. Software should be preserved safely and built/reactivated later only when actually needed.

## CONCEPT

Keep one durable list of capabilities that Xyool may need later so current architecture work does not accidentally turn into premature software development.

The backlog is **not permission to build the items now**.

Canonical rule:

~~~text
FLOW FIRST
→ PROVE BEHAVIOR / NEED
→ IDENTIFY HARD LIMIT
→ SOFTWARE ESCALATION
→ REUSE PARKED SOFTWARE IF SUITABLE
→ BUILD ONLY THE MINIMUM NECESSARY SOFTWARE
~~~

## CURRENT GATES BEFORE LATER BUILD WORK

These are not deferred software features. They are the proof gates that should happen first:

- independent Meta Audit of Continuity / PR #18;
- independent Meta Audit of Floware Consolidation / PR #19;
- combined audit of the continuity + failure + lifecycle + observation + resource architecture;
- behavioral scenario testing with real interruptions, changed evidence, failures, competing work, and discovery misses;
- repeated regression testing of learned fixes;
- isolated evaluation before maturity/promotion claims.

## FUTURE DETERMINISTIC VERIFICATION

Build only after the Flow contracts stabilize enough that automation will not freeze the wrong architecture.

### Contract checker

Deterministically check:
- required Flow identity fields and sections;
- inbound/outbound Pipe reciprocity;
- Pipe endpoint resolution;
- registry membership;
- broken internal references;
- canonical Pipeline status vocabulary;
- duplicated Flow IDs;
- obvious version/contract mismatches.

Boundary:
- structural validation only;
- must not replace semantic Meta Audit.

### Behavioral continuity test harness

Exercise:
- Run Record;
- checkpoint save/resume;
- changed-evidence refresh;
- invalidation/re-entry;
- failed persistence;
- uncertain external effects;
- duplicate-effect prevention;
- authority revalidation.

### Failure-to-regression harness

Convert validated reusable failures into persistent regression cases.

Required path:

~~~text
FAILURE RECORD
→ LEARNING
→ GENERALIZABLE FIX
→ FROZEN REGRESSION
→ LATER RUNS MUST RE-EXERCISE IT
~~~

Do not turn one incident directly into a permanent rule.

### Sealed challenge / hidden test sets

Create untouched challenge cohorts for mature Flow evaluations.

Requirements:
- outcome/answer isolation;
- clear consumed-vs-untouched state;
- immutable test definition;
- no reuse of revealed cases as fresh validation.

### Comparison / isolated A-B harness

When evidence warrants:
- freeze baseline;
- freeze treatment;
- hold model/settings/tools/budget constant where appropriate;
- record immutable outputs;
- evaluate with an independent rubric/evaluator;
- preserve NOT_RUN when true isolation is unavailable.

## FUTURE AUTONOMY INFRASTRUCTURE

The reasoning contracts already exist or are being defined. Software is needed only when continuous real-world operation is justified.

### Observation scheduler / watcher runtime

Potential implementation for:
- scheduled checks;
- due timers;
- source refresh;
- outcome resolution;
- external change detection.

Owning Flow:
`floware/core/observation-trigger.flow.md`

The runtime wakes Xyool; it does not decide materiality itself.

### Event-first source intake + HTML control surface

Concept pointer:
`2026-09-25-event-model-rss-html-control-layer.md`

Architecture direction:

~~~text
SOURCES
→ ADAPTERS
→ NORMALIZED EVENTS
→ EVENT STORE / QUEUE
→ XYOOL CORE
→ OBSERVATION / TRIGGER
~~~

RSS/Atom are source adapters rather than the canonical input model.

HTML/CSS/JavaScript may later provide:
- event-feed visualization;
- routing/status/provenance views;
- job/execution state;
- human controls such as research, prioritize, pause, redirect, and inspect.

UI actions should emit explicit events into Core rather than bypass Floware.

Prefer early JSON + Git/local-state + simple HTML viewer. Escalate to SQLite/Postgres/event queues/full web UI only after demonstrated scale/concurrency need.

### RSS / quality-source intake

Future input layer for quality sources collected by the user/project.

Potential capabilities:
- source registry;
- RSS/Atom adapters;
- source identity;
- cursor tracking;
- deduplication;
- published/fetched timestamps;
- provenance;
- domain routing;
- source-quality metadata.

Route:

~~~text
RSS / FEED ITEM
→ OBSERVATION / TRIGGER
→ owning domain Research / Story Sourcing / Evidence-to-State
~~~

Do not let feed ingestion become thesis/capital authority.

### Filing / structured-source automation

Existing SEC parsing/persistence software may be reused later.

Potential extension:
- automated EDGAR cursor checks;
- form-family routing;
- deterministic structured extraction where supported;
- evidence-event generation;
- trigger escalation.

Keep semantic interpretation in the owning stock Flows.

### Durable work queue / event bus

Possible need when Xyool handles many concurrent watched objects.

Responsibilities may include:
- pending trigger queue;
- retries;
- deduplication;
- priority envelope metadata;
- execution epochs;
- idempotency keys;
- backpressure.

Owning reasoning:
Observation + Resource Allocation + Sequencing + Failure.

### Autonomous Flow runner

Only after the above Flows prove stable.

Potential responsibilities:
- load Flow/Pipe contracts;
- maintain run identity;
- invoke the appropriate model/tools;
- persist run state;
- resume interrupted work;
- hand failures to the Failure Flow;
- respect Resource Allocation and Sequencing;
- stop at authority boundaries.

It must execute Floware, not recreate reasoning logic in code.

## FUTURE PERSISTENCE / STATE INFRASTRUCTURE

### Durable run-record / checkpoint store

Needed if local/Git persistence is insufficient.

Potential requirements:
- atomic append;
- compare-and-swap or transactions;
- unique run/epoch IDs;
- read-back receipts;
- checkpoint collision detection;
- immutable history;
- resumable state.

### Scalable domain-state backend

Current contracts are backend-independent.

Possible future backends:
- SQLite;
- PostgreSQL / Supabase;
- object storage;
- another durable store.

Migrate only when repository files become inadequate for:
- write volume;
- query volume;
- concurrent access;
- catalog size;
- transactional integrity.

### Provenance / content-addressing infrastructure

Potential deterministic support for:
- source hashes;
- artifact hashes;
- immutable evidence IDs;
- version heads;
- lineage;
- deduplication.

### Document / PDF ingestion and retrieval

Build only when a domain repeatedly needs large document collections beyond targeted retrieval.

Possible features:
- document parsing;
- chunk/provenance indexing;
- retrieval;
- source-version tracking;
- evidence extraction.

Floware remains responsible for deciding what evidence means.

## FUTURE RESOURCE / EXECUTION SUPPORT

### Resource-policy enforcement and telemetry

Software may later enforce or measure:
- model availability;
- token/tool usage;
- cost;
- latency;
- queue fairness;
- concurrency;
- hard quotas.

Owning Flow:
`floware/core/resource-allocation.flow.md`

Measurements constrain the Flow; software must not become an independent priority policy.

### Programmatic tool orchestration

Potentially useful for bounded tool-heavy processes after the Flow is proven.

Requirements:
- explicit owning Flow;
- authority preservation;
- retry/idempotency policy;
- evidence receipts;
- deterministic boundaries.

### Processor / Executioner agent runtime concept

Concept pointer:
`2026-09-25-processor-executioner-agent-loop.md`

Candidate future runtime:

~~~text
USER
→ CHATGPT / PROCESSOR
→ XYOOL CORE
→ BOUNDED JOB CAPSULE
→ EVENT / ALERT
→ EXECUTIONER AGENT
→ GIT / DURABLE STATE
→ COMPACT RECEIPT
→ EVENT / ALERT
→ PROCESSOR
→ repeat
~~~

Key principle:
- ChatGPT/Processor reasons, interprets, compiles context, and communicates;
- Executioner performs bounded tool/research/Git work;
- Git carries durable architecture/state so the Executioner may remain largely stateless;
- token savings depend on minimum-sufficient context capsules and pointer-based retrieval;
- Executioner may request follow-up work but Core/Processor authorizes the next mission.

Human-interruptible runtime is required:
- Processor remains available to the user while jobs run;
- user may inspect, redirect, pause, cancel, reprioritize, or add context;
- material changes to in-flight work create explicit job-version/supersession state rather than invisible mutation;
- autonomous continuation never removes user control.

Do not build yet. First establish Agent Contract, Job Capsule, Execution Receipt, event semantics, user-interaction/interrupt semantics, and a demonstrated context/token bottleneck, then route through Software Escalation.

### Multi-agent / parallel-worker runtime

Only if real workloads prove one adaptive executor is insufficient.

Use as an implementation of:
- Resource Allocation;
- Sequencing;
- Pipeline Integrity.

Do not create a second multi-agent reasoning architecture.

## FUTURE DEVELOPMENT / RELEASE INFRASTRUCTURE

### Git-aware Flow development support

Potential support for:
- contract diffs;
- impacted-Pipe discovery;
- patch manifests;
- branch/PR state;
- historical version lookup.

This may assist Patching but cannot replace semantic impact analysis.

### Regression-case generation tooling

Software may package already-approved failure/learning cases into repeatable tests.

It must not automatically promote a case-specific patch into a general rule.

### Promotion/release enforcement

Future software could mechanically block activation until the Promotion/Lifecycle Flow's required evidence exists.

Possible enforced states:
- RESEARCH;
- SHADOW;
- CANARY;
- PROMOTED;
- DEMOTED;
- ROLLED_BACK;
- RETIRED.

Lifecycle meaning remains Floware authority.

### Production deployment controls

If Xyool later operates outside the repository:
- deployment manifests;
- environment/version locks;
- rollback;
- health checks;
- permission boundaries;
- audit logging.

These remain implementation/safety infrastructure, not reasoning.

## PARKED SOFTWARE TO REVIEW BEFORE BUILDING NEW SOFTWARE

Before implementing any item above, inspect the retained:

- `agent/`;
- `scripts/`;
- `tests/`;
- `main.py`;
- `.github/workflows/`;
- `pyproject.toml`;
- legacy `nodes/` only where required by retained runtime compatibility.

Reuse useful deterministic components rather than rebuilding them simply because Floware now owns the reasoning contract.

## THINGS NOT TO PREMATURELY BUILD

Do not build merely because they sound architecturally attractive:

- one software service per Flow;
- a separate engine for every Pipe;
- universal scoring formulas for Resource Allocation;
- automated self-promotion;
- unrestricted recursive research;
- multi-agent infrastructure without demonstrated need;
- a database before current storage hits a real limit;
- continuous polling before Observation/Trigger behavior is proven;
- broad RAG/indexing before a domain proves targeted retrieval insufficient.

## SYSTEM EFFECT

This note becomes the durable deferred-build backlog.

The active roadmap should link here rather than repeatedly recreating future software plans in chats.

## OPEN QUESTIONS

- Which future capability will be the first to cross the Software Escalation threshold?
- What scale/concurrency threshold should trigger state-backend migration?
- Which quality RSS/feed sources will become the initial Observation inputs once autonomy is ready?
- How much of the parked runtime can be reused unchanged after Floware behavior is validated?

## RELATED CONCEPTS

- `2026-09-22-floware-and-flows.md`
- `2026-09-22-coding-to-flowing.md`
- `2026-09-23-degree-limit-is-resource-bound.md`
- `../../docs/retained-software.md`
- `../../docs/roadmap.md`
- `../../floware/core/software-escalation.flow.md`
- `../../floware/core/observation-trigger.flow.md`
- `../../floware/core/resource-allocation.flow.md`
- `../../floware/meta/failure.flow.md`
- `../../floware/meta/promotion-lifecycle.flow.md`

## STATUS

**ACTIVE / EVOLVING**

Append or refine this note when a genuinely new deferred capability is identified. Do not silently turn a deferred item into an active build without opening the appropriate goalpost and Flow/Software-Escalation path.
