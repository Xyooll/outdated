"""Offline self-build provider used before an LLM API is available.

It exercises the complete build contract with deterministic templates. When
an LLM provider is connected, it can be replaced without changing the agent.
"""
from __future__ import annotations

from .self_build_agent import BuildRequest
from .llm_self_build import GeneratedBundle


class OfflineGenerator:
    """Deterministic generator for integration testing of the self-builder."""

    def generate_bundle(self, request: BuildRequest, feedback: str = "") -> GeneratedBundle:
        source = (
            f'"""Generated capability: {request.goal}"""\n\n'
            "def run(value):\n"
            "    return value\n"
        )
        # The factory stages the candidate under request.name, so the generated
        # test must import that actual module rather than a hard-coded name.
        tests = (
            "import unittest\n"
            f"from {request.name} import run\n\n"
            "class GeneratedTests(unittest.TestCase):\n"
            "    def test_identity(self):\n"
            '        self.assertEqual(run("probe"), "probe")\n\n'
            "if __name__ == \"__main__\":\n"
            "    unittest.main()\n"
        )
        return GeneratedBundle(source, tests)
