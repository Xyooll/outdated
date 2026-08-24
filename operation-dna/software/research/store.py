"""Small SQLite persistence layer for research events and opportunity candidates."""
import json
import sqlite3
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS research_events (id TEXT PRIMARY KEY, payload TEXT NOT NULL, created_at TEXT DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS opportunity_candidates (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, domain TEXT NOT NULL, score REAL NOT NULL, payload TEXT NOT NULL, created_at TEXT DEFAULT CURRENT_TIMESTAMP);
CREATE INDEX IF NOT EXISTS idx_candidates_score ON opportunity_candidates(score DESC);
"""

class ResearchStore:
    def __init__(self, path: str = "data/research.db"):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(path)
        self.db.executescript(SCHEMA)
        self.db.commit()

    def save(self, item: dict) -> None:
        if item.get("type") == "opportunity_candidate":
            self.db.execute("INSERT INTO opportunity_candidates(name, domain, score, payload) VALUES (?, ?, ?, ?)", (item["name"], item["domain"], item["score"], json.dumps(item)))
        else:
            key = str(item.get("event_id") or item.get("id") or hash(json.dumps(item, sort_keys=True)))
            self.db.execute("INSERT OR IGNORE INTO research_events(id, payload) VALUES (?, ?)", (key, json.dumps(item)))
        self.db.commit()

    def top_candidates(self, limit: int = 25):
        rows = self.db.execute("SELECT payload FROM opportunity_candidates ORDER BY score DESC LIMIT ?", (limit,)).fetchall()
        return [json.loads(row[0]) for row in rows]

    def close(self):
        self.db.close()
