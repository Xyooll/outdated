"""Explicit persistent objective state for multi-turn autonomous work."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

ACTIVE = "active"
WAITING_HUMAN = "waiting_human"
COMPLETE = "complete"
BLOCKED = "blocked"

@dataclass
class ObjectiveState:
    text: str
    status: str = ACTIVE
    handoff: str = ""
    context: dict[str, Any] = field(default_factory=dict)
    turns: int = 0

    def resume(self, human_response: str) -> str:
        self.context["last_human_response"] = human_response
        self.status = ACTIVE
        self.handoff = ""
        self.turns += 1
        return (
            "RESUME EXISTING OBJECTIVE\n"
            f"OBJECTIVE: {self.text}\n"
            f"HUMAN RESPONSE: {human_response}\n"
            "Treat this response as input to the existing objective. Verify it, update the objective state, and continue autonomously."
        )
