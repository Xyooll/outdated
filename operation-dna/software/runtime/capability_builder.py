"""Safe AI-to-software candidate builder. Production promotion is never implicit."""
from dataclasses import dataclass
from typing import Callable, Any
from .hypothesis import CandidateSpec

@dataclass(frozen=True)
class BuildResult:
    name: str
    tests_passed: bool
    sandbox_passed: bool
    eligible_for_promotion: bool
    reason: str
    artifact: Any = None

class CapabilityBuilder:
    def __init__(self, test_runner: Callable[[Any], bool], sandbox_runner: Callable[[Any], bool]):
        self.test_runner = test_runner
        self.sandbox_runner = sandbox_runner

    def build(self, spec: CandidateSpec) -> BuildResult:
        """Validate an AI-generated candidate without deploying or changing production."""
        artifact = spec.candidate
        try:
            tests = bool(self.test_runner(artifact))
        except Exception as exc:
            return BuildResult(spec.hypothesis.statement, False, False, False, f"test failure: {exc}")
        if not tests:
            return BuildResult(spec.hypothesis.statement, False, False, False, "candidate tests failed")
        try:
            sandbox = bool(self.sandbox_runner(artifact))
        except Exception as exc:
            return BuildResult(spec.hypothesis.statement, True, False, False, f"sandbox failure: {exc}")
        if not sandbox:
            return BuildResult(spec.hypothesis.statement, True, False, False, "candidate failed sandbox gate")
        return BuildResult(spec.hypothesis.statement, True, True, True, "candidate passed build and sandbox gates", artifact)

    def promote(self, result: BuildResult, authorize: Callable[[Any], bool]) -> bool:
        """Promotion requires an explicit external authorization decision."""
        if not result.eligible_for_promotion:
            return False
        return bool(authorize(result.artifact))
