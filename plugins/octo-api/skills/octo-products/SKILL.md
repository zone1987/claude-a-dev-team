---
name: octo-products
description: 'OCTO/Ventrata product catalogue: GET /products, Product, Option and Unit schemas, all fields and enums. Use when the request names OCTO or Ventrata products, options, units, or availabilityType.'
---

# OCTO Products

The catalogue is the first step of every integration: it tells you what can be sold, in which
variants, and at which granularity. Product → Option → Unit, three levels deep.

## Endpoints

- **`GET /products`** — list everything sellable. 12 query parameters, none required.
- **`GET /products/{productId}`** — one product. 11 parameters.

**`Accept-Language` is required on `GET /products/{productId}` but not on `GET /products`.** That
asymmetry is easy to miss and returns a `400`. `Octo-Capabilities` is documented as an optional
parameter on the item endpoint, yet remains mandatory protocol-wide.

## Map or import — decide once

Either you map the products this API returns onto a catalogue you already have, or you import the
product list from here into your system. The documentation frames this as the integration's first
architectural choice, because everything downstream depends on where product identity lives.

If you map, **use `octo/mappings`.** Ventrata's own recommendation: a self-service mapping capability
that "substantially reduces the burden of maintaining mappings". Hand-maintained ID tables rot.

## The three levels

- **Product**: the sellable thing. Required: `id`, `internalName`. 23 base fields.
- **Option**: a variant of a product — a time slot pattern, a route, a package tier. Required:
  `id`. 21 base fields. Every product has at least a `default` option.
- **Unit**: who or what a ticket is for — adult, child, senior, vehicle. Required: `id`. 8 base
  fields, and `restrictions` carries the age and party-size limits.

## Enums

- **availabilityType**: `START_TIME` for timed slots, `OPENING_HOURS` for open-window admission.
  It decides how availability responses are shaped, so read it before calling availability.
- **pricingPer** (`octo/pricing`): `UNIT` or `BOOKING`.
- **waiverPer** (`octo/waivers`): `BOOKING` or `UNIT`.

## Capability fields arrive merged

Enabled capabilities merge their fields into the core product schema — there is no separate envelope
to unwrap. Read the **`Octo-Capabilities` response header** to see which were actually applied, and
treat any field it did not confirm as absent rather than null.

`GET /products/{productId}` adds no capability-specific query parameters of its own.

## Field counts

Product 23 base + 16 capability = 39. Option 21 + 13 = 34. Unit 8 + 6 = 14. These counts are
verified against the specification by `scripts/verify_spec.py`; if they no longer match, the
references are stale.

## Reference map

- **[ENDPOINTS.md](ENDPOINTS.md)**: both endpoints with every parameter, its `in`, type and rules.
- **[PRODUCT-SCHEMA.md](PRODUCT-SCHEMA.md)**: all 23 base fields of `Product`.
- **[OPTION-SCHEMA.md](OPTION-SCHEMA.md)**: all 21 base fields of `Option`, including the cutoff triplets.
- **[UNIT-SCHEMA.md](UNIT-SCHEMA.md)**: all 8 base fields of `Unit`.
- **[CAPABILITY-EXTENSIONS.md](CAPABILITY-EXTENSIONS.md)**: the 35 capability-gated fields across the three schemas.
- **[SUB-SCHEMAS-1.md](SUB-SCHEMAS-1.md)** and **[SUB-SCHEMAS-2.md](SUB-SCHEMAS-2.md)**: every referenced schema.

## Related

Call the Skill tool with "octo-protocol" for headers and error codes, or "octo-availability" for the
next step in the flow.

## Source

Generated from the Ventrata OCTO `openapi.yaml` 3.0.3, sha256 `d7bec97a0a909277`, retrieved
2026-08-20 — see `scripts/extract_spec.py`. Narrative from
[docs.ventrata.com/octo-core/products](https://docs.ventrata.com/octo-core/products).
