"""Production-readiness controls: persistent state, rollback, kill switch, and budgets."""
from dataclasses import dataclass, field
from pathlib import Path
import json
from typing import Any

@dataclass
class ResourceBudget:
    max_cost: float = 1.0
    max_actions: int = 10
    max_experiments: int = 100
    spent: float = 0.0
    actions: int = 0
    experiments: int = 0

    def allow_cost(self, amount: float) -> bool:
        return amount >= 0 and self.spent + amount <= self.max_cost
    def consume(self, cost: float = 0.0, action: bool = False, experiment: bool = False) -> None:
        if not self.allow_cost(cost): raise RuntimeError("resource cost budget exceeded")
        if action and self.actions + 1 > self.max_actions: raise RuntimeError("action budget exceeded")
        if experiment and self.experiments + 1 > self.max_experiments: raise RuntimeError("experiment budget exceeded")
        self.spent += cost; self.actions += int(action); self.experiments += int(experiment)

class KillSwitch:
    def __init__(self): self._stopped = False
    def stop(self): self._stopped = True
    def reset(self): self._stopped = False
    def check(self):
        if self._stopped: raise RuntimeError("kill switch engaged")

@dataclass
class VersionRecord:
    version: str
    artifact: Any
    status: str = "candidate"

class VersionStore:
    def __init__(self, path: str = "data/versions.json"):
        self.path = Path(path); self.path.parent.mkdir(parents=True, exist_ok=True)
        self.records: list[VersionRecord] = []
    def add(self, version: str, artifact: Any, status: str = "candidate"):
        self.records.append(VersionRecord(version, artifact, status)); self._save()
    def promote(self, version: str):
        for r in self.records: r.status = "active" if r.version == version else ("rollback" if r.status == "active" else r.status)
        self._save()
    def active(self):
        return next((r for r in reversed(self.records) if r.status == "active"), None)
    def rollback(self):
        active = self.active()
        candidates = [r for r in self.records if r.version != (active.version if active else None)]
        if not candidates: return None
        previous = candidates[-1]; self.promote(previous.version); return previous
    def _save(self):
        self.path.write_text(json.dumps([r.__dict__ for r in self.records], default=str), encoding="utf-8")

@dataclass
class RuntimeState:
    mission: str = ""
    paused: bool = False
    data: dict[str, Any] = field(default_factory=dict)

class PersistentState:
    def __init__(self, path: str = "data/runtime_state.json"):
        self.path = Path(path); self.path.parent.mkdir(parents=True, exist_ok=True)
    def save(self, state: RuntimeState): self.path.write_text(json.dumps(state.__dict__, default=str), encoding="utf-8")
    def load(self) -> RuntimeState:
        if not self.path.exists(): return RuntimeState()
        raw = json.loads(self.path.read_text(encoding="utf-8")); return RuntimeState(**raw)
