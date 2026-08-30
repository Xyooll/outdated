"""Small autonomous agent loop: model + custom behavior + means."""
from __future__ import annotations
from typing import Any, Callable
from .agent_orchestrator import AgentOrchestrator, SkillRegistry, AgentAction

class AutonomousAgent:
    """Persistent conversational agent whose model controls means, iteration, and completion."""
    def __init__(self, provider: Any, capabilities: SkillRegistry, behavior: str = "", max_steps: int = 12,
                 progress: Callable[[str], None] | None = None):
        self.provider = provider
        self.capabilities = capabilities
        self.behavior = behavior
        self.orchestrator = AgentOrchestrator(
            provider, capabilities, max_steps=max_steps, behavior=behavior, progress=progress
        )
        self.history: list[dict[str, str]] = []

    def send(self, text: str) -> AgentAction:
        action = self.orchestrator.run(text, self.history)
        self.history.extend([
            {"role": "user", "content": text},
            {"role": "assistant", "content": action.content},
        ])
        return action

    def reset(self) -> None:
        self.history.clear()
