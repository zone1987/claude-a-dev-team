---
name: octo-availability
description: 'OCTO/Ventrata availability: POST /availability, /availability/calendar, availabilityId, capacity. Use when the request names OCTO or Ventrata availability, availabilityId, or calendar.'
---

# OCTO Availability

Availability sits between the catalogue and the booking, and it produces the one value a booking
cannot be made without: the `availabilityId`.

The documentation calls this the first step of a sale, and adds one caveat worth honouring: when a
product has `allowFreesale: true` the step is *optional*, **but still recommended — it is how you
detect closures and operational limits.** Skipping it means selling into a closed day.

## Everything is POST

All availability queries are `POST`, not `GET` — the query travels in a body, not a query string.

- **`POST /availability`** — availability for one product/option over a date range.
- **`POST /availability/calendar`** — day-level summary, for painting a month view.
- **`POST /availability/batch`** and **`POST /availability/calendar/batch`** — many products in one
  round trip. Prefer these over looping.
- **`GET`/`POST /availability/resources`** — resource-level availability (`octo/resources`).

## The availabilityId is opaque

It looks like a local timestamp with an offset, e.g. `2020-01-01T10:30+08:00`, but treat it as an
opaque string: **pass back exactly what you received.** Reformatting it, normalising to UTC or
dropping the offset produces `INVALID_AVAILABILITY_ID`.

## availabilityType shapes the answer

The product's `availabilityType` decides what a response means:

- **START_TIME**: each entry is a departure or admission slot with its own capacity.
- **OPENING_HOURS**: each entry is a day with an opening window; the `openingHours` array carries
  the periods.

Read the product first. Interpreting an `OPENING_HOURS` response as slots is the classic error.

## Capacity and freesale

`vacancies` and `capacity` may be `null` — that means unlimited, not zero. Combined with the
product's `allowFreesale`, a `null` capacity is normal for freesale products. Call availability even
for freesale products: you still need the `availabilityId`.

## Reference map

- **[ENDPOINTS.md](ENDPOINTS.md)**: all six endpoints with their request bodies and parameters.
- **[AVAILABILITY-SCHEMA.md](AVAILABILITY-SCHEMA.md)**: the `Availability` object.
- **[AVAILABILITY-CALENDAR-SCHEMA.md](AVAILABILITY-CALENDAR-SCHEMA.md)**: the calendar variant.
- **[CAPABILITY-EXTENSIONS.md](CAPABILITY-EXTENSIONS.md)**: capability-gated availability fields.
- **[SUB-SCHEMAS-1.md](SUB-SCHEMAS-1.md)** and **[SUB-SCHEMAS-2.md](SUB-SCHEMAS-2.md)**: every
  referenced schema, including opening hours and pricing.

## Related

Call the Skill tool with "octo-products" for `availabilityType`, or "octo-bookings" to spend the
`availabilityId`.

## Source

Generated from the Ventrata OCTO `openapi.yaml` 3.0.3, sha256 `d7bec97a0a909277`, retrieved
2026-08-20 — see `scripts/extract_spec.py`. Narrative from
[docs.ventrata.com/octo-core/availability](https://docs.ventrata.com/octo-core/availability).
