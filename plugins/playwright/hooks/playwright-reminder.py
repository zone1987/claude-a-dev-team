#!/usr/bin/env python3
"""Playwright reminder (PostToolUse). Conservative: only fires for Playwright test/config files.
Never blocks (exit 0). Reads the hook payload from stdin."""
import json
import re
import sys


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    ti = payload.get("tool_input") or {}
    path = ti.get("file_path") or ti.get("path") or ""
    content = ti.get("content") or ti.get("new_string") or ""
    if not isinstance(path, str):
        path = ""
    if not isinstance(content, str):
        content = ""
    low = path.replace("\\", "/").lower()

    is_config = low.endswith("playwright.config.ts") or low.endswith("playwright.config.js") or low.endswith("playwright.config.mjs")
    is_test = bool(re.search(r"\.(spec|test)\.(ts|js|mjs|tsx|jsx)$", low)) or "/tests/" in low or "/e2e/" in low
    looks_pw = "@playwright/test" in content or "from 'playwright'" in content or 'from "playwright"' in content
    if not (is_config or is_test or looks_pw):
        return 0

    msgs = []
    if is_test or looks_pw:
        # hard waits / sleeps
        if re.search(r"waitForTimeout\s*\(", content) or re.search(r"page\.waitFor\(\s*\d", content):
            msgs.append("`waitForTimeout` or a fixed sleep: replace it with a web-first assertion (`await expect(locator)…`) or auto-waiting, which is what keeps the test from flaking.")
        # non-awaited expect
        if re.search(r"(?<!await )\bexpect\(\s*page\.", content) or re.search(r"(?<!await )\bexpect\(\s*locator", content):
            msgs.append("A web-first assertion without `await`: write `await expect(locator).…`, otherwise no auto-retry happens.")
        # brittle selectors
        if re.search(r"page\.\$\(|page\.\$\$\(|\$x\(", content):
            msgs.append("`page.$`, `$$` and `$x` are deprecated: use `page.locator()` or `getByRole()`.")
    if is_config:
        if "trace:" not in content:
            msgs.append("Consider `trace: 'on-first-retry'` in `use`, so a failure can be read in the Trace Viewer.")
        if re.search(r"(password|secret|token|api[_-]?key)\s*[:=]\s*['\"][^'\"]{4,}", content, re.I):
            msgs.append("Possible plaintext credentials in the config: move them to an env var or a CI secret.")

    if msgs:
        print("[playwright] " + " ".join(msgs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
