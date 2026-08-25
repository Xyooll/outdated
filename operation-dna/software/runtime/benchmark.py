"""Large-scale reproducible sandbox benchmarking."""
from dataclasses import dataclass
from typing import Callable, Any
from .evaluation import Evaluator, EvaluationMetrics, EvaluationResult

@dataclass(frozen=True)
class BenchmarkResult:
    runs: int
    ticks_per_run: int
    baseline: EvaluationMetrics
    candidate: EvaluationMetrics
    comparison: EvaluationResult

class BenchmarkRunner:
    def __init__(self, evaluator: Evaluator | None = None):
        self.evaluator = evaluator or Evaluator()

    def run(self, baseline_factory: Callable[[int], Any], candidate_factory: Callable[[int], Any], runs: int = 100, ticks: int = 1000, min_improvement: float = 0.0) -> BenchmarkResult:
        if runs < 1 or ticks < 1:
            raise ValueError("runs and ticks must be >= 1")

        def execute(factory: Callable[[int], Any], seed: int):
            sandbox = factory(seed)
            return sandbox.run(ticks)

        baseline = self.evaluator.measure(lambda seed: execute(baseline_factory, seed), runs)
        candidate = self.evaluator.measure(lambda seed: execute(candidate_factory, seed), runs)
        comparison = self.evaluator.compare(baseline, candidate, min_improvement)
        return BenchmarkResult(runs, ticks, baseline, candidate, comparison)
