"""Explicitly opt-in API-backed self-build demonstration.

Usage from repository root:
    python operation-dna/self_build_api_demo.py

This generates a candidate and tests it, but does not promote it.
"""
from __future__ import annotations

from operation_dna.software.runtime.openai_provider import OpenAIProvider
from operation_dna.software.runtime.self_build_agent import BuildRequest, SelfBuildAgent
from operation_dna.software.runtime.software_factory import SoftwareFactory


def main() -> None:
    provider = OpenAIProvider()
    factory = SoftwareFactory(root="operation-dna/.generated_api")
    agent = SelfBuildAgent(factory, provider, max_iterations=2)
    request = BuildRequest(
        name="api_probe",
        goal="build a deterministic capability that returns a short health report",
        requirements=("no network calls in generated code", "deterministic output",),
    )
    result = agent.build(request, promote=False)
    summary = provider.ledger.summary()
    print(f"API_BUILD iteration={result.iteration} syntax={result.build.syntax_ok} tests={result.build.tests_ok}")
    print(f"PROMOTED={result.promoted} REASON={result.build.reason}")
    print(f"TOKENS input={summary['input_tokens']} output={summary['output_tokens']} total={summary['total_tokens']} measured_events={summary['measured_events']}")
    print(f"LEDGER={provider.ledger.path}")


if __name__ == "__main__":
    main()
