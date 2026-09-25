# Xyool — TTC Insider Activity Context

Status: **CANONICAL CLASSIFICATION INPUT; DIRECTIONAL WEIGHTING PROVISIONAL**

## Core purpose

Insider activity can matter near a catalyst, but raw selling volume is not a valid signal by itself.

TTC must first classify **why and how** the transaction occurred before using it as evidence for catalyst probability, recognition, downside, or confidence.

Short form:

> **Insider sale != bearish signal until transaction context is classified.**

This module supplements `time-to-catalyst.md` and `ttc-catalyst-profitability.md`. It has no independent capital authority.

---

## 1. Mandatory catalyst-window insider check

For every material catalyst with a defined date/window, inspect recent insider filings and record:

```text
Ticker / Company:
Catalyst / Program:
Catalyst Date / Window:
Insider Name / Role:
Form Type: Form 4 / Form 144 / other
Transaction Date:
Transaction Type:
Shares / Value:
Ownership Before / After where available:
10b5-1 Flag:
Plan Adoption Date:
Plan Modification / Termination Date if disclosed:
Plan Aggregate Share Authorization where disclosed:
Tax-Withholding / Sell-to-Cover Flag:
Option Exercise Flag:
Gift / Transfer Flag:
Clustered Insider Activity?:
Source / Filing Date:
Interpretive State:
Confidence:
```

A catalyst ranking is incomplete if material insider activity is visible in the event window but not classified.

---

## 2. Transaction classes

### A. Discretionary open-market purchase

Potentially informative positive evidence when:
- personally funded;
- meaningful relative to prior ownership / compensation;
- not merely an automatic plan execution;
- not offset by larger contemporaneous sales;
- clustered across multiple knowledgeable insiders.

Do not treat one token purchase as decisive.

### B. Discretionary open-market sale

Potentially informative negative evidence when:
- not under a pre-arranged plan;
- meaningful relative to the insider's holdings;
- unusual versus prior selling cadence;
- clustered across multiple insiders;
- occurs inside a material catalyst window;
- not explained by taxes, liquidity, estate planning, or option mechanics.

A discretionary sale can reduce TTC confidence or widen downside assumptions, but it does not automatically invalidate a catalyst.

### C. Rule 10b5-1 pre-arranged sale

Normally **lower informational value at execution** because the timing/instructions were established earlier.

Required interpretation fields:
- adoption date;
- modification date if any;
- first eligible trade / disclosed execution window where available;
- plan size relative to insider ownership;
- number of prior executions under the same plan;
- whether the plan substantially predates the catalyst;
- whether the plan was adopted when the catalyst was already public/known;
- whether multiple insiders adopted similar plans around the same period;
- whether the plan was later modified, accelerated, cancelled, or terminated.

Do not ignore 10b5-1 activity. Instead ask:

> **What information was public and what catalyst state existed when the plan was adopted?**

The adoption date can be more informative than the execution date.

### D. Tax-withholding / sell-to-cover transaction

Usually low-information / mechanical.

Treat as neutral unless surrounding facts make the transaction unusual.

### E. Option exercise followed by sale

Classify separately.

Ask:
- was exercise required by expiration?
- how much stock was retained?
- was the sale 10b5-1 planned?
- was it only to fund exercise/taxes?

Exercise-and-hold can differ materially from exercise-and-immediate-liquidation.

### F. Gift / estate / trust transfer

Usually not directional for TTC without additional evidence.

---

## 3. 10b5-1 interpretation rule

A pre-arranged plan must not be treated as equivalent to a discretionary decision made immediately before a catalyst.

Use three timestamps:

```text
PLAN ADOPTION
PLAN MODIFICATION / TERMINATION
TRADE EXECUTION
```

The key research question is:

> **Did the insider make a discretionary planning decision at a time when the material catalyst state was already visible?**

A trade executed near a catalyst can be low-information if the plan was adopted months earlier.

Conversely, repeated new plan adoptions or material modifications by multiple insiders while a major catalyst is already visible may deserve more scrutiny than routine executions under long-standing plans.

Do not infer misconduct or possession of nonpublic information from timing alone.

---

## 4. Insider Context State

Use qualitative states until calibration is validated:

```text
POSITIVE
NEUTRAL / MECHANICAL
LOW-INFORMATION PLANNED SELLING
CAUTION
MATERIAL NEGATIVE CONTEXT
UNKNOWN / INCOMPLETE
```

Examples:

- small 10b5-1 execution from a months-old plan -> LOW-INFORMATION PLANNED SELLING
- automatic sell-to-cover for RSU taxes -> NEUTRAL / MECHANICAL
- multiple large discretionary sales by CEO/CFO before an unresolved catalyst -> CAUTION or MATERIAL NEGATIVE CONTEXT depending facts
- meaningful discretionary open-market purchases by multiple insiders -> POSITIVE

No state is a standalone BUY/SELL rule.

---

## 5. Interaction with catalyst profitability

Insider context can update:
- catalyst confidence;
- failure/downside range;
- recognition assumptions;
- shareholder-capture confidence;
- research priority;
- the need for additional diligence.

It should not mechanically alter `P(Hit)` unless there is a causal reason.

Examples:
- a tax sale should normally have no effect on P(Hit);
- a long-planned 10b5-1 sale should normally have little effect on P(Hit);
- unusual discretionary clustered selling may justify lower confidence or a wider downside range, but calibration must be evidence-based.

---

## 6. False-positive guards

Do not:
- count every Form 4 sale as bearish;
- count every insider purchase as bullish;
- treat execution date as the only relevant date for 10b5-1 transactions;
- ignore plan adoption / modification history;
- confuse sell-to-cover with discretionary selling;
- compare gross share counts without considering ownership size;
- infer intent or illegal behavior from transaction timing alone;
- double-count the same transaction across Form 4 and Form 144.

---

## 7. Miss-to-question rule

This module is a direct application of `miss-to-question-learning-loop.md`.

Generalized mandatory question:

> **What insider transactions occurred inside or near the catalyst window, what caused them, and how informative are they after classification?**

The system lesson is not "insider selling before a catalyst is bad."

The transferable lesson is:

> **Catalyst analysis is incomplete when visible insider behavior is not classified by transaction mechanism and planning date.**

---

## 8. Validation boundary

Promote now as canonical process:
- mandatory insider-activity check for material catalyst windows;
- transaction-type classification;
- separate 10b5-1 adoption / modification / execution dates;
- sell-to-cover / tax-sale identification;
- anti-double-counting across Form 4 / Form 144;
- qualitative insider context state.

Keep provisional:
- any numeric insider multiplier;
- universal bearish weight for discretionary sales;
- universal bullish weight for insider purchases;
- fixed lookback window;
- fixed thresholds for transaction size.

Future testing should compare catalyst outcomes and abnormal returns across classified insider states with strict anti-lookahead and negative controls.