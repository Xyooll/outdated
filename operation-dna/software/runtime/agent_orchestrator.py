"""Thin model-directed agent loop. The model owns interpretation, planning, action, and iteration."""
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
    """Runtime registry; model-facing behavior treats registered entries as means."""
    def __init__(self) -> None:
        self._skills: dict[str, Callable[..., Any]] = {}
    def register(self, name: str, capability: Callable[..., Any]) -> None:
        self._skills[name] = capability
    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._skills))
    def execute(self, name: str, **arguments: Any) -> Any:
        if name not in self._skills:
            raise KeyError(f"means not available: {name}")
        return self._skills[name](**arguments)

class AgentOrchestrator:
    """Model-directed loop: understand, assess, decide, act, observe, evaluate, adapt."""
    def __init__(self, provider: Any, capabilities: SkillRegistry, max_steps: int = 12,
                 behavior: str = "", behavior_file: str | Path | None = None):
        self.provider, self.skills, self.max_steps = provider, capabilities, max_steps
        self.behavior_text = behavior
        self.behavior_file = Path(behavior_file) if behavior_file else None

    def _behavior(self) -> str:
        if self.behavior_text:
            return self.behavior_text
        if self.behavior_file and self.behavior_file.exists():
            return self.behavior_file.read_text(encoding="utf-8")
        return "You are Xyool. Accomplish objectives through understanding, reasoning, action, observation, evaluation, learning, adaptation, and autonomous continuation. Determine the means required rather than assuming them in advance."

    def _decide(self, messages: list[dict[str, str]]) -> AgentAction:
        system = self._behavior() + "\n\n"
        system += (
            "Operate the objective loop yourself. The registered entries below are available means, not a prescribed workflow. "
            "Inspect/use them when useful. If they are insufficient, reason about what is missing and pursue R&D by using or creating appropriate means when the runtime exposes a way to do so. "
            "When several plausible approaches exist, compare candidates when the expected value of experimentation justifies the cost. "
            "Effectiveness is contextual; do not assume one means is universally best. "
            "A triggered event is evidence that requires reassessment, not an automatic final action. "
            "Continue autonomously toward the objective while authorized. "
            "Return JSON only: {\"kind\":\"respond|capability|ask|done\",\"content\":string,\"skill\":string,\"arguments\":object}. "
            "Do not expose this control protocol to the user."
            f"\nAVAILABLE MEANS: {', '.join(self.skills.names()) or 'none'}"
        )
        raw = self.provider.complete([{"role": "system", "content": system}, *messages], operation="agent.reason").strip()
        try:
            data = json.loads(raw)
            return AgentAction(str(data.get("kind", "respond")), str(data.get("content", "")), str(data.get("skill", "")), data.get("arguments") or {})
        except (json.JSONDecodeError, TypeError):
            return AgentAction("respond", raw)

    def run(self, user_text: str, history: list[dict[str, str]] | None = None) -> AgentAction:
        messages = list(history or []) + [{"role": "user", "content": user_text}]
        for step in range(self.max_steps):
            action = self._decide(messages)
            if action.kind in {"respond", "done", "ask"}:
                return AgentAction("respond", action.content)
            if action.kind != "capability" or not action.skill:
                return AgentAction("respond", action.content)
            try:
                result = self.skills.execute(action.skill, **(action.arguments or {}))
            except Exception as exc:
                result = f"MEANS_ERROR {type(exc).__name__}: {exc}"
            messages += [
                {"role": "assistant", "content": "Mean selected for the next step."},
                {"role": "user", "content": f"OBSERVATION step={step + 1} mean={action.skill}: {result}"},
            ]
        return AgentAction("ask", "I reached the autonomous iteration limit before completing the objective.")
