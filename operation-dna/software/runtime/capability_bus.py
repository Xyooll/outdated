"""Unified passive capability bus used by the active AI layer."""
from dataclasses import dataclass
from typing import Any, Callable

@dataclass(frozen=True)
class CapabilitySpec:
    name: str
    description: str
    handler: Callable[..., Any]
    risk_class: str = "low"
    reversible: bool = True
    requires_human: bool = False

class CapabilityBus:
    def __init__(self):
        self._capabilities: dict[str, CapabilitySpec] = {}

    def register(self, spec: CapabilitySpec) -> None:
        if spec.name in self._capabilities:
            raise ValueError(f"capability already registered: {spec.name}")
        self._capabilities[spec.name] = spec

    def catalog(self) -> list[dict[str, Any]]:
        return [
            {"name": c.name, "description": c.description, "risk_class": c.risk_class,
             "reversible": c.reversible, "requires_human": c.requires_human}
            for c in self._capabilities.values()
        ]

    def get(self, name: str) -> CapabilitySpec:
        if name not in self._capabilities:
            raise KeyError(f"unknown capability: {name}")
        return self._capabilities[name]

    def invoke(self, name: str, **arguments: Any) -> Any:
        return self.get(name).handler(**arguments)
