"""Restore a validated memory snapshot into an empty database."""
import json
import sqlite3
from pathlib import Path


def restore_snapshot(db_path: str, schema_path: str, snapshot_path: str) -> None:
    data = json.loads(Path(snapshot_path).read_text(encoding="utf-8"))
    with sqlite3.connect(db_path) as db:
        db.executescript(Path(schema_path).read_text(encoding="utf-8"))
        for table, rows in data.get("tables", {}).items():
            if not rows:
                continue
            columns = list(rows[0])
            placeholders = ",".join("?" for _ in columns)
            sql = f"INSERT OR REPLACE INTO {table} ({','.join(columns)}) VALUES ({placeholders})"
            for row in rows:
                db.execute(sql, [row[c] for c in columns])
        db.commit()
