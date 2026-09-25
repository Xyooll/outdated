# Xyool — Multi-Method Discovery and Market-Structure Shadow

Status: **EXPERIMENTAL / SHADOW-ONLY**
Date: **2026-09-22**

## Purpose

Xyool must not depend on headlines as the only doorway into a stock.

The stock domain now supports multiple independent discovery families:

```
CATALYST
FUNDAMENTAL
EXPECTATIONS
PRICE / MARKET STRUCTURE
OWNERSHIP
ENTITY / SUBSIDIARY NETWORK
REGIME / FACTOR
LIQUIDITY / MICROSTRUCTURE
STATISTICAL
```

A stock can become research-visible from any family. Discovery does not itself authorize capital.

## Corporate entity graph

Evidence may originate below or beside the listed parent:

```
PUBLIC SECURITY
  ↕
PUBLIC PARENT
  ↓
SUBSIDIARY / JV
  ↓
SEGMENT
  ↓
PROGRAM / PRODUCT
  ↓
CUSTOMER / CONTRACT
```

Required relationship evidence where applicable:
- legal entity name;
- parent;
- ownership percentage when known;
- consolidated vs unconsolidated treatment when known;
- reporting segment;
- program/product;
- contract/customer legal counterparty;
- source/provenance and effective date.

A subsidiary headline may propagate to the parent only through an explicit relationship path. Unknown ownership or consolidation remains UNKNOWN.

The graph improves:
- discovery from subsidiary/legal-entity names;
- correct contract attribution;
- materiality denominator selection;
- JV/minority-interest treatment;
- segment-level causal reasoning;
- supplier/customer correspondence.

## Market-structure state

The first shadow implementation records:
- SMA20 / SMA50 / SMA200;
- price relative to each average;
- Donchian 20-session breakout/breakdown;
- distance from rolling 52-week high;
- RSI14;
- ATR14 as percent of price;
- relative volume versus prior 20 sessions;
- anchored VWAP and distance from anchor;
- coarse structure state: BREAKOUT / BREAKDOWN / UPTREND / DOWNTREND / RANGE_OR_MIXED.

Future candidates may include:
- swing-defined higher-high/higher-low structure;
- volume profile / high-volume nodes;
- gap/reclaim/failure states;
- breadth and sector-relative structure;
- residual/factor-neutral momentum;
- volatility compression/expansion;
- support/resistance persistence.

These are observations, not automatic BUY/SELL rules.

## Fibonacci

Fibonacci retracement levels are available only as an **experimental geometry feature**.

They have zero authority by default.

The relevant RLE question is not:

> Did price touch 0.618?

It is:

> Does proximity/reaction to a Fibonacci level add incremental information after ordinary swing geometry, support/resistance, trend, volatility and volume are controlled?

If not, discard it.

## Confluence without double counting

Indicators must be grouped into causal/statistical families.

Example:

```
RSI positive
close > 50DMA
20-day breakout
near 52-week high
positive time-series momentum
```

may all be manifestations of one underlying price-persistence state.

They do **not** count as five independent confirmations.

Xyool therefore separates:
- method;
- family;
- independent_key / latent phenomenon.

Within a family/independent key, duplicate indicators are alternative measurements. Cross-family confirmation is tracked separately.

Core law:

> **Confluence is useful only to the extent that the evidence is conditionally independent or measures meaningfully different state.**

## Relationship to Recognition

The shadow sequence is:

```
MULTI-METHOD DISCOVERY
        ↓
QUALITY ELIGIBILITY
        ↓
ECONOMIC / CAUSAL STATE
        ↓
RECOGNITION
        +
MARKET STRUCTURE / EXPECTATIONS / OWNERSHIP / REGIME SHADOW
        ↓
EXPECTED PAYOFF RESEARCH
```

For the active Recognition V1 trial, these new features may be frozen and analyzed but **may not change C1**.

Any action-changing successor must receive a new method/version identity and fresh validation.

## Anti-headline requirement

A discovery scan is incomplete if it only asks for new filings/news/catalysts.

At minimum it should be capable of asking:
- what companies show unusual factor-neutral or relative momentum?
- what names are breaking/reclaiming meaningful structure?
- where did estimates/guidance materially change?
- where did insiders/beneficial owners accumulate?
- where did subsidiary/customer/supplier evidence change parent state?
- where did fundamentals inflect without a new headline catalyst?
- where did liquidity/volume/volatility state change materially?
- where is a statistical peer relationship diverging?

The output is a research queue, not a capital instruction.

## Promotion

No method becomes canonical because it is popular or intuitively convincing.

Promotion requires:
- point-in-time implementability;
- frozen definition;
- incremental value over simpler methods;
- family/indicator double-counting audit;
- multiple-testing disclosure;
- untouched sequential validation;
- outlier/class/regime robustness;
- realistic costs where relevant.
