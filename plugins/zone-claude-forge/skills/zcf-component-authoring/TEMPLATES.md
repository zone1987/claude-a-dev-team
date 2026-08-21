# Templates

Skeletons for an agent, a command and each hook shape, plus the file-naming convention they follow.

## Contents

- [File naming](#file-naming)
- [Agent](#agent)
- [Command](#command)
- [Hook: PostToolUse](#hook-posttooluse)
- [Hook: UserPromptSubmit](#hook-userpromptsubmit)
- [Hook: PreToolUse gate](#hook-pretooluse-gate)
- [Source](#source)

## File naming

Four cases, and only one of them is fixed by the platform. `REF-01`, `LANG-02`

| What | Convention | Example |
|---|---|---|
| Markdown beside `SKILL.md` | **SCREAMING-CASE.md** | `HOOK-EVENTS.md`, `RULES.md`, `README.md` |
| `SKILL.md` itself | fixed by the platform | `SKILL.md` |
| Agents and commands | lowercase kebab-case, matching the invocation name | `zcf-validate.md`, `claude-source-distiller.md` |
| Scripts | their language's convention | `validate_plugin.py`, `pre-write-gate.py` |
| Directories | lowercase kebab-case | `skills/zcf-skill-authoring/` |

**Every markdown file beside `SKILL.md` is SCREAMING-CASE**, so a reference is distinguishable from
the skill at a glance and sorts above lowercase siblings in a listing. An agent or command file is
different: its name **is** the invocation name (`/zcf-validate`), so it follows the identifier
convention instead.

### The name has to match the content

Casing is the easy half. The harder half is that **the name says what is inside, and the inside
matches the name**. `REF-03`

The name is what a reader and the model choose by: a reference map lists names, a grep matches names,
and Claude decides whether to open a file from its name plus one line. A misleading name costs a read
of the wrong file and hides the right one.

Two failures to watch for:

- **An inverted relationship.** `HOOKS-REFERENCE-07-CONTENT-MODULES.md` reads as content modules and
  holds the hooks that fire while rendering content elements. The file's own first line got it right
  (`Contao Hooks: Content elements`); the name inverted it.
- **A positional number doing the naming.** `-07-` files the document rather than naming it. Nobody
  looks for group seven, so the number spends characters and delivers nothing.

The test takes ten seconds: read the file name aloud, then read its first heading. Where the two
describe different things, rename the file.

Nothing in the platform requires any of this. The documentation asks only for descriptive names
(`form_validation_rules.md`, not `doc2.md`) and its own examples use both `FORMS.md` and
`reference/finance.md`. The catalogue records `REF-01` as a `convention` for exactly that reason:
a later reader should not mistake a habit for a necessity.

## Agent

```markdown
---
name: <product>-<role>
description: >
  <Role, and when to delegate here>. Use proactively when <anchor>, <anchor>.
tools: Read, Grep, Glob
disallowedTools: Write, Edit
model: sonnet
effort: medium
maxTurns: 20
skills: <one-or-two-skills>
---

# <Title>

<One sentence naming the job.>

## How to work

1. Call the Skill tool with "<skill>" before anything else.
2. <step, ending on a checkable condition>

## Guardrails

- **<bold lead term>**: <the positive behaviour to take>.
```

`use proactively` is the documented nudge for delegation, not a guarantee; `@agent-<plugin>:<name>`
is the guarantee. The body names its skills because `skills:` is ignored in the teammate role.

## Command

```markdown
---
name: <prefix>-<verb-object>
description: <What it does, for a human reading the slash menu.>
argument-hint: <arg> [--flag]
allowed-tools: Read, Glob, Grep
model: haiku
---

# /<prefix>-<verb-object>

<One sentence with $ARGUMENTS in it.>

## Steps

1. <step>

## Output

<the shape, so two runs look the same>

Report only what the files contain. Invent nothing.
```

## Hook: PostToolUse

Reports after the fact; cannot prevent.

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [
          { "type": "command",
            "command": ["python3", "${CLAUDE_PLUGIN_ROOT}/hooks/POST-WRITE-CHECK.py"],
            "timeout": 5 }
        ]
      }
    ]
  }
}
```

## Hook: UserPromptSubmit

No matcher, and `additionalContext` at the top level.

```python
#!/usr/bin/env python3
import json, re, sys

ANCHOR = re.compile(r"""(?xi)
    plugins/ | SKILL\.md | plugin\.json | marketplace\.json | hooks\.json
""")

def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0                      # never block on malformed input
    if not ANCHOR.search(payload.get("prompt", "")):
        return 0                      # early return: the common case costs one regex
    print(json.dumps({"additionalContext": "…"}))
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

## Hook: PreToolUse gate

The only shape that can refuse. Order matters: the cheap test first, because a timed-out gate is an
open gate.

```python
def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    path = (payload.get("tool_input") or {}).get("file_path", "")
    if "/plugins/" not in path:
        return 0                      # one string comparison, then out
    findings = check(path, payload["tool_input"].get("content", ""))
    if not findings:
        return 0
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": "; ".join(findings),
    }}))
    return 0                          # exit 0: the JSON carries the decision
```

## Source

[Hooks](https://code.claude.com/docs/en/hooks),
[subagents](https://code.claude.com/docs/en/sub-agents) and the
[plugins reference](https://code.claude.com/docs/en/plugins-reference), retrieved 2026-08-21. The
naming conventions are this marketplace's own; see `REF-01` in [`RULES.md`](../../RULES.md).
