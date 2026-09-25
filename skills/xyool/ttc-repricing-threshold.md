# Xyool — TTC Equity Repricing Threshold / Market-Cap Sensitivity

Status: **CANONICAL PROCESS — ARITHMETIC BURDEN LENS; ECONOMIC-VALUE TRANSLATION AND UNIVERSAL THRESHOLDS PROVISIONAL**

## Core purpose

Xyool must not evaluate a catalyst only by its absolute dollar size.

A modest economic event can be highly material to a very small equity value, while a much larger headline event may barely matter to a large-cap company.

Core question:

> **How much incremental shareholder-capturable value is actually required for this equity to reprice materially from its current denominator?**

Short form:

> **What is the repricing burden?**

This module complements:
- `ttc-catalyst-profitability.md`
- `ttc-dependency-chain.md`
- shareholder-capture analysis
- Recognition / price-response analogs

It does not create capital authority.

---

## 1. Why this exists

A flat catalyst framework can miss asymmetric nano/microcap setups by asking:

> "Is this contract/order/investment large?"

instead of:

> "Is it large relative to what the market currently values the common equity at?"

For a company with a $10 million current equity value:
- a +25% reprice requires roughly +$2.5 million of market value;
- a +50% reprice requires roughly +$5 million;
- a +100% reprice requires roughly +$10 million.

Those are **market-value deltas**, not revenue requirements and not intrinsic-value estimates.

The same catalyst attached to a $2 billion equity has a radically different repricing burden.

---

## 2. Repricing burden

For a target percentage move `r`:

```text
BASIC REPRICING BURDEN(r)
= current basic equity market value × r
```

Where reliable fully diluted information exists:

```text
FD REPRICING BURDEN(r)
= current fully diluted equity value × r
```

Useful audit lenses may include:

```text
+25%
+50%
+100%
```

These are not prediction targets. They are denominator checks.

Always state:
- price timestamp;
- basic shares;
- basic market cap;
- fully diluted share estimate/range if supportable;
- dilution instruments included/excluded;
- target move lenses.

---

## 3. Fully diluted denominator is preferred for fragile capital structures

For companies with meaningful:
- warrants;
- convertibles;
- ATMs / SEPAs;
- earnouts;
- acquisition shares;
- preferred stock;
- employee share pools;
- variable-price instruments;

do not rely on basic market cap alone.

Use:

```text
CURRENT BASIC EQUITY VALUE
CURRENT / NEAR-TERM FD EQUITY VALUE RANGE
POTENTIAL FUTURE SHARE SUPPLY
```

If the fully diluted count cannot be bounded, mark repricing burden:

```text
LOW CONFIDENCE / DYNAMIC DENOMINATOR
```

A falling basic market cap caused by continuing dilution can create a misleading appearance of increasing upside.

---

## 4. Enterprise-value cross-check

Stock repricing burden is an equity-value concept, but catalyst value does not necessarily accrue entirely to common shareholders.

Cross-check:

```text
ENTERPRISE VALUE
NET DEBT / NET CASH
MANDATORY FINANCING NEED
WORKING CAPITAL
CAPEX
PREFERRED / DEBT CLAIMS
```

A company can have:
- $10M equity market cap;
- $35M enterprise value;
- large cash burn / debt obligations.

In that case, a $10M operating improvement does not automatically imply a 100% common-equity reprice.

Rule:

> **Use equity value to measure the stock's percentage repricing burden, but use enterprise economics and capital structure to determine how much catalyst value reaches the common equity.**

---

## 5. Catalyst value bridge

Never equate headline dollars directly with equity value.

Required translation:

```text
HEADLINE EVENT
→ funded / committed economics
→ expected revenue or cost effect
→ gross profit / cash flow
→ duration / persistence
→ capex + working capital
→ financing / debt claims
→ dilution
→ shareholder-capturable incremental value
```

Examples:

A $20M contract is not $20M of equity value.

A $3M annual pretax-profit stream can be more important than a $20M one-time revenue order, depending on persistence, margin, capital needs, risk, and valuation.

An acquisition can create value before a new order if it brings an existing profitable operating business into the consolidated economics.

---

## 6. Repricing coverage — diagnostic only

Where a supportable range for incremental common-equity value exists:

```text
REPRICING COVERAGE(r)
= incremental shareholder-capturable value range
  ÷ repricing burden(r)
```

Interpretation is qualitative unless validated.

Possible audit language:

```text
INSUFFICIENT
PLAUSIBLY MATERIAL
COVERS TARGET BURDEN
MULTIPLE-OF-BURDEN
UNKNOWN
```

Do not turn this into a universal master score.

---

## 7. Minimum Viable Catalyst question

For every nano/microcap, ask:

> **What is the smallest credible event that could add enough common-equity value to matter at today's fully diluted market capitalization?**

This may be:
- one funded order;
- one profitable acquisition closing;
- one approval that unlocks a commercial stream;
- one customer/site expansion;
- one refinancing that removes existential dilution;
- one run-rate proof point.

The answer can be much smaller than the company's long-run bull case.

This is a mandatory research question when:
- market cap is small relative to plausible next-event economics;
- price has compressed materially;
- the next gate has strong evidence;
- or same-company event reactions show nonlinear sensitivity.

---

## 8. Repricing threshold and dependency chains

Use `ttc-dependency-chain.md` first.

For each economically meaningful node ask:

```text
What repricing burden exists today?
How much value could THIS node add by itself?
How much downstream value does it unlock?
How many gates remain before that value is shareholder-capturable?
```

This prevents two opposite errors:

### Error A — undervaluing a small gate
A definitive agreement may add little immediate revenue but remove enough uncertainty to reprice a $10M equity substantially.

### Error B — overvaluing upstream optionality
A technical milestone may unlock a large theoretical downstream market but still leave several low-confidence gates before common shareholders capture value.

---

## 9. Recognition elasticity

Track how a company's equity has historically responded to economically comparable events relative to its then-current equity value.

For each analog record where practical:

```text
event
equity market cap before event
fully diluted market cap if available
funded / capturable economic size
event-to-equity-value ratio
1D / 5D / 20D price response
share-count change around event
surprise / already-priced state
```

This is more informative than comparing absolute contract sizes across companies.

A $5M order may be trivial for one company and transformational for another.

---

## 10. Float / liquidity and nonlinear moves

Small equities can overshoot fundamental value because of:
- low effective float;
- thin liquidity;
- short positioning;
- options/warrant mechanics;
- concentrated ownership;
- sudden attention.

Classify this separately as:

```text
MARKET-MICROSTRUCTURE AMPLIFIER
```

It can increase `P(Material Price Move | Hit)` or move magnitude.

It does not increase underlying economic value.

Do not rely on squeeze/illiquidity mechanics as the fundamental thesis.

---

## 11. Reverse stock split treatment

A reverse stock split is generally a **nominal capital-structure action**, not an economic-value catalyst.

Mechanically:

```text
share price × split ratio
share count ÷ split ratio
market cap ≈ unchanged before market reaction
ownership % ≈ unchanged before other issuance
```

Therefore:

- do not treat the post-split nominal price as economic improvement;
- keep historical prices/share counts split-adjusted for analog work;
- recalculate dilution instruments according to their contractual adjustments;
- do not let a reverse split erase conversion/warrant/SEPA risk;
- treat Nasdaq-compliance effects and liquidity effects separately.

### Reverse-split pressure timer

When:
- the board already has authorization;
- the stock is below the relevant listing threshold;
- or a formal exchange deficiency exists;

track a capital-structure timer:

```text
AUTHORIZATION
→ DEFICIENCY / COMPLIANCE WINDOW
→ BOARD RATIO DECISION
→ EFFECTIVE SPLIT
→ POST-SPLIT COMPLIANCE / SUPPLY BEHAVIOR
```

The split can alter:
- listing survival probability;
- nominal access for funds/brokers;
- float / liquidity;
- short-term trading behavior;
- authorized-but-unissued share capacity.

It does not by itself create operating value.

Do not assume post-split price decline or rally. Measure same-company and close-analog behavior.

---

## 12. Compression can increase convexity — but only if the denominator is real

When price falls faster than the underlying probability-adjusted shareholder-capturable opportunity:

```text
REPRICING BURDEN FALLS
while
CATALYST VALUE REMAINS SIMILAR
→ potential convexity increases
```

But distinguish:

### Genuine compression
- business/catalyst value relatively intact;
- share count roughly stable or dilution bounded;
- market price falls due to recognition/risk aversion/technical pressure.

### False compression
- basic market cap falls because share count is expanding;
- debt/convertibles worsen;
- catalyst probability deteriorates;
- financing need rises;
- value is migrating from common equity to creditors/new shares.

Only the first can improve asymmetry cleanly.

---

## 13. Required output fields

For material catalyst-profitability work, add where supportable:

```text
Basic Market Cap:
Fully Diluted Market Cap / Range:
Enterprise Value:
Dynamic Dilution State:

25% Repricing Burden:
50% Repricing Burden:
100% Repricing Burden:

Minimum Viable Catalyst:
Catalyst Capturable-Value Range:
Repricing Coverage:
Microstructure Amplifier:
Reverse-Split / Listing Timer:
Confidence:
```

Do not fabricate fully diluted precision.

---

## 14. Top-50 implication

The Top 50 should not rank only by:
- catalyst proximity;
- absolute contract size;
- total addressable market;
- headline revenue.

It should explicitly consider:

```text
EXPECTED SHAREHOLDER-CAPTURABLE VALUE
relative to
CURRENT / FD EQUITY VALUE
through
TIME + PROBABILITY + DEPENDENCY GATES
```

A nano-cap with one credible $5M-to-$10M equity-value event can have more repricing leverage than a large-cap with a $100M event.

But a heavily dilutive nano-cap can still be a poor capital destination.

---

## 15. Validation

Prospectively record:

```text
pre-event price
basic shares
FD share estimate/range
market cap / EV
event economics
estimated capturable-value range
25/50/100% repricing burdens
dependency stage
actual 1D / 5D / 20D move
share-count change
later economic realization
```

Test whether the repricing-burden lens improves prediction of:
- which catalysts create material price moves;
- move magnitude ranges;
- missed nano/microcap opportunities;
- false positives caused by dilution or distressed balance sheets.

---

## Core rule

> **A catalyst does not need to be large in absolute terms. It needs to be large relative to the value the market currently assigns to the common equity, after accounting for the gates and claims that stand between the event and shareholders.**
