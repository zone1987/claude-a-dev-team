---
name: sw-data
description: Shopware admin data: repositoryFactory and Criteria in JS, API requests, Pinia and Vuex stores, services, error handling, ACL. Use when loading or saving data in the Shopware administration.
---

# Shopware Administration data handling

Data comes through repositoryFactory, not fetch. Pinia is current, Vuex is legacy but still present.

## Reference map

- **[ADMIN-ACL-PERMISSIONS.md](ADMIN-ACL-PERMISSIONS.md)**: Register privileges and bind them to module/route/navigation/buttons.
- **[ADMIN-API-REQUESTS.md](ADMIN-API-REQUESTS.md)**: For non-CRUD calls register an `ApiService` or.
- **[ADMIN-CATALOG.md](ADMIN-CATALOG.md)**: Answers: **"which admin building blocks exist in THIS project?"** — modules, components, services, mixi….
- **[ADMIN-DATA-HANDLING.md](ADMIN-DATA-HANDLING.md)**: Data goes through `repositoryFactory`.
- **[ADMIN-ERROR-HANDLING.md](ADMIN-ERROR-HANDLING.md)**: Catch API/save errors and show them as a notification; validation errors are bound to the entity automatic….
- **[ADMIN-PINIA-STORE.md](ADMIN-PINIA-STORE.md)**: Since 6.6/6.7 **Pinia** is the standard.
- **[ADMIN-REPOSITORY-JS.md](ADMIN-REPOSITORY-JS.md)**: `create` produces an entity with a generated ID.
- **[ADMIN-SERVICES.md](ADMIN-SERVICES.md)**: Register services via `addServiceProvider` and use them in components via `inject`.
- **[ADMIN-VUEX-STORE.md](ADMIN-VUEX-STORE.md)**: Vuex is **deprecated**.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (Administration guides) and the Meteor design system documentation, retrieved 2026-08-20. Shopware 6.7 administration: Vue 3, Pinia, Vite.
