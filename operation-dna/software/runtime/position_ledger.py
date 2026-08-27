"""Persistent order and position state for the paper trading layer."""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


@dataclass
class OrderRecord:
    client_order_id: str
    symbol: str
    qty: float
    side: str
    reference_price: float
    status: str
    broker_order_id: str | None = None


@dataclass
class Position:
    symbol: str
    qty: float = 0.0
    average_price: float = 0.0
    realized_pnl: float = 0.0


class PositionLedger:
    """Small durable ledger; fills are applied explicitly and never inferred."""

    def __init__(self, path: str = "data/paper/ledger.json"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.orders: dict[str, OrderRecord] = {}
        self.positions: dict[str, Position] = {}
        self._load()

    def record_order(self, record: OrderRecord) -> None:
        self.orders[record.client_order_id] = record
        self._save()

    def get_position(self, symbol: str) -> Position:
        return self.positions.get(symbol.upper(), Position(symbol.upper()))

    def apply_fill(self, symbol: str, qty: float, side: str, price: float) -> Position:
        symbol = symbol.upper()
        if qty <= 0 or price <= 0 or side not in {"buy", "sell"}:
            raise ValueError("invalid fill")
        p = self.get_position(symbol)
        signed = qty if side == "buy" else -qty
        old_qty = p.qty
        new_qty = old_qty + signed
        if old_qty == 0 or (old_qty > 0 and signed > 0) or (old_qty < 0 and signed < 0):
            total_abs = abs(old_qty) + abs(signed)
            p.average_price = ((abs(old_qty) * p.average_price) + (abs(signed) * price)) / total_abs
        elif new_qty == 0:
            p.realized_pnl += abs(old_qty) * (price - p.average_price) * (1 if old_qty > 0 else -1)
            p.average_price = 0.0
        else:
            closed = min(abs(old_qty), abs(signed))
            p.realized_pnl += closed * (price - p.average_price) * (1 if old_qty > 0 else -1)
            if (old_qty > 0) != (new_qty > 0):
                p.average_price = price
        p.qty = new_qty
        self.positions[symbol] = p
        self._save()
        return p

    def snapshot(self) -> dict[str, Any]:
        return {"orders": {k: asdict(v) for k, v in self.orders.items()},
                "positions": {k: asdict(v) for k, v in self.positions.items()}}

    def _load(self) -> None:
        if not self.path.exists():
            return
        raw = json.loads(self.path.read_text(encoding="utf-8"))
        self.orders = {k: OrderRecord(**v) for k, v in raw.get("orders", {}).items()}
        self.positions = {k: Position(**v) for k, v in raw.get("positions", {}).items()}

    def _save(self) -> None:
        self.path.write_text(json.dumps(self.snapshot(), sort_keys=True), encoding="utf-8")
