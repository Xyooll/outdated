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
    """Available operations are resources; the model chooses how to use them."""
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
    """Persistent observe→reassess→act loop with model-directed resource selection."""
    VALID_KINDS = {"use_mean", "respond", "done", "ask", "new_objective"}

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
            "You control the objective loop. Return EXACTLY ONE JSON object and no other text. "
            "The object must contain kind, content, skill, and arguments. kind must be one of use_mean, respond, done, ask, new_objective. "
            "Never emit multiple JSON objects or a multi-action plan. "
            "After every observation, reassess the actual state and choose the next useful action. "
            "A resource-producing, build, or R&D action is intermediate work, never proof that the objective is complete. "
            "After creating or changing something, inspect its actual result and test/evaluate it when applicable. "
            "Do not claim done until the objective's success conditions are actually verified. "
            "Do not repeat a substantially identical resource call unless the new call is deliberate verification or the state materially changed. "
            "When an existing resource is insufficient, use available R&D or engineering resources to create or improve what is needed, then test and evaluate it. "
            "Different resources can be more effective in different situations; compare candidates when useful. "
            "Any triggers encountered are evidence for reassessment, not automatic final actions. "
            "Request human action only when a genuine dependency remains: authorization/consent, human-only information or judgment, required external access, physical action, consequences beyond authority, or unacceptable risk. "
            "When a distinct user objective replaces the current objective, use kind=new_objective and put the new objective in content. "
            "Ordinary conversation uses respond. Never invent a result, resource, credential, or completion. "
            f"\nAVAILABLE RESOURCES: {', '.join(self.skills.names()) or 'none'}"
        )
        raw = self.provider.complete([{"role": "system", "content": system}, *messages], operation="agent.reason").strip()
        try:
            data = json.loads(raw)
            if not isinstance(data, dict):
                raise ValueError("action is not an object")
            kind = str(data.get("kind", "respond"))
            if kind not in self.VALID_KINDS:
                raise ValueError(f"invalid action kind: {kind}")
            args = data.get("arguments", {})
            if not isinstance(args, dict):
                args = {}
            return AgentAction(kind, str(data.get("content", "")), str(data.get("skill", "")), args)
        except (json.JSONDecodeError, TypeError, ValueError):
            return AgentAction("respond", raw)

    def run(self, user_text: str, history: list[dict[str, str]] | None = None) -> AgentAction:
        messages = list(history or []) + [{"role": "user", "content": user_text}]
        self._progress("Analyzing objective...")
        used_means: set[tuple[str, str]] = set()
        had_observation = False
        for step in range(self.max_steps):
            self._progress(f"Reasoning cycle {step + 1}/{self.max_steps}...")
            action = self._decide(messages)
            if action.kind in {"ask", "new_objective"}:
                return action
            if action.kind == "done":
                if had_observation:
                    return action
                messages.append({"role": "user", "content": "OBSERVATION: Nothing concrete has been done or observed yet. Continue autonomously."})
                continue
            if action.kind == "respond":
                return action
            if action.kind != "use_mean" or not action.skill:
                return AgentAction("respond", action.content)

            fingerprint = (action.skill, json.dumps(action.arguments or {}, sort_keys=True, default=str))
            if fingerprint in used_means:
                messages.append({"role": "user", "content": f"OBSERVATION: identical resource call {action.skill} was already executed. Do not repeat it. Choose another unresolved action or a deliberate verification."})
                continue
            used_means.add(fingerprint)
            self._progress(f"Using {action.skill}...")
            try:
                result = self.skills.execute(action.skill, **(action.arguments or {}))
            except Exception as exc:
                result = f"MEANS_ERROR {type(exc).__name__}: {exc}"
            had_observation = True
            self._progress("Observing result and reassessing...")
            result_text = str(result)
            messages += [
                {"role": "assistant", "content": json.dumps({"kind": "use_mean", "skill": action.skill, "content": action.content, "arguments": action.arguments or {}}, ensure_ascii=False)},
                {"role": "user", "content": f"OBSERVATION step={step + 1} resource={action.skill}: {result_text}"},
            ]
        return AgentAction("respond", "I reached the autonomous iteration limit before completing the objective. The current state is preserved; continue when more iteration is available.")
