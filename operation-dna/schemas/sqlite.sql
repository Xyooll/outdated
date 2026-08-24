PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS entities (
  id TEXT PRIMARY KEY,
  type TEXT NOT NULL,
  name TEXT NOT NULL,
  aliases TEXT,
  identifiers TEXT,
  geography TEXT,
  tags TEXT,
  attributes TEXT,
  confidence REAL,
  created_at TEXT,
  updated_at TEXT,
  last_verified TEXT
);

CREATE TABLE IF NOT EXISTS relationships (
  id TEXT PRIMARY KEY,
  from_entity TEXT NOT NULL REFERENCES entities(id),
  type TEXT NOT NULL,
  to_entity TEXT NOT NULL REFERENCES entities(id),
  evidence TEXT,
  confidence REAL,
  valid_from TEXT,
  valid_to TEXT,
  last_verified TEXT
);

CREATE TABLE IF NOT EXISTS events (
  id TEXT PRIMARY KEY,
  type TEXT NOT NULL,
  occurred_at TEXT NOT NULL,
  summary TEXT NOT NULL,
  impact REAL,
  novelty REAL,
  relevance REAL,
  confidence REAL,
  sources TEXT
);

CREATE TABLE IF NOT EXISTS sources (
  id TEXT PRIMARY KEY,
  type TEXT NOT NULL,
  name TEXT NOT NULL,
  uri TEXT,
  publisher TEXT,
  retrieved_at TEXT,
  reliability REAL
);

CREATE INDEX IF NOT EXISTS idx_entities_type ON entities(type);
CREATE INDEX IF NOT EXISTS idx_entities_name ON entities(name);
CREATE INDEX IF NOT EXISTS idx_relationships_from ON relationships(from_entity);
CREATE INDEX IF NOT EXISTS idx_relationships_to ON relationships(to_entity);
CREATE INDEX IF NOT EXISTS idx_relationships_type ON relationships(type);
CREATE INDEX IF NOT EXISTS idx_events_time ON events(occurred_at);
