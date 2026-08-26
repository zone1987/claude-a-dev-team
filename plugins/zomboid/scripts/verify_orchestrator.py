#!/usr/bin/env python3
"""Prove the orchestrator knows every skill and every agent in this plugin.

An orchestrator that omits a skill is worse than no orchestrator: it routes confidently to the
subset it happens to name, and the omitted skill is never reached by anything. The omission is
silent, which is why it is checked mechanically rather than by reading.

Checks:
  MISSING-SKILL   a skill directory the orchestrator never names
  MISSING-AGENT   a sibling agent the orchestrator never names
  GHOST-SKILL     a skill the orchestrator names that does not exist
  GHOST-AGENT     an agent the orchestrator names that does not exist
  NO-PURPOSE      a skill named without a stated purpose on the same line
  UNSCOPED-AGENT  an agent named without its plugin scope, which is ambiguous across plugins

Usage:
    verify_orchestrator.py [--orchestrator FILE] [--plugin DIR]
Exit code is non-zero on any finding.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

PLUGIN = pathlib.Path(__file__).resolve().parent.parent


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plugin", default=str(PLUGIN))
    ap.add_argument("--orchestrator", default="")
    args = ap.parse_args()

    plugin = pathlib.Path(args.plugin)
    agents_dir = plugin / "agents"
    skills_dir = plugin / "skills"

    agent_files = sorted(agents_dir.glob("*.md"))
    if not agent_files:
        print("no agents to check", file=sys.stderr)
        return 2

    # The orchestrator is the agent whose description says it orchestrates, unless named explicitly.
    if args.orchestrator:
        orch = pathlib.Path(args.orchestrator)
    else:
        cands = [f for f in agent_files if re.search(r"\borchestrat", f.read_text(encoding="utf-8"), re.I)]
        if len(cands) != 1:
            print(f"could not identify a single orchestrator among {len(agent_files)} agents "
                  f"({len(cands)} candidates); pass --orchestrator", file=sys.stderr)
            return 2
        orch = cands[0]

    text = orch.read_text(encoding="utf-8")
    lines = text.splitlines()
    plugin_name = plugin.name

    skills = sorted(p.name for p in skills_dir.iterdir() if p.is_dir() and (p / "SKILL.md").is_file())
    others = sorted(f.stem for f in agent_files if f != orch)

    findings: list[str] = []

    for s in skills:
        hits = [l for l in lines if s in l]
        if not hits:
            findings.append(f"MISSING-SKILL   {s} is never named in {orch.name}")
            continue
        # A bare mention in a link or a list is not routing; the line must say what it is for.
        if not any(len(l.strip()) > len(s) + 24 for l in hits):
            findings.append(f"NO-PURPOSE      {s} is named but no line states what it covers")

    for a in others:
        if a not in text:
            findings.append(f"MISSING-AGENT   {a} is never named in {orch.name}")
        elif f"{plugin_name}:{a}" not in text:
            findings.append(f"UNSCOPED-AGENT  {a} is named without its `{plugin_name}:` scope")

    for m in re.findall(r"\b(pz-[a-z0-9-]+)\b", text):
        if m in skills or m in others or m == orch.stem:
            continue
        findings.append(f"GHOST           {m} is named but is neither a skill nor an agent")

    print(f"orchestrator: {orch.name}")
    print(f"{len(skills)} skills, {len(others)} sibling agents")
    if findings:
        print()
        for f in sorted(set(findings)):
            print(f)
        print(f"\n{len(set(findings))} finding(s)")
        return 1
    print("every skill and every agent is named with a purpose")
    return 0


if __name__ == "__main__":
    sys.exit(main())
