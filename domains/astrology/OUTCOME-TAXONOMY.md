# Xyool Astrology — Outcome & Event Taxonomy

Status: **EXPERIMENTAL DOMAIN CANONICAL / OUTCOME NORMALIZATION AUTHORITY**

Purpose: keep forecasts testable by defining outcome categories before the result is known.

Core rule:

> **The outcome taxonomy must be independent of the astrological symbols used to predict it.**

---

## 1. Two parallel taxonomies

Xyool should maintain separate outcome families:

```text
A. CAPABILITY / STATE OUTCOMES
measured using `CAPABILITY-ONTOLOGY.md`

B. EXTERNAL EVENT OUTCOMES
observable events or state changes in the world
```

Do not convert one into the other after the fact.

---

## 2. External event hierarchy

Use a hierarchical category so a forecast can specify its intended resolution.

Suggested broad families:

```text
RELATIONSHIP
WORK / CAREER
MONEY / RESOURCE
HOME / FAMILY
TRAVEL / RELOCATION
EDUCATION / LEARNING
CREATIVE / PUBLICATION
SOCIAL / NETWORK
ADMINISTRATIVE / LEGAL
TECHNICAL / EQUIPMENT
SCHEDULE / DELAY
OPPORTUNITY / OFFER
CONFLICT / DISPUTE
COMPLETION / LAUNCH
OTHER_PREDECLARED
```

These categories describe events, not astrological meanings.

For medical or safety-sensitive outcomes, do not use astrology as diagnostic or decision authority; any research category must be handled under the standards of the relevant domain.

---

## 3. Event object

```yaml
event_id:
subject_id:
occurred_at:
start_at:
end_at:
category:
subcategory:
direction: favorable | adverse | neutral | mixed | not_applicable
magnitude_band:
source_type:
source_id:
objective_or_subjective:
preexisting_or_new:
notes_raw:
```

Do not infer `direction` from the astrological prediction. Determine it from the event definition or scorer rules.

---

## 4. Predeclare subcategories

For a given study, narrow categories before forecasting.

Example:

```text
OPPORTUNITY / OFFER
- job offer
- collaboration invitation
- customer/business opportunity
- funding/resource offer
- social invitation
```

A forecast for `job offer` does not become a hit because the subject received a dinner invitation unless the forecast was explicitly at the broader `OPPORTUNITY / OFFER` level.

---

## 5. Specificity ladder

Record the level at which the claim is made:

```text
LEVEL 0 — general state only
LEVEL 1 — broad event family
LEVEL 2 — named subcategory
LEVEL 3 — subcategory + direction
LEVEL 4 — subcategory + direction + capture/person/domain
LEVEL 5 — above + narrow timing/magnitude condition
```

Do not compare accuracy across specificity levels without accounting for their different difficulty.

---

## 6. Event timestamp policy

Prefer the time the event actually occurred over the time it was later reported.

Store separately when available:

```text
occurred_at
observed_at
reported_at
```

For slow state changes, use start/end intervals or a declared decision date rather than inventing an exact timestamp.

---

## 7. Event source quality

Recommended hierarchy:

```text
externally timestamped record
contemporaneous personal record
prospective self-report collected on schedule
retrospective self-report
later narrative reconstruction
```

Source quality affects evidence confidence, not whether the event emotionally mattered.

---

## 8. Magnitude bands

Do not invent universal magnitude units across event types.

Use category-specific bands defined before scoring, for example:

```text
MINOR
MODERATE
MAJOR
```

with operational criteria in the study protocol.

A magnitude prediction cannot be rescued by ignoring magnitude after the event happens.

---

## 9. Multiple events in one window

A forecast specifies whether it predicts:

```text
AT_LEAST_ONE
EXACTLY_ONE
COUNT_RANGE
SPECIFIC_EVENT
STATE_LEVEL
```

If unspecified, default to `AT_LEAST_ONE` for categorical event forecasts but record event counts separately to avoid hidden multiplicity.

---

## 10. Repeated events

Repeated/common events require base-rate-aware scoring.

Track:

```text
ordinary event frequency
inter-event intervals
calendar coverage of prediction windows
```

A frequent event is easier to “predict” by chance.

---

## 11. Event independence

Several records may represent one causal episode.

Example:

```text
argument
follow-up text
cancellation
repair conversation
```

A study may classify these as one episode or several events, but the episode rule must be defined before outcome review.

Do not count one episode as multiple independent hits merely because it generated multiple records.

---

## 12. Opportunity taxonomy

Because Opportunity is a capability/output dimension, distinguish:

```text
OPPORTUNITY_PRESENT
an objectively available opening exists

OPPORTUNITY_NOTICED
subject becomes aware of it

OPPORTUNITY_ACTED_ON
subject takes action

OPPORTUNITY_CONVERTED
opening produces the target outcome
```

These are different transitions and may have different predictors.

---

## 13. Conflict taxonomy

Separate:

```text
internal friction
interpersonal disagreement
external obstacle
delay / blockage
technical failure
```

Do not score all unpleasant experiences as one “malefic” outcome.

---

## 14. Outcome-code lock

Once a benchmark begins, the taxonomy version is frozen.

New event types discovered during scoring may be added only as a new taxonomy version and tested prospectively/untouched thereafter.

Original cases retain their original coding rules.

---

## 15. Blinded normalization

Where possible, the scorer translating raw observations into taxonomy codes should not know:

```text
forecast direction
astrology system
confidence band
```

This reduces category stretching.

---

## 16. Null outcome

Explicitly support:

```text
NO_QUALIFYING_EVENT
```

A quiet window is data. It must not disappear from the dataset.

---

## 17. Unknown versus null

Keep distinct:

```text
NO_QUALIFYING_EVENT — observed and none occurred
OUTCOME_UNAVAILABLE — insufficient observation to know
```

Treating unavailable outcomes as nulls biases results.

Final rule:

> **Decide what counts before looking at what happened.**