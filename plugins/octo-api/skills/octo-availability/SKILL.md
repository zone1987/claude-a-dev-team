---
name: octo-availability
description: 'OCTO/Ventrata availability: POST /availability, /availability/calendar, availabilityId, capacity. Use when a request names OCTO or Ventrata availability, availabilityId, or calendar.'
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

**It is bound to its day, which matters when a guest changes their mind.** The id identifies one
departure on one date, so an id held while the guest picks a different date belongs to a day they
are no longer buying. Ask availability again and take the new id; there is no way to "move" one.

## availabilityType shapes the answer

The product's `availabilityType` decides what a response means:

- **START_TIME**: each entry is a departure or admission slot with its own capacity.
- **OPENING_HOURS**: each entry is a day with an opening window; the `openingHours` array carries
  the periods.

Read the product first. Interpreting an `OPENING_HOURS` response as slots is the classic error.

**An `OPENING_HOURS` product still needs an `availabilityId`.** `POST /bookings` requires one
whatever the type, and such a product gets its single all-day availability from the same
`POST /availability` call. A client that only calls availability where it has a time field to fill
leaves those products unbookable.

**Measured over one live Ventrata catalogue:** 250 `START_TIME` against 58 `OPENING_HOURS`
products. Both are common enough that neither can be treated as the exception.

## Capacity and freesale

`vacancies` and `capacity` may be `null` — that means unlimited, not zero. Combined with the
product's `allowFreesale`, a `null` capacity is normal for freesale products. Call availability even
for freesale products: you still need the `availabilityId`.

## Three different ceilings, on three different levels

The specification describes `maxUnits` as "Max units numeric value" wherever it appears, which
says nothing about what it limits. There are three separate limits, they mean different things,
and a booking has to satisfy all of them:

| Field | Where | Limits |
|---|---|---|
| `UnitRestrictions.maxQuantity` | `Option.units[]` | how many of **that one fare** |
| `OptionRestrictions.maxUnits` | `Option.restrictions` | the **whole booking**, whatever the date |
| `Availability.maxUnits` | the chosen availability | the **whole booking**, on that departure |

**The two `maxUnits` count every unit item together, not per fare.** Two adults and a child is
three units against a `maxUnits` of 3, not one fare of two and one of one. A client that checks
each fare against it separately lets a basket through that the booking endpoint then refuses.

**`maxUnits` is a rule, `vacancies` is a fact.** `maxUnits` caps how large one order may be and
holds on an empty vehicle; `vacancies` is what is physically left. They are unrelated numbers and
either may be the smaller one — take the minimum of whichever are present.

**Only `vacancies` is scarcity.** Showing "only 3 left" because `maxUnits` is 3 tells a guest a
departure is nearly full when it may be empty. Where a storefront advertises remaining places,
that sentence is owed to `vacancies` alone.

### What the two look like in practice

Measured over one live Ventrata catalogue (Golden Tours, 82 stored availabilities, 1437 calendar
days). Numbers from one supplier, so read them as a shape rather than as a constant:

| Field | Filled | Range |
|---|---|---|
| `Availability.vacancies` | 74 of 82 | 9–223, mean 106 |
| `Availability.maxUnits` | 57 of 82 | 9–90, nearly all 76–90 |
| `Availability.capacity` | 75 of 82 | — |
| `AvailabilityCalendar.vacancies` | 809 of 1437 | 0–1858 |
| `OptionRestrictions.maxUnits` | 102 options | 1–50 |

**The binding ceiling is usually the option, not the availability.** `OptionRestrictions.maxUnits`
runs 1–50 here while the availability's sits at 76–90, so the departure's own limit rarely bites.
Only **4 of 74** availabilities had 20 or fewer places left. A client that reads only the
availability therefore lets most over-large baskets through.

**A calendar day's `vacancies` of 0 does occur**, unlike the availability's, and it is a real
sold-out day rather than the null-means-unlimited case.

## An empty calendar answer is not an empty month

A calendar response has three meanings and two of them look identical:

| Answer | Means |
|---|---|
| days, some bookable | the ordinary case |
| days, none bookable | the supplier closed that month — say so |
| **an empty list** | the supplier serves no calendar endpoint at all |

Reading the third as the second closes a shop that sells perfectly well. Where the answer is empty,
disable nothing and show no notice: only `POST /availability` can say whether a given day sells.
Not every OCTO implementation serves `/availability/calendar`, and there is no capability that
declares whether it does — feature-detect instead.

## Reference map

- **[ENDPOINTS.md](references/ENDPOINTS.md)**: all six endpoints with their request bodies and parameters.
- **[AVAILABILITY-SCHEMA.md](references/AVAILABILITY-SCHEMA.md)**: the `Availability` object.
- **[AVAILABILITY-CALENDAR-SCHEMA.md](references/AVAILABILITY-CALENDAR-SCHEMA.md)**: the calendar variant.
- **[CAPABILITY-EXTENSIONS.md](references/CAPABILITY-EXTENSIONS.md)**: capability-gated availability fields.
- **[SUB-SCHEMAS-1.md](references/SUB-SCHEMAS-1.md)** and **[SUB-SCHEMAS-2.md](references/SUB-SCHEMAS-2.md)**: every
  referenced schema, including opening hours and pricing.

## Related

Call the Skill tool with "octo-products" for `availabilityType`, or "octo-bookings" to spend the
`availabilityId`.

## Source

Generated from the Ventrata OCTO `openapi.yaml` 3.0.3, sha256 `d7bec97a0a909277`, retrieved
2026-08-20 — see `scripts/extract_spec.py`. Narrative from
[docs.ventrata.com/octo-core/availability](https://docs.ventrata.com/octo-core/availability).
