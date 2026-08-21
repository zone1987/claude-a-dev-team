# The API contract

An API plugin exists to be the **specialist** for that API. A reader who has to open the upstream
docs for one missing facet got nothing from the plugin. Rules: `API-01` to `API-06`.

## Contents

- [Per operation](#per-operation)
- [Per parameter and per property](#per-parameter-and-per-property)
- [When the upstream is silent](#when-the-upstream-is-silent)
- [Worked examples](#worked-examples)
- [The field index](#the-field-index)
- [Verify both directions](#verify-both-directions)
- [Source](#source)

## Per operation

Every operation in the source gets an entry carrying all of:

- **method and path**, exactly as the spec writes them
- **summary and description**, the upstream sentences rather than a paraphrase
- **every parameter, grouped by location**: path, query, header, cookie
- **the request body**: media type and schema
- **every response status** with its schema, not only the success case
- **a worked request and a worked response**, including the error shapes

Nothing is dropped because it looked obvious. `API-01`

```markdown
## `GET /products/{productId}`

Get Product. Get details on a specific product.

### Path parameters

- **productId** (string, required, in path): Product ID. Example: `"e7cc8bb4-8d1c-…"`.

### Query parameters

- **currency** (string, optional, in query): Currency override. Use an ISO-4217 code from
  `availableCurrencies` or `default`. Example: `"USD"`.

### Headers

- **Accept-Language** (string, required, in header): …
- **Octo-Capabilities** (string, optional, in header): comma-separated capability IDs.

### Responses

- **200**: Successful response. Returns `Product`.
- **400**: `Accept-Language` missing on this endpoint, though not on `GET /products`.
- **404**: unknown `productId`.
```

## Per parameter and per property

One entry, always carrying every facet that applies. This is the rule that makes the plugin
authoritative, and the one most easily eroded. `API-03`

| Facet | Rendered as |
|---|---|
| name | `**fieldName**` |
| type | `string`, `number`, `boolean`, `Product[]`, `OperatorSummary` |
| format | `string (uuid)`, `string (date-time)`, `string (email)` |
| optionality | `required` or `optional` |
| nullability | `nullable` |
| location (parameters) | `in query`, `in path`, `in header` |
| possible values | `One of: A, B, C`, **each with its meaning** |
| default | `Default: X` |
| constraints | min, max, pattern, minLength, maxLength, minItems, maxItems |
| example | `Example: "…"` |
| description | the upstream sentence |

```markdown
- **availabilityType** (string, optional): Availability type. One of: `START_TIME` for timed slots,
  `OPENING_HOURS` for open-window admission. It decides how availability responses are shaped, so
  read it before calling availability. Example: `"START_TIME"`.
- **id** (string (uuid), required): Unique identifier for this resource. Example: `"e7cc8bb4-…"`.
- **operator** (OperatorSummary, optional, nullable): Operator object.
```

**Every enum lists all of its values.** A truncated list produces code that handles some cases and
fails on the rest. `API-04`

## When the upstream is silent

State the silence. A blank reads as absence, and the reader cannot tell an unstated fact from a
missing one.

| Facet absent upstream | Write |
|---|---|
| optionality | `optionality not stated upstream` |
| description | `undocumented upstream` |
| example | derive one and mark it: `Example (derived): …` |
| possible values, unbounded | `values not enumerated upstream` |
| format, default, constraints | omit the facet; its absence is not ambiguous |

The first two are the ones that matter: silence about whether a field is required is itself a fact
the reader needs.

## Worked examples

Every operation carries a request and a response that can be pasted and run, **error shapes
included**. The error body is the one nobody guesses correctly, and the reason a reader falls back to
the upstream docs. `API-02`

This is the one facet `octo-api` lacks today, so it is a rule the forge adds rather than inherits.

## The field index

Every API skill ships a `FIELD-INDEX.json` holding the machine-readable inventory and the source
hash: `endpoints` keyed by `METHOD /path` with `params` and `enums`; `schemas` keyed by name with
`base`, `required`, `capabilities` and `enums`. `API-05`

It is not documentation. It is what makes the reverse check possible at all: without an index, there
is nothing to compare the prose against.

## Verify both directions

- **Forward**: every field in the specification appears in a reference file.
- **Reverse**: every field name in the prose exists in the specification.

The reverse direction is the one that catches invention: a plausible-sounding field added by hand
fails the build. Run it after every extraction and after every hand edit. `API-06`

Guard the reverse check against false positives: prose legitimately bolds things that are not field
names, such as a dotted access path (`booking.pricing.retail`), a bracketed traversal
(`unitItems[].ticket`), or an ordinary word used for emphasis. Check only bare identifiers, and keep
an explicit exclusion list with a reason per entry.

## Source

Shape and counts read from `plugins/octo-api/skills/octo-products/` and
`plugins/octo-api/scripts/verify_spec.py` in this marketplace, 2026-08-21: 1,787 rendered field
entries across 7,736 lines, verified against `openapi.yaml` sha256 `d7bec97a…` in both directions.
