"""Canonical Operation DNA memory schema."""
SCHEMA = '''
CREATE TABLE IF NOT EXISTS events (
  id TEXT PRIMARY KEY,
  source TEXT NOT NULL,
  event_type TEXT,
  title TEXT,
  url TEXT,
  published_at TEXT,
  data_json TEXT NOT NULL,
  ingested_at TEXT DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_events_source_time ON events(source, published_at);
CREATE TABLE IF NOT EXISTS opportunities (
  candidate_key TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  domain TEXT NOT NULL,
  score REAL NOT NULL,
  source_ids_json TEXT,
  data_json TEXT NOT NULL,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_opportunities_score ON opportunities(score DESC);
CREATE TABLE IF NOT EXISTS experiences (
  id TEXT PRIMARY KEY,
  event_id TEXT,
  strategy_version TEXT,
  node_id TEXT,
  data_json TEXT NOT NULL,
  observed_at TEXT NOT NULL,
  FOREIGN KEY(event_id) REFERENCES events(id) ON DELETE SET NULL
);
'''
