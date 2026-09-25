# META FLOW — Sequencing

FLOW ID: META-SEQUENCING
STATUS: **ACTIVE / CANONICAL**
DOMAIN: meta
JOB: construct and govern the dependency-aware order of operations across composed Flows, Meta Flows, domain operations, patch sets, migrations, and verification steps
AUTHORITY: operational precedence / readiness / barrier / concurrency control only; no authority to change the goal, invent domain semantics, bypass gates, or grant action authority
PARENT GOALPOST: supplied by the calling execution, development, patch, domain, or learning context
UPSTREAM FLOWS: Pipeline Integrity, Xyool Execution, Development, Patching, Domain Configurer, Mapping, Learning, domain composite Flows
DOWNSTREAM FLOWS: selected operations/Flows, Patching, Audit, owning execution context
INBOUND PIPES: `PLUMBING.md#pipe-meta-integrity-sequencing`, `PLUMBING.md#pipe-meta-patching-sequencing`
OUTBOUND PIPES: operation graph / ready frontier return through owning Pipeline/Patch context
SOFTWARE DEPENDENCIES: none by default; deterministic DAG validation, locking, transactions, queues, and execution-state tracking may support exact enforcement

## GOAL

Determine what must happen before what, what can happen in parallel, where synchronization barriers are required, what is blocked by unmet prerequisites, and when earlier work must be invalidated/re-entered because new evidence changes the state.

Core law:

> **Order follows dependency, not convenience.**

Second law:

> **Do not serialize independent work, and do not parallelize dependent work.**

## GOALPOST

A sequencing plan is sufficient when:
- the operations required for the active objective are identified;
- hard prerequisites are explicit;
- domain-mandated order is preserved;
- independent operations are distinguishable from dependent ones;
- shared-state conflicts and transaction boundaries are identified;
- barriers/merge points are explicit;
- fail-closed gates block downstream work correctly;
- re-entry/invalidation rules are defined where new evidence can reopen earlier work;
- no unresolved cycle makes the operational order ambiguous;
- the current READY frontier can be identified.

## INPUT STATE

At minimum:
- active objective / goalpost;
- selected Flow(s) / Meta Flow(s);
- current state;
- operation set;
- declared upstream/downstream dependencies;
- applicable gates;
- domain-mandated sequence rules;
- patch/migration impact graph when applicable;
- state mutation / shared-resource information when applicable;
- authority boundaries;
- current execution epoch/version.

## EVIDENCE

Use the strongest available ordering evidence:

- Flow contracts and PROCESS/GATES;
- canonical Pipe contracts / live Pipe state;
- declared UPSTREAM FLOWS / DOWNSTREAM FLOWS;
- domain configuration;
- canonical domain run sequences;
- Mapping / Patching dependency graphs;
- schema/migration compatibility constraints;
- transaction / state-mutation boundaries;
- current dependency/state graphs;
- explicit user/goalpost order requirements;
- prior sequencing misses/regressions.

Do not infer a hard ordering rule merely because two steps were historically written next to each other.

Distinguish:
- **semantic dependency** — B needs A's output;
- **authority dependency** — B may not run before A grants eligibility;
- **state dependency** — B would read/mutate state A must establish first;
- **verification dependency** — B verifies A;
- **presentation order** — cosmetic only.

Only the first four constrain execution.

## PIPE RELATIONSHIP

Pipe contracts are durable connection truth.

Sequencing derives the current operation graph from material Pipe properties such as:
- prerequisite;
- barrier;
- conditional gate;
- mutex / safe parallelism;
- invalidation;
- readiness;
- execution epoch.

Core rule:

> **Pipe describes the connection; Sequencing describes the current execution state of that connection.**

Where a first-class Pipe exists, do not maintain a contradictory independent sequencing edge. Operation edges should reference or derive from the governing Pipe when practical.

## OPERATION GRAPH

Represent the active execution as a dependency-aware operation graph.

Minimum node:

~~~text
OPERATION ID:
FLOW / STEP:
PURPOSE:
INPUTS REQUIRED:
OUTPUTS PRODUCED:
READS:
WRITES:
GATE:
AUTHORITY REQUIRED:
STATUS:
EXECUTION EPOCH:
~~~

Minimum edge:

~~~text
FROM:
TO:
EDGE TYPE:
REASON:
HARD / SOFT:
~~~

## EDGE TYPES

Use:

~~~text
REQUIRES
  TO cannot begin until FROM completes successfully.

MUST_PRECEDE
  order is mandatory even when direct data dependency is weak.

BARRIER
  TO waits for all specified predecessor branches to resolve.

MUTEX
  operations may not overlap because they mutate/conflict with the same protected state/resource.

PARALLEL_OK
  explicit evidence that operations are independent enough to run concurrently.

CONDITIONAL
  TO becomes eligible only when a declared condition from FROM/state is true.

INVALIDATES
  completion/new evidence from FROM invalidates a prior downstream result and requires a new execution epoch/re-entry.

VERIFY_AFTER
  verification/audit step occurs only after the target operation/patch set is complete.
~~~

Do not use PARALLEL_OK to override a hidden dependency.

## OPERATION STATUS

Use:

~~~text
PLANNED
READY
RUNNING
WAITING
BLOCKED
COMPLETE
FAILED
INVALIDATED
SKIPPED_NOT_APPLICABLE
SUPERSEDED
~~~

READY means all hard prerequisites/gates for the current epoch are satisfied.

## PARTIAL ORDER, NOT RIGID LIST

Prefer a partial order.

Example:

~~~text
A → B → D
 → C ─┘
~~~

B and C may run independently after A.

D waits at a barrier for both.

Do not force:

~~~text
A → B → C → D
~~~

unless B must truly precede C.

## PROCESS

~~~text
LOAD ACTIVE OBJECTIVE / GOALPOST
→ IDENTIFY REQUIRED OPERATIONS
→ LOAD FLOW / DOMAIN / PATCH DEPENDENCIES
→ EXTRACT HARD GATES + AUTHORITY ORDER
→ IDENTIFY READ/WRITE + SHARED-STATE CONFLICTS
→ BUILD OPERATION GRAPH
→ CLASSIFY EDGES
→ VALIDATE HARD-DEPENDENCY GRAPH
→ IDENTIFY PARALLEL BRANCHES
→ IDENTIFY BARRIERS / MERGE POINTS
→ IDENTIFY CURRENT READY FRONTIER
→ EXECUTE / ROUTE READY OPERATIONS
→ RECORD OUTPUTS + STATE DELTAS
→ RE-EVALUATE READINESS
→ IF NEW EVIDENCE INVALIDATES PRIOR WORK:
      MARK AFFECTED RESULTS INVALIDATED
      START NEW EXECUTION EPOCH
      REBUILD ONLY THE AFFECTED DOWNSTREAM ORDER
→ WHEN TERMINAL OPERATIONS COMPLETE:
      ROUTE REQUIRED VERIFICATION / META AUDIT
~~~

## EXECUTION EPOCHS / RE-ENTRY

The hard dependency graph for one execution epoch should be acyclic.

When new evidence requires revisiting an earlier step, do not create an ambiguous permanent cycle such as:

~~~text
A → B → C → A
~~~

Instead:

~~~text
EPOCH 1:
A1 → B1 → C1

new evidence invalidates B1/C1

EPOCH 2:
B2 → C2
~~~

Preserve the old outputs as historical execution state.

Core rule:

> **Re-entry creates a new version of the affected work; it does not erase the path that already ran.**

## VERIFICATION HANDSHAKES

Avoid circular status dependencies.

Canonical patch example:

```text
PATCH APPLY COMPLETE
→ VERIFICATION_PENDING
→ AUDIT
→ VERIFIED
```

Invalid cycle:

```text
PATCH VERIFIED
→ AUDIT
→ PATCH VERIFIED
```

A verifier must be allowed to inspect the candidate state that precedes final promotion.

## GATES VS ORDER

A gate is stronger than ordinary precedence.

Example:

~~~text
QUALITY
→ eligibility gate
→ normal capital competition
~~~

Downstream work may be analytically explored in shadow mode if the domain permits, but authority cannot advance past the gate.

Sequencing must preserve:
- PASS;
- FAIL;
- BLOCKED;
- NOT APPLICABLE with reason.

Do not translate BLOCKED into READY.

## DOMAIN ORDER

Domain-mandated sequences are authoritative within their scope.

Example in stock analysis:

~~~text
freshness / identity
→ source authority
→ discovery
→ Quality
→ causal/event/TTC work
→ economics/payoff/recognition
→ strategy
→ downstream expression only if authorized
~~~

Sequencing may parallelize independent evidence acquisition, but may not reorder a domain gate merely for speed.

## PATCHING RELATIONSHIP

Patching answers:

> **What surfaces must change?**

Sequencing answers:

> **In what dependency-safe order should those patch operations occur?**

For non-trivial patch sets:

~~~text
PATCH IMPACT GRAPH
→ SEQUENCING
→ dependency-safe patch order / parallel branches / barriers
→ APPLY
→ VERIFY
→ AUDIT
~~~

Patching owns patch completeness.
Sequencing owns operational precedence.

## MAPPING / DOMAIN CONFIGURER RELATIONSHIP

Mapping can create dependencies because a target representation may require a source contract first.

Domain Configurer can create dependencies because a domain binding may require:
- Mapping;
- adapter normalization;
- schema/config availability;
- audit.

Sequencing consumes those dependencies. It does not decide their semantics.

## XYOOL EXECUTION RELATIONSHIP

Xyool Execution chooses/routs the Flows needed for the objective.

Sequencing orders the selected operations.

~~~text
EXECUTION:
what should run?

SEQUENCING:
what is READY now, and what must wait?
~~~

## SEQUENCING VS TIME / SCHEDULING

Sequencing controls **logical operational precedence**.

It does not determine:
- calendar event dates;
- catalyst timing;
- rhythm estimates;
- external scheduling.

Those belong to the relevant domain/time/timer Flow.

Example:

```text
DOMAIN TIMER:
event expected in Q4

SEQUENCING:
refresh source before evaluating the event
→ evaluate event before payoff
→ payoff before strategy authority
```

## CAUSAL GRAPH VS OPERATION GRAPH

Do not confuse:

~~~text
CAUSAL / DOMAIN DEPENDENCY GRAPH
= how reality or a modeled process unfolds

OPERATION GRAPH
= how Xyool must perform work safely/correctly
~~~

A causal edge can inform operation order, but the two graphs are not identical.

Example:
A customer procurement must precede deployment in reality.

Xyool may research procurement history and deployment capability in parallel because those research operations are independent.

## CONCURRENCY RULES

Parallel execution is allowed only when:
- no hard prerequisite exists between operations;
- no shared protected mutable state conflict exists;
- neither operation can invalidate the other's required input during execution;
- merge semantics are known;
- authority/gates permit it.

If uncertain:
prefer WAITING / serial order over unsafe concurrency.

## BARRIERS

Use a barrier when downstream reasoning requires a complete set of upstream results.

Example:

~~~text
CHARACTER A REFRESH ─┐
CHARACTER B REFRESH ─┼→ STORY READER
CHARACTER C REFRESH ─┘
~~~

The Reader should not finalize before every material required character branch is either:
- complete;
- blocked explicitly;
- or NOT APPLICABLE with reason.

## GATES

Before marking an operation READY:
- all hard REQUIRES/MUST_PRECEDE predecessors are complete;
- barriers are satisfied;
- required authority exists;
- required inputs are current enough;
- no MUTEX conflict is active;
- operation has not been invalidated by a newer execution epoch.

Before declaring the sequence COMPLETE:
- all terminal required operations have valid terminal status;
- no required operation remains PLANNED/WAITING without explicit closure;
- required verification/audit order is preserved.

## ADAPTATION

Sequencing may:
- reorder soft-preference operations;
- parallelize newly independent branches;
- collapse NOT-APPLICABLE branches;
- pause downstream work when an upstream result changes;
- create a new execution epoch after invalidation;
- insert verification barriers when risk increases.

It may not:
- bypass hard dependencies;
- weaken gates;
- convert a blocked prerequisite into a soft preference.

## BOUNDARIES

Sequencing does not:
- choose the system goal;
- decide domain truth;
- invent Mapping semantics;
- decide what a patch should change;
- grant capital/action authority;
- change a Flow's required gate to improve throughput;
- treat chronological order of evidence as operational precedence without reason.

## FAIL-CLOSED CONDITIONS

Return BLOCKED when:
- hard dependencies form an unresolved cycle;
- prerequisite identity is ambiguous;
- two operations require incompatible simultaneous mutation;
- a required barrier cannot be satisfied;
- a domain-mandated order conflicts with a proposed generic order;
- current-state freshness makes readiness unknowable;
- required authority/gate state is unknown.

## OUTPUT STATE

~~~text
SEQUENCE ID:
EXECUTION EPOCH:
OBJECTIVE / GOALPOST:
GRAPH STATUS:
OPERATIONS:
DEPENDENCY EDGES:
READY FRONTIER:
WAITING:
BLOCKED:
PARALLEL GROUPS:
BARRIERS:
MUTEX GROUPS:
INVALIDATED PRIOR OUTPUTS:
TERMINAL CONDITIONS:
NEXT READY OPERATIONS:
~~~

## LEARNING HOOK

A Sequencing Miss occurs when:
- an operation ran before a required prerequisite;
- a domain gate was bypassed;
- independent work was unnecessarily serialized and materially harmed efficiency;
- dependent work ran concurrently and created stale/conflicting state;
- a merge occurred before required branches finished;
- an invalidated result was reused;
- a re-entry erased historical execution instead of creating a new epoch;
- a cycle/deadlock was not detected.

Recurring misses should improve:
- declared Flow dependencies;
- domain sequencing rules;
- barrier definitions;
- read/write declarations;
- deterministic DAG/lock support.

## SOFTWARE / HARD-LIMIT BOUNDARY

Floware is sufficient for reasoning about operation order.

Deterministic software may be justified for:
- DAG/cycle validation;
- queues/schedulers;
- concurrency locks;
- transactions;
- exact readiness computation;
- distributed execution;
- crash recovery;
- durable execution epochs.

Software enforces the Sequencing contract; it does not define the reasoning semantics.
