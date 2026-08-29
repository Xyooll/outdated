"""Agent-first orchestration: the model chooses skills; skills execute capabilities."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

SYSTEM = """You are the Xyool orchestrator. You are the agent, not a skill.
Reason about the user's objective and choose the next capability yourself.
Available skills are supplied by the runtime. Do not invent execution results.
Use INSPECT before building when project context is needed. Use BUILD for software work.
For ordinary conversation, use CONVERSE. After a skill returns, reason again until the
objective is complete or you need the user. Never bypass hard authorization boundaries.
Return exactly:
ACTION=<CONVERSE|INSPECT|BUILD|DONE|ASK> RESPONSE=<natural response>
"""

@dataclass(frozen=True)
class Decision:
    action: str
    response: str

class SkillRegistry:
    def __init__(self):
        self._skills: dict[str, Callable[..., Any]] = {}

    def register(self, name: str, skill: Callable[..., Any]) -> None:
        self._skills[name] = skill

    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._skills))

    def get(self, name: str) -> Callable[..., Any]:
        return self._skills[name]

class AgentOrchestrator:
    def __init__(self, provider: Any, skills: SkillRegistry, max_steps: int = 8):
        self.provider = provider
        self.skills = skills
        self.max_steps = max_steps

    def decide(self, objective: str, context: str, history: list[dict[str, str]]) -> Decision:
        skill_text = ", ".join(self.skills.names()) or "none"
        messages = [{"role": "system", "content": SYSTEM + f"\nSkills: {skill_text}"}]
        messages.extend(history)
        messages.append({"role": "user", "content": f"OBJECTIVE: {objective}\nCONTEXT:\n{context}"})
        raw = self.provider.complete(messages).strip()
        line = raw.splitlines()[0] if raw else "ACTION=ASK RESPONSE=I need more information."
        if "ACTION=" not in line or "RESPONSE=" not in line:
            return Decision("ASK", raw)
        action = line.split("ACTION=", 1)[1].split(None, 1)[0].strip()
        response = line.split("RESPONSE=", 1)[1].strip()
        if action not in {"CONVERSE", "INSPECT", "BUILD", "DONE", "ASK"}:
            action = "ASK"
        return Decision(action, response)

    def run(self, objective: str, context: str = "", history: list[dict[str, str]] | None = None) -> Decision:
        history = list(history or [])
        current_context = context
        for _ in range(self.max_steps):
            decision = self.decide(objective, current_context, history)
            if decision.action in {"CONVERSE", "DONE", "ASK"}:
                return decision
            skill_name = "inspect" if decision.action == "INSPECT" else "build"
            if skill_name not in self.skills.names():
                return Decision("ASK", f"Required skill unavailable: {skill_name}")
            result = self.skills.get(skill_name)(objective)
            current_context = str(result)
            history.extend([
                {"role": "assistant", "content": decision.response},
                {"role": "user", "content": f"SKILL_RESULT: {current_context}"},
            ])
        return Decision("ASK", "I reached the orchestration step limit before completing the objective.")
