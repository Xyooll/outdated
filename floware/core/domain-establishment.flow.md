# FLOW — Domain Establishment

FLOW ID: CORE-DOMAIN-ESTABLISHMENT
STATUS: **CANDIDATE / VERIFICATION_PENDING**
DOMAIN: core
JOB: establish the native foundation and material functions of a new or expanded domain before Meta configuration/binding
AUTHORITY: domain-foundation and function-readiness coordination only; no empirical validation, domain activation, core promotion, or external-action authority
PARENT GOALPOST: ../../research/system-tests/domain-establishment-v1-2026-09-24/GOALPOST.md
UPSTREAM FLOWS: Xyool Execution, Development, user-authorized domain objective; existing domain state when expanding a domain
DOWNSTREAM FLOWS: Domain Library, Research, Direct Resolution, Question Frontier, Evidence-to-State, Development, Correspondence when transfer is proposed, Pipeline Integrity after READY_FOR_CONFIGURATION
INBOUND PIPES: PLUMBING.md#pipe-core-execution-domain-establishment, PLUMBING.md#pipe-core-library-domain-establishment
OUTBOUND PIPES: PLUMBING.md#pipe-core-domain-establishment-library, PLUMBING.md#pipe-core-domain-establishment-integrity
SOFTWARE DEPENDENCIES: none

## GOAL

Turn an intended domain capability into enough domain-native substance that Meta Domain Configurer can bind it to Floware without inventing missing domain semantics.

Core law:

> **Establish the domain before configuring the domain. Establish each claimed function before routing work through it.**

## GOALPOST

The claimed domain scope is READY_FOR_CONFIGURATION only when:
- domain identity/objective/authority are explicit;
- native objects/relationships/state/time semantics are sufficient for scope;
- material evidence/source requirements are explicit;
- uncertainty/invalidation/outcome/failure semantics are explicit;
- every required domain function has a function contract;
- every required function's native rules/methods actually exist or are explicitly source-free deterministic operations;
- missing knowledge/rules/functions are resolved or marked outside claimed scope;
- domain Flow owners are identified or a bounded Development task is defined;
- validation/control requirements are explicit when claims require them;
- missing core capabilities are distinguished from missing local domain content;
- establishment status is auditable.

## INPUT STATE

At minimum:
- intended domain identity;
- user objective;
- claimed scope/function request;
- current domain manifest/files if any;
- known native concepts;
- known evidence/sources;
- existing domain rules/methods;
- existing domain Flows;
- applicable core capabilities;
- current authority boundary.

## EVIDENCE

Use:
- domain source materials;
- existing domain manifests;
- rule/method registries;
- domain-native standards;
- observed function requirements;
- prior domain outcomes/misses;
- user-originated domain definitions where they are the intended framework;
- core contracts only as reusable scaffolding, not as local semantics.

## PROCESS

~~~text
LOCK DOMAIN + CLAIMED SCOPE
→ LOAD ../DOMAIN-CONTRACT.md
→ LOAD PRIOR ESTABLISHMENT RECORD / VERSION IF DOMAIN ALREADY EXISTS
→ CLASSIFY NEW DOMAIN vs DOMAIN UPDATE
→ IF UPDATE: BUILD DOMAIN DELTA + AFFECTED/UNAFFECTED FUNCTION SET
→ INVENTORY CURRENT DOMAIN-NATIVE SUBSTANCE
→ QUERY CORE DOMAIN LIBRARY FOR EXISTING RULES / METHODS / BOUNDARIES / CASES
→ IDENTIFY REQUIRED FUNCTIONS FOR THE CLAIMED SCOPE
→ IF MEANING-DEPENDENT DOMAIN / FUNCTION:
     IDENTIFY MEANING-BEARING OBJECTS
     ROUTE SEMANTIC MODEL TO CORE-MEANING-ATTRIBUTION
     REQUIRE INTRINSIC / EXTRINSIC / COMPOSITE RULES AS APPLICABLE
→ PRESERVE UNAFFECTED READY FUNCTIONS UNLESS A SHARED DEPENDENCY IS INVALIDATED
→ FOR EACH REQUIRED FUNCTION:
      DEFINE JOB + AUTHORITY
      DEFINE INPUTS / OUTPUTS
      DEFINE NATIVE OBJECTS / STATE / TIME
      AUDIT ACTUAL RULE / METHOD COVERAGE
      AUDIT EVIDENCE / SOURCE COVERAGE
      DEFINE GATES / FAILURE / INVALIDATION
      DEFINE OUTCOME / SUCCESS / VALIDATION
      IDENTIFY DOMAIN FLOW OWNER
      CLASSIFY FUNCTION READINESS
→ CLASSIFY GAPS ONLY AFTER LIBRARY + CANONICAL POINTER CHECK
→ FOR LOCAL KNOWLEDGE / RULE GAPS:
      IF DOMAIN-SPECIFIC ESTABLISHMENT SUBFLOW EXISTS: CALL IT
      ELSE:
        DIRECT RESOLUTION
        → RESEARCH
        → QUESTION FRONTIER IF NEEDED
        → ESTABLISH / VERSION DOMAIN RULES
      RETURN RESULT TO DOMAIN ESTABLISHMENT RECORD
→ FOR DOMAIN FLOW GAPS:
      DEVELOPMENT
→ FOR PROPOSED CROSS-DOMAIN STRUCTURE:
      CORRESPONDENCE
      → TEST LOCALLY
→ FOR POSSIBLE MISSING CORE CAPABILITY:
      PROVE DOMAIN-LOCAL NEED FIRST
      → DEVELOPMENT ONLY IF REUSABLE
→ WRITE BACK NEW REUSABLE DOMAIN KNOWLEDGE / POINTERS TO DOMAIN LIBRARY
→ RECHECK FUNCTION INVENTORY
→ IF UPDATE: DEFINE RECONFIGURATION / PATCH SCOPE ONLY FOR AFFECTED FUNCTIONS + BINDINGS
→ IF REQUIRED FUNCTIONS READY:
      DOMAIN STATUS = READY_FOR_CONFIGURATION
      PIPE TO PIPELINE INTEGRITY
→ ELSE:
      DOMAIN STATUS = FOUNDATION_PARTIAL / FUNCTIONS_PARTIAL / BLOCKED
      STOP BEFORE META CONFIGURATION FOR UNSATISFIED SCOPE
~~~

## FUNCTION ESTABLISHMENT

Use the canonical function contract in ../DOMAIN-CONTRACT.md.

A domain function is not established merely because a Flow file exists, a schema exists, a system is named, sources are listed, an example works, or another domain has an analogous rule.

The function's local rules/evidence/outcome semantics must support the claimed job.

## CORE FEED

Core's role is to supply the reusable reasoning scaffold.

Core asks, for each function:
- what is being acted on/analyzed?
- what state is relevant?
- what establishes state?
- what changes it?
- what evidence is authoritative?
- what is uncertain?
- what can invalidate it?
- what rules/methods govern the function?
- what must happen first?
- what can fail?
- what output is produced?
- what counts as success/outcome?
- what can be learned?

The domain supplies the local answers.

Core must not fill an unanswered domain question with semantics copied from another domain.

## GATES

Before READY_FOR_CONFIGURATION:
- claimed scope explicit;
- function inventory explicit;
- required functions each have a contract;
- required native rules/methods exist;
- evidence/source authority explicit;
- state/time/outcome semantics sufficient;
- validation/control path explicit for empirical/predictive claims;
- missing items classified;
- no required local gap is disguised as a Mapping/configuration problem.

Before handing a new core capability request to Development:
- the domain-local need is understood;
- existing core capabilities are insufficient;
- the proposed abstraction is plausibly reusable beyond one local noun/calibration.

## ADAPTATION

A domain may be established for one scope and partial for another.

Example:

~~~text
domain: astrology
function: source-preserved Maya interpretation
→ potentially READY_FOR_CONFIGURATION

function: Western prospective transit prediction
→ FUNCTIONS_PARTIAL until predictive rules are established
~~~

When a new function is requested later, re-enter Domain Establishment for that function without invalidating unrelated established functions.

## BOUNDARIES

Domain Establishment does not:
- configure mappings between the domain and Floware;
- declare empirical validity;
- promote a domain/function lifecycle;
- grant action authority;
- create software by default;
- transfer thresholds/calibrations from another domain;
- require every possible domain function before a narrower scope can proceed.

Those jobs remain with Domain Configurer/Mapping, Validation/Evaluation, Promotion, Execution, Software Escalation, or the owning domain.

## FAIL-CLOSED CONDITIONS

Return FUNCTIONS_PARTIAL or BLOCKED when:
- a required function lacks actual native rules/methods;
- rule/source provenance is materially unresolved;
- required outcomes/failure conditions cannot be defined;
- the domain Flow claims functionality the native domain substrate cannot support;
- required validation is impossible for the claimed empirical authority;
- a local semantic gap is being papered over by generic core language.

## OUTPUT STATE

~~~text
DOMAIN ESTABLISHMENT ID:
PRIOR ESTABLISHMENT ID / VERSION:
UPDATE TYPE / DOMAIN UPDATE ID:
DOMAIN / VERSION:
CLAIMED SCOPE:
ESTABLISHMENT STATUS:
OBJECTIVE:
AUTHORITY:
NATIVE FOUNDATION:
FUNCTION INVENTORY:
FUNCTION READINESS:
RULE / METHOD COVERAGE:
EVIDENCE / SOURCE COVERAGE:
STATE / TIME / OUTCOME COVERAGE:
VALIDATION / CONTROL COVERAGE:
DOMAIN FLOW OWNERS:
CORE CAPABILITY NEEDS:
MISSING DOMAIN KNOWLEDGE:
MISSING DOMAIN RULES:
MISSING DOMAIN FLOWS:
MISSING CORE CAPABILITIES:
AFFECTED FUNCTIONS:
UNAFFECTED FUNCTIONS:
RECONFIGURATION SCOPE:
INVALIDATIONS:
DEFERRED / OUT-OF-SCOPE FUNCTIONS:
NEXT OWNER:
~~~

## LEARNING HOOK

Domain-establishment misses route to Learning.

Recurring misses may improve the Domain Contract, establishment questions, function-readiness gates, or core capabilities.

A missing local rule is not automatically a core-learning candidate.

## SOFTWARE / HARD-LIMIT BOUNDARY

NONE — FLOWARE SUFFICIENT

Exact calculators/parsers/persistence may later support an established function through Software Escalation. They cannot establish missing domain semantics.

## COMPLEXITY RULE

Establish only the functions required for the current claimed scope. Do not attempt to fully formalize an entire human knowledge domain before useful bounded work can begin.


## DOMAIN-SPECIFIC ESTABLISHMENT SUBFLOWS

A domain may define specialized establishment helpers when a local foundation job is complex enough to deserve its own Flow.

Examples:
- astrology rule foundation;
- a legal-jurisdiction authority foundation;
- a scientific measurement-method foundation.

These subflows:
- remain domain-local;
- answer a specific missing-domain-content job;
- return their result to Core Domain Establishment;
- do not independently declare the whole domain/function configured or active.

Core Domain Establishment remains the owner of scoped domain/function establishment readiness.


## DOMAIN UPDATE / DELTA MODE

When the domain already exists, establishment begins from its prior established state rather than from zero.

~~~text
EXISTING DOMAIN ESTABLISHMENT
→ NEW CAPABILITY REQUEST
→ CLASSIFY UPDATE
→ IDENTIFY FUNCTION DELTA
→ IDENTIFY SHARED DEPENDENCIES
→ PRESERVE UNAFFECTED READY FUNCTIONS
→ ESTABLISH ONLY NEW / INVALIDATED NATIVE SUBSTANCE
→ RE-EVALUATE AFFECTED FUNCTION CONTRACTS
→ EMIT MINIMUM RECONFIGURATION SCOPE
~~~

Required update questions:

- What exact new function is being requested?
- Which existing functions does it depend on?
- Which existing rules/state/evidence can be reused unchanged?
- Which native rules or methods are actually missing?
- Does the request map onto an existing Core capability?
- Does it invalidate any shared domain assumptions?
- Which configuration/mapping/Pipes must change?
- Which domain surfaces are explicitly unaffected?

For a function expansion, the old function version remains part of domain history. Do not rewrite prior establishment records to make the new function appear to have always existed.

### Story-shaped updates

If the requested capability is structurally:
- reconstructing how history produced current state; or
- writing conditional future branches from current state,

test whether Relational Story + Story Reader/Writer already provide the reusable Core function.

Correct pattern:

~~~text
DOMAIN HISTORY / STATE / RULES
→ STORY READER under domain binding
→ CURRENT DOMAIN STORY
→ STORY WRITER under domain transition/timing rules
→ CONDITIONAL FUTURE STORY
→ domain-specific forecast / strategy / output wrapper
~~~

The Core story machinery supplies structure.

The domain supplies:
- valid transition rules;
- state/timer semantics;
- character/relationship semantics where applicable;
- evidence authority;
- branch proof/invalidation;
- output meaning.

A missing domain transition rule remains a domain-establishment gap, not a Story Writer defect.


## DOMAIN LIBRARY INTEGRATION

Domain Establishment should become cheaper and more reliable as the domain matures.

Use:

~~~text
PRIOR DOMAIN ESTABLISHMENT
+ DOMAIN LIBRARY
→ current reusable native knowledge
→ identify only real gaps
→ Research / local establishment work
→ update canonical domain artifacts
→ write reusable result back to library
~~~

A missing rule/source/knowledge classification is invalid until the Domain Library and its canonical pointers have been checked.

The library is not proof that a rule works. Establishment still checks the underlying canonical rule, evidence, validation status, and function contract.


## MEANING-DEPENDENT DOMAIN RULE

Some domains cannot be established by factual/state/rule coverage alone because the domain's function depends on meaning itself.

Examples include:
- symbolic systems;
- occult/metaphysical systems;
- ritual systems;
- mythology;
- divination;
- narrative/artistic systems;
- user-created semantic frameworks.

For these domains, Domain Establishment must determine:
- what objects/patterns may carry meaning;
- whether meaning is intrinsic, extrinsic, composite, or unknown;
- who/what assigns that meaning;
- which claim modes are allowed;
- how meanings combine/conflict;
- what validation is required for descriptive, causal, or predictive use.

Canonical Core semantic contract:
`../MEANING-CONTRACT.md`

Canonical Flow:
`meaning-attribution.flow.md`

A domain may be READY_FOR_CONFIGURATION for symbolic/creative interpretation while remaining unvalidated for causal/predictive claims.
