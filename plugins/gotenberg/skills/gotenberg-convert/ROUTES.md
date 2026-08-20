# Gotenberg — Route overview

Every route accepts a `multipart/form-data` POST request and returns a file.

## Common request headers

| Header | Type | Description |
|--------|-----|-------------|
| `Gotenberg-Output-Filename` | string | Filename of the response (without extension). Default: random UUID. |
| `Gotenberg-Trace` | string | Custom request ID for logs. Replaces the default UUID. |

## Authentication

Basic Auth via the CLI flag `--api-enable-basic-auth`. Credentials via the env vars
`GOTENBERG_API_BASIC_AUTH_USERNAME` / `GOTENBERG_API_BASIC_AUTH_PASSWORD`.

Complete route table: `ROUTES-DETAIL.md`
