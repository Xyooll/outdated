"""Provider-neutral shadow integrations.

Shadow adapters observe/normalize external-style payloads without performing side effects.
Real providers can implement the same protocol later.
"""
from dataclasses import dataclass
from typing import Any, Protocol

@dataclass(frozen=True)
class ShadowObservation:
    provider: str
    event_type: str
    payload: dict[str, Any]
    side_effects: bool = False

class ObservationProvider(Protocol):
    name: str
    def observe(self) -> ShadowObservation: ...

class StaticProvider:
    """Deterministic adapter used for integration tests and local shadow mode."""
    def __init__(self, name: str, event_type: str, payload: dict[str, Any]):
        self.name = name
        self._observation = ShadowObservation(name, event_type, dict(payload))

    def observe(self) -> ShadowObservation:
        return self._observation

class ShadowRegistry:
    def __init__(self):
        self.providers: dict[str, ObservationProvider] = {}

    def register(self, provider: ObservationProvider) -> None:
        if provider.name in self.providers:
            raise ValueError(f"provider already registered: {provider.name}")
        self.providers[provider.name] = provider

    def observe_all(self) -> list[ShadowObservation]:
        return [self.providers[name].observe() for name in sorted(self.providers)]
