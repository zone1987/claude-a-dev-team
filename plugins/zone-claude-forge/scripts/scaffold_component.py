#!/usr/bin/env python3
"""Scaffold a compliant skill, agent, command or hook, and measure it while writing.

Measuring at write time is the point: a description that overflows is cheapest to fix before the
body exists, and a scaffold that silently produces an over-budget entry teaches the author nothing.
The script refuses rather than warns, because a warning at scaffold time is read once and ignored.

Usage:
    scaffold_component.py skill   --plugin P --name N --description D [--user-invoked] [--reference R]…
    scaffold_component.py agent   --plugin P --name N --description D [--model M] [--read-only]
    scaffold_component.py command --plugin P --name N --description D [--argument-hint H] [--model M]
Exit code is non-zero when a limit would be broken, or the target exists.
"""
from __future__ import annotations

import argparse
import os
import re
import sys

PLUGIN_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(PLUGIN_DIR))

DESC_MAX = 200
HEADROOM_MIN = 10
RESERVED = ("anthropic", "claude")
TODAY = "<YYYY-MM-DD>"


def fail(msg: str) -> None:
    print(f"refused: {msg}", file=sys.stderr)
    sys.exit(1)


def check_name(name: str, kind: str) -> None:
    if len(name) > 64:
        fail(f"name is {len(name)} characters, limit 64 (NAME-01)")
    if not re.fullmatch(r"[a-z0-9-]+", name):
        fail(f"name '{name}' allows only lowercase letters, digits and hyphens (NAME-01)")
    if kind == "skill":
        for word in RESERVED:
            if word in name:
                fail(f"a skill name may not contain the reserved word '{word}' (NAME-01)")


def check_description(desc: str, model_invoked: bool) -> None:
    if len(desc) > DESC_MAX:
        fail(f"description is {len(desc)} characters, limit {DESC_MAX} (DESC-01)")
    if "\n" in desc:
        fail("description spans more than one line (DESC-02)")
    if re.match(r"^(I |You |Use this|This skill)", desc):
        fail("description is not third person (DESC-04)")
    if not model_invoked:
        return
    if ". Use when " not in desc:
        fail("a model-invoked description needs the pattern "
             "'<Statement>. Use when <anchor>, <anchor>.' (DESC-03)")
    if DESC_MAX - len(desc) < HEADROOM_MIN:
        fail(f"only {DESC_MAX - len(desc)} characters of headroom; an entry this close to the "
             "limit truncates once a sibling plugin is enabled beside it (BUDGET-04)")


def write(path: str, text: str) -> None:
    if os.path.exists(path):
        fail(f"{os.path.relpath(path, REPO)} already exists; refusing to overwrite")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"  wrote {os.path.relpath(path, REPO)}")


def skill(args: argparse.Namespace) -> None:
    model_invoked = not args.user_invoked
    check_name(args.name, "skill")
    check_description(args.description, model_invoked)

    refs = [r if r.endswith(".md") else f"{r}.md" for r in (args.reference or [])]
    for r in refs:
        if not re.fullmatch(r"[A-Z][A-Z0-9-]*\.md", r):
            fail(f"reference '{r}' is not SCREAMING-CASE.md (REF-01)")

    fm = [f"name: {args.name}", f"description: '{args.description}'"]
    if args.user_invoked:
        fm.append("disable-model-invocation: true")

    body = [
        "---", *fm, "---", "",
        f"# {args.name}", "",
        "<One to three sentences of purpose. Load-bearing content first: after compaction only the",
        "first 5,000 tokens of this file come back.>", "",
        "## <Core model, or the decision this skill turns on>", "",
        "- **<term>**: <meaning>.", "",
    ]
    if refs:
        body += ["## Reference map", ""]
        body += [f"- **[{r}]({r})**: <what it holds, so Claude can decide whether to open it>."
                 for r in refs]
        body.append("")
    body += [
        "## Source", "",
        f"Distilled from [<upstream>](<url>) — <version, sha or file>, retrieved {TODAY}.", "",
    ]
    base = os.path.join(REPO, "plugins", args.plugin, "skills", args.name)
    write(os.path.join(base, "SKILL.md"), "\n".join(body))
    for r in refs:
        write(os.path.join(base, r), "\n".join([
            f"# {r[:-3].replace('-', ' ').title()}", "",
            "<What this file holds. A file over 100 lines with three or more sections needs a",
            "table of contents here (TOC-01).>", "",
            "## Source", "",
            f"[<specific page, never the site root>](<url>), retrieved {TODAY}.", "",
        ]))

    cost = len(args.description) + 109 if model_invoked else len(args.name)
    print(f"\ndescription {len(args.description)} characters, "
          f"{DESC_MAX - len(args.description)} of headroom")
    print(f"listing cost {cost} characters "
          f"({'model-invoked' if model_invoked else 'name only, user-invoked'})")
    print(f"\nnext: add './skills/{args.name}' to skills[] in both manifests, then\n"
          f"  python3 scripts/validate_plugin.py --plugin {args.plugin} --strict")


def agent(args: argparse.Namespace) -> None:
    check_name(args.name, "agent")
    check_description(args.description, False)
    fm = [f"name: {args.name}", "description: >", f"  {args.description}"]
    fm.append("tools: Read, Grep, Glob" + ("" if args.read_only else ", Bash, Edit, Write"))
    if args.read_only:
        fm.append("disallowedTools: Write, Edit, MultiEdit, NotebookEdit")
    fm += [f"model: {args.model}", "effort: medium", f"maxTurns: {args.max_turns}"]
    write(os.path.join(REPO, "plugins", args.plugin, "agents", f"{args.name}.md"),
          "\n".join(["---", *fm, "---", "",
                     f"# {args.name}", "",
                     "<One sentence naming the job. A subagent runs in its own context window, so",
                     "the parent pays for the summary rather than the reading.>", "",
                     "## How to work", "",
                     '1. Call the Skill tool with "<skill>" before anything else.',
                     "2. <step, ending on a checkable condition>", "",
                     "## Guardrails", "",
                     "- **<bold lead term>**: <the positive behaviour to take>.", "",
                     "## Source", "",
                     f"<Where the method comes from>, retrieved {TODAY}.", ""]))
    print("\nomitted deliberately: hooks, mcpServers and permissionMode are ignored for plugin "
          "agents (AGENT-02)")


def command(args: argparse.Namespace) -> None:
    check_name(args.name, "command")
    check_description(args.description, False)
    write(os.path.join(REPO, "plugins", args.plugin, "commands", f"{args.name}.md"),
          "\n".join(["---",
                     f"name: {args.name}",
                     f"description: {args.description}",
                     f"argument-hint: {args.argument_hint}",
                     "allowed-tools: Read, Glob, Grep",
                     f"model: {args.model}",
                     "---", "",
                     f"# /{args.name}", "",
                     "<One sentence naming the job, with $ARGUMENTS in it.>", "",
                     "## Steps", "", "1. <step>", "",
                     "## Output", "",
                     "<The shape, so two runs look the same.>", "",
                     "Report only what the files contain. Invent nothing.", ""]))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="kind", required=True)
    for kind in ("skill", "agent", "command"):
        p = sub.add_parser(kind)
        p.add_argument("--plugin", required=True)
        p.add_argument("--name", required=True)
        p.add_argument("--description", required=True)
        if kind == "skill":
            p.add_argument("--user-invoked", action="store_true")
            p.add_argument("--reference", action="append")
        if kind == "agent":
            p.add_argument("--model", default="sonnet",
                           choices=("haiku", "sonnet", "opus", "inherit"))
            p.add_argument("--read-only", action="store_true")
            p.add_argument("--max-turns", type=int, default=20)
        if kind == "command":
            p.add_argument("--argument-hint", default="<argument>")
            p.add_argument("--model", default="haiku", choices=("haiku", "sonnet", "opus"))
    args = ap.parse_args()
    {"skill": skill, "agent": agent, "command": command}[args.kind](args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
