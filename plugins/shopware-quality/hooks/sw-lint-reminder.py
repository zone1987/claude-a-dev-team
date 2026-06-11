#!/usr/bin/env python3
"""
Shopware lint/catalog reminder (PostToolUse).

Conservative: only emits a short reminder when an edited file is clearly part of a
Shopware 6 project. Never blocks (always exit 0). Reads the hook payload from stdin.
"""
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

    p = path.replace("\\", "/")
    low = p.lower()

    # Only act inside a Shopware-ish location to avoid noise elsewhere.
    shopware_ctx = (
        "custom/plugins/" in low
        or "custom/static-plugins/" in low
        or "/resources/" in low
        or low.endswith("definition.php")
        or "/migration/" in low
        or "/src/core/" in low
        or "/src/storefront/" in low
        or "/src/administration/" in low
    )
    if not shopware_ctx:
        return 0

    msgs = []
    is_admin = "/administration/" in low
    is_storefront = "/storefront/" in low

    if low.endswith(".php"):
        msgs.append("PHP geändert → `composer ecs-fix` && `composer phpstan` ausführen.")
        if low.endswith("definition.php") or "/migration/" in low:
            msgs.append("DAL-/Schema-Änderung → Entity-Katalog via `/sw-entity-map` aktualisieren.")
    elif low.endswith(".scss"):
        side = "admin" if is_admin else ("storefront" if is_storefront else "admin|storefront")
        msgs.append(f"SCSS geändert → `composer stylelint:{side}:fix`.")
    elif low.endswith(".twig"):
        msgs.append("Twig geändert → `composer ludtwig:storefront` (Storefront).")
    elif low.endswith((".vue", ".ts", ".js")):
        if is_admin:
            msgs.append("Admin-JS/TS/Vue geändert → `composer eslint:admin:fix`; ggf. `/sw-admin-map` aktualisieren.")
        elif is_storefront:
            msgs.append("Storefront-JS/TS geändert → `composer eslint:storefront:fix`; ggf. `/sw-js-plugin-map` aktualisieren.")

    if msgs:
        print("[shopware] " + " ".join(msgs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
