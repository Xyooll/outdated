# User Concept — Story Reader/Writer + Character Archetypes

Date: 2026-09-23
Status: **ACTIVE / CORE FLOWARE ARCHITECTURE**

## USER-STATED

The existing story system can become too biography-like when it mostly reads old events.

Xyool should also be able to write possible stories forward from the current state, including for domains beyond stocks.

The character layer should be richer so different characters are not forced into the same categories merely because their numerical/quantifiable qualities look similar.

Characters should preserve both:
- quantitative qualities;
- qualitative qualities.

Archetypes should help distinguish characters, but should not funnel characters into categories they do not belong in.

## ASSISTANT INTERPRETATION

This implies three separable core capabilities:

~~~text
CHARACTER SYSTEM
→ identity + quantitative traits + qualitative traits
→ behavior + resources + constraints + agency
→ non-exclusive archetype hypotheses
→ transformation state

STORY READER
→ past → present causal reconstruction

STORY WRITER
→ present → conditional possible futures
~~~

Archetypes should be evidence-backed, dynamic, non-exclusive and optional.

UNCLASSIFIED / HYBRID / EMERGENT are valid states.

## SYSTEM CONSEQUENCE

Implemented as:
- floware/core/character-system.flow.md
- floware/core/story-reader.flow.md
- floware/core/story-writer.flow.md

Relational Story remains the umbrella architecture.

Stock-market support adds:
- domains/stock-market/CHARACTER-ARCHETYPES.md
- qualitative/quantitative character profile persistence;
- Story Reader / Story Writer routing;
- Meta Audit checks for archetype forcing and branch integrity.

## RELATED CONCEPTS

- 2026-09-22-characters-in-stock-story.md
- 2026-09-22-recursive-character-stories.md
- 2026-09-23-characters-are-rerootable-stories.md
- 2026-09-23-relational-story-is-cross-domain-flow.md
- 2026-09-23-relationship-webs-and-edge-continuity.md

## OPEN QUESTION

Which archetypes are truly reusable across multiple domains versus only useful inside one domain should be learned through correspondence and testing rather than assumed.
