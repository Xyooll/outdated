# FLOW — TA / Market-Structure Strategy

FLOW ID: `STOCK-TA-STRATEGY-V1`  
STATUS: **ACTIVE / RESEARCH**  
DOMAIN: stock-market  
JOB: use price/volume/volatility structure as a trading strategy after the story/window is known  
PARENT FLOW: `strategy-layer.flow.md`

## GOAL

Use technical/market-structure evidence for the trading job it is actually suited to.

Core law:

> **TA is a strategy family, not the thesis.**

## INPUT

Require:
- story/thesis;
- event/process window if applicable;
- strategy job;
- price/volume history;
- liquidity/volatility state;
- market/sector context.

## STRATEGY FAMILIES

### TREND / MOMENTUM

Questions:
- Is price persistently moving in the thesis direction?
- Is relative strength improving?
- Is the relevant horizon medium enough for trend persistence to matter?
- Has the move already consumed the payoff?

Useful evidence may include:
- multi-horizon returns;
- moving-average state;
- breakouts;
- relative strength;
- residual/sector-relative momentum.

### BREAKOUT / RANGE EXPANSION

Questions:
- Is price exiting a prior information/recognition range?
- Is volume/liquidity consistent with new participation?
- Does the breakout occur near a causal thesis/window or is it detached from evidence?

### PULLBACK / MEAN REVERSION

Questions:
- Is the thesis intact?
- Is the decline a temporary liquidity/recognition dislocation rather than a causal deterioration?
- Has price become stretched relative to recent state?
- Is there evidence of stabilization/reversal?

### EVENT RECOGNITION

Questions:
- Is price beginning to front-run the catalyst?
- Is the event already heavily recognized?
- Does event-day absorption leave room for post-event diffusion?
- Is technical strength confirmation or payoff already consumed?

### VOLATILITY / RISK STRUCTURE

Questions:
- Is volatility expanding into the event?
- Is position risk increasing faster than expected payoff?
- Is ATR/realized volatility suitable for the intended strategy?
- Is liquidity sufficient for entry/exit?

### SUPPORT / RESISTANCE / GEOMETRY

May be recorded as market structure.

Do not grant standalone authority without evidence.

Treat arbitrary chart geometry cautiously.

## JOB MATCH

```text
ENTRY TIMING
→ trend / pullback / breakout structure

RECOGNITION
→ relative strength / event absorption / volume

RISK
→ volatility / liquidity / drawdown structure

RE-ENTRY
→ thesis intact + recognition reset + renewed structure

EXIT / HARVEST
→ payoff consumed + structure deterioration / event closeout
```

## EVIDENCE DISCIPLINE

Historical research supports some price-based effects, but not a universal TA rule.

Therefore:
- use horizon-specific strategies;
- account for costs;
- avoid data-snooped indicator selection;
- prefer simple transparent structures;
- validate by job/regime;
- do not stack correlated indicators as multiple confirmations.

## OUTPUT

```text
TA STRATEGY JOB:
CURRENT STRUCTURE:
RELEVANT HORIZON:
SIGNAL / EVIDENCE:
RECOGNITION STATE:
ENTRY / WAIT CONDITION:
FAILURE / CONTRADICTION:
RISK / VOLATILITY:
HARVEST / EXIT:
CONFIDENCE:
```

## SOFTWARE / HARD-LIMIT BOUNDARY

TA interpretation is Floware.

Exact indicator arithmetic and live market-data retrieval may use deterministic tools when useful.
