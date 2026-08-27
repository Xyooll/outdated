"""Failure analysis and bounded repair orchestration for self-building software."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

from .build_memory import BuildMemory, BuildMemoryRecord
from .self_build_agent import BuildRequest, AgentBuildResult, SelfBuildAgent


@dataclass(frozen=True)
class FailureAnalysis:
    reason: str
    category: str
    suggested_repairs: tuple[str, ...]


def analyze_failure(reason: str) -> FailureAnalysis:
    text = (reason or "unknown failure").lower()
    if "syntax" in text or "parse" in text:
        category = "syntax"
        repairs = ("fix syntax or indentation", "reduce generated code to a minimal valid implementation")
    elif "test" in text or "assert" in text or "import" in text:
        category = "test"
        repairs = ("fix the failing behavior", "align generated tests with the staged module API")
    elif "permission" in text or "authority" in text:
        category = "authorization"
        repairs = ("do not bypass the promotion gate",)
    else:
        category = "unknown"
        repairs = ("inspect the failure and produce the smallest targeted repair",)
    return FailureAnalysis(reason, category, repairs)


class RepairLoop:
    """Run bounded build attempts while feeding failure context back to the generator."""

    def __init__(self, agent: SelfBuildAgent, memory: BuildMemory | None = None,
                 max_repairs: int = 3,
                 repair: Callable[[BuildRequest, str, FailureAnalysis, tuple[str, ...]], Any] | None = None):
        if max_repairs < 0:
            raise ValueError("max_repairs must be >= 0")
        self.agent = agent
        self.memory = memory or BuildMemory()
        self.max_repairs = max_repairs
        self.repair = repair

    def run(self, request: BuildRequest, *, promote: bool = False,
            autonomy_level: int = 0) -> AgentBuildResult:
        original_generate = self.agent.generate
        feedback = ""
        final: AgentBuildResult | None = None

        for attempt in range(self.max_repairs + 1):
            if attempt:
                self.agent.generate = self._repair_generator(original_generate, feedback)
            final = self.agent.build(request, promote=promote, autonomy_level=autonomy_level)
            result = final.build
            analysis = analyze_failure(result.reason) if not (result.syntax_ok and result.tests_ok) else None
            self.memory.record(BuildMemoryRecord(
                name=request.name, goal=request.goal, iteration=attempt + 1,
                syntax_ok=result.syntax_ok, tests_ok=result.tests_ok,
                reason=result.reason, repair=analysis.suggested_repairs[0] if analysis else "",
                resolved=bool(result.syntax_ok and result.tests_ok and attempt > 0),
            ))
            if result.syntax_ok and result.tests_ok:
                self.agent.generate = original_generate
                return final
            feedback = result.reason

        self.agent.generate = original_generate
        assert final is not None
        return final

    def _repair_generator(self, original: Any, previous_failure: str) -> Any:
        memory_repairs = tuple(self.memory.successful_repairs(previous_failure))
        analysis = analyze_failure(previous_failure)
        if self.repair is not None:
            return _RepairAdapter(self.repair, analysis, memory_repairs)
        return _FallbackRepairAdapter(original, analysis, memory_repairs)


class _RepairAdapter:
    def __init__(self, repair, analysis, memory_repairs):
        self.repair = repair
        self.analysis = analysis
        self.memory_repairs = memory_repairs

    def generate_bundle(self, request, feedback):
        return self.repair(request, feedback, self.analysis, self.memory_repairs)


class _FallbackRepairAdapter:
    """Preserves the original generator but gives it richer repair context."""
    def __init__(self, original, analysis, memory_repairs):
        self.original = original
        self.analysis = analysis
        self.memory_repairs = memory_repairs

    def generate_bundle(self, request, feedback):
        enriched = (
            f"Previous failure: {feedback}\n"
            f"Failure category: {self.analysis.category}\n"
            f"Suggested repairs: {'; '.join(self.analysis.suggested_repairs)}\n"
            f"Previously successful repairs: {'; '.join(self.memory_repairs) or 'none'}"
        )
        if hasattr(self.original, "generate_bundle"):
            return self.original.generate_bundle(request, enriched)
        return self.original(request, enriched)
