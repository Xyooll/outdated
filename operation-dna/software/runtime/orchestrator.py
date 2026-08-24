"""Domain-neutral lifecycle orchestrator."""
from dataclasses import dataclass
from typing import Any

@dataclass
class RunResult:
    status: str
    data: dict[str, Any]

class Orchestrator:
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
        result = app.act(context, proposal)
        outcome = app.observe(context)
        lessons = app.learn(context, outcome)
        evolution = app.evolve(context, lessons)
        return RunResult(result.status, {"hypotheses": hypotheses, "action": result.__dict__, "outcome": outcome, "lessons": lessons, "evolution": evolution})
