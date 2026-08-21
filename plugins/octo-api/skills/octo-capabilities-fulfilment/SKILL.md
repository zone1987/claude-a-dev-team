---
name: octo-capabilities-fulfilment
description: 'OCTO/Ventrata fulfilment capabilities: redemption, extras, pickups, rentals, resources, waivers. Use when a request names an octo/* fulfilment capability, e.g. octo/redemption.'
---

# OCTO fulfilment capabilities

Everything that happens between a confirmed booking and a delivered experience: scanning a ticket,
collecting a guest, signing a waiver, handing over equipment.

## The capabilities

- **octo/redemption** (6 endpoints): scan and redeem tickets, mark no-shows, and reverse both.
  Every operation has an inverse — `DELETE /redemption/redeem` unredeems. → [REDEMPTION.md](references/REDEMPTION.md)
- **octo/extras** (10 fields, 8 schemas): add-ons sold alongside a booking. → [EXTRAS.md](references/EXTRAS.md)
- **octo/pickups** (50 fields, 7 schemas): hotel and point pickups. The largest capability in the
  API by field count. → [PICKUPS.md](references/PICKUPS.md)
- **octo/rentals** (6 fields): rental durations and equipment. → [RENTALS.md](references/RENTALS.md)
- **octo/resources** (6 fields, 2 endpoints): capacity-bearing resources such as vehicles or
  guides, with their own availability endpoints. → [RESOURCES.md](references/RESOURCES.md)
- **octo/waivers** (17 fields, 5 schemas): liability waivers. `waiverPer` decides whether one
  waiver covers the booking or one is needed per unit. → [WAIVERS.md](references/WAIVERS.md)
- **octo/questions** (9 fields, 9 schemas): custom questions asked at booking time.
  → [QUESTIONS.md](references/QUESTIONS.md)
- **octo/checkin** (3 fields, 1 endpoint): online check-in. The ID is `octo/checkin`, not
  `octo/online-check-in`. → [CHECKIN.md](references/CHECKIN.md)

## Fulfilment data is collected before confirm

Questions, waivers and pickup selections belong to the reservation, not to the confirmed booking.
Gather them between `POST /bookings` and `POST /bookings/{uuid}/confirm`, then send them with the
confirm — a required waiver missing at confirm time fails the sale.

## Redemption is reversible

Both `redeem` and `noshow` have a `DELETE` counterpart. Treat a scan as an undoable state change,
not a terminal event, and never rely on local state to decide whether a ticket was already used:
`GET /redemption/lookup` is the authority.

## Source

Field lists generated from the Ventrata OCTO `openapi.yaml` 3.0.3, sha256 `d7bec97a0a909277`,
retrieved 2026-08-20 — see `scripts/extract_caps.py`. Narrative from
[docs.ventrata.com/capabilities](https://docs.ventrata.com/capabilities) (one page per capability).
