"""Persistent layered memory plus bounded relevance retrieval."""
from dataclasses import dataclass, asdict
import json
from pathlib import Path
from typing import Any

@dataclass(frozen=True)
class MemoryItem:
    kind: str
    key: str
    content: Any
    metadata: dict[str, Any]

class MemoryStore:
    def __init__(self, path: str = "data/memory.jsonl"):
        self.path = Path(path); self.path.parent.mkdir(parents=True, exist_ok=True)
    def put(self, item: MemoryItem) -> None:
        if item.kind not in {"episodic", "semantic", "procedural"}: raise ValueError("invalid memory kind")
        with self.path.open("a", encoding="utf-8") as f: f.write(json.dumps(asdict(item), default=str) + "\n")
    def search(self, query: str, kind: str | None = None, limit: int = 20) -> list[MemoryItem]:
        if not self.path.exists(): return []
        q=query.lower(); results=[]
        for line in self.path.read_text(encoding="utf-8").splitlines():
            if not line.strip(): continue
            raw=json.loads(line); item=MemoryItem(**raw)
            if kind and item.kind != kind: continue
            if q in json.dumps(raw, default=str).lower(): results.append(item)
        return results[-limit:]
    def retrieve_relevant(self, query: str, tags: set[str] | None = None, limit: int = 10) -> list[MemoryItem]:
        items=self.search(query, limit=1000); tags=tags or set()
        def score(item): return (len(tags & set(item.metadata.get("tags", []))), float(item.metadata.get("importance", 0)))
        return sorted(items, key=score, reverse=True)[:limit]
