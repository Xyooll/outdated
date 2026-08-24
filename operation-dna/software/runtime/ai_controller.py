"""AI executive controller over passive capabilities and human authority."""
from dataclasses import dataclass
from typing import Any
from .capabilities import CapabilityRegistry
from .authority import HumanAuthority

@dataclass(frozen=True)
class Intent:
    capability: str
    arguments: dict[str, Any]
    rationale: str = ""
    autonomy_level: int = 0
    capital: float = 0.0
    irreversible: bool = False

class AIController:
    """Active intelligence; human policy remains the ultimate execution boundary."""
    def __init__(self, registry: CapabilityRegistry, authority: HumanAuthority | None = None):
        self.registry = registry
        self.authority = authority or HumanAuthority()

    def available_capabilities(self) -> list[dict]:
        return self.registry.describe()

    def execute(self, intent: Intent) -> Any:
        capability = self.registry.get(intent.capability)
        if capability.requires_authorization and not self.authority.authorize(
            autonomy_level=intent.autonomy_level,
            capital=intent.capital,
            irreversible=intent.irreversible,
        ):
            raise PermissionError(f"human authorization required: {intent.capability}")
        return self.registry.invoke(intent.capability, **intent.arguments)
