"""Demonstrate the bounded strategy evolution loop."""
from __future__ import annotations

from operation_dna.software.runtime.evolution_controller import EvolutionController


def main() -> int:
    controller = EvolutionController(state_path="data/learning/evolution_demo.json")
    for pnl in [0.40, -0.10, 0.30, -0.05, 0.25, 0.20, -0.10, 0.35, -0.05, 0.30]:
        controller.learn("baseline", pnl)

    run = controller.evolve("baseline", minimum_samples=10)
    print(f"EVOLUTION generation={run.generation} parent={run.parent}")
    print(f"CANDIDATES={len(run.candidates)} WINNER={run.winner}")
    print(f"PROMOTED={run.promoted} REASON={run.reason}")
    print(f"LEADERBOARD={controller.leaderboard()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
