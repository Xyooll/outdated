"""Persistent world-graph queries over the SQLite memory store."""
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Edge:
    from_id: str
    relation: str
    to_id: str
    confidence: float


def add_edge(db, edge: Edge, evidence: list[str] | None = None) -> None:
    import json
    db.execute(
        """INSERT OR REPLACE INTO relationships
        (id, from_id, type, to_id, data_json, confidence, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, datetime('now'), datetime('now'))""",
        (f"{edge.from_id}:{edge.relation}:{edge.to_id}", edge.from_id,
         edge.relation, edge.to_id, json.dumps({"evidence": evidence or []}), edge.confidence),
    )
    db.commit()


def neighbors(db, entity_id: str, relation: str | None = None) -> list[dict[str, Any]]:
    if relation:
        rows = db.execute(
            "SELECT from_id, type, to_id, confidence FROM relationships WHERE from_id=? AND type=?",
            (entity_id, relation),
        ).fetchall()
    else:
        rows = db.execute(
            "SELECT from_id, type, to_id, confidence FROM relationships WHERE from_id=? OR to_id=?",
            (entity_id, entity_id),
        ).fetchall()
    return [{"from_id": r[0], "relation": r[1], "to_id": r[2], "confidence": r[3]} for r in rows]


def related(db, entity_id: str, relation: str | None = None) -> list[dict[str, Any]]:
    """Return connected entities, useful for application-level intelligence queries."""
    return neighbors(db, entity_id, relation)
