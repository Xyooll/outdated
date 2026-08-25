"""AI hypothesis generation and safe candidate specification."""
from dataclasses import dataclass
from typing import Any, Callable

@dataclass(frozen=True)
class Hypothesis:
    statement: str
    target_metric: str
    expected_direction: str
    rationale: str
    parameters: dict[str, Any]

@dataclass(frozen=True)
class CandidateSpec:
    hypothesis: Hypothesis
    candidate: Callable
    description: str

class HypothesisEngine:
    """Turns observations into bounded, testable hypotheses. It does not promote code."""
    def generate(self, observations: list[dict[str, Any]], objective: str) -> list[Hypothesis]:
        if not observations:
            return []
        hypotheses = []
        for obs in observations[-10:]:
            metric = obs.get("metric")
            if metric and obs.get("signal") == "underperforming":
                hypotheses.append(Hypothesis(
                    statement=f"Adjust {metric} to improve {objective}",
                    target_metric=metric,
                    expected_direction="increase",
                    rationale=str(obs.get("reason", "recent underperformance")),
                    parameters=dict(obs.get("parameters", {})),
                ))
        return hypotheses

    def create_candidate(self, hypothesis: Hypothesis, factory: Callable[[Hypothesis], Callable]) -> CandidateSpec:
        strategy = factory(hypothesis)
        return CandidateSpec(hypothesis, strategy, f"Candidate generated from: {hypothesis.statement}")
