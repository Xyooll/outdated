"""Reusable intelligence queries for the world graph."""


def entities_by_type(db, entity_type: str) -> list[dict]:
    rows = db.execute(
        "SELECT id, name, confidence, updated_at FROM entities WHERE type=? ORDER BY confidence DESC",
        (entity_type,),
    ).fetchall()
    return [{"id": r[0], "name": r[1], "confidence": r[2], "updated_at": r[3]} for r in rows]


def relationship_network(db, entity_id: str, max_hops: int = 2) -> set[str]:
    """Breadth-first traversal with a hard hop limit."""
    seen = {entity_id}
    frontier = {entity_id}
    for _ in range(max_hops):
        if not frontier:
            break
        placeholders = ",".join("?" for _ in frontier)
        rows = db.execute(
            f"SELECT from_id, to_id FROM relationships WHERE from_id IN ({placeholders}) OR to_id IN ({placeholders})",
            tuple(frontier) + tuple(frontier),
        ).fetchall()
        next_frontier = set()
        for a, b in rows:
            for node in (a, b):
                if node not in seen:
                    seen.add(node)
                    next_frontier.add(node)
        frontier = next_frontier
    return seen
