"""Controlled evolution/promotion state machine."""
from dataclasses import dataclass

@dataclass(frozen=True)
class PromotionDecision:
    status: str
    reason: str

class PromotionController:
    def decide(self, eligible: bool, improved: bool, safe: bool, authorized: bool) -> PromotionDecision:
        if not eligible: return PromotionDecision("rejected", "not eligible")
        if not improved: return PromotionDecision("rejected", "no measured improvement")
        if not safe: return PromotionDecision("rejected", "safety gate failed")
        if not authorized: return PromotionDecision("awaiting_authorization", "human/policy authorization required")
        return PromotionDecision("approved", "all promotion gates passed")
