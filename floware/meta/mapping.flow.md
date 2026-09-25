# META FLOW — Mapping

FLOW ID: META-MAPPING
STATUS: **ACTIVE / CANONICAL**
DOMAIN: meta
JOB: construct explicit, auditable structural mappings between two representations without inventing equivalence, transferring unsupported authority, or hiding information loss
AUTHORITY: representational / structural mapping only; no empirical transfer or domain activation authority
PARENT GOALPOST: supplied by the calling Flow or Meta Flow
UPSTREAM FLOWS: Pipeline Integrity, Domain Configurer, Patching, Correspondence, Development, migration/conversion tasks, any Flow requiring representation alignment
DOWNSTREAM FLOWS: Domain Configurer, Sequencing, Relational Story, Correspondence, Audit, owning Flow
INBOUND PIPES: `PLUMBING.md#pipe-meta-integrity-mapping`
OUTBOUND PIPES: return through owning Pipeline/Pipe wrapper; material downstream Pipes remain context-specific
SOFTWARE DEPENDENCIES: none by default; deterministic schema/reference validators may support exact compatibility checks

## GOAL

Determine how a source representation and a target representation line up, including exact matches, partial matches, transformations, missing components, incompatibilities, one-to-many relationships, many-to-one relationships, and information loss.

Core law:

> **Mapping establishes how representations correspond structurally. It does not prove that a causal rule or conclusion transfers between domains.**

## GOALPOST

A mapping is complete when:
- source and target contracts/representations are identified;
- every material source component has a disposition;
- every required target component has a source, derivation, default rule, or explicit gap;
- preserved invariants are named;
- transformations and information loss are explicit;
- incompatible components are blocked rather than forced;
- authority and confidence do not silently increase through translation;
- the result is auditable.

## INPUT STATE

At minimum:
- source object/contract/version;
- target object/contract/version;
- purpose of the mapping;
- source semantics;
- target semantics;
- required invariants;
- applicable domain boundaries;
- known constraints or forbidden transfers.

## MAPPING TYPES

A mapping may be:

~~~text
EXACT
RENAMED
TRANSFORMED
ONE_TO_MANY
MANY_TO_ONE
PARTIAL
DERIVED
OPTIONAL
UNMAPPED
INCOMPATIBLE
LOSSY
BLOCKED
~~~

Do not collapse these states into a single "mapped" label.

## PROCESS

~~~text
IDENTIFY SOURCE
→ IDENTIFY TARGET
→ IDENTIFY PURPOSE
→ LOAD BOTH CONTRACTS / VERSIONS
→ DECOMPOSE SOURCE INTO MATERIAL COMPONENTS
→ DECOMPOSE TARGET INTO REQUIRED COMPONENTS
→ MATCH CANDIDATE COMPONENTS
→ CLASSIFY EACH MATCH TYPE
→ DEFINE REQUIRED TRANSFORMATIONS
→ NAME PRESERVED INVARIANTS
→ NAME INFORMATION LOSS / AMBIGUITY
→ IDENTIFY UNMAPPED / INCOMPATIBLE COMPONENTS
→ CHECK AUTHORITY / CONFIDENCE PRESERVATION
→ EMIT MAPPING OBJECT
→ ROUTE TO META AUDIT WHEN MATERIAL
~~~

## MAPPING OBJECT

Minimum auditable form:

~~~text
MAPPING ID:
PURPOSE:
SOURCE:
SOURCE VERSION:
TARGET:
TARGET VERSION:
AS-OF:

ENTRIES[]
  source_component
  target_component
  mapping_type
  transformation
  preserved_invariant
  information_loss
  ambiguity
  authority_change = NONE unless explicitly justified
  evidence / rationale
  status

UNMAPPED SOURCE COMPONENTS[]
UNSATISFIED TARGET REQUIREMENTS[]
INCOMPATIBILITIES[]
ASSUMPTIONS[]
BOUNDARIES[]
AUDIT STATUS:
~~~

## INVARIANT RULE

A mapping may change vocabulary or representation while preserving structure.

Example:

~~~text
domain-native object
→ Floware character

domain-native relation
→ relationship edge

domain-native transition
→ event/state delta
~~~

The mapping must state what is preserved and what is not.

## MAPPING VS CORRESPONDENCE

These are different jobs.

~~~text
MAPPING
= How does representation A line up with representation B?

CORRESPONDENCE
= Does a structural relationship, mechanism, or learned principle
  from domain A genuinely have a valid counterpart in domain B?
~~~

A representation such as "transit → event" can be a mapping. Whether a timing principle from another domain validly predicts anything in astrology is a correspondence question and requires target-domain evidence.

Mapping must not promote a representational match into causal or empirical support.

## MAPPING VS DOMAIN CONFIGURATION

Mapping produces explicit relationships between representations.

The Domain Configurer consumes those mappings to assemble a domain's valid Floware configuration.

~~~text
MAPPING
→ reusable structural map

DOMAIN CONFIGURER
→ composed domain configuration using one or more mappings
~~~

## GATES

Before a mapping may be treated as VALID:
- both sides have known identities/versions;
- semantic meaning is understood enough to avoid name-only matching;
- required target fields are accounted for;
- information loss is disclosed;
- incompatible fields are not silently coerced;
- local calibration/authority is not elevated.

## ADAPTATION

The Mapping Flow may recurse when a component itself contains a nested representation. Recursive mapping remains bounded by the calling goal and resource policy.

## BOUNDARIES

The Mapping Meta Flow does not:
- validate an empirical theory;
- establish causal equivalence;
- transfer probabilities, thresholds, timing bands, weights, or actions unless the target contract explicitly defines that transformation;
- activate a domain;
- change source or target contracts;
- silently discard unmapped material information.

## FAIL-CLOSED CONDITIONS

Return BLOCKED when:
- source or target semantics are materially ambiguous;
- required target structure cannot be satisfied;
- information loss would destroy a required invariant;
- a proposed mapping depends on an unverified domain-specific assumption;
- an incompatible component is being forced into a target field.

## OUTPUT STATE

~~~text
MAPPING STATUS:
MAPPING ID:
SOURCE / VERSION:
TARGET / VERSION:
PRESERVED INVARIANTS:
MAPPED COMPONENTS:
TRANSFORMATIONS:
INFORMATION LOSS:
UNMAPPED COMPONENTS:
INCOMPATIBILITIES:
UNSATISFIED TARGET REQUIREMENTS:
BOUNDARIES:
AUDIT REQUIRED?:
~~~

## LEARNING HOOK

Mapping misses route to ../core/learning.flow.md.

Repeated mapping failures may indicate:
- a weak target contract;
- a hidden domain assumption in core;
- a missing representation primitive;
- or a domain structure that should remain local.

Do not fix repeated mapping failures by broadening core until evidence shows the abstraction is genuinely reusable.

## SOFTWARE / HARD-LIMIT BOUNDARY

NONE — FLOWARE SUFFICIENT BY DEFAULT

Use deterministic software for exact schema transforms, reference resolution, serialization, or high-volume conversion only when justified.
