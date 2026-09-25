# Xyool Astrology — Data Contracts

Status: **EXPERIMENTAL DOMAIN CANONICAL / DATA INTEGRITY AUTHORITY**

Purpose: define the minimum machine-readable records needed for reproducible calculations, rule evaluation, forecasts, outcomes, atomic windows, and validation.

Core rule:

> **If Xyool cannot reconstruct what was known, calculated, interpreted, and frozen at a given time, the record is not validation-grade.**

---

## 1. Identity conventions

Use stable IDs rather than names as join keys.

Recommended patterns:

```text
subject_id: sub_<opaque-id>
input_id: inp_<opaque-id>
calculation_id: calc_<opaque-id>
rule_id: system.namespace.rule
forecast_id: fc_<opaque-id>
outcome_id: out_<opaque-id>
window_id: win_<opaque-id>
source_id: src_<opaque-id>
run_id: run_<opaque-id>
```

Personally identifying information should be stored separately from analytical records when practical.

---

## 2. Input record

```yaml
input_id:
subject_id:
created_at:
source_type: primary_record | direct_report | secondary_report | approximate | unknown
civil_date:
local_time:
time_precision_seconds:
time_uncertainty_seconds:
location_name:
latitude:
longitude:
timezone_name:
utc_offset:
calendar_convention:
notes:
version:
supersedes:
```

Rules:

- Preserve original reported data.
- Corrections create a new version.
- Rectified birth times never overwrite the original input.
- Unknown values remain null/unknown rather than being guessed silently.

---

## 3. System configuration record

```yaml
system_config_id:
system_id:
version:
settings:
  zodiac:
  ayanamsha:
  house_system:
  node_mode:
  planet_point_set:
  aspect_set:
  orb_policy:
  ephemeris_engine:
  fixed_star_catalogue:
  maya_correlation:
  dreamspell_implementation:
  leap_day_rule:
source_ids: []
created_at:
```

Only applicable fields need values. The record must still preserve which choices were intentionally not applicable.

---

## 4. Calculation record

```yaml
calculation_id:
input_id:
system_config_id:
calculated_at:
engine:
engine_version:
raw_state:
derived_state:
uncertainty_flags: []
independent_crosscheck_id:
crosscheck_status: not_run | agree | minor_difference | material_difference | blocked
content_hash:
```

The calculation record is factual/computational. Interpretive text does not belong here.

---

## 5. Rule evaluation record

```yaml
evaluation_id:
calculation_id:
rule_id:
rule_version:
trigger_state:
native_interpretation:
capture_mapping: []
capability_effects: []
timing_boundaries: []
status: triggered | not_triggered | blocked | ambiguous
blocked_reason:
dependency_ids: []
created_at:
```

A `not_triggered` result is valuable data and should not be omitted.

---

## 6. Signal dependency record

```yaml
dependency_id:
type: input | astronomical | calendar | derived_rule | interpretive_lineage | shared_source
identifier:
description:
parent_dependency_ids: []
```

This graph is used to detect pseudo-convergence caused by duplicate underlying information.

---

## 7. Atomic timing boundary record

```yaml
boundary_id:
system_id:
rule_id:
timestamp:
boundary_type: start | exact | peak | end | discrete_change
precision_seconds:
source_calculation_id:
```

All material boundaries across selected systems are unioned and sorted before constructing atomic windows.

---

## 8. Atomic window record

```yaml
window_id:
run_id:
start:
end:
active_evaluation_ids: []
active_system_ids: []
capability_vector:
convergence_state:
contradictions: []
shared_dependency_ids: []
created_at:
```

Windows are half-open by default:

```text
[start, end)
```

except the final explicitly closed endpoint when needed.

---

## 9. Forecast record

A forecast becomes immutable once frozen.

```yaml
forecast_id:
created_at:
frozen_at:
subject_id:
input_version:
system_config_ids: []
rule_versions: []
claim:
claim_type:
predicted_category:
capability:
capture_area:
window_start:
window_end:
peak_time:
magnitude_band:
confidence_band:
probability: null
hit_definition:
miss_definition:
exclusions: []
known_contradictions: []
dependency_ids: []
preregistration_hash:
status: frozen
```

If numerical probability is used, it must be in `[0,1]` and come from a declared calibration method.

---

## 10. Outcome record

```yaml
outcome_id:
forecast_id:
observed_at:
source_type: external_record | timestamped_record | prospective_self_report | retrospective_report | unavailable
source_id:
raw_observation:
normalized_category:
objective_or_subjective:
scored_at:
score_state: hit | miss | ambiguous | unavailable
scoring_rule_version:
notes_after_scoring:
```

The raw observation must be stored separately from the normalized/scored outcome to prevent rewriting the evidence to fit the prediction.

---

## 11. Validation run record

```yaml
run_id:
created_at:
protocol_version:
case_set_id:
system_ids: []
rule_versions: []
control_set_id:
random_seed:
blinding_state:
metrics:
  calculation_correctness:
  specificity:
  window_precision:
  hit_rate:
  false_positive_rate:
  ambiguous_rate:
  brier_score:
  log_loss:
  calibration_error:
  control_delta:
notes:
content_hash:
```

Unused metrics remain null. Do not fabricate values for completeness.

---

## 12. Source record

```yaml
source_id:
source_class: primary_foundational | living_tradition | scholarly | established_secondary | modern_system | xyool_hypothesis | user_derived
system_id:
title:
author_or_tradition:
published_at:
retrieved_at:
locator:
version_or_edition:
content_hash_if_local:
notes:
```

Source age/provenance and predictive validity are distinct dimensions.

---

## 13. Immutability rules

The following are append-only after freezing:

```text
forecast claim
forecast window
hit definition
miss definition
rule versions used
system settings used
confidence/probability assigned
pre-outcome contradictions
```

Corrections are represented as a new record linked by `supersedes` or `amends`, while the original remains available.

---

## 14. Content hashes

Canonicalize structured records before hashing:

```text
UTF-8
sorted keys
stable separators
no volatile formatting fields
SHA-256
```

Hashes are integrity markers, not proof that a forecast was externally timestamped. Strong prospective validation should additionally use a trustworthy timestamped repository/ledger.

---

## 15. Minimum viable evidence set

A validation-grade forecast requires at least:

```text
input identity/version
system identity/settings
rule identity/version
claim
window
hit condition
miss condition
freeze timestamp
preregistration hash
outcome source
closed score state
```

Missing any of these means the record may be useful for exploration but not clean prospective validation.

---

## 16. Degree-node / star-contact contracts

Canonical schema candidates:
- `schemas/degree-node.schema.yaml`;
- `schemas/provenance.schema.yaml`;
- `schemas/star-contact.schema.yaml`.

A validation-grade degree node preserves:
- exact longitude;
- epoch/date;
- coordinate frame;
- calculation provenance;
- derived wrappers as separate fields;
- dependency lineage.

A validation-grade star contact preserves:
- target degree-node ID;
- canonical star ID/catalog;
- common epoch/frame;
- contact method;
- threshold;
- longitude and/or spherical separation;
- contact-rule ID;
- semantic-rule IDs separately.

Astronomical contact and interpretive meaning must never be fused into one opaque field.

## 17. Catalogue / manifest identity

When fixed stars or minor bodies participate, store the frozen manifest IDs:

~~~text
fixed_star_catalog_manifest_id
minor_body_manifest_id
active_minor_body_tier
star_contact_policy_id
degree_corpus_id_if_used
~~~

A later catalog release or object-set change creates a new configuration/version rather than silently changing an old forecast.
