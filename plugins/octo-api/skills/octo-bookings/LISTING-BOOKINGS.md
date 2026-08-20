# Listing bookings

Rules for `GET /bookings` that the schema does not express: which filters are mandatory in
combination, and how pagination actually behaves.

## Contents

- [One primary filter is required](#one-primary-filter-is-required)
- [Status filter values](#status-filter-values)
- [Pagination](#pagination)

## One primary filter is required

`GET /bookings` will not return an unfiltered list. **Include exactly one filter from this set:**

| Filter | Selects by |
|---|---|
| `resellerReference` | your own reference |
| `supplierReference` | the supplier's reference |
| `localDate` | a single local travel date |
| `localDateStart` + `localDateEnd` | a local travel date range |
| `availabilityId` | one availability slot |
| `utcCreatedAtStart` + `utcCreatedAtEnd` | creation time |
| `utcUpdatedAtStart` + `utcUpdatedAtEnd` | last change |
| `utcRedeemedAtStart` + `utcRedeemedAtEnd` | redemption time |
| `utcNoshowedAtStart` + `utcNoshowedAtEnd` | no-show time |
| `utcRebookedAtStart` + `utcRebookedAtEnd` | rebooking time |
| `utcCancelledAtStart` + `utcCancelledAtEnd` | cancellation time |
| `contactEmailAddress` | guest email |
| `contactPhoneNumber` | guest phone |
| `contactLastName` | guest surname |

The `*Start` / `*End` pairs travel together — one half alone is not a valid primary filter. The
`local*` filters are travel dates in the product's time zone; the `utc*` filters are event
timestamps in UTC. Reconciliation runs on `utcCreatedAt*` or `utcUpdatedAt*`; a day sheet runs on
`localDate`.

## Status filter values

Ten values, applied on top of the primary filter:

`REDEEMED` · `NO_SHOW` · `ON_HOLD` · `CANCELLED` · `EXPIRED` · `PENDING` · `REJECTED` · `REBOOKED` ·
`QUOTE` · `CONFIRMED`

`ON_HOLD` is an unconfirmed reservation still holding capacity; `EXPIRED` is one that timed out.
Both are distinct from `CANCELLED`, which was actively cancelled. `QUOTE` never held capacity at
all.

## Pagination

- **`page` and `perPage`** are supported.
- **`Octo-Total-Pages`** is set as a response header while paginating — read the page count from
  there, not from the body.
- **Omitting `page` can return everything.** The API may aggregate all pages internally and answer
  with one combined array. Convenient for a small range, and a way to pull an unbounded response for
  a wide one: always send `page` when the range is open-ended.

## Source

[docs.ventrata.com/octo-core/bookings](https://docs.ventrata.com/octo-core/bookings), sections on
`GET /bookings` filters, status values and pagination, retrieved 2026-08-20.
