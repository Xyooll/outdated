# Xyool Astrology — Multi-System Synthesis Protocol

Status: **EXPERIMENTAL DOMAIN CANONICAL / FUSION AUTHORITY**

Purpose: combine independently generated system outputs without erasing provenance, contradictions, or shared dependencies.

Core rule:

> **Synthesis may compress evidence; it may not manufacture agreement.**

---

## 1. Entry requirement

A system contributes to synthesis only after it has produced:

```text
system_id
system version/settings
native calculated/calendar state
native interpretation/rule IDs
capability translation if used
confidence vector
dependency IDs
```

Do not synthesize free-form prose whose underlying rule identity is unknown.

---

## 2. Synthesis levels

```text
LEVEL 0 — SIDE-BY-SIDE
show native system outputs independently

LEVEL 1 — CAPABILITY ALIGNMENT
translate eligible native outputs into shared capability dimensions

LEVEL 2 — DEPENDENCY-AWARE CONVERGENCE
identify support/conflict after collapsing shared evidence groups

LEVEL 3 — CALIBRATED FUSION
combine signals using weights/models learned prospectively

LEVEL 4 — TUNER COMPRESSION
optional five-signal user-facing compression
```

Until calibration evidence exists, Xyool should normally stop at Level 2.

---

## 3. Direction states

For a shared capability use:

```text
SUPPORTS
INHIBITS
NEUTRAL
MIXED_WITHIN_SYSTEM
NOT_APPLICABLE
UNKNOWN
```

Do not force every rule into positive/negative direction if its native meaning is not directional.

---

## 4. Convergence states

```text
CONVERGENT
multiple low-dependency evidence groups support same capability/direction

PARTIALLY_CONVERGENT
some support, with dependency or contradictory limitations

ORTHOGONAL
systems address different capabilities/outcomes

CONTRADICTORY
material low-dependency signals point in opposing directions

PSEUDO_CONVERGENT
raw agreement exists but collapses to one/shared dependency group

INSUFFICIENTLY_COMPARABLE
translation would distort native meanings
```

---

## 5. No majority vote

Forbidden default:

```text
3 systems positive, 2 negative → positive wins
```

Instead ask:

```text
How many independent information groups?
Which rules have validated efficacy?
Which systems are speaking to the same outcome?
Are timing windows actually aligned?
Are contradictions native or translation-induced?
```

---

## 6. Contradiction decomposition

Record disagreement layer:

```text
CALCULATION
systems/engines disagree on state

NATIVE INTERPRETATION
two traditions assign different meanings

CAPABILITY TRANSLATION
native meanings differ only after Xyool mapping

TIMING
same directional claim but different windows

CAPTURE
same timing/theme but different life area/outcome

MAGNITUDE
same direction but different intensity
```

Different conflict layers require different resolution strategies.

---

## 7. Uncalibrated synthesis output

Before Level-3 calibration, output only structured evidence summaries such as:

```yaml
capability: Focus
state: PARTIALLY_CONVERGENT
supporting_groups: 2
contradicting_groups: 1
dependency_unknown_groups: 1
systems_supporting: [ASTRO.JYO, MAYA.TRAD]
systems_conflicting: [ASTRO.WT.MODERN]
rule_efficacy_status: experimental
notes: []
```

Do not turn this into `72% Focus` without a validated probability model.

---

## 8. Calibrated fusion candidates

Only after enough prospective data, candidate methods may include:

```text
regularized logistic regression
Bayesian hierarchical model
stacked calibrated probabilities
simple predeclared weighted average
```

Requirements:

```text
training data separate from evaluation
weights frozen before test
dependency/correlation considered
probabilities calibrated
ablation performed
simple baselines included
```

Avoid complex models when data is small.

---

## 9. System weights

No permanent a priori weights are canonical.

Future weights should be learned separately by:

```text
outcome category
capability
time horizon
system configuration
population/subject when enough personal data exists
```

A system can be useful for one capability and uninformative for another.

---

## 10. Negative evidence

A validated rule that predicts absence/lower probability is evidence too.

Do not build synthesis only from positive activations.

Record:

```text
supporting presence signals
supporting absence/inhibition signals
contradictory presence signals
```

---

## 11. Missing signals

Absence of a rule trigger is not automatically negative evidence.

Distinguish:

```text
NO TRIGGER
explicit rule did not activate

NEGATIVE TRIGGER
rule actively predicts lower/blocked state

NOT CALCULATED
system/technique unavailable

UNKNOWN
input/rule ambiguity
```

---

## 12. Timing alignment

Two systems converge temporally only if their declared windows overlap under the synthesis rule.

Store:

```text
intersection duration
union duration
peak separation
window precision
```

Do not call two month-long and two-hour predictions “exact convergence” merely because the two-hour window sits somewhere in the month.

---

## 13. Resolution hierarchy

When conflict exists, do not resolve by prestige/age of tradition.

Use, in order:

```text
1. calculation/input integrity
2. native rule identity/provenance
3. relevant target-domain validation evidence
4. dependency independence
5. calibrated performance for this outcome/horizon
6. unresolved conflict if evidence remains insufficient
```

---

## 14. Tuner downstream rule

Tuner may compress only after contradiction state is known.

If compression would hide a material conflict, expose both:

```text
TUNER SUMMARY
+ CONFLICT FLAG
```

Do not average `high Action` and `high Recovery need` into meaningless “medium Energy.”

---

## 15. Fusion ablation

For every calibrated fusion model, evaluate:

```text
all systems
minus each system
minus each dependency group
best single system
null model
```

A system whose removal does not reduce out-of-sample performance may be redundant.

---

## 16. Synthesis versioning

Any material change creates a new fusion version:

```text
added/removed system
new weight
new conflict rule
new dependency mapping
new translation
new calibration model
```

Past forecasts retain their original synthesis version.

---

## 17. User-facing structure

Preferred compact format:

```text
PRIMARY SIGNAL
what the strongest validated/independent evidence says

SUPPORT
which independent systems/groups agree

CONFLICT
what materially disagrees

TIMING
atomic window / uncertainty

CONFIDENCE
calculation vs rule-efficacy vs synthesis confidence
```

Final rule:

> **When evidence conflicts, preserve the conflict until validation—not narrative elegance—resolves it.**