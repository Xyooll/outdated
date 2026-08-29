"""Small autonomous agent loop: model + custom behavior + skills."""
from __future__ import annotations
from typing import Any
from .agent_orchestrator import AgentOrchestrator, SkillRegistry, AgentAction

class AutonomousAgent:
    """Persistent conversational agent. The model decides when to use skills and when to stop."""
    def __init__(self, provider: Any, skills: SkillRegistry, behavior: str = "", max_steps: int = 12):
        self.provider = provider
        self.skills = skills
        self.behavior = behavior
        self.orchestrator = AgentOrchestrator(provider, skills, max_steps=max_steps)
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
