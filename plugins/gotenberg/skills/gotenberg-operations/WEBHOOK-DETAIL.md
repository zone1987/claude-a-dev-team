# Gotenberg — Webhook & Remote Download (Full Reference)

## Contents

- [Concept](#concept)
- [Webhook headers](#webhook-headers)
- [Response codes for the initial request](#response-codes-for-the-initial-request)
- [Callback payloads](#callback-payloads)
- [Events URL payloads (Gotenberg-Webhook-Events-Url)](#events-url-payloads-gotenberg-webhook-events-url)
- [downloadFrom — loading remote files](#downloadfrom-loading-remote-files)
- [curl examples](#curl-examples)
- [Configuration (env variables)](#configuration-env-variables)
- [Notes](#notes)

## Concept

Gotenberg supports **asynchronous processing**: instead of waiting synchronously for the result, Gotenberg returns `204 No Content` immediately and sends the result (or an error) to a configured callback URL after processing.

Webhook headers can be used with **every** Gotenberg endpoint.

---

## Webhook headers

| Header | Type | Required | Default | Description |
|--------|-----|---------|----------|--------------|
| `Gotenberg-Webhook-Url` | string | Conditional* | — | Callback URL for successful results (POST, unless overridden) |
| `Gotenberg-Webhook-Method` | string | No | `POST` | HTTP method for the success callback; allowed: `POST`, `PUT`, `PATCH` |
| `Gotenberg-Webhook-Error-Url` | string | No | — | **Deprecated** — use `Gotenberg-Webhook-Events-Url` instead |
| `Gotenberg-Webhook-Error-Method` | string | No | `POST` | HTTP method for the error callback; allowed: `POST`, `PUT`, `PATCH` |
| `Gotenberg-Webhook-Extra-Http-Headers` | JSON string | No | — | Additional HTTP headers as a JSON object for callback requests |
| `Gotenberg-Webhook-Events-Url` | string | Conditional* | — | URL for structured JSON events (success + error) |

*At least one of `Gotenberg-Webhook-Url` or `Gotenberg-Webhook-Events-Url` must be provided, otherwise → 400.

---

## Response codes for the initial request

| Code | Description |
|------|-------------|
| `204 No Content` | Request valid, asynchronous processing started |
| `400 Bad Request` | Invalid or missing headers/fields |
| `403 Forbidden` | Webhook URL blocked by the outbound filter |

---

## Callback payloads

### Success callback (to Gotenberg-Webhook-Url)

```
Content-Disposition: attachment; filename={filename.ext}
Content-Type: {content-type}
Content-Length: {length}
Gotenberg-Trace: {trace}
traceparent: {w3c-traceparent}
User-Agent: Gotenberg

[File content as binary]
```

### Error callback (to Gotenberg-Webhook-Error-Url, deprecated)

```json
{
  "status": 500,
  "message": "conversion failed"
}
```

---

## Events URL payloads (Gotenberg-Webhook-Events-Url)

### Success event

```json
{
  "event": "webhook.success",
  "correlationId": "unique-request-id",
  "timestamp": "2025-01-15T10:30:00.000000000Z"
}
```

### Error event

```json
{
  "event": "webhook.error",
  "correlationId": "unique-request-id",
  "timestamp": "2025-01-15T10:30:00.000000000Z",
  "error": {
    "status": 500,
    "message": "conversion failed"
  }
}
```

---

## downloadFrom — loading remote files

Allows source files to be fetched from external URLs instead of being uploaded.

### Form field

| Field | Type | Required | Description |
|------|-----|---------|--------------|
| `downloadFrom` | JSON array | No | List of remote file objects |

### downloadFrom object structure

| Field | Type | Required | Default | Description |
|------|-----|---------|----------|--------------|
| `url` | string | Yes | — | Remote URL; the server **must** return a `Content-Disposition` header with a `filename` parameter |
| `extraHttpHeaders` | JSON object | No | — | Additional HTTP headers for this fetch |
| `embedded` | boolean | No | `false` | Legacy option for attachments |
| `field` | string | No | `""` | Target field: `""` (main file), `"watermark"`, `"stamp"` |

---

## curl examples

### Asynchronous conversion with webhook

```bash
curl --request POST http://localhost:3000/forms/chromium/convert/url \
  --header 'Gotenberg-Webhook-Url: https://meine-app.example.com/webhook/pdf' \
  --header 'Gotenberg-Webhook-Extra-Http-Headers: {"Authorization":"Bearer mein-token"}' \
  --form url=https://example.com
```

### Webhook with events URL (recommended)

```bash
curl --request POST http://localhost:3000/forms/pdfengines/merge \
  --header 'Gotenberg-Webhook-Url: https://meine-app.example.com/webhook/ergebnis' \
  --header 'Gotenberg-Webhook-Events-Url: https://meine-app.example.com/webhook/events' \
  --header 'Gotenberg-Webhook-Extra-Http-Headers: {"X-Api-Key":"abc123"}' \
  --form files=@/path/to/1.pdf \
  --form files=@/path/to/2.pdf
```

### Webhook with the PUT method

```bash
curl --request POST http://localhost:3000/forms/pdfengines/merge \
  --header 'Gotenberg-Webhook-Url: https://storage.example.com/pdf/output' \
  --header 'Gotenberg-Webhook-Method: PUT' \
  --form files=@/path/to/1.pdf
```

### Load a remote file (downloadFrom)

```bash
curl --request POST http://localhost:3000/forms/libreoffice/convert \
  --form 'downloadFrom=[{"url":"https://example.com/dokument.docx","extraHttpHeaders":{"X-Header":"Wert"}}]' \
  -o konvertiert.pdf
```

### Load a remote file as a watermark

```bash
curl --request POST http://localhost:3000/forms/pdfengines/watermark \
  --form files=@/path/to/dokument.pdf \
  --form watermarkSource=image \
  --form 'downloadFrom=[{"url":"https://cdn.example.com/logo.png","field":"watermark"}]' \
  --form watermarkExpression=logo.png \
  -o mit-wasserzeichen.pdf
```

---

## Configuration (env variables)

| Variable | Description | Default |
|----------|-------------|---------|
| `WEBHOOK_ALLOW_LIST` | Regex for allowed webhook URLs | — |
| `WEBHOOK_DENY_PRIVATE_IPS` | Block private IPs for webhooks | `false` |
| `WEBHOOK_DENY_PUBLIC_IPS` | Block public IPs for webhooks | `false` |
| `API_DOWNLOAD_FROM_DENY_PRIVATE_IPS` | Block private IPs for downloadFrom | `false` |
| `API_DOWNLOAD_FROM_DENY_PUBLIC_IPS` | Block public IPs for downloadFrom | `false` |

---

## Notes

- The W3C `traceparent` header is sent along in the callback request as of v8.34.0 (distributed tracing)
- Webhook callbacks and `downloadFrom` fetches pass through Gotenberg's outbound filter pipeline
- `Gotenberg-Webhook-Error-Url` is deprecated — use `Gotenberg-Webhook-Events-Url`
- The remote server for `downloadFrom` **must** return `Content-Disposition: attachment; filename=datei.ext`

---

Source: https://gotenberg.dev/docs/webhook-download
