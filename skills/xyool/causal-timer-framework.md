# Xyool — Causal Timer Framework

Status: **PROVISIONAL TIMER TAXONOMY / TTC INPUT — NO INDEPENDENT CAPITAL AUTHORITY**

## Core purpose

Xyool should not treat all catalysts as one generic time-to-event clock.

For every material catalyst ask:

> **What clock is actually running, what event started it, what event stops it, and what evidence tells us how that clock normally behaves?**

A company may have several clocks running in sequence or in parallel.

The job of the framework is to identify the correct clock, calibrate it from the most specific evidence available, and feed the result into TTC.

## Core principle

Do not measure unlike stages against one another.

```text
SIGNAL
→ FUNDING
→ INTEGRATION
→ ACCEPTANCE / QUALIFICATION
→ PROCUREMENT
→ DEPLOYMENT
→ REVENUE / CASH
→ REPEAT / ROLLOUT
```

Each arrow can carry a different timer.

A single coarse “time to catalyst” estimate can hide the actual bottleneck.

## Timer types

### 1. Signal-to-Funding Timer

Start: credible need / requirement / program signal.
Stop: funded authorization, budget, contract, or binding commitment.

Question:
> How long does a visible requirement normally take to become funded?

### 2. Integration-to-Acceptance Timer

Start: product is physically or operationally integrated into the customer platform/process.
Stop: SAT, UAT, qualification, customer acceptance, or equivalent operational sign-off.

Question:
> Once the product is working in the customer environment, how long until formal acceptance?

### 3. Acceptance-to-Procurement Timer

Start: successful acceptance / qualification.
Stop: first material funded production or procurement order.

Question:
> After the customer accepts the technology, how long until it buys at production scale?

### 4. Procurement-to-Deployment Timer

Start: funded order / award.
Stop: delivery, installation, fielding, commissioning, or operational deployment.

Question:
> How long does an awarded order take to become deployed economic reality?

### 5. Deployment-to-Revenue / Cash Timer

Start: delivery / deployment / accepted backlog.
Stop: recognized revenue, cash collection, or free-cash-flow conversion.

Question:
> How long does operational conversion take to reach the financial statements and cash account?

### 6. Rollout Probability Timer (RPT)

Start: repeatable deployment/order evidence establishes a plausible recurring unit.
Stop/reset: next comparable repeat event, broken cadence, exhausted rollout, or invalidation.

Question:
> Where are we in the evidence-backed window for the next repeat unit, and is near-term conditional probability rising or falling?

### 7. Reference-Customer Cascade Timer

Start: influential / anchor customer adopts or accepts.
Stop: first credible peer-customer adoption or evidence the cascade thesis failed.

Question:
> After an influential customer adopts, how long until adjacent customers copy or reuse the qualification path?

Do not treat management claims that others may follow as actual cascade evidence.

### 8. Replenishment Timer

Start: installed-base use, inventory depletion, fleet consumption, wear, or field utilization.
Stop: reorder, spares purchase, repair cycle, or inventory replenishment.

Question:
> Once the installed base starts consuming inventory or service life, how long until replenishment demand appears?

### 9. Capacity-Build Timer

Start: funded capex / facility expansion / mine or manufacturing build.
Stop: commissioned incremental capacity capable of fulfilling customer demand.

Question:
> How long until promised supply capacity becomes usable economic output?

### 10. Backlog-Conversion Timer

Start: funded backlog / booked order.
Stop: revenue and margin recognition.

Question:
> What portion of backlog is expected to convert, and over what period?

Keep backlog separate from revenue and revenue separate from cash.

### 11. Regulatory / Administrative Timer

Start: formal submission, completed trial package, permit application, reimbursement filing, or government approval request.
Stop: regulatory/administrative decision.

Question:
> How long does this specific authority/process normally take from complete submission to decision?

### 12. Institutionalization Timer

Start: training use, dedicated training equipment, curriculum insertion, doctrine, standard workflow, or specification activity.
Stop: standardization, standard issue, mandated use, or broad organizational requirement.

Question:
> How long does repeated use become institutionalized adoption?

### 13. Financing / Runway Timer

Start: current liquidity and burn state.
Stop: point at which external financing, refinancing, dilution, covenant relief, or restructuring becomes necessary.

Question:
> How much time remains before capital structure becomes the dominant catalyst/risk?

This belongs primarily to Quality / shareholder-capture analysis, not positive TTC promotion.

### 14. Catalyst Decay / Overdue Timer

Start: entry into an evidence-backed expected event window.
Stop: event occurs, documented reset occurs, or absence becomes meaningful negative evidence.

Question:
> At what point does “not yet” become evidence that the thesis/timing is wrong?

### 15. Management Timing Credibility Timer

Start: management makes a date/window claim.
Stop: claimed event occurs or the window expires.

Question:
> How accurate has management historically been when it says this type of event is near?

This is an evidence-weighting overlay, not a substitute for causal evidence.

### 16. Recognition Timer

Start: economic evidence becomes public or materially stronger.
Stop: market recognition plausibly catches up with the economic change or recognition materially outruns economics.

Question:
> How quickly is the market incorporating the economic state change, and how much recognition gap remains?

Recognition is a TTC input; this timer must not become a pure price-momentum rule.

### 17. Existing-Customer Scope Expansion Timer

Start: an existing paying customer begins testing, selecting, quoting, piloting, or otherwise actively evaluating an adjacent product, service, geography, site class, or project scope beyond the already-awarded relationship.
Stop: a funded adjacent-scope order / award, explicit abandonment, loss to a competitor, or evidence the expansion path has gone stale.

Question:
> Once an established customer begins actively evaluating an adjacent scope, how long until that relationship expands into a funded order?

This timer is different from the Rollout Probability Timer. RPT measures repetition of a **comparable repeat unit**. Scope Expansion measures a customer broadening the relationship into a **different but adjacent economic scope**.

Nameless example:

```text
EXISTING CUSTOMER
→ already buys maintenance + exterior product
→ begins testing / final selection for interior product
→ management says opportunity is progressing but no order exists yet
→ start Scope Expansion Timer
→ funded interior award closes the timer
```

Do not start this timer from generic statements such as “we see cross-sell opportunity.” Require customer-specific or program-specific pre-order evidence such as testing, product selection, formal quoting, pilot activity, an RFP/tender, or management disclosure that a defined adjacent project is progressing.

## Timer stack

A single opportunity can carry multiple sequential clocks.

Nameless example:

```text
INITIAL EVALUATION ORDER
        ↓  Integration-to-Acceptance Timer
ACTIVE CUSTOMER TESTING / SAT
        ↓  Acceptance-to-Procurement Timer
FIRST PRODUCTION ORDER
        ↓  Procurement-to-Deployment Timer
FIELDING
        ↓  Deployment-to-Revenue/Cash Timer
REPEAT SITE / UNIT
        ↓  Rollout Probability Timer
NEXT SITE / UNIT
```

The active TTC bottleneck is usually the next unresolved material gate, not every timer at once.

## Payoff Persistence / Activated Economic Stream

**Status: PROVISIONAL POST-TIMER ECONOMIC-STATE INPUT — NOT A NEW TIMER AND NO INDEPENDENT CAPITAL AUTHORITY.**

When a timer realizes, Xyool must not only ask what event happened. It must ask what economic state now exists after the event.

Mandatory question:

> **If this catalyst realizes, does the economic payoff end with the event, or does it activate an ongoing revenue/cash stream? If ongoing, what is the run-rate, duration, margin/cash conversion, concentration/termination risk, and how much of that stream is already recognized?**

This is **payoff persistence**. It is distinct from timer proximity and distinct from market-price persistence.

Use qualitative payoff states:

1. **ONE-OFF REALIZATION** — economics substantially end with the event.
2. **REPEATABLE DISCRETE** — the event can repeat, but each additional unit requires another order/event.
3. **RUN-RATE ACTIVATION** — realization starts an ongoing contracted or recurring revenue/cash stream.
4. **STACKED / OVERLAPPING RUN-RATE** — multiple activated streams operate concurrently and can create sequential company-level growth.
5. **DECAYING / TERMINABLE RUN-RATE** — an ongoing stream exists but meaningful termination, concentration, renewal, utilization, margin or financing risk can impair persistence.

Record where relevant:

```text
Payoff Persistence:
Activated Run-Rate / Economic Stream:
Contracted / Expected Duration:
Economic Start Date:
Margin / Cash Conversion:
Termination / Concentration Risk:
Renewal / Replenishment Path:
Already Recognized:
Next Timer:
```

### Catalyst closeout / handoff

When a material timer realizes:
1. close the old timer — do not keep awarding an “imminent” timing bonus;
2. determine the payoff-persistence state;
3. if an ongoing stream was activated, record it as an **Activated Economic Stream**;
4. update remaining opportunity, catalyst magnitude, recognition, Quality/shareholder capture and return velocity;
5. identify and start the next unresolved timer where evidence supports one.

### Anti-double-counting

A signed contract and its later activation are not two copies of the same economics.

- Contract signing can establish committed future economics.
- Activation can reduce execution uncertainty and begin actual revenue/cash conversion.
- Do not add the full contract value again at activation.
- Revenue already recognized must not be counted again as new backlog or new contract economics.
- A guidance increase caused by the same underlying contract should not be counted as a separate independent economic stream.

### Stack-to-Growth

For recurring/service businesses, multiple activations can create a distinct company-level state:

```text
CONTRACTED STACK
→ DEPLOYMENT
→ ACTIVATED RUN-RATE
→ OVERLAPPING ACTIVATED RUN-RATES
→ STACK-TO-GROWTH
→ if operating cash increasingly funds the next layer: COMPOUNDING STACK
```

The economic state can become more powerful as streams overlap, but it remains subject to Quality, financing, shareholder capture, customer concentration, margin/cash conversion and recognition.

### Economic Persistence ≠ Price-Recognition Persistence

Do not infer persistent stock-price appreciation from persistent economics.

**Economic Persistence** asks whether the realized event creates ongoing company economics.

**Price-Recognition Persistence** asks whether the market continues repricing those economics after the event. That depends separately on surprise, prior recognition, valuation, Quality, financing/shareholder friction, materiality and subsequent confirming or contradicting evidence.

A run-rate activation can therefore be economically important while producing weak or negative near-term price action if the economics were already recognized or other risks dominate.

## Parallel timers

Companies can also have independent clocks running in parallel.

Example:
- Product A in customer acceptance;
- Product B waiting for procurement;
- installed base creating replenishment demand;
- international reference customer creating peer-cascade potential;
- an established customer testing a new adjacent scope.

Do not collapse independent clocks into one average catalyst date.

## Calibration hierarchy

Use the most specific evidence available:
1. same company + same customer/program + same stage transition;
2. same company + same mechanism;
3. same customer/agency + same mechanism;
4. same company historical analog;
5. close industry analog;
6. broad sector benchmark only if better evidence is unavailable.

## Event-type integrity

Compare like events with like events.

Do not treat:
- order date as completion date;
- shipment start as acceptance;
- qualification as procurement;
- contract ceiling as funded order;
- backlog as revenue;
- revenue as cash;
- first deployment as broad rollout;
- adjacent-scope cross-sell as a same-unit rollout cadence.

## Window behavior

Each timer should record:

```text
Timer Type:
Start Event:
Start Date:
Stop Event:
Observed Historical Interval(s):
Expected Window:
Current Window Position:
Confidence:
Evidence Grade:
Known Constraints:
Last Confirming Evidence:
Promotion Trigger:
Reset Trigger:
Invalidation:
```

Do not automatically assume probability rises forever with time.

For many timers, support should rise as an evidence-backed window approaches, then decay if the expected event fails to occur.

## Authority boundary

Timers and payoff-persistence state can inform:
- FES stage and velocity;
- catalyst probability;
- distance-to-conversion;
- catalyst magnitude;
- remaining opportunity;
- return velocity;
- catalyst closeout/reset;
- recognition interpretation;
- research priority;
- TTC ranking.

They do not independently:
- create Quality;
- create funded economics;
- count unawarded orders as backlog;
- predict a technical breakout;
- imply persistent stock-price appreciation;
- justify a numeric TTC multiplier;
- force a trade;
- override shareholder-capture failure;
- set Quant risk expression.

## Validation status

The timer taxonomy is **provisional**.

The general principle — identify the actual causal start/stop events rather than one vague catalyst date — is strongly consistent with current TTC architecture.

The Existing-Customer Scope Expansion Timer was added after a live OESX review showed that a customer-specific adjacent project had been publicly described as in testing/final selection and progressing before the eventual expansion announcement. The timer concept remains provisional pending broader cross-company validation.

The Payoff Persistence / Activated Economic Stream distinction received diagnostic/conceptual support on 2026-09-15. The simple hypothesis that recurring/run-rate activation automatically produces more persistent stock-price appreciation was rejected. Economic persistence should therefore remain a qualitative post-timer TTC input, separate from recognition, with no numeric multiplier until broader untouched validation.

Individual timer calibrations, numeric hazard curves, payoff-persistence multipliers, and universal windows are not promoted.

Future testing should ask which timer types and post-timer economic states improve point-in-time timing calibration and capital decisions without creating hindsight fit or excessive false positives.
