"""Domain-neutral application protocol."""
from dataclasses import dataclass, field
from typing import Any, Protocol


@dataclass
class ApplicationContext:
    node_id: str
    version: str
    observations: list[dict[str, Any]] = field(default_factory=list)
    evidence: list[str] = field(default_factory=list)


@dataclass
class ApplicationResult:
    status: str
    observations: list[dict[str, Any]] = field(default_factory=list)
    hypotheses: list[dict[str, Any]] = field(default_factory=list)
    requested_action: dict[str, Any] | None = None
    gate_passed: bool = False
    outcome: dict[str, Any] = field(default_factory=dict)
    lessons: list[str] = field(default_factory=list)
    version: str = ""


class Application(Protocol):
    """All application organs implement the same lifecycle contract."""

    def perceive(self, context: ApplicationContext) -> list[dict[str, Any]]: ...
    def understand(self, context: ApplicationContext) -> list[dict[str, Any]]: ...
    def hypothesize(self, context: ApplicationContext) -> list[dict[str, Any]]: ...
    def test(self, context: ApplicationContext) -> dict[str, Any]: ...
    def act(self, context: ApplicationContext, proposal: dict[str, Any]) -> ApplicationResult: ...
    def observe(self, context: ApplicationContext) -> dict[str, Any]: ...
    def learn(self, context: ApplicationContext, outcome: dict[str, Any]) -> list[str]: ...
    def evolve(self, context: ApplicationContext, lessons: list[str]) -> dict[str, Any]: ...
