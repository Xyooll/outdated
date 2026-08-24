"""Deterministic simulation harness for closed-loop testing."""
from dataclasses import dataclass
from .controller import MasterController
from software.economics.learning import Forecast, Outcome

@dataclass(frozen=True)
class SimulationResult:
    cycles: int
    forecasts: int
    evaluated: int
    accuracy: float


def run(db_path: str = ":memory:") -> SimulationResult:
    controller = MasterController(db_path)
    outcomes = [(0.20, 0.10), (0.15, 0.10), (-0.05, 0.10), (0.30, 0.10)]
    for index, (actual, predicted) in enumerate(outcomes):
        fid = f"sim-{index}"
        controller.record_forecast(Forecast(fid, f"sim-{index}", .7, predicted, .2, f"cycle-{index}"))
        controller.observe(Outcome(fid, actual, 0.0, f"cycle-{index}-outcome"))
    accuracy = sum(r["direction_correct"] for r in controller.results) / len(controller.results)
    return SimulationResult(4, len(controller.forecasts), len(controller.results), accuracy)
