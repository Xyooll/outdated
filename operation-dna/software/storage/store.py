"""Single SQLite persistence layer for all Operation DNA memory."""
import json
import sqlite3
from pathlib import Path
from typing import Any


class MemoryStore:
    def __init__(self, path: str | Path):
        self.path = str(path)
        Path(self.path).parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(self.path)
        self.db.execute("PRAGMA foreign_keys = ON")

    def initialize(self, schema_path: str | Path) -> None:
        self.db.executescript(Path(schema_path).read_text(encoding="utf-8"))
        self.db.commit()

    def put_event(self, event: dict[str, Any]) -> None:
        event_id = event.get("id") or event.get("event_id")
        if not event_id:
            raise ValueError("event requires id or event_id")
        self.db.execute("""INSERT OR REPLACE INTO events
            (id, source, event_type, title, url, published_at, data_json, ingested_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'))""",
            (event_id, event.get("source") or "unknown", event.get("event_type"),
             event.get("title") or "untitled", event.get("url"),
             event.get("published_at") or event.get("timestamp"),
             json.dumps(event, sort_keys=True)))
        self.db.commit()

    @staticmethod
    def candidate_key(item: dict[str, Any]) -> str:
        sources = ",".join(sorted(map(str, item.get("source_ids", []))))
        return f"{item.get('domain','')}|{item.get('name','')}|{sources}"

    def put_opportunity(self, item: dict[str, Any]) -> None:
        key = item.get("candidate_key") or self.candidate_key(item)
        self.db.execute("""INSERT INTO opportunities
            (candidate_key,name,domain,score,source_ids_json,data_json)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(candidate_key) DO UPDATE SET
              score=excluded.score, source_ids_json=excluded.source_ids_json,
              data_json=excluded.data_json, updated_at=CURRENT_TIMESTAMP""",
            (key, item["name"], item["domain"], float(item.get("score", 0)),
             json.dumps(item.get("source_ids", [])), json.dumps(item, sort_keys=True)))
        self.db.commit()

    def put_experience(self, experience: dict[str, Any]) -> None:
        self.db.execute("""INSERT OR REPLACE INTO experiences
            (id, event_id, strategy_version, node_id, data_json, observed_at)
            VALUES (?, ?, ?, ?, ?, ?)""",
            (experience["id"], experience.get("event_id"), experience.get("strategy_version"),
             experience.get("node_id"), json.dumps(experience, sort_keys=True), experience["observed_at"]))
        self.db.commit()

    def top_opportunities(self, limit: int = 25) -> list[dict[str, Any]]:
        limit = max(1, min(int(limit), 500))
        rows = self.db.execute("SELECT data_json FROM opportunities ORDER BY score DESC, updated_at DESC LIMIT ?", (limit,)).fetchall()
        return [json.loads(row[0]) for row in rows]

    def close(self) -> None:
        self.db.close()
