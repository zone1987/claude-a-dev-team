#!/usr/bin/env python3
"""Panther reminder (PostToolUse). Conservative: only fires for PHP files that use Panther.
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

    looks_panther = (
        "panthertestcase" in content.lower()
        or "createpantherclient" in content.lower()
        or "symfony\\component\\panther" in content.lower()
        or "createhttpbrowserclient" in content.lower()
    )
    is_phpunit_cfg = low.endswith("phpunit.xml.dist") or low.endswith("phpunit.xml")
    if not (looks_panther or is_phpunit_cfg):
        return 0

    msgs = []
    if looks_panther:
        # sleep() instead of waitFor*
        if re.search(r"\bsleep\s*\(", content) or re.search(r"\busleep\s*\(", content):
            msgs.append("`sleep()`/`usleep()` in Panther-Test → bei JS/AJAX `waitForVisibility`/`waitForElementToContain`/`waitFor` nutzen (stabiler).")
        # crawler methods not implemented in Panther
        if re.search(r"->(evaluate|parents|innerText|outerHtml)\s*\(", content):
            msgs.append("Achtung: Panthers Crawler implementiert `evaluate()`/`parents()`/`innerText()`/`outerHtml()` NICHT (wirft Exception) — Alternativen in `panther-crawler`.")
        # getElement without index
        if re.search(r"->getElement\s*\(\s*\)", content):
            msgs.append("`getElement()` braucht eine Position: `getElement(0)`.")
        # hardcoded credentials
        if re.search(r"(password|passwort|secret|token)\s*(=>|=|:)\s*['\"][^'\"]{4,}", content, re.I) and "getenv" not in content.lower():
            msgs.append("Mögliche Klartext-Credentials im Test → via `.env.test`/CI-Secret beziehen.")
    if is_phpunit_cfg and looks_panther is False:
        if "panther" in content.lower() and "serverextension" not in content.lower() and "ServerExtension" not in content:
            msgs.append("Panther in phpunit.xml: Extension registrieren (PHPUnit 10+: `Symfony\\Component\\Panther\\ServerExtension`).")

    if msgs:
        print("[panther] " + " ".join(msgs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
