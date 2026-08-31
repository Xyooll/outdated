"""Context retrieval over the lightweight Xyool index and memory library."""
from __future__ import annotations
from pathlib import Path
from .indexer import MemoryIndexer
from .library import MemoryLibrary, MemoryRecord

class MemoryRetriever:
    """Choose relevant memories and repository resources without a fixed taxonomy."""
    def __init__(self, root: str | Path = ".", library: MemoryLibrary | None = None) -> None:
        self.indexer = MemoryIndexer(root)
        self.library = library or MemoryLibrary(Path(root) / "data/library")

    def retrieve(self, query: str, limit: int = 8) -> dict:
        resources = self.indexer.search(query, limit=limit)
        q = set(self.indexer._terms(query))
        memories: list[tuple[int, MemoryRecord]] = []
        for record in self.library.iter_records():
            terms = set(self.indexer._terms(record.content + " " + record.kind + " " + record.objective))
            score = len(q.intersection(terms))
            if score:
                memories.append((score, record))
        memories.sort(key=lambda item: (-item[0], item[1].created_at), reverse=False)
        return {
            "resources": [r.path for r in resources],
            "memories": [r.__dict__ for _, r in memories[:limit]],
        }
