# Shopware 6 — Admin API authentication (OAuth2)

Fetch a token at `POST /api/oauth/token`, then send `Authorization: Bearer {access_token}` on all Admin API requests.

## client_credentials (integrations, production)
Take `client_id`/`client_secret` from an **integration** (Admin → Settings → System → Integrations):
```bash
curl -X POST "$BASE/api/oauth/token" -H "Content-Type: application/json" -d '{
  "grant_type": "client_credentials",
  "client_id": "<accessKeyId>",
  "client_secret": "<secretAccessKey>"
}'
```

## password (local development only)
```bash
curl -X POST "$BASE/api/oauth/token" -H "Content-Type: application/json" -d '{
  "grant_type": "password", "client_id": "administration",
  "username": "admin", "password": "shopware"
}'
```

Response: `access_token` (bearer), `expires_in` (default **600s**), `refresh_token` (password grant only). On expiry
fetch a new one or renew via `grant_type: refresh_token`. Integrations can be granted admin rights/ACL.
Requests afterwards: `sw-admin-api-crud`, `sw-admin-api-search`. OpenAPI schema (dev): `GET /api/_info/openapi3.json`.
