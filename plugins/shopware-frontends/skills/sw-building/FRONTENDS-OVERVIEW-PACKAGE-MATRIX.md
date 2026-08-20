# Shopware Frontends — Complete package matrix & architecture

## Contents

- [Package overview (exact npm names and versions)](#package-overview-exact-npm-names-and-versions)
- [Architecture principles](#architecture-principles)
- [Dependency graph](#dependency-graph)
- [Template/starter options](#templatestarter-options)
- [Nuxt module vs. Nuxt layer](#nuxt-module-vs-nuxt-layer)

## Package overview (exact npm names and versions)

| npm package name | Version | Purpose | Skill |
|---|---|---|---|
| `@shopware/api-client` | 1.5.0 | Typed HTTP client against the Store API + Admin API | `sw-api-client-js` |
| `@shopware/api-gen` | 1.5.0 | CLI tool: generate TypeScript types from the OpenAPI spec | `sw-api-gen-types` |
| `@shopware/composables` | 1.11.1 | Vue 3 composables: useCart, useCheckout, useUser, useListing, … | `sw-composables` |
| `@shopware/helpers` | 1.7.1 | Pure utility functions (prices, URLs, media, translations) | `sw-frontends-helpers` |
| `@shopware/cms-base-layer` | 3.0.0 | Nuxt layer with Vue components for CMS sections/blocks/elements | `sw-frontends-cms` |
| `@shopware/nuxt-module` | 1.4.4 | Nuxt module: integrate api-client + composables into Nuxt | `sw-frontends-nuxt` |
| `eslint-config-shopware` | 1.0.0 | Shared ESLint config for the monorepo | — |
| `tsconfig` | 0.0.0 | Shared TypeScript configuration for the monorepo | — |
| `@shopware/unocss-design-tokens-layer` | 1.0.0 | UnoCSS design token definitions | — |

## Architecture principles

### Layer model

```
┌─────────────────────────────────────────────────────────┐
│  Application (Nuxt / Vue / your own framework)          │
├──────────────────────┬──────────────────────────────────┤
│  @shopware/composables│  @shopware/cms-base-layer        │
│  (business logic)    │  (CMS rendering)                 │
├──────────────────────┴──────────────────────────────────┤
│  @shopware/helpers  (pure utilities, no state)           │
├─────────────────────────────────────────────────────────┤
│  @shopware/api-client  (HTTP, types, context token)      │
├─────────────────────────────────────────────────────────┤
│  Shopware 6 Store API  (REST/JSON)                       │
└─────────────────────────────────────────────────────────┘
```

### Type generation

```
Shopware instance
  └── /_info/openapi3.json
        └── @shopware/api-gen loadSchema  →  api-types/storeApiSchema.json
              └── @shopware/api-gen generate  →  api-types/storeApiTypes.d.ts
                    └── #shopware  (TypeScript path alias)
                          └── createAPIClient<operations>()
```

### Core principles

1. **Public HTTP APIs only**: no access to internal Shopware classes or the database — cloud-first, stable across updates.
2. **End-to-end type safety**: generated `operations` types from OpenAPI → every `invoke()` call is fully typed.
3. **Context token mechanics**: `sw-context-token` identifies the session (cart, login, currency). The client updates it automatically from response headers.
4. **Composable-first**: business logic in `@shopware/composables`, presentation in the app or `@shopware/cms-base-layer`.
5. **Framework-agnostic** (api-client + helpers), but **Nuxt-optimised** (nuxt-module + cms-base-layer).

## Dependency graph

```
@shopware/nuxt-module
  ├── @shopware/composables
  ├── @shopware/helpers
  ├── @shopware/api-client
  └── nuxt / @nuxt/kit / h3 / js-cookie

@shopware/cms-base-layer
  ├── @shopware/composables
  ├── @shopware/helpers
  ├── @shopware/api-client
  ├── @vueuse/core
  ├── @tresjs/nuxt (3D)
  ├── @nuxt/image
  └── xss / html-to-ast / scule / vuelidate

@shopware/composables
  └── @shopware/api-client  (peer)

@shopware/helpers
  └── (no @shopware dependencies — pure)

@shopware/api-gen
  ├── openapi-typescript
  ├── ts-morph
  └── prettier / yargs
```

## Template/starter options

The official demo store (Nuxt 4 + Tailwind + UnoCSS) serves as the reference implementation:

```bash
npx degit shopware/frontends/templates/vue-demo-store my-shop
```

Further templates in the monorepo under `templates/`.

## Nuxt module vs. Nuxt layer

| Feature | `@shopware/nuxt-module` | `@shopware/cms-base-layer` |
|---|---|---|
| Kind | Nuxt module (plugin registration) | Nuxt layer (components + composables) |
| Function | `createAPIClient`, SSR cookie handling, context token | Vue components for all CMS block/element/section types |
| Integration | `modules: ['@shopware/nuxt-module']` | `extends: ['@shopware/cms-base-layer']` |
| Configuration | `shopware: { endpoint, accessToken }` | `shopware-cms: {}` |
