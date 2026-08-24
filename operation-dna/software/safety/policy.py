"""Central policy evaluation boundary. Policies are configuration, not AI output."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Policy:
    require_authorization: bool = True
    require_evidence: bool = True
    minimum_evidence_score: float = 0.5
    require_reversible_action: bool = True
    require_capability: bool = True
    max_risk_score: float = 0.25
    require_audit: bool = True


@dataclass(frozen=True)
class ActionRequest:
    authorized: bool
    evidence_score: float
    risk_score: float
    reversible: bool
    auditable: bool
    permitted: bool = False


def evaluate(policy: Policy, request: ActionRequest) -> tuple[bool, list[str]]:
    failures: list[str] = []
    if policy.require_authorization and not request.authorized:
        failures.append("authorization")
    if policy.require_evidence and request.evidence_score < policy.minimum_evidence_score:
        failures.append("evidence")
    if request.risk_score > policy.max_risk_score:
        failures.append("risk")
    if policy.require_reversible_action and not request.reversible:
        failures.append("reversibility")
    if policy.require_capability and not request.permitted:
        failures.append("capability")
    if policy.require_audit and not request.auditable:
        failures.append("audit")
    return not failures, failures
