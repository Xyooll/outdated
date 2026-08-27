"""Bounded candidate generation. Candidates never auto-promote."""
from __future__ import annotations

import hashlib
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class StrategyCandidate:
    candidate_id: str
    strategy: str
    change: str
    expected_improvement: float
    requires_validation: bool = True


def generate_candidates(strategy: str, baseline: dict, minimum_samples: int = 10) -> list[StrategyCandidate]:
    samples = int(baseline.get("samples", 0))
    if samples < minimum_samples:
        return []

    accuracy = float(baseline.get("direction_accuracy", 0.0))
    mean_pnl = float(baseline.get("mean_pnl", 0.0))
    ideas: list[str] = []

    # Evolution should not stall merely because performance is mediocre.
    # The diagnosis determines the mutation family from observed evidence.
    if accuracy < 0.55:
        ideas.append("raise confluence threshold and reduce weak-signal entries")
    elif accuracy < 0.65:
        ideas.append("test a stricter confirmation filter and compare false-entry reduction")
    else:
        ideas.append("test a small confidence-weighted position-sizing increase")

    if mean_pnl <= 0:
        ideas.append("tighten loss control before increasing position size")
    elif mean_pnl < 0.10:
        ideas.append("test earlier profit-taking and compare expectancy")
    else:
        ideas.append("test adaptive exit timing to improve realized expectancy")

    return [
        StrategyCandidate(
            candidate_id=hashlib.sha256(f"{strategy}|{idea}".encode()).hexdigest()[:16],
            strategy=strategy,
            change=idea,
            expected_improvement=round(
                max(0.01, (0.65 - accuracy) * 0.1 if accuracy < 0.65 else 0.02), 4
            ),
        )
        for idea in ideas
    ]


def candidate_payload(candidates: list[StrategyCandidate]) -> list[dict]:
    return [asdict(c) for c in candidates]
