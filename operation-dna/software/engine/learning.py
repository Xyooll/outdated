"""Safe learning primitives. Candidate promotion remains an explicit gate."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Evaluation:
    baseline_score: float
    candidate_score: float
    risk_regression: bool
    robust: bool

    @property
    def improved(self) -> bool:
        return self.candidate_score > self.baseline_score and not self.risk_regression and self.robust


def eligible_for_promotion(evaluation: Evaluation, safety_passed: bool) -> bool:
    """Return True only when objective improvement and safety requirements pass."""
    return safety_passed and evaluation.improved


def promotion_result(evaluation: Evaluation, safety_passed: bool) -> str:
    return "promote" if eligible_for_promotion(evaluation, safety_passed) else "reject_or_continue_testing"
