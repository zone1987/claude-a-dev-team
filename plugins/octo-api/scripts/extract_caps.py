#!/usr/bin/env python3
"""Generate the capability-group reference files.

A capability is documented by two things the specification alone cannot give: the exact header
value, and which schemas it widens. Both are derived here from the spec's machine-readable
attribution ("From capability `octo/x`"), so a capability's field list cannot drift.

Usage:
    extract_caps.py --spec openapi.yaml --group commerce [--out DIR]
    extract_caps.py --spec openapi.yaml --all --out-root ../skills
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys

import octo_spec as S
from extract_spec import GEN, PROSE, enrich, enum_owners, field_line, toc

# Grouped by where they land in an integration project: money first, then operations, then
# platform plumbing. Keeps the three biggest capabilities (pickups, offers, pricing) apart.
GROUPS: dict[str, dict] = {
    "commerce": {
        "skill": "octo-capabilities-commerce",
        "caps": ["octo/pricing", "octo/offers", "octo/cart", "octo/packages",
                 "octo/cardPayments", "octo/gifts", "octo/adjustments"],
    },
    "fulfilment": {
        "skill": "octo-capabilities-fulfilment",
        "caps": ["octo/redemption", "octo/extras", "octo/pickups", "octo/rentals",
                 "octo/resources", "octo/waivers", "octo/questions", "octo/checkin"],
    },
    "platform": {
        "skill": "octo-capabilities-platform",
        "caps": ["octo/webhooks", "octo/notifications", "octo/content", "octo/mappings",
                 "octo/memberships", "octo/campaigns", "octo/waitlists", "octo/identities"],
    },
}

# Documentation page slug per capability, for citation. Three differ from the ID.
PAGES = {
    "octo/pricing": "pricing", "octo/offers": "offers", "octo/cart": "cart",
    "octo/packages": "packages", "octo/cardPayments": "card-payments",
    "octo/gifts": "gift-vouchers", "octo/adjustments": "adjustments",
    "octo/redemption": "redemption", "octo/extras": "extras", "octo/pickups": "pickups",
    "octo/rentals": "rentals", "octo/resources": "resources", "octo/waivers": "waivers",
    "octo/questions": "questions", "octo/checkin": "online-check-in",
    "octo/webhooks": "webhooks", "octo/notifications": "notifications",
    "octo/content": "content", "octo/mappings": "mappings",
    "octo/memberships": "memberships", "octo/campaigns": "campaigns",
    "octo/waitlists": "waitlists", "octo/identities": "identities",
}

INTERNAL = {"octo/identities"}

# Schemas that belong to a capability by name but carry no capability marker of their own.
# CardPayment* is the clearest case: eight schemas, fifty fields, no `From capability`
# marker anywhere — so they would only ever surface in the catch-all file, far from the
# capability a client author is reading about.
OWNED_BY_PREFIX: dict[str, tuple[str, ...]] = {
    "octo/cardPayments": ("CardPayment", "ReusableCard"),
    "octo/checkin": ("CheckIn",),
    "octo/redemption": ("Redemption",),
    "octo/waitlists": ("Waitlist",),
    "octo/gifts": ("Gift",),
    "octo/cart": ("Order", "Cart"),
    "octo/memberships": ("Membership",),
    "octo/identities": ("Identity",),
    "octo/mappings": ("Mapping",),
    "octo/offers": ("Offer",),
    "octo/webhooks": ("Webhook",),
    "octo/notifications": ("Notification",),
    "octo/campaigns": ("Campaign",),
    "octo/pickups": ("Pickup",),
    "octo/questions": ("Question",),
    "octo/waivers": ("Waiver",),
    "octo/rentals": ("Rental",),
    "octo/resources": ("Resource",),
    "octo/extras": ("Extra",),
    "octo/packages": ("Package",),
    "octo/adjustments": ("Adjustment",),
    "octo/pricing": ("Pricing", "UnitPricing", "ExtraPricing"),
}

# Capabilities that add endpoints of their own, not just schema fields. Without this the
# reference would silently omit whole route families.
CAP_PATHS: dict[str, tuple[str, ...]] = {
    "octo/webhooks": ("/webhooks",),
    "octo/notifications": ("/notifications",),
    "octo/redemption": ("/redemption",),
    "octo/waitlists": ("/waitlists",),
    "octo/cart": ("/carts", "/orders"),
    "octo/gifts": ("/gifts",),
    "octo/memberships": ("/memberships",),
    "octo/identities": ("/identities",),
    "octo/mappings": ("/mappings",),
    "octo/offers": ("/offers",),
    "octo/resources": ("/resources", "/availability/resources"),
    "octo/checkin": ("/checkin",),
    "octo/cardPayments": ("/card_payments",),
    "octo/campaigns": ("/campaigns",),
    "octo/extras": ("/extras",),
    "octo/questions": ("/questions",),
    "octo/waivers": ("/waivers",),
    "octo/pickups": ("/pickups",),
    "octo/rentals": ("/rentals",),
    "octo/packages": ("/packages",),
}


def cap_operations(spec: dict, cap: str) -> list[dict]:
    prefixes = CAP_PATHS.get(cap, ())
    if not prefixes:
        return []
    return S.operations(
        spec, lambda p: any(p == x or p.startswith(x + "/") for x in prefixes)
    )


def cap_filename(cap: str) -> str:
    """octo/cardPayments -> CARD-PAYMENTS.md"""
    name = cap.split("/", 1)[1]
    out = []
    for i, ch in enumerate(name):
        if ch.isupper() and i:
            out.append("-")
        out.append(ch.upper())
    return "".join(out) + ".md"


def render_cap(spec: dict, cap: str, sha: str) -> tuple[str, dict]:
    """One file per capability: header value, the schemas it widens, every added field."""
    idx = S.capability_index(spec).get(cap, {})
    sch = S.schemas(spec)
    registry = S.enum_registry(spec)
    owners = enum_owners(spec)
    page = PAGES.get(cap, cap.split("/", 1)[1])
    total = sum(len(v) for v in idx.values())

    out = [GEN.format(sha=sha[:16]), "", f"# `{cap}`", ""]
    out.append(f"Add `{cap}` to the `Octo-Capabilities` header to receive these fields.")
    out.append("")
    if cap in INTERNAL:
        out.append("**Internal capability.** It is not returned by `GET /capabilities` and is not "
                   "available to a normal reseller connection.")
        out.append("")
    ops = cap_operations(spec, cap)

    # Schemas that exist only under this capability, declared on the schema itself rather
    # than per field. These are the response bodies an integrator parses, so they must be
    # rendered in full — not merely named.
    prefixes = OWNED_BY_PREFIX.get(cap, ())
    own = {
        n: sc
        for n, sc in sch.items()
        if n not in idx
        and (S.schema_capability(sc) == cap
             or (prefixes and n.startswith(prefixes) and not S.schema_capability(sc)))
    }
    if total:
        out.append(f"{total} fields across {len(idx)} schemas. The fields are additive: the base "
                   "schemas are unchanged when the capability is absent.")
        out.append("")
    if ops:
        out.append("## Endpoints")
        out.append("")
        out.append(f"This capability unlocks {len(ops)} endpoint(s).")
        out.append("")
        for o in ops:
            line = f"- **`{o['method']} {o['path']}`**"
            if o["summary"]:
                line += f": {o['summary'].rstrip('.')}."
            if o["requestBody"]:
                line += f" Body `{o['requestBody']}`."
            out.append(line)
            for prm in o["params"]:
                bits = [prm["type"], f"in {prm['in']}"]
                if prm["required"]:
                    bits.append("required")
                d = " ".join((prm["description"] or "").split())
                out.append(f"  - **{prm['name']}** ({', '.join(bits)})"
                           + (f": {d.rstrip('.')}." if d else "."))
        out.append("")
    if own:
        out.append("## Schemas introduced by this capability")
        out.append("")
        out.append(f"{len(own)} schema(s) exist only when `{cap}` is active.")
        out.append("")
        for n in sorted(own):
            sc = own[n]
            if S.is_array(sc):
                item = S.array_item(sc)
                out.append(f"### `{n}`")
                out.append("")
                out.append(f"Array of [`{item}`](#{item.lower()}) — a list response, no fields of "
                           "its own.")
                out.append("")
                continue
            base, _ = S.split_fields(sc)
            enrich(base, registry, owners)
            out.append(f"### `{n}`")
            out.append("")
            req = [f for f, i in base.items() if i["required"]]
            if req:
                out.append(f"Required: {', '.join(f'`{r}`' for r in req)}.")
                out.append("")
            for f, i in base.items():
                out.append(field_line(f, i))
            out.append("")

    if not total and not ops and not own:
        out.append("This capability adds no fields or endpoints to the specification: it changes "
                   "behaviour rather than shape. See the documentation page below.")
        out.append("")
    heads = ([f"`{n}`" for n in sorted(idx)] + (["Endpoints"] if ops else [])
             + (["Schemas introduced by this capability"] if own else []))
    if len(heads) > 3:
        out.insert(6, toc(heads) + "\n")
    fields_index: dict[str, list[str]] = {}
    for schema_name in sorted(idx):
        _, caps = S.split_fields(sch[schema_name])
        fields = caps.get(cap, {})
        if not fields:
            continue
        enrich(fields, registry, owners)
        fields_index[schema_name] = sorted(fields)
        out.append(f"## `{schema_name}`")
        out.append("")
        for f, i in fields.items():
            out.append(field_line(f, i))
        out.append("")
    out.append(f"## Source")
    out.append("")
    out.append(f"Field list generated from `openapi.yaml` 3.0.3, sha256 `{sha[:16]}`. "
               f"Narrative: [docs.ventrata.com/capabilities/{page}]"
               f"(https://docs.ventrata.com/capabilities/{page}).")
    out.append("")
    out.append(PROSE)
    out.append("")
    return "\n".join(out), fields_index


def build(spec: dict, group: str, sha: str) -> tuple[dict[str, str], dict]:
    cfg = GROUPS[group]
    files: dict[str, str] = {}
    index: dict = {"group": group, "specSha256": sha, "capabilities": {}}
    for cap in cfg["caps"]:
        body, fields = render_cap(spec, cap, sha)
        files[cap_filename(cap)] = body
        sch_all = S.schemas(spec)
        index["capabilities"][cap] = {
            "schemas": fields,
            "endpoints": sorted(
                f"{o['method']} {o['path']}" for o in cap_operations(spec, cap)
            ),
            "ownSchemas": sorted(
                n for n, sc in sch_all.items()
                if S.schema_capability(sc) == cap and n not in fields
            ),
        }
    return files, index


def write(files: dict[str, str], index: dict, out: str) -> None:
    os.makedirs(out, exist_ok=True)
    for name, body in files.items():
        path = os.path.join(out, name)
        prose = ""
        if os.path.exists(path):
            old = open(path, encoding="utf-8").read()
            if PROSE in old:
                prose = old.split(PROSE, 1)[1]
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(body.rstrip("\n") + prose.rstrip("\n") + "\n" if prose else body)
        print(f"wrote {path} ({body.count(chr(10))} lines)")
    with open(os.path.join(out, "FIELD-INDEX.json"), "w", encoding="utf-8") as fh:
        json.dump(index, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print(f"wrote {os.path.join(out, 'FIELD-INDEX.json')}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--spec", required=True)
    ap.add_argument("--group", choices=list(GROUPS))
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--out")
    ap.add_argument("--out-root")
    args = ap.parse_args()

    spec = S.load(args.spec)
    with open(args.spec, "rb") as fh:
        sha = hashlib.sha256(fh.read()).hexdigest()

    groups = list(GROUPS) if args.all else ([args.group] if args.group else [])
    if not groups:
        ap.error("give --group or --all")
    for g in groups:
        out = args.out or os.path.join(
            args.out_root
            or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "skills"),
            GROUPS[g]["skill"],
        )
        files, index = build(spec, g, sha)
        write(files, index, out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
