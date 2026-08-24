"""Capability registry: software is the body's executable subconscious."""
from dataclasses import dataclass
from typing import Any, Callable

@dataclass(frozen=True)
class Capability:
    name: str
    description: str
    handler: Callable[..., Any]
    requires_authorization: bool = True
    reversible: bool = True
    risk_class: str = "low"

class CapabilityRegistry:
    def __init__(self):
        self._items: dict[str, Capability] = {}

    def register(self, capability: Capability) -> None:
        if capability.name in self._items:
            raise ValueError(f"capability already registered: {capability.name}")
        self._items[capability.name] = capability

    def describe(self) -> list[dict]:
        return [{"name": c.name, "description": c.description, "requires_authorization": c.requires_authorization, "reversible": c.reversible, "risk_class": c.risk_class} for c in self._items.values()]

    def get(self, name: str) -> Capability:
        try:
            return self._items[name]
        except KeyError:
            raise KeyError(f"unknown capability: {name}") from None

    def invoke(self, name: str, **kwargs: Any) -> Any:
        return self.get(name).handler(**kwargs)
