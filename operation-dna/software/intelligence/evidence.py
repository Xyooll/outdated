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
    """Combine independent evidence conservatively; empty evidence means zero confidence."""
    if not evidence:
        return 0.0
    # Independent corroboration increases confidence without allowing one source to dominate.
    product = 1.0
    for item in evidence:
        product *= 1.0 - item.score
    return max(0.0, min(1.0, 1.0 - product))
