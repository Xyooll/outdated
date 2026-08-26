"""Deterministic live-trigger test for the Xyool attention gateway.

Read-only: this script observes a public Alpaca crypto quote and forces a
controlled trigger event from the observed spread. It never submits orders.
"""
from __future__ import annotations

from software.integrations.alpaca_public_crypto import AlpacaPublicCryptoAdapter
from software.runtime.attention import AttentionEngine, AttentionRule, Event


def main() -> int:
    adapter = AlpacaPublicCryptoAdapter()
    observation = adapter.latest_quote("BTC/USD")
    payload = adapter.as_payload(observation)

    bid = float(payload["bid_price"])
    ask = float(payload["ask_price"])
    spread = ask - bid

    # Controlled test trigger: a positive spread is guaranteed for a normal
    # two-sided quote. This proves the trigger -> attention -> AI-wake path.
    payload["trigger"] = spread > 0
    payload["trigger_reason"] = "positive_bid_ask_spread"
    payload["spread"] = spread

    engine = AttentionEngine()
    engine.register(
        AttentionRule(
            name="quote_spread_test",
            source="alpaca-public-crypto",
            predicate=lambda event: bool(event.data.get("trigger", False)),
            priority=10.0,
            estimated_ai_cost=1.0,
        )
    )

    event = Event(
        source=observation.provider,
        event_type=observation.event_type,
        data=payload,
        importance=1.0 if payload["trigger"] else 0.0,
    )
    signals = engine.evaluate(event)

    print(f"LIVE {observation.symbol}")
    print(f"BID={bid:.6f} ASK={ask:.6f} SPREAD={spread:.6f}")
    print(f"TRIGGER = {'YES' if payload['trigger'] else 'NO'}")
    print(f"ATTENTION signals={len(signals)}")
    print(f"AI WAKE = {'YES' if any(s.wake_ai for s in signals) else 'NO'}")
    if signals:
        for signal in signals:
            print(
                f"RULE={signal.rule} priority={signal.priority:.2f} "
                f"reason={payload['trigger_reason']}"
            )
    print("SIDE EFFECTS = False")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
