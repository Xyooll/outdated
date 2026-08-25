"""Append-only AI activity log. Raw events are facts; memory is interpretation."""
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any

@dataclass(frozen=True)
class AIEvent:
    event_type: str
    objective: str = ""
    trigger: str = ""
    attention_score: float = 0.0
    context: dict[str, Any] | None = None
    plan: dict[str, Any] | None = None
    capabilities: list[str] | None = None
    actions: list[dict[str, Any]] | None = None
    result: dict[str, Any] | None = None
    expected_outcome: Any = None
    actual_outcome: Any = None
    error: str | None = None
    confidence: float | None = None
    cost: float | None = None
    human_intervention: bool = False
    lessons: list[str] | None = None
    timestamp: str = ""
    session_id: str = ""

class EventLog:
    def __init__(self, path: str = "data/logs/ai_events.jsonl"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, event: AIEvent) -> None:
        if not event.event_type:
            raise ValueError("event_type is required")
        record = asdict(event)
        record["timestamp"] = event.timestamp or datetime.now(timezone.utc).isoformat()
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")

    def read(self, limit: int = 100) -> list[dict[str, Any]]:
        if limit <= 0:
            return []
        if not self.path.exists():
            return []
        lines = self.path.read_text(encoding="utf-8").splitlines()[-limit:]
        return [json.loads(line) for line in lines]
