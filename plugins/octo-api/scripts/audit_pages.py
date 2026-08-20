#!/usr/bin/env python3
"""Audit every documentation page against the plugin, term by term.

Coverage claims are worth only as much as the check behind them. This walks each page in the
sitemap, pulls out the terms a reader would look up — backticked identifiers, camelCase field
names, SCREAMING_CASE values — and reports which ones the plugin does not mention.

Pages are read from a local mirror so the audit is reproducible; fetch it with:

    for u in $(python3 -c "import re,sys;print(' '.join(re.findall(r'<loc>([^<]+)</loc>', open(sys.argv[1]).read())))" sitemap-pages.xml); do
        curl -sS "${u%/}.md" -o "$(echo "${u#https://docs.ventrata.com/}" | tr / _).md"
    done

Usage:
    audit_pages.py --pages DIR [--verbose] [--min N]
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys

PLUGIN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Terms a reader would search for. Everything else is prose.
BACKTICK = re.compile(r"`([^`\n]{3,44})`")
CAMEL = re.compile(r"\b([a-z]+[A-Z][A-Za-z]{2,})\b")
SCREAMING = re.compile(r"\b([A-Z]{3,}(?:_[A-Z0-9]+)*)\b")

STOP = set(
    "the a an and or of to in is are for with be this that it as on by from you your we our "
    "can will not if when use used using see also all any each per via has have had was were "
    "which what how why where who them they其".split()
)
# Terms deliberately not mirrored, with the reason. An explicit list beats a clever pattern:
# every exclusion here is a decision someone can review.
EXCLUDED: dict[str, str] = {
    # GitBook asset handles in image URLs — not API surface.
    "oIninjcb": "image asset id",
    "yVpqQMt": "image asset id",
    "xdXoTYcSROCBMIuEVetC": "image asset id",
    "qLWYrbujRt8AI43UnumY": "image asset id",
    "aVoBqTfgvdfWSPaPCpWX": "image asset id",
    # Ventrata's server-side Ruby helpers. The pages name them to explain why two responses
    # share a shape; a client author cannot call them.
    "serialize_booking(...)": "Ventrata server internal",
    "serialize_item(...)": "Ventrata server internal",
    "serialize_redemption(...)": "Ventrata server internal",
    "create_booking": "Ventrata server internal",
    "adyen-channel": "anchor slug on the card-payments page",
    # Customer names from the client list page: context, not integration detail.
    **{k: "client brand name" for k in
       ("CHICAGO", "CTCE", "EPIC", "FRS", "NOLA", "NYC", "SKY", "WWII", "COMING")},
    # Prose fragments the term extractor picks up as if they were identifiers.
    **{k: "prose fragment" for k in
       ("Lunch", "Shopping Break", "Subscription Object", "Redemption Object",
        "array[Redemption Object]", "(entries resolved to",
        "AvailabilityRequest (Custom Retail Extra)", "Booking (Custom Retail Extra)",
        "BookingWriteRequest (Custom Retail Extra)", "Option (Custom Retail Extra)",
        "BookingWriteRequest (Offline/In-Person)")},
    # Spelling variants of paths documented in canonical form.
    "booking.units[].ticket": "documented as unitItems[].ticket",
    "voucher.deliveryOptions[].deliveryValue": "documented as voucher.deliveryOptions",
    "pricingPer = UNIT": 'documented as pricingPer = "UNIT"',
    "membershipBenefit.title/description": "documented as separate title and description",
    "offer.title/description": "documented as separate title and description",
}
ACRONYMS = {"MDN", "CRUD", "JSON", "HTTP", "HTTPS", "URL", "URI", "API", "PDF", "PNG",
            "UUID", "ISO", "OTP", "POI", "UI", "PKPASS"}


def page_terms(text: str) -> set[str]:
    text = re.sub(r"^> For the complete.*?\n", "", text, flags=re.M)
    text = re.sub(r"\{%\s*openapi.*?\{%\s*endopenapi\s*%\}", "", text, flags=re.S)
    terms: set[str] = set()
    terms |= set(BACKTICK.findall(text))
    terms |= set(CAMEL.findall(text))
    terms |= set(SCREAMING.findall(text))
    out = set()
    for t in terms:
        t = t.strip()
        if (len(t) < 3 or t.lower() in STOP or t.startswith("http")
                or "/files/" in t or t.startswith(".gitbook")
                or t in EXCLUDED or t in ACRONYMS):
            continue
        out.add(t)
    return out


def plugin_text() -> str:
    parts = []
    for pattern in ("skills/*/*.md", "README.md", "CHANGELOG.md"):
        for f in glob.glob(os.path.join(PLUGIN, pattern)):
            parts.append(open(f, encoding="utf-8").read())
    return "\n".join(parts).lower()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pages", required=True)
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--min", type=int, default=1,
                    help="only list pages with at least N missing terms")
    args = ap.parse_args()

    plug = plugin_text()
    rows, total, missing_total = [], 0, 0
    for path in sorted(glob.glob(os.path.join(args.pages, "*.md"))):
        terms = page_terms(open(path, encoding="utf-8", errors="replace").read())
        missing = sorted(t for t in terms if t.lower() not in plug)
        total += len(terms)
        missing_total += len(missing)
        rows.append((os.path.basename(path)[:-3], len(terms), missing))

    pct = 100 * (total - missing_total) / total if total else 100
    print(f"{len(rows)} pages · {total} terms · {total - missing_total} covered "
          f"({pct:.1f}%) · {missing_total} missing")
    print()
    print(f"{'page':42} {'terms':>6} {'missing':>8}")
    print("-" * 60)
    for name, n, missing in rows:
        mark = "" if not missing else "  <-"
        print(f"{name:42} {n:6} {len(missing):8}{mark}")
        if args.verbose and len(missing) >= args.min:
            for t in missing:
                print(f"{'':44} {t}")
    print("-" * 60)
    print(f"{'TOTAL':42} {total:6} {missing_total:8}")
    return 0 if missing_total == 0 else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        sys.exit(0)
