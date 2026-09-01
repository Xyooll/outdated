"""Persistent objective-aware conversational controller for Xyool.

The model determines whether a human message advances the active objective or
starts a genuinely new one. No keyword list is used to interpret continuation.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
import json
from pathlib import Path
from typing import Any, Callable

from .agent_orchestrator import AgentAction, AgentOrchestrator, SkillRegistry


@dataclass
class ObjectiveState:
    """Durable state for the objective currently being pursued."""

    text: str
    status: str = "active"
    handoff: str = ""
    context: dict[str, Any] = field(default_factory=dict)
    turns: int = 0

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ObjectiveState":
        return cls(
            text=str(data.get("text", "")),
            status=str(data.get("status", "active")),
            handoff=str(data.get("handoff", "")),
            context=dict(data.get("context", {})),
            turns=int(data.get("turns", 0)),
        )


class AutonomousAgent:
    """Keep one objective alive while allowing the model to interpret new input."""

    def __init__(
        self,
        provider: Any,
        capabilities: SkillRegistry,
        behavior: str = "",
        max_steps: int = 12,
        progress: Callable[[str], None] | None = None,
        state_file: str | Path | None = None,
    ):
        self.provider = provider
        self.capabilities = capabilities
        self.behavior = behavior
        self.max_steps = max_steps
        self.progress = progress
        self.orchestrator = AgentOrchestrator(
            provider,
            capabilities,
            max_steps=max_steps,
            behavior=behavior,
            progress=progress,
        )
        self.history: list[dict[str, str]] = []
        self.state_file = Path(state_file) if state_file else None
        self.objective: ObjectiveState | None = self._load_state()

    def _load_state(self) -> ObjectiveState | None:
        if not self.state_file or not self.state_file.exists():
            return None
        try:
            data = json.loads(self.state_file.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                return None
            state = ObjectiveState.from_dict(data)
            return state if state.text else None
        except (OSError, json.JSONDecodeError, TypeError, ValueError):
            return None

    def _save_state(self) -> None:
        if not self.state_file:
            return
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        if self.objective is None:
            try:
                self.state_file.unlink(missing_ok=True)
            except OSError:
                pass
            return
        self.state_file.write_text(
            json.dumps(self.objective.to_dict(), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def _message_context(self, text: str) -> str:
        if self.objective is None or self.objective.status == "complete":
            self.objective = ObjectiveState(text=text)
            self.objective.context["input_type"] = "new_objective"
            return text

        prior_status = self.objective.status
        self.objective.context["last_human_input"] = text
        self.objective.context["input_type"] = "human_input_with_active_objective"
        self.objective.turns += 1
        self.objective.status = "active"
        self.objective.handoff = ""

        return (
            "ACTIVE OBJECTIVE:\n"
            f"{self.objective.text}\n\n"
            "OBJECTIVE STATE:\n"
            f"{json.dumps(self.objective.context, ensure_ascii=False, default=str)}\n\n"
            f"PREVIOUS STATUS: {prior_status}\n"
            "HUMAN MESSAGE:\n"
            f"{text}\n\n"
            "Interpret this message using the objective and conversation context. "
            "Continue the active objective when the message contributes to it, even "
            "when the user does not use a continuation phrase. Start a new objective "
            "only when the human clearly establishes a distinct objective. "
            "Do not restart useful discovery merely because the wording changed. "
            "Preserve the existing objective state unless there is strong evidence that "
            "the human intentionally replaced it."
        )

    def send(self, text: str) -> AgentAction:
        """Interpret input in context, pursue the active objective, and persist state."""
        incoming = {"role": "user", "content": text}
        text_for_agent = self._message_context(text)

        action = self.orchestrator.run(text_for_agent, self.history)
        self.history.extend([incoming, {"role": "assistant", "content": action.content}])

        if self.objective is None:
            self.objective = ObjectiveState(text=text)

        self.objective.context["last_action_kind"] = action.kind
        self.objective.context["last_action"] = action.content

        if action.kind == "ask":
            self.objective.status = "waiting_human"
            self.objective.handoff = action.content
        elif action.kind == "done":
            self.objective.status = "complete"
            self.objective.handoff = ""
        else:
            self.objective.status = "active"

        self._save_state()
        return action

    def reset(self) -> None:
        """Clear conversational and durable objective state."""
        self.history.clear()
        self.objective = None
        self._save_state()
