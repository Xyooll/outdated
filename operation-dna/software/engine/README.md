# Operation DNA Engine

This package is the deterministic subconscious layer.

## Current pipeline primitives

```text
observations
    ↓
ingest + deduplicate
    ↓
canonical events
    ↓
AI interpretation / hypothesis
    ↓
deterministic decision gates
    ↓
action or rejection
    ↓
experience record
    ↓
evaluation
    ↓
controlled candidate promotion
```

The engine intentionally does not contain an AI provider, credentials, or live trading execution yet. Those are adapters that must sit behind the safety and permission boundaries.

## Design rule

The AI may propose. The engine validates. The executor acts. Memory records what happened.
