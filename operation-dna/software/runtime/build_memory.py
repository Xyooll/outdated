"""Persistent engineering memory for self-build attempts and repair outcomes."""
from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
import json
import re
from typing import Iterable


@dataclass(frozen=True)
class BuildMemoryRecord:
    name: str
    goal: str
    iteration: int
    syntax_ok: bool
    tests_ok: bool
    reason: str
    repair: str = ""
    resolved: bool = False


class BuildMemory:
    def __init__(self, path: str = "data/self_build_memory.jsonl"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def record(self, item: BuildMemoryRecord) -> None:
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(asdict(item), sort_keys=True) + "\n")

    def records(self) -> list[BuildMemoryRecord]:
        if not self.path.exists():
            return []
        result: list[BuildMemoryRecord] = []
        for line in self.path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                result.append(BuildMemoryRecord(**json.loads(line)))
        return result

    def matching_failures(self, reason: str, limit: int = 5) -> list[BuildMemoryRecord]:
        tokens = set(re.findall(r"[a-z0-9_]+", reason.lower()))
        scored = []
        for record in self.records():
            rt = set(re.findall(r"[a-z0-9_]+", record.reason.lower()))
            score = len(tokens & rt)
            if score:
                scored.append((score, record))
        scored.sort(key=lambda pair: pair[0], reverse=True)
        return [record for _, record in scored[:limit]]

    def successful_repairs(self, reason: str, limit: int = 5) -> list[str]:
        return [r.repair for r in self.matching_failures(reason, limit) if r.resolved and r.repair]

    def summary(self) -> dict[str, int]:
        rows = self.records()
        return {
            "attempts": len(rows),
            "successful": sum(r.tests_ok for r in rows),
            "failed": sum(not r.tests_ok for r in rows),
            "resolved": sum(r.resolved for r in rows),
        }
