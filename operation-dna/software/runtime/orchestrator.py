"""Domain-neutral lifecycle orchestrator with a mandatory safety gate."""
from dataclasses import dataclass
from typing import Any

from ..safety.policy import ActionRequest, Policy, evaluate


@dataclass
class RunResult:
    status: str
    data: dict[str, Any]


class Orchestrator:
    def __init__(self, policy: Policy | None = None):
        self.policy = policy or Policy()

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

        request = ActionRequest(
            authorized=bool(proposal.get("authorized", False)),
            evidence_score=float(proposal.get("evidence_score", 0.0)),
            risk_score=float(proposal.get("risk_score", 1.0)),
            reversible=bool(proposal.get("reversible", False)),
            auditable=bool(proposal.get("auditable", False)),
        )
        gate_passed, failures = evaluate(self.policy, request)
        if not gate_passed:
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
