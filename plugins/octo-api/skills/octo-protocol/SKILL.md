---
name: octo-protocol
description: 'OCTO/Ventrata wire protocol: auth, the Octo-Capabilities header, error codes, localization. Use when a request names OCTO, Ventrata, Octo-Capabilities, Octo-Env, or an octo/* capability.'
---

# OCTO Protocol

OCTO (Open Connection for Tourism) is an open standard for tourism ticketing, maintained by OCTO
Standards NP Inc. Ventrata implements it at `https://api.ventrata.com/octo`. This skill covers what
every request needs, regardless of endpoint.

## Every request

Send these four headers. The third one is the trap.

- **Authorization** (required): `Bearer <api-key>`. The key is a UUID and grants access to
  **exactly one supplier** — expect one key per supplier, never a global one.
- **Content-Type** (required for POST, PATCH, DELETE): `application/json`.
- **Octo-Capabilities** (required): comma-separated capability IDs, e.g.
  `octo/pricing, octo/content`. **Send the header even when you need no capabilities — leave it
  empty. Omitting it returns HTTP 400.** The legacy alias `X-Capabilities` is still accepted.
- **Octo-Env** (recommended): `test` marks a booking made with live credentials as a test sale — it
  consumes no availability, barcodes stay inert, and it is not invoiced. `live` sells for real.

`Accept-Language` is optional protocol-wide, but **required on `GET /products/{productId}`**.

Responses echo `Octo-Capabilities` and `Octo-Env`, plus `Content-Language` and
`Octo-Available-Languages`.

## Error contract

There are two outcomes: `200 OK`, or `400 Bad Request` with `error` and `errorMessage` in the body.
`errorMessage` is localized via `Accept-Language`. Some codes carry an extra field naming the
offending value — `INVALID_PRODUCT_ID` returns the `productId` you sent.

Treat `400` as "your request was wrong", never as "the resource is missing": there is no 404.

## Capability model

Capabilities are additive. Requesting one merges extra fields into the core schemas; the base shape
never changes. Ask for only what you parse — each capability widens every response.

- **GET /capabilities** lists the non-internal capabilities this connection may use.
- **GET /whoami** returns supplier, connection and partner context for the API key.

There is no `/supplier` endpoint. `octo/identities` is the only internal capability.

## Values a response can carry

Every value-like field comes with its possible values in
[ENUMERATED-VALUES.md](references/ENUMERATED-VALUES.md), split by how firm the set is:

- **Declared** — the specification lists an `enum`, so the set is closed. `availabilityType` is
  `START_TIME` or `OPENING_HOURS`, nothing else.
- **Observed** — the specification types the field as a plain string and only gives an example.
  `settlementMethods` documents `DIRECT` and `DEFERRED`, but **the set is open**: handle an unknown
  value instead of switching exhaustively.

## Reference map

- **[DOCUMENTATION-MAP.md](references/DOCUMENTATION-MAP.md)**: every page of Ventrata's documentation and the
  file here that covers it — the audit trail behind "nothing was left out".
- **[GLOSSARY.md](references/GLOSSARY.md)**: the nine core terms, and the distinctions that get mismodelled —
  unit versus unit item, voucher versus ticket.
- **[AUTHENTICATION.md](references/AUTHENTICATION.md)**: the Bearer key, why one key means one supplier, and
  what a `403` actually tells you.
- **[TESTING.md](references/TESTING.md)**: the EdinExplore test supplier, its API logs, and `Octo-Env: test`
  against live credentials.
- **[INTEGRATION-STEPS.md](references/INTEGRATION-STEPS.md)**: Ventrata's four-step path from planning to
  go-live, and what their review asks for.
- **[HEADERS.md](references/HEADERS.md)**: every request and response header, verbatim requirement and example.
- **[ERRORS.md](references/ERRORS.md)**: all 10 error codes, their extra fields, and example bodies.
- **[CAPABILITY-ERRORS.md](references/CAPABILITY-ERRORS.md)**: the 21 further codes that 9 capabilities add on top of those 10.
- **[ENUMERATED-VALUES.md](references/ENUMERATED-VALUES.md)**: every possible value of every value-like field,
  with what each one means.
- **[REMAINING-SCHEMAS-1.md](references/REMAINING-SCHEMAS-1.md)** and
  **[REMAINING-SCHEMAS-2.md](references/REMAINING-SCHEMAS-2.md)**: the request wrappers, list envelopes,
  protocol objects and action results the domain skills do not lay out, so all 139 schemas are
  covered.
- **[CAPABILITY-DISCOVERY.md](references/CAPABILITY-DISCOVERY.md)**: the discovery endpoints, the Capability
  object, and all 23 capabilities mapped to the skill that documents them.
- **[LOCALIZATION.md](references/LOCALIZATION.md)**: language negotiation and which fields get translated.

## Related

Call the Skill tool with "octo-products" for the catalogue, "octo-availability" for availability
checks, or "octo-bookings" for the reserve/confirm/cancel lifecycle.

## Source

Distilled from the [Ventrata OCTO documentation](https://docs.ventrata.com) — pages
`getting-started/headers`, `getting-started/errors`, `getting-started/request-capabilities`,
`getting-started/getting-started`, `getting-started/localization`, retrieved 2026-08-20 — and from
`openapi.yaml` 3.0.3, sha256 `d7bec97a0a909277`.
OCTO is an open standard by OCTO Standards NP Inc. ([octo.travel](https://octo.travel)).
