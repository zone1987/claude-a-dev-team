---
name: zcf-component-authoring
description: 'Authors Claude Code agents, slash commands and hooks.json for this marketplace. Use when writing an agents/*.md, a commands/*.md, or a UserPromptSubmit or PostToolUse hook.'
---

# Authoring agents, commands and hooks

Three components, three cost models. An agent runs in **its own context window**, so it is where bulk
work belongs. A command is a skill the human triggers. A hook is the only **deterministic** layer:
it cannot make Claude load a skill, but it can deny a tool call outright.

The full rule set is [`RULES.md`](../../RULES.md). The IDs below name the rules each section applies.

## Which component

| The need | Component | Why it fits |
|---|---|---|
| Bulk reading whose output compresses into a summary | agent | the parent pays for the summary, not the reading |
| A judgement that must not write | agent, read-only tools | least privilege makes the write impossible |
| A repeated task with varying arguments | command | `$ARGUMENTS`, and the human owns the timing |
| An action with side effects | command, or a skill with `disable-model-invocation` | Claude never triggers a deploy on its own |
| A deterministic rule worth catching as it happens | hook | the only layer that can block |
| A nudge toward the right skill | hook, `UserPromptSubmit` | injects context; it never guarantees a load |

`COMP-01` to `COMP-05` state when each is earned, and `AGENT-04` states when an orchestrator is not.

## Agents

Cheapest adequate model: `haiku` for mechanical scanning, `sonnet` where judgement is required,
`opus` for orchestration, migration and knowledge sync. A subagent's context window is sized by
**its own** model, not the parent's. `AGENT-06`

- **Least privilege on `tools`**, and `disallowedTools` where a capability must be impossible rather
  than merely absent: it is applied **before** `tools`. `AGENT-07`
- **`maxTurns`** bounds an agent that iterates over a work list. Nothing else stops a loop. `AGENT-08`
- **`skills:` injects full content at startup**, so preload two or three at most, and name them in
  the body as well: as a teammate only `tools` and `model` apply, so `skills:` is an optimisation and
  never the mechanism. `AGENT-03`
- **Omit `hooks`, `mcpServers` and `permissionMode`**: ignored for plugin agents, so writing them
  creates false confidence. `AGENT-02`

Read [`AGENT-FRONTMATTER.md`](references/AGENT-FRONTMATTER.md) before setting any field.

## Commands

Five fields, always: `name`, `description`, `argument-hint`, `allowed-tools`, `model`. Note
`allowed-tools`, not `tools`. Take input through `$ARGUMENTS`. Close on a sentence that forbids
invention, because a command that reports what it did not find is worse than one that reports
nothing: [`COMMAND-FRONTMATTER.md`](references/COMMAND-FRONTMATTER.md).

## Hooks

Two facts decide every hook here.

**A hook cannot force a skill to load.** No such mechanism exists. It injects context or denies a
call. `HOOK-06`

**A timed-out `PreToolUse` hook does not block.** The call continues through the normal permission
flow, so a slow gate is not a late gate, it is an **open** one. Test the path first and return early,
before doing anything expensive. `HOOK-04`

The shapes that follow from that, plus every event and its matcher support, are in
[`HOOK-EVENTS.md`](references/HOOK-EVENTS.md). Two traps worth naming here because both are silent:
`additionalContext` belongs at the **top level** of the JSON, never inside `hookSpecificOutput`; and
`UserPromptSubmit` supports **no** matcher, so match inside the script. `HOOK-01/02`

## Reference map

- **[AGENT-FRONTMATTER.md](references/AGENT-FRONTMATTER.md)**: every subagent field, the ones plugins may not
  use, model and effort selection, and the concurrency and depth limits.
- **[COMMAND-FRONTMATTER.md](references/COMMAND-FRONTMATTER.md)**: the five fields, argument handling, and the
  body shape that keeps a command from inventing.
- **[HOOK-EVENTS.md](references/HOOK-EVENTS.md)**: all events with matcher support, exit-code semantics,
  the deny shape, timeouts, and the JSON a hook receives on stdin.
- **[MODEL-SELECTION.md](references/MODEL-SELECTION.md)**: which model and effort a component earns, with the
  resolution order that decides what actually runs.
- **[TEMPLATES.md](references/TEMPLATES.md)**: skeletons for an agent, a command and each hook shape.

## Related

Call the Skill tool with "zcf-skill-authoring" for `SKILL.md` itself.

## Source

Distilled from the Claude Code documentation:
[subagents](https://code.claude.com/docs/en/sub-agents),
[hooks](https://code.claude.com/docs/en/hooks) and
[plugins reference](https://code.claude.com/docs/en/plugins-reference), retrieved 2026-08-21.
Rule wording and citations live in [`rules.json`](../../rules.json) v1.0.0.
