---
name: octo-capabilities-platform
description: 'OCTO/Ventrata platform capabilities: webhooks, notifications, content, mappings, memberships, waitlists. Use when the request names an octo/* platform capability such as octo/webhooks.'
---

# OCTO platform capabilities

The plumbing around the selling flow: staying in sync, enriching content, identifying customers.

## The capabilities

- **octo/webhooks** (5 endpoints): register HTTP callbacks for events. No schema fields — it is
  endpoints only. → [WEBHOOKS.md](WEBHOOKS.md)
- **octo/notifications** (5 endpoints): notification subscriptions under
  `/notifications/subscriptions`. → [NOTIFICATIONS.md](NOTIFICATIONS.md)
- **octo/content** (14 fields, 9 schemas): titles, descriptions, images and itineraries — the
  human-readable layer over the catalogue. → [CONTENT.md](CONTENT.md)
- **octo/mappings** (5 fields, 2 endpoints): map supplier IDs to your own. → [MAPPINGS.md](MAPPINGS.md)
- **octo/memberships** (18 fields, 14 schemas, 2 endpoints): membership lookup and benefits. Adds
  the `membership[*]` parameters to product and availability calls. → [MEMBERSHIPS.md](MEMBERSHIPS.md)
- **octo/campaigns** (1 field, 1 endpoint): campaign attribution. → [CAMPAIGNS.md](CAMPAIGNS.md)
- **octo/waitlists** (1 endpoint): join a waitlist when availability is exhausted.
  → [WAITLISTS.md](WAITLISTS.md)
- **octo/identities** (10 fields, 3 endpoints): **internal capability.** Not returned by
  `GET /capabilities` and not available to a normal reseller connection. → [IDENTITIES.md](IDENTITIES.md)

## Webhooks over polling

Webhooks and notifications exist so you do not poll `GET /bookings`. Register once, then reconcile
periodically rather than continuously. A webhook delivery is a hint to re-read the booking, not a
substitute for reading it — treat the payload as untrusted and fetch the authoritative state.

## Content is not the catalogue

`octo/content` adds display fields; it never changes what is sellable. Product structure comes from
the core schemas, so a missing title is a content problem, not a catalogue problem.

## Source

Field lists generated from the Ventrata OCTO `openapi.yaml` 3.0.3, sha256 `d7bec97a0a909277`,
retrieved 2026-08-20 — see `scripts/extract_caps.py`. Narrative from
[docs.ventrata.com/capabilities](https://docs.ventrata.com/capabilities) (one page per capability).
