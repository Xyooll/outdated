# Xyool Domain Establishment Contract

Status: **CANDIDATE / VERIFICATION_PENDING**

Purpose: define the minimum domain-native substance that must exist before Meta Domain Configurer can validly bind a domain to Floware.

Core law:

> **Core can provide the questions and reusable capabilities. The domain must provide its own answers, rules, functions, evidence, and boundaries.**

A domain manifest, directory, configuration file, or mapped vocabulary is not sufficient evidence that the domain is established.

## 1. Domain establishment record

Every new or materially expanded domain should be able to produce:

~~~text
DOMAIN ESTABLISHMENT ID:
DOMAIN:
VERSION:
CLAIMED SCOPE:
STATUS:
OBJECTIVE:
ANALYSIS / DECISION UNIT:
AUTHORITY:
NATIVE OBJECTS:
NATIVE RELATIONSHIPS:
NATIVE STATE / TRANSITIONS:
TIME / TIMER SEMANTICS:
EVIDENCE / SOURCE HIERARCHY:
UNCERTAINTY / INVALIDATION:
OUTCOME / SUCCESS:
FAILURE / LOSS:
MEMORY / PERSISTENCE NEEDS:
VALIDATION / CONTROL NEEDS:
FUNCTIONS:
UNSUPPORTED / DEFERRED FUNCTIONS:
CORE CAPABILITY NEEDS:
MISSING DOMAIN KNOWLEDGE:
MISSING DOMAIN RULES:
MISSING DOMAIN FLOWS:
MISSING CORE CAPABILITIES:
ESTABLISHMENT READINESS:
~~~

The record describes what the domain is and can do natively.

Meta Domain Configurer later describes how that established domain binds to Floware.

## 2. Function contract

A domain function is a material job the domain claims it can perform.

Every required function should account for:

~~~text
FUNCTION ID:
JOB:
AUTHORITY:
INPUTS:
OUTPUTS:
NATIVE OBJECTS:
RULE / METHOD SET:
EVIDENCE / SOURCE REQUIREMENTS:
STATE / TRANSITION SEMANTICS:
TIME / TIMER SEMANTICS:
GATES:
FAILURE CONDITIONS:
UNCERTAINTY / INVALIDATION:
OUTCOME / SUCCESS:
VALIDATION / CONTROL REQUIREMENTS:
DOMAIN FLOW OWNER:
CORE CAPABILITY NEEDS:
DEPENDENCIES:
ESTABLISHMENT STATUS:
BLOCKERS:
~~~

A function may be narrow. It does not need to model the entire domain.

## 3. Establishment statuses

Domain-level:

~~~text
UNESTABLISHED
FOUNDATION_PARTIAL
FUNCTIONS_PARTIAL
READY_FOR_CONFIGURATION
BLOCKED
SUPERSEDED
~~~

Function-level:

~~~text
UNDEFINED
PARTIAL
READY_FOR_CONFIGURATION
NOT_APPLICABLE
BLOCKED
~~~

These are establishment states, not empirical-validation or release states.

READY_FOR_CONFIGURATION means the native domain substance is sufficient for Meta Domain Configurer to attempt bindings for the claimed scope.

It does not mean empirically true, operationally validated, promoted, or authorized for external action.

## 4. Native-rule requirement

When a function depends on domain rules, methods, thresholds, source traditions, or causal/interpretive semantics, those must exist before the function can be READY_FOR_CONFIGURATION.

A schema for rules is not a rule set.
A source list is not a rule set.
A system registry is not a rule set.

Required domain rules may be source-documented, established domain practice, user-defined framework, or Xyool hypothesis. Their provenance/status must remain explicit.

## 5. Core-to-domain feed

Core does not invent local semantics.

Core supplies reusable reasoning questions/capabilities such as:

~~~text
What is the object?
What is the state?
What changes state?
What evidence establishes it?
What counts as fresh/stale?
What is uncertain?
What invalidates the claim?
What function is being performed?
What are its inputs/outputs?
What must happen first?
What can fail?
What counts as success?
How is an outcome closed?
What can be learned?
What authority is allowed?
What resource horizon is justified?
~~~

The domain answers those questions in its own language.

Core capabilities may then support the domain: Research, Evidence-to-State, Direct Resolution, Question Frontier, Learning, Correspondence, Relational Story where applicable, Observation/Trigger, Resource Allocation, and Execution.

Meta capabilities later bind/map/configure the established answers.

## 6. Missing-capability classification

~~~text
MISSING DOMAIN KNOWLEDGE
MISSING DOMAIN SOURCE
MISSING DOMAIN RULE / METHOD
MISSING DOMAIN FUNCTION
MISSING DOMAIN FLOW
MISSING MEASUREMENT / OUTCOME DEFINITION
MISSING VALIDATION METHOD
MISSING CORE CAPABILITY
MISSING SOFTWARE HARD-LIMIT SUPPORT
UNKNOWN
~~~

Do not classify a missing domain rule as a missing core primitive.

Do not create a new core abstraction until the domain-local requirement is understood and there is evidence it generalizes.

## 7. Scope rule

A domain does not need to be complete in every imaginable function before use. It must be complete for the claimed scope.

Example:

~~~text
ASTROLOGY
descriptive chart calculation/interpretation
→ may be READY_FOR_CONFIGURATION

ASTROLOGY
prospective Western transit prediction
→ remains FUNCTIONS_PARTIAL if Western predictive rule objects are missing
~~~

## 8. Configuration boundary

Correct order:

~~~text
DOMAIN OBJECTIVE
→ CORE DOMAIN ESTABLISHMENT
→ domain-native foundation + function contracts
→ READY_FOR_CONFIGURATION?
    NO → Research / Development / Question Frontier / local rule work
    YES
      ↓
META MAPPING + DOMAIN CONFIGURER
→ Floware bindings / Plumbing
→ Sequencing
→ Audit
→ configured domain scope
~~~

Incorrect order:

~~~text
create domain folder
→ create CONFIGURATION.md
→ assume domain functions exist
~~~

## 9. Function-expansion rule

When an established domain gains a new material function:

~~~text
NEW FUNCTION REQUEST
→ DOMAIN ESTABLISHMENT for that function
→ establish native rules/evidence/outcome contract
→ READY_FOR_CONFIGURATION
→ Domain Configurer / Mapping
→ update Plumbing / domain Flow
→ Audit
~~~

Existing domain configuration does not automatically validate a newly added function.

## 10. Software boundary

The Domain Establishment Contract is reasoning architecture.

Software may later support exact calculation, parsing, persistence, identity, high-volume validation, or deterministic schema checking.

Software does not replace domain-native rule establishment.


## 10. Domain update / delta contract

Existing domains evolve by delta.

A new material function, rule family, evidence source class, state model, outcome model, or core-capability binding re-enters Domain Establishment without rebuilding unaffected domain scope.

Minimum update record:

~~~text
DOMAIN UPDATE ID:
DOMAIN:
PRIOR ESTABLISHMENT ID / VERSION:
REQUESTED CAPABILITY / FUNCTION:
UPDATE TYPE:
CLAIMED NEW SCOPE:

AFFECTED FUNCTIONS:
UNAFFECTED FUNCTIONS:
NEW / CHANGED NATIVE OBJECTS:
NEW / CHANGED RULES / METHODS:
NEW / CHANGED EVIDENCE REQUIREMENTS:
NEW / CHANGED STATE / TIME SEMANTICS:
NEW / CHANGED OUTCOME / VALIDATION:
CORE FLOWS TO REUSE:
NEW DOMAIN FLOWS IF ANY:
MAPPINGS / CONFIGURATION AFFECTED:
PIPES AFFECTED:
STATE / MEMORY MIGRATION:
INVALIDATIONS:
DEFERRED GAPS:
NEW ESTABLISHMENT STATUS:
RECONFIGURATION SCOPE:
~~~

Update types may include:

~~~text
NEW_FUNCTION
FUNCTION_EXPANSION
RULESET_EXPANSION
EVIDENCE_EXPANSION
STATE_MODEL_CHANGE
OUTCOME_MODEL_CHANGE
CORE_BINDING_CHANGE
LOCAL_CALIBRATION_CHANGE
DEPRECATION / RETIREMENT
~~~

Core law:

> **Preserve established domain history; establish only the delta; reconfigure only what the delta affects.**

A new function does not inherit readiness merely because adjacent functions are ready.

An unchanged function does not lose readiness merely because another function is partial, unless the update invalidates a shared dependency.

## 11. Story-capability reuse

When a domain's new capability is structurally a past→present reconstruction or present→future branching problem, Domain Establishment should test reuse of:

- `core/relational-story.flow.md`;
- `core/story-reader.flow.md`;
- `core/story-writer.flow.md`.

The domain must still establish:
- what counts as the root/characters or other native state objects;
- which relationships/state transitions matter;
- which native rules authorize transitions;
- what timers/windows exist;
- what counts as observable proof/invalidation;
- what Story Reader/Writer authority is allowed.

Do not create a domain-specific future engine when the actual job is Story Writer plus domain-local transition rules.

Do not force domain objects into Character semantics when state/timer/process semantics fit better.
