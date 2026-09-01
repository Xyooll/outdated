"""Persistent objective-aware conversational controller for Xyool."""
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
        return cls(text=str(data.get("text", "")), status=str(data.get("status", "active")), handoff=str(data.get("handoff", "")), context=dict(data.get("context", {})), turns=int(data.get("turns", 0)))

class AutonomousAgent:
    """Keep an objective alive while letting the model interpret conversation context."""
    def __init__(self, provider: Any, capabilities: SkillRegistry, behavior: str = "", max_steps: int = 12,
                 progress: Callable[[str], None] | None = None, state_file: str | Path | None = None,
                 project_objective: str = ""):
        self.provider = provider
        self.capabilities = capabilities
        self.behavior = behavior
        self.max_steps = max_steps
        self.progress = progress
        self.project_objective = project_objective.strip()
        self.orchestrator = AgentOrchestrator(provider, capabilities, max_steps=max_steps, behavior=behavior, progress=progress)
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
        self.state_file.write_text(json.dumps(self.objective.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")

    def _record_work(self, entries: list[dict[str, str]]) -> None:
        if self.objective is None:
            return
        log = self.objective.context.setdefault("work_log", [])
        if not isinstance(log, list):
            log = []
            self.objective.context["work_log"] = log
        for entry in entries:
            log.append({"what": str(entry.get("what", "")), "observation": str(entry.get("observation", ""))[:1200]})
        self.objective.context["work_log"] = log[-12:]

    def _message_context(self, text: str) -> str:
        project = f"PROJECT DEVELOPMENT OBJECTIVE:\n{self.project_objective}\n\n" if self.project_objective else ""
        if self.objective is None or self.objective.status == "complete":
            self.objective = ObjectiveState(text=text)
            self.objective.context["input_type"] = "new_objective"
            return project + text
        prior_status = self.objective.status
        self.objective.context["last_human_input"] = text
        self.objective.context["input_type"] = "human_input_with_active_objective"
        self.objective.turns += 1
        self.objective.status = "active"
        self.objective.handoff = ""
        work_log = self.objective.context.get("work_log", [])
        return (
            project + "ACTIVE OBJECTIVE:\n" + self.objective.text + "\n\nOBJECTIVE STATE:\n" +
            json.dumps(self.objective.context, ensure_ascii=False, default=str) + "\n\nRECENT WORK HISTORY:\n" +
            json.dumps(work_log[-12:], ensure_ascii=False, default=str) + "\n\nPREVIOUS STATUS: " + prior_status +
            "\nHUMAN MESSAGE:\n" + text +
            "\n\nInterpret this message using the objective, saved work history, and conversation context. If the human is asking what has happened, explain the actual saved progress and observations rather than starting unnecessary work. Continue the active objective when the message contributes to it, even without a continuation phrase. Start a new objective only when the human clearly establishes a distinct objective. When a distinct objective is established, return kind=new_objective and put the new objective in content. Preserve useful prior state unless replacement is clearly intended."
        )

    def send(self, text: str) -> AgentAction:
        incoming = {"role": "user", "content": text}
        action = self.orchestrator.run(self._message_context(text), self.history)
        self._record_work(self.orchestrator.observations)
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
        elif action.kind == "new_objective":
            self.objective = ObjectiveState(text=action.content.strip() or text.strip(), status="active")
            self.objective.context["input_type"] = "model_declared_new_objective"
        else:
            self.objective.status = "active"
        self._save_state()
        return action

    def reset(self) -> None:
        self.history.clear()
        self.objective = None
        self._save_state()
