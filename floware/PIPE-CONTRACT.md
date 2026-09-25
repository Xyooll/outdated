# Pipe Contract

Status: **CANONICAL**

A Pipe is the governed connection between Floware endpoints.

A Pipe is not a Flow.

A Flow owns reasoning/work.
A Pipe owns the validity of the connection through which outputs, state, evidence, control, or authority become available to another endpoint.

Core law:

> **Flow correctness does not imply Pipe correctness.**

## Representation pattern

Canonical Pipe representation:

~~~text
PIPE
=
ENDPOINT POINTERS
+
CONNECTION WRAPPER
+
LIVE PIPE STATE
~~~

### Endpoint pointers

Pointers identify the canonical source and target objects without duplicating them.

Minimum:

~~~text
FROM POINTER:
  flow / stage / object id
  output / state path
  version / contract pointer where material

TO POINTER:
  flow / stage / object id
  input / state path
  version / contract pointer where material
~~~

A pointer answers:

> **Where is the canonical underlying object/state?**

Pointers may resolve through IDs, paths, keys, references, graph addresses, or another deterministic addressing mechanism.

A pointer is not automatically a Pipe.

### Connection wrapper

The wrapper owns the relationship-specific contract between the pointed endpoints.

A wrapper answers:

> **Under what conditions may the source be interpreted, transformed, transported, authorized, or consumed by the target?**

Minimum material fields:

~~~text
PIPE ID:
STATUS:
DOMAIN / SCOPE:

FROM POINTER:
TO POINTER:

SOURCE CONTRACT:
TARGET CONTRACT:

MAPPING / TRANSFORMATION:
SEMANTIC INVARIANTS:
LOSS / COMPRESSION:

PROVENANCE REQUIREMENTS:
FRESHNESS / AS-OF REQUIREMENTS:
VERSION / COMPATIBILITY REQUIREMENTS:
UNCERTAINTY / CONFIDENCE PRESERVATION:

AUTHORITY IN:
AUTHORITY OUT:
GATE / CONDITION:

SEQUENCING:
  prerequisite
  barrier / merge
  parallel / mutex
  conditional
  invalidation

FAILURE BEHAVIOR:
INVALIDATION / RE-ENTRY:
AUDIT STATUS:
~~~

Not every Pipe requires every field to be materialized.

The wrapper must contain enough information to preserve every material invariant of the connection.

### Live Pipe state

The Pipe may also carry current operational state separate from its durable wrapper contract.

Examples:

~~~text
source_version
target_version
source_as_of
compatibility
readiness
gate_state
blocked_reason
last_validated_at
execution_epoch
invalidation_state
~~~

Durable Pipe contract and current Pipe state must not be confused.

## Pipe identity

Pipe identity belongs to the relationship, not merely the endpoint names.

If a materially different semantic relationship connects the same endpoints, it may require a different Pipe ID.

Example:

~~~text
FLOW A → FLOW B

PIPE 1 = evidence/state transfer
PIPE 2 = authority gate
~~~

These may remain separate if their contracts, invalidation, or audit behavior materially differ.

Do not proliferate Pipe types merely for naming convenience.

## Pointer rule

Pointers prevent duplication.

Do not copy the full source/target Flow contract into every Pipe when a stable pointer can resolve the canonical contract.

When the pointed object changes version, Patching must evaluate whether the Pipe wrapper remains compatible.

## Wrapper rule

Wrappers preserve context.

The same canonical source object may participate in different Pipes whose wrappers legitimately interpret or constrain that source differently.

A wrapper may not:
- redefine the canonical source object;
- invent missing evidence;
- silently strengthen confidence;
- silently broaden authority;
- silently change units/meaning;
- hide material information loss.

## Semantic integrity

Matching field names do not prove semantic compatibility.

Example:

~~~text
source:
confidence = HIGH

target:
P(Hit) = numeric probability
~~~

A Pipe may not silently map:

~~~text
HIGH → 0.80
~~~

without an earned Mapping/calibration.

Use `meta/mapping.flow.md` when representation alignment is not explicit.

## Provenance integrity

Where downstream claims depend on upstream evidence, provenance must survive the Pipe.

A Pipe may compress provenance only when the target contract permits the loss and the original source remains recoverable where auditability requires it.

## Freshness / version integrity

A Pipe must know enough to detect whether downstream consumption relies on stale or incompatible upstream state.

When a material upstream change invalidates the Pipe:

~~~text
UPSTREAM VERSION / STATE CHANGES
→ PIPE compatibility/readiness re-evaluated
→ affected downstream outputs INVALIDATED
→ Sequencing creates new execution epoch/re-entry
~~~

Do not silently preserve downstream conclusions across an incompatible Pipe revision.

## Authority integrity

Authority cannot silently increase through a Pipe.

~~~text
downstream authority
<= authority explicitly permitted by upstream + target governing contract
~~~

Example:

~~~text
ANALYSIS
→ Pipe
→ EXECUTION
~~~

is BLOCKED unless a separate explicit authority contract grants execution.

## Sequencing relationship

Pipe contracts are durable connection truth.

Sequencing derives current operational precedence/readiness from:
- Pipe prerequisites;
- barriers;
- conditions;
- mutex/parallel constraints;
- gate state;
- invalidation state.

Core rule:

> **Pipe describes the connection; Sequencing describes the current execution state of that connection.**

Do not maintain contradictory independent order rules in both places.

## Patching relationship

When a Flow, schema, Mapping, domain binding, or endpoint contract changes:

~~~text
CHANGE
→ traverse affected inbound/outbound Pipes
→ validate wrappers
→ identify affected connected Flows / state / tests
→ patch the connected subgraph
~~~

Reference/semantic search remains a backstop for undeclared/missing Pipes.

## Audit relationship

Audit may inspect:
- the Pipe wrapper;
- endpoint pointer resolution;
- live Pipe state;
- semantic compatibility;
- provenance/freshness/version;
- uncertainty preservation;
- authority preservation;
- sequencing/invalidation behavior.

## Fail-closed conditions

A Pipe is BLOCKED when a material connection cannot establish:
- endpoint identity;
- source/target compatibility;
- required Mapping;
- provenance continuity;
- compatible version/freshness;
- authority legality;
- gate/readiness state.

Unknown connection integrity is not equivalent to PASS.

## Historical preservation

When a Pipe contract changes materially:
- preserve prior versions needed to reconstruct historical pipeline runs;
- do not rewrite old pipeline evidence to make it appear to have used the new Pipe;
- create a new Pipe version or superseding record as appropriate.

## Software / hard-limit boundary

Floware owns Pipe semantics.

Deterministic software may support:
- pointer resolution;
- stable IDs;
- schema validation;
- version checks;
- graph traversal;
- locks/transactions;
- durable Pipe state;
- invalidation propagation;
- provenance hashes.

Software enforces the Pipe contract; it does not decide the semantic relationship.
