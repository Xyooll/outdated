"""Controlled paper loop: live observation -> decision -> risk -> paper execution.

Execution remains disabled unless both --execute and XYOOL_PAPER_EXECUTE=YES are present.
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path

from software.integrations.alpaca_paper import AlpacaPaperAdapter
from software.integrations.alpaca_readonly import AlpacaReadOnlyProvider
from software.runtime.decision_memory import DecisionMemory, DecisionRecord
from software.runtime.paper_execution_controller import AuditLog, PaperExecutionController
from software.runtime.paper_risk import RiskGate
from software.runtime.position_ledger import OrderRecord, PositionLedger
from software.runtime.production_readiness import KillSwitch, PersistentState, ResourceBudget


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", default="AAPL")
    parser.add_argument("--qty", type=float, default=0.1)
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()

    observation = AlpacaReadOnlyProvider(symbol=args.symbol.upper()).observe()
    price = float(observation.payload["price"])
    ledger = PositionLedger()
    position = ledger.get_position(args.symbol)
    confidence = 0.75
    side = "buy"

    state = PersistentState()
    kill = KillSwitch()
    budget = ResourceBudget(max_cost=1.0, max_actions=1, max_experiments=10)
    gate = RiskGate(max_notional=1000.0, max_position_qty=10.0, min_confidence=0.70)
    risk = gate.check(qty=args.qty, price=price, side=side, confidence=confidence,
                      position_qty=position.qty, realized_pnl=position.realized_pnl,
                      state=state.load(), kill_switch=kill, budget=budget)

    print(f"LIVE {args.symbol.upper()} PRICE={price:.4f} DECISION={side.upper()} CONFIDENCE={confidence:.2f}")
    print(f"RISK approved={risk.approved} reason={risk.reason} notional={risk.notional:.2f}")
    if not risk.approved:
        return 2

    if not args.execute:
        print("EXECUTION=DISABLED (use --execute plus XYOOL_PAPER_EXECUTE=YES)")
        return 0
    if os.getenv("XYOOL_PAPER_EXECUTE") != "YES":
        print("EXECUTION=BLOCKED (set XYOOL_PAPER_EXECUTE=YES for paper execution)")
        return 3

    broker = AlpacaPaperAdapter()
    controller = PaperExecutionController(
        broker=broker, budget=budget, kill_switch=kill, state=state,
        audit=AuditLog(), execution_enabled=True, max_notional=gate.max_notional,
    )
    result = controller.execute_market_order(args.symbol, args.qty, side, price)
    ledger.record_order(OrderRecord(result.client_order_id, result.symbol, result.qty,
                                    result.side, result.estimated_notional,
                                    result.status, result.order.get("id")))
    DecisionMemory().record(DecisionRecord(result.client_order_id, "paper_baseline",
                                           result.side, confidence, 0.0, True))
    print(f"PAPER ORDER={result.client_order_id} STATUS={result.status} SIDE_EFFECTS=True")
    print(f"LEDGER={Path(ledger.path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
