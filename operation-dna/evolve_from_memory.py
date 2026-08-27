"""Run the next-stage learning/evolution pass from durable decision memory."""
from __future__ import annotations

import argparse
import json

from software.runtime.decision_memory import DecisionMemory
from software.runtime.evolution_engine import candidate_payload, generate_candidates


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strategy", default="paper_baseline")
    parser.add_argument("--min-samples", type=int, default=10)
    args = parser.parse_args()
    memory = DecisionMemory()
    summary = memory.summary(args.strategy)
    candidates = generate_candidates(args.strategy, summary, args.min_samples)
    print(f"STRATEGY={args.strategy}")
    print(f"PERFORMANCE={json.dumps(summary, sort_keys=True)}")
    print(f"CANDIDATES={json.dumps(candidate_payload(candidates), sort_keys=True)}")
    print("AUTO_PROMOTE=False")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
