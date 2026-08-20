---
name: sw-javascript
description: Shopware Storefront JavaScript: writing, overriding and extending plugins, the plugin and event catalogues, TypeScript. Use when the request names a Shopware Storefront JS plugin or its events.
---

# Shopware Storefront JavaScript

Storefront JS is a plugin system: register a class against a selector. The catalogues list what already exists before you write a new one.

## Reference map

- **[JS-EVENT-CATALOG.md](JS-EVENT-CATALOG.md)**: Answers: **"which JS events exist, where are they published/subscribed, what do they carry?"** — from a….
- **[JS-EVENTS.md](JS-EVENTS.md)**: Storefront JS uses a global event emitter and native DOM events for communication between plugins.
- **[JS-PLUGIN-CATALOG.md](JS-PLUGIN-CATALOG.md)**: Answers: **"which Storefront JS plugins exist in THIS project?"** — from a cached catalog.
- **[JS-PLUGIN-EXTEND.md](JS-PLUGIN-EXTEND.md)**: `extend` registers a subclass for an existing plugin name and keeps the rest of the behavior — s….
- **[JS-PLUGIN-OVERRIDE.md](JS-PLUGIN-OVERRIDE.md)**: To completely replace the behavior of a core or third-party JS plugin, register a subclass with `override`.
- **[STOREFRONT-JS-PLUGIN.md](STOREFRONT-JS-PLUGIN.md)**: A vanilla JS plugin bound to a `data-*` attribute and initialized by the `PluginManager`.
- **[STOREFRONT-TYPESCRIPT.md](STOREFRONT-TYPESCRIPT.md)**: The Storefront supports TypeScript; JS plugins can be written as `.ts`. [STOREFRONT-TYPESCRIPT-TYPESCRIPT](STOREFRONT-TYPESCRIPT-TYPESCRIPT.md).

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (Storefront guides and reference) plus the Shopware 6.7 Storefront source, retrieved 2026-08-20.
