"""OpenAI Agents SDK runtime for Xyool.

The model is the orchestrator. Xyool supplies instructions, persistent session
memory, local application tools, skills, and optional MCP servers.
"""
from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from agents import Agent, FileSearchTool, Runner, SQLiteSession, WebSearchTool, function_tool
from agents.mcp import MCPServerManager, MCPServerStdio, MCPServerStreamableHttp

from .memory_context import MemoryContext
from .project_inspector import ProjectInspector

ROOT = Path(__file__).resolve().parents[2]

# Xyool should be runnable from the repository without requiring the launcher
# shell to export credentials first. Never store credentials in source control.
load_dotenv(ROOT.parent / ".env")
load_dotenv(ROOT / ".env")


class OpenAIAgentRuntime:
    """Thin application layer around the OpenAI Agents SDK."""

    def __init__(self, repo: str | Path, behavior_file: str | Path, skills_dir: str | Path,
                 session_db: str | Path, project_objective: str = "") -> None:
        self.repo = Path(repo).resolve()
        self.behavior_file = Path(behavior_file).resolve()
        self.skills_dir = Path(skills_dir).resolve()
        self.session_db = Path(session_db).resolve()
        self.project_objective = project_objective.strip()
        self.inspector = ProjectInspector(self.repo)
        self.memory = MemoryContext(self.repo)
        self.mcp_servers: list[Any] = []
        self._manager: MCPServerManager | None = None

    def instructions(self) -> str:
        behavior = self.behavior_file.read_text(encoding="utf-8") if self.behavior_file.exists() else ""
        skills = self._skill_index()
        project = f"\n\nPROJECT OBJECTIVE:\n{self.project_objective}" if self.project_objective else ""
        return (
            behavior + project + "\n\nSKILLS AVAILABLE:\n" +
            (skills or "No local skills are currently installed.") +
            "\n\nYou are the single Xyool intelligence. You decide when and how to use tools. "
            "Skills are reusable instructions, not separate agents or workflows. "
            "Use tools to inspect reality and take action; do not merely describe actions you could take. "
            "Verify meaningful work before claiming completion. Be truthful about what was observed, inferred, attempted, and accomplished. "
            "Preserve useful evidence and disagreement."
        )

    def _skill_index(self) -> str:
        if not self.skills_dir.exists():
            return ""
        rows: list[str] = []
        for path in sorted(self.skills_dir.rglob("*.md")):
            if path.name.lower() == "readme.md":
                continue
            try:
                first = path.read_text(encoding="utf-8").splitlines()[:8]
            except OSError:
                continue
            description = " ".join(line.strip("# ") for line in first if line.strip())[:240]
            rows.append(f"- {path.stem}: {description}")
        return "\n".join(rows)

    def _tools(self) -> list[Any]:
        runtime = self

        @function_tool
        def inspect_project() -> str:
            """Inspect the current repository and summarize its files and Python symbols."""
            return runtime.inspector.summary()

        @function_tool
        def recall_memory(query: str, limit: int = 8) -> dict[str, Any]:
            """Retrieve relevant persistent memory and evidence for a query."""
            return runtime.memory.recall(query, int(limit))

        @function_tool
        def remember_memory(content: str, kind: str = "experience", source: str = "agent",
                            objective: str = "") -> dict[str, Any]:
            """Persist useful knowledge, experience, evidence, or an observation."""
            return runtime.memory.remember(content, kind, source, objective)

        @function_tool
        def aggregate_memory(query: str, limit: int = 100) -> dict[str, Any]:
            """Aggregate persistent evidence into a higher-level knowledge bundle while preserving provenance."""
            return runtime.memory.aggregate(query, int(limit))

        @function_tool
        def index_memory() -> dict[str, Any]:
            """Rebuild the persistent memory index for faster retrieval."""
            return runtime.memory.index()

        @function_tool
        def load_skill(name: str) -> str:
            """Load a local skill by name when its specialized instructions are useful."""
            safe = Path(name).name
            candidates = [runtime.skills_dir / safe, runtime.skills_dir / f"{safe}.md"]
            for candidate in candidates:
                if candidate.exists() and candidate.suffix == ".md":
                    return candidate.read_text(encoding="utf-8")
            matches = list(runtime.skills_dir.rglob(f"{safe}.md")) if runtime.skills_dir.exists() else []
            if matches:
                return matches[0].read_text(encoding="utf-8")
            return f"Skill not found: {name}"

        @function_tool
        def run_tests(test_path: str = "") -> str:
            """Run the repository test suite or a specific pytest path and return the actual result."""
            command = [os.environ.get("PYTHON", "python"), "-m", "pytest", "-q"]
            if test_path.strip():
                command.append(test_path.strip())
            try:
                completed = subprocess.run(command, cwd=runtime.repo, text=True,
                                           capture_output=True, timeout=300)
            except (OSError, subprocess.TimeoutExpired) as exc:
                return f"TEST_ERROR {type(exc).__name__}: {exc}"
            output = (completed.stdout + "\n" + completed.stderr).strip()
            return f"exit_code={completed.returncode}\n{output[-12000:]}"

        tools: list[Any] = [WebSearchTool(), inspect_project, recall_memory, remember_memory,
                            aggregate_memory, index_memory, load_skill, run_tests]
        vector_ids = [x.strip() for x in os.getenv("XYOOL_VECTOR_STORE_IDS", "").split(",") if x.strip()]
        if vector_ids:
            tools.append(FileSearchTool(vector_store_ids=vector_ids, max_num_results=8))
        return tools

    def _load_mcp_servers(self) -> list[Any]:
        raw = os.getenv("XYOOL_MCP_SERVERS", "").strip()
        if not raw:
            return []
        try:
            configs = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"XYOOL_MCP_SERVERS is not valid JSON: {exc}") from exc
        if not isinstance(configs, list):
            raise RuntimeError("XYOOL_MCP_SERVERS must be a JSON array")

        servers: list[Any] = []
        for cfg in configs:
            if not isinstance(cfg, dict):
                continue
            name = str(cfg.get("name", "mcp"))
            transport = str(cfg.get("transport", "streamable_http"))
            approval = cfg.get("require_approval")
            if transport == "streamable_http":
                params: dict[str, Any] = {"url": str(cfg["url"]), "timeout": float(cfg.get("timeout", 10))}
                if cfg.get("headers"):
                    params["headers"] = dict(cfg["headers"])
                servers.append(MCPServerStreamableHttp(name=name, params=params, cache_tools_list=True,
                                                       max_retry_attempts=2, require_approval=approval))
            elif transport == "stdio":
                servers.append(MCPServerStdio(
                    name=name,
                    params={"command": str(cfg["command"]), "args": [str(x) for x in cfg.get("args", [])],
                            "env": dict(cfg.get("env", {}))},
                    cache_tools_list=True, require_approval=approval,
                ))
            else:
                raise RuntimeError(f"Unsupported MCP transport: {transport}")
        return servers

    async def _connect_mcp(self) -> list[Any]:
        self.mcp_servers = self._load_mcp_servers()
        if not self.mcp_servers:
            return []
        self._manager = MCPServerManager(self.mcp_servers)
        await self._manager.connect_all()
        return list(self._manager.active_servers)

    async def run(self, user_text: str, session_id: str = "default") -> str:
        active_mcp = await self._connect_mcp()
        try:
            agent = Agent(
                name="Xyool",
                model=os.getenv("XYOOL_OPENAI_MODEL", "gpt-5.6-luna"),
                instructions=self.instructions(),
                tools=self._tools(),
                mcp_servers=active_mcp,
                mcp_config={"convert_schemas_to_strict": True},
            )
            session = SQLiteSession(session_id, self.session_db)
            result = await Runner.run(agent, user_text, session=session)
            return str(result.final_output)
        finally:
            if self._manager is not None:
                await self._manager.cleanup_all()
                self._manager = None
                self.mcp_servers = []

    async def reset(self, session_id: str = "default") -> None:
        session = SQLiteSession(session_id, self.session_db)
        await session.clear_session()
