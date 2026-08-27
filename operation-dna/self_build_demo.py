"""Deterministic demonstration of the self-building agent pipeline.

Run from the repository root:
    python operation-dna/self_build_demo.py
"""
from __future__ import annotations

from operation_dna.software.runtime.authority import HumanAuthority
from operation_dna.software.runtime.self_build_agent import BuildRequest, SelfBuildAgent, write_build_record
from operation_dna.software.runtime.software_factory import SoftwareFactory


def generator(request: BuildRequest, feedback: str) -> str:
    # This is deliberately deterministic. Replace this callable with the
    # project's LLM/code-generation adapter when one is connected.
    if not feedback:
        return "def generated_signal(price):\n    return price > 0\n"
    return "def generated_signal(price):\n    if price <= 0:\n        raise ValueError('price must be positive')\n    return True\n"


def main() -> int:
    authority = HumanAuthority()
    factory = SoftwareFactory()
    agent = SelfBuildAgent(factory, generator, max_iterations=2)
    request = BuildRequest(
        name="generated_signal",
        goal="Create a safe positive-price signal function",
    )
    result = agent.build(request)
    write_build_record(result)
    print(f"SELF_BUILD name={result.request.name} iteration={result.iteration}")
    print(f"SYNTAX={result.build.syntax_ok} TESTS={result.build.tests_ok} PROMOTED={result.promoted}")
    print(f"REASON={result.build.reason}")
    print("PROMOTION=BLOCKED until explicit authority approval")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
