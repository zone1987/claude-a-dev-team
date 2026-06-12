#!/usr/bin/env python3
"""Contao reminder (PostToolUse). Conservative: only fires for clearly-Contao files.
Never blocks (exit 0). Reads the hook payload from stdin."""
import json
import sys


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    ti = payload.get("tool_input") or {}
    path = ti.get("file_path") or ti.get("path") or ""
    if not isinstance(path, str) or not path:
        return 0
    low = path.replace("\\", "/").lower()

    is_contao = (
        "/contao/dca/" in low
        or "/contao/templates/" in low
        or "/contao/languages/" in low
        or "/contao/config/" in low
        or "/controller/contentelement/" in low
        or "/controller/frontendmodule/" in low
        or "/eventlistener/" in low and "/contao" in low
        or low.endswith(".html5")  # legacy Contao templates
    )
    if not is_contao:
        return 0

    msgs = []
    if low.endswith(".php"):
        msgs.append("Contao-PHP geändert → Coding-Standards prüfen (ECS/PHP-CS-Fixer) und ggf. Cache leeren (`contao:cache:clear` / `cache:clear`).")
    if "/contao/dca/" in low:
        msgs.append("DCA geändert → ggf. Migration für DB-Änderungen; Backend-Cache leeren.")
    if low.endswith((".html.twig", ".html5")):
        msgs.append("Contao-Template geändert → Template-Cache leeren.")
    if msgs:
        print("[contao] " + " ".join(msgs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
