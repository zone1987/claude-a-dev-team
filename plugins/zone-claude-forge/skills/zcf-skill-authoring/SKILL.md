---
name: zcf-skill-authoring
description: 'Authors SKILL.md files for this marketplace: listing budget, description pattern, progressive disclosure. Use when writing a SKILL.md, a skill description, or skill frontmatter.'
---

# Authoring a SKILL.md

A skill costs its description on **every turn** and its body on every turn after it loads. Write for
that ratio: a sharp pointer, a short map, and depth in reference files that cost nothing until read.

The full rule set is [`RULES.md`](../../RULES.md), generated from `rules.json`. The IDs below name
the rules each step applies, so a rule has one authoritative wording. Never restate a rule here.

## The order that avoids rework

1. **Name the domain and its anchors first.** The description is the hardest part and constrains
   everything else. An anchor is a word that identifies **this** domain and no other: a brand name,
   a filename, an exact identifier. Bind a generic noun to one, never ship it bare. `ANCHOR-01/02`
2. **Choose invocation before writing a line.** Model-invoked spends its description permanently in
   exchange for Claude reaching it unprompted. `disable-model-invocation: true` spends nothing but
   the name, and only the human reaches it. Pick model-invocation only when Claude or another skill
   must reach the skill on its own. `INVOKE-01`
3. **Write the description, then count it.** `python3 -c "print(len('…'))"`. The pattern is
   `<Statement>. Use when <anchor>, <anchor>.` Key use case first, because the entry truncates from
   the end. `DESC-01..04`, `BUDGET-03/04`
4. **Draft the body as a map, not the territory.** Purpose in one to three sentences, the core
   model, then a reference map. Load-bearing content first: after compaction only the first 5,000
   tokens come back. `SIZE-01`, `BUDGET-06`
5. **Push depth into flat siblings.** `SCREAMING-CASE.md` beside `SKILL.md`, never a subdirectory.
   Link every one from `SKILL.md` with a note on what it holds. **Name each file after what is in
   it**, so the name alone tells a reader whether to open it. `DEPTH-01`, `REF-01`, `REF-03`,
   `LINK-01`
6. **Close on `## Source`** with the upstream URL, the version, hash or commit, and the date.
   `SRC-01`, `SRC-06`
7. **Run the gate.** `python3 scripts/validate_plugin.py --plugin <name> --strict`. A finding names
   its rule ID; look it up in `RULES.md` rather than guessing at the intent.

## What earns its tokens

Only what changes behaviour against the model's default. A sentence the model would follow anyway
pays load to say nothing, and the test is settled by running the skill, not by arguing about it.
Read [`PRUNING.md`](PRUNING.md) before deciding a paragraph is necessary.

## Frontmatter

Claude Code accepts far more fields than this marketplace uses, and six of them are all that stay
portable outside it. Both facts matter when choosing one:
[`FRONTMATTER.md`](FRONTMATTER.md). `FM-01/02`

## Reference map

- **[FRONTMATTER.md](FRONTMATTER.md)**: every documented field, what it does, and which six survive
  outside Claude Code. Read before adding any field beyond `name` and `description`.
- **[DESCRIPTION-PATTERN.md](DESCRIPTION-PATTERN.md)**: the pattern, worked examples, and how to
  bind a generic noun to an anchor that cannot collide.
- **[LISTING-BUDGET.md](LISTING-BUDGET.md)**: the arithmetic, what overflow does, and the four
  levers in the order to reach for them.
- **[DISCLOSURE.md](DISCLOSURE.md)**: the information hierarchy, the branching test for what to
  disclose, and why one level deep is a mechanism rather than a preference.
- **[COMPLETION-CRITERIA.md](COMPLETION-CRITERIA.md)**: how to end a step so the agent can tell done
  from not-done, and how demand drives the legwork.
- **[LEADING-WORDS.md](LEADING-WORDS.md)**: anchoring behaviour in one pretrained token, and why a
  prohibition makes the forbidden behaviour more available rather than less.
- **[PRUNING.md](PRUNING.md)**: single source of truth, the no-op test, sprawl, and what the
  environment already answers.
- **[SKILL-TEMPLATE.md](SKILL-TEMPLATE.md)**: the skeleton to copy, with the measuring commands.

## Related

Call the Skill tool with "zcf-component-authoring" for agents, commands and hooks. For the anchor
inventory across all plugins, tell the user to run `/zone-claude-forge:zcf-anchor-design`.

## Source

Distilled from the Claude Code documentation:
[skills](https://code.claude.com/docs/en/skills) and
[skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices),
retrieved 2026-08-21. Rule wording and citations live in
[`rules.json`](../../rules.json) v1.0.0; writing levers are distilled from
[mattpocock/skills](https://github.com/mattpocock/skills) `writing-for-agents`, retrieved 2026-08-21.
