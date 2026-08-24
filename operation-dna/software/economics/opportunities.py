"""Opportunity discovery and experiment planning primitives."""
from dataclasses import dataclass
from enum import Enum


class Decision(str, Enum):
    EXPERIMENT = "experiment"
    WATCH = "watch"
    REJECT = "reject"


@dataclass(frozen=True)
class OpportunitySignal:
    name: str
    category: str
    evidence_score: float
    expected_upside: float
    capital_required: float
    downside: float
    reversible: bool
    time_to_test_days: int

    @property
    def efficiency(self) -> float:
        return self.expected_upside / self.capital_required if self.capital_required > 0 else 0.0

    @property
    def score(self) -> float:
        risk = max(0.0, 1.0 - min(1.0, self.downside))
        speed = 1.0 / max(1, self.time_to_test_days)
        return self.efficiency * self.evidence_score * risk * (1.0 if self.reversible else 0.5) * speed


def decide(signal: OpportunitySignal, experiment_budget: float) -> Decision:
    if signal.capital_required > experiment_budget:
        return Decision.WATCH
    if signal.evidence_score < 0.6 or signal.downside > 0.5:
        return Decision.WATCH
    if signal.score <= 0:
        return Decision.REJECT
    return Decision.EXPERIMENT


def rank(signals: list[OpportunitySignal]) -> list[OpportunitySignal]:
    return sorted(signals, key=lambda s: s.score, reverse=True)
