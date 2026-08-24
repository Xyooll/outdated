"""Detect conflicting claims without destroying historical state."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Claim:
    subject: str
    relation: str
    object: str
    event_id: str
    confidence: float

@dataclass(frozen=True)
class Conflict:
    subject: str
    relation: str
    existing: Claim
    incoming: Claim


def find_conflicts(existing: list[Claim], incoming: Claim) -> list[Conflict]:
    return [Conflict(incoming.subject, incoming.relation, old, incoming)
            for old in existing
            if old.subject == incoming.subject
            and old.relation == incoming.relation
            and old.object != incoming.object]
