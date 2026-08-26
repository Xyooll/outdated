"""Run one explicitly gated paper order through the Operation-DNA safety boundary.

Default mode is a read-only readiness check. Actual paper submission requires
both --execute and XYOOL_PAPER_EXECUTE=YES. No live Alpaca endpoint is accepted.
"""
from __future__ import annotations

import argparse
import os

from software.integrations.alpaca_paper import AlpacaPaperAdapter
from software.runtime.paper_execution_controller import PaperExecutionController


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--symbol", default="AAPL")
    parser.add_argument("--qty", type=float, default=1.0)
    parser.add_argument("--side", choices=["buy", "sell"], default="buy")
    parser.add_argument("--reference-price", type=float, default=1.0)
    parser.add_argument("--max-notional", type=float, default=100.0)
    args = parser.parse_args()

    adapter = AlpacaPaperAdapter()
    account = adapter.account()
    print(f"PAPER ACCOUNT status={account.status} equity={account.equity:.2f} buying_power={account.buying_power:.2f} trading_blocked={account.trading_blocked}")

    controller = PaperExecutionController(
        broker=adapter,
        execution_enabled=args.execute,
        max_notional=args.max_notional,
    )

    if not args.execute:
        print("PAPER EXECUTION=DISABLED (readiness only)")
        print("GATES=kill_switch,pause,opt_in,account,order_validation,notional,budget,audit")
        return 0

    if os.getenv("XYOOL_PAPER_EXECUTE") != "YES":
        raise SystemExit("refusing paper order: set XYOOL_PAPER_EXECUTE=YES explicitly")

    result = controller.execute_market_order(
        args.symbol, args.qty, args.side, args.reference_price
    )
    print(f"PAPER ORDER status={result.status} id={result.client_order_id} symbol={result.symbol} qty={result.qty} side={result.side} notional={result.estimated_notional:.2f} side_effects=True")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
