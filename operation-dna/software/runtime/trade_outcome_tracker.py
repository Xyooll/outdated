"""Persistent trade outcome accounting."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class TradeOutcomeTracker:
    def __init__(self, path: str = "data/paper/trade_outcomes.jsonl"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def record(self, *, client_order_id: str, symbol: str, side: str, qty: float,
               entry_price: float, exit_price: float, reason: str) -> dict[str, Any]:
        pnl = (exit_price - entry_price) * qty if side == "buy" else (entry_price - exit_price) * qty
        result = {"client_order_id": client_order_id, "symbol": symbol, "side": side, "qty": qty,
                  "entry_price": entry_price, "exit_price": exit_price, "pnl": pnl, "reason": reason}
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(result, sort_keys=True) + "\n")
        return result

    def summary(self) -> dict[str, float | int]:
        if not self.path.exists():
            return {"samples": 0, "wins": 0, "losses": 0, "total_pnl": 0.0}
        rows = [json.loads(line) for line in self.path.read_text(encoding="utf-8").splitlines() if line]
        pnl = [float(row["pnl"]) for row in rows]
        return {"samples": len(pnl), "wins": sum(value > 0 for value in pnl),
                "losses": sum(value < 0 for value in pnl), "total_pnl": sum(pnl)}
