"""Provider-neutral LLM boundary.

No provider SDK or credential is embedded in the DNA repository.
"""
from dataclasses import dataclass
from typing import Protocol

@dataclass(frozen=True)
class LLMRequest:
    system: str
    user: str
    temperature: float = 0.0

@dataclass(frozen=True)
class LLMResponse:
    text: str
    provider: str
    model: str
    usage: dict

class LLMProvider(Protocol):
    def generate(self, request: LLMRequest) -> LLMResponse: ...

class DisabledProvider:
    """Safe default until a real provider adapter is configured."""
    def generate(self, request: LLMRequest) -> LLMResponse:
        raise RuntimeError("No LLM provider configured")
