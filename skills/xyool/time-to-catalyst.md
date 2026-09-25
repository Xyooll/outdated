# Xyool — Time to Catalyst (TTC)

Status: **CANONICAL CAPITAL-ALLOCATION / ROTATION LAYER**

## Core purpose

Xyool has two conceptual stages:

```text
1. QUALITY QUALIFIER
   Is this opportunity good enough to own?

2. TIME TO CATALYST (TTC)
   Of the qualified opportunities, where should capital be now?
```

TTC is the capital-allocation, ranking, harvest, and rotation layer. There is no separate capital-allocation controller beneath or beside TTC.

The permanent asset is **capital**. Individual securities are temporary capital destinations.

TTC answers:

> **Among opportunities that clear the quality threshold, which one offers the strongest probability-adjusted remaining payoff through time, and therefore deserves the next dollar now?**

TTC is not simply a calendar estimate. It is the complete timing-aware capital decision process.

---

## 1. Authority chain

```text
COMPANY-LEVEL XYOOL + OSE
quality / causal / economic state
        ↓
QUALITY QUALIFIER
PASS / FAIL / WATCH
        ↓
TIME TO CATALYST
probability + magnitude + distance-to-conversion + recognition + friction
        ↓
DESIRED ECONOMIC EXPOSURE
        ↓
QUANT
risk / concentration / execution expression
        ↓
EXECUTABLE POSITION / CASH
```

TTC owns desired economic exposure.

Quant may modify how approved exposure is expressed under the tested interface, but Quant does not invent the economic thesis and may not increase exposure above TTC's desired amount.

---

## 2. Quality prerequisite

TTC ranks **qualified opportunities**. A near catalyst cannot rescue an unqualified equity.

The quality qualifier is built from company-level Xyool and OSE evidence, including as relevant:
- structural demand;
- company-specific control / bottleneck / capture;
- Structural Confirmation;
- Conversion Confirmation;
- Runway Lock-In;
- shareholder capture;
- balance-sheet and financing durability;
- dilution / governance / permanent-impairment risk;
- economic asymmetry / valuation;
- evidence quality;
- credible path to conversion.

Conceptual quality output:

```text
FAIL
WATCH
QUALIFIED
HIGH QUALITY
```

Only QUALIFIED / HIGH QUALITY opportunities normally compete for capital in TTC. A WATCH opportunity may be monitored but should not outrank qualified names merely because a speculative event is close.

Once multiple names clear the quality threshold, small differences in quality should not automatically dominate a large difference in catalyst proximity or return velocity unless they materially change permanent-loss risk.

---

## 3. TTC opportunity object

Every qualified candidate and current holding must be represented as:

```text
TTC OPPORTUNITY
├── Company
├── Current Price / Position
├── Quality State
├── OSE State
├── Expected Outcomes
├── Probability
├── Highest Material Unresolved Catalyst
├── Forward Evidence State / Evidence Quality
├── Catalyst Stage
├── Catalyst Velocity
├── First Detectable Signal Date
├── Current Stage Entry Date
├── Last Confirming Evidence Date
├── Expected Conversion Window
├── Signal Age
├── Window Position
├── Decay Status
├── Remaining Gates
├── Funding / Commitment State
├── Catalyst Materiality
├── Procurement / Conversion Friction
├── Recognition Gap
├── Ignition State
├── Expected Return
├── Return Velocity
├── Remaining Opportunity
├── Downside / Failure State
├── Shareholder Capture
├── Capital Requirement
├── Liquidity / Execution
├── Confidence
└── Next Decision Trigger
```

---

## 4. Master TTC question

For every qualified opportunity ask:

> **How far is this company from the next economically meaningful event that can force a change in earnings, cash flow, backlog, strategic value, or market recognition?**

Then ask:

> **How large and probable is that event relative to the time, friction, downside, and amount already priced?**

TTC therefore integrates five dimensions:

```text
EVENT QUALITY
× EVENT PROBABILITY
× EVENT MATERIALITY
× DISTANCE TO CONVERSION
× REMAINING RECOGNITION GAP
```

subject to shareholder capture, permanent-impairment risk, liquidity, transaction costs, and portfolio constraints.

Do not collapse these dimensions into one opaque score until an empirical formula earns validation.

---

## 5. Catalyst clock

Every material opportunity must identify its relevant **causal clock**, not merely a date on a calendar.

Examples:

```text
DEFENSE / GOVERNMENT
requirement → qualification → funded path → order → delivery → revenue

SEMICONDUCTORS
qualification → design win → production order → ramp → revenue

DATA CENTER / POWER
permit / interconnect → equipment order → construction → energization → utilization

BIOTECH / MEDTECH
trial / submission → regulatory decision → reimbursement / launch → adoption

INDUSTRIAL
customer capex → award → installation → utilization → repeat order

MINING / MATERIALS
offtake / permit → financing → construction → commissioning → production

R&D
prototype → customer trial → customer-funded development → qualification → production order
```

TTC normalizes these different clocks into **distance-to-economic-conversion**.

---

## 6. Mandatory timeline fields

For each material unresolved event track:

```text
Event:
Catalyst Type:
FES Level: FES0-FES5 where applicable
FES Velocity: ↑↑ / ↑ / → / ↓ / ↓↓
Forward Evidence Quality: FE1-FE4
Confidence: Low / Medium / High
Economic Magnitude: Unknown / Small / Material / Transformational

First Detectable Public Signal Date:
Current Stage Entry Date:
Last Confirming Evidence Date:
Expected Conversion Window:
Pre-Catalyst Window:
Single-Date Timer: NONE / EXACT / TARGET
Single-Date Value:
Signal Age:
Window Position: Pre-window / Early / Mid / Late / Overdue / Unknown
Decay: Fresh / Aging / Stale

Funding State:
Remaining Gates:
Conversion Friction:
Next Trigger:
Promotion Trigger:
Demotion Trigger:
Invalidation:

Credible Event Economics:
Funded / Committed Economics:
Unfunded Ceiling / Options:
Catalyst Materiality:
Recognition Gap:
```

Funded commitments must remain separate from ceilings, options, TAM, pipeline, or management aspiration.

---

## 6A. Dual timing objects: single-date timer vs pre-catalyst window

TTC must keep two timing objects separate.

```text
SINGLE-DATE TIMER
= a verified exact event date or a dated target/deadline

PRE-CATALYST WINDOW
= the evidence-supported interval in which the unresolved catalyst can reasonably occur or materially advance and therefore deserves active monitoring / exposure consideration
```

These answer different questions.

- The single-date timer answers: **what dated stop/deadline/event requires calendar attention?**
- The pre-catalyst window answers: **when does the causal state become live enough that Xyool should care before the headline?**

A company may have both.

### Why both are required

An exact or dated deadline does not guarantee that the event resolves on that date. Regulators, customers, counterparties, and companies can act earlier. Therefore:

```text
EXACT / TARGET DATE != OWNERSHIP WINDOW
```

For exact-date binary events, the pre-catalyst window is the interval before the stop event in which exposure, recognition, early-resolution risk, and failure-gap sizing matter.

For unscheduled procurement / orders / scope expansion, the pre-catalyst window is the primary timing object and should be inferred from PFS × Hazard Heat plus the strongest causal/process evidence.

### Human list order

When Xyool renders timing lists:

```text
SINGLE-DATE LIST:
nearest unresolved date first
-> Quality descending within the same date

PRE-CATALYST WINDOW LIST:
earliest active / approaching window first
-> Quality descending within the same time bucket
```

This ordering is for **attention and workflow**, not capital rank. TTC capital priority remains a separate profitability comparison.

### RARE process lesson

The RARE UX111/FAYUVI decision resolved before the previously frozen PDUFA date. This is evidence that a valid dated regulatory timer can still be an incomplete timing representation. The structural fix is to preserve a pre-catalyst window alongside the dated timer; the empirical width/entry benefit of such windows remains subject to backtest and prospective validation.

---
## 7. Forward Evidence State inside TTC

FES is an evidence input to TTC, not a separate allocation layer.

FES asks **what economic event is forming and how far it has progressed**. TTC asks **whether that event, together with all other qualified-opportunity evidence, makes this the best capital destination now**.

FES may improve:
- catalyst-stage classification;
- expected conversion window;
- probability assessment;
- evidence freshness / decay;
- replacement-hurdle judgment;
- research priority;
- return-velocity comparison.

FES may not by itself:
- create a position;
- set a position size;
- force HOLD / BUY / SELL / ROTATE;
- promote realized conversion without actual economic evidence.

Rule:

> **FES informs TTC. TTC owns the capital decision.**

---

## 7A. Auxiliary clocks do not allocate capital

Any auxiliary causal clock may improve evidence-state representation, including:

```text
procurement clock
R&D conversion clock
regulatory clock
continuous-compounding clock
or future domain-specific clocks
```

But a clock state cannot bypass TTC.

Required authority:

```text
CLOCK / CAUSAL STATE
-> TTC CANDIDATE
-> REPRICING / RECOGNITION / HORIZON / CASH COMPARISON
-> CAPITAL ELIGIBLE or NO TRADE
```

Forbidden shortcut:

```text
CLOCK_PASS
-> automatic INITIATE / INCREASE
```

A company may be high quality, operationally strong, and economically durable while still being inferior to cash or another qualified opportunity at the current price and ownership horizon.

This guardrail was reinforced by the 2026-09-19 Continuous-Compounding Clock V4 regression: the experimental clock improved quality selection relative to rejected controls but worsened 90-day capital return and drawdown when PASS was mapped directly to LONG.

---

## 7B. Experimental expectations / execution sidecar

External research supports measuring several potentially useful signals:

```text
earnings / guidance surprise
analyst estimate revisions / dispersion
post-earnings drift
sector-relative / residual momentum
execution cost / capacity
short borrow feasibility
factor attribution
```

These remain **shadow inputs**.

Required experimental authority:

```text
ARM A — canonical TTC
ARM B — same frozen TTC + explicitly registered sidecar authority
```

Outside Arm B or a later canonical promotion:

- revisions may inform investigation but not change capital;
- residual momentum may inform recognition review but not create LONG/SHORT;
- execution estimates may be reported but do not rewrite the economic thesis;
- a negative thesis is not an executable short when borrow is blocked, but short-feasibility alpha effects still require validation;
- shadow-field changes do not invalidate rank.

Any augmented test must report returns **after estimated transaction costs and borrow costs where applicable**.

A later promotion requires incremental improvement versus the same frozen baseline on independent cases and a method-version advance.

---

## 8. Procurement Clock

For procurement-driven catalysts, TTC must compare signal age with an evidence-backed conversion window.

Timing evidence hierarchy:
1. same-company historical programs;
2. same-customer / same-agency programs;
3. same procurement mechanism;
4. close industry comparables;
5. broad sector benchmark only if better evidence is unavailable.

Example:

```text
Expected approval→funded-order window: 6-12 months
Elapsed: 3 months
Window Position: Early
Interpretation: no order yet is not negative evidence
```

Versus:

```text
Expected window: 6-12 months
Elapsed: 17 months
Window Position: Overdue
Interpretation: absence of order is material negative evidence unless a documented delay explains it
```

The absence of conversion only becomes negative when interpreted against the clock.

---

## 9. R&D Conversion Clock

Raw R&D spending is not a TTC signal.

Use:

```text
INTERNAL R&D
  ↓
WORKING PRODUCT / PROTOTYPE
  ↓
NAMED CUSTOMER TRIAL / INTEGRATION
  ↓
CUSTOMER- OR GOVERNMENT-FUNDED DEVELOPMENT
  ↓
QUALIFICATION / HARDENING COMPLETE
  ↓
INITIAL PRODUCTION ORDER
  ↓
REPEAT / SCALED PRODUCTION
```

Customer-funded late-stage R&D and completed qualification are higher-quality timing evidence than raw expense growth.

A decline in customer-funded R&D can be positive when independently explained by transition into production.

---

## 10. Reusable Asset Monetization (RAM)

Where the company owns reusable equipment that can be rented repeatedly, TTC may use:

```text
RAM = rental revenue / average gross rental assets
```

Track:
- RAM velocity;
- rental gross margin;
- fleet growth versus rental-revenue growth;
- utilization commentary;
- project/customer concentration;
- evidence rentals lead to purchase or standardization.

RAM is not SaaS recurring revenue. It is **repeatable asset revenue with utilization risk**.

RAM can support current economics while a future catalyst develops; it is not a substitute for procurement or other conversion evidence.

---

## 11. Catalyst materiality

TTC must separate **proximity** from **size**.

Conceptually:

```text
Catalyst Materiality
≈ credible funded/committed company-capturable economics
  relative to enterprise/equity value and the current earnings base
```

Rules:
- funded commitments > ceilings;
- guaranteed minimums > optional maximums;
- company-capturable economics > headline program size;
- per-share capture > gross corporate headline;
- include dilution, warrants, preferred securities, working capital and capex where material.

A tiny near-term event does not automatically outrank a larger event slightly farther away.

---

## 12. Return velocity

TTC's central comparative question is:

> **How much probability-adjusted remaining capital gain is available relative to the likely time required to realize it?**

Compare:
- expected return;
- probability of catalyst / conversion;
- catalyst materiality;
- expected conversion window;
- recognition gap;
- likely drawdown;
- shareholder capture;
- dilution / financing;
- liquidity;
- transaction and tax friction where relevant.

Return velocity is a comparative judgment, not a false-precision annualized forecast.

A larger long-run opportunity can be inferior **now** to a smaller but much nearer high-quality conversion event.

---

## 12A. Profitability transmission gate

A correct operating thesis is not sufficient for capital priority.

Before `INITIATE` or `INCREASE`, Xyool must trace the expected event through the full stock-return transmission path:

```text
CATALYST / OPERATING SUCCESS
-> INCREMENTAL REVENUE / ECONOMICS
-> NORMALIZED EARNINGS / CASH
-> VALUATION DENOMINATOR
-> RECOGNITION / SECTOR REGIME
-> SHAREHOLDER CAPTURE
-> REMAINING PRICE UPSIDE
```

Required state fields:

```text
normalized_earnings_bridge:
  CLEAN / PARTIAL / DISTORTED / UNKNOWN

incremental_economics_state:
  PROVEN / SUPPORTED / PROVISIONAL / UNKNOWN

recognition_vs_fundamentals:
  FUNDAMENTALS_AHEAD / BALANCED / PRICE_AHEAD / UNKNOWN

sector_regime:
  SUPPORTIVE / NEUTRAL / ADVERSE / UNKNOWN

shareholder_capture_state:
  STRONG / ADEQUATE / FRAGILE / BLOCKED / UNKNOWN
```

Rules:
- backlog, bookings, orders, production, deployments or utilization do not automatically imply profitable stock upside;
- one-time tax benefits, fair-value marks, acquisition accounting, unusual credits and nonrecurring items must not be treated as normalized earnings power;
- a catalyst may be fundamentally positive but capital-ineligible when recognition or sector compression has already consumed the remaining opportunity;
- if the normalized earnings/cash bridge is `DISTORTED` or `UNKNOWN`, reduce confidence and fail closed on aggressive sizing;
- if `PRICE_AHEAD` and the next incremental economics do not clear the repricing burden, TTC should prefer `HOLD / REDUCE / NO TRADE` over `INCREASE`.

The question is not only:

> **Will the company execute?**

It is also:

> **If it executes, is enough incremental per-share value still unrecognized to make the stock profitable from here?**

---

## 13. Current holding vs candidate

Before moving capital, compare both sides.

Mandatory table when timeline evidence is material:

| Dimension | Current Holding | Candidate |
|---|---:|---:|
| Quality state | | |
| Opportunity magnitude | | |
| Probability | | |
| Highest material unresolved catalyst | | |
| FES / evidence quality | | |
| Catalyst velocity | | |
| Expected conversion window | | |
| Window position | | |
| Decay status | | |
| Remaining gates | | |
| Catalyst materiality | | |
| Conversion friction | | |
| Recognition gap | | |
| Time to catalyst | | |
| Return velocity | | |
| Shareholder capture | | |
| Downside / impairment | | |
| Confidence | | |
| Remaining opportunity | | |

Candidate-only catalyst analysis is prohibited for a full thesis-to-thesis rotation.

---

## 14. Current-holding preservation / replacement hurdle

An existing holding has already earned capital. Before a full rotation, inventory all unresolved material events in that holding.

A Fresh material event with:

```text
FES3-FES5 or equivalent late causal stage
+ high-quality direct evidence
+ stable / improving velocity
+ Material / Transformational credible economics
+ inside or approaching the expected conversion window
+ incomplete recognition
```

raises the replacement hurdle.

This is not an automatic HOLD rule. It means the candidate must remain materially superior **after the current holding's unresolved catalyst is valued in the comparison**.

For Fresh material FES4/FES5-equivalent events, a full exit before conversion requires an explicit written reason.

When the opportunity differential is close, prefer:

```text
HOLD CURRENT
or
PARTIAL ROTATION
or
ALLOCATE NEW CAPITAL TO CANDIDATE
```

rather than full replacement.

---

## 15. New capital vs earned capital

**New capital** competes aggressively for the best current TTC opportunity.

**Earned capital** already inside a qualified position requires a higher removal hurdle.

Material reduction of earned capital normally requires one or more of:
- quality deterioration;
- confirmation deterioration;
- remaining-opportunity compression;
- catalyst failure / staleness;
- destructive shareholder friction;
- recognition materially outrunning economics;
- a competing opportunity clearing the higher replacement hurdle;
- portfolio survival / liquidity constraints.

High volatility alone may cap additions but does not automatically evict an intact qualified position.

---

## 16. TTC actions

TTC owns these desired economic actions:

```text
WATCH
INITIATE
INCREASE
HOLD
REDUCE
HARVEST
ROTATE
CASH
```

The action must be justified by the complete qualified-opportunity comparison, not by one timeline rung or one price signal.

---

## 17. Harvest

Harvest is not synonymous with "the stock went up."

Ask:
- has the catalyst converted?
- how much recognition gap remains?
- has price outrun economics?
- is the next catalyst weaker or farther away?
- has probability-weighted remaining upside declined?
- has downside increased?
- does another qualified opportunity now offer superior return velocity?

Harvest when the remaining opportunity no longer justifies the capital relative to qualified alternatives.

---

## 17A. Return-failure audit and loss control

A position can become a profitability failure **without** the company thesis becoming false.

Trigger a `RETURN_FAILURE_AUDIT` when one or more occur:

```text
1. price return is materially negative over the expected conversion window;
2. the catalyst or operating thesis is succeeding but recognition keeps compressing;
3. sector regime turns adverse enough to offset company execution;
4. normalized earnings/cash fails to improve as expected;
5. shareholder-capture friction increases;
6. a superior qualified opportunity or cash now has better return velocity;
7. event realization occurs and the remaining opportunity sharply falls.
```

The audit asks:

```text
THESIS INTACT?
NORMALIZED ECONOMICS IMPROVING?
REPRICING BURDEN STILL CLEARABLE?
RECOGNITION GAP STILL OPEN?
SECTOR REGIME SUPPORTIVE ENOUGH?
SHAREHOLDER CAPTURE INTACT?
BETTER USE OF CAPITAL EXISTS?
```

Allowed conclusions:

```text
HOLD — drawdown is recoverable and remaining opportunity is still superior
REDUCE — thesis survives but return velocity / asymmetry deteriorated
HARVEST — event realized or recognition consumed most remaining opportunity
ROTATE — another qualified opportunity or cash is now materially superior
EXIT / CASH — thesis/capture failure or loss severity no longer justified
```

Do **not** use a universal percentage stop. Price decline alone is not thesis failure.

But equally:

> **Do not preserve a losing position indefinitely merely because the operating thesis remains directionally correct.**

TTC owns economic capital priority. If remaining return velocity becomes inferior, capital may rotate even while the company continues to execute.

### Adverse / short event realization

For a short or adverse-catalyst position, event realization automatically opens a harvest review.

```text
ADVERSE EVENT REALIZED
-> recognition shock
-> recompute remaining downside
-> compare squeeze / mean-reversion risk
-> HARVEST / REDUCE / HOLD residual
```

A correct negative catalyst should not be forced into a fixed 30/60/90-day hold when most downside is recognized immediately.

---

## 18. Event-driven update

```text
OLD TTC STATE
      ↓
NEW EVIDENCE
      ↓
QUALITY CHANGED?
CATALYST STAGE CHANGED?
PROBABILITY CHANGED?
MATERIALITY CHANGED?
EXPECTED WINDOW CHANGED?
WINDOW POSITION / DECAY CHANGED?
RECOGNITION CHANGED?
DOWNSIDE / SHAREHOLDER CAPTURE CHANGED?
      ↓
RECALCULATE RETURN VELOCITY
      ↓
COMPARE CURRENT / CANDIDATES / CASH
      ↓
TTC DESIRED ACTION
```

Every material allocation change must record its reason.

---

## 19. Rotation decision record

Every material full or partial rotation records:

```text
Decision Date:
Current Holding:
Candidate:

Current Quality State:
Candidate Quality State:

Current Unresolved Catalysts:
Candidate Unresolved Catalysts:

Current Timeline State:
Candidate Timeline State:

Current Catalyst Materiality:
Candidate Catalyst Materiality:

Current Return-Velocity Case:
Candidate Return-Velocity Case:

Why Replacement Hurdle Is / Is Not Cleared:
Why Full vs Partial Rotation:
What Evidence Would Reverse the Decision:
Next Review Trigger:
```

If the current holding has a plausible material unresolved catalyst and its timeline evidence is missing, a full thesis-to-thesis rotation fails closed until the uncertainty is researched or explicitly incorporated into a higher replacement hurdle.

---

## 20. Position sizing

TTC separates **opportunity priority** from **position size**.

Sizing considers:
- opportunity magnitude;
- probability;
- catalyst proximity;
- catalyst materiality;
- evidence quality;
- confidence;
- permanent-impairment risk;
- liquidity;
- concentration;
- correlation;
- thesis fragility;
- ability to exit.

Key question:

> **If all capital were cash today, how much would this qualified opportunity deserve at today's price relative to the other qualified choices?**

TTC determines desired economic exposure; Quant may only express that exposure subject to its tested downward-only risk rules.

---

## 21. Decision output

When comparing opportunities, output:

### Quality
- Quality state
- strongest quality evidence
- principal disqualifier / risk

### TTC state
- highest material unresolved catalyst
- causal stage / FES
- evidence quality
- expected conversion window
- window position / decay
- remaining gates
- catalyst materiality
- recognition gap
- normalized earnings bridge
- sector regime
- recognition vs fundamentals
- shareholder capture state
- return-failure state
- return velocity

### Ranking
- preferred qualified opportunity
- second-best
- cash / no-trade condition

### Desired action
- initiate / increase / hold / reduce / harvest / rotate
- desired economic allocation range

### Replacement conditions
- what would cause the current holding to lose priority
- what would cause the candidate to overtake it

### Next evidence
- smallest set of events that can materially change the TTC ranking

---

## 22. Anti-lookahead

At every historical decision point, use only information available at that time.

Never use future contracts, earnings, prices, revisions, share counts, corporate actions, or the identity of eventual winners.

The fact that a catalyst later occurred cannot be used as proof that TTC should have predicted it earlier.

---

## 23. Validation

TTC must be tested as a **capital process**, not merely a ranking model.

Point-in-time tests should compare:
- buy and hold;
- equal-weight qualified opportunities;
- momentum baseline;
- quality qualifier without TTC;
- quality qualifier + generic timing;
- full TTC with FES / causal clocks;
- TTC + Quant expression.

Track:
- CAGR;
- maximum drawdown;
- capital growth multiple;
- return / drawdown;
- turnover;
- hit rate;
- average winner / loser;
- time invested / cash;
- opportunity capture;
- permanent impairment frequency;
- rotation regret;
- post-sale 30/60/90-day catalyst capture missed;
- catalyst realization rate by evidence quality;
- conversion lead time;
- stale-signal false-positive rate;
- full vs partial rotation outcomes.

### Freeze-completeness gate

A point-in-time profitability test cannot score dynamic loss control unless the pre-outcome decision record contains, for each active position:

```text
entry rule
promotion trigger
demotion / RF2 audit trigger
RF3 capital-priority failure condition
harvest trigger
invalidation
action mapping
```

If these are not frozen before later prices/evidence are viewed, any hypothetical post-entry exit is diagnostic only and receives **no backtest return credit**.

### Profitability-accounting requirements

Historical validation must report all of the following when a basket contains trade and no-trade decisions:

```text
ACTIVE-SIGNAL RETURN
FULL-BASKET RETURN WITH NO-TRADE SCORED AS CASH
SIMPLE ALL-LONG / RELEVANT BASELINE
HIT RATE
AVERAGE WIN
AVERAGE LOSS
LOSS-SEVERITY / DRAWDOWN
```

Do not drop NO TRADE names from the portfolio denominator merely because no position was opened. Cash is an economic state and must be scored.

Do not count a fundamentally correct thesis as a profitable result when the stock loses money over the decision horizon. Validation must preserve the bridge:

```text
OPERATING / CATALYST SUCCESS
-> NORMALIZED EARNINGS / CASH
-> VALUATION DENOMINATOR
-> RECOGNITION / SECTOR REGIME
-> SHAREHOLDER-CAPTURABLE PRICE RETURN
```

A good operating outcome with a negative stock return is a **profitability miss**, even when the causal company thesis was directionally correct.

For adverse/short catalysts, also record event-realization return versus later fixed-horizon return because correct negative catalysts can mean-revert after the adverse event is recognized.

Primary test:

> **Does TTC improve compounded capital by directing qualified capital toward nearer, larger, more probable and under-recognized economic conversions without increasing permanent impairment or destructive turnover?**

---

## 24. Permanent interpretation

```text
QUALITY QUALIFIER
= SHOULD WE OWN IT AT ALL?

FES / PROCUREMENT / R&D / OTHER CLOCKS
= WHERE IS THE ECONOMIC EVENT IN ITS CAUSAL PATH?

TIME TO CATALYST
= WHICH QUALIFIED OPPORTUNITY DESERVES CAPITAL NOW?

QUANT
= HOW SHOULD TTC-APPROVED EXPOSURE BE EXPRESSED UNDER MEASURED MARKET RISK?
```

This is the canonical Xyool allocation architecture.

## RF3 guardrail — non-price evidence required

Return Failure may use price and benchmark behavior to open an audit, but **price behavior alone cannot create RF3 capital-priority failure**.

Required authority:

```text
PRICE / RELATIVE DIVERGENCE
-> RF2 AUDIT

RF2
+ non-price evidence that remaining opportunity deteriorated
-> RF3 REDUCE / ROTATE
```

Non-price evidence may include:
- guidance deterioration;
- normalized earnings / cash deterioration;
- shareholder-capture deterioration;
- causal-gate failure;
- valuation / repricing burden becoming uncompetitive after an actual information update;
- alternative/cash return-velocity superiority supported by refreshed evidence.

Forbidden:

```text
stock <= -15%
+ benchmark <= -7%
-> automatic RF3
```

A broad-market or sector selloff can satisfy an RF2 stress condition, but cannot by itself prove capital-priority failure.

This guardrail was reinforced by the 2024-07-01 V1B backtest, where BKNG triggered the old price-only RF3 branch during a broad selloff despite strong Q2 operating evidence, and the forced reduction reduced 90-day return without improving portfolio drawdown.
