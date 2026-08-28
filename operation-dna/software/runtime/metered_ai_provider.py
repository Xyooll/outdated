"""Provider wrapper that records AI engineering token usage."""
from __future__ import annotations

from typing import Any

from .ai_provider import AIProvider, EngineeringPlan, RepairPlan
from .token_ledger import TokenLedger, TokenUsage


class MeteredAIProvider:
    """Wrap any AI provider and account for plan/reason/repair usage."""

    def __init__(self, provider: AIProvider, ledger: TokenLedger | None = None):
        self.provider = provider
        self.ledger = ledger or TokenLedger()

    def reason(self, prompt: str, context: list[dict[str, Any]]) -> dict[str, Any]:
        result = self.provider.reason(prompt, context)
        self.ledger.record_text("reason", {"prompt": prompt, "context": context}, result)
        return result

    def plan(self, goal: str) -> EngineeringPlan:
        result = self.provider.plan(goal)
        self.ledger.record_text("plan", goal, {
            "name": result.name, "goal": result.goal,
            "requirements": result.requirements, "test_strategy": result.test_strategy,
        })
        return result

    def repair(self, plan: EngineeringPlan, failure: str) -> RepairPlan:
        result = self.provider.repair(plan, failure)
        self.ledger.record_text("repair", {
            "goal": plan.goal, "requirements": plan.requirements, "failure": failure,
        }, {
            "category": result.category, "rationale": result.rationale,
            "instructions": result.instructions,
        })
        return result

    def record_api_usage(self, operation: str, input_tokens: int, output_tokens: int,
                         *, metadata: dict[str, Any] | None = None) -> None:
        """Allow a real API adapter to record exact provider-reported usage."""
        self.ledger.record(operation, TokenUsage(input_tokens, output_tokens, True), metadata=metadata)
