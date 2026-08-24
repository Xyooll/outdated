"""Minimal deterministic backtesting primitives.

This is deliberately strategy-agnostic: strategies provide signals and the engine
measures outcomes. No live orders are supported here.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Bar:
    timestamp: str
    price: float


@dataclass(frozen=True)
class Trade:
    entry: float
    exit: float
    quantity: float

    @property
    def pnl(self) -> float:
        return (self.exit - self.entry) * self.quantity


@dataclass(frozen=True)
class BacktestResult:
    trades: tuple[Trade, ...]
    initial_capital: float

    @property
    def pnl(self) -> float:
        return sum(t.pnl for t in self.trades)

    @property
    def ending_capital(self) -> float:
        return self.initial_capital + self.pnl

    @property
    def return_pct(self) -> float:
        return self.pnl / self.initial_capital if self.initial_capital > 0 else 0.0


def buy_and_hold(bars: list[Bar], initial_capital: float) -> BacktestResult:
    if len(bars) < 2 or initial_capital <= 0:
        return BacktestResult((), initial_capital)
    qty = initial_capital / bars[0].price
    return BacktestResult((Trade(bars[0].price, bars[-1].price, qty),), initial_capital)
