# Template

Copy, fill, measure, validate.

## The skeleton

```markdown
---
name: <prefix>-<domain>
description: '<Statement>. Use when <anchor>, <anchor>, or <anchor>.'
---

# <Title>

<One to three sentences of purpose. Load-bearing content first.>

## <Core model, endpoints, or the decision this skill turns on>

- **<term>** (<type>, <required|optional>): <meaning>.

## Reference map

- **[SOMETHING.md](SOMETHING.md)**: <what it holds, so Claude can decide whether to open it>.

## Related

Call the Skill tool with "<other-skill>" for <topic>.

## Source

Distilled from [<upstream>](<url>) — <version, sha or file>, retrieved <YYYY-MM-DD>.
```

A user-invoked skill adds one line, and its description becomes human-facing: a one-line summary
with the trigger list stripped, because no model reads it.

```yaml
disable-model-invocation: true
```

## Measure

```bash
# the description, before anything else
python3 -c "print(len('<Statement>. Use when <anchor>, <anchor>.'))"     # <= 200

# body length, excluding frontmatter
awk 'f{n++} /^---$/{c++; if(c==2) f=1} END{print n}' SKILL.md            # <= 120

# the gate: every blocking rule at once
python3 scripts/validate_plugin.py --plugin <plugin> --strict

# the number that actually overflows
python3 scripts/validate_plugin.py --working-set <plugin> <plugin> <plugin>
```

## Done when

- The description is under 200 characters, third person, key use case first, and every anchor in the
  `Use when` clause is a brand word, a filename, a path shape or an exact identifier.
- The body is under 120 lines, with load-bearing content in the first screen.
- Every reference file is a flat `SCREAMING-CASE.md` sibling, linked from `SKILL.md` with a note on
  what it holds, and any file over 100 lines carries a table of contents.
- `## Source` names the upstream URL and a version, sha or date.
- `validate_plugin.py --strict` exits 0.
- The intended prompts reach the skill, and prompts from a neighbouring domain leave it alone.

## Source

The template assembles the rules in [`RULES.md`](../../RULES.md); each check above names the rule it
enforces. Field validity comes from the
[frontmatter reference](https://code.claude.com/docs/en/skills#frontmatter-reference), retrieved
2026-08-21.
