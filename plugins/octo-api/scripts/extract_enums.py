#!/usr/bin/env python3
"""Render the enumerated-value reference.

Knowing that a field is a string is not enough to integrate: an integrator needs the set of
values that can come back and what each one means. This script separates two cases, because
they carry different confidence:

  declared    the specification lists an `enum` — the set is closed and authoritative
  observed    the specification gives only a `type: string` plus an `example` — the value is
              real but the set is open, so treat unknown values as valid

Meanings are hand-maintained in MEANINGS below and verified against the spec on every run:
a meaning for a value the spec no longer has is an error, not a silent leftover.

Usage:
    extract_enums.py --spec openapi.yaml [--out DIR] [--report]
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys

import octo_spec as S
from extract_spec import GEN, PROSE

PLUGIN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Which fields carry a value set is decided by the VALUES, not by the field name: a name
# heuristic misses `error`, `environment`, `brand` and `verification`, all of which return
# tokens an integrator must switch on.
#
# A token is an identifier-shaped value rather than free text or an ID: SCREAMING_SNAKE
# (BAD_REQUEST, SOLD_OUT), a bare lowercase word (adyen, visa), or a short code (USD, en).
# Free prose, URLs, dates, UUIDs and numbers are excluded.
TOKEN = re.compile(
    r"""^(?:
        [A-Z][A-Z0-9]*(?:_[A-Z0-9]+)*   # BAD_REQUEST, SOLD_OUT, PDF_URL, US, USD
      | [a-z][a-z0-9]*                  # adyen, visa, text, kg, en
    )$""",
    re.X,
)
# Values that are shaped like tokens but are not a value set: booleans and placeholders.
NOT_A_VALUE = {"true", "false", "null", "string", "number", "object", "array"}
# Fields whose token-shaped example is an identifier or free-form code, not a closed set.
# Listing them would invite treating a customer-specific value as a protocol constant.
OPEN_IDENTIFIER = {
    "code", "offerCode", "redemptionCode", "unredeemableReasonCode", "reference",
    "internalName", "taxId", "value", "id", "productId", "optionId", "unitId",
    "supplierReference", "resellerReference", "availabilityId", "uuid",
}

# What each value means for an integrator. Sourced from the Ventrata documentation and the
# specification's own field descriptions. Values absent here still get listed.
MEANINGS: dict[str, str] = {
    # Availability.status
    "AVAILABLE": "capacity confirmed and countable; `vacancies` is meaningful",
    "LIMITED": "sellable but close to capacity; expect `vacancies` to be small",
    "SOLD_OUT": "no capacity left for this slot",
    "FREESALE": "sellable without capacity tracking; `vacancies` and `capacity` may be null",
    "CLOSED": "not operating on this date or slot, regardless of capacity",
    # Booking.status
    "ON_HOLD": "reserved but not confirmed; capacity is held and the reservation can expire",
    "CONFIRMED": "the sale is complete and the ticket issued",
    "CANCELLED": "actively cancelled, distinct from expiry",
    "EXPIRED": "the reservation timed out before confirmation",
    "REDEEMED": "the ticket was scanned and used",
    "NO_SHOW": "the guest did not arrive; set via the redemption capability",
    "PENDING": "awaiting an external step, typically payment",
    "REJECTED": "the supplier declined the booking",
    "REBOOKED": "superseded by another booking",
    "QUOTE": "priced but never held capacity",
    # Product.availabilityType
    "START_TIME": "timed slots with their own capacity; availability returns departures",
    "OPENING_HOURS": "open-window admission; availability returns days with opening periods",
    # pricingPer / waiverPer / Adjustment.per
    "UNIT": "applied once per unit item, so per person or per vehicle",
    "BOOKING": "applied once for the whole booking",
    "PERCENTAGE": "expressed as a percentage rather than an absolute amount",
    # netDiscount
    "NONE": "the discount does not reduce the net amount; the reseller absorbs it",
    "FULL": "the discount reduces the net amount in full; the supplier absorbs it",
    "SPLIT": "the discount is shared between supplier and reseller",
    "PRORATED": "the discount is distributed proportionally",
    "MANUAL": "the split is set by hand rather than by rule",
    # BookingCancellation.refund
    "PARTIAL": "part of the amount is refunded, typically after a cutoff",
    # CardPayment
    "adyen": "processed through Adyen; the `adyen` object carries gateway detail",
    "external": "processed outside OCTO; the `external` object carries the reference",
    "POS": "card present at a point of sale",
    "ECOM": "online, cardholder not present",
    "MOTO": "mail order or telephone order",
    # Question.inputType
    "text": "single-line free text",
    "textarea": "multi-line free text",
    "select": "one value from a list",
    "radio": "one value from a small set shown together",
    "checkbox": "boolean or multiple selection",
    "date": "a date value",
    "number": "a numeric value",
    # WebhookDiffOperation.op
    "add": "the field was added",
    "remove": "the field was removed",
    "replace": "the field's value changed",
    # weightUnit
    "kg": "kilograms",
    "lb": "pounds",
}

# Meanings for values the specification documents by example rather than by enum. Same
# provenance as MEANINGS, lower confidence in the value set: more values may exist.
# Values documented in the prose pages but never used as a spec example. They are real and
# an integrator will meet them, so they are listed as extra knowledge rather than dropped —
# and kept separate so the stale-meaning check stays meaningful.
FROM_PROSE: dict[str, dict[str, str]] = {
    "redemptionMethod": {
        "PRINT": "a printed ticket is checked",
        "MANIFEST": "no per-guest scan; the guest appears on a manifest list",
    },
    "environment": {
        "live": "live mode: a real sale",
    },
    "unitType": {
        "CHILD": "a child guest",
        "SENIOR": "a senior guest",
    },
    "durationUnit": {
        "DAY": "the amount is counted in days",
    },
    "status": {
        "ACTIVE": "in force and usable",
    },
}

OBSERVED_MEANINGS: dict[str, str] = {
    # settlementMethod / settlementMethods — how the supplier gets paid
    "DIRECT": "the reseller settles directly with the supplier for this booking",
    "DEFERRED": "settlement is deferred, typically invoiced periodically rather than per sale",
    # redemptionMethod — how a ticket is checked
    "DIGITAL": "scanned digitally, for example a QR code",
    "PRINT": "a printed ticket is checked",
    "MANIFEST": "no per-guest scan; the guest appears on a manifest list",
    # deliveryMethod / deliveryMethods
    "VOUCHER": "one ticket media object for the whole booking, at `booking.voucher`",
    "TICKET": "one ticket media object per unit item, at `booking.unitItems[].ticket`",
    # deliveryFormat
    "PDF_URL": "a link to a PDF document",
    "QRCODE": "a QR code payload",
    # duration and cutoff units
    "HOUR": "the amount is counted in hours",
    "MINUTE": "the amount is counted in minutes",
    "DAY": "the amount is counted in days",
    # unitType / type
    "ADULT": "an adult guest",
    "CHILD": "a child guest",
    "SENIOR": "a senior guest",
    # generic status values seen on several objects
    "ACTIVE": "in force and usable",
    "STANDARD": "the default variant, with no special handling",
    "PERCENT": "expressed as a percentage",
    # error / errorCode — the machine-readable failure code; see ERRORS.md for all ten
    "BAD_REQUEST": "body malformed, a required field missing, or a wrong data type",
    "INVALID_OPTION_ID": "the `optionId` sent does not exist on that product",
    # Octo-Env / environment
    "test": "test mode: consumes no availability, barcodes stay inert, not invoiced",
    "live": "live mode: a real sale",
    # membership verification
    "VERIFIED": "the membership lookup was verified successfully",
    # currency fields — ISO 4217 codes, three letters
    "USD": "US dollar (ISO 4217)",
    "EUR": "euro (ISO 4217)",
    # locale fields — IETF language tags
    "en": "English (IETF language tag)",
    # country / countryCode — ISO 3166-1 alpha-2
    "US": "United States (ISO 3166-1 alpha-2)",
    # state — a subdivision code, not a status despite the field name
    "CA": "California: a subdivision code, not a status value",
    # card brand
    "visa": "Visa card scheme",
    # seat row
    "A": "a seat or coach row label",
    # tags — free-form labels a supplier attaches; these are the documented examples
    "gratuity": "the item is a gratuity",
    "optional": "the item is optional rather than included",
    "partner": "supplied by a partner",
    "vip": "a VIP variant",
}


def declared(spec: dict) -> dict[tuple[str, ...], dict]:
    """(field, value-set) -> {values, owners} for every enum the specification declares.

    Keyed by field AND value set, never by field name alone: `status` is a different enum on
    `Booking` than on `Availability`, and merging them produces a list where half the values
    are invalid for either use. Grouping by the value set keeps each enum whole while still
    collapsing the schemas that genuinely share one.
    """
    out: dict[tuple[str, ...], dict] = {}

    def add(field: str, values: list, owner: str) -> None:
        key = (field, *values)
        e = out.setdefault(key, {"field": field, "values": list(values), "owners": set()})
        e["owners"].add(owner)

    for name, schema in S.schemas(spec).items():
        base, caps = S.split_fields(schema)
        for f, i in list(base.items()) + [(k, v) for d in caps.values() for k, v in d.items()]:
            if i["enum"]:
                add(f, i["enum"], name)
    for op in S.operations(spec):
        for p in op["params"]:
            if p["enum"]:
                add(p["name"], p["enum"], f"{op['method']} {op['path']}")
    return out


def token_values(prop: dict) -> set[str]:
    """The token-shaped example values of a property, flattened across arrays."""
    found: set[str] = set()
    for ex in (prop.get("example"), (prop.get("items") or {}).get("example")):
        vals = ex if isinstance(ex, (list, tuple)) else ([ex] if ex not in (None, "") else [])
        for v in vals:
            sv = str(v)
            if TOKEN.match(sv) and sv.lower() not in NOT_A_VALUE:
                found.add(sv)
    return found


def observed(spec: dict, skip: set[str]) -> dict[str, dict]:
    """String fields with no enum whose examples are tokens: real values, open set.

    Selected by value shape rather than by field name, so nothing with a documented token
    value is missed.
    """
    out: dict[str, dict] = {}
    for name, schema in S.schemas(spec).items():
        for f, pr in (schema.get("properties") or {}).items():
            if not isinstance(pr, dict) or pr.get("enum") or f in skip:
                continue
            if f in OPEN_IDENTIFIER:
                continue
            is_str = str(pr.get("type", "")).startswith("string")
            is_str_arr = pr.get("type") == "array" and str(
                (pr.get("items") or {}).get("type", "")
            ).startswith("string")
            if not (is_str or is_str_arr):
                continue
            vals = token_values(pr)
            if not vals:
                continue
            e = out.setdefault(f, {"examples": set(), "owners": set()})
            e["owners"].add(name)
            e["examples"].update(vals)
    return out


def render(spec: dict, sha: str) -> str:
    dec = declared(spec)
    obs = observed(spec, {e["field"] for e in dec.values()})
    total = sum(len(v["values"]) for v in dec.values())

    out = [GEN.format(sha=sha[:16]), "", "# Enumerated values", ""]
    out.append("Every value an OCTO response can carry in a value-like field, and what it means.")
    out.append("")
    out.append("Two levels of confidence, kept apart on purpose:")
    out.append("")
    out.append("- **Declared** — the specification lists an `enum`. The set is closed: any other "
               "value is a protocol violation.")
    out.append("- **Observed** — the specification types the field as a plain string and gives an "
               "example. The value is real, but **the set is open**: handle unknown values instead "
               "of switching exhaustively.")
    out.append("")
    out.append("## Contents")
    out.append("")
    out.append("- [Declared enums](#declared-enums)")
    out.append("- [Observed values](#observed-values)")
    out.append("")
    out.append("## Declared enums")
    out.append("")
    out.append(f"{len(dec)} distinct value sets, {total} values. A field name can carry more "
               "than one set — `status` on a booking is not `status` on availability — so each "
               "set is listed against the schemas it applies to.")
    out.append("")
    # Group by field name so same-named enums sit together, then one heading per value set.
    by_field: dict[str, list] = {}
    for key, e in dec.items():
        by_field.setdefault(e["field"], []).append(e)
    for f in sorted(by_field):
        variants = sorted(by_field[f], key=lambda e: sorted(e["owners"]))
        for idx, e in enumerate(variants):
            owners = sorted(e["owners"])
            label = f"`{f}`"
            if len(variants) > 1:
                label += f" on `{owners[0]}`"
                if len(owners) > 1:
                    label += f" and {len(owners) - 1} more"
            out.append(f"### {label}")
            out.append("")
            out.append(f"On {', '.join(f'`{o}`' for o in owners)}.")
            if len(variants) > 1:
                others = [v for j, v in enumerate(variants) if j != idx]
                other_owners = ", ".join(f"`{sorted(v['owners'])[0]}`" for v in others)
                out.append("")
                out.append(f"**A different `{f}` enum exists on {other_owners}** — the values "
                           "below are not interchangeable with those.")
            out.append("")
            for v in e["values"]:
                m = MEANINGS.get(v)
                out.append(f"- **{v}**" + (f": {m}." if m else "."))
            out.append("")
    out.append("## Observed values")
    out.append("")
    out.append(f"{len(obs)} value-like fields the specification does not enumerate. The examples "
               "below are the values it documents; more are possible.")
    out.append("")
    for f in sorted(obs):
        e = obs[f]
        ex = sorted(e["examples"])
        owners = ", ".join(f"`{o}`" for o in sorted(e["owners"])[:6])
        more = "" if len(e["owners"]) <= 6 else f" and {len(e['owners']) - 6} more"
        out.append(f"### `{f}`")
        out.append("")
        out.append(f"On {owners}{more}. The specification does not enumerate this field, so "
                   "treat the set as open.")
        out.append("")
        if ex:
            for v in ex:
                # A value can appear both as a declared enum member elsewhere and as an
                # example here (CONFIRMED, ON_HOLD): reuse the meaning, never restate it.
                m = OBSERVED_MEANINGS.get(v) or MEANINGS.get(v)
                out.append(f"- **{v}**" + (f": {m}." if m else "."))
        else:
            out.append("- No value documented in the specification.")
        extra = {k: v for k, v in (FROM_PROSE.get(f) or {}).items() if k not in ex}
        for v, m in sorted(extra.items()):
            out.append(f"- **{v}**: {m}. Documented in the prose pages, not used as a "
                       "specification example.")
        out.append("")
    out.append("")
    out.append("## Source")
    out.append("")
    out.append(f"Value sets generated from the Ventrata OCTO `openapi.yaml` 3.0.3, sha256 "
               f"`{sha[:16]}`. Meanings distilled from "
               "[docs.ventrata.com](https://docs.ventrata.com) and the specification's own field "
               "descriptions; they are verified against the spec on every regeneration.")
    out.append("")
    out.append(PROSE)
    out.append("")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--spec", required=True)
    ap.add_argument("--out", default=os.path.join(PLUGIN, "skills", "octo-protocol"))
    ap.add_argument("--report", action="store_true")
    args = ap.parse_args()

    spec = S.load(args.spec)
    with open(args.spec, "rb") as fh:
        sha = hashlib.sha256(fh.read()).hexdigest()

    dec = declared(spec)
    obs = observed(spec, {e["field"] for e in dec.values()})
    live = {v for e in dec.values() for v in e["values"]}
    seen = live | {v for e in obs.values() for v in e["examples"]}
    known = {**MEANINGS, **OBSERVED_MEANINGS}
    prose = {v for d in FROM_PROSE.values() for v in d}
    stale = sorted(k for k in known if k not in seen and k not in prose)
    unexplained = sorted(v for v in seen if v not in known)

    if args.report:
        print(f"declared enum fields: {len(dec)}, values: {len(live)}")
        print(f"observed fields:      {len(obs)}")
        print(f"values total:         {len(seen)}, with a meaning: {len(seen) - len(unexplained)}")
        if unexplained:
            print(f"  without meaning: {unexplained}")
        if stale:
            print(f"  meanings for values not in the spec: {stale}")
        return 1 if stale else 0

    if stale:
        print(f"error: MEANINGS has {len(stale)} value(s) the spec no longer declares: {stale}",
              file=sys.stderr)
        return 1

    body = render(spec, sha)
    path = os.path.join(args.out, "ENUMERATED-VALUES.md")
    prose = ""
    if os.path.exists(path):
        old = open(path, encoding="utf-8").read()
        if PROSE in old:
            prose = old.split(PROSE, 1)[1]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body.rstrip("\n") + prose.rstrip("\n") + "\n" if prose else body)
    obs = observed(spec, {e["field"] for e in dec.values()})
    print(f"wrote {path} ({body.count(chr(10))} lines, {len(dec)} value sets, {len(obs)} observed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
