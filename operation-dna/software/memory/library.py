"""Persistent library for Xyool's memory and source material.

The library deliberately stores records as ordinary JSONL so it remains portable,
inspectable, and easy for Xyool to extend without committing to one database.
"""
from __future__ import annotations
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any, Iterable

@dataclass(frozen=True)
class MemoryRecord:
    id: str
    kind: str
    content: str
    source: str = ""
    objective: str = ""
    metadata: dict[str, Any] | None = None
    created_at: str = ""

class MemoryLibrary:
    """Append-only memory library with explicit provenance."""
    def __init__(self, root: str | Path = "data/library") -> None:
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.records = self.root / "records.jsonl"

    def add(self, kind: str, content: str, *, source: str = "", objective: str = "",
            metadata: dict[str, Any] | None = None, record_id: str | None = None) -> MemoryRecord:
        stamp = datetime.now(timezone.utc).isoformat()
        rid = record_id or f"mem-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S%f')}"
        record = MemoryRecord(rid, kind, content, source, objective, metadata or {}, stamp)
        with self.records.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(asdict(record), ensure_ascii=False, default=str) + "\n")
        return record

    def iter_records(self) -> Iterable[MemoryRecord]:
        if not self.records.exists():
            return
        with self.records.open("r", encoding="utf-8") as fh:
            for line in fh:
                if line.strip():
                    data = json.loads(line)
                    yield MemoryRecord(**data)

    def recent(self, limit: int = 20) -> list[MemoryRecord]:
        return list(self.iter_records())[-max(1, limit):]
