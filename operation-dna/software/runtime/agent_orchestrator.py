"""Model-directed autonomous reasoning loop."""
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
    """Registered tools are available means; the model decides whether/how to use them."""
    def __init__(self) -> None:
        self._skills: dict[str, Callable[..., Any]] = {}
    def register(self, name: str, capability: Callable[..., Any]) -> None:
        self._skills[name] = capability
    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._skills))
    def execute(self, name: str, **arguments: Any) -> Any:
        if name not in self._skills:
            raise KeyError(f"mean not available: {name}")
        return self._skills[name](**arguments)

class AgentOrchestrator:
    """Each observation returns to the model for another reasoning cycle."""
    def __init__(self, provider: Any, capabilities: SkillRegistry, max_steps: int = 12,
                 behavior: str = "", behavior_file: str | Path | None = None,
                 progress: Callable[[str], None] | None = None):
        self.provider, self.skills, self.max_steps = provider, capabilities, max_steps
        self.behavior_text = behavior
        self.behavior_file = Path(behavior_file) if behavior_file else None
        self.progress = progress

    def _progress(self, message: str) -> None:
        if self.progress:
            self.progress(message)

    def _behavior(self) -> str:
        if self.behavior_text:
            return self.behavior_text
        if self.behavior_file and self.behavior_file.exists():
            return self.behavior_file.read_text(encoding="utf-8")
        return "You are Xyool. Accomplish objectives through understanding, reasoning, action, observation, evaluation, learning, adaptation, and autonomous continuation."

    def _decide(self, messages: list[dict[str, str]]) -> AgentAction:
        system = self._behavior() + "\n\n" + (
            "You control the objective loop. After EVERY observation, reason again before deciding whether to continue or respond. "
            "Do NOT stop merely because one mean returned a result or because you can describe missing components. If the objective is incomplete, select another available mean or initiate appropriate R&D through an available means. "
            "Do not invent tools, results, or completed work. Registered means are resources, not a prescribed workflow. "
            "When multiple plausible approaches exist, compare candidates when worthwhile. Effectiveness is contextual. "
            "Triggers are evidence that prompt reassessment; they do not dictate final actions. "
            "Only finish when the objective is actually accomplished, meaningful human judgment/authorization is required, or available resources make further progress genuinely impossible. "
            "For ordinary conversation, respond naturally without unnecessary tool use. "
            "Return JSON only: {\"kind\":\"use_mean|respond|done|ask\",\"content\":string,\"skill\":string,\"arguments\":object}. "
            "For use_mean, content briefly states why this is the next action. For respond/done/ask, content is user-facing. "
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
        self._progress("Analyzing objective...")
        for step in range(self.max_steps):
            self._progress(f"Reasoning cycle {step + 1}/{self.max_steps}...")
            action = self._decide(messages)
            if action.kind in {"respond", "done", "ask"}:
                return AgentAction("respond", action.content)
            if action.kind != "use_mean" or not action.skill:
                return AgentAction("respond", action.content)
            self._progress(f"Using {action.skill}...")
            try:
                result = self.skills.execute(action.skill, **(action.arguments or {}))
            except Exception as exc:
                result = f"MEANS_ERROR {type(exc).__name__}: {exc}"
            self._progress("Observing result and reassessing...")
            messages += [
                {"role": "assistant", "content": f"Selected mean: {action.skill}. Reason: {action.content}"},
                {"role": "user", "content": f"OBSERVATION step={step + 1} mean={action.skill}: {result}"},
            ]
        return AgentAction("respond", "I reached the autonomous iteration limit before completing the objective.")
