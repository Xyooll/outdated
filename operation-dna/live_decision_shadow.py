"""Live market -> attention -> bounded AI decision -> forecast -> shadow outcome.

No broker orders, account access, or external side effects are performed.
The realized outcome is intentionally simulated from the observed quote so the
entire decision/evaluation/learning plumbing can be exercised deterministically.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from software.economics.learning import Forecast, Outcome, calibration, evaluate
from software.integrations.alpaca_public_crypto import AlpacaPublicCryptoAdapter
from software.runtime.ai_controller import AIController, Intent
from software.runtime.attention import AttentionEngine, AttentionRule, Event
from software.runtime.capabilities import Capability, CapabilityRegistry
from software.runtime.production_readiness import KillSwitch, PersistentState, ResourceBudget, RuntimeState


@dataclass(frozen=True)
class Decision:
    action: str
    confidence: float
    expected_upside: float
    expected_downside: float
    rationale: str


def stable_id(*parts: object) -> str:
    raw = "|".join(map(str, parts)).encode()
    return hashlib.sha256(raw).hexdigest()[:24]


def choose_decision(bid: float, ask: float) -> Decision:
    spread = ask - bid
    # This is deliberately a bounded shadow heuristic, not a trading strategy.
    if spread > 0:
        return Decision("OBSERVE", 0.75, 0.0, 0.0, f"positive spread={spread:.6f}; shadow system observes")
    return Decision("IGNORE", 0.90, 0.0, 0.0, "non-positive spread")


def main() -> int:
    adapter = AlpacaPublicCryptoAdapter()
    quote = adapter.latest_quote("BTC/USD")
    payload = adapter.as_payload(quote)
    event = Event(quote.provider, quote.event_type, payload, importance=1.0)

    attention = AttentionEngine()
    attention.register(AttentionRule(
        name="live_crypto_decision",
        source=quote.provider,
        predicate=lambda e: e.data.get("bid_price", 0) < e.data.get("ask_price", 0),
        priority=10.0,
        estimated_ai_cost=0.0,
    ))
    signals = attention.evaluate(event)
    if not signals or not signals[0].wake_ai:
        print("AI WAKE = NO")
        return 1

    registry = CapabilityRegistry()
    registry.register(Capability(
        name="shadow.make_decision",
        description="Create a bounded market decision without execution.",
        handler=lambda bid_price, ask_price: choose_decision(float(bid_price), float(ask_price)),
        requires_authorization=False,
        reversible=True,
        risk_class="none",
    ))
    ai = AIController(registry)
    intent = Intent(
        capability="shadow.make_decision",
        arguments={"bid_price": payload["bid_price"], "ask_price": payload["ask_price"]},
        rationale="attention signal reached AI",
        autonomy_level=0,
        capital=0.0,
        irreversible=False,
    )

    kill = KillSwitch()
    budget = ResourceBudget(max_cost=1.0, max_actions=1, max_experiments=1)
    state = PersistentState("data/shadow_runtime_state.json")
    runtime = RuntimeState(mission="live decision shadow", paused=False)
    kill.check()
    budget.consume(experiment=True)
    decision = ai.execute(intent)
    runtime.data.update({"symbol": quote.symbol, "decision": decision.__dict__})
    state.save(runtime)

    forecast_id = stable_id(quote.symbol, quote.timestamp, decision.action, payload["bid_price"], payload["ask_price"])
    forecast = Forecast(
        forecast_id=forecast_id,
        opportunity_key=quote.symbol,
        predicted_score=decision.confidence,
        predicted_upside=decision.expected_upside,
        predicted_downside=decision.expected_downside,
        created_at=datetime.now(timezone.utc).isoformat(),
    )

    # Shadow-only outcome: no market order is placed. This synthetic outcome exists
    # solely to exercise the evaluation/learning path until a paper-execution adapter exists.
    outcome = Outcome(
        forecast_id=forecast.forecast_id,
        realized_return=0.0,
        realized_cost=0.0,
        observed_at=datetime.now(timezone.utc).isoformat(),
    )
    result = evaluate(forecast, outcome)
    metrics = calibration([result])

    record = {
        "event": payload,
        "attention": {"signals": len(signals), "wake_ai": True, "priority": signals[0].priority},
        "intent": intent.__dict__,
        "decision": decision.__dict__,
        "forecast": forecast.__dict__,
        "outcome": outcome.__dict__,
        "evaluation": result,
        "calibration": metrics,
        "side_effects": False,
    }
    Path("data").mkdir(exist_ok=True)
    Path("data/live_decision_shadow.json").write_text(json.dumps(record, default=lambda x: x.__dict__, indent=2), encoding="utf-8")

    print(f"LIVE {quote.symbol}")
    print(f"BID={payload['bid_price']:.6f} ASK={payload['ask_price']:.6f}")
    print(f"AI WAKE = YES")
    print(f"AI INTENT={intent.capability}")
    print(f"DECISION={decision.action} confidence={decision.confidence:.2f}")
    print(f"FORECAST={forecast.forecast_id}")
    print(f"EVALUATION direction_correct={result['direction_correct']} absolute_error={result['absolute_error']:.4f}")
    print(f"CALIBRATION samples={metrics['samples']} direction_accuracy={metrics['direction_accuracy']:.2f}")
    print("SIDE EFFECTS = False")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
