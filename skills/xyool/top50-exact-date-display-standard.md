# Xyool — Top-50 Human Display / Timing / Profit View Standard

Status: **CANONICAL OUTPUT / PRESENTATION REQUIREMENT**

## Purpose

Top-50 output must be fast for a human to scan without hiding the timing, quality, catalyst, probability, or expected stock-price consequence that drives capital allocation.

The default human-facing Top-50 timing output uses **two complementary lists**, not one mixed timing table:

```text
A. SINGLE-DATE TIMERS
Date | Stock | Q | Timer Type | Catalyst | Happens? | Profit View

B. PRE-CATALYST WINDOWS
~Window | Stock | Q | Catalyst | Happens? | Profit View
```

The two lists answer different questions:

- **Single-Date Timers** show verified exact event dates and explicit dated company targets/deadlines.
- **Pre-Catalyst Windows** show the evidence-supported interval in which a material catalyst can reasonably form, arrive early, or progress enough to justify active monitoring / exposure consideration.

A company may appear in **both** lists. This is intentional. A dated regulatory deadline, scheduled launch, hearing, earnings date, or target does not prove that the economically meaningful event must wait until that day.

Do not add extra default columns merely because the underlying model tracks more fields. Internal fields remain available for drill-down and audit.

---

## 1. Quality display: Q1-Q5

Translate the current stock Quality state into a compact human-facing scale:

```text
Q5 = highest quality / strongest quality state
Q4 = strong quality
Q3 = acceptable / investable quality
Q2 = weak / conditional quality
Q1 = poor / blocked quality
```

Legacy display mapping:

```text
HQ      -> Q5
Q+      -> Q4
Q       -> Q3
Q / W   -> Q2
W+      -> Q2
W       -> Q1
W / F   -> Q1
```

Append `↑` when the current Quality state is explicitly improving.

Examples:

```text
Q3↑
Q2↑
```

Keep the native/internal Quality state in the audit record. The Q1-Q5 display is a human-facing compression, not a replacement for the underlying qualifier logic.

---

## 2. Date / Window rule

The main table does **not** show a synthetic expected single day when no exact day is known.

Use this hierarchy:

```text
VERIFIED EXACT DATE
→ VERIFIED COMPANY TARGET / DEADLINE
→ COMPANY-GUIDED WINDOW
→ XYOOL-INFERRED ~WINDOW
```

### Exact dates

When a current exact date is verified, show it prominently:

```text
Dec 17 EXACT
```

For an exact company target/deadline that is not a guaranteed stop-event date:

```text
Sep 30 TARGET
```

### Non-exact timing

If there is no exact date, show the best supported **window**.

If the window is directly company-guided, preserve that window.

If Xyool must infer or extend the window from causal stage, same-company history, procurement/deployment cadence, regulator/customer process, or comparable situations, prefix the display with `~`:

```text
~Oct-Nov 2026
~Q4 2026
~Q4 2026-Q1 2027
~H1 2027
```

### Two-list sorting rule

Both timing lists are ordered for **human actionability**, not TTC capital rank.

#### A. Single-Date Timers

Sort:

```text
1. nearest unresolved calendar date first
2. within the same date: higher Quality first (Q5 -> Q1)
3. then higher TTC priority / remaining Profit View only as a tertiary tie-break
```

Keep timing identity visible:

```text
EXACT = verified stop/event date
TARGET = explicit company/regulator/customer dated target or deadline that may resolve before or after the date
```

A `TARGET` must never be silently upgraded to `EXACT`.

#### B. Pre-Catalyst Windows

Sort:

```text
1. earliest active / approaching window first
2. if windows overlap materially, earlier expected economic-conversion zone first
3. within the same time bucket: higher Quality first (Q5 -> Q1)
4. then higher TTC priority / remaining Profit View only as a tertiary tie-break
```

Suggested human time buckets:

```text
ACTIVE NOW
NEXT 30 DAYS
31-60 DAYS
61-90 DAYS
>90 DAYS / BROAD
```

The displayed `~window` remains the actual evidence-supported range; the bucket is only a sorting aid.

### Pre-catalyst window is a first-class timer

The pre-catalyst window is not a decorative estimate and is not merely the midpoint around a future headline.

It is the interval in which:

```text
causal evidence is sufficiently mature
+ the unresolved event can reasonably occur or materially advance
+ recognition is not fully consumed
+ Xyool should actively monitor ownership / staging / harvest decisions
```

For an exact-date event, the pre-catalyst window may begin before the exact day and may end when the event resolves early.

For an unscheduled event, the pre-catalyst window is the primary human timing object and must be built from causal state, PFS/Hazard, company/process evidence, and the established window hierarchy.

**RARE lesson:** an FDA PDUFA date can be a valid dated timer while the decision resolves before that date. Therefore a dated timer cannot substitute for a pre-catalyst ownership/monitoring window.

---
### No naked `?` in Top-50 human output

The Top-50 display should not use a naked `?` for timing.

If evidence is weak, widen the inferred range until it honestly represents the uncertainty and mark it with `~`. Low timing confidence belongs in the internal/audit record.

The inferred window must still have an evidence basis. Do not invent narrow precision from intuition.

---

## 3. Window construction hierarchy

For unresolved events without a verified exact date, construct the window from the strongest available evidence in this order:

1. company-guided range;
2. contractual / regulatory outer bound;
3. current causal stage plus management guidance;
4. same-company historical transition timing;
5. same-customer / same-process timing;
6. close process / regulator / procurement analogs;
7. cross-company event-class analogs;
8. cadence inference;
9. broad event-class prior as the last resort.

The weaker the evidence, the broader the displayed `~window` should be.

Never create a precise day by mechanically taking the midpoint of a month or quarter.

---

## 4. Catalyst column

The Catalyst column should show the economically relevant unresolved path, not merely the nearest headline.

### Single-event catalyst

Examples:

```text
FDA decision — relacorilant
first launch
contract award
```

### Cascade / dependency-chain catalyst

When value is unlocked through linked gates, show the dependency chain compactly and mark the current primary gating node when one is designated:

```text
SAT [GATE] -> acceptance -> procurement -> deployment
capacity [GATE] -> utilization -> revenue
qualification [GATE] -> shipments -> ramp
Belrise JV [GATE] -> C.M. close -> localization -> funded orders
```

Use `[GATE]` only when the node is a verified unresolved frontier gate under `ttc-dependency-chain.md`. Do not mark a downstream blocked node as the current gate.

The visible chain should stop once additional downstream steps no longer materially affect the displayed timing/profit window.

This keeps the default Top-50 table compact without adding another column, while still exposing the dependency structure that controls the current catalyst path.

---

## 5. Happens?

`Happens?` is the human-facing catalyst-success field.

For a single event, it means:

> **How likely is the economically favorable / value-producing outcome?**

For a cascade, it means:

> **How likely is meaningful value-producing progression through the displayed cascade during the displayed window?**

It does **not** require every final downstream gate to complete inside the window.

Default qualitative labels:

```text
HIGH
MEDIUM-HIGH
MEDIUM
MEDIUM-LOW
LOW
```

Use numeric percentages only when Xyool has earned the calibration. Do not expose `P(Hit)` notation in the default human-facing table.

---

## 6. Profit View

`Profit View` means the **probable stock-price move from the current price across the displayed catalyst/window**.

It is not:
- a long-term valuation target;
- the theoretical best-case upside;
- raw `P(Material Price Move | Hit)`;
- a simple sum of every possible headline reaction.

Profit View should incorporate the underlying profitability evidence, including where applicable:

```text
catalyst-success probability
price-response probability
move-size analogs
economic materiality
recognition already consumed
shareholder / per-share capture
failure or delay downside
payoff persistence
liquidity / exit friction
```

Display as an approximate range:

```text
~+12-25%
~+20-45%
```

For binary or materially asymmetric events, show both sides:

```text
~+25-45% / -35-50%
```

Numeric ranges remain provisional unless a validation file explicitly promotes the calibration.

---

## 7. Cascade-aware Profit View

A cascade must not be valued as one isolated headline and must not be valued by naively adding independent event reactions.

For a chain such as:

```text
GATE 1 -> GATE 2 -> GATE 3 -> ECONOMIC REALIZATION
```

model later steps conditionally:

```text
P(Gate 2) = P(Gate 1) x P(Gate 2 | Gate 1)
P(Gate 3) = P(Gate 2) x P(Gate 3 | Gate 2)
```

Estimate each gate's **incremental** new information / economic recognition, then construct one cumulative probable price-move range for the displayed window.

Rules:

1. Do not double-count the same economics at multiple gates.
2. Do not assume correlated gates are independent.
3. A realized upstream gate may raise the probability of downstream gates; update the cascade when that happens.
4. Distinguish a technical/operational milestone from the later profit-producing gate.
5. The displayed window should cover the material cluster of linked gates being valued.
6. If the cascade extends far beyond the useful capital horizon, truncate the display at the economically relevant stop event and start a new timer later.

Example:

```text
WYFI
Window: ~Nov-Dec 2026
Cascade: NC-1 / Paris -> BaseTen -> Iceland -> utilization -> revenue
Profit View: cumulative probable move across that cascade window, not just the first activation headline
```

---

## 8. Internal fields remain separate

The simplified display does not delete underlying fields.

Keep internally/auditably where applicable:

```text
Exact Date
Expected / Inferred Window
Timing Type
Timing Confidence
Timing Basis
Capital Status
Native Quality State
P(Hit)
P(Material Price Move | Hit)
Conditional Upside
Basic / Fully Diluted Equity Value
25% / 50% / 100% Repricing Burden
Minimum Viable Catalyst
Dynamic Dilution State
Reverse-Split / Listing Timer
Failure / Delay Downside
Already-Priced State
Recognition Gap
Analog Set
Cascade Gate Dependencies
Next Chronological Event
Next Profit-Producing Event
```

`Priced In`, `Stock Cares?`, and repricing-burden fields are not default table columns because their effects should already be reflected in `Profit View`. Internally, `Profit View` must be sensitive to the event's shareholder-capturable economics relative to the current/fully diluted equity denominator. A reverse stock split is not itself economic upside and should not inflate `Profit View`.

---

## 9. Realized / delayed / superseded events

When a catalyst realizes, is delayed, or is superseded:

1. close the old timing object;
2. mark the old state `REALIZED / CLOSED`, `DELAYED`, or `SUPERSEDED` internally;
3. remove stale upcoming dates;
4. advance to the next causal gate or cascade segment;
5. rebuild the Date / Window and Profit View;
6. record material timing or move-range misses for calibration.

Do not keep awarding catalyst proximity to an event that already happened.

---

## 10. Capital ranking versus timing-list order

The Top-50 **capital ranking** and the two **timing-list orders** are intentionally different views.

Capital ranking remains governed by Quality eligibility, TTC profitability priority, causal timing, downside/delay, current-holding replacement rules, recognition, and Quant where executable.

Timing-list order is:

```text
TIME FIRST
-> QUALITY SECOND
-> TTC / remaining Profit View as tertiary tie-break
```

Therefore:

- a close date does not automatically deserve more capital;
- a lower-quality name can appear earlier on the calendar without outranking a later high-quality opportunity for capital;
- a Q1/Q2 control remains visible in chronological order but remains blocked/conditional for normal capital;
- the same company may appear in both the single-date and pre-catalyst-window lists.

The timing views answer **what requires attention first**. TTC answers **where capital deserves to be**.

---

## 11. Canonical human-facing output

Use two sections.

### A. Single-Date Timers

```text
Date | Stock | Q | Timer Type | Catalyst | Happens? | Profit View
```

Chronological first; Quality second within the same date.

### B. Pre-Catalyst Windows

```text
~Window | Stock | Q | Catalyst | Happens? | Profit View
```

Earliest/active window first; Quality second within the same time bucket.

Example structure:

```text
SINGLE-DATE TIMERS
Dec 17 | CORT | Q3 | EXACT | FDA decision — relacorilant | MEDIUM-HIGH | ~+25-45% / -35-50%

PRE-CATALYST WINDOWS
~Oct-Dec 2026 | CODA | Q5  | SAT -> acceptance -> procurement -> deployment | MEDIUM-HIGH | ~+18-35%
~Nov-Dec 2026 | WYFI | Q2↑ | capacity -> utilization -> revenue | MEDIUM-HIGH | ~+20-45%
```
## Core rule

> **Maintain two timing views. Put dated timers in chronological order and pre-catalyst windows in earliest-window order; within the same time bucket, put higher Quality first. Do not let an exact date erase the pre-catalyst window, because material events can resolve early. Use TTC separately for capital priority.**
