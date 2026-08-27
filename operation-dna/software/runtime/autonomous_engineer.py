"""Autonomous engineering orchestration over build, repair, and memory."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .ai_provider import AIProvider, RepairPlan
from .build_memory import BuildMemory
from .repair_loop import RepairLoop, analyze_failure
from .self_build_agent import AgentBuildResult, BuildRequest, SelfBuildAgent


@dataclass(frozen=True)
class EngineeringOutcome:
    result: AgentBuildResult
    repair_plans: tuple[RepairPlan, ...]
    attempts: int
    resolved: bool


class AutonomousEngineer:
    """Let the provider direct bounded build/repair iterations.

    The engineer can act autonomously up to validation, but cannot bypass
    the factory's promotion authority boundary.
    """

    def __init__(self, provider: AIProvider, agent: SelfBuildAgent,
                 memory: BuildMemory | None = None, max_repairs: int = 3):
        self.provider = provider
        self.agent = agent
        self.memory = memory or BuildMemory()
        self.max_repairs = max_repairs

    def build(self, request: BuildRequest, *, promote: bool = False,
              autonomy_level: int = 0) -> EngineeringOutcome:
        plans: list[RepairPlan] = []
        loop = RepairLoop(self.agent, self.memory, self.max_repairs,
                          repair=self._repair)
        result = loop.run(request, promote=promote, autonomy_level=autonomy_level)
        if not (result.build.syntax_ok and result.build.tests_ok):
            analysis = analyze_failure(result.build.reason)
            plans.append(self.provider.repair(
                self.provider.plan(request.goal), result.build.reason
            ))
        return EngineeringOutcome(
            result=result,
            repair_plans=tuple(plans),
            attempts=result.iteration,
            resolved=result.build.syntax_ok and result.build.tests_ok,
        )

    def _repair(self, request: BuildRequest, feedback: str, analysis: Any,
                memory_repairs: tuple[str, ...]):
        plan = self.provider.plan(request.goal)
        repair = self.provider.repair(plan, feedback)
        # The current provider contract returns a repair description rather
        # than source. Preserve compatibility with the existing agent by
        # enriching its generator context through a wrapper.
        original = self.agent.generate
        if hasattr(original, "generate_bundle"):
            return original.generate_bundle(
                request,
                f"{feedback}\nAI repair category: {repair.category}\n"
                f"Repair instructions: {'; '.join(repair.instructions)}\n"
                f"Memory repairs: {'; '.join(memory_repairs) or 'none'}",
            )
        return original(
            request,
            f"{feedback}\nAI repair category: {repair.category}\n"
            f"Repair instructions: {'; '.join(repair.instructions)}\n"
            f"Memory repairs: {'; '.join(memory_repairs) or 'none'}",
        )
