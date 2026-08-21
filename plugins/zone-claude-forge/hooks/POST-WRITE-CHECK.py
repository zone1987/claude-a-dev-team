#!/usr/bin/env python3
"""Report what only the whole plugin can decide, once a write has landed.

PreToolUse checks the file being written; some rules need every file on disk: the listing budget
sums across skills, manifest parity compares two files, and a link check needs the target to
exist. Those belong here, after the write.

This reports and cannot prevent, so it prints to stderr rather than rendering a decision. Exit 0
on every path.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

PLUGIN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(PLUGIN))
WATCHED = ("SKILL.md", "plugin.json", "marketplace.json", "hooks.json")


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    path = ((payload.get("tool_input") or {}).get("file_path") or "").replace(os.sep, "/")
    if "/plugins/" not in path and not path.startswith("plugins/"):
        return 0
    base = os.path.basename(path)
    if base not in WATCHED and not (
        base.endswith(".md") and ("/agents/" in path or "/commands/" in path)
    ):
        return 0

    parts = path.split("plugins/", 1)[-1].split("/")
    if not parts:
        return 0
    plugin = parts[0]

    try:
        proc = subprocess.run(
            [sys.executable, os.path.join(PLUGIN, "scripts", "validate_plugin.py"),
             "--plugin", plugin, "--json"],
            capture_output=True, text=True, timeout=8, cwd=REPO)
        data = json.loads(proc.stdout or "{}")
    except Exception:
        return 0                        # a broken check is silent, never noisy

    findings = [i for i in data.get("findings", []) if i["severity"] == "error"]
    if not findings:
        return 0

    lines = [f"[zcf] {plugin}: {len(findings)} blocking finding(s) after that write"]
    for i in findings[:5]:
        loc = f"{i['path']}:{i['line']}" if i.get("line") else i["path"]
        lines.append(f"  [{i['rule']}] {loc}: {i['message']}")
    if len(findings) > 5:
        lines.append(f"  and {len(findings) - 5} more")
    stats = data.get("stats") or {}
    if stats:
        lines.append(f"  {stats.get('visible')} model-visible skills, "
                     f"{stats.get('chars')} characters, {stats.get('budget_pct')}% of budget")
    lines.append("  rule wording: plugins/zone-claude-forge/RULES.md")
    print("\n".join(lines), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
