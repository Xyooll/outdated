"""Evidence-aware claim ranking."""
from dataclasses import dataclass

@dataclass(frozen=True)
class ClaimAssessment:
    claim_key: str
    confidence: float
    supporting_events: list[str]
    conflicting_events: list[str]


def rank_claims(claims: list[tuple[str, str, float, str]]) -> list[ClaimAssessment]:
    groups = {}
    for key, value, score, event_id in claims:
        groups.setdefault((key, value), []).append((score, event_id))
    assessments = []
    for (key, value), rows in groups.items():
        confidence = 1.0
        for score, _ in rows:
            confidence *= (1.0 - max(0.0, min(1.0, score)))
        assessments.append(ClaimAssessment(key + "=" + value, 1-confidence,
                                            [e for _, e in rows], []))
    return sorted(assessments, key=lambda x: x.confidence, reverse=True)
