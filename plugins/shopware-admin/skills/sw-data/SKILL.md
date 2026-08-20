---
name: sw-data
description: Shopware admin data: repositoryFactory and Criteria in JS, API requests, Pinia and Vuex stores, services, error handling, ACL. Use when loading or saving data in the Shopware administration.
---

# Shopware Administration data handling

Data comes through repositoryFactory, not fetch. Pinia is current, Vuex is legacy but still present.

## Reference map

- **[ADMIN-ACL-PERMISSIONS.md](ADMIN-ACL-PERMISSIONS.md)**: Privilegien registrieren und an Modul/Route/Navigation/Buttons binden.
- **[ADMIN-API-REQUESTS.md](ADMIN-API-REQUESTS.md)**: Für Nicht-CRUD-Aufrufe einen `ApiService` registrieren bzw.
- **[ADMIN-CATALOG.md](ADMIN-CATALOG.md)**: Beantwortet: **„welche Admin-Bausteine existieren in DIESEM Projekt?"** — Module, Komponenten, Services, Mixi….
- **[ADMIN-DATA-HANDLING.md](ADMIN-DATA-HANDLING.md)**: Daten laufen über `repositoryFactory`.
- **[ADMIN-ERROR-HANDLING.md](ADMIN-ERROR-HANDLING.md)**: API-/Save-Fehler abfangen und als Notification zeigen; Validierungsfehler werden von Meteor-Feldern automatis….
- **[ADMIN-PINIA-STORE.md](ADMIN-PINIA-STORE.md)**: Seit 6.6/6.7 ist **Pinia** der Standard.
- **[ADMIN-REPOSITORY-JS.md](ADMIN-REPOSITORY-JS.md)**: `create` erzeugt eine Entity mit generierter ID.
- **[ADMIN-SERVICES.md](ADMIN-SERVICES.md)**: Services über `addServiceProvider` registrieren, in Komponenten via `inject` nutzen.
- **[ADMIN-VUEX-STORE.md](ADMIN-VUEX-STORE.md)**: Vuex ist **deprecated**.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (Administration guides) and the Meteor design system documentation, retrieved 2026-08-20. Shopware 6.7 administration: Vue 3, Pinia, Vite.
