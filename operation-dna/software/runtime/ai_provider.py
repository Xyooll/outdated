"""Provider-neutral reasoning interface. Real providers are injected at runtime."""
from dataclasses import dataclass
from typing import Any, Protocol

class AIProvider(Protocol):
    def reason(self, prompt: str, context: list[dict[str, Any]]) -> dict[str, Any]: ...

@dataclass
class LocalStubProvider:
    """Deterministic test provider; performs no external calls."""
    def reason(self, prompt: str, context: list[dict[str, Any]]) -> dict[str, Any]:
        return {"status": "stub", "prompt": prompt, "context_items": len(context)}
