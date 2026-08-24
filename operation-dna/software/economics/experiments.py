"""Smallest-viable-experiment planning and outcome accounting."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Experiment:
    opportunity: str
    budget: float
    duration_days: int
    success_metric: str
    stop_loss: float


@dataclass(frozen=True)
class Outcome:
    experiment: str
    spent: float
    value_created: float
    success: bool
    notes: str = ""

    @property
    def net_value(self) -> float:
        return self.value_created - self.spent


def plan(name: str, budget: float, duration_days: int, success_metric: str,
         stop_loss: float) -> Experiment:
    if budget <= 0 or duration_days <= 0:
        raise ValueError("budget and duration must be positive")
    if stop_loss < 0:
        raise ValueError("stop_loss cannot be negative")
    return Experiment(name, budget, duration_days, success_metric, stop_loss)


def evaluate(outcome: Outcome) -> str:
    if outcome.success and outcome.net_value > 0:
        return "scale_candidate"
    if outcome.net_value >= 0:
        return "iterate"
    return "reject_or_redesign"
