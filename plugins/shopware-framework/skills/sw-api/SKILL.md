---
name: sw-api
description: Shopware API extension: Store API routes and overrides, Admin API controllers, API ACL, webhooks, app scripts. Use when adding or overriding a Shopware Store API or Admin API route.
---

# Shopware API extension

Adding endpoints. A Store API route is a controller with a route annotation plus an ACL entry.

## Reference map

- **[ACL.md](ACL.md)**: Backend access is secured through privileges.
- **[ADMIN-API-CONTROLLER.md](ADMIN-API-CONTROLLER.md)**: For non-CRUD actions in the backend.
- **[APP-SCRIPT.md](APP-SCRIPT.md)**: Apps can ship server-side logic as **Twig scripts**, executed at defined **hooks**.
- **[STORE-API.md](STORE-API.md)**: Store API routes provide data to the storefront and headless clients. [STORE-API-OVERRIDE](STORE-API-OVERRIDE.md), [STORE-API-ROUTE](STORE-API-ROUTE.md).
- **[WEBHOOK.md](WEBHOOK.md)**: Shopware can send business events to external URLs — primarily the **app system**, but also programmatically thro….

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (framework guides and reference) plus the Shopware 6.7 source, retrieved 2026-08-20.
