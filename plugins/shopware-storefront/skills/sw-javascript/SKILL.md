---
name: sw-javascript
description: Shopware Storefront JavaScript: writing, overriding and extending plugins, the plugin and event catalogues, TypeScript. Use when the request names a Shopware Storefront JS plugin or its events.
---

# Shopware Storefront JavaScript

Storefront JS is a plugin system: register a class against a selector. The catalogues list what already exists before you write a new one.

## Reference map

- **[JS-EVENT-CATALOG.md](references/JS-EVENT-CATALOG.md)**: Answers: **"which JS events exist, where are they published/subscribed, what do they carry?"** — from a….
- **[JS-EVENTS.md](references/JS-EVENTS.md)**: Storefront JS uses a global event emitter and native DOM events for communication between plugins.
- **[JS-PLUGIN-CATALOG.md](references/JS-PLUGIN-CATALOG.md)**: Answers: **"which Storefront JS plugins exist in THIS project?"** — from a cached catalog.
- **[JS-PLUGIN-EXTEND.md](references/JS-PLUGIN-EXTEND.md)**: `extend` registers a subclass for an existing plugin name and keeps the rest of the behavior — s….
- **[JS-PLUGIN-OVERRIDE.md](references/JS-PLUGIN-OVERRIDE.md)**: To completely replace the behavior of a core or third-party JS plugin, register a subclass with `override`.
- **[STOREFRONT-JS-PLUGIN.md](references/STOREFRONT-JS-PLUGIN.md)**: A vanilla JS plugin bound to a `data-*` attribute and initialized by the `PluginManager`.
- **[STOREFRONT-TYPESCRIPT.md](references/STOREFRONT-TYPESCRIPT.md)**: The Storefront supports TypeScript; JS plugins can be written as `.ts`. [STOREFRONT-TYPESCRIPT-TYPESCRIPT](references/STOREFRONT-TYPESCRIPT-TYPESCRIPT.md).

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (Storefront guides and reference) plus the Shopware 6.7 Storefront source, retrieved 2026-08-20.
