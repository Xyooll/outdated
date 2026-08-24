"""Conflict-aware knowledge updates. Existing facts are preserved as history."""
from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass(frozen=True)
class FactVersion:
    entity_id: str
    relation: str
    value: str
    confidence: float
    source_ids: list[str]
    observed_at: str
    status: str = "active"

def now() -> str:
    return datetime.now(timezone.utc).isoformat()

def compare(existing: FactVersion, incoming: FactVersion) -> str:
    if existing.entity_id != incoming.entity_id or existing.relation != incoming.relation:
        return "different_fact"
    if existing.value == incoming.value:
        return "corroborates"
    if incoming.confidence > existing.confidence:
        return "contradicts_stronger"
    return "contradicts_weaker"

def resolve(existing: FactVersion, incoming: FactVersion) -> tuple[FactVersion, str]:
    relation = compare(existing, incoming)
    if relation == "corroborates":
        merged = FactVersion(existing.entity_id, existing.relation, existing.value,
                             max(existing.confidence, incoming.confidence),
                             list(dict.fromkeys(existing.source_ids + incoming.source_ids)),
                             incoming.observed_at)
        return merged, "corroborated"
    if relation == "contradicts_stronger":
        return FactVersion(incoming.entity_id, incoming.relation, incoming.value,
                           incoming.confidence, incoming.source_ids, incoming.observed_at), "supersede"
    return existing, "retain_existing"
