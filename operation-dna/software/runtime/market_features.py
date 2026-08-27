"""Deterministic market feature extraction for live and historical observations."""
from __future__ import annotations

from dataclasses import dataclass
from statistics import mean, pstdev


@dataclass(frozen=True)
class MarketFeatures:
    price: float
    return_1: float
    return_3: float
    return_5: float
    volatility_5: float
    trend: float
    spread: float = 0.0
    volume: float = 0.0


class FeatureEngine:
    """Build features from a rolling price window without external dependencies."""

    def __init__(self, window: int = 20):
        if window < 6:
            raise ValueError("window must be >= 6")
        self.window = window
        self.prices: list[float] = []
        self.spreads: list[float] = []
        self.volumes: list[float] = []

    def update(self, price: float, bid: float | None = None, ask: float | None = None,
               volume: float = 0.0) -> MarketFeatures:
        price = float(price)
        if price <= 0:
            raise ValueError("price must be > 0")
        self.prices.append(price)
        self.volumes.append(float(volume))
        if bid is not None and ask is not None:
            spread = max(0.0, float(ask) - float(bid))
        else:
            spread = 0.0
        self.spreads.append(spread)
        self.prices = self.prices[-self.window:]
        self.spreads = self.spreads[-self.window:]
        self.volumes = self.volumes[-self.window:]

        def ret(n: int) -> float:
            if len(self.prices) <= n:
                return 0.0
            return (price - self.prices[-n - 1]) / self.prices[-n - 1]

        returns = [
            (self.prices[i] - self.prices[i - 1]) / self.prices[i - 1]
            for i in range(1, len(self.prices))
        ]
        recent = self.prices[-5:]
        trend = ((mean(recent) - mean(self.prices)) / mean(self.prices)) if len(self.prices) >= 5 else 0.0
        return MarketFeatures(
            price=price,
            return_1=ret(1),
            return_3=ret(3),
            return_5=ret(5),
            volatility_5=pstdev(returns[-5:]) if len(returns) >= 2 else 0.0,
            trend=trend,
            spread=spread,
            volume=float(volume),
        )
