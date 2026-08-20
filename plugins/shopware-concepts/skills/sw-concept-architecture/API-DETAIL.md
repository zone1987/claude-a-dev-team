# Shopware APIs — complete concept documentation

Sources: `concepts/api/index.md`, `admin-api.md`, `store-api.md`

---

## API overview (concepts/api/index.md)

Shopware provides HTTP-based APIs through which external systems and custom applications
can interact with the platform.

**Two functional APIs:**

- **Store API** — customer-facing interactions
- **Admin API** — administrative and system-side operations

Both use HTTP with JSON payloads. Shared design principles:

- **Search criteria abstraction** — filtering, sorting, pagination unified
- **Structured JSON request/response bodies**
- **Header-based contextual behaviour**

---

## Admin API (concepts/api/admin-api.md)

### Purpose

Shopware's administrative and integration surface. Provides structured access to:
- Products, orders, customers, media, configurations
- CRUD operations for **all entities** in Shopware

### Areas of use

- Backend integrations
- Automation
- Data synchronisation (import/export)
- System-to-system communication
- Notifications

### Characteristics

- **Authentication**: OAuth 2.0 (mandatory)
- **Priorities**: consistency, error handling, validation, transactional integrity
- **Performance focus**: high data loads (not primarily response time)

### Reference

https://shopware.stoplight.io/docs/admin-api/8d53c59b2e6bc-shopware-admin-api

---

## Store API (concepts/api/store-api.md)

### Purpose

Shopware's customer-facing surface. Designed for storefront/frontend interactions:
- Browse products
- Manage the cart
- Perform checkout
- Manage the customer account

Exposes only **customer-safe data** (no admin access possible).

### Architectural role

A normalised interface layer between the customer frontend and the Shopware core:
- Headless frontends (SPAs, native apps) use JSON over HTTP
- Core business logic is exposed via HTTP routes
- **Storefront AND API consumers use the same Store API services** (no logic duplication)

### Authentication

- Publicly reachable (anonymous use for browsing)
- Context token header (`sw-context-token`) for customer-related endpoints
- No OAuth required

### Usage with composable frontends

Shopware offers "Composable Frontends" as a headless frontend implementation built on the Store API.

### Reference

https://shopware.stoplight.io/docs/store-api/7b972a75a8d8d-shopware-store-api
