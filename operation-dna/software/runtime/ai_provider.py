"""Provider-neutral reasoning interface for AI-assisted software engineering."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol


class AIProvider(Protocol):
    def reason(self, prompt: str, context: list[dict[str, Any]]) -> dict[str, Any]: ...

    def plan(self, goal: str) -> "EngineeringPlan": ...

    def repair(self, plan: "EngineeringPlan", failure: str) -> "RepairPlan": ...


@dataclass(frozen=True)
class EngineeringPlan:
    name: str
    goal: str
    requirements: tuple[str, ...] = ()
    test_strategy: str = "deterministic regression tests"


@dataclass(frozen=True)
class RepairPlan:
    category: str
    rationale: str
    instructions: tuple[str, ...]


@dataclass
class LocalStubProvider:
    """Deterministic provider; performs no external calls."""
    def reason(self, prompt: str, context: list[dict[str, Any]]) -> dict[str, Any]:
        return {"status": "stub", "prompt": prompt, "context_items": len(context)}

    def plan(self, goal: str) -> EngineeringPlan:
        slug = "".join(c if c.isalnum() else "_" for c in goal.lower()).strip("_")
        return EngineeringPlan(
            "capability_" + (slug[:48] or "probe"), goal,
            ("deterministic", "testable", "side-effect free"),
        )

    def repair(self, plan: EngineeringPlan, failure: str) -> RepairPlan:
        text = failure.lower()
        if "syntax" in text:
            category = "syntax"
            instructions = ("correct syntax", "preserve the requested interface", "rerun tests")
        elif "import" in text:
            category = "dependency"
            instructions = ("repair imports", "use repository-compatible module paths", "rerun tests")
        else:
            category = "behavior"
            instructions = ("fix the smallest failing behavior", "preserve passing behavior", "rerun regression tests")
        return RepairPlan(category, f"repair selected from failure: {failure}", instructions)
