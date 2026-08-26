#!/usr/bin/env python3
"""Regenerate the delegation table inside shopware-dev.md from the marketplace.

The orchestrator can only delegate to what exists. Reading the plugins rather
than restating them keeps the table true after a skill is added or renamed.

    build_routing_table.py --marketplace <repo-root> --apply
    build_routing_table.py --marketplace <repo-root>          # print only
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys

START = "<!-- routing-table:start -->"
END = "<!-- routing-table:end -->"

# What each plugin is for, in the orchestrator's terms. Only the prose lives here;
# every name in the table is read from the plugins themselves.
TOPICS = {
    "shopware-core": "Plugin base, DI, services, events, CLI, config, logging",
    "shopware-data": "Entities, definitions, fields, associations, Criteria, migrations",
    "shopware-framework": "Scheduled tasks, message queue, rules, Flow Builder, API routes, mail, media",
    "shopware-storefront": "Controllers, pages, Twig, blocks, SCSS, storefront JS, theme",
    "shopware-cms": "Building a CMS block or element, its resolver and admin component",
    "shopware-admin": "Administration modules, components, routing, Pinia, mt-* components",
    "shopware-checkout": "Cart, payment, shipping, order state, documents, promotions",
    "shopware-testing": "PHPUnit, Jest, Playwright",
    "shopware-apps": "App system: manifest, webhooks, app SDKs",
    "shopware-migration": "Version upgrades, Meteor/Vite/Pinia migration, deprecations",
    "shopware-api": "Consuming the Admin, Store and Sync APIs",
    "shopware-quality": "Code review, static analysis, guidelines, changelog",
    "shopware-devops": "Hosting, deployment, PaaS, shopware-cli, troubleshooting",
    "shopware-commercial": "B2B, subscriptions, advanced search, migration assistant",
    "shopware-concepts": "How Shopware works, architecture, no code",
    "shopware-frontends": "Headless storefront: api-client, composables, Nuxt",
    "shopware-merchant": "Operating the administration, not developing against it",
}

ORDER = list(TOPICS)


def read_plugin(path: str):
    skills = []
    for skill in sorted(glob.glob(f"{path}/skills/*/SKILL.md")):
        text = open(skill, encoding="utf-8").read()
        match = re.search(r"^name:\s*(.+)$", text, re.M)
        if match:
            skills.append(match.group(1).strip())
    agents = []
    for agent in sorted(glob.glob(f"{path}/agents/*.md")):
        text = open(agent, encoding="utf-8").read()
        match = re.search(r"^name:\s*(.+)$", text, re.M)
        agents.append(match.group(1).strip() if match else os.path.basename(agent)[:-3])
    commands = [os.path.basename(c)[:-3] for c in sorted(glob.glob(f"{path}/commands/*.md"))]
    return skills, agents, commands


def build(root: str) -> list[str]:
    lines = [START, ""]
    lines.append("| Topic | Plugin | Agent | Skills | Commands |")
    lines.append("|---|---|---|---|---|")
    total_s = total_a = total_c = 0
    for name in ORDER:
        path = os.path.join(root, "plugins", name)
        if not os.path.isdir(path):
            continue
        skills, agents, commands = read_plugin(path)
        total_s += len(skills)
        total_a += len(agents)
        total_c += len(commands)
        agent_cell = "<br>".join(f"`{name}:{a}`" for a in agents) or "—"
        skill_cell = ", ".join(f"`{s}`" for s in skills) or "—"
        cmd_cell = ", ".join(f"`/{c}`" for c in commands) or "—"
        lines.append(
            f"| {TOPICS[name]} | `{name}` | {agent_cell} | {skill_cell} | {cmd_cell} |"
        )
    lines.append("")
    lines.append(
        f"*{len([n for n in ORDER if os.path.isdir(os.path.join(root, 'plugins', n))])} "
        f"plugins, {total_a} agents, {total_s} skills, {total_c} commands. "
        f"Regenerate with `scripts/build_routing_table.py`.*"
    )
    lines.append("")
    lines.append(END)
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--marketplace", required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    table = "\n".join(build(args.marketplace))
    target = os.path.join(args.marketplace, "plugins/shopware-core/agents/shopware-dev.md")
    if not args.apply:
        print(table)
        return 0
    text = open(target, encoding="utf-8").read()
    if START not in text or END not in text:
        print(f"markers not found in {target}", file=sys.stderr)
        return 1
    head, rest = text.split(START, 1)
    _old, tail = rest.split(END, 1)
    open(target, "w", encoding="utf-8").write(head + table + tail)
    print(f"updated {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
