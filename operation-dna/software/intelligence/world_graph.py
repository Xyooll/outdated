"""Validated world-graph promotion boundary."""
from dataclasses import dataclass
from .evidence import Evidence, confidence


@dataclass(frozen=True)
class GraphEdge:
    from_id: str
    relation: str
    to_id: str
    confidence: float
    evidence_ids: list[str]


def promote_edge(from_id: str, relation: str, to_id: str,
                 evidence: list[Evidence], minimum_confidence: float = 0.75) -> GraphEdge | None:
    score = confidence(evidence)
    if score < minimum_confidence:
        return None
    return GraphEdge(from_id, relation, to_id, score, [e.event_id for e in evidence])
