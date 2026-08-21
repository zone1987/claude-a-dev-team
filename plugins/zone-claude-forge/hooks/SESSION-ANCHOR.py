#!/usr/bin/env python3
"""Name the forge once per session, so it is present before the first prompt.

The nudge on UserPromptSubmit needs an anchor in the prompt to fire. This does not: it runs when a
session opens, so working on a plugin without ever naming a file still reaches the forge. Stdout is
added to Claude's context as plain text for this event, which is why it prints prose rather than a
decision.

It cannot block anything, and it stays short on purpose: this text is loaded every session, so every
line is a recurring cost paid whether or not the session touches a plugin.

Fires only inside this marketplace, which is the whole point of the cwd test: a session elsewhere
pays nothing.
"""
from __future__ import annotations

import json
import os
import sys

CONTEXT = """\
This repository is a Claude Code plugin marketplace. Creating or editing any plugin, skill, agent,
command or hook here goes through plugins/zone-claude-forge:

- a SKILL.md, a description, or frontmatter: call the Skill tool with "zcf-skill-authoring"
- an agent, a slash command, or a hook: call the Skill tool with "zcf-component-authoring"
- reference files from upstream docs, OpenAPI or a repository: call the Skill tool with
  "zcf-source-distillation"
- unsure which: the user runs /zone-claude-forge:zcf-forge

The 76 rules and their grounding are in plugins/zone-claude-forge/RULES.md. The gate a change passes
before it ships is /zcf-validate <plugin> --strict. A PreToolUse hook refuses a write into plugins/
that breaks a blocking rule, so reach for the skill before writing rather than after being refused.\
"""


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    # Only inside this marketplace. A session in another project gets nothing, so the cost is
    # paid exactly where it buys something.
    cwd = payload.get("cwd") or os.getcwd()
    if not os.path.isfile(os.path.join(cwd, ".claude-plugin", "marketplace.json")):
        return 0

    print(CONTEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
