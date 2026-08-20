---
name: sw-javascript
description: Shopware Storefront JavaScript: writing, overriding and extending plugins, the plugin and event catalogues, TypeScript. Use when the request names a Shopware Storefront JS plugin or its events.
---

# Shopware Storefront JavaScript

Storefront JS is a plugin system: register a class against a selector. The catalogues list what already exists before you write a new one.

## Reference map

- **[JS-EVENT-CATALOG.md](JS-EVENT-CATALOG.md)**: Beantwortet: **„welche JS-Events existieren, wo werden sie gefeuert/abonniert, was tragen sie?"** — aus einem….
- **[JS-EVENTS.md](JS-EVENTS.md)**: Storefront-JS nutzt einen globalen Event-Emitter und native DOM-Events zur Kommunikation zwischen Plugins.
- **[JS-PLUGIN-CATALOG.md](JS-PLUGIN-CATALOG.md)**: Beantwortet: **„welche JS-Storefront-Plugins existieren in DIESEM Projekt?"** — aus einem gecachten Katalog.
- **[JS-PLUGIN-EXTEND.md](JS-PLUGIN-EXTEND.md)**: `extend` registriert eine Subklasse für einen bestehenden Plugin-Namen und behält den Rest des Verhaltens — g….
- **[JS-PLUGIN-OVERRIDE.md](JS-PLUGIN-OVERRIDE.md)**: Um das Verhalten eines Core-/Fremd-JS-Plugins komplett zu ersetzen, eine Subklasse registrieren mit `override`.
- **[STOREFRONT-JS-PLUGIN.md](STOREFRONT-JS-PLUGIN.md)**: Vanilla-JS-Plugin, das an ein `data-*`-Attribut gebunden und vom `PluginManager` initialisiert wird.
- **[STOREFRONT-TYPESCRIPT.md](STOREFRONT-TYPESCRIPT.md)**: Das Storefront unterstützt TypeScript; JS-Plugins können als `.ts` geschrieben werden. [STOREFRONT-TYPESCRIPT-TYPESCRIPT](STOREFRONT-TYPESCRIPT-TYPESCRIPT.md).

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (Storefront guides and reference) plus the Shopware 6.7 Storefront source, retrieved 2026-08-20.
