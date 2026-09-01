from __future__ import annotations

import json

from operation_dna.software.runtime.agent_orchestrator import SkillRegistry
from operation_dna.software.runtime.autonomous_agent import AutonomousAgent, ObjectiveState

class RecordingProvider:
    def __init__(self) -> None:
        self.calls: list[list[dict[str, str]]] = []
    def complete(self, messages: list[dict[str, str]], operation: str = "") -> str:
        self.calls.append(messages)
        return json.dumps({"kind": "respond", "content": "I understand.", "skill": "", "arguments": {}})

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

def test_work_is_saved_for_later_status_questions(tmp_path) -> None:
    class WorkProvider:
        def __init__(self) -> None:
            self.calls = 0
        def complete(self, messages: list[dict[str, str]], operation: str = "") -> str:
            self.calls += 1
            if self.calls == 1:
                return json.dumps({"kind": "use_mean", "content": "I’m checking the existing project structure so I can reuse what is already there.", "skill": "inspect", "arguments": {}})
            return json.dumps({"kind": "respond", "content": "I checked the project structure and saved that work in my progress history.", "skill": "", "arguments": {}})
    registry = SkillRegistry()
    registry.register("inspect", lambda: "Found the runtime and testing infrastructure.")
    state_file = tmp_path / "objective.json"
    agent = AutonomousAgent(WorkProvider(), registry, behavior="You are Xyool.", state_file=state_file, max_steps=2)
    agent.send("Develop Xyool")
    restored = AutonomousAgent(RecordingProvider(), registry, behavior="You are Xyool.", state_file=state_file)
    context = restored._message_context("What have you done so far?")
    assert "RECENT WORK HISTORY:" in context
    assert "existing project structure" in context
    assert "Found the runtime and testing infrastructure." in context

def test_model_request_failure_does_not_crash_conversation(tmp_path) -> None:
    class FailingProvider:
        def complete(self, messages: list[dict[str, str]], operation: str = "") -> str:
            raise RuntimeError("temporary API failure")
    agent = AutonomousAgent(FailingProvider(), SkillRegistry(), behavior="You are Xyool.", state_file=tmp_path / "objective.json")
    action = agent.send("Continue the objective")
    assert action.kind == "respond"
    assert "couldn't complete" in action.content
    assert agent.objective is not None
    assert agent.objective.status == "active"
