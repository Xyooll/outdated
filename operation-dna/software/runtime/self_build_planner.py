"""Goal-to-build planning for the autonomous software builder.

This layer decides WHAT capability should be built; the LLM builder decides
HOW to implement it. Planning is deterministic so it can run before an LLM
API is configured.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .self_build_agent import BuildRequest


@dataclass(frozen=True)
class Capability:
    name: str
    purpose: str
    requirements: tuple[str, ...] = ()
    destination: str = "operation-dna/software/generated"


@dataclass(frozen=True)
class BuildPlan:
    goal: str
    capability: Capability
    reason: str
    missing: bool = True


class SelfBuildPlanner:
    """Turn an engineering goal into a concrete capability build request."""

    def __init__(self, capabilities: Iterable[Capability] = ()):
        self.capabilities = tuple(capabilities)

    def plan(self, goal: str) -> BuildPlan:
        if not goal or not goal.strip():
            raise ValueError("goal is required")
        normalized = goal.strip().lower()
        for capability in self.capabilities:
            if capability.name.lower() in normalized:
                return BuildPlan(goal, capability, "known capability selected", missing=False)
        name = self._derive_name(goal)
        capability = Capability(
            name=name,
            purpose=goal.strip(),
            requirements=(
                "provide a small, deterministic Python API",
                "include unittest coverage for normal and edge cases",
                "avoid network calls and irreversible side effects",
            ),
        )
        return BuildPlan(goal, capability, "no matching capability; new capability required")

    def request(self, plan: BuildPlan) -> BuildRequest:
        return BuildRequest(
            name=plan.capability.name,
            goal=plan.capability.purpose,
            requirements=plan.capability.requirements,
            destination=plan.capability.destination,
        )

    @staticmethod
    def _derive_name(goal: str) -> str:
        words = [w for w in goal.lower().replace("-", " ").split() if w.isalnum()]
        stem = "_".join(words[:5]) or "generated_capability"
        if stem[0].isdigit():
            stem = "capability_" + stem
        return stem[:60]
