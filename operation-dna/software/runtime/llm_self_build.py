"""LLM-backed autonomous software builder.

The model may generate and repair code and tests. The factory remains the
validation boundary and HumanAuthority remains the promotion boundary.
"""
from __future__ import annotations

import json
import os
import re
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

from .self_build_agent import BuildRequest, AgentBuildResult
from .software_factory import SoftwareFactory, BuildResult


@dataclass(frozen=True)
class GeneratedBundle:
    source: str
    tests: str


class OpenAICompatibleGenerator:
    """Small dependency-free client for OpenAI-compatible chat APIs.

    Configure OPENAI_API_KEY, OPENAI_MODEL, and optionally OPENAI_BASE_URL.
    The default base URL is the OpenAI API. No credentials are logged.
    """

    def __init__(self, api_key: str | None = None, model: str | None = None,
                 base_url: str | None = None, timeout: int = 120,
                 transport: Callable[..., Any] | None = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model or os.getenv("OPENAI_MODEL")
        self.base_url = (base_url or os.getenv("OPENAI_BASE_URL") or "https://api.openai.com/v1").rstrip("/")
        self.timeout = timeout
        self.transport = transport
        if not self.api_key:
            raise RuntimeError("OPENAI_API_KEY is required for LLM self-build")
        if not self.model:
            raise RuntimeError("OPENAI_MODEL is required for LLM self-build")

    def _request(self, messages: list[dict[str, str]]) -> str:
        payload = json.dumps({
            "model": self.model,
            "messages": messages,
            "temperature": 0.2,
        }).encode("utf-8")
        request = urllib.request.Request(
            f"{self.base_url}/chat/completions",
            data=payload,
            headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"},
            method="POST",
        )
        if self.transport:
            response = self.transport(request, self.timeout)
        else:
            response = urllib.request.urlopen(request, timeout=self.timeout)
        raw = response.read() if hasattr(response, "read") else response
        data = json.loads(raw.decode("utf-8") if isinstance(raw, bytes) else raw)
        try:
            return str(data["choices"][0]["message"]["content"])
        except (KeyError, IndexError, TypeError) as exc:
            raise RuntimeError("LLM response did not contain chat completion content") from exc

    def generate_bundle(self, request: BuildRequest, feedback: str = "") -> GeneratedBundle:
        prompt = (
            "Build a production-quality Python candidate for Operation DNA. "
            "Return ONLY a JSON object with keys source and tests. source is one complete Python module. "
            "tests is a complete unittest module that imports the candidate by module name. "
            "The candidate must be deterministic, dependency-light, and never execute external side effects. "
            "Requirements: " + "; ".join(request.requirements) + "\n"
            "Goal: " + request.goal + "\n"
            "Previous validation feedback: " + (feedback or "none")
        )
        content = self._request([
            {"role": "system", "content": "You are the software-building component of an autonomous engineering agent. Write code, tests, and repair failures. Never include secrets."},
            {"role": "user", "content": prompt},
        ])
        return self._parse_bundle(content)

    @staticmethod
    def _parse_bundle(content: str) -> GeneratedBundle:
        text = content.strip()
        if text.startswith("```"):
            text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.S).strip()
        try:
            data = json.loads(text)
            return GeneratedBundle(str(data["source"]), str(data["tests"]))
        except (json.JSONDecodeError, KeyError, TypeError) as exc:
            raise RuntimeError("LLM must return JSON with source and tests") from exc


class AutonomousSelfBuildAgent:
    """Let the model build, test, repair, and prepare a candidate autonomously."""

    def __init__(self, factory: SoftwareFactory, generator: OpenAICompatibleGenerator,
                 max_iterations: int = 5):
        if max_iterations < 1:
            raise ValueError("max_iterations must be >= 1")
        self.factory = factory
        self.generator = generator
        self.max_iterations = max_iterations

    def build(self, request: BuildRequest, *, promote: bool = False,
              autonomy_level: int = 0) -> AgentBuildResult:
        feedback = ""
        last: BuildResult | None = None
        notes: list[str] = []
        test_path = Path(self.factory.root) / f"{request.name}_generated_tests.py"

        for iteration in range(1, self.max_iterations + 1):
            bundle = self.generator.generate_bundle(request, feedback)
            source_path = self.factory.stage(request.name, bundle.source)
            test_path.write_text(bundle.tests, encoding="utf-8")
            last = self.factory.run_tests(source_path, str(test_path))
            if last.syntax_ok and last.tests_ok:
                notes.append("LLM candidate passed syntax and generated tests")
                promoted = False
                if promote:
                    try:
                        destination = self.factory.promote(last, request.destination, autonomy_level=autonomy_level)
                        promoted = True
                        notes.append(f"promoted to {destination}")
                    except PermissionError as exc:
                        notes.append(f"promotion blocked: {exc}")
                return AgentBuildResult(request, last, iteration, promoted, tuple(notes))
            feedback = last.reason
            notes.append(f"LLM repair iteration {iteration}: {last.reason[:500]}")

        assert last is not None
        return AgentBuildResult(request, last, self.max_iterations, False, tuple(notes))
