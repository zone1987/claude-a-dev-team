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
    # Normalise to a leading slash so a relative path matches the same tests as an absolute
    # one: Write and Edit both report whatever the caller passed.
    low = path.replace("\\", "/").lower()
    if not low.startswith("/"):
        low = "/" + low

    is_contao = (
        "/contao/dca/" in low
        or "/contao/templates/" in low
        or "/contao/languages/" in low
        or "/contao/config/" in low
        or "/controller/contentelement/" in low
        or "/controller/frontendmodule/" in low
        or ("/eventlistener/" in low and "/contao" in low)
        or low.endswith(".html5")  # legacy Contao templates
    )
    if not is_contao:
        return 0

    msgs = []
    if low.endswith(".php"):
        msgs.append("Contao PHP changed: check the coding standards (ECS, PHP-CS-Fixer) and "
                    "clear the cache where the change affects it (`contao:cache:clear`).")
    if "/contao/dca/" in low:
        msgs.append("DCA changed: a database change needs a migration, and the backend cache "
                    "needs clearing.")
    if low.endswith((".html.twig", ".html5")):
        msgs.append("Contao template changed: clear the template cache.")
    if msgs:
        print("[contao] " + " ".join(msgs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
