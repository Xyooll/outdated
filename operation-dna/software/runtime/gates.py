"""Pre-deployment gates for real-world adapters."""
from dataclasses import dataclass

@dataclass(frozen=True)
class GateResult:
    allowed: bool
    reason: str

class DeploymentGates:
    def check(self, *, tests: bool, sandbox: bool, improved: bool, authorized: bool, side_effects: bool) -> GateResult:
        if not tests: return GateResult(False, "tests failed")
        if not sandbox: return GateResult(False, "sandbox failed")
        if not improved: return GateResult(False, "no demonstrated improvement")
        if side_effects and not authorized: return GateResult(False, "authorization required for side effects")
        return GateResult(True, "deployment eligible")
