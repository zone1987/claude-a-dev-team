# Command frontmatter

A command is a skill the human triggers. Custom commands and skills are the same mechanism now, so
everything in `zcf-skill-authoring` applies; this file covers what differs. Rules: `AGENT-01`,
`COMP-01`.

## The five fields

```yaml
---
name: zcf-validate
description: Runs every blocking rule against a plugin and reports each violation with its file, line and rule id.
argument-hint: <plugin> [--strict] [--json]
allowed-tools: Read, Glob, Grep, Bash
model: haiku
---
```

- **`name`** matches the file, so `/zcf-validate` is what the human types.
- **`description`** is what the `/` menu shows. A command is invoked by hand, so this line is read by
  a person, not matched by a model: name the outcome, not the triggers.
- **`argument-hint`** shows during autocomplete. Spell the real flags; a hint that lies costs more
  than none.
- **`allowed-tools`**, never `tools`. This is the field commands use, and it pre-approves those tools
  for the invoking turn so the human is not prompted mid-run.
- **`model`**: `haiku` for mechanical and template-driven work, `sonnet` where the command judges.

## Arguments

`$ARGUMENTS` carries everything after the command name. Named positional arguments are possible with
the `arguments` field, but this marketplace uses `$ARGUMENTS` and parses inside the body, because one
field is easier to keep honest than a positional contract.

Two forms this marketplace deliberately leaves unused, both of which the platform supports:

- **`!` prefix** runs a bash command and injects its output. Powerful and easy to make non-obvious;
  a script named in the body is easier to audit.
- **`@file`** embeds a file's content. It puts the whole file in context whether or not the run needs
  it, which is the cost progressive disclosure exists to avoid.

## The body

Four movements, in order:

1. **One sentence naming the job**, with `$ARGUMENTS` in it, so the run's subject is unambiguous.
2. **Classify the input** where the command accepts more than one kind. Say how to tell them apart.
3. **The steps**, numbered, each ending on a checkable condition. Where a step is a script, name the
   script rather than describing what it would do.
4. **The output shape**, so two runs of the same command look the same.

Close on a sentence that forbids invention: **"Report only what the files contain. Invent nothing."**
A command that fills a gap with a plausible answer is worse than one that reports the gap, because
the reader cannot tell which they got.

## When a command is earned

A repeated task with varying arguments, or an action whose timing the human should own. A step
sequence people type out by hand is a command that was never written. `COMP-01`

The inverse also holds: a command nobody invokes is pure cost, since it sits in the `/` menu and in
the slash-command budget. `COMP-05`

## Source

[Skills](https://code.claude.com/docs/en/skills) for the merged command mechanism,
[frontmatter reference](https://code.claude.com/docs/en/skills#frontmatter-reference) for the fields,
and [pass arguments to skills](https://code.claude.com/docs/en/skills#pass-arguments-to-skills),
retrieved 2026-08-21.
