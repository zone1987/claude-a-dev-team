---
name: sw-admin-api-auth
description: >
  Authentifizierung an der Shopware-6 Admin API: OAuth2 token endpoint /api/oauth/token, grant_type client_credentials
  (Integration: client_id/client_secret) und password (client_id 'administration', dev), Bearer-Token, expires_in 600s,
  refresh_token. Trigger: "Admin API auth", "oauth token shopware", "/api/oauth/token", "client_credentials shopware",
  "access_token bearer admin api", "Integration access key secret", "refresh token api". Shopware 6.7.
---

# Shopware 6 — Admin-API-Authentifizierung (OAuth2)

Token holen an `POST /api/oauth/token`, dann `Authorization: Bearer {access_token}` an allen Admin-API-Requests.

## client_credentials (Integrationen, produktiv)
Aus einer **Integration** (Admin → Einstellungen → System → Integrationen) `client_id`/`client_secret`:
```bash
curl -X POST "$BASE/api/oauth/token" -H "Content-Type: application/json" -d '{
  "grant_type": "client_credentials",
  "client_id": "<accessKeyId>",
  "client_secret": "<secretAccessKey>"
}'
```

## password (nur lokale Entwicklung)
```bash
curl -X POST "$BASE/api/oauth/token" -H "Content-Type: application/json" -d '{
  "grant_type": "password", "client_id": "administration",
  "username": "admin", "password": "shopware"
}'
```

Antwort: `access_token` (Bearer), `expires_in` (Default **600s**), `refresh_token` (nur password-Grant). Bei Ablauf
neu holen bzw. via `grant_type: refresh_token` erneuern. Integrationen können Admin-Rechte/ACL bekommen.
Requests danach: `sw-admin-api-crud`, `sw-admin-api-search`. OpenAPI-Schema (dev): `GET /api/_info/openapi3.json`.
