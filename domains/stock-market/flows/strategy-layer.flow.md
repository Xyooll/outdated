# FLOW — Stock Strategy Layer

FLOW ID: `STOCK-STRATEGY-LAYER-V1`  
STATUS: **ACTIVE / DEVELOPMENT**  
DOMAIN: stock-market  
JOB: select how to trade an already-understood opportunity
AUTHORITY: strategy-family selection and conditional expression design only; no production order placement, position-sizing override, hard-risk override, or transaction authority
PARENT GOALPOST: supplied by STOCK-COMPANY-ANALYSIS or calling stock pipeline
UPSTREAM FLOWS: company-analysis, narrative-thesis, story-writer, recognition/payoff/capital-path state
DOWNSTREAM FLOWS: TA/Quant/event strategy families, authorized risk/execution layer, meta audit
INBOUND PIPES: `../PLUMBING.md#pipe-stock-story-strategy`
OUTBOUND PIPES: `../PLUMBING.md#pipe-stock-strategy-expression`
SOFTWARE DEPENDENCIES: live market data / exact risk / execution only where justified downstream

## GOAL

Once Xyool has discovered the stock, qualified it, reconstructed the story, formed a thesis, and estimated the relevant window, choose the strategy best suited to the current state.

Core law:

> **The thesis tells us what we think is happening. The Strategy Layer decides how, when, or whether to express it.**

## POSITION IN THE STOCK FLOW

```text
DISCOVERY
→ QUALITY CREDENTIALS
→ CURRENT STATE / CONNECTION MAP
→ STORY
→ THESIS
→ RHYTHM / WINDOW
→ STRATEGY LAYER
     ├─ TA / MARKET-STRUCTURE STRATEGY
     ├─ QUANT STRATEGY
     ├─ EVENT / CATALYST STRATEGY
     ├─ MEAN-REVERSION / DISLOCATION STRATEGY
     ├─ TREND / MOMENTUM STRATEGY
     ├─ RELATIVE / ROTATION STRATEGY
     ├─ THESIS-HOLD / WAIT STRATEGY
     └─ NO-TRADE / WAIT
→ EXECUTION / RISK EXPRESSION
```

A strategy may combine compatible families when each has a distinct job.

## INPUT STATE

Before strategy selection require:

```text
QUALITY / ELIGIBILITY:
THE STORY:
THESIS:
LIKELY NEXT STATE:
CONDITIONAL WINDOW:
PRIMARY INVALIDATION:
CAPITAL-PATH REGIME:
RECOGNITION STATE:
LIQUIDITY / VOLATILITY:
MARKET / SECTOR REGIME:
CURRENT PRICE STRUCTURE:
```

A strategy cannot repair an unknown thesis.

## 1. STRATEGY IS JOB-SPECIFIC

Ask:

> **What trading job needs to be solved?**

Possible jobs:

```text
EARLY ENTRY
WINDOW ENTRY
CONFIRMATION
BREAKOUT PARTICIPATION
PULLBACK ENTRY
CATALYST RISK
POST-EVENT CONTINUATION
HARVEST
RISK REDUCTION
RE-ENTRY
ROTATION
HEDGE
WAIT
```

Then select the strategy family with evidence for that job.

## 2. STRATEGY FAMILIES

### A. TA / MARKET STRUCTURE

Uses price, volume, volatility and relative structure as evidence.

Potential jobs:
- timing;
- recognition;
- confirmation/contradiction;
- entry/exit structure;
- breakout/pullback handling.

TA does not create the fundamental story.

### B. QUANT

Uses tested statistical/model relationships.

Potential jobs:
- momentum/trend;
- mean reversion;
- regime;
- risk scaling;
- relative strength;
- factor/residual state;
- liquidity/execution;
- portfolio construction.

Quant models retain independent validation requirements.

### C. EVENT / CATALYST

Uses the causal event clock.

Potential jobs:
- exact-date event risk;
- inferred-window accumulation;
- procurement/funded-order windows;
- post-event diffusion;
- catalyst closeout.

### D. TREND / MOMENTUM

Uses persistent directional/relative movement where the relevant horizon supports it.

### E. MEAN REVERSION / DISLOCATION

Uses temporary overshoot/liquidity/recognition dislocations where the thesis remains intact.

### F. RELATIVE / ROTATION

Compares the opportunity against alternatives rather than evaluating it in isolation.

### G. THESIS HOLD / WAIT

Sometimes the correct strategy is to wait for:
- a better price;
- stronger causal evidence;
- the start of the event window;
- a Quality unlock;
- reduced uncertainty.

### H. NO TRADE

A valid strategy when expected advantage is insufficient or the path is not executable.

## 3. STRATEGY MATCHING

Do not ask:

> "Which strategy is best?"

Ask:

> **Which strategy fits this story, state, horizon, and job?**

Examples:

```text
KNOWN CATALYST WINDOW + UNDERRECOGNIZED THESIS
→ event-window strategy
→ TA for entry/recognition

STRONG FORWARD ECONOMIC RESET + POST-EARNINGS UNDERREACTION
→ post-event continuation / drift candidate

INTACT THESIS + SHORT-TERM LIQUIDITY SHOCK
→ mean-reversion / dislocation candidate

NO NEAR CATALYST + PERSISTENT RELATIVE STRENGTH
→ momentum / trend candidate

BINARY EVENT + LARGE GAP RISK
→ event-risk sizing; ordinary stop is insufficient
```

## 4. STRATEGY CARD

Every selected strategy should state:

```text
STRATEGY:
JOB:
WHY IT FITS THIS STORY:
ENTRY CONDITION:
WINDOW:
CONFIRMATION:
INVALIDATION:
RISK MECHANISM:
HARVEST / EXIT:
RE-ENTRY CONDITION:
WHAT WOULD MAKE ANOTHER STRATEGY BETTER:
EVIDENCE STATUS:
```

## 5. MULTI-STRATEGY COMPOSITION

Flows may compose strategies if jobs are distinct.

Example:

```text
CATALYST STORY
→ correspondence rhythm defines window
→ momentum/TA confirms recognition
→ volatility model caps risk
→ event strategy controls binary exposure
```

Do not count correlated strategies as independent confirmation.

## 6. STRATEGY EVIDENCE

A strategy earns use by job, horizon and regime.

Evidence does not need to prove universal profitability.

It needs to answer:

> **Does this strategy improve the specific job compared with a simpler baseline under realistic costs and constraints?**

## 7. MISS AUDIT

A strategy miss occurs when Xyool:
- chooses a strategy before understanding the story;
- uses the wrong horizon;
- uses mean reversion during genuine thesis deterioration;
- uses momentum after the event payoff is already exhausted;
- treats TA as fundamental evidence;
- treats several correlated indicators as independent votes;
- ignores event gap risk;
- ignores liquidity/transaction cost;
- fails to switch strategy when the state/window changes.

## 8. OUTPUT

The user-facing result should be simple:

```text
STORY / THESIS:
WINDOW:
STRATEGY:
WHY THIS STRATEGY:
ENTRY / WAIT CONDITION:
INVALIDATION:
HARVEST / EXIT:
ALTERNATE STRATEGY IF STATE CHANGES:
```

## SOFTWARE / HARD-LIMIT BOUNDARY

Strategy reasoning is Floware.

Exact calculations, live market data, order execution, hard risk limits, and deterministic portfolio constraints may remain software/tool responsibilities where justified.
