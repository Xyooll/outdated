"""Interactive Xyool agent shell with project inspection."""
from __future__ import annotations
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
if str(REPO) not in sys.path: sys.path.insert(0, str(REPO))
from operation_dna.software.runtime.conversation_agent import ConversationAgent
from operation_dna.software.runtime.openai_provider import OpenAIProvider
from operation_dna.software.runtime.project_inspector import ProjectInspector
from operation_dna.software.runtime.self_build_agent import BuildRequest, SelfBuildAgent, write_build_record
from operation_dna.software.runtime.software_factory import SoftwareFactory

def main() -> None:
    provider = OpenAIProvider()
    agent = SelfBuildAgent(SoftwareFactory(staging_root=str(ROOT / ".generated_agent")), provider, max_iterations=3)
    brain = ConversationAgent(provider)
    inspector = ProjectInspector(REPO)
    history: list[dict[str, str]] = []
    print("XYOOL interactive agent")
    print("Type naturally. :help, :inspect, :tokens, :quit")
    print()
    while True:
        try: text = input("XYOOL> ").strip()
        except (EOFError, KeyboardInterrupt): print("\nExiting."); break
        if not text: continue
        if text in {":quit", ":exit", "quit", "exit"}: break
        if text == ":help":
            print("Talk normally. Ask questions, discuss ideas, inspect the project, or explicitly ask me to build/create/implement something.")
            print(":inspect scans the local project. :tokens shows API usage. :quit exits.")
            continue
        if text == ":inspect":
            print(inspector.summary()); print(); continue
        if text == ":tokens":
            print(provider.ledger.summary()); print(provider.ledger.operation_summary()); continue
        result = brain.respond(text, history)
        history.extend([{"role": "user", "content": text}, {"role": "assistant", "content": result.response}])
        if result.intent == "CONVERSE":
            print(f"AGENT: {result.response}")
            print(); continue
        if result.intent == "INSPECT":
            print(f"AGENT: {result.response}")
            print(inspector.summary())
            print(); continue
        print(f"AGENT: {result.response}")
        safe_name = "capability_" + str(abs(hash(text)))[:10]
        request = BuildRequest(name=safe_name, goal=text,
                                requirements=("fit the existing Operation DNA architecture", "inspect existing code before duplicating functionality", "include tests", "avoid destructive changes"))
        print("AGENT: building...")
        built = agent.build(request, promote=False)
        write_build_record(built)
        print(f"RESULT: iteration={built.iteration} syntax={built.build.syntax_ok} tests={built.build.tests_ok}")
        print(f"PROMOTED={built.promoted}")
        print(f"REASON={built.build.reason}")
        for note in built.notes: print(f"NOTE={note}")
        print(f"TOKENS={provider.ledger.summary()}")
        print()

if __name__ == "__main__": main()
