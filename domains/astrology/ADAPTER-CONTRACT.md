# Xyool Astrology — Calculation Adapter Contract

Status: **EXPERIMENTAL DOMAIN CANONICAL / CALCULATION INTERFACE AUTHORITY**

Purpose: define how external or internal calculation engines plug into Xyool without leaking engine-specific assumptions into interpretation.

Core rule:

> **Adapters calculate and normalize state; they do not assign astrological meaning.**

---

## 1. Adapter responsibilities

A calculation adapter may:

```text
validate supported input shape
resolve or require a time scale
calculate astronomical/calendar state
return exact settings/version metadata
propagate calculation warnings/uncertainty
return deterministic normalized output
```

It may not:

```text
choose an interpretive tradition
silently select an ayanamsha/house system
change a requested setting to make a chart calculable
assign personality/event meaning
combine systems
invent missing birth data
```

---

## 2. Canonical request

```yaml
request_id:
system_id:
input_id:
instant:
  civil_datetime:
  timezone:
  utc_datetime:
  uncertainty_seconds:
location:
  latitude:
  longitude:
  elevation_m:
calendar_convention:
settings: {}
requested_outputs: []
```

A date-only calendar system may omit instant/location fields that are genuinely irrelevant.

---

## 3. Canonical response

```yaml
request_id:
system_id:
adapter_id:
adapter_version:
engine:
engine_version:
data_version:
calculated_at:
settings_effective: {}
raw_state: {}
derived_state: {}
precision: {}
warnings: []
blocked_fields: []
source_ids: []
content_hash:
```

`settings_effective` must expose the settings actually used, even if they match defaults.

---

## 4. Required adapter methods

Conceptual interface:

```text
supports(request) -> bool / reason
validate(request) -> errors/warnings
calculate(request) -> CalculationRecord
health() -> engine/data/version status
```

A future Python adapter should implement these deterministically where the engine permits.

---

## 5. Error model

Use explicit error classes/states such as:

```text
UNSUPPORTED_SYSTEM
UNSUPPORTED_DATE_RANGE
INVALID_CIVIL_TIME
TIMEZONE_UNRESOLVED
MISSING_LOCATION
MISSING_REQUIRED_BIRTH_TIME
INVALID_SETTING
EPHEMERIS_DATA_MISSING
CALCULATION_CONFLICT
PRECISION_INSUFFICIENT
LICENSE_OR_PROVIDER_BLOCKED
```

Never substitute a fallback silently.

---

## 6. Cross-check interface

Validation-grade calculations should support comparison of two normalized records.

Compare only fields expected to agree under matched settings.

Example output:

```yaml
comparison_id:
primary_calculation_id:
crosscheck_calculation_id:
matched_settings: true
field_differences:
  sun_longitude_deg:
    delta: 0.00001
    tolerance: 0.0001
status: agree | minor_difference | material_difference | incomparable
```

Do not compare tropical versus sidereal positions as though one engine is wrong.

---

## 7. Suggested calculation sources

### Solar-system astronomy

Potential high-quality calculation/cross-check sources:

```text
JPL Horizons
Skyfield + pinned JPL ephemeris file
Astropy where suitable
Swiss Ephemeris / pysweph where licensing and deployment terms are acceptable
```

As of 2026, Skyfield 1.55 is a current MIT-licensed release and is suitable for high-precision positions when used with an appropriate JPL ephemeris. Astropy 8.0.1 is a current BSD-licensed astronomy platform. These are astronomy engines, not complete astrological interpretation systems.

Swiss Ephemeris remains particularly useful for astrology-specific calculations such as houses/fixed stars but deployment must preserve its version/data and comply with its licensing model.

No provider is canonical merely because it is convenient.

---

## 8. Ephemeris pinning

If an adapter uses an external ephemeris file, record:

```text
file/family name
download/source URI
version/release
coverage range
SHA-256
```

Do not allow the same adapter version to silently switch ephemerides across benchmark runs.

---

## 9. House adapter

House calculations require explicit:

```text
house system
observer latitude/longitude
civil/UT conversion
sidereal-time conventions
engine/version
```

At high latitudes, some house systems may fail or behave discontinuously. Return an explicit blocked/warning state rather than switching systems.

---

## 10. Sidereal adapter

A sidereal calculation requires a named ayanamsha/reference.

Return:

```text
ayanamsha name
ayanamsha value at epoch if available
engine implementation/version
```

Do not identify all sidereal charts as Jyotish.

---

## 11. Fixed-star adapter

Require:

```text
star identifier
catalogue/source
coordinate epoch
proper-motion handling
observer/time relation for parans
```

Separate astronomical coordinates from astrological star meaning.

---

## 12. Maya adapter

Current internal implementation:

```text
agent.astrology.maya
system: MAYA.TRAD
civil input: proleptic Gregorian date
correlation: explicit, default GMT_584283
outputs: Long Count, Tzolk'in, Haab
```

Current boundaries:

```text
supports dates at/after 0.0.0.0.0 under configured correlation
does not implement regional interpretive meaning
does not implement Dreamspell
does not imply intraday timing
```

---

## 13. Dreamspell adapter

A future adapter must explicitly define:

```text
implementation/version
Gregorian mapping algorithm
leap-day handling
Day Out of Time handling
Kin/Tone/Solar Seal/Wavespell derivation
```

Do not infer these rules from `MAYA.TRAD`.

---

## 14. Adapter promotion

An adapter is calculation-validated only after:

```text
known anchor cases
boundary/edge cases
independent cross-checks
settings identity tests
invalid-input tests
version pinning
reproducibility tests
```

Final rule:

> **Normalize engines behind one contract, but never normalize away the settings that make their outputs different.**