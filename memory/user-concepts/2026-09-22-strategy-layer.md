# User Concept — Trading Strategy as Its Own Layer

Date: **2026-09-22**  
Status: **ACTIVE / CORE STOCK ARCHITECTURE**

## USER-STATED WORDING

> "This may be TA, but in reality, in my reality, this is really strategy, trading strategy."

> "first we discover the stock, then we see where it's at, and then we form a strategy"

> "TA is just one of the strategies that may be effective, so would the quant thing that we came up with."

## CONCEPT

Trading strategy is a distinct downstream layer.

TA is not the strategy layer itself.

TA and Quant are strategy families that may or may not fit a specific stock state, thesis, horizon, or trading job.

## ASSISTANT INTERPRETATION

The stock architecture becomes:

```text
DISCOVERY
→ QUALITY
→ CURRENT STATE
→ STORY / THESIS
→ WINDOW
→ STRATEGY SELECTION
→ EXECUTION
```

The Strategy Layer chooses among approaches such as:
- TA / market structure;
- Quant;
- event/catalyst;
- momentum/trend;
- mean reversion;
- relative/rotation;
- wait/no-trade.

## SYSTEM CONSEQUENCE

Created:
- `domains/stock-market/flows/strategy-layer.flow.md`
- `domains/stock-market/flows/ta-strategy.flow.md`

Quant remains independently validated, but conceptually becomes one strategy family that the Strategy Layer may invoke.

## RELATED CONCEPTS

- Detective Story
- Quality Credentials
- Correspondence Rhythm
- Narrative Thesis
- Quant
- TA
