"""Continuous paper loop with execution lifecycle, reconciliation, exits and learning.

Paper-only. Execution requires --execute and XYOOL_PAPER_EXECUTE=YES.
"""
from __future__ import annotations
import argparse, os, time
from software.integrations.alpaca_paper import AlpacaPaperAdapter
from software.integrations.alpaca_readonly import AlpacaReadOnlyProvider
from software.runtime.decision_memory import DecisionMemory, DecisionRecord
from software.runtime.paper_execution_controller import AuditLog, PaperExecutionController
from software.runtime.paper_reconciliation import reconcile_positions
from software.runtime.paper_risk import RiskGate
from software.runtime.position_ledger import OrderRecord, PositionLedger
from software.runtime.production_readiness import KillSwitch, PersistentState, ResourceBudget
from software.runtime.trade_outcomes import OutcomeStore

STRATEGIES = {
    "baseline": {"confidence": 0.75, "take_profit": 0.01, "stop_loss": 0.01},
    "fast": {"confidence": 0.80, "take_profit": 0.005, "stop_loss": 0.0075},
    "patient": {"confidence": 0.72, "take_profit": 0.02, "stop_loss": 0.015},
}
TERMINAL = {"filled", "canceled", "cancelled", "rejected", "expired"}


def refresh_broker_state(broker, ledger, audit):
    """Synchronize local order/position state from Alpaca.

    Broker state is authoritative. For each local non-terminal order we first
    use the order history returned by Alpaca; when an order is outside that
    result set, we query it directly by broker order id. This prevents stale
    local 'accepted' entries from permanently blocking new decisions.
    """
    try:
        remote_orders = broker.get_orders(status="all", limit=100)
        by_client = {str(o.get("client_order_id")): o for o in remote_orders if o.get("client_order_id")}
        by_id = {str(o.get("id")): o for o in remote_orders if o.get("id")}
        for record in list(ledger.orders.values()):
            if record.status.lower() in TERMINAL:
                continue
            remote = by_client.get(record.client_order_id)
            if remote is None and record.broker_order_id:
                remote = by_id.get(str(record.broker_order_id))
            if remote is None and record.broker_order_id:
                try:
                    remote = broker.get_order(str(record.broker_order_id))
                except Exception:
                    remote = None
            if remote:
                ledger.update_order_status(
                    record.client_order_id,
                    str(remote.get("status", record.status)).lower(),
                )
            else:
                # A local order without a broker record is not actionable.
                # Mark it canceled so stale local state cannot block the loop.
                ledger.update_order_status(record.client_order_id, "canceled")
                audit.append(
                    "stale_local_order_closed",
                    client_order_id=record.client_order_id,
                    execution="paper",
                )
    except Exception as exc:
        audit.append("order_history_refresh_failed", error=type(exc).__name__, execution="paper")

    remote_positions = broker.get_positions()
    ledger.sync_positions(remote_positions)
    return reconcile_positions(broker, ledger, audit)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", default="AAPL")
    parser.add_argument("--qty", type=float, default=0.1)
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--cycles", type=int, default=1)
    parser.add_argument("--interval", type=float, default=5.0)
    parser.add_argument("--strategies", default="baseline")
    args = parser.parse_args()
    if args.cycles < 1:
        raise SystemExit("--cycles must be >= 1")
    symbol = args.symbol.upper()
    selected = [x.strip().lower() for x in args.strategies.split(",") if x.strip()]
    unknown = [x for x in selected if x not in STRATEGIES]
    if unknown:
        raise SystemExit(f"unknown strategies: {', '.join(unknown)}")

    market = AlpacaReadOnlyProvider(symbol=symbol)
    ledger = PositionLedger()
    state = PersistentState()
    kill = KillSwitch()
    budget = ResourceBudget(max_cost=1.0, max_actions=max(args.cycles * len(selected), 1), max_experiments=100)
    gate = RiskGate(max_notional=1000.0, max_position_qty=10.0, min_confidence=0.70)
    audit = AuditLog()
    memory = DecisionMemory()
    outcomes = OutcomeStore()
    broker = AlpacaPaperAdapter() if args.execute else None
    controller = PaperExecutionController(
        broker=broker, budget=budget, kill_switch=kill, state=state, audit=audit,
        execution_enabled=args.execute, max_notional=gate.max_notional,
    ) if broker else None

    for cycle in range(args.cycles):
        observation = market.observe()
        price = float(observation.payload["price"])
        if broker:
            reconciliation = refresh_broker_state(broker, ledger, audit)
        else:
            reconciliation = None
        position = ledger.get_position(symbol)
        open_entry = ledger.has_pending_entry(symbol)
        strategy = selected[cycle % len(selected)]
        config = STRATEGIES[strategy]
        confidence = config["confidence"]
        exit_signal = False
        if position.qty > 0 and position.average_price > 0:
            move = (price - position.average_price) / position.average_price
            exit_signal = move >= config["take_profit"] or move <= -config["stop_loss"]
        side = "sell" if exit_signal else ("hold" if position.qty > 0 or open_entry else "buy")
        print(f"CYCLE={cycle + 1} LIVE {symbol} PRICE={price:.4f} POSITION={position.qty:.4f} DECISION={side.upper()} STRATEGY={strategy} CONFIDENCE={confidence:.2f}")

        if side == "buy":
            risk = gate.check(qty=args.qty, price=price, side="buy", confidence=confidence,
                              position_qty=position.qty, realized_pnl=position.realized_pnl,
                              state=state.load(), kill_switch=kill, budget=budget)
            print(f"RISK approved={risk.approved} reason={risk.reason} notional={risk.notional:.2f}")
            if risk.approved and controller and os.getenv("XYOOL_PAPER_EXECUTE") == "YES":
                result = controller.execute_market_order(symbol, args.qty, "buy", price)
                ledger.record_order(OrderRecord(result.client_order_id, symbol, args.qty, "buy", price,
                                                result.status, result.order.get("id")))
                print(f"PAPER ENTRY={result.client_order_id} STATUS={result.status}")
            else:
                print("EXECUTION=DISABLED")
        elif side == "sell":
            qty = position.qty
            if controller and qty > 0 and os.getenv("XYOOL_PAPER_EXECUTE") == "YES":
                result = controller.execute_market_order(symbol, qty, "sell", price)
                ledger.record_order(OrderRecord(result.client_order_id, symbol, qty, "sell", price,
                                                result.status, result.order.get("id")))
                status = result.status.lower()
                if result.order.get("id") and status not in TERMINAL:
                    try:
                        refreshed = broker.get_order(str(result.order["id"]))
                        status = str(refreshed.get("status", status)).lower()
                        ledger.update_order_status(result.client_order_id, status)
                    except Exception:
                        pass
                if status == "filled":
                    pnl = (price - position.average_price) * qty
                    outcomes.close(result.client_order_id, symbol, "buy", qty,
                                   position.average_price, price, "paper-loop")
                    memory.record(DecisionRecord(result.client_order_id, strategy, "sell",
                                                  confidence, pnl, pnl > 0))
                    print(f"PAPER EXIT={result.client_order_id} STATUS=filled PNL={pnl:.4f}")
                else:
                    print(f"PAPER EXIT={result.client_order_id} STATUS={status} OUTCOME=PENDING")
            else:
                print("EXIT=READY EXECUTION=DISABLED")
        else:
            print("EXIT=WAITING")

        if broker:
            reconciliation = refresh_broker_state(broker, ledger, audit)
            print(f"RECONCILIATION in_sync={reconciliation['in_sync']} discrepancies={len(reconciliation['discrepancies'])}")
        if cycle + 1 < args.cycles:
            time.sleep(max(0.0, args.interval))

    print(f"LEARNING={memory.summary()} OUTCOMES={outcomes.summary()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
