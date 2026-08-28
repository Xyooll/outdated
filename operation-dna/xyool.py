"""Interactive Xyool agent shell.

Run from the repository root with:
    python operation-dna/xyool.py

The shell keeps a conversation in memory and routes engineering requests to
Xyool's API-backed self-build agent. Promotion remains behind authority.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from operation_dna.software.runtime.openai_provider import OpenAIProvider
from operation_dna.software.runtime.self_build_agent import BuildRequest, SelfBuildAgent, write_build_record
from operation_dna.software.runtime.software_factory import SoftwareFactory


def make_agent() -> tuple[SelfBuildAgent, OpenAIProvider]:
    provider = OpenAIProvider()
    factory = SoftwareFactory(staging_root=str(ROOT / ".generated_agent"))
    return SelfBuildAgent(factory, provider, max_iterations=3), provider


def main() -> None:
    agent, provider = make_agent()
    print("XYOOL interactive agent")
    print("Type an engineering objective, or :help, :tokens, :quit")
    print()

    while True:
        try:
            request_text = input("XYOOL> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if not request_text:
            continue
        if request_text in {":quit", ":exit", "quit", "exit"}:
            break
        if request_text == ":help":
            print("Give Xyool an engineering objective. :tokens shows API usage. :quit exits.")
            continue
        if request_text == ":tokens":
            print(provider.ledger.summary())
            print(provider.ledger.operation_summary())
            continue

        # The initial shell uses the objective itself as the build goal. The
        # API provider supplies the engineering intelligence and generated
        # tests; the local factory performs validation and repair.
        safe_name = "capability_" + str(abs(hash(request_text)))[:10]
        request = BuildRequest(
            name=safe_name,
            goal=request_text,
            requirements=(
                "fit the existing Operation DNA architecture",
                "include tests",
                "avoid destructive changes",
            ),
        )
        print("AGENT: building...")
        result = agent.build(request, promote=False)
        write_build_record(result)
        print(f"RESULT: iteration={result.iteration} syntax={result.build.syntax_ok} tests={result.build.tests_ok}")
        print(f"PROMOTED={result.promoted}")
        print(f"REASON={result.build.reason}")
        for note in result.notes:
            print(f"NOTE={note}")
        print(f"TOKENS={provider.ledger.summary()}")
        print()


if __name__ == "__main__":
    main()
