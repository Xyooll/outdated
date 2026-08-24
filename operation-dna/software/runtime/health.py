"""Runtime health checks."""
from pathlib import Path
from typing import Any

def check_database(path: str) -> dict[str, Any]:
    try:
        import sqlite3
        with sqlite3.connect(path) as db:
            db.execute("SELECT 1")
        return {"name": "database", "ok": True}
    except Exception as exc:
        return {"name": "database", "ok": False, "error": type(exc).__name__}

def check_storage(path: str) -> dict[str, Any]:
    p = Path(path)
    try:
        p.parent.mkdir(parents=True, exist_ok=True)
        return {"name": "storage", "ok": True}
    except Exception as exc:
        return {"name": "storage", "ok": False, "error": type(exc).__name__}

def check_runtime(db_path: str, audit_path: str) -> dict[str, Any]:
    checks = [check_database(db_path), check_storage(audit_path)]
    return {"ok": all(c["ok"] for c in checks), "checks": checks}
