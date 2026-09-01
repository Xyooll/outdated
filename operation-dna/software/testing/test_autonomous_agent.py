from __future__ import annotations

import json

from operation_dna.software.runtime.agent_orchestrator import SkillRegistry
from operation_dna.software.runtime.autonomous_agent import AutonomousAgent, ObjectiveState

class RecordingProvider:
    def __init__(self) -> None:
        self.calls: list[list[dict[str, str]]] = []
    def complete(self, messages: list[dict[str, str]], operation: str = "") -> str:
        self.calls.append(messages)
        return json.dumps({"kind": "respond", "content": "ack", "skill": "", "arguments": {}})

def test_human_message_stays_in_active_objective_without_keywords(tmp_path) -> None:
    agent = AutonomousAgent(RecordingProvider(), SkillRegistry(), behavior="You are Xyool.", state_file=tmp_path / "objective.json")
    agent.send("Build the memory system")
    context = agent._message_context("What about indexing?")
    assert "ACTIVE OBJECTIVE:" in context
    assert "Build the memory system" in context
    assert "What about indexing?" in context
    assert "human_input_with_active_objective" in context

def test_objective_state_persists_and_resets(tmp_path) -> None:
    state_file = tmp_path / "objective.json"
    agent = AutonomousAgent(RecordingProvider(), SkillRegistry(), behavior="You are Xyool.", state_file=state_file)
    agent.send("Finish the Xyool runtime")
    assert state_file.exists()
    restored = AutonomousAgent(RecordingProvider(), SkillRegistry(), behavior="You are Xyool.", state_file=state_file)
    assert restored.objective is not None
    assert restored.objective.text == "Finish the Xyool runtime"
    restored.reset()
    assert restored.objective is None
    assert not state_file.exists()

def test_completed_objective_can_start_a_new_objective(tmp_path) -> None:
    agent = AutonomousAgent(RecordingProvider(), SkillRegistry(), behavior="You are Xyool.", state_file=tmp_path / "objective.json")
    agent.objective = ObjectiveState(text="First objective", status="complete")
    agent._save_state()
    context = agent._message_context("Start something else")
    assert context == "Start something else"
    assert agent.objective is not None
    assert agent.objective.text == "Start something else"
    assert agent.objective.status == "active"

def test_model_can_replace_active_objective(tmp_path) -> None:
    class NewObjectiveProvider:
        def complete(self, messages: list[dict[str, str]], operation: str = "") -> str:
            return json.dumps({"kind": "new_objective", "content": "New objective", "skill": "", "arguments": {}})
    agent = AutonomousAgent(NewObjectiveProvider(), SkillRegistry(), behavior="You are Xyool.", state_file=tmp_path / "objective.json")
    agent.objective = ObjectiveState(text="Old objective")
    action = agent.send("Actually, do this other thing")
    assert action.kind == "new_objective"
    assert agent.objective is not None
    assert agent.objective.text == "New objective"
