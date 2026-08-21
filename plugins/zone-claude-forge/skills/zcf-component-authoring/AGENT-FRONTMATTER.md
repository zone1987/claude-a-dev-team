# Agent frontmatter

Every subagent field, the three a plugin may not use, and the limits a fan-out has to plan inside.
Rules: `AGENT-01` to `AGENT-09`.

## Contents

- [Every field](#every-field)
- [What a plugin agent may not set](#what-a-plugin-agent-may-not-set)
- [Preloading skills](#preloading-skills)
- [Tools](#tools)
- [Bounding the run](#bounding-the-run)
- [What a subagent does not inherit](#what-a-subagent-does-not-inherit)
- [Limits](#limits)
- [Source](#source)

## Every field

| Field | Required | What it does |
|---|---|---|
| `name` | yes | identifier; lowercase and hyphens, no colons except plugin scopes |
| `description` | yes | when Claude should delegate here |
| `tools` | no | allowlist; inherits every subagent tool when omitted |
| `disallowedTools` | no | denylist, **applied before `tools`** |
| `model` | no | `sonnet`, `opus`, `haiku`, `fable`, a full ID, or `inherit` (the default) |
| `maxTurns` | no | maximum agentic turns before stopping |
| `skills` | no | preloaded skills; **full content injected at startup** |
| `effort` | no | overrides session effort: `low` to `max` |
| `memory` | no | persistent memory scope: `user`, `project`, `local` |
| `background` | no | `true` keeps it in the background even when Claude asks for foreground |
| `isolation` | no | `worktree`, the only value a plugin agent may use |
| `color` | no | display colour in the task list |
| `initialPrompt` | no | auto-submitted first turn when run as a main session agent |
| `permissionMode` | no | **ignored for plugin agents** |
| `mcpServers` | no | **ignored for plugin agents** |
| `hooks` | no | **ignored for plugin agents** |

## What a plugin agent may not set

> For security reasons, plugin subagents don't support the `hooks`, `mcpServers`, or
> `permissionMode` frontmatter fields. These fields are ignored when loading agents from a plugin.

Writing one creates false confidence: the file reads as if the restriction applies, and nothing
enforces it. If a plugin genuinely needs them, the agent file has to be copied into `.claude/agents/`
by the user, which is outside what a plugin can ship. `AGENT-02`

## Preloading skills

> Skills to preload into the subagent's context at startup. The full skill content is injected, not
> only the description.

Two consequences. First, a generous list is a **large fixed cost per spawn**, not a convenience: keep
it to two or three. Second, when the same definition runs as a teammate, only `tools` and `model`
apply and the body is appended as instructions, so a preloaded skill silently disappears. **Name the
skills in the body as Skill-tool calls**, and treat `skills:` as an optimisation. `AGENT-03`

## Tools

Two mechanisms, and they compose:

- **`tools`** is an allowlist. Naming `Read, Grep, Glob` grants those and denies the rest.
- **`disallowedTools`** is a denylist applied **first**, so it wins. Use it where a capability must be
  impossible rather than merely unlisted: a read-only reviewer carries
  `disallowedTools: Write, Edit` as well as a narrow `tools`, and the two locks are independent.

MCP patterns work in both: `mcp__<server>`, `mcp__<server>__*`, and `mcp__*` to remove every MCP tool.

A **background** subagent is filtered further: apart from `Agent` and `ExitPlanMode`, it keeps every
MCP tool but only a fixed set of built-ins (`Read`, `Grep`, `Glob`, `Bash`, `Edit`, `Write`,
`WebFetch`, `WebSearch`, `Skill`, and a handful more). Do not rely on a niche built-in in the
background. `AGENT-07`

## Bounding the run

`maxTurns` is the only thing that stops an agent iterating past its usefulness. Set it wherever the
work is a list: extraction, auditing, scanning. `effort` overrides the session level, so a mechanical
scan need not inherit a session running at `high`. `AGENT-08`

## What a subagent does not inherit

- **Output style**: it runs its own system prompt.
- **Auto memory**: the main conversation's is not loaded.
- **Context window size**: sized by **its own** model, so a `haiku` subagent of an `opus` parent gets
  the smaller window.

It **does** inherit extended thinking: on in the session means on in the subagent, with no
per-subagent setting.

The built-in `Explore` and `Plan` agents skip `CLAUDE.md` and the parent's git status deliberately,
to keep research cheap. A custom agent does not, so a broad custom scanner costs more than `Explore`
for the same sweep.

## Limits

- **20 concurrent subagents** per session, then `Concurrent subagent limit reached`. Raise with
  `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`.
- **Spawn depth 3** below the main conversation, via `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`.

A command promising one subagent per page of a large docs site breaks against the first limit. Batch
instead. `AGENT-09`

## Model resolution order

What actually runs, highest first: `CLAUDE_CODE_SUBAGENT_MODEL`, the per-invocation `model` parameter,
this frontmatter, then the main conversation's model. A value outside an organisation's
`availableModels` allowlist is substituted, so a hard-coded model is a preference rather than a
guarantee.

## Source

[Subagents](https://code.claude.com/docs/en/sub-agents) and
[plugins reference](https://code.claude.com/docs/en/plugins-reference), retrieved 2026-08-21.
