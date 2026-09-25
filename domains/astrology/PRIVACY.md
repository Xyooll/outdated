# Xyool Astrology — Privacy & Sensitive Data Handling

Status: **EXPERIMENTAL DOMAIN CANONICAL / DATA-MINIMIZATION AUTHORITY**

Purpose: protect birth data, relationship data, personal event histories, and prospective self-tracking while keeping analytical records reproducible.

Core rule:

> **Store the minimum personal information needed for the analysis, and separate identity from analytical evidence whenever practical.**

---

## 1. Sensitive record types

Treat the following as personal data requiring care:

```text
full name
exact birth date/time/place
precise location
relationship identities
private event history
self-reported capability/behavior logs
health-related observations
contact or account information
```

Public-figure data can still contain source/copyright/provenance concerns even when publicly available.

---

## 2. Subject identifiers

Analytical records should prefer:

```text
subject_id: sub_<opaque-id>
```

over names.

Maintain the name↔subject mapping outside version-controlled research data when practical.

---

## 3. Repository rule

Do not commit private birth/person/event data to the repository merely because the repo is private.

Use:

```text
synthetic fixtures
public benchmark cases with source citations
opaque IDs
local/private data stores excluded by .gitignore
```

A repository becoming public later should not expose user birth data by surprise.

---

## 4. Data minimization

If a calculation needs only:

```text
date/time/location
```

it does not also need:

```text
legal name
address
phone
email
```

Do not collect identity fields for convenience.

---

## 5. Precise location

Birthplace typically requires geographic coordinates for calculation, not current residence.

Store:

```text
birth-location coordinates
```

only where the chosen technique needs them.

Do not reuse current-device location as birth location.

---

## 6. Relationship charts

Synastry/composite analysis involves data from more than one person.

Keep separate subject IDs and source/consent states.

Do not assume one user's permission grants unrestricted disclosure or storage of another person's private data.

---

## 7. Event logs

Prefer normalized event codes for analysis and keep raw narrative notes separately with tighter access where practical.

Example:

```text
analysis record: WORK_CAREER / job_offer / timestamp
private note: narrative details
```

This reduces unnecessary exposure while preserving testability.

---

## 8. Capability self-tracking

Capability records should use only the fields needed for the study.

Avoid collecting unrelated sensitive context just because it might later explain a miss.

New context variables require a prospective protocol version when used analytically.

---

## 9. Health-related data

If Recovery or another capability uses health/device metrics:

```text
collect only with explicit user choice
keep astrology interpretation separate from medical interpretation
never use astrology as diagnostic authority
```

---

## 10. Retention

A data store should define:

```text
purpose
retention period or deletion rule
export method
correction/version method
```

Analytical integrity may require preserving a de-identified frozen record while allowing identity mappings/raw sensitive narratives to be deleted separately.

---

## 11. Corrections

Never silently overwrite a birth-data record used in historical validation.

Correct pattern:

```text
original input version retained in audit history
new corrected input version created
future calculations point to new version
identity-sensitive storage may use separate retention controls
```

---

## 12. Logs

Do not put raw birth data or private narratives into generic debug logs unless required and protected.

Prefer IDs and hashes.

---

## 13. Public benchmark data

For public/historical figures:

```text
record source provenance
record uncertainty/conflicting sources
avoid implying public availability = verified accuracy
```

---

## 14. Synthetic tests

Software tests should default to synthetic subjects/dates unless a public external anchor is specifically needed.

The Maya calculation anchors are date/calendar fixtures and contain no personal data.

---

## 15. Data separation model

Recommended architecture:

```text
IDENTITY VAULT / PRIVATE PROFILE STORE
subject_id ↔ personal identity + raw birth source

ANALYTICAL STORE
subject_id + versioned calculation/rule/outcome records

REPOSITORY
schemas + code + synthetic/public fixtures + aggregate validation
```

---

## 16. Export and portability

If the domain later stores user-specific histories, provide a machine-readable export containing:

```text
input versions
system settings
forecasts
outcomes
scores
rule versions
```

without requiring unrelated identity fields.

---

## 17. External providers

Before sending birth data to an external calculation provider, know:

```text
what fields are sent
why they are needed
provider retention/privacy behavior where relevant
```

Prefer local deterministic calculations when quality and licensing permit.

Final rule:

> **Personal detail should enter the system because the calculation or study needs it—not because astrology invites unlimited biography.**