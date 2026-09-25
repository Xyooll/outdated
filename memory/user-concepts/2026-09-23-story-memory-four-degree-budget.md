# User Concept — Story Memory + Four-Degree Character Horizon

Date: **2026-09-23**  
Status: **ACTIVE / CORE STOCK ARCHITECTURE**

## USER-STATED CONCEPT

Finished stock stories should be fed into the memory layer so Xyool does not have to repeatedly pull and reconstruct the same information.

The user also expanded the character horizon from three degrees to four total degrees from the main character.

## DEPTH RULE

Canonical interpretation:

```text
MAIN CHARACTER / DEGREE 0
→ may expand four degrees outward

DEGREE 1 CHARACTER
→ has three degrees remaining

DEGREE 2 CHARACTER
→ has two degrees remaining

DEGREE 3 CHARACTER
→ has one degree remaining

DEGREE 4 CHARACTER
→ boundary
```

Materiality may stop earlier.

## MEMORY RULE

```text
SOURCE
→ STORY
→ STORY MEMORY
→ NEXT RUN LOADS MEMORY
→ REFRESH DELTAS ONLY
→ UPDATE STORY
```

The story is a durable reasoning object, not merely a transient response.

## SYSTEM CONSEQUENCE

Created:

`domains/stock-market/flows/story-memory.flow.md`

Stock persistent state should carry a compact story-memory head pointing to the lossless story/archive.

## RELATED CONCEPTS

- Story Sourcing
- Recursive Character Story
- Character Influence
- Narrative Thesis
- Stock Analysis Memory
- Domain State Persistence
