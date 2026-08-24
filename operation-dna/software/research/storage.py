"""SQLite persistence for research events and opportunity candidates."""
import json
import sqlite3
from pathlib import Path

SCHEMA = '''
CREATE TABLE IF NOT EXISTS events (
  event_id TEXT PRIMARY KEY, source TEXT, event_type TEXT, timestamp TEXT,
  title TEXT, payload_json TEXT NOT NULL, created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS opportunities (
  id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, domain TEXT NOT NULL,
  score REAL NOT NULL, source_ids_json TEXT, payload_json TEXT NOT NULL,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_opportunities_score ON opportunities(score DESC);
CREATE INDEX IF NOT EXISTS idx_events_source_time ON events(source, timestamp);
'''

class ResearchStore:
    def __init__(self, path: str = "data/research.db"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(self.path)
        self.conn.executescript(SCHEMA)
        self.conn.commit()

    def save(self, item):
        if isinstance(item, dict) and item.get("type") == "opportunity_candidate":
            self.conn.execute(
                "INSERT INTO opportunities(name,domain,score,source_ids_json,payload_json) VALUES(?,?,?,?,?)",
                (item["name"], item["domain"], item["score"], json.dumps(item.get("source_ids", [])), json.dumps(item)),
            )
        else:
            event_id = item.get("event_id") or item.get("id") or f"{item.get('source')}:{item.get('timestamp')}:{item.get('title')}"
            self.conn.execute(
                "INSERT OR IGNORE INTO events(event_id,source,event_type,timestamp,title,payload_json) VALUES(?,?,?,?,?,?)",
                (event_id, item.get("source"), item.get("event_type"), item.get("timestamp"), item.get("title"), json.dumps(item)),
            )
        self.conn.commit()

    def top_opportunities(self, limit: int = 25):
        rows = self.conn.execute("SELECT payload_json FROM opportunities ORDER BY score DESC LIMIT ?", (limit,)).fetchall()
        return [json.loads(row[0]) for row in rows]

    def close(self):
        self.conn.close()
