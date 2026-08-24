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
        self._ensure_compatible_schema()
        self.db.commit()

    def initialize_schema(self, schema: str) -> None:
        """Initialize from an in-memory schema and apply additive migrations."""
        self.db.executescript(schema)
        self._ensure_compatible_schema()
        self.db.commit()

    def _ensure_compatible_schema(self) -> None:
        """Apply safe, additive changes to databases created by older versions."""
        event_columns = {row[1] for row in self.db.execute("PRAGMA table_info(events)")}
        if event_columns and "event_type" not in event_columns:
            self.db.execute("ALTER TABLE events ADD COLUMN event_type TEXT")

        self.db.execute("""CREATE TABLE IF NOT EXISTS opportunities (
            candidate_key TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            domain TEXT NOT NULL,
            score REAL NOT NULL,
            source_ids_json TEXT,
            data_json TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )""")
        self.db.execute("CREATE INDEX IF NOT EXISTS idx_opportunities_score ON opportunities(score DESC)")

    def put_event(self, event: dict[str, Any]) -> None:
        event_id = event.get("id") or event.get("event_id")
        if not event_id:
            raise ValueError("event requires id or event_id")
        self.db.execute("""INSERT OR REPLACE INTO events
            (id, source, event_type, title, url, published_at, data_json, ingested_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'))""",
            (event_id, event.get("source") or "unknown", event.get("event_type") or event.get("category"),
             event.get("title") or "untitled", event.get("url"),
             event.get("published_at") or event.get("timestamp"),
             json.dumps(event, sort_keys=True)))
        self.db.commit()

    @staticmethod
    def candidate_key(item: dict[str, Any]) -> str:
        """Stable identity for an opportunity independent of changing source lists."""
        domain = str(item.get("domain", "")).strip().lower()
        name = " ".join(str(item.get("name", "")).split()).strip().lower()
        return f"{domain}|{name}"

    def put_opportunity(self, item: dict[str, Any]) -> None:
        if not item.get("name") or not item.get("domain"):
            raise ValueError("opportunity requires name and domain")
        key = item.get("candidate_key") or self.candidate_key(item)
        self.db.execute("""INSERT INTO opportunities
            (candidate_key,name,domain,score,source_ids_json,data_json)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(candidate_key) DO UPDATE SET
              name=excluded.name, domain=excluded.domain, score=excluded.score,
              source_ids_json=excluded.source_ids_json,
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
