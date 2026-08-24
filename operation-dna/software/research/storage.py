"""SQLite persistence for research events and opportunity candidates."""
import json
import sqlite3
from pathlib import Path

SCHEMA = '''
CREATE TABLE IF NOT EXISTS events (
  event_id TEXT PRIMARY KEY,
  source TEXT NOT NULL,
  event_type TEXT,
  published_at TEXT,
  title TEXT,
  payload_json TEXT NOT NULL,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS opportunities (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  candidate_key TEXT NOT NULL UNIQUE,
  name TEXT NOT NULL,
  domain TEXT NOT NULL,
  score REAL NOT NULL,
  source_ids_json TEXT,
  payload_json TEXT NOT NULL,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_opportunities_score ON opportunities(score DESC);
CREATE INDEX IF NOT EXISTS idx_events_source_time ON events(source, published_at);
'''


class ResearchStore:
    def __init__(self, path: str = "data/research.db"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(self.path)
        self.conn.executescript(SCHEMA)
        self.conn.commit()

    @staticmethod
    def _candidate_key(item: dict) -> str:
        source_ids = ",".join(sorted(map(str, item.get("source_ids", []))))
        return f"{item.get('domain','')}|{item.get('name','')}|{source_ids}"

    def save(self, item: dict) -> None:
        if item.get("type") == "opportunity_candidate":
            key = self._candidate_key(item)
            self.conn.execute(
                """INSERT INTO opportunities
                (candidate_key,name,domain,score,source_ids_json,payload_json)
                VALUES(?,?,?,?,?,?)
                ON CONFLICT(candidate_key) DO UPDATE SET
                  score=excluded.score,
                  source_ids_json=excluded.source_ids_json,
                  payload_json=excluded.payload_json,
                  updated_at=CURRENT_TIMESTAMP""",
                (key, item["name"], item["domain"], item["score"],
                 json.dumps(item.get("source_ids", [])), json.dumps(item, sort_keys=True)),
            )
        else:
            event_id = item.get("event_id") or item.get("id") or f"{item.get('source')}:{item.get('published_at')}:{item.get('title')}"
            self.conn.execute(
                """INSERT OR IGNORE INTO events
                (event_id,source,event_type,published_at,title,payload_json)
                VALUES(?,?,?,?,?,?)""",
                (event_id, item.get("source", "unknown"), item.get("event_type"),
                 item.get("published_at") or item.get("timestamp"), item.get("title"),
                 json.dumps(item, sort_keys=True)),
            )
        self.conn.commit()

    def top_opportunities(self, limit: int = 25) -> list[dict]:
        limit = max(1, min(int(limit), 500))
        rows = self.conn.execute(
            "SELECT payload_json FROM opportunities ORDER BY score DESC, updated_at DESC LIMIT ?",
            (limit,),
        ).fetchall()
        return [json.loads(row[0]) for row in rows]

    def close(self) -> None:
        self.conn.close()
