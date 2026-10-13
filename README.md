# Coding Interview Club: Bloomberg AI Interview Practice

The Coding Interview Club created these five Python exercises to help students practice debugging with an AI helper. Their workflow draws on one club member's prep and mock-interview notes. The exercises are original practice, not actual or leaked Bloomberg questions or official interview requirements. Formats and tools can vary, so follow the instructions you receive.

## Get started

Clone the repository:

```sh
git clone https://github.com/ehuerta6/bloomberg-ai-interview-practice.git
cd bloomberg-ai-interview-practice
```

Choose one exercise below. Read its PR or Ticket on GitHub (or in `assignments/` in your clone), then open only that exercise folder in VS Code with **File → Open Folder**. If the VS Code command-line tool is enabled, `code round-1/01-code-validator` opens the first exercise from the repository root. Keeping the assignment outside the folder you open helps limit what your AI tool sees.

| ID | Exercise | Assignment | Open this folder | Run from that folder |
| --- | --- | --- | --- | --- |
| `r1-p1` | Student Code Validator | [`r1-01-code-validator.md`](assignments/r1-01-code-validator.md) | `round-1/01-code-validator` | `python validator.py` |
| `r1-p2` | Event Scheduler | [`r1-02-event-scheduler.md`](assignments/r1-02-event-scheduler.md) | `round-1/02-event-scheduler` | `python scheduler.py` |
| `r1-p3` | Cappy's Snack Inventory | [`r1-03-snack-inventory.md`](assignments/r1-03-snack-inventory.md) | `round-1/03-snack-inventory` | `python inventory.py` |
| `r2-p1` | Cappy Event Registration System | [`r2-01-event-registration.md`](assignments/r2-01-event-registration.md) | `round-2/01-event-registration` | `python test_event_registration.py` |
| `r2-p2` | Cappy Orders | [`r2-02-order-processing.md`](assignments/r2-02-order-processing.md) | `round-2/02-order-processing` | `python test_order_processing.py` |

For example, from a terminal at the repository root, start Round 1, Problem 1 with:

```sh
cd round-1/01-code-validator
python validator.py
```

If you opened that problem folder directly in VS Code, its terminal is already there; run `python validator.py`. The commands below use `python`. On some systems, use `python3` instead. The exercises use Python's standard library, so no package installation or virtual environment is needed.

## What you'll practice

Round 1 is pull request review in a single Python file. The implementation and `unittest` tests are together in that file. Round 2 gives you a small multi-file codebase and an engineering ticket; trace how a request and its state move between modules.

Use this sequence: **Read the assignment. Inspect the code. Find a gap. Fix and test it.** Try a concrete input, check what the tests actually assert, and add a regression test for the behavior you investigate. Some starter tests are meant to fail. Others may be misleading, unrelated, or incomplete, so passing tests alone do not prove the code is right.

## Work with AI

Use AI to explain a function or traceback, trace a value through the code, or help think of a test. For example: “For this input, the code returns X. What should I inspect to understand why?” Ask it to point to evidence, then check that evidence yourself. Make the changes and explain your reasoning; the AI should help you investigate, not do the exercise for you.

The exercise's `AGENTS.md` asks the helper to read only that folder, avoid searching elsewhere for assignments or solutions, offer hints gradually, and leave all edits to you. These instructions guide behavior; they cannot restrict filesystem access, so an AI tool may still be able to read other folders. Open only the selected exercise in your editor and choose a read-only or non-editing AI mode; keep edit or agent mode off. Check the tool's access, and share the relevant assignment details yourself when you want help reasoning about them.

## Resources

- [Python `unittest`](https://docs.python.org/3/library/unittest.html)
- [HackerRank: AI Assistant in Interviews](https://candidatesupport.hackerrank.com/articles/6665907643-ai-assistant-in-interviews)
- [GitHub Copilot prompt engineering](https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering)
- [GitHub Copilot: Explore a codebase](https://docs.github.com/en/copilot/tutorials/explore-a-codebase)
- [Martin Fowler: Test-Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html)

Corrected solutions and explanations are kept on a separate local branch for workshop staff. They will be published after the workshop, with authorization. Cappy, the club's capybara, appears in a few exercise names.
