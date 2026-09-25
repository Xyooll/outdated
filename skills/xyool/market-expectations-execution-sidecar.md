# Xyool — Market Expectations & Execution Sidecar

Status: **EXPERIMENTAL / TEST-ONLY**

## Purpose

External research suggests several signals may add information to Xyool's causal company analysis, but they must not be granted automatic voting power before independent validation.

This sidecar captures those signals in a separate state layer.

Core rule:

> Causal company evidence explains **why** economics may change. Market-expectation and execution signals help measure **whether that change is already being recognized, diffusing, or is even tradable**.

---

## 1. Expectations-diffusion state

Track where reliable point-in-time data exists:

```text
earnings_surprise_state
guidance_delta
estimate_revision_direction
estimate_revision_magnitude
revision_breadth
revision_persistence
estimate_dispersion
post_earnings_drift_state
coverage_count
expectations_data_quality
```

Interpretation:

```text
UPWARD REVISION BREADTH + POSITIVE SURPRISE + LOW/DECLINING DISPERSION
may indicate improving consensus economics and incomplete diffusion.

DOWNWARD REVISION BREADTH + NEGATIVE GUIDANCE
may strengthen an adverse branch.

NO / SPARSE COVERAGE
must not be treated as a negative signal.
```

For microcaps, analyst coverage may be too sparse for these fields to be reliable.

Do not convert PEAD or revisions directly into LONG/SHORT.

---

## 2. Factor-neutral recognition state

Track price confirmation separately from raw stock return.

Candidate fields:

```text
total_momentum
sector_relative_momentum
residual_momentum
idiosyncratic_return_trend
breadth_confirmation
recognition_acceleration
```

Residual momentum should remove, as data permits, broad market / sector / standard factor exposure before interpreting price confirmation.

Purpose:

```text
GOOD COMPANY + STRONG RAW RETURN
may only be sector/factor beta.

GOOD COMPANY + POSITIVE RESIDUAL MOMENTUM
may provide cleaner evidence that company-specific recognition is spreading.

GOOD COMPANY + NEGATIVE RESIDUAL MOMENTUM
should trigger recognition / profitability review,
not automatic thesis failure.
```

---

## 3. Factor-exposure decomposition

For validation, estimate whether returns are explained by common factors such as:

```text
market
size
value
profitability / quality
investment
momentum
sector / industry
```

Xyool should distinguish:

```text
COMPANY-CAUSAL ALPHA
from
COMMON FACTOR / SECTOR EXPOSURE
```

This is a validation and recognition aid, not a replacement for company analysis.

---

## 4. Execution / capacity state

For every candidate, and especially small/microcaps, track:

```text
bid_ask_spread
median_dollar_volume
position_as_pct_ADV
days_to_build
days_to_exit
estimated_slippage
estimated_market_impact
halt / gap risk
execution_state
```

Candidate classifications:

```text
EXECUTION_CLEAN
EXECUTION_COSTLY
EXECUTION_FRAGILE
EXECUTION_BLOCKED
UNKNOWN
```

Expected return must be compared with implementation cost.

---

## 5. Short-feasibility state

A negative thesis is not an executable short until borrow is modeled.

Track where available:

```text
borrow_available
borrow_fee
borrow_fee_trend
utilization
short_interest
days_to_cover
float
ownership_concentration
recent squeeze / gap behavior
locate_stability
short_feasibility_state
```

Classifications:

```text
SHORT_CLEAN
SHORT_EXPENSIVE
SHORT_CROWDED
SHORT_SQUEEZE_RISK
SHORT_BLOCKED
UNKNOWN
```

The short-side expected value must be net of borrow and squeeze/recall risk.

---

## 5A. Options-implied expected-move / IV-wall state

Track only as **experimental execution/timing evidence** until independent validation.

Candidate fields:

```text
iv_wall_reference_price
iv_wall_annualized_iv
iv_wall_coverage
iv_wall_horizon_sessions
iv_wall_lower
iv_wall_upper
iv_wall_interaction
iv_wall_range_contained
iv_wall_reaction_return
iv_wall_data_quality
```

Canonical V1 research baseline:

```text
z = NormalInvCDF((1 + coverage) / 2)
log_width = z * IV * sqrt(horizon_sessions / 252)
lower = reference_price * exp(-log_width)
upper = reference_price * exp(+log_width)
```

Interpretation:

```text
LOWER_TOUCH_RECLAIM
may support execution timing for an already-approved long/add.

UPPER_TOUCH_REJECT
may support deferring an add or auditing harvest timing.

BREAK_AND_HOLD
must not be forced into a fade.

BOTH_WALLS
is a range-failure / ambiguity state, not a successful reaction.
```

Critical statistical firewall:

```text
P(price range remains inside walls)
!=
P(profitable reaction | wall touched)
```

Range containment, conditional reaction rate, directional hit rate and net
signed return must be reported separately. A nominal 90% probability envelope
must never be described as a 90% strategy win rate.

V1 requires point-in-time options data for D3 status. Current-only option
snapshots are not enough for clean historical validation.

Authoritative research specification:
- `research/system-tests/2026-09-23-iv-wall-execution-sidecar-v1-spec.md`

Implementation:
- `agent/quant/iv_walls.py`
- Quant model `V09`

---

## 6. Small/micro-cap override

For low-liquidity or financing-dependent equities, the following can dominate an otherwise correct operating thesis:

```text
dilution
ATM / shelf usage
convertible / warrant overhang
cash runway
bid-ask spread
ADV / float
borrow availability
listing / reverse-split risk
market impact
```

For these names, shareholder capture and execution are not "portfolio details." They are part of the economic thesis.

---

## 7. Experimental test design

Do not rewrite the current profitability-control baseline.

For every fresh case, freeze two parallel arms before outcome reveal:

```text
ARM A — CURRENT XYOOL
TTC + profitability transmission + return failure

ARM B — CURRENT XYOOL + SIDECAR
+ expectations diffusion
+ factor-neutral recognition
+ execution / capacity
+ short feasibility where relevant
+ separately validated options-implied execution features where D3 data exists
```

Freeze all sidecar states and data-quality flags.

Then compare incremental value on the same cases.

Minimum questions:

1. Did revisions / PEAD improve recognition timing?
2. Did residual momentum prevent false "price ahead" or false "fundamentals ahead" calls?
3. Did execution costs eliminate nominally attractive microcap trades?
4. Did short-feasibility prevent unimplementable short calls?
5. Did factor adjustment show that apparent alpha was mainly sector/style exposure?
6. Did the added layer improve return **after costs** without excessive turnover or missed winners?
7. For V09 specifically, did conditional wall-reaction return survive after separating it from simple range containment?

---

## 8. Promotion standard

No sidecar feature becomes canonical capital logic because the literature says it works in aggregate.

Promotion requires:

- point-in-time implementability;
- independent frozen validation;
- incremental improvement over existing Xyool;
- realistic cost / borrow assumptions;
- robustness across more than one stock archetype;
- prospective shadow evidence when feasible.

Until then:

> **Measure it. Do not let it vote.**
