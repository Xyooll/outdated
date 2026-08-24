"""Relationship candidate generation with explicit provenance."""
from dataclasses import dataclass


@dataclass(frozen=True)
class RelationshipCandidate:
    from_mention: str
    relation: str
    to_mention: str
    evidence_event_id: str
    confidence: float


def propose_relationship(from_mention: str, relation: str, to_mention: str,
                         event_id: str, confidence: float = 0.5) -> RelationshipCandidate:
    """Create a proposal; resolution and promotion belong to a later validation stage."""
    return RelationshipCandidate(from_mention, relation, to_mention, event_id, confidence)
