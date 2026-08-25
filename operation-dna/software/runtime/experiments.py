"""Hypothesis -> prediction -> observation -> evaluation loop."""
from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class Experiment:
    id: str
    hypothesis: str
    prediction: float
    threshold: float = 0.0

@dataclass(frozen=True)
class ExperimentResult:
    experiment_id: str
    actual: float
    error: float
    passed: bool

def evaluate(experiment: Experiment, actual: float) -> ExperimentResult:
    error = actual - experiment.prediction
    return ExperimentResult(experiment.id, actual, error, abs(error) <= experiment.threshold)
