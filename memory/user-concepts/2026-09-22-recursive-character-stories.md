# User Concept — Recursive Character Stories

Date: **2026-09-22**  
Status: **ACTIVE / CORE STOCK PHILOSOPHY**

## USER-STATED WORDING

> "We can't know vwavs story if we don't know saverones story as well as all of his subsidiaries"

## CONCEPT

A material character in a stock story cannot be represented only by its name or relationship to the parent.

If the parent thesis depends on that character, Xyool must understand the character's own story and the material entities inside it.

## ASSISTANT INTERPRETATION

The stock graph is recursive:

```text
VWAV
→ SAVERONE
   → PRODUCTS
   → CUSTOMERS
   → PARTNERS
   → FINANCING
   → SUBSIDIARIES / INVESTMENTS
   → REGULATORS
   → CATALYSTS
→ PROPAGATE MATERIAL CONSEQUENCES BACK TO VWAV
```

Recursion stops when the next layer no longer has a material causal path back to the parent stock.

## SYSTEM CONSEQUENCE

Created:
`domains/stock-market/flows/recursive-character-story.flow.md`

Character Influence should recursively expand material company characters before the parent Narrative Thesis is compressed.

## RELATED CONCEPTS

- Character Influence
- Narrative Thesis
- Wrappers and Pointers
- Corporate Entity Graph
- Shareholder Capture
- Mapping Miss

## LATER REFINEMENT — ALL MATERIAL CHARACTERS

The user clarified that SaverOne was only an example.

The recursion rule applies to **all material characters in the story**, including:
- companies;
- subsidiaries;
- JV partners;
- customers;
- regulators;
- governments/agencies;
- financiers/lenders;
- distributors;
- suppliers;
- insiders;
- exchanges;
- acquisition targets;
- technology partners;
- courts/decision makers;
- competitors when they materially affect the thesis.

Canonical refinement:

> **Every material character must either be recursively expanded or explicitly closed with a reason why deeper expansion cannot materially change the parent thesis.**

A parent story is incomplete while any material character remains silently flat.


## LATER REFINEMENT — FILINGS ARE PART OF THE STORY

The user clarified that the filings previously used for stock analysis must be part of story-building for every material character.

Canonical consequence:

> **A character's story is not current unless its own current filings and material issuer disclosures have been refreshed.**

For a material public-company character:

```text
LATEST FILINGS
+ ISSUER NEWS
+ OWNERSHIP / FINANCING DISCLOSURES
+ REGULATOR / EXCHANGE EVENTS
→ CHARACTER STORY DELTA
→ PROPAGATE TO PARENT IF MATERIAL
```

The parent story cannot be fresher than its material characters.

A material nested filing/news item omitted from the story is a system miss.


## LATER REFINEMENT — THREE DEGREES OF SEPARATION

User rule:

> Story sourcing and character expansion go up to **three degrees of separation from the main character**.

Canonical interpretation:

```text
DEGREE 0 — main public stock
DEGREE 1 — direct material characters
DEGREE 2 — material characters of Degree 1
DEGREE 3 — material characters of Degree 2
```

Materiality may stop recursion earlier.

Normal analysis does not recursively open Degree 4+ stories.

If a Degree-3 state depends on something beyond the boundary, note that dependency without fully expanding it.

This creates a bounded but deep-enough story graph.
