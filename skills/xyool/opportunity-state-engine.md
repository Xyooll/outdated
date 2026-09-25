# Xyool — Opportunity State Engine

## Purpose

The Opportunity State Engine (OSE) is the dynamic state layer between company-level Xyool analysis and the Capital Allocation Controller (CAC).

Its purpose is to continuously answer:

> **What is the opportunity becoming, how much of it remains, and how strong is the evidence that it is becoming real?**

The OSE prevents Xyool from treating an opportunity as a static score. Opportunities evolve through evidence, time, price recognition, fundamental conversion, and risk changes.

Core state flow:

**POTENTIAL → CONFIRMATION → IGNITION → RECOGNITION → MATURITY → HARVEST / ROTATION**

The OSE does not decide portfolio size by itself. It produces a state representation that CAC uses to allocate capital.

---

## 1. Core Principle

Every opportunity has two independent dimensions:

### Potential

> **How much capital multiplication could still remain if the thesis develops?**

### Confirmation

> **How much evidence says the thesis is actually developing?**

Do not combine these into one score too early.

The highest-value state is generally:

> **HIGH REMAINING POTENTIAL × RAPIDLY RISING CONFIRMATION × APPROACHING IGNITION**

This is the primary hunting state for asymmetric opportunities.

---

## 2. Opportunity State Object

Represent every candidate and holding as:

```text
OPPORTUNITY STATE
├── identity
├── price
├── position
├── potential
│   ├── economic magnitude
│   ├── remaining upside
│   ├── scenario range
│   └── opportunity horizon
├── confirmation
│   ├── evidence strength
│   ├── evidence breadth
│   ├── evidence freshness
│   └── confirmation velocity
├── fundamental trajectory
├── ignition state
├── recognition state
├── shareholder capture
├── capital efficiency
├── resistance / friction
├── permanent impairment risk
├── time-to-catalyst
├── time-to-maturity
├── opportunity differential
├── confidence
├── state
├── state direction
└── next trigger
```

Every field should have, where possible:

- current state
- previous state
- direction ↑ / → / ↓
- magnitude
- confidence
- evidence timestamp
- supporting evidence
- invalidation condition
- next update trigger

---

## 3. Potential Engine

Potential measures the remaining economic opportunity rather than historical stock performance.

Evaluate:

1. Current economic state
2. Plausible future economic state
3. Revenue potential supported by evidence
4. Margin potential
5. EBITDA / FCF potential
6. Market-share or bottleneck expansion
7. New revenue streams
8. Capacity expansion
9. Per-share economics
10. Plausible valuation range
11. Time required to reach the state
12. Bear/base/bull outcomes

Never use unconstrained TAM as the opportunity itself.

Potential must be connected to a causal chain:

**DEMAND → CONTROL → ORDERS → BACKLOG → DEPLOYMENT → REVENUE → MARGIN → EBITDA → FCF → PER-SHARE VALUE**

### Potential states

- **P0 — Minimal**: little identifiable asymmetric opportunity
- **P1 — Emerging**: plausible opportunity but limited evidence
- **P2 — Material**: meaningful economic path exists
- **P3 — Large**: substantial supported expansion path
- **P4 — Exceptional**: unusually large asymmetric path with strong structural support
- **P5 — Extreme**: potentially transformational outcome, but requires explicit probability discipline

Potential is not probability.

A P5 opportunity can have low confirmation and therefore deserve little or no capital.

---

## 4. Confirmation Engine

Confirmation measures whether reality is moving toward the potential state.

Evidence should be classified:

### C0 — Narrative
Management claims, thematic discussion, TAM, strategy, or unverified expectation.

### C1 — Initial Evidence
Early customer activity, pilots, small contracts, initial backlog, early operating improvement.

### C2 — Repeated Evidence
Multiple quarters, repeated orders, backlog growth, recurring customers, improving operating metrics.

### C3 — Economic Confirmation
Revenue, margins, EBITDA, OCF, FCF, per-share economics, or other financial conversion validates the thesis.

### C4 — Independent Confirmation
Multiple independent evidence streams confirm the same trajectory: customers, contracts, industry data, competitors, filings, financial results, capacity, and market behavior.

### C5 — Self-Reinforcing Confirmation
The thesis is becoming increasingly difficult to invalidate because economic evidence, customer behavior, financial results, capacity, and market recognition reinforce one another.

Confirmation should track both **level** and **velocity**.

### Confirmation velocity

Ask:

> **Is the evidence confirming the thesis faster than the market is recognizing it?**

Possible states:

- accelerating ↑↑
- improving ↑
- stable →
- weakening ↓
- collapsing ↓↓

---

## 5. Potential × Confirmation Matrix

Use the matrix as a decision aid, not an automatic trade rule.

| | Low Confirmation | Rising Confirmation | High Confirmation |
|---|---|---|---|
| **Low Potential** | Avoid | Watch | Mature / limited upside |
| **Medium Potential** | Watch | Candidate | Selective allocation |
| **High Potential** | Early optionality | **Sweet spot** | Strong opportunity / maturity check |
| **Exceptional Potential** | Speculative | **High-priority validation** | **Major opportunity; compare remaining upside** |

### Sweet spot

**High/exceptional potential + rapidly rising confirmation**.

If ignition is approaching and resistance is manageable, the opportunity can become a high-priority CAC candidate.

### Important distinction

High potential + low confirmation is not equivalent to high potential + high confirmation.

The first is an option.

The second is an increasingly validated opportunity.

---

## 6. Fundamental Trajectory Engine

Track the leading economic sequence:

**DEMAND → ORDERS → BOOKINGS → BACKLOG → NEW REVENUE STREAMS → DEPLOYMENT → REVENUE → MARGIN → EBITDA → OCF → FCF**

For each rung record:

- level
- direction
- rate of change
- acceleration/deceleration
- evidence quality
- confidence
- next trigger

### Desired condition

> **Leading fundamentals accelerate before trailing financial results fully reflect them.**

Examples:

- bookings accelerating before revenue
- backlog accelerating before revenue
- new contracts before earnings
- utilization before margin expansion
- operating leverage before FCF inversion

This allows the OSE to detect trajectory before the income statement fully catches up.

---

## 7. Ignition Integration

Use the existing Xyool Ignition ladder:

- **I0 — Dormant**
- **I1 — Pressure**
- **I2 — Absorption**
- **I3 — Release**
- **I4 — Ignition**
- **I5 — Reflexive**

The OSE asks:

1. Is potential high enough to matter?
2. Is confirmation rising?
3. Are fundamentals accelerating?
4. Is recognition still incomplete?
5. Is resistance compressing?
6. Is a catalyst approaching?
7. Is price beginning to respond?

### Priority state

A particularly valuable configuration is:

**P3+ + C2→C4 + I2→I3 + large recognition gap**

This means:

- opportunity is large
- confirmation is materially increasing
- ignition may be approaching
- market recognition remains incomplete

This state should be surfaced aggressively to CAC.

---

## 8. Recognition State

Track how much of the economic trajectory has been priced.

Recognition ladder:

- R0 — Ignored
- R1 — Narrative recognized
- R2 — Initial recognition
- R3 — Earnings recognized
- R4 — Estimate revisions
- R5 — Institutional recognition
- R6 — Valuation expansion
- R7 — Fully priced

The OSE must distinguish:

**fundamental acceleration** from **recognition acceleration**.

The ideal asymmetric state is often:

> **Fundamentals ↑↑ while recognition remains relatively low.**

As recognition catches up, remaining opportunity must be recalculated.

---

## 9. Remaining Opportunity Engine

Historical return is not remaining opportunity.

Calculate conceptually:

**Remaining Opportunity = Future Economic Value Still Available × Probability of Realization − Friction / Permanent Impairment Risk**

Then adjust for time and shareholder capture.

Ask:

- What economic milestones remain?
- How much valuation expansion remains reasonable?
- How much growth is already priced?
- How much recognition remains?
- How much dilution remains?
- How much time remains?
- What new information could increase or destroy the opportunity?

A stock that has already risen 80% can have greater remaining opportunity than a stock that has not moved.

A stock that has not moved can have almost no remaining opportunity if its thesis is failing.

---

## 9A. Profitability Transmission State

OSE must explicitly represent whether company execution can plausibly transmit into **profitable stock returns from the current price**.

Required fields:

```text
profitability_transmission:
  incremental_economics
  normalized_earnings_bridge
  valuation_denominator
  recognition_vs_fundamentals
  sector_regime
  shareholder_capture
  remaining_price_upside
  confidence
```

The transmission path is:

```text
COMPANY EXECUTION
-> INCREMENTAL ECONOMICS
-> NORMALIZED EARNINGS / CASH
-> CURRENT VALUATION DENOMINATOR
-> RECOGNITION + SECTOR REGIME
-> SHAREHOLDER CAPTURE
-> REMAINING PRICE UPSIDE
```

This state exists because:

```text
GOOD COMPANY RESULT
!=
PROFITABLE STOCK RESULT
```

Examples of transmission failure:
- backlog converts, but the valuation already discounts it;
- revenue grows, but margins/cash do not;
- EBITDA improves, but GAAP/cash economics are distorted by one-time items;
- the company executes while its sector undergoes multiple compression;
- operating value rises while dilution/debt captures the value before common shareholders;
- a catalyst succeeds after recognition has already exhausted the remaining upside.

OSE should therefore distinguish:

```text
TRANSMISSION_STRONG
TRANSMISSION_ADEQUATE
TRANSMISSION_FRAGILE
TRANSMISSION_BLOCKED
TRANSMISSION_UNKNOWN
```

A `TRANSMISSION_FRAGILE / BLOCKED` state may reduce remaining opportunity even while Confirmation increases.

---

## 9B. Experimental Market-Expectation / Execution Shadow State

OSE may preserve a parallel **shadow state** for external-market and implementation evidence:

```text
EXPECTATIONS DIFFUSION
+ FACTOR-NEUTRAL RECOGNITION
+ EXECUTION / CAPACITY
+ SHORT FEASIBILITY
```

Candidate observations include:
- earnings surprise and guidance change;
- analyst revision direction, breadth, magnitude, persistence and dispersion;
- sector-relative and factor-residual momentum;
- bid/ask spread, dollar volume, slippage and market impact;
- borrow availability, borrow fee, crowding and squeeze risk.

Shadow-state purpose:

```text
CAUSAL COMPANY STATE explains WHY economics may change.
SHADOW MARKET STATE measures WHETHER expectations are diffusing,
whether price recognition is company-specific,
and whether the thesis is implementable.
```

Authority firewall:

```text
SHADOW STATE
-> MEASURE / LOG / TEST
-> no direct OSE promotion
-> no direct TTC allocation
-> no rank invalidation
```

unless the analysis is inside a pre-registered augmented validation arm.

No sparse analyst coverage may be interpreted as negative revision evidence.

A negative residual-momentum state may open recognition/profitability review but cannot by itself create RF3/RF4.

Canonical test contract:
- `skills/xyool/market-expectations-execution-sidecar.md`
- `skills/xyool/research-validation-governance.md`

---

## 10. State Transitions

Every event must update the state rather than simply append information.

```text
OLD STATE
   ↓
NEW EVIDENCE
   ↓
WHAT CHANGED?
   ↓
POTENTIAL?
CONFIRMATION?
FUNDAMENTALS?
IGNITION?
RECOGNITION?
FRICTION?
TIME?
   ↓
NEW OPPORTUNITY STATE
   ↓
CAC ALLOCATION UPDATE
```

### Example

```text
P3 / C1 / I2
      ↓
large funded order
      ↓
P3 / C2 / I2
      ↓
revenue begins converting
      ↓
P3 / C3 / I3
      ↓
estimate revisions + volume
      ↓
P3 / C4 / I4
      ↓
recognition accelerates
      ↓
P3 / C5 / I5
      ↓
remaining opportunity recalculated
      ↓
HARVEST / HOLD / ROTATE
```

The same process works in reverse.

## 10A. Return Failure State

OSE must track a separate **Return Failure State** so a holding is not preserved merely because the underlying company thesis remains intact.

States:

```text
RF0 — NONE
RF1 — WATCH
RF2 — ACTIVE DIVERGENCE
RF3 — CAPITAL-PRIORITY FAILURE
RF4 — THESIS / CAPTURE FAILURE
```

Interpretation:

- **RF0**: price/return behavior is compatible with the expected opportunity path.
- **RF1**: underperformance or recognition compression deserves review but does not alter capital priority yet.
- **RF2**: company evidence remains intact, but stock return/recognition/sector behavior is diverging enough to require a full profitability-transmission audit.
- **RF3**: the company thesis may still be directionally right, but expected remaining return velocity is now inferior to alternatives/cash.
- **RF4**: fundamental thesis or shareholder-capture path has materially failed.

A move to RF2+ must trigger:

```text
NORMALIZED EARNINGS CHECK
+ VALUATION / REPRICING CHECK
+ RECOGNITION CHECK
+ SECTOR REGIME CHECK
+ SHAREHOLDER-CAPTURE CHECK
+ ALTERNATIVE / CASH COMPARISON
```

RF3 is sufficient to recommend `REDUCE / ROTATE / CASH` even when confirmation of the operating thesis is still high.

Price decline alone cannot create RF3 or RF4. The state requires evidence that the remaining opportunity or return velocity has deteriorated.

### RF3 evidence firewall

A benchmark selloff does not convert price movement into fundamental evidence.

Allowed:

```text
RF2 PRICE / RELATIVE DIVERGENCE
+ refreshed non-price evidence of weaker economics / capture / repricing / opportunity cost
-> RF3
```

Not allowed:

```text
stock drawdown threshold
+ benchmark drawdown threshold
-> RF3 automatically
```

Price and benchmark thresholds may trigger or intensify the RF2 audit. RF3 must still be supported by at least one non-price deterioration in the remaining-opportunity case.

Example deterioration:

```text
P3 / C4 / I3
      ↓
backlog cancellation + guidance cut
      ↓
P2 / C2 / I1
      ↓
probability falls
      ↓
remaining opportunity falls
      ↓
ROTATION REVIEW
```

---

## 11. State Velocity

Static state is insufficient.

Track the velocity of change:

### Potential velocity
Is the plausible economic destination becoming larger or smaller?

### Confirmation velocity
Is evidence strengthening or weakening faster?

### Fundamental velocity
Are economic metrics accelerating or decelerating?

### Ignition velocity
Is the stock moving from dormant → pressure → release → ignition?

### Recognition velocity
Is the market closing the recognition gap?

### Resistance velocity
Is financial/structural friction compressing or increasing?

### Opportunity velocity
Is the probability-adjusted remaining opportunity improving faster or slower than alternatives?

The controller should prioritize **positive state velocity** when remaining opportunity is large.

---

## 12. Opportunity Differential Integration

OSE produces the state needed by CAC.

For two opportunities A and B compare:

```text
Potential
Confirmation
Confirmation Velocity
Fundamental Velocity
Ignition
Recognition Gap
Remaining Opportunity
Time
Shareholder Capture
Capital Efficiency
Permanent Impairment Risk
Confidence
```

Conceptually:

**Opportunity Differential(A,B) = Remaining Opportunity(A) − Remaining Opportunity(B)**

But also track:

**Confirmation Differential**

**Time Differential**

**Risk Differential**

**Ignition Differential**

This prevents a large theoretical upside from dominating when its evidence is stagnant.

---

## 13. Rotation Trigger Matrix

### Increase / Initiate
Prefer when:

- potential is high
- confirmation is accelerating
- fundamental trajectory is accelerating
- recognition gap remains large
- ignition is approaching
- shareholder capture is strong
- capital efficiency is improving
- permanent impairment risk is manageable

### Maintain
Prefer when:

- remaining opportunity remains superior
- confirmation is stable/improving
- fundamentals support valuation
- no materially superior alternative exists

### Reduce
Consider when:

- potential remains but confirmation weakens
- recognition gap compresses rapidly
- valuation outruns fundamentals
- capital requirements increase
- shareholder capture deteriorates
- another opportunity becomes materially superior

### Harvest / Rotate
Prefer when:

- remaining opportunity falls below alternatives
- recognition is substantially complete
- valuation materially outruns fundamental trajectory
- catalyst is realized and future catalysts are weak
- thesis probability falls materially
- permanent impairment risk increases

### Hold despite price decline
Possible when:

- potential remains high
- confirmation remains intact
- fundamentals are improving
- recognition gap remains large
- decline is recoverable volatility rather than thesis impairment

### Sell despite profit
Possible when:

- remaining opportunity has materially fallen
- superior opportunity exists
- thesis has matured
- valuation has outrun fundamentals
- capital efficiency has deteriorated

---

## 14. Replacement Hurdle

An existing holding has a structural advantage: its thesis has already earned capital.

Therefore a new opportunity should not replace it because of a small ranking difference.

Require a **replacement hurdle**:

```text
Candidate advantage
−
transaction costs
−
tax friction where applicable
−
liquidity / execution friction
−
uncertainty penalty
−
concentration impact
>
minimum rotation threshold
```

The threshold should widen when:

- evidence is weak
- liquidity is poor
- taxes are high
- portfolio concentration is high
- thesis fragility is high

The threshold can narrow when:

- confirmation is rapidly accelerating
- catalyst is near
- opportunity differential is large
- current thesis is deteriorating
- permanent impairment risk is rising

---

## 15. Opportunity Lifecycle

```text
DISCOVERY
   ↓
POTENTIAL IDENTIFIED
   ↓
VALIDATION
   ↓
CONFIRMATION ACCELERATES
   ↓
IGNITION APPROACHES
   ↓
IGNITION
   ↓
RECOGNITION
   ↓
VALUATION / THESIS MATURITY
   ↓
HARVEST
   ↓
ROTATION
   ↓
NEW OPPORTUNITY
```

Do not assume every opportunity completes the lifecycle.

Many should terminate early through:

- failed demand
- failed bottleneck capture
- backlog deterioration
- poor conversion
- financing failure
- dilution
- margin failure
- FCF failure
- catalyst failure
- recognition without fundamental confirmation

---

## 16. Evidence Quality Rules

Evidence hierarchy should generally favor:

1. audited financial results
2. regulatory filings
3. funded/definitized contracts
4. customer disclosures
5. repeated operating metrics
6. company guidance
7. industry data
8. management commentary
9. analyst estimates
10. narrative/social discussion

Lower-quality evidence can initiate investigation but should not be treated as equivalent to financial confirmation.

Independent evidence streams should be preferred over repeated versions of the same claim.

---

## 17. Anti-Chasing Rules

The OSE must prevent recognition from masquerading as opportunity.

Do not increase solely because:

- price rose sharply
- volume exploded
- social attention increased
- analysts upgraded after a large move
- a stock broke out without fundamental improvement

Instead ask:

> **Did the economic opportunity improve faster than the market price?**

If price recognition is outrunning fundamental improvement, remaining opportunity may be falling even while momentum rises.

---

## 18. Anti-Value-Trap Rules

Do not interpret a large recognition gap as automatically bullish.

A large gap can exist because:

- fundamentals are deteriorating
- demand is weak
- bottleneck control is false
- backlog is low quality
- contracts are unfunded
- margins cannot scale
- financing requirements are destructive
- dilution overwhelms growth
- catalyst probability is falling

Therefore:

**Recognition Gap requires Potential + Confirmation analysis.**

---

## 19. Decision Output to CAC

For each opportunity output a compact state card:

```text
OPPORTUNITY STATE CARD

Company:
Price:
Position:

Potential: P0–P5
Confirmation: C0–C5
Confirmation Velocity: ↑↑ / ↑ / → / ↓ / ↓↓
Fundamental Velocity: ↑↑ / ↑ / → / ↓ / ↓↓
Ignition: I0–I5
Recognition: R0–R7
Recognition Gap: Low / Medium / High / Extreme
Profitability Transmission: STRONG / ADEQUATE / FRAGILE / BLOCKED / UNKNOWN
Normalized Earnings Bridge: CLEAN / PARTIAL / DISTORTED / UNKNOWN
Sector Regime: SUPPORTIVE / NEUTRAL / ADVERSE / UNKNOWN
Return Failure State: RF0-RF4
Remaining Opportunity: Low / Medium / High / Exceptional
Time to Catalyst:
Time to Maturity:
Shareholder Capture:
Capital Efficiency:
Permanent Impairment Risk:
Confidence:

Current State:
Previous State:
State Direction:

Best Evidence:
Weakest Link:
Next Trigger:
Invalidation:
CAC Action: HOLD / INCREASE / REDUCE / HARVEST / ROTATE
```

---

## 20. Required CAC Interaction

OSE must run before final allocation decisions.

Pipeline:

```text
MARKET / FUNDAMENTAL EVENT
        ↓
XYOOL COMPANY STATE UPDATE
        ↓
OPPORTUNITY STATE ENGINE
        ↓
POTENTIAL × CONFIRMATION
        ↓
IGNITION + RECOGNITION
        ↓
REMAINING OPPORTUNITY
        ↓
OPPORTUNITY DIFFERENTIAL
        ↓
CAPITAL ALLOCATION CONTROLLER
        ↓
HOLD / INCREASE / REDUCE / HARVEST / ROTATE
```

CAC owns capital decisions.

OSE owns dynamic opportunity-state representation.

Company-level Xyool owns causal business analysis.

These layers must remain separate.

---

## 21. Backtest Requirements

OSE must be tested with point-in-time information.

At each historical decision date:

1. freeze all available information;
2. construct potential state;
3. construct confirmation state;
4. calculate state velocities using only prior observations;
5. assign ignition and recognition states;
6. calculate remaining opportunity;
7. pass state to CAC;
8. record allocation;
9. reveal only subsequent information;
10. update states;
11. record state transitions;
12. record rotation decisions.

Never use future outcomes to assign historical confirmation.

Required comparisons:

- buy/hold
- Xyool identification only
- Xyool + Ignition
- Xyool + OSE
- Xyool + OSE + CAC

Primary question:

> **Does dynamic Potential × Confirmation state tracking improve capital compounding and rotation decisions beyond static opportunity ranking?**

Secondary questions:

- Does OSE identify inflection states before large repricing?
- Does it reduce premature rotation?
- Does it reduce chasing after recognition?
- Does it identify thesis deterioration earlier?
- Does it improve capital allocation efficiency?
- Does it reduce permanent impairment?
- Does it improve return/drawdown?

---

## 22. Core Principle

> **Do not ask only how good the opportunity is. Ask what state the opportunity is in, which direction it is moving, how quickly the evidence is confirming it, and how much opportunity remains.**

The highest-value Xyool state is not simply a high score.

It is:

> **Large remaining potential + rapidly increasing confirmation + accelerating fundamentals + approaching ignition + incomplete recognition + manageable resistance.**

That state is what CAC should compete hardest to own.
