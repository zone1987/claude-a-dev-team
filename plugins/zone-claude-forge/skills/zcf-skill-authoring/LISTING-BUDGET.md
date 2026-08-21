# The listing budget

Claude Code loads a listing of skill names and descriptions into the system prompt. That listing has
a hard character budget, and what happens when it overflows decides how a skill must be written.
Rules: `BUDGET-01` to `BUDGET-06`, `COUNT-01`.

## Contents

- [The arithmetic](#the-arithmetic)
- [What overflow does](#what-overflow-does)
- [The four levers](#the-four-levers)
- [Measure the working set](#measure-the-working-set)
- [Compaction](#compaction)
- [Source](#source)

## The arithmetic

- **Cost per entry** = `len(description) + len(when_to_use) + 109`. The 109 is measured overhead
  (XML tags, name, location), not documented: see
  [anthropics/claude-code#64606](https://github.com/anthropics/claude-code/issues/64606).
- **Budget** = 1 % of the context window, so **8,000 characters at 200k**. Raisable by the user with
  `skillListingBudgetFraction` or `SLASH_COMMAND_TOOL_CHAR_BUDGET`, which is an escape hatch rather
  than a licence.
- **Per-entry cap** = 1,536 characters regardless of budget, configurable with
  `skillListingMaxDescChars`.
- **A `disable-model-invocation` skill still contributes its name**, because the listing always
  contains every skill name. It is cheap, not free. `BUDGET-01`

## What overflow does

> When the listing overflows, Claude Code drops descriptions starting with the skills you invoke
> least, so the skills you use most keep their full text.

Overflow does not punish the longest skill. It silences the **rarest** one, and a skill without a
description never auto-activates again. So a specialist skill needed twice a year is the first to go
quiet, and it fails at exactly the moment it was the only thing that could have helped.

The user cannot repair it either: `skillOverrides`, the setting that would collapse a skill to
name-only, **does not reach plugin skills**. Staying inside the budget is the author's job.

## The four levers

In the order to reach for them:

1. **Cut the description, not the knowledge.** Reference files cost nothing until read, so depth is
   free and only the pointer is dear. `octo-api` documents 7,736 lines for 2,392 characters.
2. **Choose invocation deliberately.** `disable-model-invocation: true` removes the description from
   context and a router restores reachability. The largest single lever.
3. **Merge by domain.** Two skills that always fire together spend two descriptions and two
   overheads for one concept. `COUNT-01`
4. **Sharpen the anchors.** A description that fires on the wrong prompt costs a full skill load,
   which dwarfs the entry it saved.

## Measure the working set

A per-plugin percentage is misleading, because a session enables several plugins that share one
budget:

```bash
python3 scripts/validate_plugin.py --working-set <plugin> <plugin> <plugin>
```

That total is the number that actually overflows. A plugin at 30 % is fine alone and ruinous beside
three others. `BUDGET-02`

Two in-session checks: `/doctor` estimates the listing's cost and its biggest contributors, and the
Skills row in `/context` reports the size **after** the budget is applied, so it matches what the
model received. `--debug` logs the overflow warning.

## Compaction

> Claude Code re-attaches the most recent invocation of each skill after the summary, keeping the
> first 5,000 tokens of each. Re-attached skills share a combined budget of 25,000 tokens.

The budget fills from the most recently invoked skill, so older ones can be dropped entirely. Two
consequences for writing: put load-bearing content first, because anything past the first 5,000
tokens does not come back, and expect a long session to have lost the earliest skills. `BUDGET-06`

Once a skill loads, its content stays in context for the rest of the session, so every line is a
recurring cost. State what to do, not how you arrived at it.

## Source

[Skill descriptions are cut short](https://code.claude.com/docs/en/skills#skill-descriptions-are-cut-short),
[skill content lifecycle](https://code.claude.com/docs/en/skills#skill-content-lifecycle) and
[override skill visibility from settings](https://code.claude.com/docs/en/skills#override-skill-visibility-from-settings),
retrieved 2026-08-21. The 109-character overhead is measured, not documented.
