"""Append-only structured audit events."""
import json
from datetime import datetime, timezone
from pathlib import Path

def record(path: str, event: dict) -> None:
    payload = {"timestamp": datetime.now(timezone.utc).isoformat(), **event}
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as f:
        f.write(json.dumps(payload, sort_keys=True) + "\n")
