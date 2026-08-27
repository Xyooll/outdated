"""Self-building agent loop for Operation DNA.

The agent can propose and validate software candidates, but promotion remains
behind the existing HumanAuthority boundary. The code-generation layer is
injected so this module works with any LLM/provider without coupling the
runtime to a specific vendor.
"""
from __future__ import annotations

from dataclasses import dataclass, field
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

    `generate` receives a BuildRequest and returns complete Python source.
    The agent may iterate on failed candidates, but it cannot bypass the
    SoftwareFactory validation or HumanAuthority promotion gate.
    """

    def __init__(
        self,
        factory: SoftwareFactory,
        generate: Callable[[BuildRequest, str], str],
        test_file_for: Callable[[BuildRequest], str] | None = None,
        max_iterations: int = 3,
    ):
        if max_iterations < 1:
            raise ValueError("max_iterations must be >= 1")
        self.factory = factory
        self.generate = generate
        self.test_file_for = test_file_for or (lambda request: request.test_file)
        self.max_iterations = max_iterations

    def build(self, request: BuildRequest, *, promote: bool = False,
              autonomy_level: int = 0) -> AgentBuildResult:
        feedback = ""
        last: BuildResult | None = None
        notes: list[str] = []

        for iteration in range(1, self.max_iterations + 1):
            source = self.generate(request, feedback)
            path = self.factory.stage(request.name, source)
            test_file = self.test_file_for(request)
            if not test_file:
                last = self.factory.validate(path)
            else:
                last = self.factory.run_tests(path, test_file)

            if last.syntax_ok and last.tests_ok:
                notes.append("candidate passed syntax and tests")
                promoted = False
                if promote:
                    destination = self.factory.promote(
                        last, request.destination, autonomy_level=autonomy_level
                    )
                    promoted = True
                    notes.append(f"promoted to {destination}")
                return AgentBuildResult(request, last, iteration, promoted, tuple(notes))

            feedback = last.reason
            notes.append(f"iteration {iteration} rejected: {last.reason}")

        assert last is not None
        return AgentBuildResult(request, last, self.max_iterations, False, tuple(notes))


def write_build_record(result: AgentBuildResult, path: str = "data/self_build_history.jsonl") -> None:
    """Append an audit record; never stores generated secrets."""
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
