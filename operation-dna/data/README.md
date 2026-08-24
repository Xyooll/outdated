# Canonical Data Layer

Markdown/YAML records are the portable source of truth. A generated SQLite index should be treated as a derived artifact and rebuilt from these records.

## Record families

- `entities/` — canonical entities
- `relationships/` — typed connections
- `events/` — dated occurrences and catalysts
- `sources/` — evidence and provenance
- `research/` — synthesized analysis

Every factual relationship should carry evidence and confidence. Prefer primary sources. Never put credentials or private keys in this tree.
