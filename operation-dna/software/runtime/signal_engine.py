"""Explainable trading signals derived from market features."""
from __future__ import annotations

from dataclasses import dataclass

from .market_features import MarketFeatures


@dataclass(frozen=True)
class Signal:
    action: str
    confidence: float
    score: float
    reason: str


class SignalEngine:
    """Convert normalized features into bounded BUY/SELL/HOLD signals."""

    def __init__(self, entry_threshold: float = 0.35, exit_threshold: float = 0.30):
        self.entry_threshold = entry_threshold
        self.exit_threshold = exit_threshold

    def evaluate(self, features: MarketFeatures, position_qty: float = 0.0) -> Signal:
        score = 0.0
        reasons: list[str] = []

        if features.return_3 > 0:
            score += 0.30
            reasons.append("positive_3_step_momentum")
        elif features.return_3 < 0:
            score -= 0.30
            reasons.append("negative_3_step_momentum")

        if features.return_5 > 0:
            score += 0.25
            reasons.append("positive_5_step_momentum")
        elif features.return_5 < 0:
            score -= 0.25
            reasons.append("negative_5_step_momentum")

        if features.trend > 0:
            score += 0.20
            reasons.append("short_trend_above_baseline")
        elif features.trend < 0:
            score -= 0.20
            reasons.append("short_trend_below_baseline")

        # Excessive volatility reduces conviction rather than forcing a direction.
        if features.volatility_5 > 0.01:
            score *= 0.75
            reasons.append("volatility_penalty")

        if position_qty > 0 and score <= -self.exit_threshold:
            action = "sell"
        elif position_qty <= 0 and score >= self.entry_threshold:
            action = "buy"
        else:
            action = "hold"

        confidence = min(0.99, max(0.50, 0.50 + abs(score) * 0.45))
        return Signal(action, round(confidence, 4), round(score, 4), ";".join(reasons) or "no_directional_signal")
