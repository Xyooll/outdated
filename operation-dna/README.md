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

### Economic engine
Business, investment and trading candidates use a shared opportunity model, evidence gate, capital-efficiency ranking, experiment framework and outcome loop.

### Research/data adapters
Read-only adapters now support SEC company facts, Alpaca market data and CoinGecko crypto market data. A canonical event model converts provider-specific payloads into the common research pipeline.

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
- business/investment/trading opportunity scanners
- deterministic backtesting foundation
- SEC company-facts ingestion
- Alpaca stock/crypto market-data ingestion
- CoinGecko crypto-market ingestion
- canonical research-event normalization
- research pipeline tests

## Data providers

Provider credentials are never stored in the DNA. Environment variables or a secrets manager supply credentials at runtime.

The current adapters are intentionally read-only. They feed research and backtesting; they do not place trades or spend funds.

## Deliberate boundary

Live external execution, credentials, autonomous privileged deployment, and production trading are adapters—not implicit powers of the AI. They must be explicitly provisioned behind the safety layer.
