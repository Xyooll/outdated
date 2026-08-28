"""OpenAI API provider for the Xyool self-build agent.

The provider is deliberately narrow: it generates a build bundle and records
provider-reported token usage in the existing token ledger. It never promotes
software and never logs credentials.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Any

import requests

from .token_ledger import TokenLedger, TokenUsage


DEFAULT_BASE_URL = "https://api.openai.com/v1"
DEFAULT_MODEL = "gpt-5.6-luna"


@dataclass(frozen=True)
class OpenAIBuildBundle:
    source: str
    tests: str
    usage: TokenUsage
    response_id: str = ""


class OpenAIProvider:
    """Small, metered Responses API client used by the self-build pipeline."""

    def __init__(self, api_key: str | None = None, *, model: str | None = None,
                 base_url: str = DEFAULT_BASE_URL,
                 ledger: TokenLedger | None = None,
                 session: requests.Session | None = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise RuntimeError("OPENAI_API_KEY is required")
        self.model = model or os.getenv("XYOOL_OPENAI_MODEL", DEFAULT_MODEL)
        self.base_url = base_url.rstrip("/")
        self.ledger = ledger or TokenLedger()
        self.session = session or requests.Session()

    @property
    def headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def _request(self, prompt: str, operation: str) -> tuple[dict[str, Any], TokenUsage]:
        payload = {
            "model": self.model,
            "input": prompt,
        }
        response = self.session.post(
            f"{self.base_url}/responses",
            headers=self.headers,
            json=payload,
            timeout=120,
        )
        response.raise_for_status()
        data = response.json()
        usage = data.get("usage") or {}
        token_usage = TokenUsage(
            int(usage.get("input_tokens", 0)),
            int(usage.get("output_tokens", 0)),
            True,
        )
        return data, token_usage

    @staticmethod
    def _text(data: dict[str, Any]) -> str:
        if isinstance(data.get("output_text"), str):
            return data["output_text"]
        parts: list[str] = []
        for item in data.get("output", []):
            for content in item.get("content", []):
                text = content.get("text")
                if isinstance(text, str):
                    parts.append(text)
        return "\n".join(parts)

    def generate_bundle(self, request: Any, feedback: str = "") -> OpenAIBuildBundle:
        operation = "build.repair" if feedback else "build.generate"
        prompt = f"""You are the Xyool autonomous software engineer.
Generate a deterministic Python capability for this request.

NAME: {request.name}
GOAL: {request.goal}
REQUIREMENTS: {list(request.requirements)}
FEEDBACK FROM PRIOR ATTEMPT: {feedback or 'none'}

Return ONLY valid JSON with exactly two string fields:
{{"source":"complete Python source","tests":"complete unittest source"}}

The generated source must be self-contained, deterministic, and safe to run
locally. Tests must test the requested behavior and use unittest.
"""
        data, usage = self._request(prompt, operation)
        raw = self._text(data)
        try:
            bundle = json.loads(raw)
            source = str(bundle["source"])
            tests = str(bundle["tests"])
        except (json.JSONDecodeError, KeyError, TypeError) as exc:
            self.ledger.record(operation, usage, success=False,
                               metadata={"model": self.model, "parse_error": str(exc),
                                         "name": request.name})
            raise RuntimeError("OpenAI returned a non-JSON build bundle") from exc

        self.ledger.record(
            operation,
            usage,
            success=True,
            metadata={"model": self.model, "response_id": str(data.get("id", "")),
                      "name": request.name, "feedback": bool(feedback)},
        )
        return OpenAIBuildBundle(source, tests, usage, str(data.get("id", "")))
