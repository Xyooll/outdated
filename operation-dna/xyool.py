"""Interactive Xyool agent shell."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from operation_dna.software.runtime.intent_router import classify
from operation_dna.software.runtime.openai_provider import OpenAIProvider
from operation_dna.software.runtime.self_build_agent import BuildRequest, SelfBuildAgent, write_build_record
from operation_dna.software.runtime.software_factory import SoftwareFactory


def make_agent() -> tuple[SelfBuildAgent, OpenAIProvider]:
    provider = OpenAIProvider()
    factory = SoftwareFactory(staging_root=str(ROOT / ".generated_agent"))
    return SelfBuildAgent(factory, provider, max_iterations=3), provider


def conversation_reply(text: str) -> str:
    lowered = text.lower().strip(" .!?;:")
    if lowered in {"are you ready", "ready", "hello", "hi", "hey"}:
        return "Yes. API connected and self-build pipeline is operational."
    if lowered in {"what can you do", "help", "what do you do"}:
        return "I can converse, inspect the project, or build capabilities. Use :help for commands."
    return "I understand. If you want me to create or modify software, give me the objective explicitly with a build/create/implement request."


def inspect_reply(text: str) -> str:
    lowered = text.lower()
    if "status" in lowered:
        return "Self-build pipeline: API connected; generation, testing, repair, token accounting, and authority-gated promotion are available."
    if "token" in lowered:
        return ""  # handled by :tokens in main
    return "I can inspect project state through the engineering pipeline; ask for a specific status, component, or explanation."


def main() -> None:
    agent, provider = make_agent()
    print("XYOOL interactive agent")
    print("Type an objective, or :help, :tokens, :quit")
    print()

    while True:
        try:
            request_text = input("XYOOL> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break
        if not request_text:
            continue
        if request_text in {":quit", ":exit", "quit", "exit"}:
            break
        if request_text == ":help":
            print("Conversation is handled normally. Explicit build/create/implement requests invoke the self-build agent.")
            print(":tokens shows API usage. :quit exits.")
            continue
        if request_text == ":tokens":
            print(provider.ledger.summary())
            print(provider.ledger.operation_summary())
            continue

        intent = classify(request_text)
        if intent.kind == "conversation":
            print(f"AGENT: {conversation_reply(request_text)}")
            continue
        if intent.kind == "inspect":
            print(f"AGENT: {inspect_reply(request_text)}")
            continue

        safe_name = "capability_" + str(abs(hash(request_text)))[:10]
        request = BuildRequest(
            name=safe_name,
            goal=request_text,
            requirements=(
                "fit the existing Operation DNA architecture",
                "include tests",
                "avoid destructive changes",
            ),
        )
        print("AGENT: building...")
        result = agent.build(request, promote=False)
        write_build_record(result)
        print(f"RESULT: iteration={result.iteration} syntax={result.build.syntax_ok} tests={result.build.tests_ok}")
        print(f"PROMOTED={result.promoted}")
        print(f"REASON={result.build.reason}")
        for note in result.notes:
            print(f"NOTE={note}")
        print(f"TOKENS={provider.ledger.summary()}")
        print()


if __name__ == "__main__":
    main()
