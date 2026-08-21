# Hooks

The deterministic layer. A hook cannot make Claude load a skill, and it can refuse a tool call.
Rules: `HOOK-01` to `HOOK-06`.

## Contents

- [What a hook can and cannot do](#what-a-hook-can-and-cannot-do)
- [Events and matcher support](#events-and-matcher-support)
- [Exit codes](#exit-codes)
- [Denying a tool call](#denying-a-tool-call)
- [Adding context](#adding-context)
- [Timeouts, and why speed is correctness](#timeouts-and-why-speed-is-correctness)
- [The input on stdin](#the-input-on-stdin)
- [Handler types](#handler-types)
- [Hooks in skills and agents](#hooks-in-skills-and-agents)
- [Source](#source)

## What a hook can and cannot do

**Cannot**: force a skill to load. No such mechanism exists. A hook that "makes" Claude use a skill is
a promise the platform cannot keep. `HOOK-06`

**Can**: inject context that makes the right choice obvious, and **deny a tool call outright**. Only
`PreToolUse` blocks; everything later can report but not prevent.

## Events and matcher support

The ones that matter for authoring, with what a matcher matches:

| Event | Matcher | Fires |
|---|---|---|
| `SessionStart` | how the session started | at start, resume, clear, compact, fork |
| `UserPromptSubmit` | **none** | on every prompt |
| `PreToolUse` | tool name | before a tool call; **can block** |
| `PostToolUse` | tool name | after a tool succeeded |
| `PostToolUseFailure` | tool name | after a tool failed |
| `PostToolBatch` | none | after a batch |
| `SubagentStart` / `SubagentStop` | agent type | around a subagent |
| `PreCompact` / `PostCompact` | `manual` or `auto` | around compaction |
| `SessionEnd` | reason | at the end; shares a 1.5 s budget |
| `FileChanged` | literal filenames | when a watched file changes |
| `Stop` | none | when Claude stops |

Others exist (`PermissionRequest`, `Notification`, `TaskCreated`, `ConfigChange`, `WorktreeCreate`,
`Elicitation`, and more); consult the reference before reaching for one.

**`UserPromptSubmit` supports no matcher.** Writing one is silently ignored, so it fires on every
prompt and the matching belongs in the script, with an early return before any other work. `HOOK-01`

All matching hooks run **in parallel**. The same handler defined in two settings files runs once; a
plugin's or skill's copy stays separate.

## Exit codes

| Exit | Meaning |
|---|---|
| `0` | success. The intended code when printing JSON for structured control |
| `2` | blocking error. On `PreToolUse` it blocks; even a JSON `permissionDecision: allow` cannot override it |
| other | non-blocking error. The transcript shows a hook error with the first line of stderr |

On exit 0, stdout goes to the debug log and not the transcript, **except** for `UserPromptSubmit`,
`UserPromptExpansion` and `SessionStart`, where plain-text stdout is added as context Claude can act
on.

## Denying a tool call

Two ways, and the JSON form is better:

```python
# exit 0, and print the decision
print(json.dumps({"hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "[DESC-01] description is 214 characters, limit 200",
}}))
```

Exit 2 also blocks, but then the reason reaches Claude only as scraped stderr text. The JSON form
hands over a structured reason, so keep exit 2 for the script's **own** failure, where there is no
decision to report. `HOOK-03`

Printing no decision and exiting 0 means "no opinion": the normal permission flow continues.

## Adding context

```python
print(json.dumps({"additionalContext": "…"}))     # top level
```

**`additionalContext` sits at the top level**, not inside `hookSpecificOutput`. It is a universal
field. Nesting it is the failure that looks like it worked: the hook exits 0, prints valid JSON, and
the context never arrives. `HOOK-02`

## Timeouts, and why speed is correctness

Defaults: `command`, `http` and `mcp_tool` are **600 s**, lowered to **30 s** on
`UserPromptSubmit` and 10 s on `MessageDisplay`; `prompt` is 30 s and `agent` 60 s.

> A timed-out `command`, `http`, or `mcp_tool` hook doesn't block the tool call. The call continues
> through the normal permission flow, so don't count on a stalled hook to act as a gate.

So a slow gate is not a late gate, it is an **open** one, and the output is discarded entirely. Two
consequences: set an explicit low `timeout`, and order the script so the cheap test comes first. A
path comparison before any file read is what keeps a `PreToolUse` gate inside its budget. `HOOK-04`

Exit 0 on every path, and never block the user's work on an unrelated error.

## The input on stdin

Common to every event: `session_id`, `prompt_id`, `transcript_path`, `cwd`, `permission_mode`,
`effort`, `hook_event_name`, plus `agent_id` and `agent_type` inside a subagent.

Tool events add `tool_name`, `tool_input` and `tool_use_id`. For `Write` and `Edit`, the path is
`tool_input.file_path` and the content `tool_input.content`. Read them defensively: wrap the
`json.load` and return early on anything unexpected, because a hook that raises is a hook that does
not fire.

## Handler types

`command` (a script on stdin), `http` (event JSON as a POST), `mcp_tool` (a tool on a connected MCP
server), `prompt` (single-turn model evaluation), `agent` (a subagent that can use tools).

The last two cost a model call per fire, so they do not belong on `UserPromptSubmit` or
`PreToolUse`, which run constantly. Use `command` for anything synchronous.

**A string command, with the placeholder quoted:**

```json
{ "type": "command",
  "command": "python3 \"${CLAUDE_PLUGIN_ROOT}/hooks/PRE-WRITE-GATE.py\"",
  "timeout": 5 }
```

The plugins reference recommends the **exec form** instead, an array of `["python3", "…"]`, so that
each path arrives as one argument with no quoting to get wrong. **Claude Code 2.1.238 rejects it**:
it reports `expected string, received array` and then fails to load the **entire** hooks file, so
every hook in that plugin silently stops firing.

So use the string form and quote the placeholder, which buys the same protection against a path
containing a space. Where the documentation and the running build disagree, the build decides what
works. Re-check on a later version. `HOOK-05`

## Hooks in skills and agents

A skill's `hooks` frontmatter registers on invocation and **keeps running for the rest of the
session**, including turns after the skill's own; `once: true` limits it to a single run. An agent's
hooks run only while that agent runs, and a `Stop` hook there becomes `SubagentStop`.

Neither applies to a **plugin** agent: `hooks` is one of the three ignored fields. `AGENT-02`

## Source

[Hooks](https://code.claude.com/docs/en/hooks) and
[plugins reference](https://code.claude.com/docs/en/plugins-reference), retrieved 2026-08-21.
