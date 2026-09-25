# Xyool — TTC Event Execution Policy

Status: **PROVISIONAL EXECUTION LAYER — PROCESS DEFINED; NUMERIC PARAMETERS UNDER CALIBRATION**

## Purpose

Translate a TTC-approved economic opportunity into an entry, harvest, exit, and possible re-entry process without allowing price mechanics to create or override the thesis.

This layer sits downstream of Quality / FES / catalyst integrity / TTC and upstream of the final executable position.

```text
QUALITY / FES
→ TTC + PROFIT VIEW
→ DESIRED ECONOMIC EXPOSURE
→ QUANT RISK / EXPRESSION CAP
→ EVENT EXECUTION POLICY
→ EXECUTABLE POSITION / CASH
```

The execution policy may reduce, delay, harvest, or recycle approved exposure. It may not promote a Quality-blocked name, invent a catalyst, or increase exposure above TTC/Quant authority.

---

## 1. Two-sleeve model

Do not force one exit rule onto every share.

### THESIS / EARNED SLEEVE

Capital that has already earned its place through intact Quality + economics + conversion.

Rules:
- no ordinary trailing stop merely because another stock temporarily ranks higher;
- exit/reduce on thesis invalidation, Quality deterioration, shareholder-capture failure, severe over-recognition, or a materially superior replacement that clears the earned-capital hurdle;
- a realized catalyst closes its timer but does not automatically force liquidation if a new economically relevant timer remains.

### CATALYST / TACTICAL SLEEVE

Temporary exposure specifically justified by an unresolved event/window.

Rules:
- explicit entry window;
- explicit failure/delay downside;
- explicit risk budget;
- explicit profit-harvest logic;
- explicit time stop;
- may use trailing exit and evidence-gated re-entry.

This separation is intended to prevent two opposite errors:
1. holding a temporary event trade forever after its catalyst is exhausted;
2. selling an intact earned compounder because a short-term trailing stop fired.

---

## 2. Do not default to "buy the day before"

The entry rule depends on event class and timing type.

### A. Exact-date binary catalyst

Examples: FDA decision, court ruling, binary readout.

A stop-loss cannot be the primary risk control because overnight news can gap through the stop.

Pre-event exposure is allowed only when:
- Quality/capital status allows it;
- event identity and date are fresh;
- Profit View / downside is positive enough to justify risk;
- the position is sized from the modeled failure gap;
- recognition has not already consumed most of the favorable move.

Primary sizing concept:

```text
MAX CATALYST SLEEVE
<= PORTFOLIO EVENT-RISK BUDGET / MODELED FAILURE GAP
<= TTC DESIRED EXPOSURE
<= QUANT / LIQUIDITY CAP
```

Example only:
- modeled failure gap = 50%;
- allowed portfolio loss on the event = 1%;
- gross pre-event sleeve cap ≈ 2% of portfolio before other caps.

The 1% figure is not canonical; event-risk budgets must be calibrated.

### B. Exact-date non-binary / scheduled operating catalyst

Examples: scheduled launch, earnings, commissioning date.

A T-1 entry may be reasonable only if the event remains under-recognized. Prefer staged exposure across the supported pre-event window rather than an automatic full-size purchase at T-1.

If the stock has already captured most of Profit View before the event, do not chase merely because the date is close.

### C. Company-guided / inferred operating window — non-procurement

Examples: SAT/acceptance, qualification, commissioning, deployment, activation, run-rate proof.

Do not wait for an artificial "day before." Enter only as causal evidence, event probability and remaining Profit View improve.

The earlier universal research sketch:

```text
1/3 — timer ARMED
1/3 — timer enters supported window / evidence strengthens
1/3 — realization / confirmation
```

is **not a canonical universal ladder**. It remains only a comparison baseline for non-procurement operating catalysts until class-specific testing earns better parameters.

### D. Unscheduled funded order / repeat procurement / scope expansion

For an unscheduled funded event, the universal one-third ladder is **superseded** by:

- `skills/xyool/pre-funded-event-hunter.md`
- `skills/xyool/pfs-promotion-standard.md`

The objective is to own the causal procurement window, not guess the announcement day.

Required execution object:

```text
PFS STATE
+ HAZARD HEAT
+ EVIDENCE FRESHNESS
+ MATERIALITY
+ RECOGNITION CONSUMED
+ REMAINING PROFIT VIEW
→ RAW TACTICAL RUNG
```

Current research ladder, as a fraction of the **TTC-approved catalyst sleeve**:

```text
PFS0-PFS2       -> 0%
PFS3 / WARM     -> 0-15%
PFS3 / HOT      -> 10-20%
PFS4 / COLD     -> 0-10%
PFS4 / WARM     -> 20-30%
PFS4 / HOT      -> 40-50%
PFS5 / COLD     -> 20-30%
PFS5 / WARM     -> 40-60%
PFS5 / HOT      -> 60-75%
```

The raw rung is then capped:

```text
RAW PFS/HEAT RUNG
→ Remaining Profit View / Recognition cap
→ TTC desired exposure cap
→ Quant / liquidity / portfolio-risk cap
→ EXECUTABLE TACTICAL EXPOSURE
```

Do not climb the ladder from time passage or price strength. Promotion requires new causal evidence under `pfs-promotion-standard.md`.

A later funded-order headline may be a harvest/reset event rather than the first entry point.

---

## 3. Recognition-consumed control

At every prospective add, calculate conceptually:

```text
RECOGNITION CONSUMED
≈ price move already captured since the relevant signal / entry reference
  relative to remaining Profit View
```

Do not use a rigid universal ratio yet.

Operational interpretation:
- LOW: most modeled payoff remains;
- MEDIUM: partial payoff consumed; stage additions carefully;
- HIGH: event/cascade has already repriced materially; do not chase full size;
- EXHAUSTED: current catalyst Profit View has largely realized; close/reset the timer.

Recognition can block an add without changing the true causal PFS/Heat state.

---

## 4. Sell hierarchy

### Priority 1 — thesis / event invalidation

Exit or sharply reduce the catalyst sleeve when:
- catalyst fails;
- material unexplained delay breaks the timer;
- customer/regulator/program identity changes;
- Quality or shareholder capture deteriorates;
- financing/dilution makes the original per-share economics invalid;
- the downstream profit-producing gate is no longer credible.

This overrides technical trailing logic.

### Priority 2 — event closeout

When a catalyst realizes:
1. close that timer;
2. score the actual event vs Happens? / Profit View;
3. identify the next unresolved profit-producing timer;
4. decide whether remaining economics justify a runner or thesis sleeve.

Do not continue awarding an "imminent catalyst" bonus after realization.

### Priority 3 — Profit View harvest

Provisional ladder for the catalyst sleeve:

```text
FIRST HARVEST
when realized move reaches roughly 50% of Profit View midpoint
→ harvest ~1/3 of catalyst sleeve

SECOND HARVEST
when realized move reaches roughly 80-100% of Profit View upper band
or the catalyst realizes with recognition heavily consumed
→ harvest another ~1/3

RUNNER
retain the final ~1/3 only if a credible downstream timer remains
```

These fractions and thresholds are calibration targets, not final constants.

A gap above the Profit View upper band is normally a harvest/no-chase condition, not a reason to increase exposure.

---

## 5. Trailing exit

Trailing exits apply to the catalyst/runner sleeve, not automatically to the earned thesis sleeve.

Initial research grid:

```text
8% / 10% / 12% / 15% close-based trail from post-entry peak
```

The trail should activate only after:
- first profit harvest; or
- material favorable realization; or
- a minimum favorable excursion established by the calibration study.

Why close-based for initial testing:
- avoids false precision from unknown intraday high/low ordering in daily historical bars;
- reduces whipsaw from thin small-cap prints.

Future production execution may use ATR/volatility-aware intraday mechanics after separate validation.

---

## 6. Time stop

A catalyst sleeve cannot remain open indefinitely merely because the thesis sounds good.

If the supported event window expires:
- timer becomes STALE / DELAYED / RESET;
- reduce or close the catalyst sleeve unless fresh evidence establishes a new window;
- an earned thesis sleeve may remain if the underlying long-duration thesis is still qualified.

For PFS4/WARM-style unscheduled funded events, the current research calibration additionally tests:

```text
~60 calendar days without causal progression
→ no add; normally halve tactical starter

~120 calendar days without progression / explicit reaffirmation
→ normally close/reset remaining tactical sleeve
```

These constants remain provisional and must not be exported blindly to other event classes.

---

## 7. Trailing buy / re-buy

Re-buy is **evidence-gated**, not automatic averaging down.

A trailing-buy mechanism can be used only after all of the following remain true:

```text
Quality still passes
AND a current / new timer remains credible
AND the prior exit was profit-harvest / recognition management, not thesis failure
AND remaining Profit View is again attractive
AND no material adverse evidence has appeared
```

For pre-funded-event trades, also require that current PFS/Heat has not materially deteriorated or that fresh evidence has legitimately re-armed the event.

Then a technical re-entry trigger may be used as execution assistance.

Initial research grid:

```text
Required reset from catalyst peak/gain: 20% / 30% / 40% of the prior catalyst move
Trailing-buy rebound from post-exit low: 3% / 5% / 8%
Maximum mechanical re-buys per unchanged catalyst: 1
```

A new independent catalyst may create a new trade object.

Never mechanically re-buy after:
- failed clinical/regulatory outcome;
- broken customer relationship;
- failed acceptance/qualification;
- destructive financing;
- Quality downgrade that blocks normal capital.

---

## 8. Exact binary gap rule

For binary catalysts, risk is controlled primarily **before** the event through size.

A 10% stop does not protect a position that opens 40-50% lower after bad overnight news.

Therefore:

```text
BINARY RISK CONTROL
= position sizing from failure-gap distribution
+ scenario EV
+ capital-status gate
+ optional hedge where separately validated
NOT
= ordinary stop-loss alone
```

---

## 9. Calibration metrics

Execution rules must be scored on:

```text
terminal capital
median trade return
mean trade return
win rate
max drawdown
worst gap loss
profit captured vs maximum favorable excursion
giveback from peak
turnover
number of re-buys
false re-buys after deteriorating evidence
time in cash
capital-days / opportunity cost
rotation regret
```

Report by event class:
- major funded order / strategic award;
- small contract / scope expansion;
- activation / commissioning;
- technical milestone;
- regulatory binary;
- qualification / acceptance;
- repeat-order cascade;
- run-rate proof.

Do not optimize one parameter set across all classes if the economic path differs materially.

---

## 10. Current provisional execution thesis

The working strategy to test is:

> **Own the causal window, not the calendar day. Risk-size binaries. Scale into operating catalysts as evidence matures. For unscheduled funded events, size by PFS × Hazard Heat. Harvest as Profit View is consumed. Trail only the tactical runner. Re-buy only when causal evidence remains intact and recognition has reset.**

This is deliberately different from:

> buy every stock the day before a catalyst, use a fixed stop-loss, and blindly re-buy every pullback.

The latter is expected to fail on overnight gaps, fully priced events, low-impact technical milestones, broken catalysts, and credible-but-too-early procurement signals.
