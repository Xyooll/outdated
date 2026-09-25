# Xyool Astrology — Risk of Bias & Threat Model

Status: **EXPERIMENTAL DOMAIN CANONICAL / BIAS CONTROL AUTHORITY**

Purpose: enumerate failure modes that can make an astrology framework appear more accurate than it is, and require controls appropriate to each threat.

Core rule:

> **If a result can be explained by analyst freedom, selection, expectancy, or base rates, do not attribute the excess confidence to astrology.**

---

## 1. Barnum / Forer flexibility

Threat:

```text
broad statements feel personally specific while fitting many people
```

Controls:

```text
decoy descriptions
blind matching
specificity coding
predeclared category/capability outcomes
```

---

## 2. Confirmation bias

Threat:

```text
remembering hits more than misses
searching for supporting manifestations
```

Controls:

```text
forecast ledger
mandatory window closure
explicit null outcomes
miss log
```

---

## 3. Hindsight bias

Threat:

```text
outcome makes the “correct” symbol/technique look obvious afterward
```

Controls:

```text
preregistration
frozen rule versions
hidden outcomes
retrospective discovery label
```

---

## 4. Selection bias

Threat:

```text
studying only dramatic charts/dates or only subjects who report resonance
```

Controls:

```text
predefined inclusion rules
consecutive/random cases
all eligible windows logged
```

---

## 5. Survivorship / publication bias

Threat:

```text
successful readings are preserved; failures disappear
```

Controls:

```text
append-only ledger
publish/report all preregistered cases
retain rejected rules
```

---

## 6. Multiple comparisons

Threat:

```text
many planets, aspects, stars, houses, techniques, systems, and windows make some match likely by chance
```

Controls:

```text
predeclared search set
search-space logging
holdout/prospective validation
appropriate multiplicity correction for confirmatory tests
```

---

## 7. Researcher degrees of freedom

Threat:

```text
changing orb, house system, ayanamsha, timing window, event meaning, or rule after seeing results
```

Controls:

```text
system-config version
rule version
forecast hash
no post-hoc rescue
```

---

## 8. Expectancy / suggestion effect

Threat:

```text
seeing a forecast changes behavior or self-report
```

Controls:

```text
subject blinding when testing efficacy
record prediction exposure
separate “forecast association” from “forecast-as-intervention” studies
```

---

## 9. Demand characteristics

Threat:

```text
participant gives responses they think the astrologer expects
```

Controls:

```text
blinded outcome forms
neutral wording
objective/behavioral measures where possible
```

---

## 10. Regression to the mean

Threat:

```text
readings sought during unusually bad/good periods are followed by normal reversion
```

Controls:

```text
baseline time series
matched control periods
pre-event trend measurement
```

---

## 11. Circadian / weekly / seasonal confounding

Threat:

```text
Focus, Action, Recovery, social events, and opportunities naturally vary by clock time/day/season
```

Controls:

```text
matched windows
null temporal models
personal baseline
stratified or residualized comparison when enough data exists
```

---

## 12. Autocorrelation

Threat:

```text
adjacent hours/days share the same real-world state, inflating effective N
```

Controls:

```text
clustered units
block bootstrap/permutation when eventually implemented
report raw N and effective episode/day N
```

---

## 13. Outcome relabeling

Threat:

```text
a career forecast becomes “really about identity” after no career event occurs
```

Controls:

```text
frozen outcome taxonomy
capture-area lock
original miss remains a miss before new hypothesis is created
```

---

## 14. Semantic double counting

Threat:

```text
one configuration generates several synonymous predictions counted as multiple hits
```

Controls:

```text
prediction families
dependency graph
one causal episode / one family scoring where declared
```

---

## 15. Cross-system pseudo-convergence

Threat:

```text
several systems agree because they share the same planet/date/source interpretation
```

Controls:

```text
dependency metadata
effective evidence groups
ablation
dependency-aware fusion tests
```

---

## 16. Source circularity

Threat:

```text
modern sources copy each other, creating fake “traditional consensus”
```

Controls:

```text
source lineage
primary/foundational references when practical
separate independent traditions from derivative summaries
```

---

## 17. Rectification circularity

Threat:

```text
birth time is tuned to known events, then those same events are used as evidence that the chart works
```

Controls:

```text
training events separated from validation events
holdout future/untouched events
rectification version frozen before test
```

---

## 18. Instrumentation drift

Threat:

```text
rating scale, app, ephemeris, tzdb, rules, or converter changes during a study
```

Controls:

```text
version every instrument
new version = new cohort or explicit compatibility analysis
```

---

## 19. Missingness bias

Threat:

```text
measurements are skipped more often during inconvenient or contradictory periods
```

Controls:

```text
track adherence
record missingness reason
compare missingness by predicted state
```

---

## 20. Data leakage

Threat:

```text
analyst sees biography/outcome information while constructing the forecast
```

Controls:

```text
minimal input packet
blind case IDs
separate calculation/interpretation/scoring roles where possible
```

---

## 21. Overpersonalization from tiny samples

Threat:

```text
one or two personal coincidences become a custom law
```

Controls:

```text
label discovery only
require repeated prospective replication
shrink confidence toward general/uninformed baseline
```

---

## 22. Tool/provider opacity

Threat:

```text
external astrology tool changes hidden defaults or versions
```

Controls:

```text
store raw output
store provider/version/settings
cross-check anchor cases
prefer reproducible calculation layers
```

---

## 23. Bias audit object

Each validation report should state:

```yaml
outcome_blinded:
subject_blinded:
analyst_blinded:
pre_registered:
search_space_predeclared:
missing_data_rate:
forecast_exposure:
source_lineage_checked:
dependency_graph_complete:
known_biases: []
```

---

## 24. Interpretation of positive results

A positive result should become weaker, not stronger, when:

```text
sample is tiny
claims are broad
controls are weak
analyst is unblinded
forecast coverage is huge
many techniques were searched
outcomes are retrospective
```

Do not use confidence language that ignores these conditions.

Final rule:

> **The system is strongest when it actively searches for ways its own apparent accuracy could be an artifact.**

---

## 25. Star-catalogue density / asteroid mining

Threat:

~~~text
with enough stars, asteroids, degrees and broad orbs,
almost every chart/date can be made to contain a compelling contact
~~~

Controls:
- frozen star catalogue;
- frozen magnitude/inclusion policy;
- frozen contact method/orb;
- report fraction of degree space covered by admitted contacts;
- rotated-star null catalogue;
- bounded asteroid tiers;
- no namesake-asteroid search in confirmatory work.

## 26. Degree-corpus flexibility

Threat:

~~~text
switching among Sabian or other degree-symbol corpora
after seeing which interpretation fits
~~~

Controls:
- corpus ID/version frozen before outcome review;
- degree-index convention frozen;
- alternate corpora treated as separate systems/rules;
- permuted-cell null in validation.

## 27. Orb rescue

Threat:

~~~text
a failed contact becomes a hit after widening the orb
~~~

Controls:
- predeclared orb grid in discovery;
- one frozen threshold for confirmation;
- sensitivity analyses reported separately;
- original miss remains a miss under its frozen rule.

## 28. Coordinate-wrapper pseudo-evidence

Threat:

~~~text
one longitude generates sign + decan + house + degree + star labels
that are counted as independent convergence
~~~

Controls:
- dependency graph;
- feature-family ablation;
- effective evidence groups;
- no confirmation count based only on number of derived labels.
