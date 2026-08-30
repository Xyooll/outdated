"""Persistent objective-aware autonomous agent loop."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Callable
from .agent_orchestrator import AgentOrchestrator, SkillRegistry, AgentAction

@dataclass
class ObjectiveState:
    text: str
    status: str = "active"
    handoff: str = ""
    context: dict[str, Any] = field(default_factory=dict)
    turns: int = 0

class AutonomousAgent:
    """Keep one objective alive across turns; human replies resume the same objective."""
    def __init__(self, provider: Any, capabilities: SkillRegistry, behavior: str = "", max_steps: int = 12,
                 progress: Callable[[str], None] | None = None):
        self.provider = provider
        self.capabilities = capabilities
        self.behavior = behavior
        self.max_steps = max_steps
        self.progress = progress
        self.orchestrator = AgentOrchestrator(provider, capabilities, max_steps=max_steps,
                                               behavior=behavior, progress=progress)
        self.history: list[dict[str, str]] = []
        self.objective: ObjectiveState | None = None

    def send(self, text: str) -> AgentAction:
        """Start an objective or resume it after a handoff; do not restart unnecessarily."""
        if self.objective and self.objective.status == "waiting_human":
            text_for_agent = (
                "RESUME EXISTING OBJECTIVE.\n"
                f"OBJECTIVE: {self.objective.text}\n"
                f"PREVIOUS HANDOFF: {self.objective.handoff}\n"
                f"HUMAN RESPONSE: {text}\n"
                "Verify the response, update objective state, and continue autonomously. "
                "Do not treat this as a new unrelated objective."
            )
            self.objective.status = "active"
            self.objective.turns += 1
        else:
            self.objective = ObjectiveState(text=text)
            text_for_agent = text

        action = self.orchestrator.run(text_for_agent, self.history)
        self.history.extend([{"role": "user", "content": text},
                             {"role": "assistant", "content": action.content}])

        lower = action.content.lower()
        handoff_markers = (
            "human action is required", "human involvement is required", "please provide",
            "please authorize", "you need to", "you must provide", "requires your approval",
        )
        if action.kind == "ask" or any(marker in lower for marker in handoff_markers):
            self.objective.status = "waiting_human"
            self.objective.handoff = action.content
        elif action.kind == "done":
            self.objective.status = "complete"
        return action

    def reset(self) -> None:
        self.history.clear()
        self.objective = None
