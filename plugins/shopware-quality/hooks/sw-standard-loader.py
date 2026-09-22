#!/usr/bin/env python3
"""
Shopware standard loader (SessionStart / UserPromptSubmit).

When the working directory is a Shopware 6 project, state the binding rules once so the
session works to them without anybody having to remember to ask. Never blocks (exit 0).

Detection is deliberately narrow: a Shopware project has custom/plugins or
custom/static-plugins, or a composer.json requiring shopware/core.
"""
import json
import os
import sys
from pathlib import Path

NOTICE = """[shopware] Shopware project detected. The binding standard applies to every plugin here.

BEFORE writing code, load the skill `sw-testing-standard` (plugin: shopware-testing).
It settles what must exist in a plugin, how it is configured, and when work is finished.

Rules that hold whatever the task:
- Everything in English except README.md and the wiki. No prose comments in code.
- No copyright headers in classes; the licence lives in LICENSE and composer.json.
- `composer gate` before every commit - not ecs-fix or phpstan on their own.
- Commit only on a feature branch, ask once at the start whether committing is wanted,
  and NEVER `git push`.
- Build only with `shopware-cli project admin-build|storefront-build --only-extensions <Plugin>`.
- Everything runs in DDEV; credentials come from shopware/.env.local and are never printed.
- Services in PHP without autowiring; XML is @deprecated tag:v6.8.0.
- One task at a time. Finished means committed with a green gate, not "the code works".

Orchestrator for anything spanning domains: `shopware-core:shopware-dev`."""


def is_shopware_project(root: Path) -> bool:
    if (root / "custom" / "plugins").is_dir() or (root / "custom" / "static-plugins").is_dir():
        return True
    for candidate in (root, root / "shopware"):
        composer = candidate / "composer.json"
        if composer.is_file():
            try:
                data = json.loads(composer.read_text(encoding="utf-8"))
            except Exception:
                continue
            requires = {}
            for key in ("require", "require-dev"):
                value = data.get(key)
                if isinstance(value, dict):
                    requires.update(value)
            if any(name.startswith("shopware/") for name in requires):
                return True
            if data.get("type") == "shopware-platform-plugin":
                return True
    return False


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}

    cwd = payload.get("cwd") or os.getcwd()
    root = Path(cwd)

    # Walk up a few levels: a session may start inside the plugin rather than the project.
    for candidate in [root, *list(root.parents)[:4]]:
        if is_shopware_project(candidate):
            print(NOTICE)
            return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
