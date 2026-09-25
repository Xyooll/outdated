# META FLOW — Domain Configurer

FLOW ID: META-DOMAIN-CONFIGURER
STATUS: **ACTIVE / CANONICAL**
DOMAIN: meta
JOB: configure a domain to use Floware by identifying its native semantics, selecting applicable core/general Flows, consuming explicit mappings, detecting capability gaps, and producing a validated domain configuration without contaminating core contracts
AUTHORITY: configuration / compatibility / routing only; no domain activation, empirical validation, or external-action authority
PARENT GOALPOST: supplied by domain creation/modification objective
UPSTREAM FLOWS: Core Domain Establishment through Pipeline Integrity, Mapping, Patching, domain manifest, core Flow contracts, existing domain Flows, Correspondence when imported principles are proposed
DOWNSTREAM FLOWS: Sequencing, domain Flows, Relational Story, Evidence-to-State, Memory/State, Audit, Learning, Correspondence, Xyool Execution
INBOUND PIPES: `PLUMBING.md#pipe-meta-integrity-configurer`
OUTBOUND PIPES: validated domain binding returns through owning Pipeline/Pipe wrapper
SOFTWARE DEPENDENCIES: none by default; deterministic schema/persistence validators may support configuration integrity

## GOAL

Turn an already-established domain scope into an explicit, auditable Floware configuration that states how the domain uses general Xyool contracts while preserving domain-specific semantics locally.

Core law:

> **Configure the established domain to Floware; do not use configuration to invent the domain.**

## GOALPOST

A domain configuration is complete when:
- domain identity/objective/authority are explicit;
- domain-native primitives are identified;
- applicable Floware contracts are selected;
- required domain-to-Floware mappings exist;
- local semantics, evidence, time, state, outcome, memory, audit, and learning rules are explicit;
- unsupported capabilities are named;
- domain-specific calibrations remain local;
- imported principles carry correspondence status;
- the configuration passes Meta Audit or is explicitly BLOCKED/EXPERIMENTAL.

## INPUT STATE

Load:
- Core Domain Establishment record with status `READY_FOR_CONFIGURATION` for the claimed scope;
- prior domain configuration/version when updating an existing domain;
- Domain Establishment delta record including affected/unaffected functions and reconfiguration scope when applicable;
- domain manifest and status;
- domain objective / user or decision unit;
- native entities/objects;
- native relationships;
- evidence/source hierarchy;
- state and transition semantics;
- time/timer semantics;
- actions/authority;
- outcome/failure semantics;
- persistence/freshness requirements;
- validation and anti-lookahead rules;
- relevant core/general Flow contracts;
- existing mappings and correspondence objects.

## PROCESS

~~~text
IDENTIFY DOMAIN + VERSION + CLAIMED SCOPE
→ LOAD DOMAIN ESTABLISHMENT RECORD
→ REQUIRE ESTABLISHMENT STATUS = READY_FOR_CONFIGURATION
→ LOAD DOMAIN MANIFEST / CURRENT FLOWS / STATE CONTRACT
→ DECOMPOSE DOMAIN-NATIVE PRIMITIVES
→ IDENTIFY REQUIRED FLOWARE CAPABILITIES
→ IF DOMAIN UPDATE: PRESERVE UNAFFECTED VALID BINDINGS AND LIMIT WORK TO DECLARED RECONFIGURATION SCOPE
→ SELECT APPLICABLE CORE / GENERAL FLOWS
→ CALL MAPPING META FLOW FOR EACH MATERIAL DOMAIN↔FLOWARE BOUNDARY
→ BIND LOCAL SEMANTICS TO GENERAL CONTRACTS
→ DECLARE EVIDENCE / TIME / STATE / MEMORY / OUTCOME / AUTHORITY RULES
→ DECLARE RESOURCE + FRESHNESS POLICIES
→ IDENTIFY REQUIRED ADAPTERS / DETERMINISTIC SUPPORT
→ DETECT UNSATISFIED CAPABILITIES / GAPS
→ PRESERVE LOCAL CALIBRATIONS + NON-TRANSFER RULES
→ PRODUCE DOMAIN CONFIGURATION
→ RUN META AUDIT
→ REGISTER / UPDATE DOMAIN ONLY AT EARNED STATUS
~~~

## DOMAIN CONFIGURATION CONTRACT

A configuration should account for the following where applicable:

~~~text
DOMAIN IDENTITY / VERSION
STATUS / MATURITY
PRIMARY OBJECTIVE
DECISION / ANALYSIS UNIT
AUTHORITY BOUNDARIES

ENTITY / OBJECT SEMANTICS
CHARACTER PROFILE SEMANTICS
QUANTITATIVE TRAIT POLICY
QUALITATIVE TRAIT POLICY
ARCHETYPE POLICY / DOMAIN REGISTRY
CHARACTER TRANSFORMATION SEMANTICS
RELATIONSHIP SEMANTICS
EVENT SEMANTICS
STATE SEMANTICS
STATE-TRANSITION SEMANTICS
OPERATION SEQUENCING / DOMAIN-MANDATED ORDER
DOMAIN GATES / BARRIERS / RE-ENTRY RULES
TIME / TIMER / RHYTHM SEMANTICS

EVIDENCE / SOURCE AUTHORITY
FRESHNESS / STALENESS
MATERIALITY
UNCERTAINTY
INVALIDATION

STORY READER AUTHORITY
STORY WRITER AUTHORITY / BRANCHING LIMITS
PREDICTION / CLAIM SEMANTICS
OUTCOME / CLOSURE SEMANTICS
FAILURE / LOSS SEMANTICS
CAPTURE / BENEFICIARY SEMANTICS
RECOGNITION / RESPONSE SEMANTICS

MEMORY / PERSISTENCE
POINTER / IDENTITY RULES
RESOURCE HORIZON
AUDIT SPECIALIZATIONS
LEARNING / MISS LOOP
CORRESPONDENCE IMPORT STATUS
LOCAL CALIBRATIONS
SOFTWARE / HARD-LIMIT SUPPORT

APPLICABLE CORE FLOWS
DOMAIN FLOWS
MAPPINGS
UNSUPPORTED / BLOCKED CAPABILITIES
~~~

A field may be NOT APPLICABLE with reason. It may not disappear silently when material.

## RELATIONAL STORY BINDING

When a domain uses ../core/relational-story.flow.md, the Domain Configurer must provide or bind a story configuration that includes:

~~~text
ROOT / CHARACTER TYPES
CHARACTER PROFILE / TRAIT BINDINGS
ARCHETYPE REGISTRY OR EXPLICIT NONE
STORY READER / WRITER AUTHORITY
DOMAIN SEQUENCING / GATE BINDINGS
RELATIONSHIP TYPES
EVENT / STATE-DELTA INTERPRETATION
SOURCE HIERARCHY
MATERIALITY TEST
PROPAGATION TARGET
RESOURCE HORIZON
STOP / CLOSURE RULES
MEMORY BACKEND / POINTER RULES
AUDIT SPECIALIZATIONS
FINAL STORY OUTPUT
~~~

These values come from the domain configuration, not from changes to the Relational Story core.

A domain may disable archetypes or restrict the Story Writer. For high-stakes/evidence-sensitive domains, Writer branches must remain evidence-bounded conditional hypotheses. A creative domain may explicitly authorize broader generative writing.

## ADAPTER RULE

Specific adapters may exist below the Domain Configurer for native calculations, APIs, formats, systems, or deterministic conversions.

~~~text
DOMAIN-NATIVE SYSTEM / DATA
→ SPECIALIZED ADAPTER(S)
→ DOMAIN-NATIVE NORMALIZED STATE
→ DOMAIN CONFIGURER
→ MAPPING META FLOW
→ FLOWARE CONTRACT BINDINGS
~~~

An adapter handles a specific interface/translation.

The Domain Configurer governs how the domain as a whole fits Floware.

Do not use "Domain Adapter" as a substitute for the entire configuration layer when that hides multiple mappings, contracts, or adapters.

## CAPABILITY SELECTION

The Domain Configurer should select only the Floware capabilities the domain actually needs.

When a domain has mandatory order-of-operations rules, bind them to:
`sequencing.flow.md`

Domain order is semantic authority within that scope. Sequencing may parallelize independent work around it, but may not weaken or bypass the domain gate.

~~~text
DOMAIN
→ requires relational story? YES/NO
→ requires persistent live state? YES/NO
→ requires prediction/outcome closure? YES/NO
→ requires correspondence? YES/NO
→ requires deterministic calculation? YES/NO
→ requires external action authority? define separately
~~~

Do not force every domain through every Flow.

## GAP HANDLING

If configuration discovers a missing native rule/function that should have been established upstream, return the affected scope to `../core/domain-establishment.flow.md` rather than inventing local semantics inside Meta.

If a required capability has no valid mapping or implementation:

~~~text
MISSING CAPABILITY
→ classify:
   MISSING DOMAIN RULE / FUNCTION → RETURN TO CORE DOMAIN ESTABLISHMENT
   MISSING MAPPING
   MISSING CORE PRIMITIVE
   MISSING ADAPTER
   MISSING EVIDENCE
   MISSING SOFTWARE HARD-LIMIT SUPPORT
→ mark configuration PARTIAL / BLOCKED
→ route to responsible development layer
~~~

Do not repair a gap by silently copying semantics from another domain.

## CONFIGURATION STATUS

Use:

~~~text
DRAFT
PARTIAL
EXPERIMENTAL
VALIDATED_FOR_SCOPE
ACTIVE
BLOCKED
SUPERSEDED
~~~

A domain's broader release status may use additional labels, but configuration status must not imply empirical validity beyond its scope.

## GATES

Before a domain can claim a valid Floware configuration:
- a `READY_FOR_CONFIGURATION` Domain Establishment record exists for the claimed scope;
- every configured function is covered by that establishment record;
- domain objective and authority are explicit;
- required mappings are present;
- core contracts are not modified with local nouns/calibrations;
- evidence and outcome semantics are defined;
- local calibrations are separated;
- unsupported capabilities are named;
- Meta Audit has no unresolved FAIL for the claimed scope.

## DOMAIN ESTABLISHMENT VS DOMAIN CONFIGURER

These are separate jobs:

~~~text
CORE DOMAIN ESTABLISHMENT
= what the domain is natively and what functions/rules actually exist for the claimed scope

META DOMAIN CONFIGURER
= how that established native scope binds to reusable Floware contracts
~~~

The Configurer may expose an establishment gap. It may not repair that gap by fabricating domain content.

## DOMAIN CONFIGURER VS MAPPING VS CORRESPONDENCE

~~~text
MAPPING
= how representations line up

DOMAIN CONFIGURER
= how one domain composes and binds Floware capabilities using mappings

CORRESPONDENCE
= whether a learned structural relationship validly transfers across domains
~~~

The Domain Configurer may consume correspondence results, but it must preserve their validation status.

## BOUNDARIES

The Domain Configurer does not:
- establish the domain's native rules/functions;
- decide that a domain theory is empirically true;
- transfer source-domain calibrations by default;
- grant financial/medical/legal/physical/external-action authority;
- rewrite core contracts to make a local domain fit;
- hide missing mappings;
- treat configuration compatibility as validation.

## FAIL-CLOSED CONDITIONS

Return BLOCKED/PARTIAL when:
- Domain Establishment record is missing, stale, or not `READY_FOR_CONFIGURATION` for the claimed scope;
- a configured function is absent from the establishment record;
- domain identity/objective is ambiguous;
- a material core binding lacks a mapping;
- local semantics would require contaminating a core contract;
- action authority is undefined for a material operation;
- evidence/outcome semantics are insufficient to audit the claimed use;
- required specialized adapters or deterministic support are unavailable.

## OUTPUT STATE

~~~text
DOMAIN CONFIG ID:
DOMAIN ESTABLISHMENT ID / STATUS:
DOMAIN / VERSION:
CLAIMED SCOPE:
CONFIGURATION STATUS:
OBJECTIVE:
AUTHORITY:
APPLICABLE CORE FLOWS:
DOMAIN FLOWS:
MAPPINGS:
SPECIALIZED ADAPTERS:
STATE / TIME / EVIDENCE BINDINGS:
MEMORY / OUTCOME / AUDIT / LEARNING BINDINGS:
LOCAL CALIBRATIONS:
UNSUPPORTED CAPABILITIES:
GAPS / BLOCKERS:
META AUDIT RESULT:
~~~

## LEARNING HOOK

Configuration misses route to ../core/learning.flow.md.

A recurring configuration miss can propose:
- a better mapping;
- a clearer domain contract;
- a new reusable core candidate;
- or a domain-local extension.

Promotion into core still requires evidence that the abstraction is genuinely cross-domain.

## SOFTWARE / HARD-LIMIT BOUNDARY

NONE — FLOWARE SUFFICIENT BY DEFAULT

Use software only for exact schema/config validation, deterministic adapters/calculations, persistence, identity, permissions, or other justified hard limits.


## DOMAIN UPDATE / RECONFIGURATION SCOPE

For an existing domain, consume the delta emitted by Core Domain Establishment.

~~~text
PRIOR VALID CONFIGURATION
+ READY_FOR_CONFIGURATION DOMAIN DELTA
→ preserve unaffected bindings
→ remap/rebind only affected functions
→ invalidate only bindings whose shared assumptions changed
→ patch affected Plumbing / domain Flow surfaces
→ audit the changed scope plus any shared dependency boundary
~~~

The Configurer must not:
- rebuild the entire domain by default;
- silently expand configuration beyond the established delta;
- preserve a binding whose native dependency was invalidated;
- mark an unaffected function PARTIAL merely because a different new function is incomplete.

Output should name:
- preserved bindings;
- changed bindings;
- invalidated bindings;
- new bindings;
- required Pipe/Flow patch scope.
