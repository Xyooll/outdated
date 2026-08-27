"""Continuous paper loop: market -> risk -> paper execution -> reconciliation.

Default mode is observation-only. Paper order submission requires both --execute
and XYOOL_PAPER_EXECUTE=YES. No live endpoint is accepted by the broker adapter.
"""
from __future__ import annotations

import argparse
import os
import time

from software.integrations.alpaca_paper import AlpacaPaperAdapter
from software.integrations.alpaca_readonly import AlpacaReadOnlyProvider
from software.runtime.decision_memory import DecisionMemory, DecisionRecord
from software.runtime.paper_execution_controller import AuditLog, PaperExecutionController
from software.runtime.paper_reconciliation import reconcile_positions
from software.runtime.paper_risk import RiskGate
from software.runtime.position_ledger import OrderRecord, PositionLedger
from software.runtime.production_readiness import KillSwitch, PersistentState, ResourceBudget


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", default="AAPL")
    parser.add_argument("--qty", type=float, default=0.1)
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--cycles", type=int, default=1)
    parser.add_argument("--interval", type=float, default=5.0)
    args = parser.parse_args()
    if args.cycles < 1:
        raise SystemExit("--cycles must be >= 1")

    symbol = args.symbol.upper()
    market = AlpacaReadOnlyProvider(symbol=symbol)
    ledger = PositionLedger()
    state = PersistentState()
    kill = KillSwitch()
    budget = ResourceBudget(max_cost=1.0, max_actions=max(args.cycles, 1), max_experiments=100)
    gate = RiskGate(max_notional=1000.0, max_position_qty=10.0, min_confidence=0.70)
    audit = AuditLog()
    broker = AlpacaPaperAdapter() if args.execute else None
    controller = PaperExecutionController(broker=broker, budget=budget, kill_switch=kill,
                                          state=state, audit=audit, execution_enabled=args.execute,
                                          max_notional=gate.max_notional) if broker else None
    memory = DecisionMemory()

    for cycle in range(args.cycles):
        observation = market.observe()
        price = float(observation.payload["price"])
        position = ledger.get_position(symbol)
        side = "buy" if position.qty == 0 else "hold"
        confidence = 0.75
        print(f"CYCLE={cycle + 1} LIVE {symbol} PRICE={price:.4f} POSITION={position.qty:.4f} DECISION={side.upper()} CONFIDENCE={confidence:.2f}")

        if side == "buy":
            risk = gate.check(qty=args.qty, price=price, side="buy", confidence=confidence,
                              position_qty=position.qty, realized_pnl=position.realized_pnl,
                              state=state.load(), kill_switch=kill, budget=budget)
            print(f"RISK approved={risk.approved} reason={risk.reason} notional={risk.notional:.2f}")
            if risk.approved and controller and os.getenv("XYOOL_PAPER_EXECUTE") == "YES":
                result = controller.execute_market_order(symbol, args.qty, "buy", price)
                ledger.record_order(OrderRecord(result.client_order_id, symbol, args.qty, "buy",
                                                price, result.status, result.order.get("id")))
                memory.record(DecisionRecord(result.client_order_id, "paper_baseline", "buy", confidence, 0.0, True))
                print(f"PAPER ENTRY={result.client_order_id} STATUS={result.status}")
            else:
                print("EXECUTION=DISABLED")
        else:
            print("EXIT=WAITING_FOR_EXIT_ENGINE")

        if broker:
            reconciliation = reconcile_positions(broker, ledger, audit)
            print(f"RECONCILIATION in_sync={reconciliation['in_sync']} discrepancies={len(reconciliation['discrepancies'])}")
        if cycle + 1 < args.cycles:
            time.sleep(max(0.0, args.interval))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
