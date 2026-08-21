# Model and effort

Which model a component earns, and what actually runs. Rules: `AGENT-06`, `AGENT-08`.

## The tiers

| Model | Earned by | Examples here |
|---|---|---|
| `haiku` | mechanical, template-driven, no judgement | scaffolding a file, scanning a tree, a lookup |
| `sonnet` | a focused specialist that judges | reviewing a component, distilling a page |
| `opus` | orchestration, migration, knowledge sync | extracting a whole docs site, a self-update agent |

The test for `opus` is not difficulty but **breadth of consequence**: work that decides the shape of
many later files, or that has to hold a large map in one head. A hard single-file judgement is
`sonnet` work.

The test for `haiku` is whether a wrong answer is **obvious**. Scaffolding is safe because a broken
template fails the gate immediately; a security judgement is not.

## Effort

`effort` (`low`, `medium`, `high`, `xhigh`, `max`) overrides the session level for that component.
A mechanical scan should not inherit a session running at `high`, and setting `low` on it is a real
saving repeated over every spawn.

Extended thinking is different: a subagent **inherits** the session's setting and there is no
per-subagent control.

## Resolution order

What actually runs, highest priority first:

1. `CLAUDE_CODE_SUBAGENT_MODEL`
2. the per-invocation `model` parameter on the Agent call
3. the agent definition's `model` frontmatter
4. the main conversation's model

`model: inherit` is the default, so omitting the field is a choice to follow the session rather than
an absence of one. A value outside an organisation's `availableModels` allowlist is **substituted**,
not honoured, so frontmatter is a preference and never a guarantee.

## Context window

A subagent's context window is sized by **its own** model. A `haiku` subagent of an `opus` parent gets
the smaller window, so a task that needs 200k of room cannot be sent to a small model to save money:
it will not fit, and the saving turns into a truncated read.

## Skills carry no model here

`model` and `effort` **are** valid skill fields. This marketplace leaves them out of skills for
portability, since only six fields survive outside Claude Code, and puts model selection in agents
and commands where it costs nothing. That is a convention with a reason, not a platform limit.

## Source

[Subagents](https://code.claude.com/docs/en/sub-agents),
[model configuration](https://code.claude.com/docs/en/model-config) and the
[skills frontmatter reference](https://code.claude.com/docs/en/skills#frontmatter-reference),
retrieved 2026-08-21.
