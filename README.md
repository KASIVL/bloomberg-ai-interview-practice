# Bloomberg AI Interview Practice

A practical debugging and code review pack from the **Coding Interview Club (CIC)**. Students investigate small pull requests and unfamiliar multi-file applications, then make and explain focused fixes.

> These are original educational simulations. They are not actual or leaked Bloomberg interview questions and do not describe official Bloomberg requirements or guarantee any interview format.

## Two rounds

- **Round 1: Pull request review and fix.** Three independent, single-production-file Python exercises. Review both code and tests, correct defects, and add regression coverage.
- **Round 2: Engineering tickets.** Two independent, multi-module Python applications. Trace request and state changes across the codebase, identify a root cause, and verify a focused fix.

| ID | Exercise | Focus | Estimated time |
| --- | --- | --- | --- |
| `r1-p1` | Student Code Validator | Data validation, boundaries, trustworthy tests | 20–30 min · Introductory |
| `r1-p2` | Event Scheduler | Half-open intervals, edge cases, side effects | 25–35 min · Introductory |
| `r1-p3` | Cappy's Snack Inventory | State, invariants, invalid input | 25–35 min · Intermediate |
| `r2-p1` | Cappy Event Registration System | Request flow, status, capacity invariants | 40–60 min · Intermediate |
| `r2-p2` | Cappy Orders | Cross-module state, failures, idempotency | 45–65 min · Intermediate |

## Select a problem

Open the matching assignment under [`assignments/`](assignments/) on GitHub and read it separately. Then create a workspace for just that exercise:

```sh
python scripts/start_problem.py r1-p1
```

Choose any ID in the table. The launcher copies that problem's starter source and tests, plus the student AI instructions, into `~/cic-practice/<id>`. Open that directory in your IDE and run:

```sh
python -m unittest discover -s tests -v
```

The assignment stays outside the generated workspace so students can decide what context to share with an AI helper. This reduces accidental exposure; it does **not** guarantee isolation if an AI tool can read files elsewhere on your computer. Review your tool's workspace and filesystem access.

## Practice workflow

Use **READ SPEC → INSPECT CODE → FIND GAPS → FIX + TEST**. Reproduce behavior with a concrete case, follow the relevant code path, check whether each assertion reflects the assignment, then make a focused change and explain why it works. See [the interview workflow](docs/interview-workflow.md) and [using AI as a helper](docs/using-ai.md).

A green suite can miss a bug: some starter tests are incomplete, misleading, or unrelated to the requirement. Read what each assertion proves, and add cases that would catch plausible incorrect behavior. Treat AI suggestions as hypotheses to verify against the spec and code.

For the simulated interview, ask AI for hints and investigation steps rather than having it edit the code. GitHub Copilot users should use **Ask mode**, not autonomous Agent/Edit mode. Repository instructions influence assistant behavior; they do not impose filesystem permissions.

## Solutions

Corrected solutions and meaningful regression suites are maintained on a separate local `solutions` branch for workshop staff. That branch must remain unpublished until the workshop is over and publication is explicitly authorized. The public starter branch contains no answer keys.

## Credit

Created for the **Coding Interview Club (CIC)**. Cappy, the club capybara, makes appearances in a few exercise names.
