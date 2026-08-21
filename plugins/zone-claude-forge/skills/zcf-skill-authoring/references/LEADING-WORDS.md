# Leading words, and steering by the positive

Two levers that decide how much behaviour a sentence buys.

## Leading words

A **leading word** is a compact concept already living in the model's pretraining that the agent
thinks with while running the document: *tight*, *seam*, *red*, *fog of war*, *tracer bullet*.
Repeated as a token and never as a sentence, it accumulates a distributed definition and anchors a
whole region of behaviour in the fewest tokens, because it recruits priors the model already holds.

It anchors twice:

- **In the body, execution**: the agent reaches for the same behaviour every time the word appears,
  and inside flat reference it focuses attention on a class of thing to look for.
- **In a pointer, invocation**: when the same word lives in your prompts, your docs and your
  codebase, the agent links that shared language to the material and reaches it more reliably.

Coining your own works if you define it clearly, but a made-up word recruits no priors: you pay in
definition tokens what a pretrained word gives free. Reach for an existing word first.

Hunt for passages that collapse into one token:

| Spelled out | Leading word |
|---|---|
| "fast, deterministic, low-overhead" | a **tight** loop |
| "a loop you believe in" | the loop goes **red** on the bug |
| "the public boundary you test at" | the **seam** |
| "the dim view of decisions you can tell are coming" | the **fog of war** |

You win twice: fewer tokens, and a sharper hook for the agent to hang its thinking on. Assume every
document is carrying restatements that leading words retire.

A leading word too weak to beat the default is a no-op. "Be thorough" when the agent is already
thorough-ish buys nothing; the fix is a stronger word, not a different technique.

## State the positive

Steering by prohibition drags the forbidden behaviour into context and makes it **more** available,
not less. *Don't think of an elephant*, and the elephant is all there is: the negation is a weak
modifier that the strongly-activated concept overruns, so the ban half-reads as an instruction.

Prompt the target instead:

| Prohibition | Positive |
|---|---|
| "do not invent fields" | "verify each field against the specification" |
| "don't write long descriptions" | "count the description; keep it under 200" |
| "never nest references" | "link every reference directly from `SKILL.md`" |

A prohibition earns its place only as a hard guardrail you cannot phrase positively, and even then
pair it with the positive target so attention lands on what to do.

**An anti-pattern needs a tell.** Naming a mistake is not enough; say how to recognise it. That is
why every judgement-bound rule in `rules.json` carries one.

## Source

Distilled from [mattpocock/skills](https://github.com/mattpocock/skills) `writing-for-agents`,
retrieved 2026-08-21. The documentation's related guidance is
[use consistent terminology](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices#use-consistent-terminology),
retrieved 2026-08-21.
