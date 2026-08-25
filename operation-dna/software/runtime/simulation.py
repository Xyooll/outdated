"""Deterministic simulation environment for safe learning before real execution."""
from dataclasses import dataclass
from typing import Callable, Any

@dataclass(frozen=True)
class SimulationRun:
    name: str
    steps: int
    outputs: tuple[Any, ...]

class Simulator:
    def __init__(self): self.history: list[SimulationRun] = []
    def run(self, name: str, actions: list[Callable[[], Any]]) -> SimulationRun:
        outputs = tuple(action() for action in actions)
        result = SimulationRun(name, len(actions), outputs)
        self.history.append(result)
        return result
