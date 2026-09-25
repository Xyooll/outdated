# Xyool — TTC Catalyst Profitability / Event Integrity

Status: **CANONICAL REQUIRED TTC INPUTS; NUMERIC CALIBRATION PROVISIONAL**

## Core purpose

A catalyst is useful to capital allocation only if it can plausibly create realizable shareholder profit.

TTC therefore separates internally:

```text
CATALYST PROXIMITY
CATALYST SUCCESS PROBABILITY
PRICE-RECOGNITION PROBABILITY
MOVE MAGNITUDE
FAILURE / DELAY DOWNSIDE
CASCADE DEPENDENCY
```

The objective is not to own the stock with the nearest event. The objective is to prefer qualified opportunities with the strongest probability-adjusted remaining payoff through time.

> **A close catalyst with little expected repricing is not a strong TTC catalyst.**

This file supplements `time-to-catalyst.md`. It does not create a separate allocation authority.

---

## 1. Event-integrity lock — mandatory before probability work

Every material catalyst must first pass an identity/freshness check.

Record:

```text
Ticker / Company:
Program / Product / Project:
Catalyst Type:
Causal Stage:
Decision Maker / Customer / Regulator:
Exact Stop Event:
Hard Date or Window:
Timing Type: HARD DATE / COMPANY-GUIDED / INFERRED
Primary Source:
Primary Source Date:
Last Freshness Check:
Superseding Evidence Search:
Current Status: UNRESOLVED / REALIZED / DELAYED / SUPERSEDED / INVALIDATED
```

The event key is:

```text
COMPANY + PROGRAM/PROJECT + STAGE + DECISION MAKER + STOP EVENT
```

Do not transfer evidence from another program at the same company. A contract ceiling is not a funded order. A deployment in Product A does not prove acceptance for Product B.

Before presenting a hard date as current:
1. verify it from a primary filing, regulator, or issuer source;
2. search for delay, extension, withdrawal, superseding transaction, or completed event;
3. preserve exact program/product identity;
4. record the check date.

Once an event happens, close it immediately and advance to the next supported causal timer.

---

## 2. Catalyst Profitability Object

For each unresolved material catalyst keep internally:

```text
P(Hit):
P(Material Price Move | Hit):
Conditional Upside Range if Hit:
Conditional Downside Range if Failure / Delay:
P(Delay / No-Decision):
Expected Event Window:
Days / Window to Event:
Surprise State: UNEXPECTED / PARTLY EXPECTED / WELL TELEGRAPHED
Already-Priced State: LOW / MEDIUM / HIGH
Economic Materiality vs Equity / EV:
Basic Market Cap:
Fully Diluted Market Cap / Range:
Enterprise Value:
25% / 50% / 100% Repricing Burden:
Minimum Viable Catalyst:
Dynamic Dilution State:
Per-Share Capture:
Payoff Persistence:
Liquidity / Exit Friction:
Confidence:
Analog Set:
Cascade ID / Gate Number:
Dependency Node ID:
Primary Gating Node?: YES / NO
Upstream Dependencies:
Downstream Profit-Producing Gate:
Terminal Economic Node:
Profitability Gap Closure: qualitative/range where supportable
```

For contract-like catalysts first apply the Contract Decomposition Rule in `contract-economic-ladder.md`. Retain a separate profitability record for each economically distinct material component.

```text
Contract Component ID / Tranche:
Contract Economic Rung: CE0-CE5
Contract Commitment Quality: PROTECTED / CONDITIONAL / WEAK / UNKNOWN
Optioned Economic Surface:
Committed Economic Value:
Ceiling / Maximum:
Company-Specific or Shared:
Currently Obligated / Funded:
Next CE Transition:
```

Apply `contract-economic-ladder.md`. Do not use a vehicle ceiling, total program value, optional maximum, or customer budget as committed event economics.

Do not map CE/CQ directly to position size. CE/CQ informs economic reliability; TTC still owns profitability/capital priority and Quant owns downstream executable risk expression.

`P(Material Price Move | Hit)` remains separate from `P(Hit)` internally. A catalyst can have high P(Hit) and low stock response.

These technical probability fields are **not required as separate columns in the default human-facing Top-50 display**. Their effects are compressed into `Happens?` and `Profit View` under `top50-exact-date-display-standard.md`.

---

## 3. Dependency-adjusted catalyst economics

For a catalyst that sits inside a serial or branching economic path, apply `ttc-dependency-chain.md` before interpreting headline economics.

Required questions:

```text
Is this node a prerequisite, conversion gate, or terminal economic event?
Which required upstream nodes remain unresolved?
What downstream economic nodes become reachable if this node succeeds?
What revenue / gross-profit / cash-breakeven gap can the path plausibly close?
What financing or dilution remains before common shareholders capture that value?
What is the current basic/fully diluted repricing burden?
Could a modest but credible node clear that burden even if its absolute economics look small?
```

Apply `ttc-repricing-threshold.md` for the equity-denominator lens. This is especially important for nano/microcaps and distressed equity denominators.

Do not assign a downstream funded-order or profitability payoff to an upstream technical/contractual gate merely because it is necessary.

Conceptual joint probability can be useful for reasoning about a serial path, but universal multiplication of unvalidated point probabilities is prohibited. Preserve conditional dependence and uncertainty.

A catalyst may have high immediate `P(Hit)` while the probability of reaching the terminal profit-producing node remains much lower because several required gates remain.

---

## 4. Price-move evidence hierarchy

Estimate price-response probability and move size from the most specific evidence available:

1. same company + same catalyst type + prior realized event;
2. same company + economically similar event;
3. same customer/regulator/mechanism + close peer;
4. close industry/event archetype;
5. broad event-study prior only if nothing better exists.

For realized analogs record where practical:

```text
Event Date:
1D Move:
5D Move:
20D Move:
Relevant Benchmark Move:
Approx. Abnormal Move:
Was Event Expected?:
Was Economics Similar?:
```

One case is evidence, not a universal coefficient. Do not invent a precise probability from a weak analog set. Widen the range and lower confidence.

---

## 5. Event economics vs stock response

For every catalyst ask:

1. Did the event change economics?
2. How large are company-capturable economics relative to equity/EV and earnings?
3. How much was already expected?
4. Does it remove a meaningful uncertainty discount?
5. Does it create recurring / stacked economics or one-off value?
6. Can it materially alter per-share value?
7. Will financing, dilution, debt, concentration, valuation, or liquidity absorb the benefit?
8. What has the stock done when comparable information arrived?

Persistent economics do not imply persistent price appreciation. Recognition must be modeled separately.

---

## 6. Multi-gate catalysts and cascades

Do not collapse a causal chain into one undifferentiated probability.

Example:

```text
FIELD TEST / SAT
   ↓
ACCEPTANCE
   ↓
PROCUREMENT
   ↓
DEPLOYMENT
   ↓
REVENUE
```

Each gate can have different timing, probability, economic materiality, and market impact.

TTC must identify separately:

```text
NEXT CHRONOLOGICAL EVENT
NEXT ECONOMIC-CONVERSION EVENT
NEXT PROFIT-PRODUCING EVENT
```

### Cascade dependency

When later gates depend on earlier gates, model them conditionally rather than as independent events.

For a chain:

```text
G1 -> G2 -> G3 -> REALIZATION
```

use the logic:

```text
P(G2) = P(G1) × P(G2 | G1)
P(G3) = P(G2) × P(G3 | G2)
```

The exact implementation may use ranges rather than point probabilities, but dependency must be preserved.

### Cascade Profit View

For a cascade stock, `Profit View` is the **probable cumulative stock-price move across the displayed cascade window**.

It is not the reaction to only the nearest headline and it is not the simple arithmetic sum of isolated event reactions.

Construct it by estimating the **incremental new information / economic recognition** at each gate, conditional on prior gates, and then forming one cumulative range.

Mandatory controls:
1. do not double-count the same economics at multiple gates;
2. do not treat correlated gates as independent;
3. update downstream probabilities when an upstream gate realizes;
4. distinguish technical confirmation from funded economics;
5. truncate the cascade at the economically relevant stop event for the current capital horizon;
6. reopen a new timer when later downstream value becomes decision-relevant.

Examples include:

```text
CODA: SAT -> acceptance -> procurement -> deployment
WYFI: site activations -> utilization -> revenue
APLD: build -> live MW -> rent
ASTS: deployment -> beta -> commercial service
```

---

## 7. Binary regulatory events

Regulatory decisions must not win merely because their date is exact.

For biotech/medtech record separately:
- quality of pivotal evidence;
- prior CRL / deficiency history;
- whether issues were clinical, CMC, inspection, administrative, or labeling;
- advisory-committee status where relevant;
- unmet need / first-in-class state;
- company dependence on the program;
- diversification from other programs;
- approval economics relative to market cap;
- failure downside and financing runway.

For materially asymmetric binary events, human-facing `Profit View` should display both probable upside and downside ranges.

---

## 8. Operating catalyst classes

Treat these separately:

### Contract / order
Often price-sensitive when value is large relative to company size, unexpected, funded, and incremental.

### Deployment / activation
Can have high P(Hit) but low surprise if already contracted and scheduled. It may still be important as an upstream cascade gate.

### Revenue / run-rate proof
Often more important than deployment because it proves utilization, margin, recurring economics, or operating leverage.

### Capacity commissioning
Material only if demand, utilization, and shareholder capture are credible.

### Qualification / acceptance
May remove uncertainty but is not procurement. Model whether it unlocks funded economics downstream.

### Launch / technical milestone
A technically successful launch can have low immediate economic value if expected and no new revenue is unlocked.

---

## 9. Provisional profitability calculation

Until validated, do not compress TTC into one opaque master score.

For a single event, a transparent scenario framework remains:

```text
Catalyst EV ≈
P(Hit) × P(Material Move | Hit) × Expected Upside if Recognized
− P(Failure) × Expected Failure Downside
− P(Material Delay) × Delay / Opportunity Cost
```

For a cascade, use conditional gate progression and incremental move contributions rather than applying this equation independently to every gate and summing the results.

All terms should be ranges when precision is not earned.

Use the calculation to expose assumptions, not hide them.

---

## 10. Profitability priority

Every TTC comparison must preserve two distinct orders internally:

```text
CHRONOLOGICAL CATALYST ORDER
= what is expected to resolve first?

PROFITABILITY PRIORITY
= which qualified opportunity offers the best probability-adjusted realizable payoff through time?
```

A catalyst can be first chronologically and low on profitability priority.

A multi-step cascade can outrank a nearer single event when the cumulative probability-adjusted realizable payoff is stronger, but cascade length by itself is not a positive signal.

---

## 11. Output requirements

### Internal / audit output

For serious TTC comparison retain:

```text
next chronological event
next profit-producing event
hard date / inferred window
timing type and basis
event-integrity status
P(Hit) range
P(Material Price Move | Hit) range
conditional upside
failure / delay downside
already-priced / recognition state
price-reaction analogs
basic / fully diluted market cap
repricing burden / minimum viable catalyst
dynamic dilution / reverse-split state
cascade dependencies
profitability priority
confidence
```

### Default human-facing Top-50 output

Use the canonical compressed display:

```text
Rank | Stock | Q | Date / Window | Catalyst | Happens? | Profit View
```

Where:
- `Happens?` translates catalyst/cascade success probability into human language;
- `Profit View` is the probable stock-price move across the displayed window;
- `Priced In` and `Stock Cares?` stay internal because their effects are already reflected in `Profit View`;
- exact dates remain explicit;
- non-exact timing uses an honest window, with `~` when Xyool inference/analogs are required;
- cascade stocks show the linked economically relevant chain.

Authoritative presentation rules live in `skills/xyool/top50-exact-date-display-standard.md`.

---

## 12. Miss-prevention questions

Before publishing or acting on a catalyst ranking, ask:

1. Am I discussing the exact same program/project as the scheduled event?
2. Did I verify the date/window from a primary source where possible?
3. Did I search for a newer delay, extension, superseding event, or completed event?
4. Am I calling an expected milestone a surprise?
5. If it hits, what actually changes per share?
6. Has a similar event moved this stock before?
7. Is the economically larger event one gate later?
8. Is this a cascade rather than a single event?
9. Did I double-count economics across cascade gates?
10. What happens if the catalyst hits and the stock does nothing?
11. What is the failure/delay downside?
12. Has the prior catalyst already been recognized and therefore needs to be closed?
13. Did I compare the catalyst's capturable value with the current / fully diluted equity repricing burden rather than absolute dollars alone?
14. Is a low market cap genuine compression or merely a shrinking basic denominator caused by dilution / debt pressure?
15. If this is a contract catalyst, what CE rung is actually supported?
16. Am I confusing Optioned Economic Surface with Committed Economic Value?
17. Is the headline ceiling company-specific, shared, optional, or still subject to future task-order competition?

These questions are canonical process controls derived from the miss-to-question learning loop.

---

## 13. Validation boundary

Mandatory event identity, freshness, closeout, separate success/response concepts, cascade dependency, and anti-double-counting are **canonical process requirements**.

Numeric probability bands, event-type priors, move-size priors, cascade move ranges, and any compressed profitability number remain **PROVISIONAL** until tested on prospective and historical holdouts with anti-lookahead controls.

Promote calibration only if it improves realized capital outcomes or timing decisions without materially increasing false positives, turnover, drawdown, or hindsight fit.
