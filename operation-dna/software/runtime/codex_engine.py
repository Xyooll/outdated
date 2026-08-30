"""Codex-class repository engineering mean for Xyool.

Uses the OpenAI Responses API with a Codex model and Xyool-owned filesystem/shell
functions. The model is a replaceable means; Xyool remains responsible for the
objective, evaluation, authorization, and human handoff.
"""
from __future__ import annotations
import json
import os
import subprocess
from pathlib import Path
from typing import Any
import requests

DEFAULT_BASE_URL = "https://api.openai.com/v1"
DEFAULT_MODEL = "gpt-5.3-codex"

_DENY = ("git push", "git reset --hard", "git clean -fd", "Remove-Item", "rmdir", "del /s", "format ")

class CodexEngine:
    def __init__(self, repo: str | Path, api_key: str | None = None,
                 model: str | None = None, base_url: str = DEFAULT_BASE_URL,
                 max_turns: int = 20):
        self.repo = Path(repo).resolve()
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise RuntimeError("OPENAI_API_KEY is required")
        self.model = model or os.getenv("XYOOL_CODEX_MODEL", DEFAULT_MODEL)
        self.base_url = base_url.rstrip("/")
        self.max_turns = max_turns

    def _path(self, path: str) -> Path:
        p = (self.repo / path).resolve()
        if p != self.repo and self.repo not in p.parents:
            raise ValueError("path escapes Xyool repository")
        return p

    def _read_file(self, path: str) -> str:
        p = self._path(path)
        return p.read_text(encoding="utf-8")

    def _write_file(self, path: str, content: str) -> str:
        p = self._path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
        return f"wrote {p.relative_to(self.repo)} ({len(content)} chars)"

    def _list_files(self, path: str = ".") -> list[str]:
        root = self._path(path)
        return [str(p.relative_to(self.repo)) for p in root.rglob("*") if p.is_file()][:500]

    def _run_command(self, command: str) -> str:
        lowered = command.lower()
        if any(x.lower() in lowered for x in _DENY):
            return "COMMAND_DENIED: destructive or remote git/filesystem command"
        result = subprocess.run(command, cwd=self.repo, shell=True, text=True,
                                capture_output=True, timeout=180)
        out = (result.stdout + "\n" + result.stderr).strip()
        return f"exit_code={result.returncode}\n{out[-12000:]}"

    def _tool_defs(self) -> list[dict[str, Any]]:
        return [
            {"type":"function","name":"read_file","description":"Read a UTF-8 file inside the Xyool repository.","parameters":{"type":"object","properties":{"path":{"type":"string"}},"required":["path"],"additionalProperties":False},"strict":True},
            {"type":"function","name":"write_file","description":"Create or replace a UTF-8 file inside the Xyool repository. Use only when the change is justified by the objective.","parameters":{"type":"object","properties":{"path":{"type":"string"},"content":{"type":"string"}},"required":["path","content"],"additionalProperties":False},"strict":True},
            {"type":"function","name":"list_files","description":"List repository files to discover existing means and integration points.","parameters":{"type":"object","properties":{"path":{"type":"string"}},"required":[],"additionalProperties":False},"strict":True},
            {"type":"function","name":"run_command","description":"Run a non-destructive local repository command for tests, syntax checks, inspection, or builds.","parameters":{"type":"object","properties":{"command":{"type":"string"}},"required":["command"],"additionalProperties":False},"strict":True},
        ]

    def run(self, objective: str) -> dict[str, Any]:
        instructions = f"""You are the Xyool software-engineering mean, powered by {self.model}.
Work autonomously on the user's objective inside this repository: {self.repo}
OBJECTIVE: {objective}

You are a MEANS, not the overall Xyool objective controller. Inspect before changing. Reuse existing code. Diagnose failures instead of repeating the same action. You may create or repair software, run tests, and iterate. Do not use git push or destructive filesystem commands. Do not claim success until you have inspected the actual result and run relevant tests. Return a concise final report with files changed, tests run, results, remaining blockers, and whether another means should be tried.
"""
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        input_items: list[dict[str, Any]] = [{"role":"user","content":objective}]
        last_id = None
        events: list[dict[str, Any]] = []
        for _ in range(self.max_turns):
            payload: dict[str, Any] = {"model":self.model,"instructions":instructions,"input":input_items,"tools":self._tool_defs(),"tool_choice":"auto"}
            if last_id:
                payload["previous_response_id"] = last_id
                payload.pop("input", None)
                payload["input"] = input_items
            r = requests.post(f"{self.base_url}/responses", headers=headers, json=payload, timeout=240)
            r.raise_for_status()
            data = r.json()
            last_id = data.get("id")
            output = data.get("output", [])
            tool_calls = [x for x in output if x.get("type") == "function_call"]
            if not tool_calls:
                text = data.get("output_text") or ""
                if not text:
                    for item in output:
                        for c in item.get("content", []):
                            if isinstance(c.get("text"), str): text += c["text"]
                return {"ok":True,"model":self.model,"response_id":last_id,"report":text.strip(),"events":events}
            input_items = []
            for call in tool_calls:
                name = call.get("name")
                args = json.loads(call.get("arguments") or "{}")
                try:
                    if name == "read_file": result = self._read_file(args["path"])
                    elif name == "write_file": result = self._write_file(args["path"], args["content"])
                    elif name == "list_files": result = self._list_files(args.get("path", "."))
                    elif name == "run_command": result = self._run_command(args["command"])
                    else: result = f"UNKNOWN_TOOL: {name}"
                except Exception as exc:
                    result = f"TOOL_ERROR {type(exc).__name__}: {exc}"
                events.append({"tool":name,"arguments":args,"result":result[-4000:]})
                input_items.append({"type":"function_call_output","call_id":call["call_id"],"output":str(result)})
        return {"ok":False,"model":self.model,"response_id":last_id,"report":"Codex engineering mean reached its iteration limit.","events":events}
