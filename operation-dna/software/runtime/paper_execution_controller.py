"""Final risk and safety gate for paper trading."""
from __future__ import annotations

import json
import os
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Protocol

from ..integrations.alpaca_paper import AlpacaPaperAdapter, PaperAccount
from .production_readiness import KillSwitch, PersistentState, ResourceBudget


class PaperBroker(Protocol):
    def account(self) -> PaperAccount: ...
    def submit_market_order(self, symbol: str, qty: float, side: str, client_order_id: str | None = None) -> dict[str, Any]: ...


@dataclass(frozen=True)
class PaperExecutionResult:
    status: str
    client_order_id: str
    symbol: str
    qty: float
    side: str
    estimated_notional: float
    order: dict[str, Any]


class AuditLog:
    def __init__(self, path: str = "data/logs/paper_execution.jsonl"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, event_type: str, **data: Any) -> None:
        record = {"timestamp": datetime.now(timezone.utc).isoformat(), "event_type": event_type, **data}
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, default=str, sort_keys=True) + "\n")


class PaperExecutionController:
    """Authorize and submit one paper order through every runtime gate."""
    def __init__(self, broker: PaperBroker | None = None, budget: ResourceBudget | None = None,
                 kill_switch: KillSwitch | None = None, state: PersistentState | None = None,
                 audit: AuditLog | None = None, execution_enabled: bool = False,
                 max_notional: float = 100.0, execution_cost: float = 0.0):
        self.broker = broker or AlpacaPaperAdapter()
        self.budget = budget or ResourceBudget()
        self.kill_switch = kill_switch or KillSwitch()
        self.state = state or PersistentState()
        self.audit = audit or AuditLog()
        self.execution_enabled = execution_enabled
        self.max_notional = max_notional
        self.execution_cost = execution_cost

    def execute_market_order(self, symbol: str, qty: float, side: str, reference_price: float,
                             client_order_id: str | None = None) -> PaperExecutionResult:
        self.kill_switch.check()
        if self.state.load().paused:
            raise RuntimeError("runtime is paused")
        if not self.execution_enabled:
            raise RuntimeError("paper execution is disabled")
        if os.getenv("XYOOL_PAPER_EXECUTE") != "YES":
            raise RuntimeError("paper execution requires XYOOL_PAPER_EXECUTE=YES")

        symbol = symbol.strip().upper()
        if not symbol or "/" in symbol:
            raise ValueError("paper stock order symbol must be a stock ticker, e.g. AAPL")
        if qty <= 0:
            raise ValueError("qty must be > 0")
        if side not in {"buy", "sell"}:
            raise ValueError("side must be buy or sell")
        if reference_price <= 0:
            raise ValueError("reference_price must be > 0")

        estimated_notional = qty * reference_price
        if estimated_notional > self.max_notional:
            raise RuntimeError(f"estimated notional {estimated_notional:.2f} exceeds limit {self.max_notional:.2f}")

        account = self.broker.account()
        if account.status != "ACTIVE" or account.trading_blocked:
            raise RuntimeError("paper account is not eligible for trading")

        order_id = client_order_id or f"xyool-paper-{uuid.uuid4().hex[:20]}"
        self.budget.consume(cost=self.execution_cost, action=True)
        self.audit.append("paper_order_authorized", symbol=symbol, qty=qty, side=side,
                          reference_price=reference_price, estimated_notional=estimated_notional,
                          client_order_id=order_id, execution="paper")
        try:
            order = self.broker.submit_market_order(symbol, qty, side, order_id)
        except Exception as exc:
            self.audit.append("paper_order_failed", symbol=symbol, qty=qty, side=side,
                              client_order_id=order_id, execution="paper", error=type(exc).__name__)
            raise
        self.audit.append("paper_order_submitted", symbol=symbol, qty=qty, side=side,
                          client_order_id=order_id, execution="paper", order_id=order.get("id"),
                          order_status=order.get("status"))
        return PaperExecutionResult(str(order.get("status", "submitted")), order_id, symbol,
                                    qty, side, estimated_notional, order)
