#!/usr/bin/env python3
"""Gotenberg reminder (PostToolUse). Conservative: only fires when a written/edited file
clearly touches Gotenberg (a /forms/... route or a gotenberg client). Never blocks (exit 0).
Reads the hook payload from stdin."""
import json
import re
import sys


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    ti = payload.get("tool_input") or {}
    content = ti.get("content") or ti.get("new_string") or ""
    path = ti.get("file_path") or ti.get("path") or ""
    if not isinstance(content, str):
        content = ""
    blob = (content + "\n" + (path if isinstance(path, str) else "")).lower()

    touches_gotenberg = (
        "/forms/chromium/" in blob
        or "/forms/libreoffice/" in blob
        or "/forms/pdfengines/" in blob
        or "gotenberg" in blob
    )
    if not touches_gotenberg:
        return 0

    msgs = []
    # Route hygiene
    if "/forms/" in blob:
        msgs.append("Gotenberg-Aufruf erkannt → Route + Form-Feldnamen/Defaults gegen die `gotenberg-*`-Skills prüfen (multipart/form-data, Eingaben als `files`).")
    # Credentials leak check (public repo / shared code)
    if re.search(r"basic[_-]?auth|authorization:\s*basic|gotenberg_api_basic_auth_(username|password)", blob):
        if re.search(r"(password|passwort)\s*[:=]\s*['\"]?[^\s'\"]{3,}", blob) and "platzhalter" not in blob and "your-" not in blob and "changeme" not in blob:
            msgs.append("Mögliche Klartext-Credentials → als Secret/Env-Platzhalter auslagern, nichts Echtes committen.")
    # Output filename hint
    if "/forms/" in blob and "gotenberg-output-filename" not in blob:
        msgs.append("Tipp: Output-Dateiname per Header `Gotenberg-Output-Filename` setzen; lange Jobs ggf. async via Webhook (`Gotenberg-Webhook-Url`).")

    if msgs:
        print("[gotenberg] " + " ".join(msgs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
