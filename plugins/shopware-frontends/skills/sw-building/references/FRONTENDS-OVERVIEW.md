# Shopware Frontends — Overview

Framework for **decoupled (headless) storefronts** based on the **Store API** — an alternative to the Twig storefront,
ideal for custom Vue/Nuxt frontends.

## Packages
| Package | Purpose |
|---|---|
| `@shopware/api-client` | typed Store API client (`createAPIClient`, `invoke`) → `sw-api-client-js` |
| `@shopware/api-gen` | generate TypeScript types from the OpenAPI spec → `sw-api-gen-types` |
| `@shopware/composables` | Vue composables (`useCart`, `useCheckout`, …) → `sw-composables` |
| `@shopware/helpers` | utils (prices, translations, URLs) → `sw-frontends-helpers` |
| `@shopware/cms-base` | rendering of CMS sections/blocks/elements → `sw-frontends-cms` |

## Principles
- **HTTP APIs only** (Store API), no internal volatile APIs → cloud-first, stable.
- Stack of the templates: **Nuxt 4 / Vue 3 / Vite / Tailwind** (`sw-frontends-nuxt`).
- Session/context via `sw-context-token` (`sw-frontends-session-context`).

For the API itself (endpoints/auth) see the plugin `shopware-api` (`sw-store-api-endpoints`, `sw-store-api-auth`).
For the classic Twig storefront instead: plugin `shopware-storefront`.

→ Complete reference: [FRONTENDS-OVERVIEW-PACKAGE-MATRIX.md](FRONTENDS-OVERVIEW-PACKAGE-MATRIX.md)
