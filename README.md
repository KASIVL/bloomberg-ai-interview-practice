# Coding Interview Club: Bloomberg AI Interview Practice

A small workshop repository from the Coding Interview Club (CIC). It contains five original debugging exercises inspired by AI-assisted software engineering practice. These are educational simulations, not actual or leaked Bloomberg interview questions or official interview requirements.

## Get started

Clone the repository, then open **one exercise folder** in VS Code. Read its matching PR or Ticket from `assignments/` on GitHub. Assignment documents stay outside the exercise folder so you can decide what requirement details to share with your AI helper.

```sh
git clone https://github.com/ehuerta6/bloomberg-ai-interview-practice.git
cd bloomberg-ai-interview-practice
code round-1/problem-01
```

Python's standard library is all you need. No install or setup step is required.

## Pick a problem

| ID | Exercise | Round | Assignment |
| --- | --- | --- | --- |
| `r1-p1` | Student Code Validator | Single-file PR review | [`assignments/r1-p1.md`](assignments/r1-p1.md) |
| `r1-p2` | Event Scheduler | Single-file PR review | [`assignments/r1-p2.md`](assignments/r1-p2.md) |
| `r1-p3` | Cappy's Snack Inventory | Single-file PR review | [`assignments/r1-p3.md`](assignments/r1-p3.md) |
| `r2-p1` | Cappy Event Registration System | Multi-file engineering ticket | [`assignments/r2-p1.md`](assignments/r2-p1.md) |
| `r2-p2` | Cappy Orders | Multi-file engineering ticket | [`assignments/r2-p2.md`](assignments/r2-p2.md) |

Run the exercise from its own folder:

```sh
(cd round-1/problem-01 && python validator.py)
(cd round-1/problem-02 && python scheduler.py)
(cd round-1/problem-03 && python inventory.py)
(cd round-2/problem-01 && python test_events.py)
(cd round-2/problem-02 && python test_orders.py)
```

The Round 1 files include both implementation and `unittest` tests. Round 2 test files can be run directly from the problem folder.

## Debug with care

Starter tests may fail because the code contains intentional bugs. Some assertions are misleading, unrelated, or incomplete, so a passing suite does not prove the implementation is correct. Compare each test with the assignment, reproduce behavior, and add a regression test. Make and explain the code changes yourself.

Each exercise's `AGENTS.md` gives the AI helper progressive hints and asks it to inspect only that exercise's code and tests. It asks the assistant not to read assignments or solutions, edit files, or provide a full answer. These instructions guide behavior; they do not enforce filesystem access. Open only the selected exercise folder in your editor and check what files your AI tool can access. Share the relevant requirement yourself when you want help reasoning about it.

## Learning resources

- [Python `unittest`](https://docs.python.org/3/library/unittest.html)
- [GitHub Copilot prompt engineering](https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering)
- [Martin Fowler: Test-Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html)

Corrected solutions and explanations are kept on a separate local branch for workshop staff. They will be published only after the workshop and explicit authorization. Created for the **Coding Interview Club**; Cappy is the club's capybara mascot.
