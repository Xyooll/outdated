"""Generate bounded candidate strategies and compare them in safe synthetic worlds."""
from dataclasses import dataclass
from typing import Callable
from .evaluation import EvaluationMetrics
from ..simulations.trading_market import run_strategy, momentum_baseline
from ..simulations.business_market import run_business_strategy, fit_baseline

@dataclass(frozen=True)
class Candidate:
    name: str
    strategy: Callable
    description: str

@dataclass(frozen=True)
class SearchResult:
    domain: str
    baseline: EvaluationMetrics
    candidates: list[tuple[str, EvaluationMetrics]]
    winner: str | None

class StrategySearch:
    def _measure(self, factory, runs: int, domain: str) -> EvaluationMetrics:
        results = [factory(seed) for seed in range(runs)]
        if domain == "trading":
            scores = [r.return_pct for r in results]
            errors = [r.max_drawdown_pct / 100.0 for r in results]
        else:
            scores = [r.profit for r in results]
            errors = [0.0 for _ in results]
        return EvaluationMetrics(sum(scores)/len(scores), min(scores), max(scores), sum(errors)/len(errors), len(scores))

    def search_trading(self, candidates: list[Candidate], runs: int = 50, ticks: int = 1000) -> SearchResult:
        baseline = self._measure(lambda seed: run_strategy(momentum_baseline, seed, ticks), runs, "trading")
        measured = [(c.name, self._measure(lambda seed, c=c: run_strategy(c.strategy, seed, ticks), runs, "trading")) for c in candidates]
        eligible = [(n, m) for n, m in measured if m.mean_score > baseline.mean_score and m.mean_error_rate <= baseline.mean_error_rate]
        winner = max(eligible, key=lambda x: x[1].mean_score)[0] if eligible else None
        return SearchResult("trading", baseline, measured, winner)

    def search_business(self, candidates: list[Candidate], runs: int = 50, opportunities: int = 1000) -> SearchResult:
        baseline = self._measure(lambda seed: run_business_strategy(fit_baseline, seed, opportunities), runs, "business")
        measured = [(c.name, self._measure(lambda seed, c=c: run_business_strategy(c.strategy, seed, opportunities), runs, "business")) for c in candidates]
        eligible = [(n, m) for n, m in measured if m.mean_score > baseline.mean_score]
        winner = max(eligible, key=lambda x: x[1].mean_score)[0] if eligible else None
        return SearchResult("business", baseline, measured, winner)


def create_trading_candidates() -> list[Candidate]:
    def short_momentum(history):
        return 1 if len(history) >= 10 and history[-1].price > history[-10].price else 0
    def fast_momentum(history):
        return 1 if len(history) >= 3 and history[-1].price > history[-3].price else 0
    return [Candidate("fast_momentum", fast_momentum, "3-tick momentum"), Candidate("short_momentum", short_momentum, "10-tick momentum")]


def create_business_candidates() -> list[Candidate]:
    def high_fit(o):
        return o.fit >= 0.75 and o.competition <= 0.65
    def value_fit(o):
        return o.fit >= 0.60 and o.value >= 250 and o.competition <= 0.70
    return [Candidate("high_fit", high_fit, "higher fit threshold"), Candidate("value_fit", value_fit, "value plus fit")]
