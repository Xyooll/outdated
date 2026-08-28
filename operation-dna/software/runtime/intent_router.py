"""Lightweight conversational intent router for the Xyool shell."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Intent:
    kind: str
    reason: str


BUILD_WORDS = {
    "build", "create", "implement", "add", "make", "develop", "write",
    "generate", "code", "engineer", "refactor", "fix", "repair",
}
INSPECT_WORDS = {
    "inspect", "status", "check", "show", "list", "what", "which",
    "where", "explain", "describe", "diagnose", "why",
}


def classify(text: str) -> Intent:
    words = {w.strip(".,!?;:()[]{}").lower() for w in text.split()}
    if words & BUILD_WORDS:
        return Intent("build", "engineering action detected")
    if words & INSPECT_WORDS:
        return Intent("inspect", "inspection/information request detected")
    return Intent("conversation", "no engineering action detected")
