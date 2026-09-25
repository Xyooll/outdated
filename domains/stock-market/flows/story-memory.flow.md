# FLOW — Stock Story Memory

FLOW ID: `STOCK-STORY-MEMORY-V1`  
STATUS: **ACTIVE / CANONICAL**  
DOMAIN: stock-market  
JOB: persist a completed stock story so future runs resume from memory and refresh only material deltas
CORE PARENT FLOW: `../../../floware/core/relational-story.flow.md`  

## GOAL

Preserve the finished evidence-backed story as durable operational memory.

Core law:

> **Do not rebuild a known story from zero. Load the last closed story, refresh only what can have changed, and rewrite the story only where evidence changed it.**

## MEMORY ARCHITECTURE

```text
LOSSLESS STORY / ANALYSIS ARCHIVE
        ↓
COMPACT STORY MEMORY HEAD
        ↓
CHARACTER + SOURCE + THESIS POINTERS
        ↓
NEXT RUN LOADS STORY FIRST
        ↓
DELTA REFRESH
        ↓
UPDATED STORY MEMORY VERSION
```

The lossless archive preserves the complete finished story.

The compact story memory exists for fast operational resumption.

## STORY MEMORY HEAD

Minimum fields:

```text
STORY ID
AS OF
STORY STATUS
SOURCE AUTHORITY
CLOSURE STATUS
MAX ABSOLUTE DEGREE
DEPTH-BUDGET RULE

STORY READER HEAD
COMPRESSED STORY
THESIS
PRIMARY CONFLICT
PRIMARY BOTTLENECK
LIKELY NEXT STATE
CONDITIONAL WINDOW
PRIMARY INVALIDATION

STORY WRITER HEAD
FUTURE BRANCHES[]
COUNTER_STORY_BRANCHES[]
NEXT_OBSERVABLE_PROOFS[]
WRITER_FREEZE_ID

KEY CHARACTERS[]
  identity
  degree_from_main
  local_root
  local_degree
  remaining_depth_budget
  role
  character_type
  quantitative_trait_head
  qualitative_trait_head
  archetype_hypotheses
  transformation_state
  current_state
  propagation_to_parent
  source_authority
  fresh_through
  story_pointer if separately persisted

RELATIONSHIP GRAPH[]
  from
  to
  relationship_type
  prior_state
  current_state
  relationship_delta
  economic_transmission
  evidence
  fresh_through

LOCAL WEB HEADS[]
  root_character
  absolute_degree
  remaining_depth_budget
  material_children[]
  subsidiaries[]
  customers[]
  partners[]
  regulators[]
  financing[]
  source_status

NEWLY ENTERED CHARACTERS[]
ENDED / SUSPENDED RELATIONSHIPS[]
RELATIONSHIP DELTAS[]

MATERIAL SOURCE GAPS[]
UNRESOLVED QUESTIONS[]
NEXT REFRESH TARGETS[]
LOSSLESS STORY PATH
```

## RESOURCE-HORIZON POLICY

The Story Memory depth cap is a **research-budget policy**.

Persist:

```text
current_max_degree
degree_policy_reason = RESOURCE_BOUND
beyond_boundary_branches[]
boundary_risk[]
expansion_ready = true
```

This allows a future system with greater capacity to resume beyond the current boundary without reconstructing why research stopped.

A boundary means:

`NOT EXPANDED UNDER CURRENT RESOURCE BUDGET`

It does **not** mean:

`NO FURTHER MATERIAL RELATIONSHIPS EXIST`

## FOUR-DEGREE DEPTH BUDGET

The main story receives a total outward budget of four degrees:

```text
DEGREE 0 — MAIN CHARACTER
remaining depth = 4

DEGREE 1 — FIRST-ORDER CHARACTER
remaining depth = 3

DEGREE 2 — SECOND-ORDER CHARACTER
remaining depth = 2

DEGREE 3 — THIRD-ORDER CHARACTER
remaining depth = 1

DEGREE 4 — FOURTH-ORDER CHARACTER
remaining depth = 0 / boundary
```

This is equivalent to saying:

> **Each character inherits the unused portion of the main character's four-degree story horizon.**

Materiality may stop expansion before the budget is exhausted.

No normal full expansion begins beyond Degree 4.

## CHARACTER-MEMORY POINTER RULE

Story Memory is root-relative. Character Memory is reusable across roots.

For material entity characters, Story Memory should store a pointer:

```text
character_id
character_memory_path
story_role
degree_from_current_root
remaining_depth_budget
```

Do not make the Story Memory the only place where the character's local web exists.

Load:

`character-memory-reroot.flow.md`

when:
- a material subsidiary/entity is first expanded;
- a character already has reusable memory;
- the user switches the main research character.

## LOAD-FIRST RULE

Before external research on a cataloged stock:

1. load the latest story memory;
2. load character/source freshness heads;
3. identify which characters or claims are stale/due;
4. refresh only those branches;
5. propagate new evidence upward;
6. preserve unchanged story branches;
7. issue a new story version only when a material story delta occurs.

## RELATIONSHIP-MEMORY RULE

Story Memory preserves graph continuity across runs.

On refresh:

```text
LOAD PRIOR CHARACTER GRAPH
→ REFRESH SOURCES
→ DISCOVER CURRENT CHARACTERS / EDGES
→ COMPARE OLD EDGE vs CURRENT EDGE
→ CLASSIFY DELTA
→ ADD NEW ENTRANTS
→ RETIRE / SUSPEND ENDED EDGES
→ RECOMPUTE AFFECTED LOCAL WEBS
→ PROPAGATE TO MAIN STORY
```

Relationship delta states:

```text
NEW
SAME
STRENGTHENED
WEAKENED
CHANGED_TYPE
SUSPENDED
ENDED
```

A character can remain in memory historically while leaving the active story if the relationship that connected it has ended.

Each material character also retains a **local web head** so future runs resume that character's own subsidiaries/customers/partners/regulators/financing graph rather than treating the character as a flat node.

## STORY DELTA

A new item changes story memory only if it materially changes one or more:

```text
CHARACTER STATE
QUALITATIVE TRAIT / BEHAVIOR SIGNATURE
ARCHETYPE / TRANSFORMATION STATE
RELATIONSHIP
OWNERSHIP / CONTROL
ECONOMICS
FINANCING / DILUTION
TIMING / RHYTHM
REGULATORY PERMISSION
SHAREHOLDER CAPTURE
SOURCE AUTHORITY
THESIS
WINDOW
STRATEGY HANDOFF
```

Tiny factual refreshes can update source freshness without rewriting the full story.

## LOSSLESS + OPERATIONAL

Story memory does not replace deep-analysis memory.

Use both:

```text
LOSSLESS ANALYSIS / STORY
→ preserves full finished reasoning artifact

STORY MEMORY HEAD
→ fast operational state

EVIDENCE / TIMERS / GRAPHS
→ atomic supporting state
```

## FAIL-CLOSED CONDITIONS

Story memory is incomplete when:
- a material character is unexpanded inside the active depth budget;
- a material relationship edge has no current state or provenance;
- a new material character entered a local web but is absent from memory;
- an ended/changed relationship remains active without revalidation;
- a subsidiary/material child has no local-web disposition;
- a material source branch is stale/blocked without disclosure;
- the story has no provenance pointer;
- a material conclusion disappears between lossless story and operational memory;
- the stored thesis is based on a superseded material state;
- a material character is forced into an archetype despite contradictory evidence;
- an active Writer branch has no frozen current-state basis or observable invalidation.

## OUTPUT

```text
STORY MEMORY STATUS:
LATEST STORY ID:
LOAD-FIRST READY:
DELTA REFRESH TARGETS:
MATERIAL STORY CHANGES:
NEXT MEMORY VERSION REQUIRED?:
```

## SOFTWARE / HARD-LIMIT BOUNDARY

Floware determines story meaning and what changed.

Deterministic software/state storage is justified for:
- persistence;
- versioning;
- identity;
- provenance pointers;
- schema validation;
- atomic writes.
