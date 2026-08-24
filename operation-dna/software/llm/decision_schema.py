"""Structured AI proposal schema; proposals are not execution commands."""
from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class Proposal:
    objective: str
    hypothesis: str
    evidence_ids: list[str] = field(default_factory=list)
    confidence: float = 0.0
    requested_action: dict[str, Any] | None = None
    constraints: list[str] = field(default_factory=list)

    def validate(self) -> None:
        if not self.objective or not self.hypothesis:
            raise ValueError("objective and hypothesis are required")
        if not 0 <= self.confidence <= 1:
            raise ValueError("confidence must be between 0 and 1")
