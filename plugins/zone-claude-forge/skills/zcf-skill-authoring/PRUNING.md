# Pruning

What to delete, and how to tell. A loaded skill is a recurring cost on every turn, so a line that
changes nothing is a line paid for repeatedly.

## Hunt no-ops

A **no-op** is an instruction the model already obeys by default. It pays load to say nothing.

The test: **does this sentence change behaviour against the default?** It is model-relative, not
reader-relative, so two people disagreeing about a no-op disagree about the default, and they settle
it by **running the document**, not by debate.

When a sentence fails the test, delete the whole sentence rather than trimming its words. Trimming
leaves a shorter no-op.

Common no-ops in this marketplace's own drafts:

- "Be careful and thorough." The agent is already thorough-ish; a stronger word or a count is the fix.
- "Read the file before editing it." Already the default.
- "Use good judgement." Names no behaviour.
- Explaining what an API or a file format *is*, when Claude already knows.

## Single source of truth

Keep each meaning in one authoritative place, so changing the behaviour is a one-place edit.
**Duplication** costs maintenance and tokens, and it inflates a meaning's prominence past its real
rank on the hierarchy.

This is why a skill here names a rule ID instead of restating the rule: `rules.json` owns the wording,
`RULES.md` renders it, and the skill points. Duplication is the accidental inverse of a leading word,
which repeats a **token** on purpose and never the meaning.

## The environment is a source of truth

`package.json` scripts, config files, the directory layout, `--help` output: a document that restates
them is a **cache**, and a cache earns its load only when the lookup is expensive.

- **Cache** what the agent cannot find by looking: the unwritten convention, the reason behind a
  choice, the gotcha no config confesses.
- **Leave** the one-file, one-command lookups to the environment, where they cannot go stale.

## Relevance

Check every line: does it still bear on what the document does? A line loses relevance by never
bearing on the task (mere exposition, or a branch that should be disclosed) or by going stale as the
world it describes changes.

Without a pruning discipline the default fate is **sediment**: stale layers that settle because adding
feels safe and removing feels risky, until you have to core down through them to find what is still
live. Shorter documents are easier to keep relevant, which is the compounding reason to prune early.

## What is never pruned

Facts. Distillation removes redundancy of expression, never information: a field without its type, an
enum value without its meaning, a parameter without its optionality are all gaps. Where the upstream
is silent, say so, because a blank reads as absence. `COV-04`

Shortening a body by deleting facts is the one optimisation the gate rejects.

## Source

[Concise is key](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices#concise-is-key)
and [skill content lifecycle](https://code.claude.com/docs/en/skills#skill-content-lifecycle),
retrieved 2026-08-21. The no-op test, single-source-of-truth and sediment framings are distilled from
[mattpocock/skills](https://github.com/mattpocock/skills) `writing-for-agents`, retrieved 2026-08-21.
