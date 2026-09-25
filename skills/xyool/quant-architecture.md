# Xyool — Quant Layer Architecture

## Floware Strategy-Layer role

Within the current Floware stock architecture, Quant is best understood as a **strategy family / strategy-support family** that may be invoked after the story, thesis, and trading job are known.

This does **not** remove Quant's independent validation requirement.

The two ideas coexist:

```text
RESEARCH / VALIDATION
Quant models earn utility independently.

LIVE FLOWARE
Strategy Layer may invoke validated Quant models for:
timing / risk / sizing / regime / rotation / execution / selection.
```

Quant does not create the fundamental story or override Quality.

Canonical Strategy Layer:
`domains/stock-market/flows/strategy-layer.flow.md`

---

## Status

The Quant Layer is an **independent parallel analytical system**.

It is not part of Company-Level Xyool, OSE, the Quality Qualifier, or Time to Catalyst (TTC) during independent model testing.

```text
FUNDAMENTAL SYSTEM                        QUANT SYSTEM

Company Xyool                             Market/Fundamental Data
      ↓                                             ↓
OSE                                       Canonical Quant Models
      ↓                                             ↓
Quality Qualifier                         Standardized Signals
      ↓                                             ↓
Time to Catalyst                          Quant Tournament
                                                    ↓
                                              Utility Cards
```

Only models that earn **USE** or **CORE** status may enter later integration experiments.

---

## Documents

### Conceptual foundation

`skills/xyool/quant-layer.md`

Defines:
- independence from Xyool/OSE/TTC;
- standard signal object;
- signal normalization;
- regime testing;
- independence testing;
- utility-card concept;
- initial integration hypotheses.

### Authoritative model registry

`skills/xyool/quant-model-catalog.md`

Defines the expanded canonical universe across:
- alpha/security selection;
- statistical/relative value;
- volatility/regime;
- risk/portfolio construction.

### Tournament specification

`skills/xyool/quant-tournament.md`

Defines:
- job-specific leagues;
- feasibility gates;
- canonical baseline testing;
- robustness;
- out-of-sample testing;
- regime survival;
- cost/liquidity stress;
- independence/redundancy;
- utility testing;
- promotion/downgrade rules;
- final fundamental-system challenge.

---

## Runtime

`agent/quant/catalog.py`

Machine-readable canonical model registry.

`agent/quant/tournament.py`

Machine-readable tournament state engine.

`tests/test_quant_tournament.py`

Tests registry integrity, data-state gates, rejection, promotion to USE/CORE, job scoreboards, and family grouping.

---

## Tournament status flow

```text
NOT_STARTED
    ↓
DATA CHECK
    ├── insufficient → HOLD_FOR_DATA
    └── D3 ready → RESEARCH
                    ↓
              TOURNAMENT EVIDENCE
                    ↓
        ┌───────────┼───────────┐
        ↓           ↓           ↓
      REJECT       USE         CORE
```

CORE is intentionally rare.

---

## Data readiness

```text
D0 — unavailable
D1 — current/live only
D2 — historical but incomplete
D3 — point-in-time backtest ready
```

Only D3 datasets can produce a final Tournament 1 result for a given model/universe.

---

## Implementation waves

```text
WAVE 1 — PRICE / RISK FOUNDATION
WAVE 2 — FUNDAMENTAL FACTORS
WAVE 3 — EVENT / OWNERSHIP
WAVE 4 — STATISTICAL / REGIME
WAVE 5 — PORTFOLIO CONSTRUCTION
```

Implementation wave is not expected-performance rank.

---

## Machine learning rule

Machine learning is deferred until the canonical transparent model set establishes a baseline.

Later ML must answer one of four concrete questions:

1. Does it combine independent signals better?
2. Does it capture nonlinear interactions that survive out of sample?
3. Does it improve regime-conditioned weighting?
4. Does it improve probability calibration?

ML must compete against the canonical baseline after costs. Complexity is not itself an advantage.

---

## TTC integration boundary

The Quant Layer may support:
- discovery;
- recognition / ignition corroboration;
- risk control;
- concentration control;
- sizing expression;
- execution;
- regime detection.

But TTC remains the capital-priority layer for qualified opportunities.

Conceptually:

```text
QUALITY QUALIFIER
      ↓
TTC DESIRED EXPOSURE
      ↓
QUANT RISK / CONCENTRATION / EXECUTION MODIFIER
      ↓
EXECUTABLE POSITION
```

Quant cannot increase a name above TTC desired exposure or create a fundamental thesis.

Legacy internal implementation field names may remain temporarily for backward compatibility, but new conceptual documentation and interfaces should use TTC terminology.

---

## Final objective

The Quant Layer is useful only if it improves one or more of:
- discovery;
- selection;
- timing;
- confirmation;
- risk control;
- sizing;
- rotation;
- execution;
- regime detection;
- portfolio construction;

and ultimately improves:

> **CAPITAL COMPOUNDING THROUGH OPPORTUNITY ROTATION**