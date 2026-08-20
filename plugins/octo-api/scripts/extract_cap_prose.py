#!/usr/bin/env python3
"""Extract the integration knowledge the capability pages hold and the specification does not.

Three things live only in the prose, and all three are what a client author needs:

  routes     which existing endpoints a capability extends
  paths      where the added fields actually appear in a payload
             (`availability.unitPricing[]`, `unitItems[].unit.pricing`)
  rules      the conditional behaviour — "if pricingPer is UNIT the price sits on the unit,
             if BOOKING it sits on the option" — plus the warning callouts

Output goes beside the generated field list for each capability, under the prose marker, so
regenerating the field list never destroys it.

Usage:
    extract_cap_prose.py --pages DIR [--capability pricing] [--report]
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys

PLUGIN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Capability page slug -> the reference file that documents it.
PAGE_TO_FILE = {
    "pricing": "octo-capabilities-commerce/PRICING.md",
    "offers": "octo-capabilities-commerce/OFFERS.md",
    "cart": "octo-capabilities-commerce/CART.md",
    "packages": "octo-capabilities-commerce/PACKAGES.md",
    "card-payments": "octo-capabilities-commerce/CARD-PAYMENTS.md",
    "gift-vouchers": "octo-capabilities-commerce/GIFTS.md",
    "adjustments": "octo-capabilities-commerce/ADJUSTMENTS.md",
    "redemption": "octo-capabilities-fulfilment/REDEMPTION.md",
    "extras": "octo-capabilities-fulfilment/EXTRAS.md",
    "pickups": "octo-capabilities-fulfilment/PICKUPS.md",
    "rentals": "octo-capabilities-fulfilment/RENTALS.md",
    "resources": "octo-capabilities-fulfilment/RESOURCES.md",
    "waivers": "octo-capabilities-fulfilment/WAIVERS.md",
    "questions": "octo-capabilities-fulfilment/QUESTIONS.md",
    "online-check-in": "octo-capabilities-fulfilment/CHECKIN.md",
    "webhooks": "octo-capabilities-platform/WEBHOOKS.md",
    "notifications": "octo-capabilities-platform/NOTIFICATIONS.md",
    "content": "octo-capabilities-platform/CONTENT.md",
    "mappings": "octo-capabilities-platform/MAPPINGS.md",
    "memberships": "octo-capabilities-platform/MEMBERSHIPS.md",
    "campaigns": "octo-capabilities-platform/CAMPAIGNS.md",
    "waitlists": "octo-capabilities-platform/WAITLISTS.md",
    "identities": "octo-capabilities-platform/IDENTITIES.md",
}
MARKER = "<!-- prose below this line is written by hand and preserved on regeneration -->"
SECTION = "## Integration notes"

ROUTE_RE = re.compile(r"`((?:GET|POST|PATCH|PUT|DELETE)(?:/(?:GET|POST|PATCH|PUT|DELETE))*\s+[^`\n]+)`")
PATH_RE = re.compile(r"`([a-z][A-Za-z]*(?:\.[a-zA-Z][A-Za-z]*|\[\])+[A-Za-z\[\]\.]*)`")
HINT_RE = re.compile(r"\{%\s*hint[^%]*%\}(.*?)\{%\s*endhint\s*%\}", re.S)
# "* `BOOKING_UPDATE`" and "* `START`: The starting location." — token lists and the
# per-value explanations that follow them. Both only exist in the prose.
TOKEN_BULLET_RE = re.compile(r"^\s*[*\-]\s+`([A-Za-z_][\w\.\[\]]*)`\s*(?::\s*(.+))?$", re.M)
# "`font`: `id`, `name`, `normalTtfUrl`, …" — a field list attached to a nested object.
FIELD_LIST_RE = re.compile(
    r"^\s*[*\-]\s+`([a-zA-Z][\w\.\[\]]*)`\s*:\s*((?:`[^`]+`(?:,\s*)?){2,})$", re.M)


def strip_noise(text: str) -> str:
    """Remove everything that is not prose: transclusions, code, images, GitBook tags.

    Hint blocks are extracted separately, so their markers must go too — otherwise a
    `{% hint %}` tag rides along inside a sentence and reaches the output.
    """
    text = re.sub(r"^> For the complete.*?\n", "", text, flags=re.M)
    text = re.sub(r"\{%\s*openapi.*?\{%\s*endopenapi\s*%\}", "", text, flags=re.S)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\{%[^%]*%\}", "\n", text)          # any remaining GitBook tag
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)  # links to their label
    return text


def collect(path: str) -> dict:
    raw = open(path, encoding="utf-8", errors="replace").read()
    text = strip_noise(raw)

    routes: list[str] = []
    for m in ROUTE_RE.finditer(text):
        r = " ".join(m.group(1).split())
        if r not in routes:
            routes.append(r)

    paths: list[str] = []
    for m in PATH_RE.finditer(text):
        p = m.group(1)
        if p not in paths and not p.endswith("."):
            paths.append(p)

    hints = [" ".join(h.split()) for h in HINT_RE.findall(raw)]

    # Token bullets: a value on its own, optionally with what it means.
    tokens: list[tuple[str, str]] = []
    for m in TOKEN_BULLET_RE.finditer(text):
        name, why = m.group(1), " ".join((m.group(2) or "").split())
        if "`" in (m.group(2) or ""):
            continue  # a field list, handled below
        if not any(name == t[0] for t in tokens):
            tokens.append((name, why))

    # Field lists: which properties a nested object carries.
    field_lists: list[tuple[str, list[str]]] = []
    for m in FIELD_LIST_RE.finditer(text):
        fields = re.findall(r"`([^`]+)`", m.group(2))
        if fields and not any(m.group(1) == f[0] for f in field_lists):
            field_lists.append((m.group(1), fields))

    # Conditional rules: sentences that make behaviour depend on a value.
    rules: list[str] = []
    for sentence in re.split(r"(?<=[.!])\s+(?=[A-Z`])", text):
        s = " ".join(sentence.split())
        if len(s) < 30 or len(s) > 300:
            continue
        if "{%" in s or "%}" in s:
            continue
        if re.match(r"^(If|When|Notice|Make sure|For |Using |Each |Batch |Throughout)", s) \
           or " must " in s or " only " in s or " instead" in s:
            if s not in rules:
                rules.append(s)
    return {"routes": routes, "paths": paths, "hints": hints, "rules": rules,
            "tokens": tokens, "fieldLists": field_lists}


def render(slug: str, data: dict) -> str:
    out = [SECTION, ""]
    out.append(f"Behaviour the specification does not carry, from "
               f"[docs.ventrata.com/capabilities/{slug}]"
               f"(https://docs.ventrata.com/capabilities/{slug}).")
    out.append("")
    if data["routes"]:
        out.append("### Routes this capability extends")
        out.append("")
        for r in data["routes"]:
            out.append(f"- `{r}`")
        out.append("")
    if data["paths"]:
        out.append("### Where the fields appear")
        out.append("")
        out.append("Payload paths the documentation names explicitly — useful when mapping a "
                   "response onto typed objects:")
        out.append("")
        for p in data["paths"]:
            out.append(f"- `{p}`")
        out.append("")
    if data["tokens"]:
        out.append("### Values named in the prose")
        out.append("")
        out.append("Event names, notification types and enum members the specification does not "
                   "declare:")
        out.append("")
        for name, why in data["tokens"]:
            out.append(f"- **{name}**" + (f": {why}" if why else "."))
        out.append("")
    if data["fieldLists"]:
        out.append("### Nested object fields")
        out.append("")
        for name, fields in data["fieldLists"]:
            out.append(f"- **{name}**: " + ", ".join(f"`{f}`" for f in fields) + ".")
        out.append("")
    if data["rules"]:
        out.append("### Rules and conditionals")
        out.append("")
        for r in data["rules"]:
            out.append(f"- {r}")
        out.append("")
    if data["hints"]:
        out.append("### Callouts")
        out.append("")
        for h in data["hints"]:
            out.append(f"- **{h}**")
        out.append("")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pages", required=True)
    ap.add_argument("--capability")
    ap.add_argument("--report", action="store_true")
    args = ap.parse_args()

    slugs = [args.capability] if args.capability else sorted(PAGE_TO_FILE)
    written = 0
    for slug in slugs:
        page = os.path.join(args.pages, f"{slug}.md")
        target = PAGE_TO_FILE.get(slug)
        if not os.path.exists(page) or not target:
            print(f"  skip {slug}: no page or no target")
            continue
        data = collect(page)
        counts = {k: len(v) for k, v in data.items()}
        if args.report:
            print(f"{slug:18} routes={counts['routes']:2} paths={counts['paths']:3} "
                  f"rules={counts['rules']:2} tokens={counts['tokens']:3} "
                  f"lists={counts['fieldLists']:2} hints={counts['hints']}")
            continue
        if not any(counts.values()):
            continue
        dest = os.path.join(PLUGIN, "skills", target)
        body = open(dest, encoding="utf-8").read()
        head = body.split(MARKER)[0] if MARKER in body else body
        with open(dest, "w", encoding="utf-8") as fh:
            fh.write(head.rstrip("\n") + "\n\n" + MARKER + "\n\n" + render(slug, data))
        written += 1
        print(f"  {target}: +{counts['routes']} routes, +{counts['paths']} paths, "
              f"+{counts['rules']} rules, +{counts['hints']} callouts")
    if not args.report:
        print(f"\nupdated {written} capability files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
