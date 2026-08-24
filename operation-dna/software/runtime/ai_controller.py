"""AI executive controller over registered software capabilities."""
from dataclasses import dataclass
from typing import Any
from .capabilities import CapabilityRegistry

@dataclass(frozen=True)
class Intent:
    capability: str
    arguments: dict[str, Any]
    rationale: str = ""

class AIController:
    """Turns model decisions into capability calls; safety remains below it."""
    def __init__(self, registry: CapabilityRegistry):
        self.registry = registry

    def available_capabilities(self) -> list[dict]:
        return self.registry.describe()

    def execute(self, intent: Intent) -> Any:
        capability = self.registry.get(intent.capability)
        if capability.requires_authorization:
            raise PermissionError(f"authorization required for capability: {intent.capability}")
        return self.registry.invoke(intent.capability, **intent.arguments)
