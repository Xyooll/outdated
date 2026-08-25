"""Synthetic market for safe strategy evaluation. No real market/network access."""
from dataclasses import dataclass
import random
from typing import Callable

@dataclass(frozen=True)
class MarketTick:
    price: float
    return_pct: float
    volatility: float

@dataclass(frozen=True)
class StrategyResult:
    final_cash: float
    return_pct: float
    max_drawdown_pct: float
    trades: int

class SyntheticMarket:
    def __init__(self, seed: int = 42, start_price: float = 100.0):
        self.rng = random.Random(seed)
        self.price = start_price
        self.peak_equity = 100.0

    def ticks(self, count: int = 1000):
        previous = self.price
        for _ in range(count):
            shock = self.rng.gauss(0.0002, 0.01)
            self.price = max(0.01, self.price * (1.0 + shock))
            yield MarketTick(self.price, (self.price / previous - 1.0) * 100.0, abs(shock))
            previous = self.price


def run_strategy(strategy: Callable[[list[MarketTick]], int], seed: int = 42, ticks: int = 1000) -> StrategyResult:
    """Run a long/flat strategy: action 1=long, 0=flat. No leverage or shorting."""
    market = SyntheticMarket(seed)
    cash, position, trades = 100.0, 0.0, 0
    equity = cash
    peak = equity
    max_dd = 0.0
    history: list[MarketTick] = []
    for tick in market.ticks(ticks):
        history.append(tick)
        action = 1 if strategy(history) else 0
        if action and position == 0.0:
            position = cash / tick.price
            cash = 0.0
            trades += 1
        elif not action and position > 0.0:
            cash = position * tick.price
            position = 0.0
            trades += 1
        equity = cash + position * tick.price
        peak = max(peak, equity)
        max_dd = max(max_dd, (peak - equity) / peak * 100.0)
    if position:
        cash = position * market.price
    return StrategyResult(cash, (cash / 100.0 - 1.0) * 100.0, max_dd, trades)


def momentum_baseline(history: list[MarketTick]) -> int:
    return 1 if len(history) >= 5 and history[-1].price > history[-5].price else 0
