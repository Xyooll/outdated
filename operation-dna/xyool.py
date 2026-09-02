"""Interactive Xyool shell backed by the OpenAI Agents SDK."""
from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from operation_dna.software.runtime.openai_agent_runtime import OpenAIAgentRuntime

BEHAVIOR = ROOT / "agent_behavior.md"
SESSION_DB = ROOT / "data" / "xyool_sessions.sqlite"
PROJECT_OBJECTIVE_FILE = ROOT / "data" / "xyool_objective.json"
SKILLS_DIR = ROOT / "skills"
SESSION_ID = "default"


def load_project_objective() -> str:
    if not PROJECT_OBJECTIVE_FILE.exists():
        return ""
    try:
        data = json.loads(PROJECT_OBJECTIVE_FILE.read_text(encoding="utf-8"))
        return str(data.get("objective", "")).strip() if isinstance(data, dict) else ""
    except (OSError, json.JSONDecodeError, TypeError):
        return ""


async def main() -> None:
    runtime = OpenAIAgentRuntime(
        repo=REPO,
        behavior_file=BEHAVIOR,
        skills_dir=SKILLS_DIR,
        session_db=SESSION_DB,
        project_objective=load_project_objective(),
    )

    print("XYOOL")
    print("OpenAI agent runtime. Type naturally. :help, :reset, :quit")
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
            await runtime.reset(SESSION_ID)
            print("AGENT: conversation reset.\n")
            continue
        if text == ":help":
            print("Xyool is one OpenAI agent. It uses instructions, skills, tools, memory, and optional MCP servers as needed.")
            print(":reset clears the persistent conversation; :quit exits.\n")
            continue

        try:
            result = await runtime.run(text, session_id=SESSION_ID)
            print(f"AGENT: {result}\n")
        except Exception as exc:
            print(f"AGENT: I couldn't complete that request because {type(exc).__name__}: {exc}\n")


if __name__ == "__main__":
    asyncio.run(main())
