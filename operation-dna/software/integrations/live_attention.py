"""Bridge live read-only observations into Xyool's attention engine."""
from __future__ import annotations

from dataclasses import dataclass

from software.runtime.attention import AttentionEngine, AttentionRule, Event
from software.integrations.shadow import ShadowObservation

@dataclass(frozen=True)
class AttentionDecision:
    event: Event
    wake_ai: bool
    reasons: tuple[str, ...]


def observation_to_event(observation: ShadowObservation) -> Event:
    payload = dict(observation.payload)
    importance = 0.1 if observation.event_type == "market.signal" else 0.0
    size = payload.get("size")
    if isinstance(size, (int, float)) and size >= 10000:
        importance += 2.0
    return Event(source=observation.provider, event_type=observation.event_type, data=payload, importance=importance)


def _large_market_trade(event: Event) -> bool:
    size = event.data.get("size")
    return isinstance(size, (int, float)) and size >= 10000


def _ordinary_market_trade(event: Event) -> bool:
    size = event.data.get("size")
    return not isinstance(size, (int, float)) or size < 10000


def build_default_attention() -> AttentionEngine:
    engine = AttentionEngine()
    engine.register(AttentionRule("large_market_trade", "alpaca", _large_market_trade, priority=3.0, estimated_ai_cost=0.05))
    engine.register(AttentionRule("ordinary_market_trade", "alpaca", _ordinary_market_trade, priority=-1.0, estimated_ai_cost=0.01))
    return engine


def decide(observation: ShadowObservation, engine: AttentionEngine | None = None) -> AttentionDecision:
    event = observation_to_event(observation)
    signals = (engine or build_default_attention()).evaluate(event)
    active = [signal for signal in signals if signal.wake_ai]
    if not signals:
        return AttentionDecision(event, False, ("no matching rule",))
    if not active:
        return AttentionDecision(event, False, tuple(signal.rule for signal in signals))
    return AttentionDecision(event, True, tuple(signal.rule for signal in active))
