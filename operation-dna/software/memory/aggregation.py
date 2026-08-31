"""Source-preserving aggregation for library material."""
from __future__ import annotations
from collections import defaultdict
from dataclasses import asdict
from .library import MemoryLibrary, MemoryRecord

class MemoryAggregator:
    """Create higher-level bundles while retaining every source and disagreement."""
    def __init__(self, library: MemoryLibrary | None = None) -> None:
        self.library = library or MemoryLibrary()

    def collect(self, query: str, limit: int = 100) -> list[MemoryRecord]:
        terms = set(query.lower().split())
        records = []
        for record in self.library.iter_records():
            haystack = (record.content + " " + record.objective + " " + record.kind).lower()
            if not terms or any(term in haystack for term in terms):
                records.append(record)
        return records[-limit:]

    def bundle(self, query: str, limit: int = 100) -> dict:
        records = self.collect(query, limit)
        by_source = defaultdict(list)
        for record in records:
            by_source[record.source or "unknown"].append(asdict(record))
        return {
            "query": query,
            "records": [asdict(r) for r in records],
            "sources": dict(by_source),
            "preserves_provenance": True,
            "preserves_disagreement": True,
        }
