"""Durable trade outcome tracking."""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path


@dataclass(frozen=True)
class TradeOutcome:
    trade_id: str
    symbol: str
    side: str
    qty: float
    entry_price: float
    exit_price: float
    pnl: float
    return_pct: float
    opened_at: str
    closed_at: str


class OutcomeStore:
    def __init__(self, path: str = "data/paper/outcomes.json"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.records: list[TradeOutcome] = []
        self._load()

    def close(self, trade_id: str, symbol: str, side: str, qty: float,
              entry_price: float, exit_price: float, opened_at: str,
              closed_at: str | None = None) -> TradeOutcome:
        if qty <= 0 or entry_price <= 0 or exit_price <= 0:
            raise ValueError("trade values must be positive")
        if side not in {"buy", "sell"}:
            raise ValueError("side must be buy or sell")
        pnl = (exit_price - entry_price) * qty * (1 if side == "buy" else -1)
        result = TradeOutcome(
            trade_id, symbol.upper(), side, qty, entry_price, exit_price, pnl,
            pnl / (entry_price * qty), opened_at,
            closed_at or datetime.now(timezone.utc).isoformat(),
        )
        self.records.append(result)
        self._save()
        return result

    def summary(self) -> dict:
        if not self.records:
            return {"samples": 0, "wins": 0, "losses": 0, "win_rate": 0.0,
                    "total_pnl": 0.0, "mean_pnl": 0.0}
        wins = sum(r.pnl > 0 for r in self.records)
        total = sum(r.pnl for r in self.records)
        return {"samples": len(self.records), "wins": wins,
                "losses": len(self.records) - wins,
                "win_rate": wins / len(self.records), "total_pnl": total,
                "mean_pnl": total / len(self.records)}

    def _load(self) -> None:
        if self.path.exists():
            self.records = [TradeOutcome(**r) for r in json.loads(self.path.read_text(encoding="utf-8"))]

    def _save(self) -> None:
        self.path.write_text(json.dumps([asdict(r) for r in self.records], sort_keys=True), encoding="utf-8")
