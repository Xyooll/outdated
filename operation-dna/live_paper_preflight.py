"""Preflight and explicitly gated paper execution for Xyool.

Default behavior is READ-ONLY: verify credentials and account state.
Submitting a paper order requires BOTH --submit and XYOOL_PAPER_EXECUTE=YES.
The adapter hard-rejects any non-paper Alpaca endpoint.
"""
from __future__ import annotations

import argparse
import os
import uuid

from software.integrations.alpaca_paper import AlpacaPaperAdapter


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--submit", action="store_true", help="submit one paper market order")
    parser.add_argument("--symbol", default="AAPL")
    parser.add_argument("--qty", type=float, default=1.0)
    parser.add_argument("--side", choices=["buy", "sell"], default="buy")
    args = parser.parse_args()

    adapter = AlpacaPaperAdapter()
    account = adapter.account()
    print(
        f"PAPER ACCOUNT status={account.status} equity={account.equity:.2f} "
        f"buying_power={account.buying_power:.2f} trading_blocked={account.trading_blocked}"
    )

    if not args.submit:
        print("PAPER EXECUTION=DISABLED (preflight only)")
        return 0

    if os.getenv("XYOOL_PAPER_EXECUTE") != "YES":
        raise SystemExit("refusing paper order: set XYOOL_PAPER_EXECUTE=YES explicitly")
    if account.status != "ACTIVE" or account.trading_blocked:
        raise SystemExit("refusing paper order: account is not eligible for trading")

    client_order_id = f"xyool-paper-{uuid.uuid4().hex[:20]}"
    order = adapter.submit_market_order(args.symbol, args.qty, args.side, client_order_id)
    print(f"PAPER ORDER SUBMITTED id={order.get('id')} status={order.get('status')} side_effects=True")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
