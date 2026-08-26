"""Run Xyool's Stage-2 provider shadow integration locally.

This intentionally performs no external writes. Replace StaticProvider instances with
real read-only adapters as they become available.
"""
from software.integrations.shadow import ShadowRegistry, StaticProvider

def build_shadow_registry() -> ShadowRegistry:
    registry = ShadowRegistry()
    registry.register(StaticProvider("alpaca", "market.signal", {"symbol": "TEST", "price": 101.0}))
    registry.register(StaticProvider("binance", "crypto.signal", {"symbol": "TESTUSDT", "price": 50.0}))
    registry.register(StaticProvider("business", "opportunity.signal", {"category": "test", "score": 0.9}))
    return registry

def main() -> int:
    registry = build_shadow_registry()
    for observation in registry.observe_all():
        print(f"SHADOW provider={observation.provider} event={observation.event_type} side_effects={observation.side_effects} payload={observation.payload}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
