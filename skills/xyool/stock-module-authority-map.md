# Xyool — Stock Module Authority Map

Status: **CANONICAL PRECEDENCE / COMPATIBILITY MAP**

Purpose: preserve useful prior Xyool work without allowing older names, state ladders, or research heuristics to conflict with the current stock-market architecture.

This file does not replace the underlying modules. It answers:

> **Which module owns which question, what remains useful, and what has been superseded or rejected?**

---

## 1. Current authority chain

```text
COMPANY-LEVEL XYOOL
→ DISCOVERY VISIBILITY (ESTABLISHED QUALITY ∪ HIDDEN TRANSITION)
→ OSE economic/state context
→ QUALITY QUALIFIER
→ BREADCRUMBS / FES / CAUSAL TIMERS / PFS / RPT as evidence inputs
→ TTC + CATALYST PROFITABILITY
→ DESIRED ECONOMIC EXPOSURE
→ QUANT downward-only risk / expression controls
→ EVENT EXECUTION POLICY
→ EXECUTABLE POSITION / CASH
```

Authority rules:
- Discovery Visibility decides whether a candidate remains research-visible before Quality exclusion; it has no capital authority.
- Quality decides normal capital eligibility.
- TTC owns capital priority and desired economic exposure.
- Quant may reduce/change expression within its tested authority; it may not invent the thesis or exceed TTC desired exposure.
- Event Execution may stage, delay, harvest, trail, or recycle TTC-approved exposure; it may not promote a blocked equity or increase above TTC/Quant caps.

---

## 2. Current module map

| Module | Current role | Status / treatment |
|---|---|---|
| `discovery-visibility-gate.md` | pre-Quality research visibility; established-quality ∪ hidden-transition intake | **CANONICAL PROCESS; NO CAPITAL AUTHORITY** |
| `sec-filing-company-memory.md` | SEC filing intake, per-stock evidence aggregation, insider-origin/hidden-transition discovery, cross-filing confluence | **CANONICAL PROCESS; NO CAPITAL AUTHORITY** |
| `time-to-catalyst.md` | capital priority, return velocity, earned-vs-new capital, desired action | **CANONICAL** |
| `ttc-evidence-tested-rules.md` | promoted/rejected allocation rules and historical evidence | **CANONICAL EVIDENCE GOVERNANCE** |
| `ttc-catalyst-profitability.md` | event integrity, Happens?/Profit View internals, price-response analogs, cascade dependency | **CANONICAL PROCESS; NUMERIC CALIBRATION PROVISIONAL** |
| `ttc-event-execution-policy.md` | tactical/thesis sleeves, entry/harvest/trailing/rebuy mechanics | **PROVISIONAL EXECUTION LAYER** |
| `ttc-breadcrumb-to-timer-detection.md` | mandatory public-evidence scanner; WATCHING/ARMED/ACTIVE | **PROMOTED PROCESS; WEIGHTS PROVISIONAL** |
| `causal-timer-framework.md` | identifies the actual transition clock and causal bottleneck | **KEEP — PROVISIONAL TAXONOMY / TTC INPUT** |
| `ose-forward-evidence-state.md` | broad upstream state from requirement through fielding | **KEEP — BROAD FORWARD-EVIDENCE STATE** |
| `pre-funded-event-hunter.md` | specific not-yet-realized funded order/procurement maturity | **KEEP — PROVISIONAL PROCUREMENT EXECUTION INPUT** |
| `pfs-promotion-standard.md` | promotion/demotion rules for PFS and Hazard Heat | **CANONICAL PFS PROCESS; NUMERIC RUNGS PROVISIONAL** |
| `ose-cascade-score.md` | measures actual replication/rollout after meaningful adoption | **KEEP — PROVISIONAL HUNTING/STATE VARIABLE** |
| `ttc-repeat-cadence-question.md` | mandatory question: what repeats and when could it repeat again? | **KEEP AS PROCESS QUESTION** |
| `rollout-probability-timer.md` | canonical timing interpretation for comparable repeat/cascade events | **KEEP / CANONICAL TIMER IMPLEMENTATION; CURVE PROVISIONAL** |
| `ttc-window-proximity.md` | old name for RPT timing concept | **SUPERSEDED COMPATIBILITY POINTER** |
| `ose-dual-confirmation.md` | Structural Confirmation, Conversion Confirmation, Runway Lock-In | **PROMOTED / REQUIRED** |
| `ose-sector-demand.md` | external demand regime context | **KEEP / REQUIRED CONTEXT; NO INDEPENDENT CAPITAL AUTHORITY** |
| `conversion-debt.md` | weak-conversion/financing-burden early warning | **KEEP RESEARCH/TRACKING ONLY; NOT SELL TRIGGER** |
| `ttc-insider-activity.md` | classifies catalyst-window insider behavior | **KEEP CANONICAL CLASSIFICATION; DIRECTIONAL WEIGHT PROVISIONAL** |
| `opportunity-state-engine.md` | base ontology for Potential, trajectory, Ignition, Recognition, Remaining Opportunity | **KEEP BASE ONTOLOGY WITH LEGACY COMPATIBILITY LIMITS** |
| `top50-exact-date-display-standard.md` | human-facing Top-50 format | **CANONICAL PRESENTATION** |
| `miss-to-question-learning-loop.md` | converts misses into generalizable questions/tests | **CANONICAL GOVERNANCE** |
| `market-expectations-execution-sidecar.md` / Quant `V09` | experimental market-recognition/execution evidence including IV expected-move walls | **RESEARCH ONLY; NO CAPITAL AUTHORITY** |

---

## 3. Legacy compatibility rules

### A. CAC is a legacy allocation name

Older OSE/Sector-Demand files refer to a separate **Capital Allocation Controller (CAC)**.

Current authority is:

> **TTC is the capital-allocation / rotation layer. There is no separate current CAC controller beneath or beside TTC.**

When an older file says:

```text
OSE → CAC → Quant
```

interpret it as:

```text
OSE → Quality / TTC → Quant
```

Do not resurrect a second allocator merely because a legacy file uses CAC terminology.

### B. Single `Confirmation` is compatibility-only

The original `opportunity-state-engine.md` uses a single `C0-C5 Confirmation` ladder.

Current analyses must use:
- Structural Confirmation (`SC`);
- Conversion Confirmation (`CC`);
- Runway Lock-In (`RL`) where relevant.

Aggregate `Confirmation` may be preserved for backward compatibility / historical comparison only. It must not overwrite SC/CC distinctions.

### C. Ignition remains descriptive, not causal authority

The legacy Ignition ladder can remain useful as a market/recognition state description.

It may corroborate recognition/execution context, but it cannot:
- promote Quality;
- promote PFS/FES/CS;
- make Hazard Heat HOT;
- create a funded-event timer;
- force a trade by itself.

Price action is downstream observation, not proof that procurement or conversion occurred.

---

## 4. Similar-looking modules that should NOT be merged

### Breadcrumb Detection vs FES vs PFS

- Breadcrumb Detection asks: **did new public information change a specific causal transition?**
- FES asks: **how far has broad upstream economic evidence progressed?**
- PFS asks: **how mature is the path to this exact not-yet-realized funded event?**

Keep all three.

### PFS vs Hazard Heat

- PFS = causal/procurement maturity.
- Heat = time proximity.

A PFS4/PFS5 event can stay WARM for months.

### Cascade Score vs RPT

- Cascade Score = is replication actually happening, and how broadly?
- RPT = where are we in the supported timing window for the next comparable repeat?

Keep both; do not double-count the same repeat event.

### FES vs Cascade Score

- FES leads a future event before realization.
- Cascade Score records real/authorized replication after meaningful adoption evidence.

They can coexist at different points of the same causal chain.

### Quality / SC-CC-RL vs TTC

Quality decides whether normal capital can compete.
TTC decides where qualified capital should go now.
Do not collapse them into one master score.

---

## 5. Superseded execution/timing assumptions

### Universal `1/3 → 1/3 → 1/3` for unscheduled funded events

**SUPERSEDED for unscheduled funded orders/repeat procurement.**

Use:

```text
PFS STATE × HAZARD HEAT
→ raw tactical rung
→ Recognition / remaining Profit View cap
→ TTC / Quant / liquidity cap
```

The 1/3 concept may still be used as a research comparison for other non-binary operating catalysts, but it is no longer the default procurement entry ladder.

### `Buy the day before the catalyst`

**REJECT as a universal strategy.**

It remains a possible specialized execution choice for exact-date, under-recognized, non-binary catalysts. Unscheduled funded events should be owned through the causal window when evidence earns exposure.

### Fixed ordinary stop-loss as primary binary-event risk control

**REJECT.** Overnight binary failures can gap through stops. Primary control is pre-event sizing from modeled failure gap / risk budget.

### Aggressive continuous rotation among healthy qualified winners

**REJECTED by historical stress testing.** A relative TTC rank change alone does not force removal of earned capital.

### Cascade as a direct price predictor

**REJECT.** Cascade is causal/economic state. Price response still depends on recognition, surprise, valuation, capture, financing and materiality.

### Recurring economics automatically imply persistent price appreciation

**REJECT.** Payoff persistence remains useful economic information; price-recognition persistence is separate.

### Fixed confidence-sensitive concentration ladder

**NOT PROMOTED.** Concentration may reflect confidence qualitatively, but the tested fixed sizing ladder did not earn authority.

---

## 6. Useful older ideas that remain active

### Reusable Asset Monetization (RAM)

Keep as a business/economic-state input where the company owns reusable rental assets.

Useful for questions such as:
- utilization;
- rental margin;
- rental revenue / asset base;
- whether rentals lead to purchases/standardization.

Do not call it SaaS and do not let RAM substitute for procurement evidence.

### Payoff Persistence / Activated Economic Stream

Keep after catalyst closeout:
- one-off realization;
- repeatable discrete;
- run-rate activation;
- stacked/overlapping run-rate;
- decaying/terminable run-rate.

It updates remaining opportunity; it does not create a price-persistence multiplier.

### Conversion Debt

Keep as warning context, especially when SC remains high but CC, cash conversion and financing deteriorate.

Do not use it as a mechanical sell trigger until a new trigger survives validation.

### Sector Demand

Keep as external context that can strengthen/weaken Potential/SC when independently evidenced.

Do not use sector strength to rescue weak company capture.

### Insider classification

Keep the transaction-mechanism classification and 10b5-1 timing checks.

Do not use a universal insider-sale bearish multiplier.

---

## 7. Precedence when files disagree

Use this order:

1. current domain manifest / system instructions;
2. evidence-tested promoted/rejected rule files;
3. current canonical process standard for the exact question;
4. newer calibrated specialized module;
5. older base ontology / compatibility field;
6. research-only candidate.

Specific examples:
- `pfs-promotion-standard.md` controls PFS/Heat promotion over looser examples in older calibration notes.
- `rollout-probability-timer.md` controls the old `ttc-window-proximity.md` name.
- `ose-dual-confirmation.md` controls SC/CC interpretation over single legacy Confirmation.
- `time-to-catalyst.md` controls capital authority over old CAC references.
- `ttc-evidence-tested-rules.md` controls rejected allocation heuristics even if an older research file still describes them positively.

Never silently average conflicting rules.

---

## 8. Current improvement frontier

The architecture should now resist adding new conceptual layers unless a miss exposes a genuinely missing question.

Current work should concentrate on calibration:
- PFS/Heat realization rates by 30/60/90/180 days;
- false positives and stale signals;
- Profit View event-class distributions;
- recognition-consumed thresholds;
- entry-rung sizes and decay;
- harvest/trailing/re-buy mechanics;
- transaction/liquidity realism;
- untouched forward results.

> **The remaining problem is mainly calibration and execution validation, not adding more state machines.**