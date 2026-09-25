# FLOW — Stock Character Influence

FLOW ID: `STOCK-CHARACTER-INFLUENCE-V1`  
STATUS: **ACTIVE / CANONICAL**  
DOMAIN: stock-market  
JOB: map every material character in the stock story and trace how changes in that character can reach price
CORE PARENT FLOW: `../../../floware/core/relational-story.flow.md`
CORE CHARACTER FLOW: `../../../floware/core/character-system.flow.md`  

## GOAL

Identify all material characters in the company story and understand how each can change:

- economics;
- control;
- timing;
- probability;
- financing;
- dilution;
- recognition;
- and ultimately common-shareholder value.

Also identify what kind of character this appears to be qualitatively, without forcing it into an exclusive category.

Core law:

> **A company does not move through its story alone. Every material counterparty, regulator, customer, financier, partner, insider, and gatekeeper is a character whose state can change the thesis.**

## 1. CHARACTER INVENTORY

Search for:

```text
COMPANY / MANAGEMENT
CUSTOMERS / BUYERS
JV PARTNERS
ACQUISITION TARGETS
SUBSIDIARIES
REGULATORS
GOVERNMENTS / AGENCIES
LENDERS
EQUITY FINANCIERS
DISTRIBUTORS
SUPPLIERS
TECHNOLOGY PARTNERS
LICENSORS
INSIDERS
COMPETITORS
EXCHANGES / LISTING AUTHORITIES
COURTS / OTHER DECISION MAKERS
```

Do not stop at the obvious characters.

Cross-references, conditions precedent, financing agreements, ownership filings and regulator correspondence may introduce characters that never appear in headline summaries.

## 1A. RECURSIVE EXPANSION

When a material character is itself a company/entity with its own economically relevant structure, load:

`recursive-character-story.flow.md`

Do not treat the character as a flat label.

Every material character must receive an expansion state:

```text
EXPAND
CLOSE
BLOCKED
```

Expand enough of its own story to determine what can materially propagate back to the parent stock.

## 1B. RELATIONSHIP EDGE STATE

A character graph is made of **relationships**, not only nodes.

For every material edge record:

```text
FROM CHARACTER:
TO CHARACTER:
RELATIONSHIP TYPE:
DIRECTION:
PRIOR RELATIONSHIP STATE:
CURRENT RELATIONSHIP STATE:
RELATIONSHIP DELTA:
  NEW / SAME / STRENGTHENED / WEAKENED / CHANGED_TYPE / SUSPENDED / ENDED
CONTROL / DEPENDENCE:
ECONOMIC TRANSMISSION:
TIMING / GATE:
EVIDENCE:
FRESH THROUGH:
```

Do not assume the relationship that originally introduced a character remains unchanged.

Examples:

```text
PROSPECTIVE PARTNER
→ DEFINITIVE JV PARTNER

CUSTOMER PILOT
→ FUNDED CUSTOMER

ACQUISITION TARGET
→ CONTROLLED SUBSIDIARY

EQUITY INVESTMENT
→ DILUTED MINORITY INTEREST

ACTIVE LENDER
→ RESTRUCTURED / DEFERRED CREDITOR

REGULATOR
→ ACTIVE GATEKEEPER
```

A changed edge can change the story even when neither character is new.

## 1C. NEW-CHARACTER ENTRANCE

At every refresh ask:

```text
DID A NEW MATERIAL CHARACTER ENTER THE MAIN CHARACTER'S STORY?
DID A NEW MATERIAL CHARACTER ENTER ANY NESTED CHARACTER'S STORY?
WHICH EXISTING RELATIONSHIP INTRODUCED THEM?
WHAT DEGREE DO THEY OCCUPY?
CAN THEIR STATE PROPAGATE BACK TO THE MAIN CHARACTER?
```

New entrants must be added to the appropriate local web and then propagated upward.

A character may enter through:
- a new contract;
- acquisition;
- financing;
- subsidiary formation;
- customer win;
- regulator action;
- partnership;
- ownership filing;
- litigation;
- supplier relationship;
- new program or government process.

## 1D. CHARACTER PROFILE GATE

Before using a character as a story driver, load or construct its profile through:

`../../../floware/core/character-system.flow.md`

Stock-local archetype definitions:
`../CHARACTER-ARCHETYPES.md`

Required separation:

```text
CHARACTER TYPE
= what kind of entity is it?

STORY ROLE
= what is it doing relative to this root?

QUALITATIVE / QUANTITATIVE TRAITS
= what properties does evidence show?

ARCHETYPE
= what recurring pattern might those properties resemble?
```

Do not infer an archetype from a ticker, market cap, sector label, or one numeric score.

UNCLASSIFIED / HYBRID / EMERGENT are valid.

## 2. CHARACTER CARD

For every material character record:

```text
CHARACTER:
LOCAL ROOT CHARACTER:
LOCAL DEGREE FROM ROOT:
DEGREE FROM MAIN CHARACTER: 0 / 1 / 2 / 3 / 4
REMAINING DEPTH BUDGET: 4 / 3 / 2 / 1 / 0
MATERIALITY TO PARENT:
EXPANSION STATE:
CHARACTER TYPE:
ROLE:
QUANTITATIVE TRAITS:
QUALITATIVE TRAITS:
BEHAVIOR SIGNATURE:
RESOURCES / CAPABILITIES:
CONSTRAINTS / DEPENDENCIES:
AGENCY:
ARCHETYPE HYPOTHESES + CONTRADICTIONS:
TRANSFORMATION STATE:
RELATIONSHIP TO PARENT CHARACTER:
RELATIONSHIP STATE / DELTA:
WHAT THIS CHARACTER WANTS:
WHAT VWAV / COMPANY WANTS FROM THEM:
CONTROL / BARGAINING POWER:
COMMITMENT LEVEL:
CURRENT STATE:
NEXT ACTION / DECISION:
TIMING / RHYTHM:
ECONOMIC TRANSMISSION:
SHAREHOLDER TRANSMISSION:
PRICE TRANSMISSION:
FAILURE / DELAY PATH:
EVIDENCE:
```

## 3. PRICE TRANSMISSION

Price is not assumed to move mechanically because a character exists.

Trace the causal path:

```text
CHARACTER STATE CHANGES
→ INFORMATION / PROBABILITY CHANGES
→ EXPECTED COMPANY ECONOMICS CHANGE
→ EXPECTED SHAREHOLDER CAPTURE CHANGES
→ MARKET RECOGNITION / POSITIONING CHANGES
→ PRICE CAN REPRICE
```

Different characters can affect price through different channels:

```text
CUSTOMER
→ demand / order / revenue

REGULATOR
→ permission / denial / timing

FINANCIER
→ survival / dilution / debt burden

JV PARTNER
→ access / scale / control / economics

ACQUISITION TARGET
→ capability / ownership / consideration / dilution

INSIDER
→ information / confidence / supply-demand context

EXCHANGE
→ listing eligibility / forced corporate action
```

## 4. CHARACTER WEIGHT IS DYNAMIC

A character can move from background to dominant.

Examples:

```text
minor regulator
→ formal review begins
→ becomes gating character

potential customer
→ funded purchase order
→ becomes economic character

passive financier
→ covenant / conversion / ATM activity
→ becomes shareholder-capture character
```

Therefore character importance must be updated when state changes.

## 5. CHARACTER RELATIONSHIPS

Characters may point to each other.

Map:

```text
CHARACTER A
→ controls condition for
CHARACTER B
→ enables transaction with
COMPANY
```

Example:

```text
BELRISE
→ definitive JV condition
→ C.M. COMPOSITE CLOSE
→ VWAV CONTROL / INDIA PLATFORM
```

The story may be driven by the relationship between characters rather than by any one character independently.

## 6. CHARACTER CONFLICT

Characters may exert opposing forces.

Example:

```text
BELRISE / C.M.
→ potential operating value creation

YA II / AEGIS / FINANCING
→ survival capital
→ but also dilution / repayment burden
```

The thesis should explain which force currently dominates and what event would change that balance.

## 7. CHARACTER-TO-PRICE STORY

Final narrative should answer:

> **Which characters currently have the greatest ability to change the stock's expected value, why, and through what causal path?**

Do not simply list characters.

## 8. MISS RULE

A Character Miss occurs when:

- a material character existed in available evidence but was not mapped;
- the character was mapped but its role was misunderstood;
- a relationship between two characters was missed;
- Xyool failed to trace the character's state to economics/shareholder capture;
- Xyool kept treating a character as important after its role became inactive;
- Xyool failed to notice a new character entering the story;
- Xyool forced a character into an archetype despite contradictory evidence;
- Xyool missed a qualitative transformation that changed how the character should be modeled.

Canonical rule:

> **If a material character could change the story and Xyool failed to include that character, the analysis is incomplete.**

## 9. OUTPUT

```text
MAIN CHARACTER:
KEY CHARACTER PROFILES / ARCHETYPES:
KEY SUPPORTING CHARACTERS:
KEY GATING CHARACTERS:
KEY NEGATIVE / CONSTRAINING CHARACTERS:
NEWLY ENTERED CHARACTERS:
CHARACTER RELATIONSHIP GRAPH:
DOMINANT CHARACTER-TO-PRICE PATH:
CHARACTER MOST LIKELY TO CHANGE THE NEXT STATE:
UNMAPPED / UNKNOWN CHARACTERS:
STORY CLOSURE STATUS:
```

## SOFTWARE / HARD-LIMIT BOUNDARY

`NONE — FLOWARE SUFFICIENT`