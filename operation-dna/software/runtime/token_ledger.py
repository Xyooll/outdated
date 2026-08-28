"""Token accounting for AI engineering operations.

The ledger separates measured provider usage from estimates. Real API providers
can supply exact input/output counts; offline providers use a deterministic
character-based estimate so the engineering loop can still be benchmarked.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
import json
from typing import Any


@dataclass(frozen=True)
class TokenUsage:
    input_tokens: int
    output_tokens: int
    measured: bool = False

    @property
    def total_tokens(self) -> int:
        return self.input_tokens + self.output_tokens


@dataclass(frozen=True)
class TokenEvent:
    operation: str
    input_tokens: int
    output_tokens: int
    measured: bool
    success: bool = True
    metadata: dict[str, Any] | None = None

    @property
    def total_tokens(self) -> int:
        return self.input_tokens + self.output_tokens


class TokenLedger:
    def __init__(self, path: str = "data/token_usage.jsonl"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.events: list[TokenEvent] = []

    @staticmethod
    def estimate(text: Any) -> int:
        """Conservative local estimate; not a substitute for tokenizer counts."""
        if text is None:
            return 0
        value = text if isinstance(text, str) else json.dumps(text, default=str, separators=(",", ":"))
        return max(0, (len(value) + 3) // 4)

    def record(self, operation: str, usage: TokenUsage, *, success: bool = True,
               metadata: dict[str, Any] | None = None) -> TokenEvent:
        event = TokenEvent(operation, usage.input_tokens, usage.output_tokens,
                           usage.measured, success, metadata)
        self.events.append(event)
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(asdict(event), default=str) + "\n")
        return event

    def record_text(self, operation: str, prompt: Any, response: Any, *,
                    success: bool = True, metadata: dict[str, Any] | None = None) -> TokenEvent:
        return self.record(operation, TokenUsage(self.estimate(prompt), self.estimate(response), False),
                           success=success, metadata=metadata)

    def summary(self) -> dict[str, Any]:
        total = sum(e.total_tokens for e in self.events)
        inp = sum(e.input_tokens for e in self.events)
        out = sum(e.output_tokens for e in self.events)
        measured = sum(1 for e in self.events if e.measured)
        successes = sum(1 for e in self.events if e.success)
        return {
            "events": len(self.events),
            "input_tokens": inp,
            "output_tokens": out,
            "total_tokens": total,
            "measured_events": measured,
            "successes": successes,
            "tokens_per_success": (total / successes) if successes else 0.0,
        }

    def operation_summary(self) -> dict[str, dict[str, Any]]:
        result: dict[str, dict[str, Any]] = {}
        for event in self.events:
            row = result.setdefault(event.operation, {"events": 0, "input_tokens": 0,
                                                       "output_tokens": 0, "total_tokens": 0})
            row["events"] += 1
            row["input_tokens"] += event.input_tokens
            row["output_tokens"] += event.output_tokens
            row["total_tokens"] += event.total_tokens
        return result

    def efficiency(self, *, successful_capabilities: int = 0) -> dict[str, Any]:
        summary = self.summary()
        total = summary["total_tokens"]
        return {
            **summary,
            "successful_capabilities": successful_capabilities,
            "tokens_per_capability": (total / successful_capabilities) if successful_capabilities else 0.0,
        }
