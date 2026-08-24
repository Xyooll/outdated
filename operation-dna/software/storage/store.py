"""Small SQLite persistence layer for Operation DNA memory."""
import json
import sqlite3
from pathlib import Path
from typing import Any


class MemoryStore:
    def __init__(self, path: str | Path):
        self.path = str(path)
        self.db = sqlite3.connect(self.path)
        self.db.execute("PRAGMA foreign_keys = ON")

    def initialize(self, schema_path: str | Path) -> None:
        schema = Path(schema_path).read_text(encoding="utf-8")
        self.db.executescript(schema)
        self.db.commit()

    def put_event(self, event: dict[str, Any]) -> None:
        self.db.execute(
            """INSERT OR REPLACE INTO events
               (id, source, title, url, published_at, data_json, ingested_at)
               VALUES (?, ?, ?, ?, ?, ?, datetime('now'))""",
            (event["id"], event["source"], event["title"], event.get("url"),
             event.get("published_at"), json.dumps(event, sort_keys=True)),
        )
        self.db.commit()

    def put_experience(self, experience: dict[str, Any]) -> None:
        self.db.execute(
            """INSERT OR REPLACE INTO experiences
               (id, event_id, strategy_version, node_id, data_json, observed_at)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (experience["id"], experience.get("event_id"),
             experience.get("strategy_version"), experience.get("node_id"),
             json.dumps(experience, sort_keys=True), experience["observed_at"]),
        )
        self.db.commit()

    def close(self) -> None:
        self.db.close()
