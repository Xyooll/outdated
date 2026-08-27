"""Self-building agent loop for Operation DNA."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Any
import json

from .software_factory import SoftwareFactory, BuildResult


@dataclass(frozen=True)
class BuildRequest:
    name: str
    goal: str
    requirements: tuple[str, ...] = ()
    test_file: str = ""
    destination: str = "operation-dna/software/generated"


@dataclass(frozen=True)
class AgentBuildResult:
    request: BuildRequest
    build: BuildResult
    iteration: int
    promoted: bool = False
    notes: tuple[str, ...] = ()


class SelfBuildAgent:
    """Closed-loop software builder with explicit promotion control.

    Generators may either be legacy callables returning source text or bundle
    providers exposing ``generate_bundle(request, feedback)`` and returning an
    object with ``source`` and ``tests`` attributes.
    """

    def __init__(self, factory: SoftwareFactory, generate: Any,
                 test_file_for: Callable[[BuildRequest], str] | None = None,
                 max_iterations: int = 3):
        if max_iterations < 1:
            raise ValueError("max_iterations must be >= 1")
        self.factory = factory
        self.generate = generate
        self.test_file_for = test_file_for or (lambda request: request.test_file)
        self.max_iterations = max_iterations

    def _generate(self, request: BuildRequest, feedback: str) -> tuple[str, str | None]:
        if hasattr(self.generate, "generate_bundle"):
            bundle = self.generate.generate_bundle(request, feedback)
            return str(bundle.source), str(bundle.tests)
        if callable(self.generate):
            return str(self.generate(request, feedback)), None
        raise TypeError("generator must be callable or expose generate_bundle(request, feedback)")

    def build(self, request: BuildRequest, *, promote: bool = False,
              autonomy_level: int = 0) -> AgentBuildResult:
        feedback = ""
        last: BuildResult | None = None
        notes: list[str] = []
        generated_test_path: Path | None = None

        for iteration in range(1, self.max_iterations + 1):
            source, generated_tests = self._generate(request, feedback)
            path = self.factory.stage(request.name, source)

            test_file = self.test_file_for(request)
            if generated_tests is not None and not test_file:
                generated_test_path = Path(self.factory.root) / f"{request.name}_generated_tests.py"
                generated_test_path.write_text(generated_tests, encoding="utf-8")
                test_file = str(generated_test_path)

            last = self.factory.run_tests(path, test_file) if test_file else self.factory.validate(path)
            if last.syntax_ok and last.tests_ok:
                notes.append("candidate passed syntax and tests")
                promoted = False
                if promote:
                    try:
                        destination = self.factory.promote(last, request.destination, autonomy_level=autonomy_level)
                        promoted = True
                        notes.append(f"promoted to {destination}")
                    except PermissionError as exc:
                        notes.append(f"promotion blocked: {exc}")
                return AgentBuildResult(request, last, iteration, promoted, tuple(notes))

            feedback = last.reason
            notes.append(f"iteration {iteration} rejected: {last.reason}")

        assert last is not None
        return AgentBuildResult(request, last, self.max_iterations, False, tuple(notes))


class AutonomousSelfBuildAgent(SelfBuildAgent):
    """Autonomous interface; promotion remains behind explicit authority."""
    pass


def write_build_record(result: AgentBuildResult, path: str = "data/self_build_history.jsonl") -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "name": result.request.name,
        "goal": result.request.goal,
        "iteration": result.iteration,
        "syntax_ok": result.build.syntax_ok,
        "tests_ok": result.build.tests_ok,
        "promoted": result.promoted,
        "reason": result.build.reason,
        "notes": result.notes,
    }
    with target.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, default=str) + "\n")
