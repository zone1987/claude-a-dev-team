# Shopware APIs — concept

Complete concept documentation: `API-DETAIL.md`

## Brief overview

Shopware provides **two functional APIs**:

| | Store API | Admin API |
|---|---|---|
| Purpose | Customer-facing interactions | Administrative/backend operations |
| Auth | Public + context header | OAuth 2.0 |
| Path | `/store-api/` | `/api/` |
| Usage | Storefront, headless frontend, SPAs | Backend integrations, sync, automation |

## Shared patterns

- JSON payloads (HTTP)
- Search criteria abstraction (filtering, sorting, pagination)
- Header-based contextual behaviour

## Store API particularity

A normalised interface layer between frontend and Shopware core. Storefront and headless clients
use **the same Store API routes** — no duplicated business logic.

Technical implementation: `shopware-api`, `shopware-framework` (dev plugins)
