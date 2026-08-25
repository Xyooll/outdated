"""Event-driven attention engine: passive software decides when the active AI is worth waking."""
from dataclasses import dataclass
from typing import Any, Callable

@dataclass(frozen=True)
class Event:
    source: str
    event_type: str
    data: dict[str, Any]
    importance: float = 0.0

@dataclass(frozen=True)
class AttentionRule:
    name: str
    source: str
    predicate: Callable[[Event], bool]
    priority: float = 1.0
    estimated_ai_cost: float = 1.0

@dataclass(frozen=True)
class AttentionSignal:
    rule: str
    priority: float
    event: Event
    wake_ai: bool

class AttentionEngine:
    def __init__(self):
        self._rules: list[AttentionRule] = []

    def register(self, rule: AttentionRule) -> None:
        self._rules.append(rule)

    def evaluate(self, event: Event) -> list[AttentionSignal]:
        signals = []
        for rule in self._rules:
            if rule.source != event.source:
                continue
            if rule.predicate(event):
                score = max(0.0, rule.priority + event.importance)
                signals.append(AttentionSignal(rule.name, score, event, score > 0))
        return sorted(signals, key=lambda x: x.priority, reverse=True)
