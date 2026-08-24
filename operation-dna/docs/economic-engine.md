# Economic Engine

The economic engine is domain-neutral. Business, investment, and trading research all produce the same candidate structure and pass through the same evidence, risk, experiment, and capital-allocation layers.

```text
Feeds / APIs
    ↓
Normalized events
    ↓
Domain scanners
 ┌──┼──────────┐
Business  Investment  Trading
 └──┼──────────┘
    ↓
Evidence validation
    ↓
Opportunity ranking
    ↓
Smallest viable experiment / backtest
    ↓
Outcome measurement
    ↓
Scale / iterate / reject
```

## Current implementation

- `software/economics/scanners.py` — unified domain scanners
- `software/economics/opportunities.py` — opportunity scoring and decisions
- `software/economics/experiments.py` — experiment planning and outcomes
- `software/economics/backtest.py` — deterministic backtesting primitives
- `software/economics/capital.py` — capital allocation primitives
- `software/research/validation.py` — evidence gate
- `software/runtime/permissions.py` — capability boundaries

## Safety boundary

Scanners create candidates. Backtests evaluate historical data. Experiments are disabled by default. Nothing in this layer places a live trade, spends funds, or deploys infrastructure.

Live execution requires a separate authorized adapter and must pass the central safety/permission system.
