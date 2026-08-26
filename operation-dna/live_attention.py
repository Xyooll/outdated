"""Live Alpaca observation -> Xyool attention gateway.

The gateway deliberately keeps ordinary quotes out of the AI path. Only
configured deterministic triggers wake the active AI layer. This script is
read-only and never submits or modifies an order.
"""
from __future__ import annotations

from software.integrations.alpaca_public_crypto import AlpacaPublicCryptoAdapter
from software.runtime.attention import AttentionEngine, AttentionRule, Event


def main() -> int:
    adapter = AlpacaPublicCryptoAdapter()
    observation = adapter.latest_quote("BTC/USD")
    payload = adapter.as_payload(observation)

    engine = AttentionEngine()
    engine.register(
        AttentionRule(
            name="quote_anomaly",
            source="alpaca-public-crypto",
            predicate=lambda event: bool(event.data.get("trigger", False)),
            priority=2.0,
            estimated_ai_cost=1.0,
        )
    )

    event = Event(
        source=observation.provider,
        event_type=observation.event_type,
        data=payload,
        importance=0.0,
    )
    signals = engine.evaluate(event)

    print(f"LIVE {observation.symbol}")
    print("ATTENTION signals=", len(signals))
    print("AI WAKE =", "YES" if any(s.wake_ai for s in signals) else "NO")
    if signals:
        for signal in signals:
            print(
                f"RULE={signal.rule} priority={signal.priority:.2f} "
                f"estimated_ai_cost={next(r.estimated_ai_cost for r in engine._rules if r.name == signal.rule):.2f}"
            )
    else:
        print("REASON=No configured trigger matched; log-only path")
    print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
