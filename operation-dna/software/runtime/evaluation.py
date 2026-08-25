"""Baseline-vs-candidate evaluation for safe learning and evolution."""
from dataclasses import dataclass
from statistics import mean
from typing import Callable, Any

@dataclass(frozen=True)
class EvaluationMetrics:
    mean_score: float
    min_score: float
    max_score: float
    mean_error_rate: float
    samples: int

@dataclass(frozen=True)
class EvaluationResult:
    baseline: EvaluationMetrics
    candidate: EvaluationMetrics
    improvement: float
    candidate_better: bool
    reason: str

class Evaluator:
    def measure(self, runner: Callable[[int], Any], runs: int = 10) -> EvaluationMetrics:
        if runs < 1:
            raise ValueError("runs must be >= 1")
        results = [runner(i) for i in range(runs)]
        scores = [float(r.score) for r in results]
        errors = [float(r.errors) / max(1, int(r.ticks)) for r in results]
        return EvaluationMetrics(mean(scores), min(scores), max(scores), mean(errors), len(scores))

    def compare(self, baseline: EvaluationMetrics, candidate: EvaluationMetrics, min_improvement: float = 0.0) -> EvaluationResult:
        improvement = candidate.mean_score - baseline.mean_score
        better = improvement > min_improvement and candidate.mean_error_rate <= baseline.mean_error_rate
        reason = "candidate improves score without increasing error rate" if better else "candidate did not meet promotion criteria"
        return EvaluationResult(baseline, candidate, improvement, better, reason)
