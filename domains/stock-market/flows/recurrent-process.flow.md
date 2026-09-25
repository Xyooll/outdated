# FLOW — Stock Recurrent Process Payoff

FLOW ID: `STOCK-RECURRENT-PROCESS-V1`  
STATUS: **ACTIVE / DEVELOPMENT**  
DOMAIN: stock-market  
JOB: capital-path reasoning for recurring operating/economic processes  
PARENT FLOW: `capital-path.flow.md`

## GOAL

Estimate the payoff state when the entry event is a measurement of an economic process that continues after the event.

Examples:
- recurring revenue / ARR;
- marketplace activity;
- utilization;
- orders / backlog conversion;
- subscriber/customer growth;
- operating-margin conversion;
- recurring transaction/volume processes.

Core question:

> **What process continues after this event, and how did the new evidence change its expected rate, duration, quality, and shareholder capture?**

## WHY THIS FLOW EXISTS

Consumed evidence rejected several simple rules:

- strong pre-event TA = continuation;
- strong pre-event TA = exhaustion;
- weak TA = underrecognition;
- broad simultaneous acceleration = convex payoff;
- persistence alone = continuation;
- first negative response = underreaction;
- first positive response = confirmation.

Therefore `RECURRENT_PROCESS` requires a relational economic state, not a single feature.

## INPUT STATE

- event-local payoff state;
- identified recurring economic process;
- prior company guidance / prior process state;
- new results and forward guidance;
- leading indicators;
- shareholder capture;
- pre-event Recognition/repricing burden;
- sector/regime dependencies when causally material;
- next expected remeasurement.

## 1. PROCESS IDENTITY

Name the actual process.

Examples:

```text
subscriber growth → revenue → margin → FCF
orders → backlog → revenue → margin
GMV → monetization → contribution profit
asset/deposit growth → transaction/revenue surfaces → operating leverage
locations → recurring gross profit → EBITDA / FCF
```

Do not use a generic label such as "growth" when the causal process can be stated.

## 2. FORWARD TRAJECTORY

Separate trailing performance from the forward state.

Record evidence for:

```text
RATE
Is the process accelerating, confirming, decelerating, or resetting?

DURATION
How long can the process plausibly continue?

BREADTH
How many economically distinct surfaces improved?

CONVERSION
Is growth converting into margin, cash, backlog, retention, or shareholder value?

FORWARD ANCHOR
Guidance, backlog, orders, contracts, capacity, customer additions, or another observable forward constraint.

DEPENDENCY
What external regime/customer/funding/credit/commodity/market state can interrupt it?
```

Labels are summaries only. Preserve the underlying evidence.

## 3. CONTRADICTION FIRST

Before rewarding a strong event, ask:

> **What part of the new information argues against continuation?**

Examples:
- raised revenue but lower margin;
- customer growth but worsening credit;
- exceptional trailing growth but major forward deceleration;
- record demand but capacity/working-capital bottleneck;
- high transaction growth that depends on an unstable market regime.

A material contradiction is not automatically fatal.

It must remain visible in the payoff distribution.

## 4. RECOGNITION / REPRICING RELATION

Recognition has no universal sign.

Ask:

> **How large is the new forward-state change relative to what the current equity already appears to discount?**

Use:
- pre-event price recognition;
- valuation/repricing burden;
- prior company expectations;
- surprise versus prior guidance;
- company-relative economic magnitude.

Do not assume:
- de-rated = cheap;
- extended = exhausted;
- breakout = confirmation;
- weak price = opportunity.

## 5. FIRST RESPONSE

First tradable response remains:

`DESCRIPTIVE / CONDITIONAL ONLY`

The consumed C2-RESPONSE-V1 challenger failed to beat B2.

Retain:
- abnormal response;
- volume;
- evidence/response disagreement;
- possible contradiction clue.

Do not give response independent rank authority.

If a future challenger uses first response prospectively, its forecast origin must move until after the response is observable.

## 6. RECURRENT-PROCESS STATE

Produce a structured state rather than a master score.

Minimum output:

```text
PROCESS:
FORWARD RATE:
FORWARD DURATION:
FORWARD ANCHOR:
CONVERSION / CAPTURE:
MATERIAL CONTRADICTIONS:
DEPENDENCIES / REGIME:
RECOGNITION / REPRICING BURDEN:
NEXT REMEASUREMENT:
UNCERTAINTY:
```

Optional synthesis labels:

```text
ACCELERATING
CONFIRMING
DECELERATING
RESETTING
CONTRADICTED
REGIME_DEPENDENT
UNKNOWN
```

Multiple labels may coexist.

## 7. ORDERING RULE

Compare two recurrent-process opportunities by asking, in order:

1. Which has the stronger **forward** economic change, not trailing headline?
2. Which has the more durable/observable continuation mechanism?
3. Which converts more of that continuation into shareholder-capturable economics?
4. Which carries fewer material contradictions?
5. Which requires less additional repricing relative to the new economics?
6. Which has lower path fragility inside the capital horizon?

If evidence does not discriminate, abstain.

Do not create a universal weighted score.

## 8. KNOWN REGRESSIONS

Any future recurrent-process method must preserve these lessons:

- HOOD — broad platform acceleration was materially under-ranked.
- IOT — positive recurring evidence did not prevent a material loss.
- AFRM — large payoff from a de-rated state; breadth alone did not explain it.
- SE — broad multi-business acceleration was not sufficient.
- DASH — strong payoff despite being a breadth negative control.
- NU — contradictions mattered despite broad growth.
- HIMS — strong operating evidence overcame weak pre-event structure.
- ELF — forward reset dominated exceptional trailing results.
- CAVA — extreme recognition did not guarantee exhaustion.
- DUOL — strong operating evidence plus high recognition still produced a 60D decline.

## 9. MAGNITUDE

Do not assign narrow numeric ranges yet.

Current consumed range calibration is inadequate.

Until a magnitude method earns coverage:

```text
DIRECTIONAL PAYOFF STATE
+ RELATIVE MAGNITUDE CLASS
+ DOWNSIDE CLASS
+ UNCERTAINTY WIDTH
```

are preferred to false precision.

## SOFTWARE / HARD-LIMIT BOUNDARY

`NONE — FLOWARE SUFFICIENT`