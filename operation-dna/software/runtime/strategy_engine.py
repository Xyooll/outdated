"""Multi-strategy evaluation and paper performance tracking."""
from __future__ import annotations

from dataclasses import dataclass

from .market_features import MarketFeatures
from .signal_engine import Signal, SignalEngine


@dataclass(frozen=True)
class StrategyResult:
    strategy: str
    signal: Signal


@dataclass
class StrategyStats:
    samples: int = 0
    wins: int = 0
    total_pnl: float = 0.0
    max_drawdown: float = 0.0
    equity_peak: float = 0.0
    equity: float = 0.0

    @property
    def win_rate(self) -> float:
        return self.wins / self.samples if self.samples else 0.0

    @property
    def mean_pnl(self) -> float:
        return self.total_pnl / self.samples if self.samples else 0.0


class StrategyEngine:
    """Runs multiple strategies against identical observations and ranks them."""

    def __init__(self, strategies: dict[str, SignalEngine] | None = None):
        self.strategies = strategies or {
            "baseline": SignalEngine(0.35, 0.30),
            "fast": SignalEngine(0.25, 0.20),
            "patient": SignalEngine(0.45, 0.35),
            "momentum": SignalEngine(0.40, 0.30),
            "mean_reversion": SignalEngine(0.50, 0.45),
        }
        self.stats = {name: StrategyStats() for name in self.strategies}

    def evaluate(self, features: MarketFeatures, position_qty: float = 0.0) -> list[StrategyResult]:
        results = [StrategyResult(name, engine.evaluate(features, position_qty))
                   for name, engine in self.strategies.items()]
        return sorted(results, key=lambda r: (-r.signal.confidence, r.strategy))

    def record(self, strategy: str, pnl: float) -> None:
        if strategy not in self.stats:
            raise KeyError(strategy)
        s = self.stats[strategy]
        s.samples += 1
        s.total_pnl += float(pnl)
        s.equity += float(pnl)
        s.equity_peak = max(s.equity_peak, s.equity)
        s.max_drawdown = max(s.max_drawdown, s.equity_peak - s.equity)
        if pnl > 0:
            s.wins += 1

    def leaderboard_for(self, strategy: str) -> dict:
        if strategy not in self.stats:
            raise KeyError(strategy)
        s = self.stats[strategy]
        return {
            "samples": s.samples,
            "direction_accuracy": s.win_rate,
            "mean_pnl": s.mean_pnl,
            "total_pnl": s.total_pnl,
        }

    def leaderboard(self) -> list[dict]:
        rows = []
        for name, s in self.stats.items():
            score = s.mean_pnl + (s.win_rate * 0.01) - (s.max_drawdown * 0.001)
            rows.append({"strategy": name, "samples": s.samples,
                         "win_rate": round(s.win_rate, 4),
                         "mean_pnl": round(s.mean_pnl, 6),
                         "total_pnl": round(s.total_pnl, 6),
                         "max_drawdown": round(s.max_drawdown, 6),
                         "score": round(score, 6)})
        return sorted(rows, key=lambda r: (-r["score"], r["strategy"]))
