"""Evidence scoring and provenance primitives."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Evidence:
    source_id: str
    event_id: str
    source_tier: float
    corroboration: float
    recency: float
    specificity: float

    @property
    def score(self) -> float:
        values = [self.source_tier, self.corroboration, self.recency, self.specificity]
        return max(0.0, min(1.0, sum(values) / len(values)))


def confidence(evidence: list[Evidence]) -> float:
    """Combine evidence conservatively while avoiding double-counting one source."""
    if not evidence:
        return 0.0

    # Multiple articles/events from the same source are not independent evidence.
    best_by_source: dict[str, float] = {}
    for item in evidence:
        best_by_source[item.source_id] = max(best_by_source.get(item.source_id, 0.0), item.score)

    product = 1.0
    for score in best_by_source.values():
        product *= 1.0 - score
    return max(0.0, min(1.0, 1.0 - product))
