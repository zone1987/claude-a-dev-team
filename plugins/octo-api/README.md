# octo-api

Source of truth for the **OCTO API** (Open Connection for Tourism) — the open standard for tourism
ticketing maintained by [OCTO Standards NP Inc.](https://octo.travel), in the reference
implementation published by [Ventrata](https://docs.ventrata.com).

Every endpoint, parameter, schema field, enum value and capability attribution in this plugin is
**generated from the upstream OpenAPI document and machine-verified** — not written from memory.

## Coverage

| | Count |
|---|---:|
| Documentation pages covered | 39 of 39 |
| Operations | 65 of 65 |
| Paths | 46 |
| Schemas | 139 of 139 |
| Properties | 412 of 412 |
| Response schemas | 42 of 42 |
| Capability-gated fields | 254 |
| Capabilities | 23 of 23 |
| Enumerated values | 43 declared + 32 observed fields |
| Capability error codes | 21 |

Every field carries its type, whether it is **required or optional**, whether it is nullable, its
possible values where the specification declares them, and an example where one exists. Every
operation names the schema it returns per status code.

Three scripts hold that claim up:

- **`verify_spec.py`** — 22 checks in both directions: every specified schema, property, response
  body and operation is documented, and every documented field exists in the specification. The
  second direction is what prevents plausible-sounding invention.
- **`audit_pages.py`** — walks all 39 pages of Ventrata's documentation and reports any term the
  plugin does not mention. Currently 1,162 of 1,162.
- **`check_sitemap.py`** — maps every sitemap entry to the file covering it, so a page Ventrata adds
  later surfaces as a gap instead of going unnoticed. Output: `skills/octo-protocol/DOCUMENTATION-MAP.md`.

Every field carries its type, whether it is **required or optional**, whether it is nullable, its
possible values where they are known, and an example where the specification gives one. Every
operation names the schema it returns per status code.

## Skills

Eight skills, costing 2,376 characters of the skill listing budget — about 30 % of the 8,000
available at a 200k context.

| Skill | Covers |
|---|---|
| `octo-protocol` | Auth, the mandatory `Octo-Capabilities` header, all 10 error codes, capability discovery, localization |
| `octo-products` | `GET /products`, Product / Option / Unit schemas, every field and enum |
| `octo-availability` | The six availability endpoints, `availabilityId`, capacity, opening hours |
| `octo-bookings` | reserve → confirm → cancel, plus update and extend; `Booking` and `BookingUnitItem` |
| `octo-capabilities-commerce` | `octo/pricing`, `offers`, `cart`, `packages`, `cardPayments`, `gifts`, `adjustments` |
| `octo-capabilities-fulfilment` | `octo/redemption`, `extras`, `pickups`, `rentals`, `resources`, `waivers`, `questions`, `checkin` |
| `octo-capabilities-platform` | `octo/webhooks`, `notifications`, `content`, `mappings`, `memberships`, `campaigns`, `waitlists`, `identities` |
| `octo-gocity` | Go City Trade API as a delta overlay: what it omits, changes or inverts |

Each skill's `SKILL.md` is a map; the detail sits in flat sibling files (`ENDPOINTS.md`,
`PRODUCT-SCHEMA.md`, `CAPABILITY-EXTENSIONS.md`, …) loaded only when needed.

## Agent and commands

- **`octo-integrator`** (sonnet) — integration specialist. Preloads `octo-protocol` and
  `octo-products`, reaches the rest on demand, and has no write access.
- **`/octo-lookup <endpoint|schema|field|capability>`** (haiku) — prints parameters, required flags
  and a `curl` example. Add `--vendor gocity` for the overlay.
- **`/octo-spec-sync --check | --apply`** (sonnet) — detects upstream drift and regenerates.

## Automatic activation

A `UserPromptSubmit` hook points Claude at these skills, but **only on brand anchors**: `octo`,
`octo/*`, `Octo-Capabilities`, `Octo-Env`, `ventrata`, `go city`, `/octo/`, `availabilityId`,
`X-Capabilities`.

It deliberately ignores generic commerce vocabulary — `product`, `booking`, `availability`,
`pricing`, `cart`, `unit`, `option` — because those are everyday words in e-commerce work. A prompt
about a Shopware product entity does not load this plugin.

## Keeping it current

The specification URL is content-addressed: its hash changes whenever Ventrata publishes. Never
hardcode it.

```bash
python3 scripts/resolve_blob.py --download /tmp/octo-openapi.yaml
python3 scripts/verify_spec.py --spec /tmp/octo-openapi.yaml --all
```

`/octo-spec-sync --check` does both and reports drift by category. `--apply` regenerates the
references, preserving hand-written prose below each file's prose marker. State lives in
`.spec-state.json`.

## Regenerating by hand

```bash
# facts, from the specification
python3 scripts/extract_spec.py      --spec /tmp/octo-openapi.yaml --domain products
python3 scripts/extract_caps.py      --spec /tmp/octo-openapi.yaml --all
python3 scripts/extract_remaining.py --spec /tmp/octo-openapi.yaml   # run after the two above
python3 scripts/extract_enums.py     --spec /tmp/octo-openapi.yaml
python3 scripts/extract_gocity.py                                    # Go City's own spec

# prose, from the documentation pages (fetch them with curl first)
python3 scripts/extract_cap_errors.py --pages /tmp/caps
python3 scripts/extract_cap_prose.py  --pages /tmp/caps

# verify
python3 scripts/verify_spec.py   --spec /tmp/octo-openapi.yaml --all
python3 scripts/audit_pages.py   --pages /tmp/pages
python3 scripts/check_sitemap.py --write
```

Requires Python 3 with PyYAML. Content above a generated file's prose marker is overwritten on every
run — never edit it by hand.

## Other OCTO implementations

OCTO is an open standard, not a Ventrata product. Other implementers include **Peek Pro**, **Zaui**,
**Xola** and **Anchor**; **Go City** is covered here as an overlay. The standard itself lives at
[docs.octo.travel](https://docs.octo.travel) and
[github.com/octotravel](https://github.com/octotravel).

This plugin documents the generic OCTO specification as Ventrata implements it. Where another
provider deviates, expect the same pattern as `octo-gocity`: a delta overlay rather than a fork of
the base.

## Source

Generated from the Ventrata OCTO `openapi.yaml` (OpenAPI 3.0.3, version 1.0.0, server
`https://api.ventrata.com/octo`), sha256 `d7bec97a0a909277…`, retrieved 2026-08-20. Narrative
distilled from the 40 pages of [docs.ventrata.com](https://docs.ventrata.com).

Rights to the original documentation remain with Ventrata; the OCTO standard is maintained by OCTO
Standards NP Inc. The Go City OpenAPI document bundled in `skills/octo-gocity/` is published by
Go City in their Trade Partner Portal.
