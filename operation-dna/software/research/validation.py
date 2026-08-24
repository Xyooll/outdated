"""Research validation gate between discovery and economic decisions."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Validation:
    evidence_score: float
    independent_sources: int
    primary_source: bool
    contradiction_count: int

    @property
    def score(self) -> float:
        source_bonus = min(0.3, self.independent_sources * 0.1)
        primary_bonus = 0.2 if self.primary_source else 0.0
        contradiction_penalty = min(0.4, self.contradiction_count * 0.1)
        return max(0.0, min(1.0, self.evidence_score + source_bonus + primary_bonus - contradiction_penalty))


def is_actionable(validation: Validation, threshold: float = 0.75) -> bool:
    return validation.score >= threshold and validation.contradiction_count == 0
