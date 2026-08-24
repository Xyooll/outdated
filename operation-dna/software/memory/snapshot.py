"""Portable memory snapshots without copying secrets."""
import json
import sqlite3
from pathlib import Path
from datetime import datetime, timezone

TABLES = ("entities", "relationships", "events", "experiences", "sources")

def export_snapshot(db_path: str, output_path: str) -> None:
    with sqlite3.connect(db_path) as db:
        snapshot = {"created_at": datetime.now(timezone.utc).isoformat(), "tables": {}}
        for table in TABLES:
            rows = db.execute(f"SELECT * FROM {table}").fetchall()
            columns = [d[0] for d in db.execute(f"SELECT * FROM {table} LIMIT 0").description]
            snapshot["tables"][table] = [dict(zip(columns, row)) for row in rows]
    p = Path(output_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(snapshot, indent=2, default=str), encoding="utf-8")
