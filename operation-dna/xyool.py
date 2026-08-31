"""Interactive Xyool shell: one model, behavior, and an expandable environment."""
from __future__ import annotations
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))
from operation_dna.software.runtime.agent_orchestrator import SkillRegistry
from operation_dna.software.runtime.autonomous_agent import AutonomousAgent
from operation_dna.software.runtime.capability_environment import CapabilityEnvironment
from operation_dna.software.runtime.codex_engine import CodexEngine
from operation_dna.software.runtime.openai_provider import OpenAIProvider
from operation_dna.software.runtime.project_inspector import ProjectInspector
from operation_dna.software.runtime.self_build_agent import BuildRequest, SelfBuildAgent, write_build_record
from operation_dna.software.runtime.software_factory import SoftwareFactory
from operation_dna.software.runtime.web_skill import WebSkill
from operation_dna.software.runtime.memory_context import MemoryContext

BEHAVIOR = ROOT / "agent_behavior.md"

def main() -> None:
    provider = OpenAIProvider()
    factory = SoftwareFactory(staging_root=str(ROOT / ".generated_agent"))
    builder = SelfBuildAgent(factory, provider, max_iterations=3)
    inspector = ProjectInspector(REPO)
    environment = CapabilityEnvironment(REPO)
    codex = CodexEngine(REPO)
    memory = MemoryContext(REPO)
    skills = SkillRegistry()

    skills.register("inspect_environment", lambda objective="", **_: environment.inspect(objective))
    skills.register("inspect_project", lambda query="", objective="", **_: inspector.summary())
    skills.register("web_search", WebSkill())
    skills.register("codex_engine", lambda objective="", **_: codex.run(objective))
    skills.register("memory_recall", lambda query="", limit=8, **_: memory.recall(query, int(limit)))
    skills.register("memory_remember", lambda content="", kind="experience", source="agent", objective="", metadata=None, **_: memory.remember(content, kind, source, objective, metadata))
    skills.register("memory_index", lambda **_: memory.index())
    skills.register("memory_aggregate", lambda query="", limit=100, **_: memory.aggregate(query, int(limit)))

    def create_software(objective="", **_: object):
        name = "software_" + str(abs(hash(objective)))[:10]
        request = BuildRequest(name=name, goal=objective, requirements=(
            "inspect existing resources before creating anything",
            "fit the existing repository architecture",
            "include tests", "avoid destructive changes"))
        result = builder.build(request, promote=False)
        write_build_record(result)
        return {"iteration": result.iteration, "syntax_ok": result.build.syntax_ok,
                "tests_ok": result.build.tests_ok, "promoted": result.promoted,
                "reason": result.build.reason, "notes": result.notes}

    skills.register("create_software", create_software)

    def progress(message: str) -> None:
        print(f"[XYOOL] {message}", flush=True)

    agent = AutonomousAgent(provider, skills, behavior=BEHAVIOR.read_text(encoding="utf-8"), max_steps=12, progress=progress)
    print("XYOOL autonomous agent")
    print("Type naturally. :help, :tokens, :reset, :quit")
    print()
    while True:
        try:
            text = input("XYOOL> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break
        if not text:
            continue
        if text in {":quit", ":exit"}:
            break
        if text == ":reset":
            agent.reset()
            print("AGENT: conversation reset.\n")
            continue
        if text == ":help":
            print("Talk naturally or give Xyool an objective. It decides when to use memory, inspect the environment, research, code, test, or create new resources.")
            print(":tokens shows API usage; :reset clears conversation; :quit exits.\n")
            continue
        if text == ":tokens":
            print(provider.ledger.summary())
            print(provider.ledger.operation_summary())
            print()
            continue
        result = agent.send(text)
        print(f"AGENT: {result.content}\n")

if __name__ == "__main__":
    main()
