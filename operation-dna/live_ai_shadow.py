"""Live observation -> attention -> AI controller shadow test.

The script uses the live read-only Alpaca crypto quote, wakes the AI controller
through the attention engine, and executes only a harmless local capability.
No broker order/account endpoint is called.
"""
from __future__ import annotations

from software.integrations.alpaca_public_crypto import AlpacaPublicCryptoAdapter
from software.runtime.ai_controller import AIController, Intent
from software.runtime.attention import AttentionEngine, AttentionRule, Event
from software.runtime.capabilities import Capability, CapabilityRegistry


def main() -> int:
    adapter = AlpacaPublicCryptoAdapter()
    observation = adapter.latest_quote("BTC/USD")
    payload = adapter.as_payload(observation)
    payload["trigger"] = True
    payload["trigger_reason"] = "shadow_behavior_test"

    attention = AttentionEngine()
    attention.register(
        AttentionRule(
            name="live_crypto_shadow",
            source="alpaca-public-crypto",
            predicate=lambda event: bool(event.data.get("trigger")),
            priority=10.0,
            estimated_ai_cost=0.0,
        )
    )

    event = Event(
        source=observation.provider,
        event_type=observation.event_type,
        data=payload,
        importance=1.0,
    )
    signals = attention.evaluate(event)
    wake = any(signal.wake_ai for signal in signals)

    registry = CapabilityRegistry()
    registry.register(
        Capability(
            name="shadow.inspect_signal",
            description="Inspect a live signal without external side effects.",
            handler=lambda symbol, bid_price, ask_price: {
                "action": "inspect",
                "symbol": symbol,
                "bid_price": bid_price,
                "ask_price": ask_price,
                "side_effects": False,
            },
            requires_authorization=False,
            reversible=True,
            risk_class="none",
        )
    )
    controller = AIController(registry)

    print(f"LIVE {observation.symbol}")
    print(f"ATTENTION signals={len(signals)}")
    print(f"AI WAKE = {'YES' if wake else 'NO'}")

    if not wake:
        print("SHADOW ACTION = NOT RUN")
        return 1

    signal = signals[0]
    intent = Intent(
        capability="shadow.inspect_signal",
        arguments={
            "symbol": payload["symbol"],
            "bid_price": payload["bid_price"],
            "ask_price": payload["ask_price"],
        },
        rationale=payload["trigger_reason"],
        autonomy_level=0,
        capital=0.0,
        irreversible=False,
    )
    result = controller.execute(intent)

    print(f"RULE={signal.rule} priority={signal.priority:.2f}")
    print(f"AI INTENT={intent.capability}")
    print(f"RATIONALE={intent.rationale}")
    print(f"SHADOW RESULT={result}")
    print("SIDE EFFECTS = False")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
