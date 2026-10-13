#!/usr/bin/env python3
"""Create an isolated workspace for one CIC debugging exercise."""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROBLEMS = {
    "r1-p1": ("round-1/problem-01", "python validator.py"),
    "r1-p2": ("round-1/problem-02", "python scheduler.py"),
    "r1-p3": ("round-1/problem-03", "python inventory.py"),
    "r2-p1": ("round-2/problem-01", "python -m unittest discover -s tests -v"),
    "r2-p2": ("round-2/problem-02", "python -m unittest discover -s tests -v"),
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Start one isolated CIC practice exercise.")
    parser.add_argument("problem", choices=sorted(PROBLEMS), help="exercise ID, such as r1-p1")
    args = parser.parse_args()
    relative_path, run_command = PROBLEMS[args.problem]
    source = ROOT / relative_path
    destination = Path.home() / "cic-practice" / args.problem
    if destination.exists():
        print(f"Workspace already exists: {destination}\nMove or rename it before starting again.", file=sys.stderr)
        return 1

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(
        source,
        destination,
        symlinks=False,
        ignore=shutil.ignore_patterns("SOLUTION.md", "__pycache__", "*.pyc"),
    )
    shutil.copy2(ROOT / "AGENTS.md", destination / "AGENTS.md")
    github = destination / ".github"
    github.mkdir(exist_ok=True)
    shutil.copy2(ROOT / ".github" / "copilot-instructions.md", github / "copilot-instructions.md")
    print(f"Workspace created: {destination}")
    print(f"Run this exercise's tests from that directory:\n  {run_command}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
