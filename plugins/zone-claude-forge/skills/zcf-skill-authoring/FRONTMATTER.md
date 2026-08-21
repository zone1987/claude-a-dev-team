# Skill frontmatter

Every field Claude Code accepts in `SKILL.md`, what it costs, and which six survive outside
Claude Code. Rules: `FM-01` to `FM-05`, `NAME-01/02`, `INVOKE-01/02`.

## Contents

- [What this marketplace uses](#what-this-marketplace-uses)
- [The portability boundary](#the-portability-boundary)
- [Invocation control](#invocation-control)
- [Every documented field](#every-documented-field)
- [Fields to leave alone, and why](#fields-to-leave-alone-and-why)
- [Source](#source)

## What this marketplace uses

`name`, `description`, and `disable-model-invocation` where the skill is user-invoked. Nothing else,
unless a specific field earns its place against the two costs below.

Two costs decide every addition: a field that stays in the listing spends **context** on every turn,
and a field outside the six-field spec spends **portability**.

## The portability boundary

Outside Claude Code only six fields are legal: `name`, `description`, `license`, `compatibility`,
`metadata`, `allowed-tools`.

> If you include any field the spec doesn't allow, packaging or upload fails with a hard error
> instead of ignoring the field

The failure is hard, not silent, so a skill carrying `argument-hint` cannot be uploaded to claude.ai
or shipped through the Skills API at all. Keeping to `name` and `description` therefore buys
portability for free. `FM-02`

## Invocation control

Two fields, and the table is the whole mechanism:

| Frontmatter | You invoke | Claude invokes | Description in context |
|---|---|---|---|
| (default) | yes | yes | always |
| `disable-model-invocation: true` | yes | no | **no** |
| `user-invocable: false` | no | yes | always |

The middle row is the largest cost lever available: the description leaves context entirely, and only
the name remains in the listing. The price is that **nothing but the human can reach the skill**, so
no other skill may call it, and a step depending on it is written as an instruction to the human.
`INVOKE-01/02`

The third row is for background knowledge that is not an action: a `legacy-system-context` skill
Claude should know about but nobody would type.

Boolean fields accept `yes`, `no`, `on`, `off`, `1`, `0` in any case as well as `true`/`false`; before
v2.1.218 only `true` and `false` were recognised.

## Every documented field

| Field | What it does | Cost |
|---|---|---|
| `name` | invocation name. Max 64 chars, lowercase, digits, hyphens. Never `anthropic` or `claude` | none |
| `description` | what the skill does and when. Max 1,024 chars; the listing entry truncates at 1,536 | the listing entry |
| `when_to_use` | appended to `description` in the listing, against the same cap | buys nothing; `FM-03` |
| `argument-hint` | autocomplete hint | portability |
| `arguments` | named positional arguments for `$name` substitution | portability |
| `disable-model-invocation` | only the human invokes | saves the description |
| `user-invocable` | only Claude invokes | none |
| `allowed-tools` | pre-approves tools for the invoking turn; clears on the next message | none, and spec-legal |
| `disallowed-tools` | removes tools while the skill is active | portability |
| `model` | model for the rest of the turn; accepts `inherit` | portability |
| `effort` | effort level while active: `low` to `max` | portability |
| `context: fork` | run in a forked subagent | portability; `FM-05` |
| `agent` | subagent type when `context: fork` is set | portability |
| `background` | with `context: fork`, `false` waits for the result in the invoking turn | portability |
| `hooks` | hooks registered on invocation, kept for the session; `once: true` for a single run | portability |
| `paths` | glob patterns that **limit** activation | breaks prose triggering; `FM-04` |
| `shell` | `bash` or `powershell` for inline commands | portability |
| `metadata` | free-form map for your own tooling; Claude Code does not read it | none, spec-legal |
| `license` | Agent Skills spec field; accepted, not acted on | none, spec-legal |
| `compatibility` | environment requirements, max 500 chars | none, spec-legal |

`model` and `effort` **are** valid skill fields. `CLAUDE.md:265` states otherwise; the frontmatter
reference documents both in full. This marketplace still leaves them out, for portability rather
than validity, and that is a choice the catalogue records as a convention rather than a fact.

## Fields to leave alone, and why

- **`triggers`** does not exist. It is parsed as unknown and does nothing. Triggers belong in
  `description`.
- **`when_to_use`** is real but pointless here: it lands in the same 1,536-character entry as
  `description` and doubles the maintenance surface. `FM-03`
- **`paths`** filters rather than amplifies: with it set, the skill loads automatically **only** when
  a matching file is open, so a plain question matches nothing. That is the main case for a knowledge
  skill. `FM-04`
- **`context: fork` on a reference skill** returns nothing, because the subagent receives guidelines
  with no actionable task. Fork a skill that *does* something. `FM-05`

## Source

[Skills frontmatter reference](https://code.claude.com/docs/en/skills#frontmatter-reference),
[control who invokes a skill](https://code.claude.com/docs/en/skills#control-who-invokes-a-skill),
[using skill frontmatter outside Claude Code](https://code.claude.com/docs/en/skills#using-skill-frontmatter-outside-claude-code),
and [skill structure](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices#skill-structure),
retrieved 2026-08-21.
