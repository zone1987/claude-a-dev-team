# Steps and completion criteria

Every step ends on a **completion criterion**: the condition that tells the agent the work is done.
Two properties make it a lever, and both are written into the wording rather than added afterwards.

## Clarity

Can the agent tell done from not-done? A vague bound invites **premature completion**: ending the
step before it is genuinely finished, attention slipping to *being done*.

| Vague | Checkable |
|---|---|
| "understanding reached" | "every open question in the list has an answer" |
| "the docs are covered" | "every page in the sitemap maps to a reference file" |
| "the description is good" | "`len(description) <= 200` and the gate reports no `DESC-*`" |

The visible steps still ahead supply the pull toward finishing early; the criterion's clarity is the
resistance. Defend in that order: **sharpen the bound first**, because it is local and cheap. Only if
it is irreducibly fuzzy *and* you observe the rush, split the sequence to hide the later steps, and
note that hiding works only across a real context boundary. An inline call leaves the later steps in
context and clears nothing.

## Demand

How much the criterion requires. "Every modified model accounted for" forces thorough work where
"produce a change list" does not. Demand drives **legwork**: the digging the agent does inside the
work, latent in the wording rather than written as its own step.

Demand is not step-bound. "Every rule applied" binds a body of flat reference just as "every step
done" binds a sequence, which is how an all-reference document still carries an exhaustiveness bar.

**The strongest criteria are both checkable and exhaustive.** A count is the cheapest way to get
both: 65 operations, 39 pages, 254 fields. A number the agent can compare against is worth a
paragraph of exhortation.

## Prefer a command

Where a criterion can be a command, make it one. `validate_plugin.py --strict` is a completion
criterion with no interpretation left in it, and a step that ends on an exit code cannot be talked
into being finished.

## Source

Distilled from [mattpocock/skills](https://github.com/mattpocock/skills) `writing-for-agents`,
retrieved 2026-08-21. The documentation's own version of this lever is the workflow checklist in
[use workflows for complex tasks](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices#use-workflows-for-complex-tasks),
retrieved 2026-08-21.
