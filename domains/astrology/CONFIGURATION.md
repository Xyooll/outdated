# Astrology — Floware Domain Configuration

CONFIG ID: ASTROLOGY-FLOWARE-CONFIG-V1
STATUS: **PARTIAL / VERIFICATION_PENDING**
DOMAIN MATURITY: **EXPERIMENTAL**
ESTABLISHMENT: `ESTABLISHMENT.md` — **FUNCTIONS_PARTIAL**
DOMAIN: astrology
VERSION: 1
GOALPOST: ../../research/system-tests/domain-foundations-v1-2026-09-24/GOALPOST.md

## Objective

Bind only the currently established Astrology functions/scopes to Floware without treating configuration compatibility as evidence that all registered Astrology systems/functions are established or empirically true.

## Authority

- deterministic astronomical/calendrical calculations may be treated as reproducible computational outputs when inputs/system settings are known;
- astrological interpretation remains interpretive/research authority;
- predictive claims require the domain validation protocol;
- no medical, legal, financial, safety, or external-action authority is created.

## Applicable Floware capabilities

Primary:
- `../../floware/core/domain-establishment.flow.md`
- `../../floware/core/xyool-execution.flow.md`
- `flows/astrology-analysis.flow.md`
- `../../floware/core/learning.flow.md`
- `../../floware/core/meaning-attribution.flow.md` for meaning-dependent Astrology functions
- `../../floware/meta/sequencing.flow.md`
- `../../floware/meta/mapping.flow.md`
- `../../floware/meta/domain-configurer.flow.md`
- `../../floware/meta/pipeline-integrity.flow.md`

Conditional:
- `../../floware/core/relational-story.flow.md` + `story-reader.flow.md` + `story-writer.flow.md` through `STORY-BINDING.md` for history-aware/predictive story work;
- `flows/rule-foundation.flow.md` when Core Domain Establishment identifies a local Astrology rule gap;
- `flows/intrinsic-degree-foundation.flow.md` when the missing work is LOCAL30 / ABS360 intrinsic degree meaning research;
- `flows/predictive-astrology.flow.md` only after `ASTRO-FN-PREDICTIVE` becomes READY_FOR_CONFIGURATION;
- Research when source/rule questions are unresolved;
- Evaluation for frozen capability comparisons when explicitly selected;
- Observation/Trigger only when future autonomous timing/outcome monitoring is eventually activated;
- Correspondence only for explicit cross-domain hypothesis transfer.

Not required by default:
- Character System;
- stock Quality/TTC/capital Flows.

## Native → Floware mappings

| Astrology-native object | Floware role | Mapping | Boundary |
|---|---|---|---|
| subject / event / chart | domain analysis object | EXACT / DOMAIN-LOCAL | not forced into stock/security semantics |
| system identity + settings | configuration identity | EXACT | silent system mixing is blocked |
| calculated positions / cycles | evidence/state input | EXACT when computationally verified | calculation does not prove interpretation |
| interpretive rule | domain method/rule | DOMAIN-LOCAL | provenance/tradition required |
| interpretive proposition | claim | TRANSFORMED | uncertainty/claim type preserved |
| timing window / forecast | prediction claim | TRANSFORMED | hit/miss/window frozen before outcome |
| observed outcome | learning/evaluation evidence | TRANSFORMED | subjective vs objective response preserved |
| cross-system synthesis | mapped synthesis | LOSSY / CONDITIONAL | native outputs must remain recoverable |
| confidence label | qualitative uncertainty | PARTIAL | no automatic numeric probability mapping |

## Domain-native constraints

- every material analysis names its astrology system/tradition;
- incompatible systems remain separate until an explicit synthesis step;
- birth/event input precision constrains allowed techniques;
- historical timezone/calendar assumptions are material state;
- predictive work freezes claim, window, hit, miss, and allowed techniques before outcome;
- cross-system agreement is not independent evidence when systems share dependencies.

## Specialized deterministic support

Existing calculation utilities may support:
- ephemeris/position calculations;
- calendrical conversion;
- timezone conversion;
- aspect/window exactness;
- independent calculation cross-checks.

They do not own interpretation.

## Local calibrations

Remain domain-local:
- orb policy;
- house system;
- ayanamsha;
- node mode;
- dignity/condition rules;
- source-tradition interpretation;
- timing-technique calibration;
- convergence weighting;
- confidence language.

## Unsupported / blocked capabilities

- empirical predictive authority beyond validated scope;
- universal convergence weighting;
- silent hybrid rule sets;
- medical/legal/financial decision substitution;
- external action authority.

## Validation boundary

Configuration status may become VALIDATED_FOR_SCOPE only after the architecture/Pipes pass independent audit. That status still does not imply astrological efficacy. Efficacy remains governed by `VALIDATION.md`.


## Establishment scope

This configuration consumes `ESTABLISHMENT.md`.

Currently READY_FOR_CONFIGURATION:
- system identity / configuration locking;
- sourced Maya interpretation under the existing rule file;
- sourced Dreamspell interpretation under the existing rule file;
- validation / preregistration / scoring methodology.

Currently PARTIAL and therefore not globally configured as rule-complete:
- Western interpretation;
- Jyotish interpretation;
- stellar interpretation;
- predictive astrology;
- broad capability-translation cohorts.

When a PARTIAL function is requested, return to Core Domain Establishment before extending configuration.


## Predictive mode

Predictive Astrology is a candidate domain function and is currently **PARTIAL** in `ESTABLISHMENT.md`.

Correct path:

~~~text
PREDICTIVE FUNCTION REQUEST
→ CORE DOMAIN ESTABLISHMENT
→ if rule gap: ASTROLOGY RULE FOUNDATION
→ return rules to CORE DOMAIN ESTABLISHMENT
→ update function readiness
→ only when ASTRO-FN-PREDICTIVE = READY_FOR_CONFIGURATION:
     META DOMAIN CONFIGURATION / INTEGRATION
     → ASTROLOGY ANALYSIS
     → PREDICTIVE ASTROLOGY
     → VALIDATION
~~~

The Rule Foundation helper cannot bypass Core establishment or independently activate predictive mode.


## Astrology story binding

For story-shaped work, consume `STORY-BINDING.md`.

Structural reuse:

~~~text
ASTROLOGY HISTORY / STATE
→ CORE RELATIONAL STORY
   → STORY READER: past → present
   → STORY WRITER: present → conditional future
→ ASTROLOGY PREDICTIVE WRAPPER
→ prospective validation
~~~

Core supplies story structure.

Astrology supplies:
- valid system/rules;
- timing transitions;
- capture/life-area semantics;
- evidence authority;
- proof/invalidation;
- predictive boundaries.

Relational Story is only activated for a scope that Core Domain Establishment has marked ready enough for the requested Reader/Writer job.


## Domain library

Reusable Astrology knowledge begins at:
`library/INDEX.md`

Research/establishment behavior:

~~~text
ASTROLOGY LIBRARY
→ reuse sufficient current knowledge
→ identify real gaps
→ external research only where justified
→ update canonical rule/source/validation artifacts
→ distill reusable knowledge back into library
~~~

The library is a knowledge-memory/index layer, not a substitute for canonical rules, sources, validation, or current subject state.


## Star Astrology / degree-field mode

Candidate framework:
`STAR-DEGREE.md`

Current establishment:
`ASTRO-FN-STAR-DEGREE-V1 = PARTIAL`

Therefore:
- preserve exact degree state whenever available;
- do not yet treat intrinsic degree meanings as established;
- do not yet activate unrestricted star-field interpretation;
- route missing degree/star rules to Core Domain Establishment → Astrology Rule Foundation;
- preserve sign/house/decan as contextual wrappers rather than replacements for degree state.

When established, Star Astrology may feed full-chart aggregation and Story Reader/Writer as a specialized domain layer.


## Intrinsic degree configuration boundary

Representation may preserve both:
- LOCAL30 coordinate identity;
- ABS360 coordinate identity.

Interpretation may use only explicitly versioned source/candidate rule IDs.

Current local/absolute source seeds are research inputs, not validated prediction authority.

If a requested degree meaning is missing or unresolved:
→ Core Domain Establishment
→ Intrinsic Degree Foundation
→ return candidate
→ re-evaluate readiness.


## Meaning attribution binding

Meaning-rich Astrology scopes use Core Meaning Attribution rather than defining a parallel semantic authority.

For Star Astrology:
- intrinsic degree meanings = INTRINSIC meaning objects;
- house/sign/decan/star/aspect/rulership context = EXTRINSIC meaning objects unless a specific source defines a different ontology;
- combined reading = COMPOSITE meaning object when explicit synthesis is requested.

Meaning provenance/claim mode must remain recoverable.

Symbolic/creative interpretive readiness does not imply causal or predictive validity.
