"""Domain-neutral lifecycle orchestrator with mandatory safety and capability gates."""
from dataclasses import dataclass
from typing import Any

from ..safety.policy import ActionRequest, Policy, evaluate
from .permissions import Capability, PermissionSet


@dataclass
class RunResult:
    status: str
    data: dict[str, Any]


class Orchestrator:
    def __init__(self, policy: Policy | None = None, permissions: PermissionSet | None = None):
        self.policy = policy or Policy()
        self.permissions = permissions or PermissionSet(frozenset())

    def run(self, app, context):
        observations = app.perceive(context)
        context.observations = observations
        understood = app.understand(context)
        context.observations = understood
        hypotheses = app.hypothesize(context)
        test = app.test(context)
        proposal = test.get("proposal")
        if proposal is None:
            lessons = app.learn(context, test)
            return RunResult("observed", {"test": test, "lessons": lessons})

        capability_name = proposal.get("capability")
        permitted = False
        capability_error = None
        try:
            capability = Capability(capability_name) if capability_name else None
            permitted = capability is not None and self.permissions.allows(capability)
            if capability is None:
                capability_error = "missing capability"
        except ValueError:
            capability_error = f"unknown capability: {capability_name}"

        request = ActionRequest(
            authorized=bool(proposal.get("authorized", False)),
            evidence_score=float(proposal.get("evidence_score", 0.0)),
            risk_score=float(proposal.get("risk_score", 1.0)),
            reversible=bool(proposal.get("reversible", False)),
            auditable=bool(proposal.get("auditable", False)),
            permitted=permitted,
        )
        gate_passed, failures = evaluate(self.policy, request)
        if capability_error:
            failures.append("capability")
        if not gate_passed or capability_error:
            return RunResult(
                "blocked",
                {
                    "hypotheses": hypotheses,
                    "proposal": proposal,
                    "gate_passed": False,
                    "gate_failures": failures,
                },
            )

        result = app.act(context, proposal)
        outcome = app.observe(context)
        lessons = app.learn(context, outcome)
        evolution = app.evolve(context, lessons)
        return RunResult(
            result.status,
            {
                "hypotheses": hypotheses,
                "action": result.__dict__,
                "outcome": outcome,
                "lessons": lessons,
                "evolution": evolution,
                "gate_passed": True,
            },
        )
