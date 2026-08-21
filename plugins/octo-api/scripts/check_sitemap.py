#!/usr/bin/env python3
"""Map every documentation page to the plugin file that covers it.

"We left nothing out" is only a claim until every page in the sitemap points at a file. This
script fetches the sitemap, resolves each page to its coverage, and fails when a page has
none — so a page Ventrata adds later shows up as a gap instead of going unnoticed.

Usage:
    check_sitemap.py [--offline PATH] [--write]
"""
from __future__ import annotations

import argparse
import os
import re
import sys

from resolve_blob import fetch

PLUGIN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITEMAP = "https://docs.ventrata.com/sitemap-pages.xml"

# page path -> the skill files that carry it. A capability page maps to its own reference
# file; a core page maps to the whole domain skill it generated.
COVERAGE: dict[str, tuple[str, ...]] = {
    "": ("octo-protocol/SKILL.md",),
    "getting-started/steps-to-integrate": ("octo-protocol/INTEGRATION-STEPS.md",),
    "getting-started/glossary-of-terms": ("octo-protocol/GLOSSARY.md",),
    "getting-started/getting-started": ("octo-protocol/AUTHENTICATION.md",),
    "getting-started/test-credentials": ("octo-protocol/TESTING.md",),
    "getting-started/headers": ("octo-protocol/HEADERS.md",),
    "getting-started/errors": ("octo-protocol/ERRORS.md",
                               "octo-protocol/CAPABILITY-ERRORS.md"),
    "getting-started/localization": ("octo-protocol/LOCALIZATION.md",),
    "getting-started/request-capabilities": ("octo-protocol/CAPABILITY-DISCOVERY.md",),
    "octo-core/products": ("octo-products/SKILL.md", "octo-products/ENDPOINTS.md",
                           "octo-products/PRODUCT-SCHEMA.md"),
    "octo-core/availability": ("octo-availability/SKILL.md",
                               "octo-availability/ENDPOINTS.md"),
    "octo-core/bookings": ("octo-bookings/SKILL.md", "octo-bookings/ENDPOINTS.md",
                           "octo-bookings/AFTER-CONFIRMATION.md",
                           "octo-bookings/LISTING-BOOKINGS.md"),
    "capabilities/pricing": ("octo-capabilities-commerce/PRICING.md",),
    "capabilities/offers": ("octo-capabilities-commerce/OFFERS.md",),
    "capabilities/cart": ("octo-capabilities-commerce/CART.md",),
    "capabilities/packages": ("octo-capabilities-commerce/PACKAGES.md",),
    "capabilities/card-payments": ("octo-capabilities-commerce/CARD-PAYMENTS.md",),
    "capabilities/gift-vouchers": ("octo-capabilities-commerce/GIFTS.md",),
    "capabilities/adjustments": ("octo-capabilities-commerce/ADJUSTMENTS.md",),
    "capabilities/redemption": ("octo-capabilities-fulfilment/REDEMPTION.md",),
    "capabilities/extras": ("octo-capabilities-fulfilment/EXTRAS.md",),
    "capabilities/pickups": ("octo-capabilities-fulfilment/PICKUPS.md",),
    "capabilities/rentals": ("octo-capabilities-fulfilment/RENTALS.md",),
    "capabilities/resources": ("octo-capabilities-fulfilment/RESOURCES.md",),
    "capabilities/waivers": ("octo-capabilities-fulfilment/WAIVERS.md",),
    "capabilities/questions": ("octo-capabilities-fulfilment/QUESTIONS.md",),
    "capabilities/online-check-in": ("octo-capabilities-fulfilment/CHECKIN.md",),
    "capabilities/webhooks": ("octo-capabilities-platform/WEBHOOKS.md",),
    "capabilities/notifications": ("octo-capabilities-platform/NOTIFICATIONS.md",),
    "capabilities/content": ("octo-capabilities-platform/CONTENT.md",),
    "capabilities/mappings": ("octo-capabilities-platform/MAPPINGS.md",),
    "capabilities/memberships": ("octo-capabilities-platform/MEMBERSHIPS.md",),
    "capabilities/campaigns": ("octo-capabilities-platform/CAMPAIGNS.md",),
    "capabilities/waitlists": ("octo-capabilities-platform/WAITLISTS.md",),
    "capabilities/identities": ("octo-capabilities-platform/IDENTITIES.md",),
    # Context rather than integration detail: recorded in the plugin README, deliberately
    # not a skill, because it would cost listing budget for knowledge nobody codes against.
    "additional-resources/ventrata-clients": ("README.md",),
    "additional-resources/other-octo-implementations": ("README.md",),
    "additional-resources/support": ("README.md",),
    "additional-resources/faqs": ("README.md",),
}


def _resolve(f: str) -> str:
    """Locate a mapped file, whether it sits flat or under references/ (REF-04).

    The map records skill-relative paths like 'octo-protocol/HEADERS.md'. References moved into
    skills/<skill>/references/, so resolve both layouts rather than restating every path here:
    the mapping states which page a file covers, not where the file happens to live.
    """
    skill, _, base = f.partition("/")
    cands = [os.path.join(PLUGIN, "skills", f), os.path.join(PLUGIN, f)]
    if base:                       # a skill-relative path may have moved into references/
        cands.insert(0, os.path.join(PLUGIN, "skills", skill, "references", base))
    for cand in cands:
        if os.path.exists(cand):
            return cand
    return ""

def pages(offline: str = "") -> list[str]:
    xml = open(offline, encoding="utf-8").read() if offline else fetch(SITEMAP).decode("utf-8")
    return [
        u.replace("https://docs.ventrata.com", "").strip("/")
        for u in re.findall(r"<loc>([^<]+)</loc>", xml)
    ]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--offline", default="")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    found = pages(args.offline)
    uncovered, dangling, rows = [], [], []
    for page in found:
        files = COVERAGE.get(page)
        if not files:
            uncovered.append(page)
            continue
        missing = [f for f in files if not _resolve(f)]
        if missing:
            dangling.append((page, missing))
        rows.append((page, files))

    unknown = sorted(set(COVERAGE) - set(found))

    print(f"{len(rows)}/{len(found)} documentation pages mapped to a plugin file")
    for p in uncovered:
        print(f"  UNCOVERED: {p}")
    for p, m in dangling:
        print(f"  DANGLING:  {p} -> {m}")
    for p in unknown:
        print(f"  STALE:     {p} is mapped but no longer in the sitemap")

    if args.write:
        out = os.path.join(PLUGIN, "skills", "octo-protocol", "DOCUMENTATION-MAP.md")
        lines = ["# Documentation map", "",
                 f"Every one of the {len(found)} pages in Ventrata's sitemap, and where this "
                 "plugin covers it. Regenerate with `scripts/check_sitemap.py --write`.", "",
                 "| Documentation page | Covered by |", "|---|---|"]
        for page, files in rows:
            url = f"https://docs.ventrata.com/{page}" if page else "https://docs.ventrata.com"
            label = page or "(home)"
            lines.append(f"| [{label}]({url}) | " + ", ".join(f"`{f}`" for f in files) + " |")
        lines += ["", "## Source", "",
                  f"[{SITEMAP}]({SITEMAP}), retrieved 2026-08-20. Schema and endpoint detail "
                  "comes from the OpenAPI document those pages transclude; these files carry "
                  "the prose the specification does not contain.", ""]
        with open(out, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))
        print(f"wrote {out}")

    return 1 if uncovered or dangling or unknown else 0


if __name__ == "__main__":
    sys.exit(main())
