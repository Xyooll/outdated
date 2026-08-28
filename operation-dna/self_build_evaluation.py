"""Evaluate the API-backed self-build repair loop and token efficiency.

Usage:
    python operation-dna/self_build_evaluation.py

The evaluation deliberately keeps promotion disabled. It measures each API
engineering operation and reports whether the candidate required repair.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from operation_dna.software.runtime.openai_provider import OpenAIProvider
from operation_dna.software.runtime.self_build_agent import BuildRequest, SelfBuildAgent, write_build_record
from operation_dna.software.runtime.software_factory import SoftwareFactory


@dataclass(frozen=True)
class Evaluation:
    name: str
    iteration: int
    syntax_ok: bool
    tests_ok: bool
    promoted: bool
    total_tokens: int
    repair_events: int


def main() -> None:
    ledger_path = "data/self_build_evaluation_tokens.jsonl"
    ledger = __import__("operation_dna.software.runtime.token_ledger", fromlist=["TokenLedger"]).TokenLedger(ledger_path)
    provider = OpenAIProvider(ledger=ledger)
    factory = SoftwareFactory(staging_root="operation-dna/.generated_evaluation")
    agent = SelfBuildAgent(factory, provider, max_iterations=3)

    request = BuildRequest(
        name="evaluation_probe",
        goal="build a deterministic Python capability that returns a short health report",
        requirements=(
            "no network calls in generated code",
            "deterministic output",
            "include generated tests",
        ),
    )

    result = agent.build(request, promote=False)
    write_build_record(result, "data/self_build_history.jsonl")
    summary = ledger.summary()
    operations = ledger.operation_summary()
    repair_events = operations.get("build.repair", {}).get("events", 0)
    evaluation = Evaluation(
        request.name,
        result.iteration,
        result.build.syntax_ok,
        result.build.tests_ok,
        result.promoted,
        summary["total_tokens"],
        repair_events,
    )

    print(f"EVALUATION name={evaluation.name} iteration={evaluation.iteration}")
    print(f"SUCCESS={evaluation.syntax_ok and evaluation.tests_ok} PROMOTED={evaluation.promoted}")
    print(f"REPAIRS={evaluation.repair_events}")
    print(f"TOKENS input={summary['input_tokens']} output={summary['output_tokens']} total={evaluation.total_tokens}")
    print(f"TOKENS_PER_SUCCESS={summary['tokens_per_success']:.1f}")
    print(f"OPERATIONS={operations}")
    print(f"LEDGER={ledger.path}")


if __name__ == "__main__":
    main()
