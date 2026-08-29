"""Thin model-directed agent loop. The model owns interpretation and planning."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable
import json
from pathlib import Path

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
            raise KeyError(f"capability not available: {name}")
        return self._skills[name](**arguments)

class AgentOrchestrator:
    """A minimal loop: model decides, runtime executes, model observes and decides again."""
    def __init__(self, provider: Any, skills: SkillRegistry, max_steps: int = 12,
                 behavior_file: str | Path | None = None):
        self.provider, self.skills, self.max_steps = provider, skills, max_steps
        self.behavior_file = Path(behavior_file) if behavior_file else None

    def _behavior(self) -> str:
        if self.behavior_file and self.behavior_file.exists():
            return self.behavior_file.read_text(encoding="utf-8")
        return (
            "You are Xyool, an autonomous general-purpose agent. Understand objectives in context. "
            "Inspect available capabilities, reuse or adapt what exists, create what is missing, "
            "test and evaluate results, observe outcomes, and continue toward completion. "
            "Conversation is open-ended; never use keyword-triggered workflows."
        )

    def _decide(self, messages: list[dict[str, str]]) -> AgentAction:
        system = self._behavior() + "\n\n"
        system += (
            "You control the reasoning loop. Available capabilities are exposed below. "
            "Choose a capability only when useful. You may call capabilities repeatedly and in sequence. "
            "Return JSON only: {\"kind\":\"respond|capability|ask|done\",\"content\":string,"
            "\"skill\":string,\"arguments\":object}. "
            "Do not expose this control protocol to the user."
            f"\nAVAILABLE CAPABILITIES: {', '.join(self.skills.names()) or 'none'}"
        )
        raw = self.provider.complete([{"role": "system", "content": system}, *messages], operation="agent.reason").strip()
        try:
            data = json.loads(raw)
            return AgentAction(str(data.get("kind", "respond")), str(data.get("content", "")),
                               str(data.get("skill", "")), data.get("arguments") or {})
        except (json.JSONDecodeError, TypeError):
            return AgentAction("respond", raw)

    def run(self, user_text: str, history: list[dict[str, str]] | None = None) -> AgentAction:
        messages = list(history or []) + [{"role": "user", "content": user_text}]
        for _ in range(self.max_steps):
            action = self._decide(messages)
            if action.kind in {"respond", "done", "ask"}:
                return AgentAction("respond", action.content)
            if action.kind != "capability" or not action.skill:
                return AgentAction("respond", action.content)
            try:
                result = self.skills.execute(action.skill, **(action.arguments or {}))
            except Exception as exc:
                result = f"CAPABILITY_ERROR {type(exc).__name__}: {exc}"
            messages += [
                {"role": "assistant", "content": "Capability selected."},
                {"role": "user", "content": f"CAPABILITY RESULT ({action.skill}): {result}"},
            ]
        return AgentAction("ask", "I reached the runtime step limit before completing the objective.")
