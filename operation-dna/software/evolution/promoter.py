"""Safe promotion gate for new strategies/rules."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Evaluation:
    candidate_version: str
    baseline_score: float
    candidate_score: float
    regression_count: int
    samples: int


def eligible(evaluation: Evaluation, min_samples: int = 30) -> bool:
    return (
        evaluation.samples >= min_samples
        and evaluation.regression_count == 0
        and evaluation.candidate_score > evaluation.baseline_score
    )
