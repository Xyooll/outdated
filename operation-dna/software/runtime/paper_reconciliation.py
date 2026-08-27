"""Persistent broker-to-ledger reconciliation for paper trading."""
from __future__ import annotations

from typing import Any

from .paper_execution_controller import AuditLog
from .position_ledger import PositionLedger


def reconcile_positions(broker: Any, ledger: PositionLedger, audit: AuditLog | None = None) -> dict[str, Any]:
    audit = audit or AuditLog()
    remote_rows = broker._request("GET", "/v2/positions") or []
    remote = {str(row.get("symbol", "")).upper(): float(row.get("qty", 0)) for row in remote_rows}
    local = {symbol.upper(): float(position.qty) for symbol, position in ledger.positions.items() if position.qty}
    symbols = sorted(set(remote) | set(local))
    discrepancies = [{"symbol": symbol, "broker_qty": remote.get(symbol, 0.0), "ledger_qty": local.get(symbol, 0.0)}
                     for symbol in symbols if abs(remote.get(symbol, 0.0) - local.get(symbol, 0.0)) > 1e-9]
    audit.append("positions_reconciled", symbols=len(symbols), discrepancies=len(discrepancies))
    return {"symbols": len(symbols), "discrepancies": discrepancies, "in_sync": not discrepancies}
