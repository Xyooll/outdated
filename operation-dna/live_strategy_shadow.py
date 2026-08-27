"""Live market strategy shadow runner.

Reads Alpaca market data, builds rolling features, evaluates multiple strategies,
and ranks them. This module never places or modifies orders.
"""
from __future__ import annotations

import argparse
import time

from software.integrations.alpaca_readonly import AlpacaReadOnlyProvider
from software.runtime.market_features import FeatureEngine
from software.runtime.strategy_engine import StrategyEngine


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", default="AAPL")
    parser.add_argument("--cycles", type=int, default=20)
    parser.add_argument("--interval", type=float, default=5.0)
    parser.add_argument("--strategies", default="baseline,fast,patient,momentum,mean_reversion")
    args = parser.parse_args()
    if args.cycles < 1:
        raise SystemExit("--cycles must be >= 1")
    if args.interval < 0:
        raise SystemExit("--interval must be >= 0")

    all_strategies = StrategyEngine()
    selected = [x.strip().lower() for x in args.strategies.split(",") if x.strip()]
    unknown = [x for x in selected if x not in all_strategies.strategies]
    if unknown:
        raise SystemExit(f"unknown strategies: {', '.join(unknown)}")
    engine = StrategyEngine({name: all_strategies.strategies[name] for name in selected})
    market = AlpacaReadOnlyProvider(symbol=args.symbol.upper())
    features = FeatureEngine()

    for cycle in range(args.cycles):
        observation = market.observe()
        payload = observation.payload
        current = features.update(float(payload["price"]), volume=float(payload.get("size") or 0))
        results = engine.evaluate(current)
        leader = results[0]
        print(
            f"CYCLE={cycle + 1} LIVE {args.symbol.upper()} PRICE={current.price:.4f} "
            f"RETURN3={current.return_3:.5f} RETURN5={current.return_5:.5f} "
            f"VOL5={current.volatility_5:.5f} LEADER={leader.strategy} "
            f"ACTION={leader.signal.action.upper()} CONFIDENCE={leader.signal.confidence:.4f} "
            f"SCORE={leader.signal.score:.4f} REASON={leader.signal.reason}"
        )
        for result in results:
            print(
                f"  STRATEGY={result.strategy} ACTION={result.signal.action.upper()} "
                f"CONFIDENCE={result.signal.confidence:.4f} SCORE={result.signal.score:.4f}"
            )
        if cycle + 1 < args.cycles:
            time.sleep(args.interval)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
