# Stock-Market Character Archetypes

Status: **CANONICAL DOMAIN VOCABULARY / PROVISIONAL ARCHETYPE DEFINITIONS**

Parent Flow:
floware/core/character-system.flow.md

## Purpose

This file provides a starter archetype vocabulary for stock-market characters.

It is not an exhaustive taxonomy.

Core rule:

> **Archetypes describe recurring structural/behavioral patterns. They are not boxes that every company must fit.**

A company may:
- express multiple archetypes at once;
- change archetypes as its state changes;
- remain UNCLASSIFIED;
- be HYBRID;
- require a newly proposed EMERGENT archetype.

Archetypes never replace the underlying quantitative and qualitative traits.

## Form is not condition

The archetype describes **what structural/behavioral form the character expresses**.

It does not say whether the form is:
- healthy;
- mature;
- progressing;
- stalled;
- deteriorating;
- Quality-eligible;
- attractive for capital.

Preserve separately:

```text
ARCHETYPE FORM
+ CHARACTER CONDITION
+ TRAJECTORY
+ QUALITY / CAPITAL STATE
```

Example:

```text
CAPACITY / INDUSTRIAL SCALE-UP OPERATOR
+ CONDITION = PROGRESSING
+ TRAJECTORY = IMPROVING
+ QUALITY = Q3

or

CAPACITY / INDUSTRIAL SCALE-UP OPERATOR
+ CONDITION = REMEDIATING
+ TRAJECTORY = MIXED
+ QUALITY = Q1 / BLOCKED
```

The archetype may be equally valid in both cases.

## Archetype record

For each candidate archetype, record:

~~~text
ARCHETYPE:
STATUS:
DEFINITION:
COMMON QUALITATIVE TRAITS:
COMMON QUANTITATIVE EVIDENCE:
COMMON TRANSFORMATIONS:
CONTRADICTIONS / ANTI-SIGNALS:
KNOWN FAILURE MODES:
~~~

Do not infer membership from one keyword or one metric.

## Starter archetypes

### PLATFORM ASSEMBLER

Definition:
Builds value by assembling multiple operating, technology, distribution, acquisition, or strategic branches into a broader platform.

Typical qualitative traits:
- dense relationship graph;
- several partially independent value branches;
- integration/control questions matter;
- story complexity exceeds any single product;
- value realization depends on coordination across characters.

Common transformations:
- Platform Assembler → Integrated Operator;
- Platform Assembler → Holding / Optionality Vehicle;
- Platform Assembler → Capital-Stressed Aggregator.

Anti-signals:
- one dominant mature operating engine with little dependency on acquisitions/partnerships.

### CAPITAL-DEPENDENT TRANSFORMER

Definition:
The intended business/state transition requires repeated external financing before the desired economics become self-sustaining.

Typical qualitative traits:
- financing is a first-class character in the story;
- survival and shareholder capture can diverge;
- operating progress may coexist with dilution;
- capital timing can dominate operating timing.

Common transformations:
- Capital-Dependent Transformer → Self-Funding Operator;
- Capital-Dependent Transformer → Dilutive Survivor;
- Capital-Dependent Transformer → Restructurer.

### SERIAL ACQUIRER / DEAL-DRIVEN TRANSFORMER

Definition:
Material state change is repeatedly pursued through acquisitions, investments, JVs, or other transactions.

Typical qualitative traits:
- transaction pipeline is part of strategy;
- control and consideration matter as much as target quality;
- integration and financing are recurring gates.

Anti-signal:
- acquisitions are incidental rather than a repeated mechanism.

### OPTIONALITY AGGREGATOR

Definition:
Accumulates multiple possible future value paths whose economics are individually uncertain or not yet fully converted.

Typical qualitative traits:
- many branches;
- high future-state dispersion;
- value often depends on a subset of branches converting;
- headline count can exceed realized economics.

Common transformation:
- Optionality Aggregator → Focused Operator when one branch becomes dominant and economically realized.

### NICHE OPERATOR

Definition:
Creates value primarily through an established focused operating capability rather than continual corporate transformation.

Typical qualitative traits:
- relatively stable core capability;
- direct customer/problem relationship;
- operating execution dominates transaction complexity.

### PROCUREMENT CONVERTER

Definition:
Has technically or operationally credible capability, with material value dependent on converting validation/acceptance into funded procurement and deployment.

Typical qualitative traits:
- acceptance and procurement are separate states;
- customer/process timing is important;
- technical proof may precede economic proof.

Common transformation:
- Procurement Converter → Repeat Program Operator.

### REPEAT-PROCESS OPERATOR

Definition:
A demonstrated customer/process cadence creates recurring or repeatable funded events.

Typical qualitative traits:
- same or similar customer process repeats;
- cadence/rhythm can become informative;
- each repeat still requires incremental-economics and recognition checks.

### BACKLOG CONVERTER

Definition:
Has already-contracted or backlogged economics whose value depends on execution converting that backlog into delivery, revenue, margin and cash while preserving or replenishing future backlog.

Typical qualitative traits:
- customer commitment is already more mature than a prospect/pipeline;
- execution/delivery quality matters more than merely winning the order;
- backlog composition, timing and margin matter;
- replenishment determines whether current conversion is durable.

Common transformations:
- Backlog Converter → Repeat Program Operator when replenishment becomes recurring;
- Backlog Converter → Mature Operator when backlog conversion becomes steady operating cadence;
- Backlog Converter → Backlog Eroder when delivery occurs without profitable replenishment.

Distinct from Procurement Converter:

```text
PROCUREMENT CONVERTER
validation / acceptance
→ funded award

BACKLOG CONVERTER
funded / contracted backlog
→ execution / delivery
→ revenue / margin / cash
```

Anti-signals:
- backlog is mostly unfunded/non-binding;
- the company is still waiting primarily for customer procurement rather than executing contracted work.

### CAPACITY / INDUSTRIAL SCALE-UP OPERATOR

Definition:
Has built, acquired, qualified, or is constructing productive capability whose value depends on converting that capacity into utilized throughput, volume, margin absorption and cash economics.

Typical qualitative traits:
- capability/capacity exists before full economic utilization;
- commissioning, readiness, yield, throughput or utilization are central;
- fixed-cost absorption or scale economics matter;
- capital intensity may be material but is not required.

Applicable examples can include:
- manufacturing;
- data-center/integration capacity;
- mining/material processing;
- satellite/physical infrastructure;
- industrial production.

Common transformations:
- Scale-Up Operator → Mature High-Utilization Operator;
- Scale-Up Operator → Rollout Engine when economics shift toward replicating deployments externally;
- Scale-Up Operator → Stranded-Capacity Operator when utilization/economics fail.

Distinct from Rollout / Deployment Engine:

```text
CAPACITY / INDUSTRIAL SCALE-UP
internal productive capability
→ utilization / throughput
→ unit economics / margin / cash

ROLLOUT / DEPLOYMENT
proven offering
→ repeated external sites / fleets / customers
→ scaled deployment economics
```

Anti-signals:
- spending/capex without a credible productive-capacity path;
- purely financial asset accumulation;
- growth driven mainly by acquiring unrelated entities rather than utilizing productive capacity.

### ROLLOUT / DEPLOYMENT ENGINE

Definition:
Value growth depends on scaling an already demonstrated offering across sites, facilities, fleets, customers, or geographies.

Typical qualitative traits:
- deployment count and economics matter;
- rollout cadence is central;
- expansion can be same-chain realization rather than new independent optionality.

### RECURRING-SERVICE / RENTAL OPERATOR

Definition:
A meaningful portion of value comes from recurring service, rental, subscription, usage, or installed-base economics.

Typical qualitative traits:
- persistence/renewal/utilization matter;
- installed-base growth can reduce dependence on single binary events;
- unit economics and retention are important.

### BINARY / GATED PROGRAM COMPANY

Definition:
A dominant value path depends on a small number of high-impact external gates or program decisions.

Typical qualitative traits:
- discrete decision points;
- large state change at resolution;
- ordinary operating cadence may be secondary.

### ASSET MONETIZER

Definition:
Value realization depends primarily on selling, licensing, harvesting, or otherwise monetizing existing assets rather than scaling a recurring operating engine.

### TURNAROUND / RESTRUCTURER

Definition:
The main story is repair of a damaged operating/capital state.

Typical qualitative traits:
- survival and balance-sheet repair are first-order;
- prior structure is not sustainable;
- success requires transition from deterioration to stable operation.

### HOLDING / OPTIONALITY VEHICLE

Definition:
Owns interests or claims on other characters while direct operating control/cash conversion is limited.

Typical qualitative traits:
- value is mediated through ownership stakes/rights;
- look-through economics and capture matter;
- parent story may differ substantially from investee stories.

## Archetype combinations

Combinations are expected.

Prefer composition over taxonomy expansion.

Before proposing a new archetype ask:

```text
CAN THE CHARACTER BE EXPLAINED BY:
existing archetype A
+ existing archetype B
+ raw qualitative traits
?
```

If yes, do not invent a new catch-all archetype.

A new archetype should normally require:
- a recurring structural pattern;
- more than one materially different positive case;
- a distinction that changes Story Reader/Writer behavior;
- meaningful anti-signals / negative controls.

Do not create industry archetypes merely because several companies share a sector.

Example:

~~~text
PLATFORM ASSEMBLER
+ CAPITAL-DEPENDENT TRANSFORMER
+ OPTIONALITY AGGREGATOR
~~~

is a valid hybrid profile when evidence supports all three.

Do not compress the combination into a single master score.

## Qualitative stock-character traits

The stock domain should preserve evidence-backed qualitative traits such as:

~~~text
CONTROL:
  HIGH / MIXED / LOW / UNKNOWN

CAPITAL DEPENDENCE:
  LOW / MODERATE / HIGH / CRITICAL

CONVERSION MATURITY:
  CONCEPT / VALIDATION / PROCUREMENT / DEPLOYMENT /
  RECURRING / MATURE / DECLINING / MIXED

RELATIONSHIP DENSITY:
  SPARSE / MODERATE / DENSE / COMPLEX

AGENCY:
  SELF-DIRECTED / SHARED / EXTERNALLY_GATED / REACTIVE

OPTIONALITY:
  LOW / MODERATE / HIGH / FRAGMENTED

OPERATING PROOF:
  WEAK / EMERGING / DEMONSTRATED / REPEATABLE

SHAREHOLDER-CAPTURE CLARITY:
  CLEAR / MIXED / FRAGILE / BLOCKED

BEHAVIORAL STYLE:
  BUILD / ACQUIRE / INTEGRATE / DEPLOY / REPEAT /
  MONETIZE / RESTRUCTURE / FINANCE / OTHER
~~~

These are descriptive states, not automatic numeric inputs.

## Anti-funnel rule

If the character does not fit:
1. preserve its traits;
2. mark archetype UNCLASSIFIED / EMERGENT;
3. propose a new archetype only when repeated evidence justifies one.

Never modify the character evidence to make the archetype vocabulary appear complete.
