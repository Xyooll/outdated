"""Persistent objectives and constraints for the active AI layer."""
from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class Objective:
    name: str
    description: str
    priority: float = 1.0
    success_metric: str = ""
    constraints: tuple[str, ...] = ()
    resources: dict[str, Any] = field(default_factory=dict)

class ObjectiveRegistry:
    def __init__(self):
        self._objectives: dict[str, Objective] = {}

    def set(self, objective: Objective) -> None:
        if not objective.name.strip():
            raise ValueError("objective name is required")
        self._objectives[objective.name] = objective

    def active(self) -> list[Objective]:
        return sorted(self._objectives.values(), key=lambda x: x.priority, reverse=True)

    def get(self, name: str) -> Objective:
        return self._objectives[name]
