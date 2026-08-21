# Authentication

## Bearer token

```http
Authorization: Bearer {your_API_key}
```

The API key is a **UUID**, for example `5bd1629a-323e-4edb-ac9b-327ef51e6136`. The supplier issues it
by creating a connection for your reseller account; that same connection also controls **which
products you see and which pricing applies**. A key is therefore not just a credential — it is the
scope of your catalogue.

## One key per supplier

> In Ventrata's implementation of OCTO, **the API key provides access to a single supplier**. You
> will have different API keys for each supplier you'd like to connect with.

Design the integration for many keys from the start. A single-key assumption forces a rewrite as
soon as the second supplier arrives, and there is no cross-supplier endpoint to fall back on.

## Transport and failure modes

- **HTTPS only.** Calls over plain HTTP fail.
- **No authentication** → the request fails.
- **Invalid or deactivated token** → `403 Forbidden`. A supplier can deactivate a connection at any
  time, so treat `403` as "ask the supplier", not as a bug in your request.
- **`POST`, `PATCH`, `DELETE`** must send `Content-Type: application/json` and a JSON-encoded body.
  Every endpoint answers with JSON unless documented otherwise.

## Key hygiene

> API keys must be kept secure. **You are responsible for any bookings made with your API key.** If
> your key is disclosed publicly, ask the supplier to delete and recreate your connection, or
> contact Ventrata to rotate the key.

There is no self-service rotation: recovery runs through the supplier or Ventrata. Store keys where
a leak is recoverable, and never in a repository.

## Source

[docs.ventrata.com/getting-started/getting-started](https://docs.ventrata.com/getting-started/getting-started),
retrieved 2026-08-20.
