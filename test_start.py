import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent
SCRIPT = ROOT / "start.py"
PROBLEMS = {
    "r1-p1": ("validator.py",),
    "r1-p2": ("scheduler.py",),
    "r1-p3": ("inventory.py",),
    "r2-p1": ("models.py", "repository.py", "routes.py", "services.py", "tests/test_registration.py"),
    "r2-p2": ("inventory.py", "models.py", "orders.py", "payments.py", "repository.py", "tests/test_orders.py"),
}


class StartTests(unittest.TestCase):
    def run_cli(self, home: str, *args: str) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["HOME"] = home
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            cwd=ROOT,
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_each_id_copies_only_one_exercise_without_private_docs(self):
        with tempfile.TemporaryDirectory() as temp:
            for problem_id, required_files in PROBLEMS.items():
                with self.subTest(problem_id=problem_id):
                    result = self.run_cli(temp, problem_id)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    workspace = Path(temp) / "cic-practice" / problem_id
                    expected_files = {Path(path).as_posix() for path in required_files}
                    actual_files = {path.relative_to(workspace).as_posix() for path in workspace.rglob("*") if path.is_file() and path.name not in {"AGENTS.md", "copilot-instructions.md"}}
                    self.assertEqual(actual_files, expected_files)
                    self.assertTrue((workspace / "AGENTS.md").is_file())
                    self.assertTrue((workspace / ".github/copilot-instructions.md").is_file())
                    self.assertFalse((workspace / "assignments").exists())
                    self.assertFalse((workspace / ".git").exists())
                    self.assertFalse(list(workspace.rglob("SOLUTION.md")))
                    expected_command = "python validator.py" if problem_id == "r1-p1" else None
                    if expected_command:
                        self.assertIn(expected_command, result.stdout)
                    self.assertFalse(any(path.is_symlink() for path in workspace.rglob("*")))

    def test_unknown_id_is_rejected_without_creating_workspaces(self):
        with tempfile.TemporaryDirectory() as temp:
            result = self.run_cli(temp, "r3-p1")
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse((Path(temp) / "cic-practice").exists())

    def test_existing_workspace_is_never_overwritten(self):
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
