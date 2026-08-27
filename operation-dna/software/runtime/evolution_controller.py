"""Closed-loop strategy evolution: measure, diagnose, mutate, compete, and gate promotion."""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable

from .evolution_engine import StrategyCandidate, generate_candidates
from .strategy_engine import StrategyEngine


@dataclass(frozen=True)
class EvolutionRun:
    generation: int
    parent: str
    candidates: list[dict[str, Any]]
    winner: str | None
    promoted: bool
    reason: str


class EvolutionController:
    """Orchestrates bounded evolution without ever bypassing promotion authority."""

    def __init__(self, strategy_engine: StrategyEngine | None = None,
                 state_path: str = "data/learning/evolution.json"):
        self.engine = strategy_engine or StrategyEngine()
        self.state_path = Path(state_path)
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        self.generation = 0
        self.history: list[dict[str, Any]] = []
        self._load()

    def learn(self, strategy: str, pnl: float) -> None:
        self.engine.record(strategy, pnl)
        self._save()

    def diagnose(self, strategy: str, minimum_samples: int = 10) -> list[StrategyCandidate]:
        if strategy not in self.engine.stats:
            raise KeyError(strategy)
        return generate_candidates(strategy, self.engine.leaderboard_for(strategy), minimum_samples)

    def evolve(self, strategy: str, minimum_samples: int = 10,
               promote: bool = False,
               authority: Callable[[StrategyCandidate], bool] | None = None) -> EvolutionRun:
        candidates = self.diagnose(strategy, minimum_samples)
        self.generation += 1
        if not candidates:
            run = EvolutionRun(self.generation, strategy, [], None, False,
                               "insufficient evidence for mutation")
            self._record(run)
            return run

        # Candidate competition is deterministic until real evaluation is supplied.
        # Expected improvement is used only as a ranking prior, never as proof of fitness.
        winner = max(candidates, key=lambda c: (c.expected_improvement, c.candidate_id))
        promoted = False
        reason = "winner requires validation before promotion"
        if promote:
            if authority is None:
                reason = "promotion requires explicit authority"
            elif authority(winner):
                promoted = True
                reason = "explicit authority approved validated winner"
            else:
                reason = "authority denied promotion"
        run = EvolutionRun(self.generation, strategy, [asdict(c) for c in candidates],
                           winner.candidate_id, promoted, reason)
        self._record(run)
        return run

    def leaderboard(self) -> list[dict[str, Any]]:
        return self.engine.leaderboard()

    def _record(self, run: EvolutionRun) -> None:
        self.history.append(asdict(run))
        self._save()

    def _save(self) -> None:
        payload = {"generation": self.generation, "history": self.history}
        self.state_path.write_text(json.dumps(payload, sort_keys=True), encoding="utf-8")

    def _load(self) -> None:
        if self.state_path.exists():
            raw = json.loads(self.state_path.read_text(encoding="utf-8"))
            self.generation = int(raw.get("generation", 0))
            self.history = list(raw.get("history", []))


# Small compatibility helper keeps evolution logic independent of StrategyStats internals.
def _leaderboard_for(self: StrategyEngine, strategy: str) -> dict[str, Any]:
    s = self.stats[strategy]
    return {"samples": s.samples, "direction_accuracy": s.win_rate,
            "mean_pnl": s.mean_pnl, "total_pnl": s.total_pnl}


StrategyEngine.leaderboard_for = _leaderboard_for  # type: ignore[attr-defined]
