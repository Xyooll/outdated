"""Run the autonomous LLM software-builder against the existing factory."""
from __future__ import annotations

from operation_dna.software.runtime.llm_self_build import AutonomousSelfBuildAgent, OpenAICompatibleGenerator
from operation_dna.software.runtime.self_build_agent import BuildRequest
from operation_dna.software.runtime.software_factory import SoftwareFactory


def main() -> int:
    request = BuildRequest(
        name="generated_signal",
        goal="Create a deterministic signal scorer from a numeric observation.",
        requirements=(
            "Expose score(value: float) -> float",
            "return a bounded score between 0 and 1",
            "include no network calls or side effects",
        ),
        destination="operation-dna/software/generated",
    )
    generator = OpenAICompatibleGenerator()
    agent = AutonomousSelfBuildAgent(SoftwareFactory(), generator)
    result = agent.build(request, promote=False)
    print(f"SELF_BUILD iteration={result.iteration}")
    print(f"SYNTAX={result.build.syntax_ok} TESTS={result.build.tests_ok}")
    print(f"PROMOTED={result.promoted}")
    print(f"REASON={result.build.reason[:500]}")
    for note in result.notes:
        print(f"NOTE={note}")
    return 0 if result.build.syntax_ok and result.build.tests_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
