"""Convert stored events into auditable intelligence candidates."""
from .extract import candidate_mentions
from .relationships import RelationshipCandidate, propose_relationship


def analyze_event(event: dict) -> dict:
    text = f"{event.get('title', '')} {event.get('summary', '')}"
    mentions = candidate_mentions(text)
    return {
        "event_id": event["id"],
        "mentions": [m.__dict__ for m in mentions],
        "relationship_candidates": [],
    }


def add_relationship_candidate(result: dict, from_mention: str, relation: str,
                                to_mention: str, confidence: float = 0.5) -> None:
    candidate = propose_relationship(
        from_mention, relation, to_mention, result["event_id"], confidence
    )
    result["relationship_candidates"].append(candidate.__dict__)
