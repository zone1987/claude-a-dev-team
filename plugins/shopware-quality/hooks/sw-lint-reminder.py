#!/usr/bin/env python3
"""
Shopware gate reminder (PostToolUse).

Conservative: only emits a short reminder when an edited file is clearly part of a
Shopware 6 project. Never blocks (always exit 0). Reads the hook payload from stdin.

The one command is `composer gate` — it runs the fixers and then every check, so nobody
has to remember the list. Individual tools are named only where the gate does not cover
them (Jest, Playwright, the asset build).
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
    is_spec = low.endswith((".spec.js", ".spec.ts"))

    if low.endswith(".php"):
        msgs.append("PHP changed -> run `composer gate` (fixers, then PHPStan max, style, Rector, stylelint, unit tests).")
        if low.endswith("definition.php"):
            msgs.append(
                "DAL definition -> every field needs setDescription(); no association may set autoload; "
                "refresh the entity catalogue with /sw-entity-map."
            )
        if "/migration/" in low:
            msgs.append("Migration -> schema in live shops is untouchable; refresh /sw-entity-map.")
        if "/tests/" in low:
            msgs.append("Test changed -> `composer coverage:all` is the figure that counts, measured not assumed.")
    elif low.endswith(".scss"):
        msgs.append("SCSS changed -> `composer lint:scss` is part of the gate; run `composer gate`.")
    elif low.endswith(".twig"):
        if is_admin:
            msgs.append("Admin template -> every mt-button carries size=\"default\"; the conventions spec enforces it.")
        else:
            msgs.append("Twig changed -> template behaviour is proved end to end, never by an integration test.")
    elif low.endswith((".vue", ".ts", ".js")):
        if is_admin:
            msgs.append(
                "Admin JS changed -> `composer test:admin` (Jest, 100 % on all four metrics) "
                "and `npm --prefix src/Resources/app/administration run lint`."
            )
            if not is_spec:
                msgs.append("A spec lives beside the component and mounts it; assert rendered DOM, never wrapper.vm.")
            msgs.append("Rebuild with `ddev exec shopware-cli project admin-build --only-extensions <PluginName>`.")
        elif is_storefront:
            msgs.append(
                "Storefront JS changed -> Jest is mandatory as soon as storefront JavaScript exists; "
                "`npm --prefix src/Resources/app/storefront run lint`."
            )
            msgs.append("Rebuild with `ddev exec shopware-cli project storefront-build --only-extensions <PluginName>`.")
    elif low.endswith((".xml",)) and "/resources/config/" in low:
        msgs.append(
            "XML service definitions are @deprecated tag:v6.8.0 -> register services in "
            "services.php plus services/*.php, explicitly and without autowiring."
        )

    if msgs:
        print("[shopware] " + " ".join(msgs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
