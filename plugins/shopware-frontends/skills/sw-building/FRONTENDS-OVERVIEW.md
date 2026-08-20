# Shopware Frontends — Überblick

Framework für **entkoppelte (headless) Storefronts** auf Basis der **Store API** — Alternative zum Twig-Storefront,
ideal für eigene Vue/Nuxt-Frontends.

## Pakete
| Paket | Zweck |
|---|---|
| `@shopware/api-client` | typisierter Store-API-Client (`createAPIClient`, `invoke`) → `sw-api-client-js` |
| `@shopware/api-gen` | TypeScript-Typen aus der OpenAPI generieren → `sw-api-gen-types` |
| `@shopware/composables` | Vue-Composables (`useCart`, `useCheckout`, …) → `sw-composables` |
| `@shopware/helpers` | Utils (Preise, Übersetzungen, URLs) → `sw-frontends-helpers` |
| `@shopware/cms-base` | Rendering der CMS-Sections/Blocks/Elemente → `sw-frontends-cms` |

## Prinzipien
- **Nur HTTP-APIs** (Store API), keine internen volatilen APIs → cloud-first, stabil.
- Stack der Templates: **Nuxt 4 / Vue 3 / Vite / Tailwind** (`sw-frontends-nuxt`).
- Session/Kontext über `sw-context-token` (`sw-frontends-session-context`).

Für die API selbst (Endpunkte/Auth) siehe Plugin `shopware-api` (`sw-store-api-endpoints`, `sw-store-api-auth`).
Klassisches Twig-Storefront stattdessen: Plugin `shopware-storefront`.

→ Vollständige Referenz: [FRONTENDS-OVERVIEW-PACKAGE-MATRIX.md](FRONTENDS-OVERVIEW-PACKAGE-MATRIX.md)
