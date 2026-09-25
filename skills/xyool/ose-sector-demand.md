# Xyool OSE — Sector Demand Extension

Status: **MANDATORY OSE CONTEXT / NOT AN INDEPENDENT CAPITAL-ACTION RULE**

This file is a mandatory extension of `opportunity-state-engine.md` and `ose-dual-confirmation.md`.

## Purpose

Sector Demand answers a different question from the company-level Xyool Demand Ladder.

Company-level Xyool asks:

> **What end demand is causal to this company, and can this company capture it?**

OSE Sector Demand asks:

> **What is happening to demand across the relevant sector/end-market, how broad and durable is it, and is the company's opportunity being carried by a strengthening or weakening external demand regime?**

Sector Demand belongs in OSE because it is a dynamic cross-company opportunity-state variable. It is upstream of CAC and separate from Quant/technical price signals.

## Authority boundary

```text
COMPANY XYOOL
company-specific demand / control / capture
        ↓
OSE
Sector Demand context + SC + CC + RL + Potential + Friction
        ↓
CAC
judgment / desired economic exposure
        ↓
QUANT
risk / sizing / execution expression
```

Sector Demand may inform OSE state and CAC judgment. It does **not** independently create a position, set a portfolio weight, override CAC, or authorize Quant to add exposure.

Until fresh point-in-time validation establishes an incremental capital rule, Sector Demand must remain an evidence/state variable rather than an automatic sizing formula.

## Sector Demand State — SD0-SD5

- **SD0 — Contracting / absent:** relevant end-market demand is shrinking, unfunded, or materially impaired.
- **SD1 — Stable / base:** demand exists but breadth and growth are limited or ordinary.
- **SD2 — Broadening:** more customers, applications, geographies, programs, or budgets are participating.
- **SD3 — Accelerating:** sector orders, bookings, utilization, deployments, or spending are accelerating across independent participants.
- **SD4 — Strategic / funded:** demand is supported by durable customer budgets, contractual commitments, strategic programs, regulation, infrastructure buildout, or government appropriations.
- **SD5 — Structural / demand shock:** unusually broad, durable, capacity-absorbing demand is changing sector economics or creating persistent bottlenecks.

Sector Demand level and velocity must be tracked separately.

### Sector Demand Velocity

- accelerating ↑↑
- improving ↑
- stable →
- weakening ↓
- collapsing ↓↓

## What counts as Sector Demand evidence

Prefer independent, causal evidence such as:

1. end-customer budgets, capex, procurement plans, or appropriations;
2. orders/bookings/backlog across multiple independent companies;
3. utilization, lead times, capacity commitments, qualification queues, or delivery constraints;
4. shipment/deployment/throughput data across the value chain;
5. funded infrastructure, defense, industrial, energy, healthcare, technology, or other program demand;
6. repeated customer and competitor commentary consistent with observed activity;
7. inventory behavior when it clearly distinguishes real consumption from channel loading;
8. industry data with transparent methodology.

Narrative TAM, social attention, analyst enthusiasm, sector ETF performance, stock-price momentum, or multiple companies repeating the same unsupported claim are not sufficient Sector Demand evidence.

## Causal mapping requirement

Sector Demand only matters when it maps into the company's actual economic chain:

```text
SECTOR / END-MARKET DEMAND
        ↓
SPECIFIC CUSTOMER NEED
        ↓
DEMAND CASCADE
        ↓
BOTTLENECK / CONTROL POINT
        ↓
COMPANY CAPTURE
        ↓
ORDERS / BACKLOG / DEPLOYMENT
        ↓
REVENUE / MARGIN / CASH / PER-SHARE VALUE
```

A strong sector with weak company control does not create a strong company opportunity.

A weak sector can still contain a strong company opportunity if the company is gaining share, controls a tightening bottleneck, has locked-in runway, or serves a structurally stronger subsegment.

## Relationship to Structural Confirmation

Sector Demand is an input to Structural Confirmation, not a substitute for it.

Strong Sector Demand can strengthen SC when:

- the evidence is independent of the company's own claims;
- it is directly relevant to the company's served end-market;
- bottleneck/control evidence also exists;
- the company has credible capture exposure.

Sector Demand alone cannot promote SC to a high state if control/capture remains weak or unproven.

Avoid double counting. The same order, backlog item, or customer statement cannot simultaneously count as multiple independent confirmations merely because it appears in company and sector analysis.

## Relationship to Conversion Confirmation

Sector Demand does **not** promote Conversion Confirmation by itself.

CC still requires company-specific conversion evidence:

**ORDERS → BOOKINGS → BACKLOG → DEPLOYMENT → REVENUE → MARGIN → EBITDA → OCF → FCF → PER-SHARE VALUE**

A sector boom with weak company conversion can still be a shareholder trap.

## Relationship to Potential

Sector Demand may change Potential when it changes the plausible future economic destination.

Potential can rise when sector evidence shows:

- larger funded demand;
- broader customer participation;
- longer demand duration;
- faster capacity absorption;
- new use cases moving from narrative to funded deployment;
- a bottleneck becoming more valuable because sector demand exceeds supply response.

Potential should not rise merely because sector securities reprice upward.

## Relationship to Runway Lock-In

Sector Demand and Runway Lock-In are distinct.

- Sector Demand asks how strong the external demand regime is now and where it is heading.
- RL asks how much future company economics are already protected if external demand stops accelerating.

High RL can buffer an OSE downgrade when Sector Demand cools. It does not immunize the company from cancellation, financing, execution, or shareholder-capture failure.

## Relationship to Recognition / Quant

Sector price performance is recognition/market behavior, not Sector Demand.

Price, volume, trend, volatility, correlation, and other market-derived signals remain in Recognition/Quant. They may corroborate that the market is noticing a sector change, but they cannot establish economic Sector Demand.

## OSE state update

Every material sector-demand event should update:

```text
OLD SECTOR DEMAND STATE
        ↓
NEW INDEPENDENT EVIDENCE
        ↓
LEVEL?
BREADTH?
VELOCITY?
FUNDING?
DURATION?
CAPACITY ABSORPTION?
        ↓
CAUSAL EXPOSURE TO COMPANY?
        ↓
IMPACT ON SC / POTENTIAL / RUNWAY / FRICTION?
        ↓
NEW OSE STATE
```

Required fields:

```text
Sector Demand: SD0-SD5
Sector Demand Velocity: ↑↑ / ↑ / → / ↓ / ↓↓
Sector Demand Breadth: Narrow / Mixed / Broad
Sector Demand Funding: Unfunded / Partial / Funded / Locked
Sector Demand Duration: Short / Medium / Multi-year / Structural
Sector Demand Evidence Quality: Low / Medium / High
Sector Demand Confidence: Low / Medium / High
Sector Demand Best Evidence:
Sector Demand Weakest Link:
Sector Demand Next Trigger:
Sector Demand Invalidation:
```

## Updated OSE state card requirement

All new OSE analyses should include:

```text
Sector Demand: SD0-SD5
Sector Demand Velocity:
Sector Demand Breadth:
Sector Demand Funding:
Sector Demand Duration:
```

alongside Potential, Structural Confirmation, Conversion Confirmation, Runway Lock-In, Friction, Recognition, and Remaining Opportunity.

## CAC interpretation

Sector Demand can affect the opportunity differential, but CAC should interpret it in context.

### Favorable configuration

`SD3-SD5 + SC4-SC5 + improving CC + meaningful RL + incomplete recognition`

This is stronger than company evidence occurring in isolation because independent external demand is reinforcing the causal opportunity.

### Warning configuration

`SD4-SD5 + weak SC`

The sector can be excellent while the company is the wrong capture vehicle.

### Trap configuration

`SD4-SD5 + high SC + persistent weak CC + high Friction`

A strong sector and a real bottleneck still do not guarantee shareholder value.

### Cooling-sector configuration

`SD↓ + high SC + high RL + stable/improving CC`

Do not automatically rotate. Determine whether locked runway, share gains, bottleneck migration, or company-specific economics offset the sector slowdown.

## Validation requirement

Sector Demand must be validated point-in-time before any automatic capital-action rule is promoted.

The future test should compare otherwise-identical OSE/CAC decisions with and without the explicit Sector Demand state, using already-approved historical evidence where possible. Primary questions:

- Does explicit Sector Demand improve opportunity ranking beyond company-specific demand/SC alone?
- Does it identify demand cascades and bottleneck migration earlier?
- Does it reduce false positives in fashionable but weakly funded sectors?
- Does it improve rotation timing without causing premature exits from high-RL companies?
- Does it improve compounded capital growth after CAC and Quant constraints?

Until that evidence exists, Sector Demand is **required context, not independent allocation authority**.
