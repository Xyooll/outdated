# Xyool — Research Validation Governance

Status: **DOMAIN-CANONICAL RESEARCH SAFETY PROTOCOL**

## Purpose

Xyool improves by repeated gauntlets, revisions, and external research. That creates a second-order risk: a method can appear strong because many alternatives were tried against the same history.

This protocol treats **research trials themselves as first-class evidence**.

Core rule:

> A better backtest is not evidence of a better system unless Xyool can account for how many alternatives were tried, what was known before outcome reveal, and whether the result survives fresh data.

---

## 1. Trial registry

Every materially distinct research or strategy variant must receive a `trial_id` before scoring.

Record:

```text
trial_id
trial_family_id
introduced_at
origin / source
hypothesis
universe
selection rule
data vintage / point-in-time boundary
features / states used
decision mapping
entry rule
exit / harvest rule
holding horizon
benchmark
transaction-cost model
borrow assumptions if short
expected direction of improvement
status: TRAINING / VALIDATION / PROSPECTIVE / RETIRED
```

Changing any field that can materially alter trades creates a new trial.

Do not hide variants by calling them "small tweaks."

---

## 2. Dataset roles

Every case/basket must be labeled before outcome reveal:

```text
TRAINING / DEFECT-DISCOVERY
INDEPENDENT VALIDATION
PROSPECTIVE / SHADOW
```

A training or defect-discovery basket can diagnose failure modes and test mechanics.

It cannot be recycled into proof that a repair improves expected returns.

---

## 2A. Epistemic-state / holdout consumption

Every validation cohort has a current epistemic state separate from its original dataset role.

```text
REGISTERED_UNSEALED
SEALED_VALIDATION
PROSPECTIVE_FUTURE
DEVELOPMENT_CONSUMED
TRAINING
RETIRED
```

Canonical rule:

> **Once outcome information has been revealed to the Xyool research process, that cohort is permanently consumed as development data for all descendant methods.**

A consumed cohort remains valid evidence for the method that was frozen before its reveal, but it may not be represented as untouched out-of-sample evidence for a later rule learned from that outcome.

The transition is one-way:

```text
SEALED_VALIDATION
-> REVEAL
-> DEVELOPMENT_CONSUMED

PROSPECTIVE_FUTURE
-> TIME / REVEAL
-> DEVELOPMENT_CONSUMED
```

Do not relabel consumed data as unseen.

---

## 2B. Confirmatory primary endpoint

Before a confirmatory trial can enter `FROZEN`, it must identify exactly one primary endpoint:

```text
primary metric
primary horizon
primary benchmark / cash comparison
```

30/60/90-day or other secondary checkpoints may all be reported, but the primary conclusion cannot be selected after outcome reveal.

If older trials did not explicitly freeze one primary endpoint, preserve that fact as a legacy limitation. Do not reconstruct one from whichever checkpoint later looked most informative.

---

## 2C. Shadow-information blindness

A software rank firewall is not enough when a human researcher can see an experimental signal.

For baseline-vs-augmented trials:

```text
BASELINE RESEARCHER
-> canonical information only
-> baseline decision freeze
-> then experimental shadow information may be revealed to augmented arm
```

If the baseline researcher sees the shadow state before the baseline decision is frozen, the trial must disclose shadow leakage and cannot be treated as a clean test of incremental signal value.

---

## 2D. Trial viability must be checked before blindness is spent

Before baseline research begins, confirm all static prerequisites that can be checked without outcome data:

```text
identity / prior-exposure screen
+ required market-history availability
+ required source availability
+ production-Quant readiness
+ required borrow / execution data availability if the trial depends on them
+ cohort-size sufficiency
```

Only after this **preflight viability gate** passes should the baseline researcher spend the cohort's shadow-information blindness.

If an augmented signal is revealed and the trial later proves structurally unexecutable, the cohort is consumed for that same clean baseline-vs-augmented design even when outcome prices were never revealed.

Rule:

> **Do not spend an untouched cohort on a trial that could have failed a static preflight check.**

A pre-outcome abort remains valuable process evidence and must be recorded rather than repaired in place.

---

## 2E. Contrast sufficiency before outcome reveal

Champion/challenger research requires an actual treatment contrast.

Before revealing outcome data, compute the preregistered arm difference using only information available at the freeze.

Possible capital-relevant contrasts include:

```text
different LONG / SHORT / NO TRADE action
different desired weight
different entry timing
different exit / harvest mapping
different executable treatment explicitly linked to the primary endpoint
```

If the candidate arm is identical to the baseline on the treatment variable relevant to the primary endpoint:

```text
ZERO TREATMENT CONTRAST
-> NON_IDENTIFYING_PRE_OUTCOME
-> DO NOT REVEAL OUTCOME JUST TO SCORE A ZERO
-> PRESERVE OUTCOME HOLDOUT
-> RECORD FEATURE-BLINDNESS AS SPENT
```

Future trials must preregister their minimum acceptable contrast before sidecar reveal. The minimum may be stricter than nonzero when statistical usefulness requires multiple independent treatment changes.

This is a research-efficiency / identifiability safeguard, not an alpha rule.

### Outcome holdout vs feature blindness

Track these separately:

```text
outcome_reveal_status
holdout_consumed

shadow_blindness_consumed
```

A cohort can have:
- sealed outcome data;
- but consumed feature blindness after an experimental signal was revealed.

Do not call such a cohort fresh for the same baseline-vs-feature experiment, but do not falsely label the unseen outcome as consumed either.

---

## 3. Multiple-testing ledger

For every promoted research claim, report:

```text
number_of_material_variants_tried
number_of_universes_tried
number_of_horizons_tried
number_of_selection_rules_tried
number_of_exit_rules_tried
best_variant_selected_after_search: yes/no
```

If the "winner" was selected from a family of alternatives, its naive Sharpe / return is not sufficient evidence.

---

## 4. Selection-adjusted validation

Use the strongest method the sample size permits.

### Deflated Sharpe Ratio (DSR)
Use when comparing Sharpe-like outcomes after multiple trials and non-normal returns.

### Probability of Backtest Overfitting (PBO / CSCV)
Use when Xyool has a family of strategy variants and enough independent observations to compare in-sample winners with out-of-sample ranks.

### White Reality Check / Hansen SPA
Use when many competing predictive rules are tested against a benchmark and data snooping is material.

These methods do not replace fresh out-of-sample testing. They quantify how fragile a discovery may be after model search.

---

## 5. Time-series leakage control

When observations overlap through labels, holding periods, event windows, or delayed accounting information:

- preserve point-in-time information sets;
- separate training and validation chronologically where applicable;
- purge observations whose outcome windows overlap validation;
- use an embargo when adjacent observations can share information through the label horizon;
- keep corporate actions, delistings, and filing availability timestamps point-in-time.

Random row-level train/test splits are not sufficient for time-dependent market research.

---

## 6. Promotion rule

A technique may be promoted in one of two ways.

### Process safeguard
A rule that reduces research bias without claiming return alpha may become canonical immediately.

Examples:
- trial registry;
- freeze-before-outcome;
- point-in-time timestamps;
- transaction-cost accounting;
- borrow-feasibility accounting;
- multiple-testing disclosure.

### Alpha-bearing feature
A feature that changes LONG / SHORT / NO TRADE, rank, size, entry, or exit remains **EXPERIMENTAL** until it shows incremental value on independent frozen cases.

Minimum requirement:

```text
existing Xyool logic
vs
existing Xyool logic + candidate feature
```

on the same fresh, pre-frozen cases.

---

## 7. Required performance decomposition

Do not report raw return alone.

Where sample size permits, report:

```text
raw return
excess return vs cash
excess return vs relevant benchmark
factor-adjusted alpha / residual return
Sharpe / Sortino
max drawdown
expected shortfall
hit rate
average winner / loser
payoff ratio
turnover
estimated transaction cost
capacity / liquidity burden
short borrow cost when applicable
NO TRADE contribution
event-realization return
calibration / Brier score for explicit probabilities
```

---

## 8. Promotion failure conditions

Do not promote a technique when improvement depends on:

- retroactive parameter choice;
- using a training basket as validation;
- ignoring failed variants;
- price information unavailable at decision time;
- post-event analyst estimates or sector evidence;
- unrealistic fills, spreads, or borrow;
- excluding delisted or failed names;
- comparing against an artificially weak benchmark;
- a single lucky outlier;
- a gain that disappears after costs;
- repeated tuning on the same validation set.

---

## 8A. Machine freeze-readiness gate

Future confirmatory trials must pass the repository validator before outcome reveal:

- `scripts/validate_research_trial.py`

The validator blocks, among other conditions:
- future-publication timestamps beyond the freeze;
- missing `trial_family_id`;
- missing primary endpoint / horizon / benchmark;
- missing freeze artifact or commit for a frozen trial;
- incomplete action-rule freeze;
- revealed outcomes not marked as consumed;
- material post-freeze amendments that reuse the same trial;
- shadow-information leakage;
- shorts without an explicit borrow assumption;
- hidden or unrecorded variant multiplicity.

The validator is a process control. Passing it does **not** imply investment alpha.

### Legacy trials

Trials executed before this validator existed are not retroactively promoted to full manifest compliance.

For legacy research:
- reconstruct only fields supported by contemporaneous artifacts;
- mark unavailable preregistration fields `UNKNOWN / NOT EXPLICITLY FROZEN`;
- mark revealed cohorts `DEVELOPMENT_CONSUMED`;
- preserve uncertainty about the effective historical trial count.

Never invent a historical primary endpoint, trial count, or action rule merely to make an old trial pass the new validator.

---

## 9. Canonical research doctrine

```text
IDEA
-> TRIAL REGISTRATION
-> PRE-OUTCOME FREEZE
-> TRAINING / DEFECT DISCOVERY
-> INDEPENDENT VALIDATION
-> SELECTION-ADJUSTED REVIEW
-> PROSPECTIVE SHADOW TEST
-> CANONICAL PROMOTION OR RETIREMENT
```

The stocks remain probes.

**Xyool is the object under test.**
