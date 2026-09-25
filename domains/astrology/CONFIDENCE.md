# Xyool Astrology — Confidence Model

Status: **EXPERIMENTAL DOMAIN CANONICAL / UNCERTAINTY AUTHORITY**

Purpose: prevent one vague confidence label from mixing input quality, calculation certainty, source authenticity, rule evidence, and cross-system agreement.

Core rule:

> **Confidence is a vector first. A single summary label is optional and must never hide a weak critical component.**

---

## 1. Confidence dimensions

For a material claim track separately:

```text
INPUT CONFIDENCE
How trustworthy/precise are birth/event/date inputs?

CALCULATION CONFIDENCE
How reproducible is the calculated/calendar state under declared settings?

PROVENANCE CONFIDENCE
How certain are we that the rule accurately represents its named source/tradition?

RULE-EFFICACY CONFIDENCE
How much controlled evidence supports the rule for this purpose?

TIMING CONFIDENCE
How precise/validated is the timing window?

CAPTURE CONFIDENCE
How strongly does the rule support the predicted life area/outcome category?

TRANSLATION CONFIDENCE
How well-supported is translation into the Xyool capability vocabulary?

SYNTHESIS CONFIDENCE
How well-supported is combining multiple signals/systems after dependency adjustment?

OUTCOME-EVIDENCE CONFIDENCE
How reliable is the evidence used to score the result?
```

---

## 2. Initial qualitative states

Until empirically calibrated, use:

```text
HIGH
MEDIUM
LOW
BLOCKED
NOT_APPLICABLE
```

Do not convert these to numeric probabilities by arbitrary mapping.

---

## 3. Critical-path rule

Some confidence components are prerequisites.

Examples:

```text
If INPUT = BLOCKED for exact birth time,
then angle/paran/house-dependent claims = BLOCKED.

If CALCULATION = BLOCKED,
interpretation using that calculation = BLOCKED.

If RULE-EFFICACY = LOW/UNTESTED,
high calculation precision does not make the prediction high-confidence.
```

Do not average a blocked component away.

---

## 4. Provenance is not efficacy

Example:

```text
PROVENANCE: HIGH
The rule is clearly present in a named traditional text.

RULE EFFICACY: UNTESTED / LOW
Xyool has not shown that the rule predicts the target outcome beyond controls.
```

This is a valid and common state.

---

## 5. Calculation is not interpretation

Example:

```text
CALCULATION: HIGH
Exact transit geometry is reproducible.

RULE EFFICACY: LOW
Meaning assigned to that transit has weak/no controlled validation.
```

Never collapse these into “high confidence astrology.”

---

## 6. Confidence object

```yaml
input: high | medium | low | blocked | not_applicable
calculation: high | medium | low | blocked | not_applicable
provenance: high | medium | low | blocked | not_applicable
rule_efficacy: high | medium | low | blocked | not_applicable
timing: high | medium | low | blocked | not_applicable
capture: high | medium | low | blocked | not_applicable
translation: high | medium | low | blocked | not_applicable
synthesis: high | medium | low | blocked | not_applicable
outcome_evidence: high | medium | low | blocked | not_applicable
notes: []
```

---

## 7. Summary label

If a user-facing summary is needed, use conservative logic.

Possible states:

```text
CALCULATED / NOT VALIDATED
EXPLORATORY
LOW CONFIDENCE
MEDIUM CONFIDENCE
HIGH CONFIDENCE — EMPIRICALLY CALIBRATED ONLY
BLOCKED
```

`HIGH CONFIDENCE` for predictive claims should not be available until the relevant class has demonstrated calibration prospectively.

---

## 8. Cross-system agreement

Raw agreement may increase `synthesis` attention but cannot increase `rule_efficacy` automatically.

Correct:

```text
3 low-dependency systems converge
→ synthesis hypothesis strengthened
→ still require prospective fusion evidence
```

Incorrect:

```text
3 systems agree
→ 90% confidence
```

---

## 9. Numerical probability

Numerical probabilities require:

```text
defined outcome
defined horizon
sufficient historical/prospective sample
calibration method/version
out-of-sample calibration check
```

Store:

```yaml
probability:
calibration_model_id:
calibration_sample_n:
calibration_period:
```

If these are absent, use qualitative confidence only.

---

## 10. Uncertainty propagation

When upstream uncertainty affects downstream outputs, preserve it.

Example:

```text
birth time ±20 min
→ Ascendant changes across interval
→ house placement changes
→ capture mapping LOW/BLOCKED
→ planet sign stable
→ sign-level native interpretation may remain calculable
```

Do not downgrade unrelated stable features unnecessarily.

---

## 11. Sensitivity analysis

For uncertain inputs/settings, calculate outputs across plausible alternatives when feasible.

Report:

```text
STABLE FEATURES
change little across plausible range

SENSITIVE FEATURES
change materially

DISCONTINUOUS FEATURES
cross a sign/house/day/boundary
```

Confidence should track sensitivity rather than a generic “birth time approximate” disclaimer.

---

## 12. Evidence decay

Confidence in a live timing claim may decay when:

```text
window expires without outcome
input is superseded
source/provider changes
rule is rejected/demoted
calibration drifts
```

Do not preserve an old high-confidence label after its evidence basis changed.

---

## 13. Unknown is a valid state

Use `UNKNOWN` in narrative outputs when the structured confidence dimensions do not support a conclusion.

Do not force every chart/configuration into a strong interpretation.

---

## 14. User-facing explanation

A concise reading may say:

```text
Calculation: high confidence
Traditional meaning: source-documented
Predictive evidence: still experimental
Cross-system convergence: partial, with shared dependencies
```

This is more useful than one opaque “confidence: 8/10.”

Final rule:

> **Never let certainty in the astronomy, calendar, or source wording inflate certainty in an unvalidated prediction.**