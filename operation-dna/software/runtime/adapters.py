"""Domain adapter contracts. Real integrations remain outside the sandbox."""
from dataclasses import dataclass
from typing import Any, Protocol

class DomainAdapter(Protocol):
    name: str
    def observe(self) -> list[dict[str, Any]]: ...
    def act(self, action: str, inputs: dict[str, Any]) -> Any: ...

@dataclass
class SyntheticAdapter:
    name: str
    observer: Any
    actor: Any
    def observe(self): return self.observer()
    def act(self, action, inputs): return self.actor(action, inputs)
