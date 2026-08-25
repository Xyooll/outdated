"""Multi-step plans produced by the active AI layer.

Unknown capabilities become build requests rather than hard failures.
"""
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

@dataclass(frozen=True)
class CapabilityRequest:
    name: str
    purpose: str
    arguments: dict[str, Any] = field(default_factory=dict)

class PlanValidationError(ValueError):
    pass

def validate_plan(plan: Plan) -> None:
    if not plan.goal.strip():
        raise PlanValidationError("plan goal cannot be empty")
    if not plan.steps:
        raise PlanValidationError("plan must contain at least one step")

def resolve_missing(plan: Plan, available: set[str]) -> list[CapabilityRequest]:
    """Return build requests for missing capabilities; existing capabilities are ignored."""
    requests: list[CapabilityRequest] = []
    seen: set[str] = set()
    for step in plan.steps:
        if step.capability not in available and step.capability not in seen:
            requests.append(CapabilityRequest(step.capability, step.purpose or f"Required by goal: {plan.goal}", dict(step.arguments)))
            seen.add(step.capability)
    return requests

def resolve_or_build(plan: Plan, available: set[str], builder) -> tuple[Plan, list[CapabilityRequest]]:
    """Ask the supplied software builder to create missing capabilities, then re-check the plan."""
    validate_plan(plan)
    requests = resolve_missing(plan, available)
    for request in requests:
        builder(request)
    return plan, requests
