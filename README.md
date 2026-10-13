# Coding Interview Club: Bloomberg AI Interview Practice

Five original, unofficial debugging exercises for the Coding Interview Club (CIC). These simulations are not actual or leaked Bloomberg interview questions and do not describe official requirements or guarantee an interview format.

## Choose an exercise

| ID | Exercise | Practice focus |
| --- | --- | --- |
| `r1-p1` | Student Code Validator | Input validation and meaningful tests |
| `r1-p2` | Event Scheduler | Interval boundaries and side effects |
| `r1-p3` | Cappy's Snack Inventory | State changes and invariants |
| `r2-p1` | Cappy Event Registration System | Request flow, status, and capacity |
| `r2-p2` | Cappy Orders | Cross-module state, failures, and retries |

Read the matching file under `assignments/` separately. Create an isolated workspace for one exercise:

```sh
python start.py r1-p1
```

The launcher places it at `~/cic-practice/<id>`. For Round 1, run the source file directly, for example `python validator.py`. Its embedded `unittest` suite may fail because the starter has intentional defects. For Round 2, run `python -m unittest discover -s tests -v` from that exercise directory.

Round 1 is single-file PR review. Round 2 is a small, independent multi-file ticket investigation. Each exercise can be started on its own.

## A useful workflow

**READ SPEC → INSPECT CODE → FIND GAPS → FIX + TEST.** Reproduce one concrete case, trace the relevant function or request flow, compare each test assertion with the assignment, then make a focused change. Passing tests do not prove correctness when tests are incomplete or misleading. Add regression coverage and explain why your fix satisfies the requirement.

## Use AI as a helper

The generated workspace contains only the selected exercise and AI instructions; assignment files remain outside it. This helps keep the assignment out of an assistant's workspace context, but does not guarantee isolation if the AI tool can read other files on your computer. `AGENTS.md` and Copilot instructions guide an assistant; they cannot enforce filesystem access restrictions.

Ask AI to trace a value, reason through a specific input, or suggest a regression test. Have it point to evidence, then verify that evidence yourself. Keep the edits and final explanation yours. For the simulated interview, use GitHub Copilot **Ask mode**, not autonomous Agent/Edit mode.

## Learning resources

- [Python `unittest`](https://docs.python.org/3/library/unittest.html)
- [GitHub Copilot prompt engineering](https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering)
- [Martin Fowler: Test-Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html)
- [System Design Primer](https://github.com/donnemartin/system-design-primer)

## Solutions and credit

Corrected solutions, regression tests, and explanations are kept on a separate local `solutions` branch for workshop staff. It must remain unpublished until after the workshop and explicit authorization to publish. Created for the **Coding Interview Club**; Cappy is the club's capybara mascot.
