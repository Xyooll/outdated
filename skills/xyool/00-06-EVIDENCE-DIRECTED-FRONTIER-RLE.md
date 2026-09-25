# Xyool — Evidence-Directed + Frontier Recursive Learning

Floware execution:
`floware/core/learning.flow.md`

The Flow is the reasoning authority. Existing RLE software is supporting deterministic machinery and must not become the default location for new learning logic.

Status: **CANONICAL RLE 2.0 GOVERNANCE / IMPLEMENTATION TARGET**
Date: **2026-09-22**

## Core doctrine

> **Research discovers possibilities. Evidence constrains belief. Audit determines relevance. Development implements only what survives. Fresh evidence determines authority.**

A second law prevents validated knowledge from becoming dogma:

> **Evidence constrains belief, but never closes the search space.**

And the authority boundary remains:

> **Novelty may enter freely as a hypothesis; only evidence may increase its authority.**


Goalpost/effectiveness governance is canonical at:
`skills/xyool/00-07-GOALPOST-EFFECTIVENESS-GOVERNANCE.md`

Additional laws:

> **Freeze the goal before optimization. A failed method changes the approach, not the goal.**

> **Seek effectiveness within reason, not perfection. Streamline by evidence; every added layer must earn its complexity.**

## 1. Canonical learning sequence

The default sequence is:

```text
RESEARCH
    ↓
EXISTING EVIDENCE
    ↓
EVIDENCE MAP
    ↓
AUDIT
    ↓
COMPETING EXPLANATIONS
    ↓
MOST-INFORMATIVE TEST
    ↓
DEVELOP CHALLENGER ONLY IF NEEDED
    ↓
FREEZE / PREREGISTER
    ↓
TEST
    ↓
NEW XYOOL EVIDENCE
    ↓
BELIEF UPDATE
    ↓
VALIDATE / SIMPLIFY / REJECT
    ↓
AUTHORITY
    ↓
SELECT NEXT MOST-INFORMATIVE QUESTION
    ↺
```

Development does not precede evidence assessment merely because an idea is coherent.

## 2. Research and evidence are different

Research is the search process.

Evidence is the assessed output of that process.

Research may surface:
- published methods;
- replications;
- failures;
- contradictory studies;
- practitioner techniques;
- alternative representations;
- negative results;
- Xyool's prior trials;
- correspondence-derived questions;
- unresolved anomalies.

The evidence map must then classify material claims as one of:

```text
STRONG
SUPPORTED
MIXED
WEAK
REJECTED
UNKNOWN
```

An evidence record should preserve:
- the claim;
- supporting evidence;
- contradicting evidence;
- population / regime / time period;
- implementation assumptions;
- known failure modes;
- Xyool-local evidence;
- unresolved questions;
- current confidence;
- last challenge date;
- whether authority exists.

External evidence is a prior. It is not target-domain authority.

## 3. Audit comes before development

For every proposed improvement ask:

1. Do we already have this mechanism?
2. Is it implemented correctly?
3. Does it duplicate another signal or latent phenomenon?
4. Does it address a demonstrated Xyool miss, limitation, or opportunity?
5. Does it contradict a current rule?
6. Is the disagreement due to calibration, representation, regime, dependency, execution, or bad evidence?
7. Is there a simpler explanation or implementation?
8. What evidence would make us reject the proposal?

If there is no falsification path, the proposal cannot earn authority.

## 4. Competing explanations, not single-story learning

A miss must not immediately become a rule.

Maintain multiple live explanations when evidence cannot distinguish them.

Example:

```text
H1 event was already expected
H2 valuation/repricing burden dominated
H3 price structure was deteriorating
H4 sector/market regime dominated
H5 entry reaction already consumed recognition
H6 financing/dilution dominated
H7 evaluation horizon was wrong
H8 currently unexplained / noise
```

The next experiment should be selected partly by how well it separates live hypotheses.

A hypothesis may be:
- ACTIVE;
- WEAKENED;
- SUPPORTED;
- REJECTED;
- SUPERSEDED;
- UNRESOLVED.

Do not collapse uncertainty merely to produce one explanation.

## 5. Information-directed experiment selection

The next test should not default to "another N random cases."

Prefer cases/tests with high expected learning value.

Conceptual priority:

```text
EXPERIMENT PRIORITY ≈
expected discrimination / information gain
× decision relevance
× recurrence
× potential capital impact
÷
cost
+ contamination risk
+ delay
```

No false precision is required. Ordinal HIGH / MEDIUM / LOW estimates are acceptable until calibration is earned.

High-value tests include:
- model/action disagreements;
- cases where multiple plausible hypotheses predict different outcomes;
- recurring expensive misses;
- regimes where current evidence is weakest;
- negative controls that could falsify a favored explanation.

A case where every model agrees and the mechanism is already well-supported may be useful for regression, but often carries less learning value.

## 6. Two RLE lanes

Xyool has two complementary recursive-learning lanes.

### Lane A — Evidence-Directed Improvement

Purpose:
- improve or simplify mechanisms already supported by evidence;
- calibrate known relationships;
- repair demonstrated defects;
- compare against simpler baselines;
- reduce uncertainty.

This lane is conservative about novelty but efficient about refinement.

### Lane B — Frontier Experimentation

Purpose:
- search beyond established methods when the current framing reaches a limit.

Frontier Mode may activate when one or more conditions persist:

```text
PERFORMANCE_PLATEAU
REPEATED_UNEXPLAINED_MISS
MODELS_AGREE_BUT_REALITY_DISAGREES
KNOWN_FEATURES_ADD_NO_INFORMATION
REGIME_SHIFT_SUSPECTED
COMPLEXITY_RISES_WITHOUT_GAIN
ANOMALY_CLUSTER
REPRESENTATION_LIMIT
```

Frontier Mode may explore:
- new representations;
- novel feature interactions;
- alternative horizons;
- unconventional technical/statistical structures;
- removal or reversal of established assumptions;
- latent-state clustering;
- new model families;
- correspondence-derived hypotheses;
- new causal/state decompositions.

Hard rule:

> **Frontier Mode gets more freedom of exploration and less authority.**

Every Frontier output begins as RESEARCH_ONLY or SHADOW_ONLY.

## 7. Anomaly mining

Repeated prediction failures are not merely errors to average away.

When similar violations recur:

```text
CURRENT MODEL EXPECTS A
REALITY REPEATEDLY PRODUCES B
```

create an anomaly cluster.

The cluster should record:
- common pre-outcome features;
- what incumbent models predicted;
- what reality produced;
- candidate hidden variables/relations;
- whether the anomaly crosses jobs/classes/regimes;
- possible new representation;
- discriminating test.

Anomaly clusters may justify Frontier Mode even when no published method exists.

## 8. Assumption challenge lifecycle

Canonical rules remain falsifiable.

Every material rule/assumption should be able to record:

```text
ASSUMPTION
SUPPORTING EVIDENCE
CONTRADICTING EVIDENCE
CURRENT CONFIDENCE
REGIME / POPULATION BOUNDARY
LAST CHALLENGED
NEXT CHALLENGE CONDITION
STATUS
```

Possible status:

```text
CANONICAL_SUPPORTED
PROVISIONAL
WEAKENED
SUPERSEDED
REJECTED
RETIRED
```

"Validated" does not mean "never question again."

Challenge priority should increase when:
- regime relevance changes;
- contradictory evidence accumulates;
- simpler models catch up;
- implementation context changes;
- the assumption becomes a major capital bottleneck.

## 9. Evidence age versus regime relevance

Do not decay evidence merely because it is old.

Distinguish:

```text
EVIDENCE AGE
!=
EVIDENCE REGIME RELEVANCE
```

Relevance can decline when material context changes, including:
- market microstructure;
- information diffusion speed;
- regulation;
- liquidity;
- industry structure;
- capital availability;
- accounting/reporting environment;
- execution technology.

Old evidence may remain strong if the mechanism and implementation conditions remain comparable.

## 10. Complexity tax

RLE must be capable of deleting or compressing architecture.

When two candidates have similar validated utility, prefer the simpler representation unless complexity has an independently demonstrated benefit.

Ask:
- does the new feature add information after existing features?
- does it merely rename an existing latent phenomenon?
- can the same result be achieved with fewer fields/rules/models?
- does added complexity improve robustness, calibration, or capital outcomes enough to justify itself?

Possible outcomes include:

```text
PROMOTE
KEEP_SHADOW
SIMPLIFY
MERGE
SUPERSEDE
REJECT
RETIRE
```

Recursive learning is not synonymous with recursive accumulation.

## 11. Repeated testing / holdout governance

The RLE must track at trial-family level:
- hypotheses tested;
- challengers tried;
- horizons examined;
- variants examined;
- outcome peeks;
- holdout consumption;
- selection history;
- freeze artifacts;
- contamination risk.

Repeated outcome inspection consumes information.

A new "best" challenger produced after many variants does not inherit untouched-holdout status.

## 11A. Competing-event / dual-outcome governance

Event-driven trials must distinguish:

```text
CAPITAL OUTCOME
= what the frozen position actually earned over the preregistered horizon

ATTRIBUTION OUTCOME
= what occurred before a later material information event changed the causal state
```

A later material event does not erase the capital path. It creates an attribution boundary.

For stock Recognition:
- fixed-horizon capital scoring remains economically relevant;
- the clean attribution track ends at the last tradable close before the next material event becomes public;
- no competing event means the tracks explicitly coincide;
- competing events must be identified and timestamped;
- post-hoc endpoint replacement is prohibited.

This prevents a 60-session experiment from silently becoming a multi-event causal claim.

See:
`research/system-tests/stock-recognition-dual-outcome-attribution-protocol-2026-09-22.md`

## 12. Relationship to Correspondence

Correspondence remains a question/hypothesis transfer mechanism, not authority transfer.

```text
SOURCE DOMAIN EVIDENCE
        ↓
ABSTRACT RELATION
        ↓
CORRESPONDENCE HYPOTHESIS
        ↓
TARGET-DOMAIN RESEARCH / EVIDENCE MAP
        ↓
TARGET-DOMAIN AUDIT
        ↓
TARGET-DOMAIN TEST
        ↓
TARGET-DOMAIN AUTHORITY
```

Frontier Mode may use correspondence to generate novel hypotheses.

Numeric calibration, actions, objectives and target conclusions remain non-transferable.

## 13. Relationship to Gauntlet

The Gauntlet is an experiment executor and regression surface.

It should increasingly answer:

> **Which cases will teach Xyool the most?**

rather than:

> **How many cases can Xyool process?**

Random/broad batches remain useful for regression and coverage, but active disagreement/anomaly cohorts should receive priority when learning efficiency is the objective.

## 13A. Development-pool mode

Once a domain has accumulated enough resolved cases, ordinary model iteration should default to consumed evidence rather than repeatedly spending fresh holdout cases.

Maintain three evidence roles:

```text
DEVELOPMENT POOL
- consumed outcomes
- feature discovery / ablation / fitting / error analysis
- no validation authority

REGRESSION POOL
- consumed hard cases
- repeated protection against resurrecting known failures
- no validation authority

FUTURE HOLDOUT
- untouched evidence
- consumed only for mature challenger validation or when existing evidence cannot discriminate hypotheses
```

Hard rules:

- Known outcomes may improve a model but cannot validate that improvement.
- Do not spend fresh evidence to answer a question the consumed library can already answer.
- A model chosen after development-pool inspection must receive a new version and later untouched evaluation.
- Archetype-local relationships must not be promoted as universal merely because they fit the pooled development set.
- Correspondence transfers the question/structure, not the fitted sign, coefficient, threshold or action.

For stock payoff/Recognition work, see:
`research/system-tests/stock-payoff-development-ablation-mode-2026-09-22.md`

### Payoff-target separation

Event-driven capital research must also distinguish two jobs:

```text
EVENT-LOCAL PAYOFF
= outcome attributable to the frozen event before a new material information state begins

CAPITAL-PATH PAYOFF
= realized capital path across the full frozen holding horizon, including later state transitions
```

A single event snapshot should not be presumed sufficient for both jobs.

The capital-path engine may use event-local forecasts plus future-event/TTC/dependency state, but this mapping must be tested separately.

## 14. Relationship to Miss-to-Question

Miss-to-Question remains useful but is no longer the first post-miss action.

The sequence becomes:

```text
MISS
→ reconstruct frozen evidence
→ evidence audit
→ competing explanations
→ identify what evidence discriminates them
→ THEN derive missing question/state/process change if supported
```

This prevents every miss from being forced into "we failed to ask a question" when the real cause may be calibration, noise, regime, execution, or a bad representation.

## 15. Authority law

The RLE may search broadly.

It may not:
- promote novelty because it is novel;
- promote established research because it is established;
- treat literature as target-domain validation;
- promote a model using the same outcomes that selected it;
- increase production authority from a consumed holdout;
- allow Frontier Mode to bypass Quality/safety/authority boundaries;
- let a model rewrite its own evaluator without independent governance.

Final law:

> **Research expands the search space. Evidence narrows belief. Audit identifies the real gap. Experimentation may reopen the search space. Only fresh validation increases authority.**
