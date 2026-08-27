"""Explicit portfolio/risk gate layered above paper execution."""
from __future__ import annotations

from dataclasses import dataclass

from .production_readiness import KillSwitch, ResourceBudget, RuntimeState


@dataclass(frozen=True)
class RiskDecision:
    approved: bool
    reason: str
    notional: float


class RiskGate:
    """Deterministic pre-trade gate. It never submits orders itself."""

    def __init__(self, max_notional: float = 100.0, max_position_qty: float = 10.0,
                 max_daily_loss: float = 100.0, min_confidence: float = 0.70):
        self.max_notional = max_notional
        self.max_position_qty = max_position_qty
        self.max_daily_loss = max_daily_loss
        self.min_confidence = min_confidence

    def check(self, *, qty: float, price: float, side: str, confidence: float,
              position_qty: float = 0.0, realized_pnl: float = 0.0,
              state: RuntimeState | None = None, kill_switch: KillSwitch | None = None,
              budget: ResourceBudget | None = None) -> RiskDecision:
        if kill_switch is not None:
            kill_switch.check()
        if state is not None and state.paused:
            return RiskDecision(False, "runtime is paused", 0.0)
        if qty <= 0 or price <= 0:
            return RiskDecision(False, "qty and price must be positive", 0.0)
        if side not in {"buy", "sell"}:
            return RiskDecision(False, "side must be buy or sell", 0.0)
        if confidence < self.min_confidence:
            return RiskDecision(False, "confidence below risk threshold", qty * price)
        notional = qty * price
        if notional > self.max_notional:
            return RiskDecision(False, "notional exceeds risk limit", notional)
        projected = position_qty + (qty if side == "buy" else -qty)
        if abs(projected) > self.max_position_qty:
            return RiskDecision(False, "position limit exceeded", notional)
        if realized_pnl < -abs(self.max_daily_loss):
            return RiskDecision(False, "daily loss limit exceeded", notional)
        if budget is not None and not budget.allow_cost(0.0):
            return RiskDecision(False, "resource budget unavailable", notional)
        return RiskDecision(True, "risk checks passed", notional)
