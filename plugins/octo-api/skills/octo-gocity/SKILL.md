---
name: octo-gocity
description: 'Go City Trade API as an OCTO overlay: what Go City omits, changes or inverts. Use when a request names Go City, gocity, or compares Ventrata with Go City.'
---

# Go City overlay

Go City implements OCTO, but only a subset of it, and with different semantics in several places.
**Read the base skills first, then apply these deltas.** Everything not listed here behaves as
generic OCTO.

## What Go City is

Go City sells **passes** — multi-attraction city passes with a validity duration — not tours with
departure times. That single difference explains most of the others: a pass has no capacity, so
availability is a formality, and there is no itinerary to describe.

## The four deltas that change your code

- **Only `octo/pricing`.** Of the 23 OCTO capabilities, Go City supports one. Requesting others is
  pointless. The header is also optional here, and a `?_capabilities=octo/pricing` query parameter
  works as an alternative — unlike Ventrata, where the header is mandatory and its absence returns
  a `400`.
- **Availability is always `FREESALE`.** Never `SOLD_OUT`, never `LIMITED`. Call availability
  anyway: you still need the `availabilityId` to book. Do not build a capacity display against it.
- **Separate hosts instead of `Octo-Env`.** Staging is `https://api.staging.gocity.tech`, production
  `https://api.gocity.com`, each with its own token. There is no `Octo-Env: test` switch, so a
  configuration mistake here talks to the wrong environment rather than making a test sale.
- **9 endpoints, not 65.** The core flow only. No cart, no redemption, no webhooks, no extras.

## One endpoint Ventrata does not have

`GET /octo/supplier` returns supplier details. Generic OCTO has no such route — it uses
`GET /whoami` and `GET /capabilities`, neither of which Go City implements. Feature-detect rather
than assuming either shape.

## Reference map

- **[DELTAS.md](references/DELTAS.md)**: every difference by area — auth, capabilities, availability, products,
  bookings — with the Ventrata behaviour beside it.
- **[ENDPOINTS.md](references/ENDPOINTS.md)**: the 9 supported operations.
- **`gocity-openapi.json`**: the Go City OpenAPI 3.1 specification as published.

## Related

Call the Skill tool with "octo-protocol" for the base wire protocol, or "octo-products" for the
schemas Go City reuses.

## Source

[Go City Trade API V2 OpenAPI 3.1 specification](https://api.gocity.com) as published in the Trade
Partner Portal, bundled here as `gocity-openapi.json` — 9 operations, 23 schemas. Behavioural notes
distilled from Go City partner documentation. Go City is a separate OCTO implementer, unaffiliated
with Ventrata.
