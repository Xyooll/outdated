"""AI-directed software factory with a human-controlled promotion boundary."""
from dataclasses import dataclass
from pathlib import Path
import ast
import os
import subprocess
import sys
from .authority import HumanAuthority

@dataclass(frozen=True)
class BuildResult:
    name: str
    path: str
    syntax_ok: bool
    tests_ok: bool
    promoted: bool
    reason: str

class SoftwareFactory:
    def __init__(self, staging_root: str = "data/software_staging", authority: HumanAuthority | None = None):
        self.root = Path(staging_root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.authority = authority or HumanAuthority()

    def stage(self, name: str, source: str) -> Path:
        if not name.isidentifier():
            raise ValueError("software name must be a Python identifier")
        path = self.root / f"{name}.py"
        path.write_text(source, encoding="utf-8")
        return path

    def validate(self, path: Path) -> BuildResult:
        try:
            ast.parse(path.read_text(encoding="utf-8"))
        except SyntaxError as exc:
            return BuildResult(path.stem, str(path), False, False, False, f"syntax: {exc}")
        return BuildResult(path.stem, str(path), True, False, False, "syntax passed; tests required")

    def run_tests(self, path: Path, test_file: str) -> BuildResult:
        base = self.validate(path)
        if not base.syntax_ok:
            return base
        test_path = Path(test_file).resolve()
        if not test_path.exists():
            return BuildResult(base.name, base.path, True, False, False, f"test file not found: {test_file}")

        # Run the generated test module as a normal unittest target. This is
        # deliberately isolated in a subprocess so candidate code cannot
        # mutate the factory's interpreter state. Both the candidate staging
        # directory and the repository's existing import roots are available.
        env = os.environ.copy()
        roots = [str(path.parent.resolve())]
        repo_root = Path.cwd().resolve()
        roots.append(str(repo_root))
        existing = env.get("PYTHONPATH", "")
        if existing:
            roots.append(existing)
        env["PYTHONPATH"] = os.pathsep.join(dict.fromkeys(roots))

        runner = (
            "import importlib.util, pathlib, sys, unittest; "
            "p=pathlib.Path(sys.argv[1]).resolve(); "
            "spec=importlib.util.spec_from_file_location('candidate_tests', p); "
            "m=importlib.util.module_from_spec(spec); "
            "sys.modules['candidate_tests']=m; spec.loader.exec_module(m); "
            "suite=unittest.defaultTestLoader.loadTestsFromModule(m); "
            "r=unittest.TextTestRunner(verbosity=2).run(suite); "
            "sys.exit(0 if r.wasSuccessful() else 1)"
        )
        try:
            result = subprocess.run(
                [sys.executable, "-c", runner, str(test_path)],
                cwd=str(path.parent.resolve()),
                env=env,
                capture_output=True,
                text=True,
                timeout=60,
            )
        except (OSError, subprocess.SubprocessError) as exc:
            return BuildResult(base.name, base.path, True, False, False, f"test runner error: {exc}")

        ok = result.returncode == 0
        output = (result.stdout + "\n" + result.stderr).strip()
        return BuildResult(base.name, base.path, True, ok, False, "tests passed" if ok else output[-4000:])

    def promote(self, result: BuildResult, destination: str, *, autonomy_level: int = 0) -> Path:
        if not (result.syntax_ok and result.tests_ok):
            raise PermissionError("software cannot be promoted until validation passes")
        if not self.authority.authorize(autonomy_level=autonomy_level):
            raise PermissionError("human authorization required for software promotion")
        src = Path(result.path)
        dst = Path(destination) / src.name
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
        return dst
