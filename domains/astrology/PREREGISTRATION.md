# Xyool Astrology — Preregistration & Forecast Integrity

Status: **EXPERIMENTAL DOMAIN CANONICAL / ANTI-HINDSIGHT AUTHORITY**

Purpose: make forecasts auditable before outcomes occur and prevent post-hoc changes from being counted as original predictions.

Core rule:

> **A forecast earns predictive evidence only from the version that was frozen before the outcome was known.**

---

## 1. Freeze object

Before a forecast can enter prospective validation, freeze:

```text
forecast_id
created_at
subject/date identity
input version
system IDs + configuration versions
rule IDs + versions
claim
predicted category / capability
capture area if used
window start
window end
peak if used
magnitude band if used
confidence band or calibrated probability
hit definition
miss definition
exclusions
known contradictory signals
known dependencies
```

Then compute a canonical content hash.

---

## 2. Canonical hashing

For JSON-like records:

```text
remove preregistration_hash field
normalize timestamps to ISO-8601 UTC where possible
sort keys recursively
serialize using stable separators
encode UTF-8
SHA-256
```

Store the resulting hash in the forecast record.

A hash detects changes to the frozen content. It does not by itself prove when the record existed; use repository commit time, signed ledger, or another trusted timestamp for stronger evidence.

---

## 3. Forecast lifecycle

```text
DRAFT
→ FROZEN
→ OPEN
→ CLOSED_PENDING_SCORE
→ SCORED
```

Optional terminal states:

```text
CANCELLED_PRE_WINDOW
UNAVAILABLE_OUTCOME
INVALIDATED_INPUT_ERROR
```

`INVALIDATED_INPUT_ERROR` is allowed only for a demonstrable pre-existing data/calculation defect, not because the forecast looks likely to miss.

---

## 4. Amendments

A frozen forecast is never edited in place.

If new information arrives before or during the window:

```text
original forecast remains frozen
→ create amendment record
→ state reason
→ state what information was newly available
→ create new forecast version if needed
```

The original forecast is still scored under its original rules unless the protocol explicitly classifies the new information as a valid predeclared cancellation condition.

---

## 5. Cancellation rules

Valid cancellation conditions must be declared before the forecast window.

Examples:

```text
birth input shown to be wrong by primary record
calculation engine defect proven
subject/event ceases to exist in a way that makes outcome impossible
predeclared missing-data condition occurs
```

Invalid cancellation reasons:

```text
new contradictory astrology signal not originally considered
forecast appears to be failing
analyst changes interpretation
window feels too narrow
another system disagrees
```

Those belong in scoring/miss analysis.

---

## 6. Window closure

At `window_end`:

1. mark forecast closed;
2. collect outcome evidence under the predeclared outcome-source rules;
3. preserve raw outcome evidence;
4. normalize using the frozen scoring rubric;
5. assign `hit / miss / ambiguous / unavailable`;
6. compute applicable metrics;
7. write post-score notes separately.

Never extend the window because the expected event did not occur.

---

## 7. Multi-claim forecasts

Avoid bundling many predictions into one statement.

Preferred:

```text
FC001 — Focus elevated during X window
FC002 — Communication friction elevated during X window
FC003 — Partnership-domain event more likely during Y window
```

Not preferred:

```text
"A powerful transformative period may affect work, love, creativity, money, identity, and communication."
```

Each claim should have its own miss condition.

---

## 8. Confidence lock

Confidence is frozen before outcome review.

If using labels:

```text
LOW
MEDIUM
HIGH
```

If using probability:

```text
0.0 <= p <= 1.0
```

Probabilities require a named calibration model/version. Uncalibrated intuition should remain a confidence band rather than pseudo-precision.

---

## 9. Discovery forecasts

A forecast generated while inspecting historical outcomes is not prospective evidence.

Label:

```text
RETROSPECTIVE DISCOVERY
```

It can generate a rule hypothesis for untouched cases but cannot be counted as a clean hit.

---

## 10. Blind scoring

When practical, scoring should be performed without exposing:

```text
which astrology system generated the claim
analyst confidence
whether the case is expected to be positive/negative
```

This reduces motivated interpretation at the outcome-labeling stage.

---

## 11. Forecast ledger invariants

A ledger implementation should enforce:

```text
frozen record hash matches stored content
original frozen record cannot mutate
amendments reference parent forecast
outcome cannot be scored before required window closure unless event occurrence itself closes the rule
post-score notes cannot alter raw outcome
rule versions referenced by a forecast remain addressable
```

---

## 12. Minimum prospective standard

A forecast counts toward prospective performance only if:

```text
[ ] frozen before outcome
[ ] timestamped
[ ] hashed
[ ] rule/system versions locked
[ ] hit and miss defined
[ ] window finite
[ ] outcome evidence collected by declared method
[ ] closed regardless of hit or miss
```

Final rule:

> **Do not reward a system for predictions it was allowed to rewrite after reality answered.**

---

## 13. Star Astrology / full-chart manifest freeze

Before a Star Astrology or degree-node v2 forecast can count as prospective evidence, freeze in addition to the normal forecast record:

~~~text
degree-system ID/version
degree-corpus ID/version if used
coordinate-frame policy
ephemeris release/data manifest
fixed-star catalogue ID/version/hash
star-contact algorithm
star orb/threshold
magnitude threshold if used
longitude-vs-spherical contact mode
minor-body catalogue manifest
active minor-body tier
house system
rulership/dispositor convention
aspect set/orbs
timing techniques
outcome ontology
null-model set
ablation model ID A/B/C/D/E
multiplicity family
~~~

No object, star, degree corpus, orb, or timing method may be added to a frozen confirmatory run because the original configuration appears to miss.

## 14. Experiment package

A confirmatory Star Astrology run should reference:
- `catalogs/fixed-stars/manifest.yaml`;
- `catalogs/minor-bodies/manifest.yaml`;
- `rules/star_degree_seed_v1.yaml` or its explicit successor;
- `research/system-tests/astrology-predictive-v1-2026-09-24/ABLATION-PROTOCOL.md`.

The package should be hash-frozen before outcome review.
