# Shopware 6 — API integration (complete reference)

Sources: `guides/development/integrations-api/index.md`, `auth-api-requests.md`

## Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Step 1: Admin API token (OAuth2 client_credentials)](#step-1-admin-api-token-oauth2-client_credentials)
- [Local shortcut: password grant (LOCAL only)](#local-shortcut-password-grant-local-only)
- [Step 2: authenticated API request](#step-2-authenticated-api-request)
- [Step 3: download the OpenAPI schema](#step-3-download-the-openapi-schema)
- [Step 4: Store API](#step-4-store-api)
- [Troubleshooting](#troubleshooting)
- [Concepts shared by both APIs](#concepts-shared-by-both-apis)

## Overview

Shopware offers two HTTP APIs:

- **Admin API** (`/api/*`): back-end operations — products, orders, customers, plugins, bulk processing
- **Store API** (`/store-api/*`): customer-facing interactions — headless frontends, mobile apps, cart, checkout, sales channel access

Official Stoplight documentation:
- Admin API: https://shopware.stoplight.io/docs/admin-api/
- Store API: https://shopware.stoplight.io/docs/store-api/

Complete endpoint documentation (local instance): `/api/_info/stoplightio.html`

## Prerequisites

- A Shopware instance is running: `http://127.0.0.1:8000`
- Admin: `http://localhost:8000/admin`
- `APP_ENV=dev` for schema access and better error messages

```bash
# Check:
docker compose exec web printenv APP_ENV
# If not 'dev': .env.local → APP_ENV=dev → make up
```

## Step 1: Admin API token (OAuth2 client_credentials)

Create an integration: **Admin → Settings → System → Integrations** → enable the "Administrator" toggle.
- Access key ID → `client_id`
- Secret access key → `client_secret`

```bash
curl -s "http://127.0.0.1:8000/api/oauth/token" \
  -H "Content-Type: application/json" \
  -d '{
    "grant_type": "client_credentials",
    "client_id": "YOUR_ACCESS_KEY_ID",
    "client_secret": "YOUR_SECRET_ACCESS_KEY"
  }'
```

Response:
```json
{
  "token_type": "Bearer",
  "expires_in": 3600,
  "access_token": "..."
}
```

## Local shortcut: password grant (LOCAL only)

```bash
curl -X POST "http://localhost:8000/api/oauth/token" \
  -H "Content-Type: application/json" \
  -d '{
    "grant_type": "password",
    "client_id": "administration",
    "scopes": "write",
    "username": "admin",
    "password": "shopware"
  }'
```

The response contains `access_token` (600 s) and `refresh_token`. **For local development only** — in integrations always use `client_credentials`.

## Step 2: authenticated API request

Prefer `POST /api/search/{entity}` over `GET /api/{entity}`:
- GET: simple listing without filter/sort
- POST search: complete Criteria (filter, sort, associations, aggregations, pagination)

```bash
curl -X POST "http://127.0.0.1:8000/api/search/product" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

A successful response contains the keys: `data`, `meta`, `aggregations`. An empty `data` array = not an error, just no products.

## Step 3: download the OpenAPI schema

**Prerequisite: `APP_ENV=dev`**

```bash
# Admin API OpenAPI Spec
curl -X GET "http://localhost:8000/api/_info/openapi3.json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -o openapi.json

# Entity schema
curl -X GET "http://localhost:8000/api/_info/open-api-schema.json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -o entity-schema.json

# Store API
curl -s "http://127.0.0.1:8000/store-api/_info/openapi3.json" -o store-openapi.json

# Filter the available paths:
jq -r '.paths | keys[]' store-openapi.json | grep -E 'checkout|account|payment'
```

Schema endpoints:
- OpenAPI Spec: `/(api|store-api)/_info/openapi3.json`
- Entity Schema: `/(api|store-api)/_info/open-api-schema.json`
- Stoplight UI: `/(api|store-api)/_info/stoplightio.html`

## Step 4: Store API

Sales channel access key: Admin → **Sales Channels → Storefront (or the active channel)** → API access area.

Generating a new key invalidates the old one.

```bash
curl -s "http://127.0.0.1:8000/store-api/product" \
  -H "sw-access-key: YOUR_ACCESS_KEY"
```

A JSON response = success. An empty `elements` array = not an error, no products.

Store API domain: if `127.0.0.1:8000` does not work → Admin: Sales Channels → Domains → add it.

## Troubleshooting

### DB error: `Table 'shopware.system_config' doesn't exist`

```bash
docker compose exec web bin/console system:install --create-database --basic-setup
```

### HTTP 500 on schema endpoints

`APP_ENV` has to be `dev`. `.env.local`:
```dotenv
APP_ENV=dev
```
Then restart the container: `make up` (or `docker compose up -d`).

### The token request returns no output

Leave nested shell sessions and try again.

### Store API: the product does not appear

Checklist:
- The product is `active`
- It has a valid `price`
- It has `visibilities` for the sales channel
- The correct Store API access key is used
- The storefront sales channel domain matches the local URL

## Concepts shared by both APIs

- The same search Criteria syntax (filtering, sorting, pagination)
- Context-dependent responses (permissions / sales channel state)

Rule of thumb: Admin API = manage data. Store API = act as a buyer.
