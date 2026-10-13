# A practical debugging workflow

## READ SPEC → INSPECT CODE → FIND GAPS → FIX + TEST

### 1. Read the specification

Write down inputs, expected outcomes, boundary cases, and rules that must stay true. Note ambiguity instead of guessing. For these exercises the assignment document is separate from the starter workspace; keep it available to yourself and share only the relevant details with AI.

### 2. Inspect the code

Start at the function or request entry point named by the behavior. In a multi-file exercise, follow the data through each caller, service, and repository. Read the tests too, but treat them as claims to evaluate rather than as the specification.

### 3. Find the gap

Compare expected behavior with an observed result. Reproduce one concrete case and form a hypothesis about the responsible condition or state transition. Ask what invariant should hold before and after the operation.

### 4. Fix and test

Add or correct a focused regression test, make the smallest change that satisfies the requirement, then run the full exercise suite. Inspect the diff and try nearby edge cases. Be ready to explain what was wrong, why the change addresses it, and what the tests do and do not establish.

## Keep the reasoning visible

Before editing, jot down the expected behavior, relevant data or request flow, and the first test that could distinguish the code's behavior from the requirement. Update that note as evidence changes your hypothesis.
