"""Fast discovery index for the Xyool repository and memory library."""
from __future__ import annotations
from dataclasses import asdict, dataclass
import hashlib
import json
from pathlib import Path
from typing import Iterable

@dataclass(frozen=True)
class IndexEntry:
    path: str
    kind: str
    size: int
    sha256: str
    terms: tuple[str, ...]

class MemoryIndexer:
    """Build a lightweight lexical index without imposing a fixed resource taxonomy."""
    DEFAULT_SUFFIXES = {".md", ".txt", ".json", ".jsonl", ".py", ".yaml", ".yml"}
    SKIP_DIRS = {".git", ".venv", "__pycache__", "build", "dist"}

    def __init__(self, root: str | Path = ".", index_file: str | Path = "data/library/index.json") -> None:
        self.root = Path(root).resolve()
        self.index_file = Path(index_file)
        self.index_file.parent.mkdir(parents=True, exist_ok=True)

    def build(self, suffixes: set[str] | None = None) -> list[IndexEntry]:
        allowed = suffixes or self.DEFAULT_SUFFIXES
        entries: list[IndexEntry] = []
        for path in self._files():
            try:
                data = path.read_bytes()
                text = data.decode("utf-8", errors="ignore")
            except OSError:
                continue
            terms = tuple(sorted(set(self._terms(text + " " + path.name))))
            kind = "documentation" if path.suffix.lower() == ".md" else "code" if path.suffix.lower() == ".py" else "data"
            entries.append(IndexEntry(str(path.relative_to(self.root)), kind, len(data), hashlib.sha256(data).hexdigest(), terms))
        payload = {"version": 1, "root": str(self.root), "entries": [asdict(e) for e in entries]}
        self.index_file.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        return entries

    def search(self, query: str, limit: int = 20) -> list[IndexEntry]:
        if not self.index_file.exists():
            self.build()
        payload = json.loads(self.index_file.read_text(encoding="utf-8"))
        q = set(self._terms(query))
        scored = []
        for raw in payload.get("entries", []):
            entry = IndexEntry(**raw)
            score = len(q.intersection(entry.terms))
            if score:
                scored.append((score, entry))
        scored.sort(key=lambda item: (-item[0], item[1].path))
        return [entry for _, entry in scored[:limit]]

    def _files(self) -> Iterable[Path]:
        for path in self.root.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in self.DEFAULT_SUFFIXES:
                continue
            if any(part in self.SKIP_DIRS for part in path.parts):
                continue
            yield path

    @staticmethod
    def _terms(text: str) -> Iterable[str]:
        import re
        for term in re.findall(r"[A-Za-z0-9_./-]{3,}", text.lower()):
            yield term
