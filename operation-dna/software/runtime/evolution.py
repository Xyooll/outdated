"""Controlled self-improvement: compare candidates against a baseline."""
from dataclasses import dataclass
from typing import Callable, Any

@dataclass(frozen=True)
class Candidate:
    name: str
    version: str
    score: float
    artifact: Any

@dataclass(frozen=True)
class PromotionDecision:
    candidate: str
    promote: bool
    reason: str

def compare(baseline: Candidate, candidate: Candidate, minimum_gain: float = 0.0) -> PromotionDecision:
    gain = candidate.score - baseline.score
    if gain > minimum_gain:
        return PromotionDecision(candidate.name, True, f"gain={gain:.6f}")
    return PromotionDecision(candidate.name, False, f"insufficient gain={gain:.6f}")
