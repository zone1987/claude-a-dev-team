---
name: sw-api
description: Shopware API extension: Store API routes and overrides, Admin API controllers, API ACL, webhooks, app scripts. Use when adding or overriding a Shopware Store API or Admin API route.
---

# Shopware API extension

Adding endpoints. A Store API route is a controller with a route annotation plus an ACL entry.

## Reference map

- **[ACL.md](ACL.md)**: Backend-Zugriffe werden über Privilegien abgesichert.
- **[ADMIN-API-CONTROLLER.md](ADMIN-API-CONTROLLER.md)**: Für Nicht-CRUD-Aktionen im Backend.
- **[APP-SCRIPT.md](APP-SCRIPT.md)**: Apps können serverseitige Logik als **Twig-Scripts** mitliefern, ausgeführt an definierten **Hooks**.
- **[STORE-API.md](STORE-API.md)**: Store API routes provide data to the storefront and headless clients. [STORE-API-OVERRIDE](STORE-API-OVERRIDE.md), [STORE-API-ROUTE](STORE-API-ROUTE.md).
- **[WEBHOOK.md](WEBHOOK.md)**: Shopware kann Business-Events an externe URLs senden — primär das **App-System**, aber auch programmatisch üb….

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (framework guides and reference) plus the Shopware 6.7 source, retrieved 2026-08-20.
