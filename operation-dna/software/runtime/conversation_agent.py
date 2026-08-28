"""API-backed conversational brain for Xyool."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


SYSTEM_PROMPT = """You are Xyool, an AI software-engineering agent.
Have normal conversation when the user is conversational. Answer questions directly.
When the user asks to build, create, implement, modify, fix, or repair software,
return a BUILD intent. Otherwise return CONVERSE or INSPECT intent.
Return exactly one line in this format:
INTENT=<CONVERSE|INSPECT|BUILD> RESPONSE=<short natural response>
Do not claim to have changed files unless the build pipeline actually ran.
"""


@dataclass(frozen=True)
class ConversationResult:
    intent: str
    response: str


class ConversationAgent:
    def __init__(self, provider: Any):
        self.provider = provider

    def respond(self, text: str, history: list[dict[str, str]] | None = None) -> ConversationResult:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        messages.extend(history or [])
        messages.append({"role": "user", "content": text})
        raw = self.provider.complete(messages)
        line = raw.strip().splitlines()[0] if raw.strip() else "INTENT=CONVERSE RESPONSE=I am ready."
        if "RESPONSE=" not in line or "INTENT=" not in line:
            return ConversationResult("CONVERSE", raw.strip())
        intent = line.split("INTENT=", 1)[1].split(None, 1)[0].strip()
        response = line.split("RESPONSE=", 1)[1].strip()
        if intent not in {"CONVERSE", "INSPECT", "BUILD"}:
            intent = "CONVERSE"
        return ConversationResult(intent, response)
