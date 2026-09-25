# FLOW — Stock Quality Credentials

FLOW ID: `STOCK-QUALITY-CREDENTIALS-V1`  
STATUS: **ACTIVE / CANONICAL**  
DOMAIN: stock-market  
JOB: identify stocks with the strongest credentials and potential before deeper thesis work
AUTHORITY: Quality qualification and normal-capital eligibility only; no TTC capital-priority, sizing, strategy-selection, or execution authority
PARENT GOALPOST: supplied by STOCK-COMPANY-ANALYSIS or calling stock pipeline
UPSTREAM FLOWS: company-analysis, discovery/evidence intake, evidence-to-state
DOWNSTREAM FLOWS: company-analysis, TTC/dependency analysis, narrative-thesis, meta audit
INBOUND PIPES: `../PLUMBING.md#pipe-stock-discovery-quality`
OUTBOUND PIPES: `../PLUMBING.md#pipe-stock-quality-ttc`
SOFTWARE DEPENDENCIES: none by default

## GOAL

Answer one simple question:

> **Does this stock have enough quality/potential credentials to deserve deeper capital/thesis analysis?**

Quality is an upstream qualification layer.

It does not need to explain the entire stock story.

## CORE IDEA

Quality is the company's **credentials**.

Those credentials should indicate:
- there is something economically real;
- the company can capture/control enough of it;
- evidence supports the transition;
- the company can survive to the unlock;
- common shareholders can plausibly benefit;
- the potential reward is meaningful relative to risk.

## CREDENTIALS

### 1. REAL DEMAND
Is there credible demand, customer need, adoption, procurement pull, clinical need, or another real economic reason for the company/product to exist?

### 2. CONTROL / CAPTURE
Does the company actually control, own, contractually capture, or economically participate in the value?

### 3. STRUCTURAL PROOF
Is there evidence beyond narrative?

Examples:
- contracts;
- approvals;
- funded programs;
- recurring customers;
- validated technology;
- production qualification;
- operating traction;
- ownership/control rights.

### 4. CONVERSION
Is the opportunity converting toward:

```text
revenue
cash
margin
backlog
royalties
asset value
contract value
shareholder value
```

or is it still mostly optionality/story?

### 5. FINANCING / SURVIVAL
Can the company survive long enough to reach the unlock without destroying shareholder capture?

Consider:
- cash/runway;
- debt;
- dilution;
- working capital;
- financing access;
- listing risk;
- capital intensity.

### 6. SHAREHOLDER CAPTURE
If the business succeeds, do common shareholders actually benefit?

### 7. ASYMMETRY / POTENTIAL
Is the plausible economic upside meaningful relative to:
- current enterprise/equity value;
- dilution burden;
- downside;
- time required;
- probability of reaching the unlock?

### 8. TRAJECTORY
Is Quality:

```text
IMPROVING
STABLE
DETERIORATING
BINARY-DEPENDENT
UNKNOWN
```

### 9. UNLOCK
What specific event/state would materially improve Quality?

### 10. SURVIVAL TO UNLOCK
Can the company plausibly reach that unlock?

```text
PASS
WATCH
FAIL
UNKNOWN
```

## OUTPUT

Keep the output simple:

```text
QUALITY: FAIL / WATCH / QUALIFIED / HIGH QUALITY

STRONGEST CREDENTIALS:
- ...

WEAKEST CREDENTIALS:
- ...

QUALITY TRAJECTORY:

QUALITY UNLOCK:

SURVIVAL TO UNLOCK:

POTENTIAL:
LOW / MODERATE / HIGH / VERY HIGH

WHY THIS STOCK DESERVES OR DOES NOT DESERVE DEEPER WORK:
```

## RANKING USE

When screening many stocks, Quality should prioritize those with the strongest combination of:

```text
CREDENTIAL STRENGTH
+ POTENTIAL
+ IMPROVING TRAJECTORY
+ SURVIVAL TO UNLOCK
+ SHAREHOLDER CAPTURE
```

Do not turn this into a complicated universal numeric score unless evidence proves that one is better.

## RELATION TO STORY / THESIS

Quality asks:

> **Is this worth investigating deeply?**

The Narrative Thesis asks:

> **What is actually happening, what is likely to happen next, and when?**

Therefore:

```text
QUALITY CREDENTIALS
→ select / qualify
→ DETECTIVE STORY
→ THESIS
→ WINDOW
→ PAYOFF
→ TA / EXPRESSION
```

## DISCOVERY BOUNDARY

A weak current Quality score may not erase a hidden-transition stock from research visibility.

Discovery can keep a stock visible when a credible Quality unlock exists.

Quality controls normal capital eligibility, not whether Xyool is allowed to notice the stock.

## SOFTWARE / HARD-LIMIT BOUNDARY

`NONE — FLOWARE SUFFICIENT`