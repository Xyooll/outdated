# Astrology — Domain Establishment Record

DOMAIN ESTABLISHMENT ID: ASTROLOGY-ESTABLISHMENT-V1
DOMAIN: astrology
VERSION: 1
CLAIMED SCOPE: current registered experimental astrology capabilities
STATUS: **FUNCTIONS_PARTIAL**
OBJECTIVE: support system-identified astrological calculation/interpretation and bounded validation without overstating empirical authority
ANALYSIS / DECISION UNIT: chart/date/system-specific interpretive proposition, timing hypothesis, or validation record
AUTHORITY: experimental interpretive/research only

## Native foundation

Present:
- domain identity/objective;
- system registry;
- source hierarchy;
- time standards;
- outcome taxonomy;
- preregistration;
- scoring/null models;
- validation architecture;
- rule schema/versioning contract;
- Maya traditional sourced rule corpus;
- Dreamspell sourced rule corpus;
- calculation/interpretation separation.

Partial:
- broad/general Western rule corpus beyond the bounded `ASTRO.WT.XYOOL_STORY_V1` cohort;
- concrete Jyotish rule corpus;
- concrete stellar predictive rule corpus;
- system-specific predictive timing cohorts;
- validated capability-translation rule cohorts.

## Function inventory

### ASTRO-FN-SYSTEM-IDENTITY

JOB: identify and lock astrology system/tradition/settings.

RULE / METHOD SET:
SYSTEM-REGISTRY.md + DOMAIN.md identity requirements.

EVIDENCE:
declared system/settings + input provenance.

OUTCOME:
stable system identity before interpretation.

FLOW OWNER:
flows/astrology-analysis.flow.md

ESTABLISHMENT STATUS: **READY_FOR_CONFIGURATION**

### ASTRO-FN-MAYA-INTERPRETATION

JOB: preserve and interpret the currently sourced Maya traditional day-meaning rules.

RULE / METHOD SET:
rules/maya_trad_komon_tohil.yaml

EVIDENCE:
named living-tradition/Smithsonian source provenance.

OUTCOME:
source-preserved native interpretation with no predictive efficacy implied.

FLOW OWNER:
flows/astrology-analysis.flow.md

ESTABLISHMENT STATUS: **READY_FOR_CONFIGURATION**

### ASTRO-FN-DREAMSPELL-INTERPRETATION

JOB: preserve and interpret the registered Dreamspell tone/seal rules.

RULE / METHOD SET:
rules/dreamspell_arguelles_core.yaml

EVIDENCE:
named modern-system primary source.

OUTCOME:
source-preserved Dreamspell interpretation kept separate from traditional Maya meanings.

FLOW OWNER:
flows/astrology-analysis.flow.md

ESTABLISHMENT STATUS: **READY_FOR_CONFIGURATION**


### ASTRO-FN-WT-STORY-READER-V1

JOB: reconstruct bounded Western Tropical historical/current story state using the explicit Xyool Story v1 grammar.

SYSTEM:
ASTRO.WT.XYOOL_STORY_V1

RULE / METHOD SET:
rules/western_tropical_xyool_story_v1.yaml

EVIDENCE:
dated subject/event history through an as-of cutoff + reproducible chart/timing calculations + frozen rule versions.

CORE DEPENDENCIES:
CORE-RELATIONAL-STORY, CORE-STORY-READER.

OUTCOME:
a current-state story that preserves historical matches, misses, contradictions, unknowns, and discovery-vs-confirmation boundaries.

FLOW OWNER:
flows/astrology-analysis.flow.md + STORY-BINDING.md

ESTABLISHMENT STATUS: **READY_FOR_CONFIGURATION**

BOUNDARY:
ready for historical/current-state reconstruction and rule discovery only; this does not establish predictive efficacy.

### ASTRO-FN-WT-STORY-WRITER-V1

JOB: write conditional future branches from the current Western Tropical story under the v1 timing/transition grammar.

SYSTEM:
ASTRO.WT.XYOOL_STORY_V1

RULE / METHOD SET:
rules/western_tropical_xyool_story_v1.yaml

CORE DEPENDENCIES:
CORE-RELATIONAL-STORY, CORE-STORY-WRITER.

ESTABLISHMENT STATUS: **PARTIAL**

BLOCKERS:
- capture/outcome translations remain broad;
- subject-specific Ascendant-dependent methods require input-precision clearance;
- prospective branch specificity/false-positive behavior is unvalidated.

### ASTRO-FN-WESTERN-INTERPRETATION

JOB: execute Western Tropical/Traditional interpretation from concrete versioned rules.

RULE / METHOD SET:
missing concrete ASTRO.WT.* rule objects.

EVIDENCE:
source requirements exist; actual imported/versioned rule corpus does not.

FLOW OWNER:
flows/astrology-analysis.flow.md

ESTABLISHMENT STATUS: **PARTIAL**

BLOCKER:
source-grounded Western rules must be established before broad Western interpretation is claimed as rule-complete.

### ASTRO-FN-JYOTISH-INTERPRETATION

JOB: execute Jyotish interpretation from concrete versioned rules.

RULE / METHOD SET:
missing concrete ASTRO.JYO.* rule objects.

EVIDENCE:
source requirements/system definition exist; concrete rule corpus does not.

FLOW OWNER:
flows/astrology-analysis.flow.md

ESTABLISHMENT STATUS: **PARTIAL**

### ASTRO-FN-STELLAR-INTERPRETATION

JOB: execute fixed-star/stellar interpretation using declared astronomical and interpretive rules.

RULE / METHOD SET:
conceptual/system framework exists; concrete rule cohort incomplete.

ESTABLISHMENT STATUS: **PARTIAL**


### ASTRO-FN-STAR-DEGREE-V1

JOB: interpret and test exact-degree chart state using the user-derived Star Astrology framework, including explicit stellar-neighborhood context.

SYSTEM:
ASTRO.STAR.DEGREE.XYOOL_V1

RULE / METHOD SET:
STAR-DEGREE.md + future versioned degree/star rule cohort.

EVIDENCE:
exact calculated longitude, declared coordinate frame/epoch, star catalogue/positions, explicit intrinsic-degree rule provenance, chart wrappers/relationships.

CORE DEPENDENCIES:
CORE-DOMAIN-LIBRARY, CORE-MEANING-ATTRIBUTION, CORE-RELATIONAL-STORY when story work is requested.

ESTABLISHMENT STATUS: **PARTIAL**

READY COMPONENT:
- exact degree can be preserved as a first-class calculated chart-state object.

BLOCKERS:
- intrinsic degree meanings now have versioned source seeds and a synthesis Flow, but Xyool-native meanings remain PARTIAL/unvalidated;
- stellar-neighborhood inclusion/orb/latitude/magnitude policy is not frozen;
- actual star-interpretation cohort is incomplete;
- degree/star/sign/house/aspect combination rules are incomplete;
- predictive/discriminative value is unvalidated.


### ASTRO-FN-INTRINSIC-DEGREE-MEANING-V1

JOB: research, version, and test intrinsic meanings for local 30-degree identity and absolute 360-degree identity.

SYSTEM:
ASTRO.STAR.DEGREE.XYOOL_V1

RULE / METHOD SET:
- rules/local_degree_30_modern_seed_v1.yaml;
- rules/absolute_degree_360_monomoiria_v1.yaml;
- rules/degree_intrinsic_synthesis_contract_v1.yaml;
- flows/intrinsic-degree-foundation.flow.md.

CORE DEPENDENCY:
CORE-MEANING-ATTRIBUTION — canonical intrinsic/extrinsic/composite meaning representation.

READY COMPONENTS:
- dual LOCAL30 / ABS360 coordinate ontology;
- local 30-degree modern source seed captured with indexing-conflict warning;
- all 360 sign-based monomoiria planetary degree rulers generated and versioned;
- source-corpus lineage/dependency map;
- synthesis and null-control contract.

ESTABLISHMENT STATUS: **PARTIAL**

BLOCKERS:
- Xyool-native 30 local meanings have not yet earned validation;
- Xyool-native 360 absolute meanings are not yet synthesized across multiple independent corpora;
- primary Stojanovic source has not yet been recovered;
- 360 symbolic corpora are not yet normalized into copyright-safe structured semantic primitives;
- no prospective intrinsic-degree efficacy validation yet.

### ASTRO-FN-PREDICTIVE

JOB: produce prospective falsifiable forecasts by reusing Core Relational Story / Story Reader / Story Writer under an Astrology-specific story binding and frozen system/rule cohort.

RULE / METHOD SET:
validation/preregistration/scoring framework exists; STORY-BINDING.md defines the candidate story mapping; system-specific experiment-ready predictive transition/timing rule cohorts are not generally established.

ESTABLISHMENT STATUS: **PARTIAL**

BLOCKER:
selected system must have actual rule objects with timing/falsification/search-space boundaries before predictive configuration.

CORE DEPENDENCIES:
CORE-RELATIONAL-STORY, CORE-STORY-READER, CORE-STORY-WRITER.

DOMAIN BINDING:
STORY-BINDING.md — candidate/partial until the selected predictive function scope is established.

### ASTRO-FN-VALIDATION

JOB: preregister, close, score, and compare astrology claims against controls/nulls.

RULE / METHOD SET:
VALIDATION.md, PREREGISTRATION.md, EXPERIMENT-DESIGN.md, NULL-MODELS.md, SCORING.md, OUTCOME-TAXONOMY.md.

ESTABLISHMENT STATUS: **READY_FOR_CONFIGURATION**

## Core capability needs

Applicable:
- Research;
- Evidence-to-State;
- Learning;
- Question Frontier;
- Evaluation;
- Mapping/Domain Configurer after function establishment;
- Correspondence only for explicit transfer hypotheses.

## Missing domain knowledge / rules

- broader Western rule corpus beyond `ASTRO.WT.XYOOL_STORY_V1`;
- Jyotish rule corpus;
- stellar interpretive/predictive rule corpus;
- validated capability translations;
- experiment-ready predictive rule cohorts.

## Establishment readiness

~~~text
DOMAIN OVERALL: FUNCTIONS_PARTIAL

READY SCOPES:
- system identity
- current sourced Maya interpretation
- current sourced Dreamspell interpretation
- validation/preregistration/scoring methodology
- bounded Western Tropical Story Reader v1 for historical/current-state discovery

PARTIAL SCOPES:
- Star Astrology / exact-degree + stellar-field interpretation
- broad Western interpretation beyond the bounded Story v1 cohort
- Western Tropical Story Writer v1 / prospective branch generation
- Jyotish interpretation
- stellar interpretation
- predictive astrology
- broad capability translation
~~~

Core Domain Establishment must be re-entered when a PARTIAL scope is requested.

A Floware configuration may bind READY scopes without implying that all Astrology functions are established.


## Domain update — predictive story capability

Update record:
`../../research/system-tests/astrology-predictive-v1-2026-09-24/DOMAIN-UPDATE.md`

This is an **existing-domain delta**, not a new Astrology domain.

Unaffected READY scopes remain preserved:
- system identity;
- current sourced Maya interpretation;
- current sourced Dreamspell interpretation;
- validation/preregistration/scoring methodology.

Affected scope:
- ASTRO-FN-PREDICTIVE;
- story binding needed to reuse Core Relational Story / Reader / Writer;
- selected system's timing/transition/capture rule set.

Current result:
**FUNCTIONS_PARTIAL**

The new function does not inherit readiness from unrelated Astrology functions.


## Domain library status

Library:
`library/INDEX.md`

Current reusable knowledge includes:
- system-separation boundary;
- established Maya/Dreamspell rule pointers;
- bounded Western Story v1 knowledge;
- Story Reader/Writer binding;
- input-precision failure boundary;
- validation methodology;
- full-chart/asteroid v2 as an explicit partial/open update.

Domain Establishment must query this library before classifying a missing Astrology knowledge/rule/source gap.


## Deep Research establishment delta — 2026-09-25

Durable research record:
`../../research/system-tests/astrology-predictive-v1-2026-09-24/DEEP-RESEARCH-STAR-ASTROLOGY-2026-09-25.md`

New source-grounded / established-for-method components:
- astronomical state/provenance policy;
- epoch-aware stellar-neighborhood model;
- bounded fixed-star catalogue policy;
- bounded minor-body object policy;
- degree-node dependency model;
- source/provenance authority separation;
- A→E ablation and null-model design;
- preregistration/search-space freeze requirements.

New canonical artifacts:
- `systems/ASTRO.STAR.DEGREE.XYOOL_V1.yaml`;
- `systems/ASTRO.WT.XYOOL_STORY_V2_DEGREE_NODE.yaml`;
- `rules/star_degree_seed_v1.yaml`;
- `catalogs/fixed-stars/manifest.yaml`;
- `catalogs/minor-bodies/manifest.yaml`;
- `schemas/degree-node.schema.yaml`;
- `schemas/provenance.schema.yaml`;
- `schemas/star-contact.schema.yaml`.

### Star Astrology readiness after research

~~~text
exact-degree state representation
→ READY FOR MODELING / METHOD ESTABLISHED

source/provenance architecture
→ READY FOR CONFIGURATION

fixed-star astronomical neighborhood method
→ SOURCE-GROUNDED / CONTACT CALIBRATION PARTIAL

Ptolemaic fixed-star semantic seed
→ SOURCE-DOCUMENTED / EMPIRICALLY UNVALIDATED

Sabian degree lineage
→ SOURCE-DOCUMENTED LINEAGE / EMPIRICALLY UNVALIDATED

minor-body bounded object manifest
→ READY FOR CONTROLLED RESEARCH

intrinsic degree efficacy
→ PARTIAL

full degree-node Story v2
→ PARTIAL

predictive Star Astrology
→ BLOCKED UNTIL RULE/OUTCOME COHORT FREEZE + PROSPECTIVE VALIDATION
~~~

No source-grounded interpretive rule is promoted to empirical support merely because Deep Research found a historical or practitioner source.


## Meaning architecture

Astrology does not own a second general meaning ontology.

Canonical semantic authority:
- `../../floware/MEANING-CONTRACT.md`;
- `../../floware/core/meaning-attribution.flow.md`.

Astrology supplies domain-local objects, rules, source traditions, and contextual relationships.

Core Meaning Attribution supplies:
- INTRINSIC / EXTRINSIC / COMPOSITE distinction;
- authorship/provenance representation;
- claim-mode boundaries;
- semantic primitive representation;
- creative-use versus empirical-validity separation.

This allows future occult/metaphysical domains to reuse the same semantic architecture without inheriting Astrology rules.
