"""Append-only structured audit events."""
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

class AuditLog:
    def __init__(self, path: str):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def record(self, event_type: str, payload: dict[str, Any]) -> None:
        entry = {"timestamp": datetime.now(timezone.utc).isoformat(), "event_type": event_type, "payload": payload}
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry, sort_keys=True) + "\n")

def record(path: str, event: dict) -> None:
    AuditLog(path).record(event.get("event_type", "event"), event)
