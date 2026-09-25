# FLOW — Novelty Enhancer

FLOW ID: CORE-NOVELTY-ENHANCER
STATUS: **CANDIDATE / VERIFICATION_PENDING**
DOMAIN: core
JOB: intentionally increase conceptual novelty for creative/generative work while preserving hard constraints and separating invention from evidence
AUTHORITY: candidate generation only; no factual, empirical, or action authority
PARENT GOALPOST: supplied by creative/development/story objective
UPSTREAM FLOWS: Correspondence, Meaning Attribution, Story Reader/Writer, Development, Domain Library
DOWNSTREAM FLOWS: Story Writer, Development, creative domain Flows, Evaluation when comparing candidates
INBOUND PIPES: PLUMBING.md#pipe-core-correspondence-novelty
OUTBOUND PIPES: PLUMBING.md#pipe-core-novelty-story-writer, PLUMBING.md#pipe-core-novelty-development
SOFTWARE DEPENDENCIES: none

## GOAL

Generate candidates that are meaningfully less obvious than the baseline without becoming random, incoherent, or falsely factual.

Core law:

> **Novelty should increase distance from the obvious while preserving the constraints that make the result useful.**

## GOALPOST

A novelty pass is sufficient when a baseline exists, hard constraints are frozen, novelty budget is declared, operators are traceable, outputs are structurally distinct, invention is separated from evidence, and coherence/usefulness remains evaluable.

## INPUT STATE

Creative/development objective; baseline candidate; hard constraints; soft preferences; available meanings/archetypes/correspondences; allowed invention authority; novelty budget.

## EVIDENCE

Novelty may use evidence-backed structures, symbolic meanings, correspondences, creative inventions, and domain libraries. Provenance should remain visible where factual or source-derived content participates.

## NOVELTY BUDGET

LOW = small variation around familiar structure.
MEDIUM = one or two meaningful structural departures.
HIGH = multiple cross-domain or structural transformations.
EXPERIMENTAL = deliberately remote combinations; coherence must be re-earned.

Novelty budget controls exploration, not quality.

## NOVELTY OPERATORS

Correspondence jump — import a structural invariant from a distant domain while stripping local nouns/calibration.

Semantic recombination — combine intrinsic/extrinsic meanings or primitives that rarely co-occur.

Inversion — reverse a default relationship, hierarchy, polarity, or causal direction.

Scale shift — move the structure across micro/macro, personal/systemic, local/global, short/long horizons.

Re-root — make a peripheral character/object/process the central viewpoint.

Constraint mutation — alter one soft assumption while freezing hard constraints.

Temporal displacement — move the structure earlier/later, cyclical/recursive, or outside its default sequence.

Contradiction fusion — preserve two conflicting ideas and search for a structure that makes both locally true.

Ontology swap — re-express the same function as story, graph, ritual, game, ecosystem, market, language, architecture, etc.

Sparse perturbation — change a small number of non-critical dimensions to escape a conceptual local minimum.

## PROCESS

FREEZE GOAL + HARD CONSTRAINTS
-> GENERATE / IDENTIFY BASELINE
-> CHOOSE NOVELTY BUDGET
-> SELECT DIVERGENCE OPERATORS
-> GENERATE DISTINCT CANDIDATES
-> RECORD OPERATOR LINEAGE / MEANING SOURCES / INVENTED ELEMENTS
-> CHECK HARD-CONSTRAINT RETENTION
-> CHECK STRUCTURAL DISTINCTNESS
-> CHECK COHERENCE / USEFULNESS
-> REMOVE COSMETIC DUPLICATES
-> RETURN DIVERSE CANDIDATE SET
-> OPTIONAL EVALUATION / SELECTION ELSEWHERE

## GATES

Creative/generative authority must be explicit; hard constraints must be frozen; evidence-bound facts may not be silently mutated; novelty must be structural rather than only lexical.

## ADAPTATION

Art/fiction/design may use HIGH or EXPERIMENTAL novelty. Development/architecture should usually prefer MEDIUM novelty and preserve a path back to constraints. Evidence-sensitive domains may use novelty to generate questions/hypotheses only.

## BOUNDARIES

The Novelty Enhancer does not make a candidate true, override evidence, promote hypotheses, rewrite source history, bypass safety/authority, or inject invented facts into evidence-bound Reader state.

## FAIL-CLOSED CONDITIONS

Return NOVELTY_BLOCKED when factual fidelity forbids invention, hard constraints are unknown, consequence is high and novelty would alter factual/action state, or candidate lineage cannot distinguish invention from evidence.

## OUTPUT STATE

NOVELTY STATUS; BASELINE; NOVELTY BUDGET; HARD CONSTRAINTS; CANDIDATES[] with candidate_id, description, operators_used, correspondence_sources, meaning_sources, invented_elements, preserved_constraints, coherence_notes, novelty_notes; EVALUATION REQUIRED.

## LEARNING HOOK

Creative/development evaluation may reveal which operators generate useful originality, which generate noise, where novelty collapses coherence, and where supposedly novel candidates were superficial variation.

## SOFTWARE / HARD-LIMIT BOUNDARY

NONE — FLOWARE SUFFICIENT

## COMPLEXITY RULE

Use the fewest novelty operations needed to escape the obvious solution. More mutation is not automatically more creative.