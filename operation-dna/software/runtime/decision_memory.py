"""Persistent decision performance memory."""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class DecisionRecord:
    decision_id: str
    strategy: str
    action: str
    confidence: float
    realized_pnl: float
    direction_correct: bool


class DecisionMemory:
    def __init__(self, path: str = "data/learning/decisions.json"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.records: list[DecisionRecord] = []
        self._load()

    def record(self, result: DecisionRecord) -> None:
        self.records.append(result)
        self._save()

    def summary(self, strategy: str | None = None) -> dict:
        rows = [r for r in self.records if strategy is None or r.strategy == strategy]
        if not rows:
            return {"samples": 0, "direction_accuracy": 0.0, "mean_pnl": 0.0, "total_pnl": 0.0}
        return {
            "samples": len(rows),
            "direction_accuracy": sum(r.direction_correct for r in rows) / len(rows),
            "mean_pnl": sum(r.realized_pnl for r in rows) / len(rows),
            "total_pnl": sum(r.realized_pnl for r in rows),
        }

    def _load(self) -> None:
        if self.path.exists():
            self.records = [DecisionRecord(**r) for r in json.loads(self.path.read_text(encoding="utf-8"))]

    def _save(self) -> None:
        self.path.write_text(json.dumps([asdict(r) for r in self.records], sort_keys=True), encoding="utf-8")
