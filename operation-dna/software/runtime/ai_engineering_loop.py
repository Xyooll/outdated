"""Provider-driven engineering loop.

This is the bridge between the AI reasoning interface and the self-build
system. It lets the future LLM decide what to build and how to repair it,
while validation and promotion remain controlled by the existing runtime.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .ai_provider import AIProvider, EngineeringPlan, RepairPlan
from .self_build_agent import BuildRequest, AgentBuildResult
from .self_build_pipeline import SelfBuildPipeline


@dataclass(frozen=True)
class EngineeringRun:
    goal: str
    plan: EngineeringPlan
    build: AgentBuildResult
    repairs: tuple[RepairPlan, ...] = ()


class AIEngineeringLoop:
    """Turn an AI provider's plan into a validated self-build operation."""

    def __init__(self, provider: AIProvider, pipeline: SelfBuildPipeline):
        self.provider = provider
        self.pipeline = pipeline

    def plan(self, goal: str) -> EngineeringPlan:
        return self.provider.plan(goal)

    def run(self, goal: str, *, promote: bool = False, autonomy_level: int = 0) -> EngineeringRun:
        plan = self.provider.plan(goal)
        result = self.pipeline.run(goal, promote=promote, autonomy_level=autonomy_level)
        repairs: list[RepairPlan] = []
        if not result.build.build.tests_ok or not result.build.build.syntax_ok:
            repairs.append(self.provider.repair(plan, result.build.build.reason))
        return EngineeringRun(goal, plan, result.build, tuple(repairs))

    def repair_strategy(self, goal: str, failure: str) -> RepairPlan:
        return self.provider.repair(self.provider.plan(goal), failure)
