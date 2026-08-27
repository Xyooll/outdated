"""End-to-end self-build pipeline.

The pipeline separates planning, generation, validation, repair, and
promotion so an LLM can eventually own the engineering loop while every
high-impact boundary remains explicit.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any
from .self_build_planner import SelfBuildPlanner, BuildPlan
from .self_build_agent import AgentBuildResult
from .software_factory import SoftwareFactory

@dataclass(frozen=True)
class PipelineResult:
    plan: BuildPlan
    build: AgentBuildResult

class SelfBuildPipeline:
    def __init__(self, factory: SoftwareFactory, planner: SelfBuildPlanner, builder: Any):
        self.factory = factory
        self.planner = planner
        self.builder = builder

    def run(self, goal: str, *, promote: bool = False, autonomy_level: int = 0) -> PipelineResult:
        plan = self.planner.plan(goal)
        request = self.planner.request(plan)
        result = self.builder.build(request, promote=promote, autonomy_level=autonomy_level)
        return PipelineResult(plan, result)
