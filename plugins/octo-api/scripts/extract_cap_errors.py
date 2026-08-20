#!/usr/bin/env python3
"""Collect capability-specific error codes from the documentation pages.

The OpenAPI document lists the ten protocol-wide error codes; the capability pages add their
own in prose and nowhere else. Those codes are exactly what a client has to switch on, so
they are extracted here rather than paraphrased, and each one keeps the sentence that says
when it fires.

The pages are the input, so pass a directory of `<capability>.md` files fetched with
`curl https://docs.ventrata.com/capabilities/<name>.md`.

Usage:
    extract_cap_errors.py --pages DIR [--out FILE] [--report]
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys

from extract_spec import PROSE

PLUGIN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE_RE = re.compile(r"`([A-Z][A-Z0-9]*(?:_[A-Z0-9]+){1,})`")
# Protocol-wide codes live in octo-protocol/ERRORS.md; do not restate them here.
PROTOCOL_CODES = {
    "INVALID_PRODUCT_ID", "INVALID_OPTION_ID", "INVALID_UNIT_ID", "INVALID_AVAILABILITY_ID",
    "INVALID_AVAILABILIY_ID", "INVALID_BOOKING_UUID", "BAD_REQUEST", "UNPROCESSABLE_ENTITY",
    "INTERNAL_SERVER_ERROR", "UNAUTHORIZED", "FORBIDDEN",
}
# Tokens that look like codes but are event names or enum members documented elsewhere.
NOT_ERRORS = {
    "BOOKING_UPDATE", "AVAILABILITY_UPDATE", "PRODUCT_UPDATE",
    "START_TIME", "OPENING_HOURS", "SOLD_OUT", "NO_SHOW", "ON_HOLD", "PDF_URL",
}
# Documentation page slug -> capability ID, where they differ.
PAGE_TO_CAP = {
    "gift-vouchers": "octo/gifts",
    "online-check-in": "octo/checkin",
    "card-payments": "octo/cardPayments",
}


# When each code fires, read off the capability pages. Curated rather than sliced out of the
# surrounding sentence: the pages introduce several codes in one bullet list, so automatic
# extraction produces text that starts mid-clause and runs into the next topic.
TRIGGERS: dict[str, str] = {
    # octo/adjustments
    "ADJUSTMENTS_INVALID_PER":
        "the adjustment's `per` value is not one of `BOOKING`, `UNIT`, `PERCENTAGE`",
    "ADJUSTMENTS_INVALID_NET_DISCOUNT":
        "the adjustment's `netDiscount` value is not one of the allowed modes",
    "ADJUSTMENTS_NET_DISCOUNT_NOT_ALLOWED":
        "a `netDiscount` was sent where the connection does not permit one",
    # octo/cardPayments
    "INVALID_CARD_ID": "the `cardId` sent does not exist",
    "GATEWAY_MISMATCH": "the gateway in the request does not match the one on the connection",
    "GATEWAY_INVALID_SOURCE":
        "`source` is not one of `POS`, `ECOM`, `MOTO` for this gateway",
    "GATEWAY_CURRENCY_MISMATCH":
        "the payment currency differs from the booking currency",
    "PAYMENT_PENDING":
        "the payment has not settled yet; poll rather than treating it as a failure",
    # octo/checkin
    "BOOKING_NOT_FOUND": "no booking matches the check-in lookup",
    # octo/extras
    "EXTRAS_QTY_LIMIT": "a booking-level extra exceeds its configured quantity limit",
    "EXTRAS_UNIT_QTY_LIMIT": "a unit-level extra exceeds its configured quantity limit",
    "EXTRAS_RETAIL_REQUIRED":
        "a custom-retail extra was sent without a `retail` amount",
    "EXTRAS_RETAIL_BELOW_MINIMUM":
        "the custom `retail` amount is below `restrictions.minCustomRetail`",
    "EXTRAS_RETAIL_ABOVE_MAXIMUM":
        "the custom `retail` amount is above `restrictions.maxCustomRetail`",
    # octo/gifts
    "GIFTS_FIELDS_REQUIRED": "a required gift field is missing from the request",
    # octo/pricing
    "PRICING_MATCH_REQUIRED":
        "the price sent does not match the current price; re-read availability and retry",
    # octo/questions
    "INVALID_QUESTION_ID": "the `questionId` sent is not one of the product's questions",
    # octo/rentals
    "INVALID_RENTAL_DURATION_ID":
        "the rental duration ID sent is not offered by the product",
    # octo/waivers
    "INVALID_WAIVER_ID": "`waiverId` does not match any entry in `product.waivers[]`",
    "WAIVER_ON_BOOKING_ONLY":
        "a `waiverId` was sent per unit item where the product requires it per booking",
    "WAIVER_ON_TICKET_ONLY":
        "a `waiverId` was sent at booking level where the product requires it per unit item",
}


def collect(pages_dir: str) -> dict[str, dict[str, str]]:
    """capability -> code -> the sentence that documents it."""
    out: dict[str, dict[str, str]] = {}
    for path in sorted(glob.glob(os.path.join(pages_dir, "*.md"))):
        slug = os.path.basename(path)[:-3]
        cap = PAGE_TO_CAP.get(slug, f"octo/{slug}")
        text = open(path, encoding="utf-8", errors="replace").read()
        found: dict[str, str] = {}
        for m in CODE_RE.finditer(text):
            code = m.group(1)
            if code in PROTOCOL_CODES or code in NOT_ERRORS or code in found:
                continue
            found[code] = TRIGGERS.get(code, "")
        if found:
            out[cap] = found
    return out


def render(data: dict[str, dict[str, str]]) -> str:
    total = sum(len(v) for v in data.values())
    out = ["# Capability error codes", ""]
    out.append("Error codes a capability adds on top of the ten protocol-wide codes in "
               "[ERRORS.md](ERRORS.md). They arrive in the same `400` body shape: `error` carries "
               "the code, `errorMessage` the localized text.")
    out.append("")
    out.append(f"{total} codes across {len(data)} capabilities. A code only ever appears when its "
               "capability is active, so switch on `error` and fall back on the protocol codes.")
    out.append("")
    out.append("## Contents")
    out.append("")
    for cap in sorted(data):
        anchor = cap.replace("/", "").lower()
        out.append(f"- [`{cap}`](#{anchor})")
    out.append("")
    for cap in sorted(data):
        out.append(f"## `{cap}`")
        out.append("")
        for code in sorted(data[cap]):
            why = data[cap][code]
            out.append(f"- **{code}**: fires when {why}." if why
                       else f"- **{code}**: documented on the capability page.")
        out.append("")
    out.append("## Source")
    out.append("")
    out.append("Extracted from the capability pages at "
               "[docs.ventrata.com/capabilities](https://docs.ventrata.com/capabilities), "
               "retrieved 2026-08-20, by `scripts/extract_cap_errors.py`. These codes are "
               "documented in prose only: the OpenAPI document does not list them.")
    out.append("")
    out.append(PROSE)
    out.append("")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pages", required=True)
    ap.add_argument("--out", default=os.path.join(
        PLUGIN, "skills", "octo-protocol", "CAPABILITY-ERRORS.md"))
    ap.add_argument("--report", action="store_true")
    args = ap.parse_args()

    if not os.path.isdir(args.pages):
        print(f"error: no such directory: {args.pages}", file=sys.stderr)
        return 1
    data = collect(args.pages)
    if args.report:
        for cap in sorted(data):
            print(f"{cap}: {sorted(data[cap])}")
        total = sum(len(v) for v in data.values())
        print(f"\n{total} codes across {len(data)} capabilities")
        no_trigger = sorted(c for v in data.values() for c, t in v.items() if not t)
        stale = sorted(c for c in TRIGGERS
                       if c not in {x for v in data.values() for x in v})
        if no_trigger:
            print(f"  without a documented trigger: {no_trigger}")
        if stale:
            print(f"  triggers for codes no longer on any page: {stale}")
        return 1 if stale else 0

    body = render(data)
    prose = ""
    if os.path.exists(args.out):
        old = open(args.out, encoding="utf-8").read()
        if PROSE in old:
            prose = old.split(PROSE, 1)[1]
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(body.rstrip("\n") + prose.rstrip("\n") + "\n" if prose else body)
    print(f"wrote {args.out} ({body.count(chr(10))} lines, "
          f"{sum(len(v) for v in data.values())} codes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
