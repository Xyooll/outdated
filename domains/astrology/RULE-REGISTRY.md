# Xyool Astrology — Rule Registry

Status: **EXPERIMENTAL DOMAIN CANONICAL / RULE VERSIONING AUTHORITY**

Purpose: give every interpretive, timing, translation, and synthesis rule an identity so Xyool can test it without hindsight modification.

---

## 1. Rule classes

```text
NATIVE_CALCULATION_RULE
NATIVE_INTERPRETIVE_RULE
TIMING_RULE
CAPTURE_RULE
CAPABILITY_TRANSLATION_RULE
CONVERGENCE_RULE
TUNER_COMPRESSION_RULE
ACTION_MAPPING_RULE
CORRESPONDENCE_RULE
```

Rules from different classes must not be treated as if they have the same evidentiary status.

---

## 2. Canonical rule object

```text
rule_id
rule_class
system_id
subsystem / technique
name
version
status
source_provenance
source_reference
source_quote_or_summary if legally/appropriately stored
required_inputs
calculation_prerequisites
trigger_configuration
native_interpretation
capture_mapping
capability_translation
polarity / direction if used
strength_rule if used
timing_start_rule
timing_peak_rule
timing_end_rule
orb / threshold / correlation settings
conflict_rules
known_dependencies
known_exceptions
falsification_condition
positive_controls
negative_controls
discovery_cases
validation_cases
prospective_cases
false_positive_notes
miss_notes
created_at
supersedes
```

Blank fields are acceptable when genuinely not applicable; hidden assumptions are not.

---

## 3. Rule statuses

```text
SOURCE-DOCUMENTED — NOT TESTED BY XYOOL
USER-DERIVED FRAMEWORK
DOMAIN HYPOTHESIS
IN TESTING
PROVISIONALLY SUPPORTED
SUPPORTED WITH BOUNDARIES
REJECTED
SUPERSEDED
```

`SOURCE-DOCUMENTED` means Xyool has evidence that a tradition/system teaches the rule. It does **not** mean Xyool has validated the rule's predictive efficacy.

---

## 4. Rule identity lock

A rule change creates a new version when any material element changes, including:

```text
orb
window
signification
capture area
strength weighting
planet/point inclusion
ayanamsha
house logic
dasha interpretation
Maya correlation
Dreamspell mapping
fixed-star orb / paran condition
capability translation
conflict-resolution logic
confidence threshold
```

The prior version remains in history.

---

## 5. Discovery versus validation

If a rule is invented or modified after observing a case:

```text
that case = DISCOVERY CASE
```

It cannot also serve as clean validation evidence for the modified rule.

The new version must be tested on untouched or prospective cases.

---

## 6. Native meaning versus Xyool translation

For cross-system synthesis, store separately:

```text
native_interpretation
XYOOL capability translation
Tuner compression effect
```

Example:

```text
source rule: a declared Maya day meaning
native interpretation: source-preserved wording/summary
capability translation: Investigation + / Action neutral
Tuner effect: Clarity +
```

The latter two are Xyool-created rules unless the source tradition explicitly makes those same mappings.

---

## 7. Convergence rule object

A convergence rule must identify which underlying signals are truly distinct.

Additional fields:

```text
participating_systems
participating_rule_ids
shared_data_dependencies
shared_astronomical_dependencies
shared_interpretive_lineage
independence_assessment
combination_method
conflict_method
ablation_results
combined_performance
best_single_system_performance
```

A convergence rule is not promoted merely because several systems can be made to tell a similar story.

---

## 8. Capability translation rules

Use the shared capability vocabulary:

```text
Mental Capacity
Focus
Action
Opportunity
Communication
Creation
Investigation
Connection
Recovery
Friction / Impulsiveness
```

A translation should specify:

```text
capability
expected direction
conditions
strength logic
timing logic
what would count as a translation miss
```

Do not translate every symbol into every capability. Sparsity improves testability.

---

## 9. Tuner compression rules

Tuner dimensions:

```text
Energy
Direction
Stability
Intensity
Clarity
```

A compression rule must identify which capability variables feed it and must preserve contradictory inputs rather than averaging them away invisibly.

---

## 10. System-specific fields

### Western / Jyotish

May require:

```text
zodiac
ayanamsha
house system
sect
nakshatra
aspect doctrine
orb
dasha / time-lord system
Panchang element
```

### Star Astrology / degree field

May require:

```text
exact ecliptic longitude
coordinate frame
epoch/date
degree-bin policy
intrinsic degree rule ID if used
stellar-neighborhood rule ID
star catalogue
star longitude / latitude
star magnitude
proper motion / epoch if material
projected-longitude distance
true angular distance if used
house/sign/decan wrappers
occupant/activator object IDs
asteroid/object inclusion set
anti-double-counting dependencies
```

Keep intrinsic degree meaning separate from fixed-star meaning.

### Fixed stars / parans

May require:

```text
star catalogue / coordinates
proper motion / epoch if material
contact type
orb
angle
paran event / angularity condition
birth-time precision requirement
```

### MAYA.TRAD

May require:

```text
calendar object
day number
day sign
community / language / source tradition
correlation_id
calendar converter
```

### DREAMSPELL.ARGUELLES

May require:

```text
Kin
Tone
Solar Seal
Wavespell
mapping algorithm
leap-day rule
implementation version
```

---

## 11. Rule registry operational files

When the registry begins accumulating real rules, prefer machine-readable storage alongside this schema, for example:

```text
domains/astrology/rules/*.yaml
```

or another structured format that preserves version history and can be tested automatically.

Do not start with hundreds of copied interpretations. Begin with high-value rules that Xyool is actually prepared to test.

---

## 12. Promotion question

Before promoting a rule, ask:

```text
Is the calculation reproducible?
Is the rule identity stable?
Is the claim specific enough to fail?
Does it beat relevant controls?
Does it survive untouched/prospective cases?
Does it add information beyond correlated rules?
Are failure boundaries documented?
```

Final rule:

> **A rule is not improved by becoming harder to falsify.**

## 10. Registered bounded rule cohorts

### ASTRO.WT.XYOOL_STORY_V1.RULESET

Path:
`rules/western_tropical_xyool_story_v1.yaml`

System:
`ASTRO.WT.XYOOL_STORY_V1`

Purpose:
bounded Western Tropical grammar for Story Reader/Writer experimentation.

Current readiness:
- deterministic calculation grammar: READY_FOR_CONFIGURATION;
- historical Story Reader grammar: READY_FOR_CONFIGURATION for discovery/current-state reconstruction;
- future Story Writer grammar: PARTIAL;
- prospective prediction: PARTIAL.

The cohort intentionally mixes source-documented conventions with separately labeled Xyool domain hypotheses. It is not a universal Western astrology ruleset.


## 11. Star Astrology seed rule cohort

### ASTRO.STAR.DEGREE.SEED_V1

Path:
`rules/star_degree_seed_v1.yaml`

System:
`ASTRO.STAR.DEGREE.XYOOL_V1`

Contains:
- exact-degree state preservation;
- epoch-aware stellar field;
- longitude and spherical-distance star-contact hypotheses;
- Sabian degree-cell lineage mapping;
- initial Ptolemaic fixed-star semantic primitives for Aldebaran, Regulus, Spica, Antares, Fomalhaut, Sirius, Procyon, and Arcturus.

Authority boundary:
- astronomical method rules may be source-grounded;
- contact thresholds remain Xyool hypotheses until validated;
- Ptolemaic meanings are SOURCE-DOCUMENTED / EMPIRICALLY UNVALIDATED;
- no event prediction follows automatically from a historical planetary analogy.

Catalog manifests:
- `catalogs/fixed-stars/manifest.yaml`
- `catalogs/minor-bodies/manifest.yaml`


## 12. Intrinsic degree research cohorts

### ASTRO.DEGREE.LOCAL30.MODERN_SEED_V1

Path:
`rules/local_degree_30_modern_seed_v1.yaml`

Purpose:
candidate local 0–29 degree meanings from the modern Nikola Stojanovic Degree Theory lineage.

Status:
**SECONDARY-SOURCE RECONSTRUCTION / UNVALIDATED**

Important:
secondary sources conflict on indexing, especially 0°. The current seed preserves one documented variant and must not be treated as canonical Xyool truth.

### ASTRO.DEGREE.ABS360.MONOMOIRIA_V1

Path:
`rules/absolute_degree_360_monomoiria_v1.yaml`

Purpose:
assign one historical planetary degree lord to every absolute zodiac degree cell.

Status:
**SOURCE-DOCUMENTED HISTORICAL / EMPIRICALLY UNVALIDATED**

Variant:
sign-based monomoiria only. Trigonal/sect alternatives remain separate.

### ASTRO.DEGREE.INTRINSIC.SYNTHESIS_CONTRACT_V1

Path:
`rules/degree_intrinsic_synthesis_contract_v1.yaml`

Flow:
`flows/intrinsic-degree-foundation.flow.md`

Purpose:
create Xyool-native local30 and absolute360 intrinsic meaning candidates from multiple source corpora while preserving lineage dependence and validation boundaries.
