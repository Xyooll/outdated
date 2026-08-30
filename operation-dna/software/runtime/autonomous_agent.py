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
    CONTINUE_INPUTS = {"continue", "contnue", "keep going", "proceed", "go on", "do it", "build it", "fix it", "handle this"}

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
        """Start an objective or resume the current objective when context makes that clear."""
        incoming = {"role": "user", "content": text}
        normalized = " ".join(text.lower().split())
        resume_existing = bool(self.objective and self.objective.status in {"active", "waiting_human"}) and (
            normalized in self.CONTINUE_INPUTS or self.objective.status == "waiting_human"
        )
        if resume_existing:
            self.objective.context["last_human_response"] = text
            self.objective.context["input_type"] = "human_response_to_handoff" if self.objective.status == "waiting_human" else "objective_continuation"
            self.objective.status = "active"
            self.objective.turns += 1
            text_for_agent = (
                f"EXISTING OBJECTIVE: {self.objective.text}\n"
                f"CURRENT OBJECTIVE STATE: {self.objective.context}\n"
                f"HUMAN INPUT: {text}\n"
                "Continue the existing objective from its current state. Do not restart discovery. "
                "Inspect prior observations and unresolved work, then select the next useful means."
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
        else:
            self.objective.status = "active"
        return action

    def reset(self) -> None:
        self.history.clear()
        self.objective = None
