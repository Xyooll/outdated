# Xyool Astrology — Experiment Design

Status: **EXPERIMENTAL DOMAIN CANONICAL / STUDY DESIGN AUTHORITY**

Purpose: define study designs that can distinguish astrological signal from expectation, routine, base rates, analyst flexibility, and ordinary temporal structure.

Core rule:

> **A useful experiment changes one uncertainty at a time and preserves a real possibility of null results.**

---

## 1. Study families

```text
CALCULATION VALIDATION
Does the engine calculate the declared system correctly?

DESCRIPTIVE DISCRIMINATION
Can a frozen rule distinguish target from decoy better than chance/control?

TIMING DISCRIMINATION
Are outcomes/capabilities enriched in preregistered windows relative to comparable control time?

PROBABILITY CALIBRATION
Do confidence/probability classes match observed frequencies?

CROSS-SYSTEM FUSION
Does combination add information beyond constituents?

N-OF-1 PERSONALIZATION
Does a rule discriminate within one person's repeated observations?

GENERALIZATION
Does a rule survive new subjects/contexts?
```

---

## 2. N-of-1 design

For personal capability timing, a strong initial design is repeated-measures N-of-1.

Procedure:

1. Define capability outcomes independently of astrology.
2. Establish baseline measurements across ordinary days/times.
3. Generate astrology windows without showing them to the subject when practical.
4. Randomize or schedule measurements independently of predicted strength.
5. Record actual capability outcomes.
6. Compare predicted versus control windows within the same person.
7. Repeat across enough cycles to avoid one-week storytelling.

Benefits:

```text
controls stable personal differences
supports personal baselines
reduces between-person noise
allows time-of-day/day-of-week adjustment
```

Limit:

```text
may not generalize to others
```

---

## 3. Measurement schedule

Avoid measuring only when astrology looks interesting.

Preferred options:

```text
random experience-sampling moments
fixed clock times
predeclared task sessions
all qualifying atomic windows plus matched controls
```

If measurement selection depends on the prediction, record that dependency explicitly.

---

## 4. Control windows

Matched control windows should resemble predicted windows on obvious non-astrological dimensions where possible:

```text
time of day
day of week
workday/weekend
sleep context
season/date proximity
scheduled workload
location/context when important
```

Do not compare a 9 AM workday focus prediction only against midnight weekend observations.

---

## 5. Randomization

Useful randomization targets include:

```text
measurement prompts
which decoy chart/date is shown to an analyst
order of cases
which predictions are hidden/revealed
control-window selection within matching constraints
```

Do not randomize the underlying astrology calculation itself except when constructing a deliberate shuffle/placebo control.

---

## 6. Blinding levels

```text
B0 — open: subject and analyst know prediction
B1 — subject blinded
B2 — outcome scorer blinded
B3 — analyst blinded to outcome
B4 — analyst + subject + scorer separated where practical
```

Record blinding level per study. Open studies remain useful for exploratory/user-utility questions but are weaker for efficacy claims.

---

## 7. Expectancy exposure

If the subject saw the forecast before the outcome, store:

```text
forecast_seen: true
seen_at:
expected_effect:
```

This allows separate analysis of:

```text
prediction association
versus
prediction + expectancy intervention
```

Both can be interesting, but they answer different questions.

---

## 8. Baseline period

Before calibrating personal thresholds, gather baseline observations with no astrology-based selection if possible.

Estimate:

```text
mean / median
variance
circadian pattern
day-of-week pattern
serial correlation
measurement adherence
```

Use these as null/context models rather than assuming every deviation is astrologically generated.

---

## 9. Serial correlation

Daily/hourly outcomes are not independent coin flips.

Capability states can persist because of:

```text
sleep
a project deadline
relationship conflict
illness
weather
work schedule
habit
prior-day state
```

Validation should consider lagged outcome/state when enough data exists.

Do not treat hundreds of adjacent atomic windows as hundreds of independent samples.

---

## 10. Clustered windows

If several astrology windows occur inside one persistent real-world episode, define a clustering rule.

Possible unit:

```text
calendar day
episode
forecast cycle
subject-day
```

Use a unit appropriate to the outcome. Preserve raw windows but avoid overstating effective sample size.

---

## 11. Discovery protocol

For discovering candidate rules:

```text
allow broad feature inspection
label all resulting rules DISCOVERY
record search space
freeze new rule version
move to untouched cases
```

Discovery work can be creative; confirmation cannot reuse the same flexibility.

---

## 12. Confirmatory protocol

Before running:

```text
freeze hypothesis
freeze rule version
freeze population/case inclusion
freeze outcome taxonomy
freeze window construction
freeze controls
freeze scoring
freeze exclusion rules
```

Then run without changing rules.

---

## 13. Sample splitting

Recommended structure when enough data exists:

```text
DISCOVERY
→ TUNING / VALIDATION
→ FINAL UNTOUCHED TEST
→ PROSPECTIVE REPLICATION
```

Do not repeatedly inspect the final test set while tuning.

---

## 14. Event studies

For discrete external events:

```text
select event category independently
predefine event timestamp rule
predefine astrology signal/window
compare event-window frequency with matched non-event periods
```

A later event narrative cannot choose which astrology technique was “really” active.

---

## 15. Chart matching studies

For natal/descriptive claims:

1. Freeze rule-derived structured descriptions.
2. Build target plus plausible decoys.
3. Randomize presentation order.
4. Use blinded raters/subjects where possible.
5. Score target selection or graded similarity under predeclared rules.
6. Track whether descriptions differ in length/detail.

Generic flattering descriptions need Barnum/Forer controls.

---

## 16. Multi-system study design

Correct sequence:

```text
System A alone
System B alone
System C alone
→ frozen fusion rule
→ fusion test
→ ablations
```

Do not construct fusion after inspecting which systems happened to hit each case.

---

## 17. Personalization

A personal rule may be fit only from past/training observations and then tested forward.

Avoid:

```text
"Mars means Action for this person because Mars was active on the day they acted" 
```

unless that association is subsequently frozen and tested on future Mars windows and controls.

---

## 18. Stopping rule

Predefine when a study stops if practical:

```text
N observations
N resolved forecasts
calendar duration
number of independent cycles
```

Do not stop immediately after a favorable streak and call it validated.

---

## 19. Missing data

Record why data is missing:

```text
forgotten measurement
technical failure
subject unavailable
outcome genuinely unobservable
```

Do not discard missing periods differently depending on forecast direction.

---

## 20. Reporting

Every experiment report should state:

```text
question
protocol version
systems/rules
population/case set
blinding
controls
sample size/effective sample unit
missing data
metrics
results
uncertainty
misses
changes allowed only after scoring
```

Final rule:

> **Use astrology to generate the hypothesis; use study design to prevent astrology from grading its own homework.**