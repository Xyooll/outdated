# Xyool Astrology — Time Standards

Status: **EXPERIMENTAL DOMAIN CANONICAL / TEMPORAL INTEGRITY AUTHORITY**

Purpose: prevent civil-time, timezone, day-boundary, ephemeris-time, and calendar-conversion errors from propagating into astrological interpretation.

Core rule:

> **Never calculate from a local clock label when the actual instant is unresolved.**

---

## 1. Store both civil and absolute time

When time is relevant, preserve:

```text
local civil date/time
timezone identifier
UTC offset actually in force
DST/legal-time status if known
UTC instant
input uncertainty
```

Prefer IANA timezone identifiers such as:

```text
America/New_York
Europe/London
Asia/Kolkata
```

over ambiguous abbreviations such as `EST`, `IST`, or `CST`.

---

## 2. Timezone database version

Historical civil-time conversion depends on the timezone database and local legal history.

Record:

```text
tzdb_version
timezone_name
resolved_utc_offset
```

For dates/places with uncertain historical rules, attach a time-conversion uncertainty flag rather than pretending the offset is exact.

---

## 3. DST ambiguity and non-existent local times

Two edge cases require explicit handling:

```text
FOLD — a local time occurs twice when clocks move backward
GAP  — a local time does not occur when clocks move forward
```

Do not silently choose one fold occurrence. Store a fold/disambiguation value or mark the instant unresolved.

Non-existent local times are invalid until corrected by source evidence.

---

## 4. Astronomical time scales

Do not treat every astronomical API timestamp as plain UTC.

Potential scales include:

```text
UTC
UT1
TT / Terrestrial Time
TDB / Barycentric Dynamical Time
Julian Day defined on a declared scale
```

Record the scale at every adapter boundary.

When using Swiss Ephemeris or JPL sources, respect the documented input/output time-scale conventions rather than converting by intuition.

---

## 5. Delta T

Historical conversions between Earth-rotation time and uniform dynamical time may depend on ΔT estimates.

For ancient/historical calculations:

```text
record delta-T model/source
record model version where possible
propagate material uncertainty into exact-angle/house/paran timing
```

Do not claim second-level historical astronomical timing where the time model cannot support it.

---

## 6. Calendar conventions

For historical dates, explicitly identify:

```text
proleptic Gregorian
historical Gregorian
Julian
other civil/calendar system
```

A date string without a calendar convention can be ambiguous for historical work.

---

## 7. Day boundary identity

Different systems may define a “day” differently.

Possible boundaries:

```text
00:00 local civil time
sunrise
sunset
solar noon
system-specific ritual/calendar boundary
UTC boundary
```

Each rule requiring a day identity must declare its boundary convention.

Do not assume a Maya, Panchang, Dreamspell, or civil day changes at the same instant unless the specific system defines it that way.

---

## 8. Panchang/local astronomical dependence

When using Panchang or other location-dependent calendrical factors, record:

```text
observer location
timezone
date boundary rule
sunrise/sunset calculation source where relevant
ayanamsha and lunar calculation conventions where relevant
```

Do not reuse a Panchang generated for one location as though it were universally local.

---

## 9. Maya civil-date conversion

For `MAYA.TRAD`, record:

```text
input civil calendar convention
input civil date
correlation/converter identity
resulting calendar fields
```

If the rule is date-based rather than clock-time-based, do not introduce artificial intraday precision.

If a living/regional practice defines a boundary differently from the converter's civil-date convention, preserve the regional rule as its own configuration.

---

## 10. Dreamspell boundary convention

For `DREAMSPELL.ARGUELLES`, lock:

```text
Gregorian mapping implementation
13 Moon mapping/version
leap-day handling
Day Out of Time handling
civil-day boundary assumption
```

Different implementations must not be silently mixed in one validation cohort.

---

## 11. Atomic-window precision

Each timing boundary should carry:

```text
timestamp
precision_seconds
source
system_id
rule_id
```

When two boundaries are closer than their uncertainty permits resolving, do not manufacture an ordering. Mark the local window ordering as uncertain or merge according to a predeclared uncertainty rule.

---

## 12. Birth-time precision propagation

Examples:

```text
exact recorded minute ≠ exact physical birth instant
reported “around 3 PM” should become an interval
unknown time should not default to noon without being labeled as a computational placeholder
```

A placeholder time can be used only for time-insensitive calculations and must never be allowed to create authoritative houses/angles/parans.

---

## 13. Time input state

Recommended state:

```yaml
reported_local_time:
source_precision:
uncertainty_interval:
timezone_name:
tzdb_version:
fold:
calendar_convention:
resolved_utc:
resolution_status: verified | reported | approximate | conflicted | blocked
```

---

## 14. Current/future calculations

For live forecasts:

```text
recompute the requested period
record calculation timestamp
record engine/version
close windows after expiration
```

Do not reuse a stale chart/calendar cache when a system's settings or source version changed.

---

## 15. Historical anti-lookahead

Freeze the time-conversion/calculation model used for a historical benchmark before revealing the target outcome.

If a later correction to timezone history is discovered, preserve:

```text
original run
corrected run
reason for correction
```

Do not rewrite the original benchmark record.

Final rule:

> **Every timing claim inherits the precision and ambiguity of the clock, calendar, location, and time scale that produced it.**