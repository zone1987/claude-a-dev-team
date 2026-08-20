# Go City deltas

Every known difference from generic OCTO, by area. Ventrata is the reference implementation in the
right-hand column.

## Contents

- [Base configuration](#base-configuration)
- [Authentication](#authentication)
- [Capabilities](#capabilities)
- [Availability](#availability)
- [Products](#products)
- [Bookings](#bookings)
- [Endpoint coverage](#endpoint-coverage)

## Base configuration

| Aspect | Go City | Ventrata |
|---|---|---|
| Production base URL | `https://api.gocity.com` | `https://api.ventrata.com/octo` |
| Staging base URL | `https://api.staging.gocity.tech` | none — same host, `Octo-Env: test` |
| Path prefix | `/octo` on every route | `/octo` on every route |
| Specification | OpenAPI 3.1, published | OpenAPI 3.0.3, published |

The two-host model is the operational risk: an environment mix-up talks to production with a
staging token, or worse, sells for real while you believe you are testing.

## Authentication

| Aspect | Go City | Ventrata |
|---|---|---|
| Scheme | HTTP Bearer | HTTP Bearer |
| Token source | Connectivity Manager | Ventrata platform / account setup |
| Test mode | separate staging host and token | `Octo-Env: test` header |
| Transport | HTTPS only | HTTPS only |

## Capabilities

Go City supports exactly one: **`octo/pricing`**. The other 22 OCTO capabilities are not
implemented, so requesting them changes nothing.

| Aspect | Go City | Ventrata |
|---|---|---|
| Supported | `octo/pricing` only | all 23 |
| Header required | no | **yes** — omitting it returns `400` |
| Query alternative | `?_capabilities=octo/pricing` | none |
| Discovery endpoint | none | `GET /capabilities`, `GET /whoami` |

Write capability handling so the header is always sent (harmless on Go City, mandatory on Ventrata)
and so a missing capability field degrades rather than throws.

## Availability

| Aspect | Go City | Ventrata |
|---|---|---|
| Status values | always `FREESALE` | `AVAILABLE`, `FREESALE`, `SOLD_OUT`, `LIMITED`, `CLOSED` |
| Capacity | not meaningful | `capacity` / `vacancies`, `null` = unlimited |
| Calendar endpoint | not implemented | `POST /availability/calendar` (+ batch) |
| Batch endpoints | not implemented | `POST /availability/batch` |

**Still call availability.** A booking needs an `availabilityId`, and only availability issues one.
What you must not do is render capacity or a sold-out state from a Go City response.

## Products

| Aspect | Go City | Ventrata |
|---|---|---|
| Product concept | city passes: multiple destinations, brands, duration types | tours and activities |
| `availabilityType` | duration-based passes | `START_TIME` or `OPENING_HOURS` |
| Content fields | none (`octo/content` unsupported) | via `octo/content` |
| Itineraries | none | via `octo/content` |

## Bookings

| Aspect | Go City | Ventrata |
|---|---|---|
| Reserve → confirm | yes, same two-step flow | yes |
| Cancel | `POST /octo/bookings/{id}/cancel` | same, plus cutoff rules |
| Extend | not implemented | `POST /bookings/{uuid}/extend` |
| Update | not implemented | `PATCH /bookings/{uuid}` |
| Path parameter | `{id}` | `{uuid}` |

The parameter name differs (`{id}` vs `{uuid}`) even though both carry a booking identifier. Do not
build a shared URL template from the parameter name.

## Endpoint coverage

Go City implements 9 operations; the Ventrata specification has 65.

| Method | Path |
|---|---|
| `GET` | `/octo/products` |
| `GET` | `/octo/products/{id}` |
| `POST` | `/octo/availability` |
| `GET` | `/octo/bookings` |
| `POST` | `/octo/bookings` |
| `GET` | `/octo/bookings/{id}` |
| `POST` | `/octo/bookings/{id}/confirm` |
| `POST` | `/octo/bookings/{id}/cancel` |
| `GET` | `/octo/supplier` |

`GET /octo/supplier` exists only here — generic OCTO has no `/supplier` route and uses `GET /whoami`
instead, which Go City does not implement.

## Source

`gocity-openapi.json` (Go City Trade API V2, OpenAPI 3.1 — 9 operations, 23 schemas) for structure;
Go City partner documentation for behavioural notes. Compared against the Ventrata OCTO
`openapi.yaml` 3.0.3, sha256 `d7bec97a0a909277`, retrieved 2026-08-20.
