# Using AI as a debugging helper

## Keep yourself in the driver’s seat

Ask AI to help you understand one part of the problem at a time: restate a requirement, map a request path, reason through an input, or suggest a regression test. Make the edits yourself and inspect every change. You should be able to explain the final behavior and decisions without relying on the chat.

Useful prompts:

- “For this requirement, what cases should I write down before looking at the implementation?”
- “Trace this request through the files I can access. Where does this value change?”
- “For input X, the code returns A and I expect B. What should I inspect next? Don’t edit files.”
- “What assertion would prove this invariant, and what incorrect implementation would it catch?”
- “Review my diff for behavior that contradicts this requirement. Point to evidence and suggest a counterexample.”

Provide the relevant assignment text yourself when needed. The assignment is the source of truth; source code and tests can both be wrong. Ask AI to show its reasoning in terms of the code or observed output, then verify it.

## What the helper can see

The launcher copies one exercise's code, tests, `AGENTS.md`, and Copilot instructions to a predictable directory under your home folder. It leaves the PR or ticket document in the repository so you can read it separately. This limits accidental AI context in tools scoped to the generated workspace, but it is not a security boundary. An AI tool with unrestricted filesystem access may still read other directories. Check the tool's configured workspace, indexing, and permissions.

`AGENTS.md` is guidance, not an access control system. An assistant may not support it, may interpret it imperfectly, or may have broader tools. Instructions cannot prevent reading or writing files when the tool itself permits that.

## Choose an appropriate mode

For this simulated interview, use **GitHub Copilot Ask mode**. Ask for explanation, investigation ideas, or test design. Avoid autonomous Agent/Edit modes during the exercise so you get practice making and reviewing the changes yourself.

More generally, read-only AI tools can explain and inspect available context. Editing-capable agents can change files and may run commands. Choose the mode that matches your practice goal, and check proposed edits yourself if you use one outside the simulation.
