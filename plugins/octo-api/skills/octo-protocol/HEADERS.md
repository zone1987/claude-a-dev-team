# Headers

Every OCTO request carries these. Source: `docs.ventrata.com/getting-started/headers`.

## Request headers

| Header | Required | Value |
|---|---|---|
| `Authorization` | Required | `Bearer <api-key>` |
| `Content-Type` | Required for POST, PATCH, DELETE | `application/json` |
| `Octo-Capabilities` | **Required** | Comma-separated capability IDs, e.g. `octo/pricing, octo/content` |
| `Octo-Env` | Recommended | `test` or `live` |
| `Accept-Language` | Optional (required on `GET /products/{productId}`) | Standard HTTP language tag, e.g. `fr` |

### `Octo-Capabilities` is not optional

Verbatim from the documentation:

> A list of Capabilities to include in the response, for example
> `Octo-Capabilities: octo/pricing, octo/content`. **Include the header but leave it empty if no
> capabilities are needed. If this header is not included, Ventrata returns a `400` error.**

So a request needing no capabilities still sends `Octo-Capabilities:` with an empty value. The
legacy alias `X-Capabilities` is accepted for older integrations.

### `Octo-Env` decides whether a sale is real

> This can mark any booking performed with live credentials as a test sale in Ventrata. This means
> it will not consume availability, barcodes will not work, and you will not be invoiced.

Use `Octo-Env: test` while integrating even with live credentials, and switch to `live` only when
you intend to sell. A supplier can force a connection into `test` mode regardless of what you send —
check the response header to see which mode actually applied.

## Response headers

| Header | Meaning |
|---|---|
| `Content-Type` | `application/json` |
| `Octo-Capabilities` | The capabilities that were actually applied to this request |
| `Octo-Env` | `test` or `live`, after any supplier-side override |
| `Content-Language` | Language of the returned content |
| `Octo-Available-Languages` | Languages the supplier has translated content into |

Compare the returned `Octo-Capabilities` against what you sent: a capability your connection may not
use is dropped silently rather than rejected.

## Example

```http
GET /octo/products HTTP/1.1
Host: api.ventrata.com
Authorization: Bearer <api-key>
Octo-Capabilities: octo/pricing, octo/content
Octo-Env: test
Accept-Language: en
```

## Source

[docs.ventrata.com/getting-started/headers](https://docs.ventrata.com/getting-started/headers) and
`getting-started/getting-started` (authentication), retrieved 2026-08-20.
