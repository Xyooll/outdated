# FLOW — Recursive Character Story

FLOW ID: `STOCK-RECURSIVE-CHARACTER-STORY-V1`  
STATUS: **ACTIVE / CANONICAL**  
DOMAIN: stock-market  
JOB: recursively expand material characters into their own stories and propagate relevant consequences back to the parent stock
CORE PARENT FLOW: `../../../floware/core/relational-story.flow.md`  

## GOAL

Do not treat any material character as a flat node.

If the parent stock's thesis depends on another company, subsidiary, JV, customer, regulator, government, financier, lender, acquisition target, distributor, supplier, insider, exchange, court, technology partner, operating entity, or other decision-maker, reconstruct enough of that character's own story to understand what can flow back into the parent security.

Core law:

> **You cannot know the parent's story if a material part of that story lives inside another character whose own state you have not understood.**

## 0. CHARACTER EVIDENCE REFRESH

Canonical source-selection subflow:

`story-sourcing.flow.md`

Every material character, including the parent, must have a claim-specific source packet before its story can close.

Before reconstructing any material character's story, refresh the character's own evidence.

For a public-company character, check at minimum:

```text
LATEST SEC / REGULATORY FILINGS
+ ISSUER IR / PRESS RELEASES
+ MATERIAL EXCHANGE / LISTING DISCLOSURES
+ OWNERSHIP FILINGS
+ FINANCING / REGISTRATION FILINGS
+ CURRENT OPERATING / FINANCIAL REPORTS
+ SUPERSEDING EVENTS / TERMINATIONS / CLOSINGS
```

Use the character's existing company memory and source cursor where available, then fetch only missing/stale/due evidence.

Filings are not background paperwork.

A filing can change:
- character identity;
- ownership/control;
- customer conversion;
- financing/dilution;
- governance;
- timing;
- conditions precedent;
- legal rights;
- shareholder capture;
- the parent stock's thesis.

Required freshness state:

```text
CHARACTER EVIDENCE FRESH THROUGH:
LATEST FILING CHECK:
LATEST ISSUER-NEWS CHECK:
LATEST MATERIAL DELTA:
UNRESOLVED SOURCE GAP:
SOURCE AUTHORITY STATE: SOURCE-SUPPORTED / SOURCE-PARTIAL / SOURCE-BLOCKED
```

A material character may not reach `STORY_CLOSED` without a current freshness check.

If a source family is delayed or unavailable, mark:

`STORY_BLOCKED — CHARACTER FRESHNESS GAP`

## 1. RECURSIVE EXPANSION

Start with the parent:

```text
PARENT STOCK
→ MATERIAL CHARACTER
→ CHARACTER'S OWN STORY
→ CHARACTER'S SUBSIDIARIES / PARTNERS / CUSTOMERS / FINANCING / REGULATORS / PROGRAMS
→ MATERIAL STATE CHANGES
→ PROPAGATE RELEVANT CONSEQUENCES BACK TO PARENT
```

If a nested character is itself material, recurse again.

## 1A. ALL-MATERIAL-CHARACTERS RULE

Expansion is mandatory for **all material characters**, not only corporate characters.

For each character identified by `character-influence.flow.md`, output one:

```text
EXPAND — character has a material nested story
CLOSE — flat enough; no deeper material branch
BLOCKED — material branch exists but evidence is insufficient
```

A character may not remain silently unexpanded.

Examples of characters that may require recursion:

```text
COMPANY
SUBSIDIARY
JV PARTNER
CUSTOMER
REGULATOR
GOVERNMENT / AGENCY
FINANCIER
LENDER
DISTRIBUTOR
SUPPLIER
INSIDER
EXCHANGE
ACQUISITION TARGET
TECHNOLOGY PARTNER
COURT / DECISION MAKER
COMPETITOR
```

Recursion depth is determined by materiality, not entity type.

## 1B. STORY CLOSURE

The parent story is not complete until every material character has reached a closure state.

Required ledger:

```text
CHARACTER:
MATERIAL TO PARENT? YES / NO / UNKNOWN
EXPANSION STATE: EXPAND / CLOSE / BLOCKED
LOCAL WEB ROOT:
LOCAL DEGREE:
INCOMING RELATIONSHIP EDGE:
RELATIONSHIP DELTA:
CHILD CHARACTERS FOUND:
MATERIAL CHILDREN EXPANDED:
PROPAGATION PATH TO PARENT:
UNRESOLVED MATERIAL BRANCHES:
CLOSURE REASON:
```

Final status:

```text
STORY_CLOSED
STORY_INCOMPLETE — MATERIAL CHARACTER UNEXPANDED
STORY_BLOCKED — MATERIAL CHARACTER EVIDENCE MISSING
```

## 1C0. DEGREE LIMIT IS A RESOURCE BOUND

The current degree limit is **not** an epistemic claim that four degrees is the best or complete representation of reality.

It is an operational constraint imposed by finite resources.

Without a boundary:

```text
CHARACTER
→ ITS WEB
→ EACH CHARACTER'S WEB
→ EACH NEW CHARACTER'S WEB
→ ...
```

the graph tends toward open-ended expansion.

If every edge were also kept continuously fresh in real time, research cost would grow across:
- retrieval;
- source verification;
- context;
- storage;
- graph maintenance;
- refresh frequency;
- contradiction handling;
- provenance;
- compute / tool usage.

Therefore:

> **Four degrees is the current affordable research horizon, not the natural limit of the story.**

The architecture must preserve the ability to increase the horizon later.

If future resources, storage, retrieval, indexing, or autonomous refresh capacity improve, the degree cap may be raised without changing the underlying story semantics.

Do not convert the current cap into a philosophical rule about causality.

## 1C. FOUR-DEGREE DEPTH BUDGET

Canonical recursion horizon from the main stock:

```text
DEGREE 0 — MAIN CHARACTER
remaining depth budget = 4

DEGREE 1 — DIRECT MATERIAL CHARACTER
remaining depth budget = 3

DEGREE 2 — MATERIAL CHARACTER OF DEGREE 1
remaining depth budget = 2

DEGREE 3 — MATERIAL CHARACTER OF DEGREE 2
remaining depth budget = 1

DEGREE 4 — MATERIAL CHARACTER OF DEGREE 3
remaining depth budget = 0 / boundary
```

The main character may therefore see up to four degrees of separation.

A Degree-1 character has three degrees remaining.
A Degree-2 character has two degrees remaining.
A Degree-3 character has one degree remaining.
Degree 4 is the normal expansion boundary.

Materiality may stop recursion earlier.

Do not automatically recurse to Degree 5+ merely because another relationship exists.

### Example

```text
DEGREE 0: VWAV
   ↓
DEGREE 1: SaverOne
   ↓
DEGREE 2: Cemex
   ↓
DEGREE 3: Cemex Germany / material operating program
   ↓
DEGREE 4: material regulator / financing / customer dependency affecting that program
```

The purpose is not to map the entire world.

The purpose is to capture enough relational depth to reconstruct the parent stock's material story.

### Degree-4 boundary rule

At Degree 4:
- identify material outgoing dependencies needed to understand the Degree-4 state;
- do not open those dependencies as full Degree-5 stories under the normal flow;
- record any exceptional unresolved dependency as a boundary note.

Output:

```text
MAX DEGREE REACHED:
REMAINING DEPTH BUDGET:
EARLY STOP REASON:
DEGREE-4 BOUNDARY NOTES:
UNRESOLVED BEYOND-BOUNDARY RISK:
```

## 1C2. CHARACTER MEMORY

For every material entity character, load or create canonical Character Memory:

`character-memory-reroot.flow.md`

The local web belongs to the character, not only to the parent story.

If this character is later selected as the main research subject, reuse the saved local web and evidence, reset it to Degree 0, and give it a full four-degree horizon.

## 1D. LOCAL CHARACTER WEB

Every expanded material character becomes a **local root** for its own web.

The web is not a single descendant chain.

For the local root search all material branches:

```text
LOCAL ROOT CHARACTER
├─ subsidiaries
├─ JVs
├─ customers
├─ suppliers
├─ partners
├─ acquisition targets
├─ investees
├─ regulators / governments
├─ financiers / lenders
├─ insiders / management
├─ distributors
├─ technology / licensors
├─ courts / exchanges
└─ other material decision-makers
```

### Absolute degree vs local degree

Both must be tracked.

Example:

```text
VWAV = absolute D0

SaverOne = absolute D1 / SaverOne-local D0
  Cemex = absolute D2 / SaverOne-local D1
    Cemex Germany = absolute D3 / SaverOne-local D2
      material dependency = absolute D4 / SaverOne-local D3
```

Therefore SaverOne has a three-degree local web because it inherited three remaining degrees from VWAV.

Likewise:

```text
ABS D1 CHARACTER → local web depth up to 3
ABS D2 CHARACTER → local web depth up to 2
ABS D3 CHARACTER → local web depth up to 1
ABS D4 CHARACTER → local boundary only
```

This applies equally to subsidiaries.

A subsidiary is not merely a child label. It becomes a local root whose own subsidiaries, customers, suppliers, financing, regulators and partners must be searched when material and within budget.

## 1E. EDGE CONTINUITY BETWEEN DEGREES

Every step outward must preserve the edge that justifies the next degree.

Required path form:

```text
CHARACTER A
—[RELATIONSHIP TYPE + CURRENT STATE]→
CHARACTER B
—[RELATIONSHIP TYPE + CURRENT STATE]→
CHARACTER C
```

At refresh, compare each edge with memory:

```text
EDGE UNCHANGED
EDGE STRENGTHENED
EDGE WEAKENED
EDGE CHANGED TYPE
EDGE SUSPENDED
EDGE ENDED
NEW EDGE
```

If the edge changes, recompute:
- materiality;
- propagation path;
- character degree where necessary;
- thesis impact;
- timing/window;
- source requirements.

Do not preserve a descendant in the active story merely because an old relationship once connected it.

## 2. CHARACTER STORY PACKET

For every expanded character capture:

```text
IDENTITY:
ROLE IN PARENT STORY:
OWNERSHIP / CONTROL:
CONSOLIDATION / ACCOUNTING:
ITS OWN QUALITY:
ITS OWN MAIN STORY:
ITS OWN KEY CHARACTERS:
ITS OWN SUBSIDIARIES / JVS / PROGRAMS:
ITS OWN FINANCING / DILUTION:
ITS OWN CATALYSTS / TIMERS:
ITS OWN FAILURE PATH:
WHAT CAN PROPAGATE TO PARENT:
HOW IT PROPAGATES:
```

## 3. SUBSIDIARY / CHILD-ENTITY RULE

For each subsidiary/child entity ask:

- who owns it?
- who controls it?
- is it consolidated?
- what product/program/customer sits inside it?
- can its economics materially change the character?
- can that change materially reach the parent stock?

Do not equate:

```text
SUBSIDIARY SUCCESS
=
PARENT SHAREHOLDER SUCCESS
```

Trace the ownership/capture chain.

## 4. UPWARD PROPAGATION

A nested event matters to the parent only through an evidence-backed path.

Examples:

```text
SUBSIDIARY CUSTOMER WIN
→ subsidiary revenue
→ consolidated parent economics
→ parent shareholder value

PARTIAL-OWNED COMPANY DILUTION
→ parent's ownership percentage falls
→ capture falls
→ parent thesis changes

JV PARTNER DELAY
→ condition precedent remains open
→ parent acquisition cannot close
→ timer shifts

NESTED FINANCING
→ child survives
but
→ parent ownership/capture may dilute
```

## 5. MATERIALITY STOP

Recursion stops when the next layer cannot materially change the parent thesis **or when Degree 4 has been reached**.

Stop when one or more applies:

```text
NO ECONOMIC PATH TO PARENT
IMMATERIAL OWNERSHIP / EXPOSURE
NO CONTROL OR CAPTURE RELEVANCE
NO TIMING / GATING RELEVANCE
REDUNDANT WITH ALREADY-MAPPED STATE
ONLY BACKGROUND CONTEXT
EVIDENCE TOO WEAK TO SUPPORT A MATERIAL EDGE
```

Do not stop merely because the next entity is another company.

Do not recurse forever merely because another connection exists.

## 6. RECURSION PRIORITY

Expand first when a character can alter:

1. parent ownership/control;
2. parent revenue/cash/equity value;
3. a condition precedent or major gate;
4. financing/dilution;
5. regulatory permission;
6. timing/window;
7. market narrative/recognition.

## 7. STORY COMPRESSION

After recursion, compress back upward.

Final parent narrative should not dump every nested fact.

It should state:

```text
CHARACTER X MATTERS BECAUSE...
INSIDE CHARACTER X, THE IMPORTANT STORY IS...
THE STATE THAT CAN REACH THE PARENT IS...
THE TRANSMISSION PATH IS...
THE NEXT NESTED EVENT TO WATCH IS...
```

## 7A. STORY DELTA PROPAGATION

Every fresh material filing/news item is evaluated as a **story delta**:

```text
NEW EVIDENCE
→ WHICH CHARACTER CHANGED?
→ WHAT STATE CHANGED?
→ WHICH NESTED RELATIONSHIP CHANGED?
→ CAN IT PROPAGATE TO THE PARENT?
→ DOES THE PARENT THESIS / WINDOW / STRATEGY CHANGE?
```

Do not wait for the parent company to mention a nested-character development.

If SaverOne changes materially, VWAV's story must be reconsidered because VWAV has an economic and strategic link to SaverOne.

## 8. MISS RULE

A **Recursive Story Miss** occurs when:

- Xyool maps a material character but never inspects the character's own story;
- **FILING / NEWS MISS:** a fresh material filing or issuer disclosure existed for the character but was not loaded into its story;
- a subsidiary/JV/program materially affects the character and is ignored;
- child financing/dilution changes parent capture but is not propagated upward;
- a nested gate changes timing but the parent timer is not updated;
- a child event is incorrectly attributed directly to the parent;
- a relationship edge changed but the old relationship state remained in memory;
- a new character entered a local web but was not mapped;
- a subsidiary was mapped as a flat child without opening its own material local web;
- recursion stops before the economically material branch.

## 8A. CLOSURE AUDIT

Before compressing the parent thesis ask:

```text
HAVE ALL MATERIAL FIRST-ORDER CHARACTERS BEEN EXPANDED OR CLOSED?

FOR EACH EXPANDED CHARACTER:
HAVE ALL MATERIAL CHILD CHARACTERS BEEN EXPANDED OR CLOSED?

IS THERE ANY UNRESOLVED NESTED BRANCH THAT COULD CHANGE:
- ownership?
- control?
- timing?
- economics?
- financing/dilution?
- shareholder capture?
- regulatory permission?
- market recognition?
```

If yes, the story is incomplete or blocked.

## 9. RELATION TO CHARACTER INFLUENCE

`character-influence.flow.md` identifies which characters matter.

`recursive-character-story.flow.md` opens the important characters and reconstructs the relevant nested story.

Together:

```text
WHO MATTERS?
→ WHAT IS THEIR OWN STORY?
→ WHAT PART OF THAT STORY CAN REACH THE PARENT?
```

## 10. SOFTWARE / HARD-LIMIT BOUNDARY

`NONE — FLOWARE SUFFICIENT`

Existing corporate-entity graph software may support exact ownership/attribution paths, but recursive reasoning remains Floware.