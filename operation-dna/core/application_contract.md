# Common Application Contract

Every application is an organ of the same adaptive operating system.

## Required stages

1. `perceive` — receive observations from approved sources.
2. `understand` — normalize observations into canonical entities/events.
3. `hypothesize` — produce explicit hypotheses with evidence and confidence.
4. `test` — evaluate hypotheses using deterministic or isolated experiments.
5. `act` — request an action through the safety gate.
6. `observe` — capture actual outcomes.
7. `learn` — convert outcomes into experience and lessons.
8. `evolve` — propose versioned improvements through the learning engine.

## Required interfaces

An application must be able to reference:

- canonical entities and relationships
- evidence/provenance
- memory/experience
- strategy or procedure versions
- safety/authorization state
- node/runtime context
- evaluation results

## Boundary

Applications may specialize reasoning, metrics and actions for their domain. They cannot bypass core provenance, safety, audit, memory, or rollback controls.

## Application-neutral result

Applications should return structured results containing:

- status
- observations
- hypothesis/decision where applicable
- evidence references
- requested action
- gate result
- outcome
- lessons
- version
