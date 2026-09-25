# Xyool — Discovery Visibility Gate

Status: **CANONICAL PRE-QUALITY DISCOVERY PROCESS / NO INDEPENDENT CAPITAL AUTHORITY**

## Purpose

Prevent Xyool from hiding high-upside transition stocks before Quality has a chance to evaluate them.

A current low-Quality state must not erase a stock from research visibility when public breadcrumbs show a specific, economically meaningful transition that could materially improve the company's future economics or shareholder capture.

Core distinction:

> **Discovery visibility asks whether a stock deserves research attention. Quality asks whether it deserves normal capital now.**

These are not the same question.

---

## Search-entry architecture

Candidate generation must use a union.

SEC filing memory is a canonical source for both sides of the union. An insider-origin, strategic-owner, operating-transition, or financing-risk filing may create research visibility before Quality is known.

Candidate generation must use:

```text
ESTABLISHED-QUALITY SCREEN
          \
           +--> VISIBLE RESEARCH CANDIDATES
          /
HIDDEN-TRANSITION BREADCRUMB SCREEN
```

Then:

```text
VISIBLE CANDIDATES
→ CURRENT QUALITY
→ QUALITY TRAJECTORY
→ QUALITY UNLOCK CONDITION
→ SURVIVAL TO UNLOCK
→ TTC / PROFITABILITY
→ CAPITAL AUTHORITY
```

Never use current Quality as the sole pre-filter for research visibility.

---

## Discovery lanes

Every newly surfaced stock should be classified into one or more lanes.

### ESTABLISHED_QUALITY

The company already shows enough operating/shareholder quality to justify a full Quality review even without a special hidden-transition signal.

Typical evidence:
- real revenue / margins / cash conversion;
- durable funded backlog or recurring economics;
- balance-sheet durability;
- bounded dilution;
- strong shareholder capture;
- reasonable valuation/asymmetry.

### HIDDEN_TRANSITION

Current Quality may be weak, incomplete or blocked, but public evidence suggests a specific causal transition that could materially improve economics.

Required:
1. a specific causal breadcrumb;
2. a named transition;
3. an economically relevant stop event;
4. a falsifiable confirmation/invalidation path;
5. a plausible chain from the transition to shareholder value.

Examples:
- testing → qualification → production;
- strategic agreement → transaction close → consolidation → orders;
- repeat production orders → delivery → revenue;
- funded capacity → activation → recurring revenue;
- regulatory decision → launch → adoption.

### BOTH

The stock already has acceptable current Quality and also contains a strong hidden/forward transition.

This is often the most interesting discovery state because it combines present survivability with unrecognized forward conversion.

### RISK_ONLY

A negative breadcrumb exposes financing, dilution, customer loss, delay or another hazard but does not create a positive hidden-opportunity path.

Keep for risk/watch purposes where relevant. Do not promote as a hidden-upside candidate solely because something is changing.

---

## SEC-origin discovery

Canonical source process:
- `skills/xyool/sec-filing-company-memory.md`

SEC-origin lanes may include:

```text
INSIDER_ORIGIN
HIDDEN_TRANSITION
STRATEGIC_OWNER
RISK_ONLY
```

A true open-market insider purchase may originate a research candidate even before an operating breadcrumb is known. The next required question is then:

> **Why is the insider buying now, and is there an independent causal/economic transition that explains the timing?**

Insider-origin discovery has no independent capital authority.

## Pre-Quality visibility test

A stock is **DISCOVERY_VISIBLE** when either lane is satisfied:

```text
ESTABLISHED_QUALITY_CANDIDATE
OR
HIDDEN_TRANSITION_CANDIDATE
```

A hidden-transition candidate must pass:

### 1. Transition test
Can the breadcrumb be expressed as a specific state change?

### 2. Delta test
Is the information actually new versus the prior state?

### 3. Agency / commitment test
Is a customer, regulator, supplier, government body or the company taking observable action?

### 4. Falsifiability test
What confirms or kills the interpretation?

### 5. Economic-link test
Can the stop event plausibly change orders, backlog, revenue, margin, cash, control or common-shareholder value?

### 6. Dependency-path test
Can Xyool name at least a provisional path from the breadcrumb to an economic terminal?

### 7. Survival-to-unlock precheck
Is it at least plausible that the company/security can survive to the unlock without clearly destroying common-shareholder capture first?

This is a visibility precheck, not a final Quality pass.

If survival is clearly impossible or the security cannot plausibly capture the economics, classify:

```text
VISIBLE_RISK / REJECT_HIDDEN_UPSIDE
```

rather than silently removing the evidence.

---

## Quality-transition fields

After a stock becomes visible, Quality must record both the current state and the transition state.

Required fields:

```text
CURRENT QUALITY:
QUALITY TRAJECTORY:
QUALITY UNLOCK CONDITION:
SURVIVAL TO UNLOCK:
POST-UNLOCK SHAREHOLDER-CAPTURE QUESTION:
DISCOVERY LANE:
```

### Quality trajectory

Allowed states:

```text
IMPROVING
STABLE
DETERIORATING
BINARY / DEPENDENT
UNKNOWN
```

This is descriptive research state, not independent capital authority.

### Quality unlock condition

The smallest observable set of events that could justify a materially better Quality state.

Examples:

```text
definitive JV
→ acquisition close
→ funded order
→ bounded dilution
```

or:

```text
customer qualification
→ production commitment
→ shipment/revenue proof
```

Do not promote Quality merely because an unlock path exists.

---

## Survival to unlock

A hidden opportunity is not economically useful if the common equity is likely to be impaired before the unlock arrives.

At minimum inspect:
- cash / runway;
- debt maturity / covenant pressure;
- ATM / shelf / convertibles / warrants / preferred stock;
- expected capex / working capital;
- reverse-split / listing pressure;
- dilution required to reach the next gate;
- transaction structure / security-class capture;
- time to unlock relative to financing runway.

Output:

```text
PASS
WATCH
FAIL
UNKNOWN
```

Rule:

> **Low current Quality may preserve research visibility, but Survival-to-Unlock FAIL prevents normal capital and should materially reduce hidden-opportunity priority.**

---

## What this changes

Old failure mode:

```text
BROAD UNIVERSE
→ QUALITY FILTER
→ low-quality stock disappears
→ breadcrumbs never analyzed
```

New process:

```text
BROAD UNIVERSE
→ ESTABLISHED-QUALITY SCREEN
  UNION
  HIDDEN-TRANSITION BREADCRUMB SCREEN
→ VISIBLE CANDIDATE SET
→ QUALITY + TRAJECTORY + UNLOCK + SURVIVAL
→ TTC
```

This preserves the protection of the Quality gate while preventing research blindness.

---

## What this does NOT change

Quality still owns normal capital eligibility.

A stock may therefore be:

```text
DISCOVERY VISIBLE: YES
HIDDEN TRANSITION: STRONG
CURRENT QUALITY: Q1 / WATCH / FAIL
QUALITY TRAJECTORY: IMPROVING
SURVIVAL TO UNLOCK: WATCH
CAPITAL STATUS: BLOCKED
```

There is no contradiction.

Likewise, a tiny repricing burden cannot rescue a blocked Quality case.

Breadcrumb strength may increase research priority. It may not directly authorize capital.

---

## Search behavior

When the user asks Xyool to:
- find hidden stocks;
- search for quality stocks;
- build or refresh the Top 50;
- find the next runner/catalyst setup;
- discover mispriced small caps;

the candidate search must include **both discovery lanes**.

Do not search only for already-profitable / already-clean companies.

The search should deliberately include public evidence containing causal verbs such as:
- testing;
- qualifying;
- selecting;
- ordering;
- expanding;
- funding;
- constructing;
- installing;
- activating;
- commissioning;
- repeating;
- replenishing;
- consolidating;
- closing;
- launching.

Then apply the breadcrumb six-test filter before escalating the candidate.

---

## Output requirement for discovered names

For any hidden-transition candidate show:

```text
Discovery Lane:
Breadcrumb:
Causal Transition:
Economic Terminal:
Current Quality:
Quality Trajectory:
Quality Unlock Condition:
Survival to Unlock:
Current Capital Status:
Next Research Question:
```

This makes the reason for visibility explicit even when capital remains blocked.

---

## Core rule

> **Quality may block capital. Quality may not, by itself, block discovery. A causal breadcrumb with a credible economic path must be visible long enough for Xyool to evaluate the Quality unlock and survival path.**
