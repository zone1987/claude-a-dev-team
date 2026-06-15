#!/usr/bin/env python3
"""shadcn-vue reminder (PostToolUse). Conservative: only fires for files that clearly touch shadcn-vue.
Never blocks (exit 0). Reads the hook payload from stdin."""
import json
import os
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
    base = os.path.basename(low)

    is_components_json = base == "components.json"
    is_vue_comp = "/components/ui/" in low and low.endswith(".vue")
    uses = (
        "@/components/ui/" in content
        or "from \"@/lib/utils\"" in content
        or "from '@/lib/utils'" in content
        or "reka-ui" in content
    )
    is_css = base in ("globals.css", "app.css", "index.css", "style.css", "main.css", "tailwind.css")
    css_tokens = "--background" in content or "--primary" in content or "@theme" in content

    if not (is_components_json or is_vue_comp or uses or (is_css and css_tokens)):
        return 0

    msgs = []
    if is_vue_comp or uses:
        if re.search(r":class=\"`", content) and "cn(" not in content:
            msgs.append("Klassen besser über `cn()` aus `@/lib/utils` zusammenführen (clsx + tailwind-merge) statt Template-Strings.")
        if re.search(r"(bg|text|border)-(red|blue|green|zinc|slate|gray|neutral)-\d{2,3}", content):
            msgs.append("Feste Farb-Utilities gefunden — bevorzugt semantische Theme-Tokens (bg-background/text-foreground/bg-primary …).")
        if "radix-vue" in content:
            msgs.append("`radix-vue` ist veraltet → shadcn-vue nutzt jetzt `reka-ui` (Imports anpassen).")
    if is_components_json:
        msgs.append("components.json geändert → Aliase (@/components, @/lib/utils, composables), `style`, `tailwind.cssVariables`, `framework` prüfen; Komponenten via `npx shadcn-vue@latest add` holen.")
        if re.search(r"(token|secret|api[_-]?key)\s*[\"']?\s*:\s*[\"'][^\"']{6,}", content, re.I):
            msgs.append("Mögliche Credentials in components.json → Registry-Auth via Env-Var, nichts Echtes committen.")
    if is_css and css_tokens:
        if ".dark" not in content and ":root" in content:
            msgs.append("Theme-Tokens in :root, aber kein `.dark`-Block — Dark-Mode-Werte ergänzen.")

    if msgs:
        print("[shadcn-vue] " + " ".join(msgs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
