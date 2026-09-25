# Xyool Astrology — Birth-Time Rectification Protocol

Status: **EXPERIMENTAL DOMAIN CANONICAL / RECTIFICATION AUTHORITY**

Purpose: treat rectification as an explicit model-fitting problem and prevent known life events from being reused as proof that the fitted birth time is correct.

Core rule:

> **Events used to fit a birth time cannot also validate that birth time.**

---

## 1. Evidence hierarchy

Prefer, in order:

```text
contemporaneous birth record
hospital/civil record
reliable family contemporaneous record
reported clock time
bounded approximate interval
rectification inference
unknown
```

A primary record overrides a purely astrological rectification unless there is independent reason to believe the record itself is wrong.

---

## 2. Rectification object

```yaml
rectification_id:
subject_id:
original_input_id:
prior_start:
prior_end:
resolution_step_seconds:
allowed_systems: []
allowed_rule_ids: []
training_event_ids: []
validation_event_ids: []
loss_function:
complexity_penalty:
selected_time:
credible_or_stability_interval:
status:
version:
```

Do not start with an unbounded 24-hour search unless genuinely necessary.

---

## 3. Prior interval

The prior interval comes from non-astrological evidence where possible.

Examples:

```text
“around 3 PM” → declared interval such as 14:30–15:30 based on source confidence
“morning” → broader interval
completely unknown → full-day exploratory search, low confidence
```

The exact interval rule should be documented; do not tighten it after seeing chart fit.

---

## 4. Training events

Use events with relatively clear dates/categories.

Prefer:

```text
externally timestamped events
major moves
formal relationship events
job starts/ends
public launches
education milestones
other predeclared event types
```

Avoid events whose date/category can be flexibly reconstructed from memory.

---

## 5. Validation events

Reserve untouched events before fitting.

Strongest validation:

```text
future/prospective events
```

Next best:

```text
historical events hidden from the rectification process
```

The validation set must not influence selected time, technique, orb, or loss function.

---

## 6. Technique lock

Before search, freeze:

```text
systems
ayanamsha / zodiac
house system
allowed timing techniques
orbs/windows
capture mapping
scoring rules
```

Do not add a technique because it improves the known training-event fit unless the current model is first recorded and the new model becomes a separate version.

---

## 7. Objective function

Rectification needs an explicit loss/score.

Do not use:

```text
“this time feels most accurate”
```

without structured components.

Possible components:

```text
event-category match
timing distance
capture-area match
number of searched configurations
false-positive windows
```

No universal weighting is canonical yet.

---

## 8. Complexity penalty

A time that fits events only by using many extra techniques/configurations should not automatically beat a simpler fit.

Track:

```text
number of techniques searched
number of triggered rules
window coverage
free parameters
```

Prefer parsimonious models when predictive fit is comparable.

---

## 9. Stability interval

Do not report a single exact minute if nearby times perform similarly.

Calculate the region of times that produce materially comparable fit/outputs.

Report:

```text
selected time
stable interval
sensitive boundaries
features that change across interval
```

A 07:43 result with a ±18 minute stability region should not be presented as “birth time proven to 07:43.”

---

## 10. Boundary sensitivity

Flag times near:

```text
Ascendant sign changes
house cusp changes
Moon sign/nakshatra changes
dasha boundary changes
fixed-star/paran thresholds
other discrete state changes
```

A tiny time shift causing a large interpretive change reduces confidence unless independently supported.

---

## 11. Search-grid refinement

Recommended computational strategy:

```text
coarse scan across prior interval
→ retain candidate regions under frozen objective
→ finer scan inside candidates
→ preserve complete score landscape
```

Do not discard unsuccessful times from the research record if doing so would hide the search space.

---

## 12. Holdout performance

After selecting time:

```text
freeze it
→ score untouched validation events
→ compare against alternative candidate times and controls
```

If the selected time does not outperform plausible alternatives out of sample, rectification remains unresolved.

---

## 13. Prospective validation

Best evidence:

```text
rectified time frozen today
→ future forecast generated
→ future outcome scored
```

Do not continue retuning the time after every new event and still call the same rectification validated.

---

## 14. Multiple candidate times

If evidence does not distinguish candidates, preserve a mixture/set:

```text
candidate A
candidate B
uncertainty interval
```

Downstream readings can restrict themselves to features shared across candidates.

---

## 15. Personal narrative leakage

Avoid using personality descriptions as both:

```text
rectification target
and
natal-chart validation
```

This creates circular confirmation.

Prefer objective/timestamped fitting targets where possible.

---

## 16. Rectification confidence

Track separately:

```text
source prior confidence
training fit
validation fit
stability around selected time
prospective replication
```

Do not summarize as one exactness claim unless the evidence supports it.

---

## 17. Failure states

```text
INSUFFICIENT EVENTS
EVENT DATES TOO UNCERTAIN
NO CANDIDATE DISCRIMINATION
OVERFIT TRAINING ONLY
HOLDOUT FAILURE
PROSPECTIVE FAILURE
TECHNIQUE INSTABILITY
INPUT RECORD CONFLICT
```

A failed rectification should return the domain to a wider birth-time uncertainty interval.

---

## 18. Output

Preferred wording:

```text
The current rectification model favors 07:35–07:52 under rule set R3,
but this is an inference interval, not a recorded birth time. Two held-out
events remain to be tested.
```

Not:

```text
Your true birth time is definitely 07:43.
```

Final rule:

> **Rectification is parameter estimation under uncertainty, not a license to make the chart fit the biography.**