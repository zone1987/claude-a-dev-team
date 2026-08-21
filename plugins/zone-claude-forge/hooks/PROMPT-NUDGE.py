#!/usr/bin/env python3
"""Name the forge when a prompt is about authoring a plugin in this marketplace.

A nudge, and honest about being one: no mechanism forces a skill to load, so this raises the odds
and never guarantees anything. UserPromptSubmit supports no matcher, so it fires on every prompt
and the matching happens here, behind an early return.

additionalContext goes at the TOP level of the JSON. Inside hookSpecificOutput it is silently
dropped, which is the failure that looks like it worked: exit 0, valid JSON, no context.
"""
from __future__ import annotations

import json
import re
import sys

# Artifacts, not activities. "write me a skill" must not fire this: every plugin's users discuss
# skills, agents and hooks constantly. A path or an exact filename is unambiguous where a topic
# is not.
ANCHOR = re.compile(r"""(?xi)
      plugins/[\w-]+/               # a path into a plugin
    | \bSKILL\.md\b
    | \bplugin\.json\b
    | \bmarketplace\.json\b
    | \bhooks\.json\b
    | \b(?:agents|commands)/[\w*.-]+\.md\b
    | \b(?:UserPromptSubmit|PreToolUse|PostToolUse|SubagentStop)\b
    | \bdisable-model-invocation\b
    | \bskill\s+listing\s+budget\b
    | \bzone-claude-forge\b
""")

HINT = (
    "This marketplace has an authoring plugin: zone-claude-forge. Creating or editing a plugin, "
    "skill, agent, command or hook goes through it.\n"
    "- Writing a SKILL.md: call the Skill tool with \"zcf-skill-authoring\".\n"
    "- Writing an agent, command or hook: call the Skill tool with \"zcf-component-authoring\".\n"
    "- Distilling upstream docs into reference files: call the Skill tool with "
    "\"zcf-source-distillation\".\n"
    "- Unsure which: the user can run /zone-claude-forge:zcf-forge.\n"
    "The 75 rules and their grounding are in plugins/zone-claude-forge/RULES.md; "
    "/zcf-validate <plugin> --strict is the gate a change passes before it ships. "
    "A PreToolUse hook refuses a write that breaks a blocking rule."
)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    if not ANCHOR.search(payload.get("prompt") or ""):
        return 0                        # the common case costs one regex and nothing else
    print(json.dumps({"additionalContext": HINT}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
