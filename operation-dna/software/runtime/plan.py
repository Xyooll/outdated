"""Multi-step plans produced by the active AI layer."""
from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class PlanStep:
    capability: str
    arguments: dict[str, Any] = field(default_factory=dict)
    purpose: str = ""

@dataclass(frozen=True)
class Plan:
    goal: str
    steps: tuple[PlanStep, ...]

class PlanValidationError(ValueError):
    pass

def validate_plan(plan: Plan, available: set[str]) -> None:
    if not plan.goal.strip():
        raise PlanValidationError("plan goal cannot be empty")
    if not plan.steps:
        raise PlanValidationError("plan must contain at least one step")
    missing = [s.capability for s in plan.steps if s.capability not in available]
    if missing:
        raise PlanValidationError(f"unknown capabilities: {missing}")
