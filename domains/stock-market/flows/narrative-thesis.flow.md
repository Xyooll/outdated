# FLOW — Stock Narrative Thesis

FLOW ID: `STOCK-NARRATIVE-THESIS-V1`  
STATUS: **ACTIVE / CANONICAL**  
DOMAIN: stock-market  
JOB: convert mapped evidence into one coherent causal story and thesis
AUTHORITY: descriptive / explanatory thesis synthesis only; no TTC priority, strategy-selection, sizing, or execution authority
PARENT GOALPOST: supplied by STOCK-COMPANY-ANALYSIS or calling stock pipeline
UPSTREAM FLOWS: company-analysis, character-influence, recursive-character-story, story-reader, Quality/TTC/economic/recognition state
DOWNSTREAM FLOWS: story-writer, strategy-layer, company-analysis, meta audit
INBOUND PIPES: `../PLUMBING.md#pipe-stock-reader-thesis`
OUTBOUND PIPES: `../PLUMBING.md#pipe-stock-thesis-writer`, `../PLUMBING.md#pipe-stock-story-strategy`
SOFTWARE DEPENDENCIES: none by default
CORE PARENT FLOW: `../../../floware/core/relational-story.flow.md`
CORE CHARACTER FLOW: `../../../floware/core/character-system.flow.md`
CORE STORY READER: `../../../floware/core/story-reader.flow.md`
CORE STORY WRITER: `../../../floware/core/story-writer.flow.md`  

## GOAL

Turn a complete stock evidence/state map into a human-readable causal narrative that explains:

- what the company is trying to become;
- what forces are helping or blocking that transition;
- which connections matter;
- how those connections transmit into shareholder economics;
- what must happen next;
- what would invalidate the thesis;
- what Xyool may have overlooked.

Core law:

> **The data is not the thesis. The mapped relationship between the data is the thesis.**

## 0A. STORY SOURCING

Before detective reconstruction, load:

`story-sourcing.flow.md`

The parent and every material character must be sourced with the strongest claim-specific evidence available.

Canonical rule:

> **The quality of the story cannot exceed the quality of the evidence supporting it.**

For material relationships, seek both sides where available.

## 0. DETECTIVE MODEL

Treat stock analysis as evidence-backed detective work:

```text
CLUES / EVIDENCE
→ BUILD CHARACTER PROFILES
→ MAP CONNECTIONS
→ STORY READER: RECONSTRUCT PAST → PRESENT
→ FORM CURRENT THESIS
→ STORY WRITER: CONSTRUCT CONDITIONAL FUTURE BRANCHES
→ SELECT / STATE LIKELY NEXT STATE ONLY WHEN EVIDENCE DISCRIMINATES
→ ESTIMATE WINDOW
→ USE TA / MARKET STRUCTURE INSIDE THE WINDOW
→ UPDATE STORY AS NEW CLUES ARRIVE
```

The objective is not perfect prediction.

The objective is the most accurate causal story and falsifiable thesis available from current evidence.

## INPUT

Use the already gathered evidence/state from:
- company-analysis flow;
- Quality;
- event/dependency state;
- TTC;
- capital path;
- Recognition;
- shareholder capture;
- persistent company memory.

Do not re-research facts unnecessarily.

## INPUT CHARACTER PROFILES

Before narrative compression, material characters should have a Character System disposition:

```text
PROFILED
PARTIAL
UNCLASSIFIED / EMERGENT
BLOCKED
```

Archetypes are optional and non-exclusive. The thesis must remain valid if an archetype label is removed; raw traits/relationships/evidence are authoritative.

## 1. CHARACTER / CONNECTION MAP

Canonical subflow:
`character-influence.flow.md`

Before compressing the stock into a thesis, identify every material character and trace how that character can change economics, control, timing, shareholder capture, and market recognition.

Do not merely list entities. Explain their role in the story and their path to price.

### ENTITY / CONNECTION MAP

Identify the important actors around the company:

```text
COMPANY
├─ subsidiaries
├─ acquisition targets
├─ JV partners
├─ customers
├─ distributors
├─ lenders
├─ financiers
├─ insiders
├─ regulators
├─ strategic partners
├─ suppliers
├─ technology partners
└─ competitors / substitutes
```

For each connection ask:

```text
WHAT IS THE RELATION?
WHAT DOES EACH PARTY WANT?
WHAT IS COMMITTED?
WHAT IS OPTIONAL?
WHAT DOES VWAV CONTROL?
WHAT DOES VWAV NOT CONTROL?
WHAT ECONOMIC VALUE CAN FLOW THROUGH THE CONNECTION?
WHAT CAN BLOCK THAT FLOW?
WHAT HAPPENS TO COMMON SHAREHOLDERS?
```

## 1A. RECURSIVE CHARACTER STORIES

A material company character may contain another story.

Use:
`recursive-character-story.flow.md`

Before finalizing the parent thesis, expand material nested stories and propagate only the consequences that can reach the parent.

## 1B. CHARACTER FRESHNESS GATE

Before narrative compression, every material character must have a current evidence refresh under:

`recursive-character-story.flow.md`

This includes the character's own filings and issuer disclosures.

Rule:

> **A parent story cannot be fresher than its material characters.**

A material nested filing/news item omitted from the parent story is a system miss if it could change economics, timing, control, financing, shareholder capture, or recognition.

## 1C. STORY CLOSURE GATE

Before compressing the story, require recursive closure from:

`recursive-character-story.flow.md`

The thesis may not be marked complete while a material character or material nested branch is unexpanded.

Allowed states:

```text
STORY_CLOSED
STORY_INCOMPLETE — MATERIAL CHARACTER UNEXPANDED
STORY_BLOCKED — MATERIAL CHARACTER EVIDENCE MISSING
```

## 2. WRAPPERS AND POINTERS

Use the programming-language correspondence explicitly.

### Wrapper

A wrapper is the local structure around another capability.

In stock analysis this may be:
- a JV;
- acquisition vehicle;
- distribution agreement;
- subsidiary;
- licensing structure;
- financing structure;
- strategic partnership.

The wrapper changes how value reaches the company.

### Pointer

A pointer/reference is a connection to another object/state without embedding the whole thing.

In stock analysis this may be:
- an SEC cross-reference;
- a contract dependency;
- a condition precedent;
- a beneficial ownership link;
- a milestone tied to another program;
- an agreement whose economics depend on another agreement;
- an insider/entity relationship.

Pointers create the graph.

The narrative follows the graph.

## 2A. WAITING-CATALYST RHYTHM

If the thesis is waiting on an unresolved process-driven catalyst, load:

`correspondence-rhythm.flow.md`

The story should state:
- which process is running;
- where the company is inside it;
- which correspondence beam is being used;
- what rhythm the analog processes imply;
- what would reset that rhythm.

## 2B. STORY READER / WRITER SEPARATION

First run the Story Reader.

It answers:
- what happened;
- how characters/relationships changed;
- what current state those changes produced.

Only after the Reader current state is stable, run the Story Writer.

The Writer must produce materially distinct conditional branches such as:
- conversion;
- continuation;
- delay/stall;
- failure;
- character transformation;
- parallel path becoming dominant;
- capital/financing counter-story.

A branch must state trigger, transition sequence, observable proof and invalidation.

The Writer does not convert a coherent narrative into certainty.

## 3. BUILD THE STORY

Tell the story in causal order:

```text
PAST STATE
→ WHAT CHANGED
→ WHAT THE COMPANY IS TRYING TO BECOME
→ WHAT CONNECTIONS ENABLE THAT
→ WHAT CONNECTIONS CONSTRAIN IT
→ WHAT MUST HAPPEN NEXT
→ HOW ECONOMICS REACH SHAREHOLDERS
→ WHAT BREAKS THE STORY
```

Do not organize the final thesis by filing type.

Organize it by causal meaning.

## 4. THESIS

A valid thesis should answer:

1. **What is the company becoming?**
2. **Why could that create shareholder value?**
3. **Which connections make that possible?**
4. **Which connection is the current bottleneck?**
5. **What is the next observable proof point?**
6. **What is the primary failure path?**
7. **What is already recognized by the market?**

Prefer one coherent thesis over a long list of independent catalysts.

## 4A. CONDITIONAL FUTURE BRANCHES

Use:
`../../../floware/core/story-writer.flow.md`

Required minimum:

```text
PRIMARY BRANCHES[]
COUNTER-STORY BRANCHES[]
DRIVING CHARACTERS / TRAITS / ARCHETYPES
TRIGGERS / PREREQUISITES
TRANSITION SEQUENCE
OBSERVABLE PROOF
INVALIDATION
WINDOW / RHYTHM
```

Do not require a single winning branch when evidence does not discriminate.

## 4B. CONDITIONAL DEDUCTION

Compress the story into a testable statement:

> **Based on [evidence + mapped relationships + corresponding-process rhythm], X may occur during Y window, unless Z invalidates or delays the story.**

Required fields:

```text
LIKELY NEXT STATE / EVENT:
WHY:
CORRESPONDENCE / ANALOG SUPPORT:
CONDITIONAL WINDOW:
CONFIDENCE:
PRIMARY INVALIDATION:
DELAY / RESET CONDITION:
```

Use `may`, `likely`, ranges, and conditional windows when certainty is not earned.

Do not convert a plausible story into a fake exact prediction.

## 4C. TA AFTER THE WINDOW EXISTS

TA / market structure is downstream of the thesis.

Preferred order:

```text
STORY
→ THESIS
→ EVENT / PROCESS WINDOW
→ TA / MARKET STRUCTURE
→ TIMING / RECOGNITION / EXPRESSION
```

TA may help determine:
- whether price is already anticipating the thesis;
- whether recognition is strengthening or failing;
- entry timing inside/near the expected window;
- whether market behavior contradicts the story;
- execution/expression.

TA may not create the causal thesis.

## 5. CONNECTION TRANSMISSION

For every important connection, trace:

```text
CONNECTION
→ CAPABILITY / ACCESS / CAPITAL / DEMAND
→ COMPANY CONTROL OR DEPENDENCE
→ ECONOMIC CONVERSION
→ CASH / EARNINGS / ASSET VALUE
→ COMMON SHAREHOLDER CAPTURE
```

If the chain breaks, say where.

A connection is not economically valuable merely because it exists.

## 6. MISS DEFINITION

A **MISS** is not only a wrong stock outcome.

A miss occurs when Xyool overlooks a material:

- entity;
- relationship;
- dependency;
- condition precedent;
- economic transmission path;
- financing branch;
- dilution path;
- timing edge;
- control distinction;
- contradiction;
- future node;
- invalidation path.

Canonical rule:

> **If the information existed and materially changed the story, but Xyool failed to map it, that is a system miss.**

## 7. MISS AUDIT

Before finalizing the thesis ask:

```text
WHO IS CONNECTED TO THIS COMPANY THAT WE HAVE NOT MAPPED?

WHAT AGREEMENT POINTS TO ANOTHER AGREEMENT?

WHAT EVENT DEPENDS ON ANOTHER EVENT?

WHAT ECONOMIC VALUE IS CONTROLLED BY SOMEONE ELSE?

WHAT FINANCING OBLIGATION CAN INTERRUPT THE STORY?

WHAT CONNECTION LOOKS POSITIVE BUT HAS NO COMMITTED ECONOMICS?

WHAT CONNECTION LOOKS MINOR BUT CONTROLS A MAJOR GATE?

WHAT WOULD A SMART SKEPTIC SAY WE OVERLOOKED?
```

If a material unanswered question remains, mark the thesis incomplete.

## 8. OUTPUT

Final output should read like a story.

Structure:

```text
THE STORY
SOURCE AUTHORITY / MATERIAL SOURCE GAPS
THE THESIS
THE KEY CHARACTER PROFILES / ARCHETYPES
THE KEY CHARACTERS
THE KEY CONNECTIONS
THE BOTTLENECK
THE STORY WRITER BRANCHES
THE COUNTER-STORY
THE LIKELY NEXT STATE (ONLY IF DISCRIMINATED)
THE CONDITIONAL WINDOW
THE NEXT PROOF
THE FAILURE / DELAY PATH
THE MARKET'S CURRENT STORY
TA / MARKET STRUCTURE INSIDE THE WINDOW
STORY CLOSURE STATUS
THE MISS AUDIT
```

The underlying detailed state remains available for audit, but the operational reasoning should be understandable without reading every field.

## 9. VWAV EXAMPLE

A simplified VWAV narrative:

```text
VWAV is trying to transform from a thin-revenue public vehicle
into a defense / autonomy / RF-security platform.

It is assembling that platform through connections:
SaverOne, C.M. Composite, Belrise, Foresight, Stratonex,
D-Fence and other strategic relationships.

Those connections are not equal.

Belrise + C.M. forms the strongest current control/economic path
because the JV condition is tied directly to the C.M. acquisition close.

SaverOne provides a more-real operating asset but VWAV does not fully control it.

Foresight / Stratonex provide capability or distribution,
but weak committed economics.

Meanwhile financing, debt service and dilution are actively consuming
shareholder capacity while the strategic network is still converting.

Therefore the thesis is not:
"VWAV has many catalysts."

It is:
"VWAV is assembling a potentially valuable defense platform,
but common shareholders only win if one or more strategic connections
convert into controlled cash economics before financing dilution consumes
the transition value."

The next important proof is conversion, not another announcement.
```

## SOFTWARE / HARD-LIMIT BOUNDARY

`NONE — FLOWARE SUFFICIENT`
