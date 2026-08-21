#!/usr/bin/env python3
"""Refuse a write into plugins/ that breaks a blocking rule.

This is the only deterministic layer in the plugin: no mechanism forces a skill to load, but
PreToolUse can deny a tool call. It denies with exit 0 plus a permissionDecision rather than
exit 2, so Claude receives a structured reason instead of scraped stderr.

Speed is correctness here, not tidiness. A timed-out PreToolUse hook does not block: the call
continues through the normal permission flow. So the cheap test comes first, and nothing expensive
runs until the path is known to matter. Exit 0 on every path, including every error path: a hook
that raises is a hook that does not fire.

ZCF_BYPASS=1 downgrades the denial to a warning, for the one honest case: repairing a plugin that
is already red, where the first fixing write would itself be refused.
"""
from __future__ import annotations

import json
import os
import sys

PLUGIN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BYPASS = os.environ.get("ZCF_BYPASS", "").strip().lower() in ("1", "true", "yes", "on")


def decision(reason: str) -> None:
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": reason,
    }}))


def refuse(reason: str) -> int:
    """Deny a write, or warn only when ZCF_BYPASS is set, as the content gate does."""
    if BYPASS:
        print(f"[zcf] ZCF_BYPASS set, allowing a non-compliant write: {reason}", file=sys.stderr)
        return 0
    decision(reason)
    return 0


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0                       # malformed input is never the user's problem

    tool_input = payload.get("tool_input") or {}
    path = tool_input.get("file_path") or ""

    # The cheap test, first and always: two string comparisons decide the common case.
    if "/plugins/" not in path.replace(os.sep, "/") and not path.startswith("plugins/"):
        return 0
    base = os.path.basename(path)
    norm = path.replace(os.sep, "/")

    # REF-04 is decidable from the path alone, before any content is parsed: a reference
    # belongs in skills/<skill>/references/. Catching it here stops the file being created in
    # the wrong place, which is cheaper than moving it and re-pointing SKILL.md afterwards.
    if base.endswith(".md") and "/skills/" in norm and base != "SKILL.md":
        parts = norm.split("/skills/", 1)[1].split("/")
        if len(parts) == 2:            # skills/<skill>/FILE.md
            return refuse(
                f"[REF-04] '{base}' would sit beside SKILL.md. Every reference belongs in "
                f"skills/{parts[0]}/references/{base} and must be linked directly from "
                "SKILL.md. Never add an INDEX.md there: SKILL.md's reference map is the "
                "index, and a second one drops every file behind it to a head -100 preview "
                "(DEPTH-01)."
            )
        if len(parts) >= 3 and parts[1] == "references" and base in (
            "INDEX.md", "README.md", "CONTENTS.md"
        ):
            return refuse(
                f"[DEPTH-01] '{base}' inside references/ is an index file. Every reference is "
                "linked directly from SKILL.md instead; an index downgrades every file behind "
                "it to a head -100 preview, hiding everything past line 100."
            )

    if base != "SKILL.md" and base != "hooks.json" and not (
        base.endswith(".md") and ("/agents/" in path or "/commands/" in path)
    ):
        return 0                       # a README, a script: not gated

    content = tool_input.get("content")
    if content is None:
        # Edit and MultiEdit carry no full content, so the file on disk is not yet the new one.
        # Checking the old content would deny the very write that fixes it.
        return 0

    sys.path.insert(0, os.path.join(PLUGIN, "scripts"))
    try:
        import validate_plugin as V
    except Exception:
        return 0                       # a broken gate must not block anyone's work

    rep = V.Report()
    try:
        fm, _, body = V.parse_frontmatter(content)
        if base == "SKILL.md":
            check_skill_content(V, rep, path, fm, body)
        elif base == "hooks.json":
            check_hooks_content(V, rep, path, content)
        else:
            check_component_content(V, rep, path, fm, body)
    except Exception:
        return 0

    errors = [i for i in rep.items if i["severity"] == "error"]
    if not errors:
        return 0

    detail = "; ".join(f"[{i['rule']}] {i['message']}" for i in errors[:4])
    if len(errors) > 4:
        detail += f"; and {len(errors) - 4} more"

    if BYPASS:
        print(f"[zcf] ZCF_BYPASS set, allowing a non-compliant write: {detail}", file=sys.stderr)
        return 0

    # Name the skill that carries the fix, not only the rule that was broken. A rule id tells the
    # model what is wrong; the skill tells it how to write the file correctly, which is the whole
    # reason the plugin exists.
    decision(
        f"{detail}. "
        f"Call the Skill tool with \"{skill_for(base, path)}\" for how to write this file, then "
        f"write it again. Rule wording and grounding: plugins/zone-claude-forge/RULES.md "
        f"(look up the rule id). Check the whole plugin with /zcf-validate <plugin> --strict. "
        f"To repair a plugin that is already failing, set ZCF_BYPASS=1 for that write."
    )
    return 0


def skill_for(base: str, path: str) -> str:
    """The skill that carries the guidance for this kind of file."""
    if base == "SKILL.md":
        return "zcf-skill-authoring"
    return "zcf-component-authoring"


def check_skill_content(V, rep, path: str, fm: dict, body: list[str]) -> None:
    """The subset of check_skill that a file's own text can decide."""
    rel = path
    name = fm.get("name", "")
    desc = fm.get("description", "")
    if not name:
        rep.error("NAME-02", rel, "no name field, so the install directory name would be used")
    else:
        if len(name) > 64:
            rep.error("NAME-01", rel, f"name is {len(name)} characters, limit 64")
        for word in V.RESERVED_NAME_WORDS:
            if word in name.lower():
                rep.error("NAME-01", rel, f"name contains the reserved word '{word}'")
    if not desc:
        rep.error("DESC-03", rel, "no description")
    else:
        if len(desc) > V.DESC_MAX:
            rep.error("DESC-01", rel, f"description is {len(desc)} characters, limit {V.DESC_MAX}")
        if V.is_truthy(fm.get("disable-model-invocation", "")) is False and (
                ". Use when " not in desc and not desc.startswith("Use when ")):
            pass                        # a warning in the full gate, not a denial
        if desc[:1] and desc.split()[0] in ("I", "You"):
            rep.error("DESC-04", rel, "description is not third person")
    for field in V.FORBIDDEN_SKILL_FIELDS & set(fm):
        rule = {"when_to_use": "FM-03", "paths": "FM-04"}.get(field, "FM-01")
        rep.error(rule, rel, f"field '{field}' does not belong in a skill here")
    if len(body) > V.BODY_MAX:
        rep.error("SIZE-01", rel, f"body is {len(body)} lines, limit {V.BODY_MAX}")
    if "## Source" not in "\n".join(body):
        rep.error("SRC-01", rel, "no '## Source' section naming where the knowledge came from")


def check_component_content(V, rep, path: str, fm: dict, body: list[str]) -> None:
    rel = path
    if "/agents/" in path:
        for field in sorted(V.AGENT_REQUIRED - set(fm)):
            rep.error("AGENT-01", rel, f"no {field} field")
        for field in sorted(V.AGENT_FORBIDDEN & set(fm)):
            rep.error("AGENT-02", rel, f"'{field}' is ignored for plugin subagents")
        preload = [s for s in fm.get("skills", "").replace(",", " ").split() if s]
        if len(preload) > V.MAX_PRELOAD:
            rep.error("AGENT-03", rel,
                      f"preloads {len(preload)} skills; full content is injected at startup")
    else:
        for field in sorted(V.COMMAND_REQUIRED - set(fm)):
            rep.error("AGENT-01", rel, f"no {field} field")


def check_hooks_content(V, rep, path: str, content: str) -> None:
    try:
        cfg = json.loads(content)
    except json.JSONDecodeError as exc:
        rep.error("HOOK-01", path, f"not valid JSON: {exc}")
        return
    for event, entries in (cfg.get("hooks") or {}).items():
        for entry in entries:
            if event == "UserPromptSubmit" and "matcher" in entry:
                rep.error("HOOK-01", path, "UserPromptSubmit supports no matcher")
            for h in entry.get("hooks", []):
                if h.get("type") != "command":
                    continue
                cmd = h.get("command")
                if isinstance(cmd, str) and "${CLAUDE_PLUGIN_ROOT}" in cmd:
                    rep.error("HOOK-05", path, "a path placeholder needs exec form")
                if "timeout" not in h:
                    rep.error("HOOK-04", path,
                              f"{event} hook sets no timeout; a timed-out gate does not block")


if __name__ == "__main__":
    sys.exit(main())
