#!/usr/bin/env python3
"""Copy one student workspace outside the repository."""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROBLEMS = {
    "r1-p1": "round-1/problem-01",
    "r1-p2": "round-1/problem-02",
    "r1-p3": "round-1/problem-03",
    "r2-p1": "round-2/problem-01",
    "r2-p2": "round-2/problem-02",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Create an isolated Coding Interview Club practice workspace.")
    parser.add_argument("problem", choices=sorted(PROBLEMS), help="problem identifier, such as r1-p1")
    args = parser.parse_args()
    source = ROOT / "starters" / PROBLEMS[args.problem]
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
    print("Run tests from that directory:")
    print("  python -m unittest discover -s tests -v")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
