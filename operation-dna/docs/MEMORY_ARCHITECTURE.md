# Xyool Memory Architecture

Memory is an environment resource, not a single prompt or database.

## Layers

- **Working memory** — current objective, active context, recent observations, unresolved state.
- **Semantic memory** — durable knowledge and concepts.
- **Experience memory** — what Xyool attempted, what happened, conditions, and lessons.
- **Exact archive** — source material that must remain retrievable verbatim.

## Library

Persistent material is organized as a library under `data/library/`. Records use JSONL so the storage remains portable and inspectable. Larger source collections can live beside the record store without changing the retrieval contract.

## Index

`software/memory/indexer.py` builds a lightweight discovery index over repository documentation, code, and data. The index answers **where should I look?** It is not the memory itself.

## Retrieval

`software/memory/retrieval.py` combines indexed repository resources with stored memory. Retrieval should optimize for relevance while keeping access cost in mind. More advanced vector, graph, cache, or model-based retrieval can be added later without changing the library contract.

## Aggregation

`software/memory/aggregation.py` creates source-preserving bundles for higher-level reasoning. Aggregation must retain provenance and meaningful disagreement rather than flattening conflicting evidence.

## Design rule

The AI decides when memory is useful and what information it needs. The memory software provides storage, discovery, retrieval, and aggregation mechanisms; it does not decide the objective or final conclusion.
