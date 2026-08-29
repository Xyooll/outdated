"""Interactive Xyool shell: agent orchestrates, software provides skills."""
from __future__ import annotations
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
if str(REPO) not in sys.path: sys.path.insert(0, str(REPO))
from operation_dna.software.runtime.agent_orchestrator import AgentOrchestrator, SkillRegistry
from operation_dna.software.runtime.openai_provider import OpenAIProvider
from operation_dna.software.runtime.project_inspector import ProjectInspector
from operation_dna.software.runtime.self_build_agent import BuildRequest, SelfBuildAgent, write_build_record
from operation_dna.software.runtime.software_factory import SoftwareFactory
from operation_dna.software.runtime.web_skill import WebSkill

def main() -> None:
    provider = OpenAIProvider()
    factory = SoftwareFactory(staging_root=str(ROOT / ".generated_agent"))
    builder = SelfBuildAgent(factory, provider, max_iterations=3)
    inspector = ProjectInspector(REPO)
    skills = SkillRegistry()
    skills.register("inspect_project", lambda query="", objective="": inspector.summary())
    skills.register("web_search", WebSkill())
    def build_software(objective="", **_):
        name = "capability_" + str(abs(hash(objective)))[:10]
        request = BuildRequest(name=name, goal=objective, requirements=(
            "fit the existing Operation DNA architecture",
            "inspect existing code before duplicating functionality",
            "include tests", "avoid destructive changes"))
        result = builder.build(request, promote=False)
        write_build_record(result)
        return {"iteration": result.iteration, "syntax_ok": result.build.syntax_ok,
                "tests_ok": result.build.tests_ok, "promoted": result.promoted,
                "reason": result.build.reason, "notes": result.notes}
    skills.register("build_software", build_software)
    orchestrator = AgentOrchestrator(provider, skills)
    history: list[dict[str, str]] = []
    print("XYOOL interactive agent")
    print("Type naturally. :help, :tokens, :quit")
    print()
    while True:
        try: text = input("XYOOL> ").strip()
        except (EOFError, KeyboardInterrupt): print("\nExiting."); break
        if not text: continue
        if text in {":quit", ":exit"}: break
        if text == ":help":
            print("Tell Xyool what you want. The agent decides whether and how to use its skills.")
            print(":tokens shows API usage. :quit exits."); continue
        if text == ":tokens":
            print(provider.ledger.summary()); print(provider.ledger.operation_summary()); continue
        result = orchestrator.run(text, history)
        print(f"AGENT: {result.content}")
        history += [{"role": "user", "content": text}, {"role": "assistant", "content": result.content}]
        print()

if __name__ == "__main__": main()
