# User Concept — Relationship Webs and Edge Continuity

Date: **2026-09-23**  
Status: **ACTIVE / CORE STOCK ARCHITECTURE**

## USER-STATED CONCEPT

While building the story, Xyool must track whether relationships remain the same or change as the graph moves from one degree to the next.

If a new character enters the main character's story, that character must be included.

Characters underneath the main character must also have their own webs of relationships and degrees of separation, including subsidiaries and the subsidiaries' own material characters.

## SYSTEM INTERPRETATION

The stock story is a recursive **network of local webs**, not a single tree or chain.

Every material relationship is a first-class edge with a lifecycle:

```text
NEW
SAME
STRENGTHENED
WEAKENED
CHANGED_TYPE
SUSPENDED
ENDED
```

Every material character becomes a local root within the remaining global depth budget.

Example:

```text
VWAV — absolute D0 / local root

SaverOne — absolute D1 / SaverOne local D0
  Cemex — absolute D2 / SaverOne local D1
  RBtec — absolute D2 / SaverOne local D1
  subsidiaries — absolute D2 / SaverOne local D1
    their customers/partners/etc. — absolute D3 / local D2
```

## CORE RULES

> **Do not only remember who is connected. Remember how they are connected and whether that relationship changed.**

> **Every material character owns a local web within the unused portion of the main story's four-degree horizon.**

> **A new material character entering any local web is a story delta.**

## RELATED FLOWS

- `domains/stock-market/flows/character-influence.flow.md`
- `domains/stock-market/flows/recursive-character-story.flow.md`
- `domains/stock-market/flows/story-sourcing.flow.md`
- `domains/stock-market/flows/story-memory.flow.md`
