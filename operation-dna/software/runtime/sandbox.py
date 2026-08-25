"""Deterministic, side-effect-free sandbox for high-volume Xyool simulation cycles."""
from dataclasses import dataclass, field
from typing import Any, Callable
import random

@dataclass
class SandboxState:
    tick: int = 0
    cash: float = 100.0
    score: float = 0.0
    variables: dict[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class SimulationEvent:
    tick: int
    source: str
    event_type: str
    data: dict[str, Any]

@dataclass(frozen=True)
class SimulationResult:
    ticks: int
    initial_cash: float
    final_cash: float
    score: float
    events: int
    errors: int

class Sandbox:
    """No network, filesystem, brokerage, or external side effects."""
    def __init__(self, seed: int = 42, initial_cash: float = 100.0):
        self.rng = random.Random(seed)
        self.state = SandboxState(cash=initial_cash)
        self._sources: list[Callable[[SandboxState, random.Random], SimulationEvent | None]] = []
        self._handlers: dict[str, Callable[[SandboxState, SimulationEvent], float]] = {}

    def add_source(self, source: Callable[[SandboxState, random.Random], SimulationEvent | None]) -> None:
        self._sources.append(source)

    def register_handler(self, event_type: str, handler: Callable[[SandboxState, SimulationEvent], float]) -> None:
        self._handlers[event_type] = handler

    def step(self) -> list[SimulationEvent]:
        self.state.tick += 1
        events: list[SimulationEvent] = []
        for source in self._sources:
            event = source(self.state, self.rng)
            if event is None:
                continue
            events.append(event)
            handler = self._handlers.get(event.event_type)
            if handler:
                try:
                    self.state.score += float(handler(self.state, event))
                except Exception:
                    self.state.variables["errors"] = self.state.variables.get("errors", 0) + 1
        return events

    def run(self, ticks: int = 1000) -> SimulationResult:
        if ticks < 1:
            raise ValueError("ticks must be >= 1")
        initial = self.state.cash
        count = 0
        for _ in range(ticks):
            count += len(self.step())
        return SimulationResult(self.state.tick, initial, self.state.cash, self.state.score, count, self.state.variables.get("errors", 0))
