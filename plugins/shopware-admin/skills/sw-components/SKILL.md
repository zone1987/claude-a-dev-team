---
name: sw-components
description: Shopware admin components: creating and overriding components, modules, menu entries, routing, data grids, directives, mixins, filters. Use when building a Shopware administration module or component.
---

# Shopware Administration components

The Vue layer. A module registers routes and menu entries; components are registered globally and overridden by name.

## Reference map

- **[ADMIN-COMPONENT.md](ADMIN-COMPONENT.md)**: Components are registered via `Shopware.Component.register`. [ADMIN-COMPONENT-OVERRIDE](ADMIN-COMPONENT-OVERRIDE.md).
- **[ADMIN-DATA-GRID.md](ADMIN-DATA-GRID.md)**: Lists with `sw-entity-listing` or.
- **[ADMIN-DIRECTIVES.md](ADMIN-DIRECTIVES.md)**: Use the admin's built-in Vue directives in the template:.
- **[ADMIN-MENU.md](ADMIN-MENU.md)**: Menu entries are defined in the module via `navigation` or.
- **[ADMIN-MIXINS.md](ADMIN-MIXINS.md)**: Mixins encapsulate reusable component behaviour.
- **[ADMIN-MODULE.md](ADMIN-MODULE.md)**: A module bundles the routes, components and navigation of a backend area. [ADMIN-MODULE-ADMINISTRATION](ADMIN-MODULE-ADMINISTRATION.md).
- **[ADMIN-ROUTING.md](ADMIN-ROUTING.md)**: Routes are declared in the module under `routes`.
- **[ADMIN-UTILS-FILTERS.md](ADMIN-UTILS-FILTERS.md)**: The admin offers many helpers on the `Shopware` object — before writing your own code, check whether one already exists.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (Administration guides) and the Meteor design system documentation, retrieved 2026-08-20. Shopware 6.7 administration: Vue 3, Pinia, Vite.
