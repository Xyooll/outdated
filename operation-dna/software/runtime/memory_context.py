"""Memory/environment adapter exposed to the single Xyool agent."""
from __future__ import annotations
from pathlib import Path
from typing import Any
from operation_dna.software.memory.library import MemoryLibrary
from operation_dna.software.memory.retrieval import MemoryRetriever
from operation_dna.software.memory.aggregation import MemoryAggregator

class MemoryContext:
    """One model-facing resource for recall, storage, indexing, and aggregation."""
    def __init__(self, root: str | Path = ".") -> None:
        self.root = Path(root).resolve()
        self.library = MemoryLibrary(self.root / "data/library")
        self.retriever = MemoryRetriever(self.root, self.library)
        self.aggregator = MemoryAggregator(self.library)

    def recall(self, query: str, limit: int = 8) -> dict[str, Any]:
        return self.retriever.retrieve(query, limit=limit)

    def remember(self, content: str, kind: str = "experience", source: str = "agent", objective: str = "", metadata: dict[str, Any] | None = None) -> dict[str, Any]:
        return self.library.add(kind, content, source=source, objective=objective, metadata=metadata).__dict__

    def index(self) -> dict[str, Any]:
        entries = self.retriever.indexer.build()
        return {"indexed": len(entries), "index": str(self.retriever.indexer.index_file)}

    def aggregate(self, query: str, limit: int = 100) -> dict[str, Any]:
        return self.aggregator.bundle(query, limit=limit)
