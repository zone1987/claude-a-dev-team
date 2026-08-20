---
name: octo-bookings
description: 'OCTO/Ventrata booking lifecycle: reserve, confirm, update, cancel, extend, plus the Booking schema. Use when the request names OCTO or Ventrata bookings, reservations, or a booking uuid.'
---

# OCTO Bookings

A booking is created in two steps. Missing that is the most expensive mistake in an OCTO
integration: a reservation that is never confirmed expires and the sale is lost.

## The lifecycle

1. **`POST /bookings`** — reserve. Holds capacity and returns a booking with a `uuid`.
2. **`POST /bookings/{uuid}/confirm`** — confirm. Only now is the sale real and the ticket issued.
3. **`POST /bookings/{uuid}/cancel`** — cancel, subject to the option's cancellation cutoff.

Alongside those: **`PATCH /bookings/{uuid}`** to change a reservation before confirming,
**`POST /bookings/{uuid}/extend`** to push out the expiry of a held reservation,
**`GET /bookings`** to list and **`GET /bookings/{uuid}`** to read one.

`GET /bookings` requires one primary filter — an unfiltered list is not available. See
[LISTING-BOOKINGS.md](LISTING-BOOKINGS.md).

**`INVALID_BOOKING_UUID` on confirm usually means the reservation expired**, not that the UUID is
wrong. Reserve again rather than retrying the confirm.

## After a successful confirm

Five fields carry the outcome: `supplierReference` (give it to the guest — support and billing run
on it), then either `voucher` or `unitItems[].ticket` depending on `deliveryMethods`, and finally
`pricing.retail` against `pricing.net`. Amounts are in minor units, so `4600` at
`currencyPrecision: 2` is 46.00.

Charge `retail`, expect to be invoiced `net`; the difference is your margin.

## Read and write shapes differ

This is the second classic trap. `BookingUnitItem` — what you receive — requires `status` and
`uuid`. `BookingUnitItemWriteRequest` — what you send — requires only `unitId`. Do not post back a
unit item you read; construct the write shape.

## The uuid is yours to generate

You may supply the booking `uuid` on reserve, which makes the call idempotent: a retry with the same
UUID does not double-book. Generate one per checkout attempt and reuse it across retries.

## Reference map

- **[ENDPOINTS.md](ENDPOINTS.md)**: all seven operations with parameters and request bodies.
- **[BOOKING-SCHEMA.md](BOOKING-SCHEMA.md)**: the `Booking` object and its status values.
- **[BOOKING-UNIT-ITEM-SCHEMA.md](BOOKING-UNIT-ITEM-SCHEMA.md)**: `BookingUnitItem`, all fields.
- **[CAPABILITY-EXTENSIONS.md](CAPABILITY-EXTENSIONS.md)**: capability-gated booking fields.
- **[AFTER-CONFIRMATION.md](AFTER-CONFIRMATION.md)**: which fields to read once a booking is
  confirmed, `VOUCHER` versus `TICKET`, and the delivery-option shape.
- **[LISTING-BOOKINGS.md](LISTING-BOOKINGS.md)**: the mandatory primary filter for `GET /bookings`,
  all 10 status values, and how pagination really behaves.
- **[SUB-SCHEMAS-1.md](SUB-SCHEMAS-1.md)** and **[SUB-SCHEMAS-2.md](SUB-SCHEMAS-2.md)**: contact,
  ticket, voucher, pricing and every other referenced schema.

## Related

Call the Skill tool with "octo-availability" for the `availabilityId` a reservation needs, or
"octo-protocol" for the error contract.

## Source

Generated from the Ventrata OCTO `openapi.yaml` 3.0.3, sha256 `d7bec97a0a909277`, retrieved
2026-08-20 — see `scripts/extract_spec.py`. Narrative from
[docs.ventrata.com/octo-core/bookings](https://docs.ventrata.com/octo-core/bookings).
