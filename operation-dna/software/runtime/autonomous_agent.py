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
    """Keep one objective alive across turns; every human-originated message remains role=user."""
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
        """Start or resume an objective. Semantic context is tracked separately from message role."""
        incoming = {"role": "user", "content": text}
        if self.objective and self.objective.status == "waiting_human":
            self.objective.context["last_human_response"] = text
            self.objective.context["input_type"] = "human_response_to_handoff"
            self.objective.status = "active"
            self.objective.turns += 1
            text_for_agent = (
                f"EXISTING OBJECTIVE: {self.objective.text}\n"
                f"HUMAN INPUT: {text}\n"
                "This is a user response to a pending dependency in the existing objective. "
                "Verify it, update state, and continue the same objective autonomously. Do not create a new objective."
            )
        else:
            self.objective = ObjectiveState(text=text)
            self.objective.context["input_type"] = "new_objective"
            text_for_agent = text

        action = self.orchestrator.run(text_for_agent, self.history)
        self.history.extend([incoming, {"role": "assistant", "content": action.content}])

        if action.kind == "ask":
            self.objective.status = "waiting_human"
            self.objective.handoff = action.content
        elif action.kind == "done":
            self.objective.status = "complete"
        return action

    def reset(self) -> None:
        self.history.clear()
        self.objective = None
