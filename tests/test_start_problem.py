import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "start_problem.py"


class StartProblemTests(unittest.TestCase):
    def run_cli(self, home: str, *args: str) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["HOME"] = home
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            cwd=REPO,
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_creates_only_requested_runnable_workspace(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            result = self.run_cli(temp, "r2-p1")
            self.assertEqual(result.returncode, 0, result.stderr)
            workspace = Path(temp) / "cic-practice" / "r2-p1"
            self.assertTrue((workspace / "AGENTS.md").is_file())
            self.assertTrue((workspace / ".github/copilot-instructions.md").is_file())
            self.assertTrue((workspace / "tests").is_dir())
            self.assertFalse(list(workspace.rglob("PR.md")))
            self.assertFalse(list(workspace.rglob("TICKET.md")))
            self.assertFalse(list(workspace.rglob("SOLUTION.md")))
            self.assertFalse((workspace / ".git").exists())
            self.assertIn("python -m unittest discover -s tests -v", result.stdout)

    def test_rejects_unknown_id_and_does_not_create_workspace(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            result = self.run_cli(temp, "r3-p1")
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse((Path(temp) / "cic-practice").exists())

    def test_existing_workspace_is_never_overwritten(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp) / "cic-practice" / "r1-p1"
            workspace.mkdir(parents=True)
            marker = workspace / "keep.txt"
            marker.write_text("student work")
            result = self.run_cli(temp, "r1-p1")
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(marker.read_text(), "student work")


if __name__ == "__main__":
    unittest.main()
