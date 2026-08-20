---
name: sw-components
description: Shopware admin components: creating and overriding components, modules, menu entries, routing, data grids, directives, mixins, filters. Use when building a Shopware administration module or component.
---

# Shopware Administration components

The Vue layer. A module registers routes and menu entries; components are registered globally and overridden by name.

## Reference map

- **[ADMIN-COMPONENT.md](ADMIN-COMPONENT.md)**: Komponenten werden über `Shopware.Component.register` registriert. [ADMIN-COMPONENT-OVERRIDE](ADMIN-COMPONENT-OVERRIDE.md).
- **[ADMIN-DATA-GRID.md](ADMIN-DATA-GRID.md)**: Listen mit `sw-entity-listing` bzw.
- **[ADMIN-DIRECTIVES.md](ADMIN-DIRECTIVES.md)**: Eingebaute Vue-Direktiven der Admin im Template nutzen:.
- **[ADMIN-MENU.md](ADMIN-MENU.md)**: Menüeinträge werden im Modul über `navigation` bzw.
- **[ADMIN-MIXINS.md](ADMIN-MIXINS.md)**: Mixins kapseln wiederverwendbares Komponentenverhalten.
- **[ADMIN-MODULE.md](ADMIN-MODULE.md)**: Ein Modul bündelt Routen, Komponenten und Navigation eines Backend-Bereichs. [ADMIN-MODULE-ADMINISTRATION](ADMIN-MODULE-ADMINISTRATION.md).
- **[ADMIN-ROUTING.md](ADMIN-ROUTING.md)**: Routen werden im Modul unter `routes` deklariert.
- **[ADMIN-UTILS-FILTERS.md](ADMIN-UTILS-FILTERS.md)**: Die Admin bietet viele Helfer am `Shopware`-Objekt — vor eigenem Code prüfen, ob es schon existiert.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (Administration guides) and the Meteor design system documentation, retrieved 2026-08-20. Shopware 6.7 administration: Vue 3, Pinia, Vite.
