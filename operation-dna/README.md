# Operation DNA

A domain-independent adaptive operating system for research, business creation, product development, operations, finance, marketing and trading.

## Architecture

```text
PERCEIVE → UNDERSTAND → HYPOTHESIZE → TEST → ACT → OBSERVE → LEARN → EVOLVE
```

### Mind
AI provides interpretation, reasoning, hypotheses, planning and strategy proposals.

### Subconscious
Deterministic software handles ingestion, normalization, calculation, validation, monitoring and execution.

### Memory
SQLite-backed entities, relationships, events and experiences provide persistent operational memory.

### Intelligence
Evidence, entity resolution, relationship candidates and a validated world graph turn observations into structured knowledge.

### Safety
Hard gates, authorization, risk limits, reversibility, auditability and protected invariants constrain action.

### Evolution
Candidates are isolated, tested against baselines, stress-tested, shadowed where applicable, and promoted only when evidence and safety gates pass.

### Applications
Trading, business, research, product, marketing, finance and operations are interchangeable application organs built on the same core.

### Geographic cloning
The DNA is portable. Nodes can be recreated in multiple regions from versioned source and schema plus node-local configuration. Secrets and privileged permissions are provisioned independently.

## Current implementation

The repository contains working primitives for:

- RSS/Atom ingestion
- event normalization and deduplication
- SQLite memory
- entity/relationship storage
- entity resolution
- evidence scoring
- world-graph queries
- conflict-aware knowledge updates
- safety policy evaluation
- application lifecycle orchestration
- append-only audit logging
- learning candidate evaluation
- node manifests and replication rules
- core and intelligence tests

## Deliberate boundary

Live external execution, credentials, autonomous privileged deployment, and production trading are adapters—not implicit powers of the AI. They must be explicitly provisioned behind the safety layer.
