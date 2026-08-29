"""Model-directed agent orchestration. Conversation is intentionally open-ended."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable
import json

@dataclass(frozen=True)
class AgentAction:
    kind: str
    content: str = ""
    skill: str = ""
    arguments: dict[str, Any] | None = None

class SkillRegistry:
    def __init__(self) -> None:
        self._skills: dict[str, Callable[..., Any]] = {}
    def register(self, name: str, skill: Callable[..., Any]) -> None:
        self._skills[name] = skill
    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._skills))
    def execute(self, name: str, **arguments: Any) -> Any:
        if name not in self._skills:
            raise KeyError(f"skill not available: {name}")
        return self._skills[name](**arguments)

class AgentOrchestrator:
    """The model decides what to say and which registered skill to invoke."""
    def __init__(self, provider: Any, skills: SkillRegistry, max_steps: int = 12):
        self.provider, self.skills, self.max_steps = provider, skills, max_steps

    def _decide(self, messages: list[dict[str, str]]) -> AgentAction:
        system = (
            "You are Xyool, the agent and orchestrator. Conversation is open-ended; "
            "there are no scripted conversational rules. Reason about the user's objective, "
            "decide the next action, and use available skills when useful. "
            f"Available skills: {', '.join(self.skills.names()) or 'none'}. "
            "Return JSON only with keys kind, content, skill, arguments. "
            "kind must be respond, skill, done, or ask. Never claim a skill ran unless its result is present."
        )
        raw = self.provider.complete([{"role": "system", "content": system}, *messages], operation="agent.reason").strip()
        try:
            data = json.loads(raw)
            return AgentAction(str(data.get("kind", "respond")), str(data.get("content", "")), str(data.get("skill", "")), data.get("arguments") or {})
        except (json.JSONDecodeError, TypeError):
            return AgentAction("respond", raw)

    def run(self, user_text: str, history: list[dict[str, str]] | None = None) -> AgentAction:
        messages = list(history or []) + [{"role": "user", "content": user_text}]
        for _ in range(self.max_steps):
            action = self._decide(messages)
            if action.kind in {"respond", "done", "ask"}:
                return action
            if action.kind != "skill" or not action.skill:
                return AgentAction("respond", action.content)
            try:
                result = self.skills.execute(action.skill, **(action.arguments or {}))
            except Exception as exc:
                result = f"SKILL_ERROR {type(exc).__name__}: {exc}"
            messages += [
                {"role": "assistant", "content": action.content},
                {"role": "user", "content": f"RESULT FROM SKILL {action.skill}: {result}"},
            ]
        return AgentAction("ask", "I need another reasoning cycle to continue this objective.")
