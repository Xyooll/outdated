# Xyool Astrology — Capability Outcome Ontology

Status: **EXPERIMENTAL DOMAIN CANONICAL / OUTCOME DEFINITION AUTHORITY**

Purpose: make the 10-capability framework measurable enough for prospective testing instead of relying on retrospective impressions.

Core rule:

> **A capability must be defined independently of the astrology signal that predicts it.**

---

## 1. Measurement layers

For each capability distinguish:

```text
SUBJECTIVE STATE
what the person reports feeling/experiencing

BEHAVIORAL PERFORMANCE
observable task/action behavior

EXTERNAL OUTCOME
what happened in the environment
```

Do not treat these as interchangeable.

Example:

```text
high subjective Focus
≠ necessarily high productivity
≠ necessarily favorable external outcome
```

---

## 2. Common rating scale

For lightweight prospective self-tracking use a fixed 0–4 scale:

```text
0 = unusually low / strongly impaired
1 = below personal baseline
2 = normal personal baseline
3 = above personal baseline
4 = unusually high / strongly expressed
```

Ratings should be collected before revealing the astrology prediction when practical.

A personal baseline is preferable to population stereotypes for N-of-1 testing.

---

## 3. Mental Capacity

Definition:

> Available cognitive bandwidth for reasoning, holding complexity, learning, and coherent decision processing.

Possible subjective indicators:

```text
mental sharpness
working-memory ease
ability to understand complexity
cognitive fatigue
```

Possible behavioral proxies:

```text
error rate on standardized task
time to solve a fixed class of problems
working-memory task performance
completion of planned cognitively demanding work
```

Do not define Mental Capacity from productivity alone.

---

## 4. Focus

Definition:

> Ability to sustain attention on the selected target and resist irrelevant switching.

Subjective indicators:

```text
sustained-attention ease
distractibility
urge to task-switch
```

Behavioral proxies:

```text
uninterrupted work duration
number of unplanned task switches
planned-task completion rate
```

Focus is distinct from Energy: a person can be energetic but scattered.

---

## 5. Action

Definition:

> Readiness and ability to initiate and carry through intentional behavior.

Subjective indicators:

```text
drive
activation
resistance to starting
physical/behavioral momentum
```

Behavioral proxies:

```text
latency from intention to start
number of planned actions initiated
completion of action-oriented tasks
```

Action is not the same as impulsiveness.

---

## 6. Opportunity

Definition:

> Rate or salience of externally available openings that could advance a declared objective.

Unlike most capabilities, Opportunity is substantially environment-facing.

Possible external indicators:

```text
inbound invitations
useful introductions
unexpected resources
relevant openings/offers
serendipitous access events
```

Predefine what qualifies as an opportunity for the specific study. Do not count any pleasant event after the fact.

---

## 7. Communication

Definition:

> Ease, precision, reception, and effectiveness of information exchange.

Subjective indicators:

```text
verbal fluency
clarity expressing ideas
perceived misunderstanding
```

Behavioral/external indicators:

```text
message corrections needed
conversation misunderstandings
response/acceptance of a clearly defined request
communication-task ratings by blinded third party
```

Do not reduce Communication to sociability.

---

## 8. Creation

Definition:

> Ability to generate, develop, and externalize novel or expressive material.

Subjective indicators:

```text
idea generation
creative flow
novel-association ease
```

Behavioral proxies:

```text
number of usable ideas under fixed prompt
completion of creative artifact
blinded quality/novelty rating where feasible
```

Quantity and quality should be scored separately.

---

## 9. Investigation

Definition:

> Capacity/motivation to probe beneath surface information, detect structure, and pursue unresolved questions.

Subjective indicators:

```text
curiosity
pattern-search drive
tolerance for ambiguity
```

Behavioral proxies:

```text
relevant questions generated
sources checked
errors/anomalies discovered in a fixed task
```

Investigation is distinct from Mental Capacity: it describes inquiry orientation, not only cognitive horsepower.

---

## 10. Connection

Definition:

> Ease and quality of affiliative, relational, and cooperative engagement.

Subjective indicators:

```text
felt social openness
felt attunement
relational ease
```

Behavioral/external indicators:

```text
successful planned social interaction
reciprocal engagement
conflict/repair outcome under predeclared criteria
```

Connection should not be judged from number of messages alone.

---

## 11. Recovery

Definition:

> Ability to downshift, restore depleted capacity, and return toward personal baseline after exertion/stress.

Subjective indicators:

```text
restfulness
perceived restoration
ability to relax
post-effort recovery
```

Behavioral/device proxies when voluntarily available:

```text
sleep quality measures
rest adherence
return-to-baseline performance after effort
```

Astrology must not substitute for medical interpretation of health metrics.

---

## 12. Friction / Impulsiveness

This dimension contains two related but separable components.

### Friction

> Resistance, interruption, conflict, or inefficiency that impedes intended action.

Possible indicators:

```text
avoidable delays
rework
misunderstandings
unplanned interruptions
subjective resistance
```

### Impulsiveness

> Tendency toward rapid action without sufficient deliberation relative to the person's intended decision standard.

Possible indicators:

```text
unplanned purchases/actions if explicitly tracked
premature messages/decisions
reversals after insufficient deliberation
```

For validation, store `friction` and `impulsiveness` separately when data permits; combine only at the output layer if useful.

---

## 13. Composite Tuner variables

The 5-signal Tuner is a downstream compression:

```text
Energy
Direction
Stability
Intensity
Clarity
```

Each must be calculated from predeclared capability inputs rather than free-form impression.

Initial mapping candidates remain hypotheses:

```text
Energy     ← Action + Recovery context
Direction  ← Focus + Opportunity alignment
Stability  ← Recovery + low Friction
Intensity  ← Action + Friction/Impulsiveness amplitude
Clarity    ← Mental Capacity + Focus + Investigation
```

Do not hard-code weights until validation supports them.

---

## 14. Measurement timing

For atomic-window studies, avoid rating every tiny interval if measurement itself would disrupt behavior.

Possible designs:

```text
end-of-window rating for selected preregistered windows
experience-sampling at randomized moments
end-of-day summary plus objective logs
fixed tasks at comparable times across days
```

Measurement schedule must be chosen before seeing astrology outputs in confirmatory studies.

---

## 15. Blinding

Strongest practical design:

```text
astrology system predicts window
→ prediction hidden from subject
→ capability/outcome collected
→ prediction revealed/scored later
```

When blinding is impossible, track expectancy exposure explicitly.

---

## 16. Personal baseline

For N-of-1 work establish baseline distributions before assigning probability thresholds.

Track:

```text
mean
variance
time-of-day pattern
day-of-week pattern
measurement adherence
```

This prevents normal circadian or routine effects from being misattributed to astrology.

---

## 17. Outcome independence

Do not score an outcome using language copied from the astrology interpretation.

Bad:

```text
prediction: "high Mars energy"
outcome: "felt Mars energy"
```

Better:

```text
prediction: Action 3–4 / Friction elevated
outcome: start latency, completed actions, interruption count, blinded 0–4 rating
```

---

## 18. Minimum capability record

```yaml
subject_id:
observed_at:
window_id:
measurement_method:
blinded_to_prediction: true | false
mental_capacity:
focus:
action:
opportunity:
communication:
creation:
investigation:
connection:
recovery:
friction:
impulsiveness:
notes:
```

Fields not measured remain null.

Final rule:

> **Translate symbols into capabilities only if the capability can be defined and measured without looking back at the symbol.**