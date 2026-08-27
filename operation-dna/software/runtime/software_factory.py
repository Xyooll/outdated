"""AI-directed software factory with a human-controlled promotion boundary."""
from dataclasses import dataclass
from pathlib import Path
import ast
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

        test_path = Path(test_file)
        if test_path.exists() and test_path.is_file():
            # Discover from the test file's directory so temporary/generated
            # candidates can be tested without modifying the repository.
            command = [
                sys.executable,
                "-m",
                "unittest",
                "discover",
                "-s",
                str(test_path.parent),
                "-p",
                test_path.name,
                "-v",
            ]
        else:
            command = [sys.executable, "-m", "unittest", test_file, "-v"]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=60,
        )
        ok = result.returncode == 0
        failure = (result.stderr or result.stdout)[-2000:]
        return BuildResult(
            base.name,
            base.path,
            True,
            ok,
            False,
            "tests passed" if ok else failure,
        )

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
