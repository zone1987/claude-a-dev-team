# Gotenberg — Webhook & Download

Asynchronous processing: Gotenberg returns 204 immediately and sends the result
via a callback request. Supports an events URL and `downloadFrom` for remote files.
Reference: `WEBHOOK-DETAIL.md`

Response code: `204 No Content` (processing runs in the background)
