# Shopware Frontends — Vollständige Paketmatrix & Architektur

## Paketübersicht (exakte npm-Namen und Versionen)

| npm-Paketname | Version | Zweck | Skill |
|---|---|---|---|
| `@shopware/api-client` | 1.5.0 | Typisierter HTTP-Client gegen Store API + Admin API | `sw-api-client-js` |
| `@shopware/api-gen` | 1.5.0 | CLI-Tool: TypeScript-Typen aus OpenAPI-Spec generieren | `sw-api-gen-types` |
| `@shopware/composables` | 1.11.1 | Vue-3-Composables: useCart, useCheckout, useUser, useListing, … | `sw-composables` |
| `@shopware/helpers` | 1.7.1 | Reine Utility-Funktionen (Preise, URLs, Media, Übersetzungen) | `sw-frontends-helpers` |
| `@shopware/cms-base-layer` | 3.0.0 | Nuxt-Layer mit Vue-Komponenten für CMS-Sections/Blocks/Elemente | `sw-frontends-cms` |
| `@shopware/nuxt-module` | 1.4.4 | Nuxt-Modul: api-client + composables in Nuxt integrieren | `sw-frontends-nuxt` |
| `eslint-config-shopware` | 1.0.0 | Shared ESLint-Config für das Monorepo | — |
| `tsconfig` | 0.0.0 | Shared TypeScript-Konfiguration für das Monorepo | — |
| `@shopware/unocss-design-tokens-layer` | 1.0.0 | UnoCSS Design-Token-Definitionen | — |

## Architekturprinzipien

### Schichtenmodell

```
┌─────────────────────────────────────────────────────────┐
│  Anwendung (Nuxt / Vue / eigenes Framework)             │
├──────────────────────┬──────────────────────────────────┤
│  @shopware/composables│  @shopware/cms-base-layer        │
│  (Geschäftslogik)    │  (CMS-Rendering)                 │
├──────────────────────┴──────────────────────────────────┤
│  @shopware/helpers  (reine Utilities, kein State)        │
├─────────────────────────────────────────────────────────┤
│  @shopware/api-client  (HTTP, Types, Context-Token)      │
├─────────────────────────────────────────────────────────┤
│  Shopware 6 Store API  (REST/JSON)                       │
└─────────────────────────────────────────────────────────┘
```

### Typgenerierung

```
Shopware-Instance
  └── /_info/openapi3.json
        └── @shopware/api-gen loadSchema  →  api-types/storeApiSchema.json
              └── @shopware/api-gen generate  →  api-types/storeApiTypes.d.ts
                    └── #shopware  (TypeScript-Pfad-Alias)
                          └── createAPIClient<operations>()
```

### Kernprinzipien

1. **Nur öffentliche HTTP-APIs**: kein Zugriff auf interne Shopware-Klassen oder Datenbank — cloud-first, stabil über Updates hinweg.
2. **Typsicherheit end-to-end**: generierte `operations`-Typen aus OpenAPI → jeder `invoke()`-Aufruf ist vollständig typisiert.
3. **Context-Token-Mechanik**: `sw-context-token` identifiziert die Session (Warenkorb, Login, Währung). Der Client aktualisiert ihn automatisch aus Response-Headern.
4. **Composable-First**: Geschäftslogik in `@shopware/composables`, Darstellung in der App oder `@shopware/cms-base-layer`.
5. **Framework-agnostisch** (api-client + helpers), aber **Nuxt-optimiert** (nuxt-module + cms-base-layer).

## Abhängigkeitsgraph

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
  └── (keine @shopware-Abhängigkeiten — rein)

@shopware/api-gen
  ├── openapi-typescript
  ├── ts-morph
  └── prettier / yargs
```

## Template-/Starter-Optionen

Der offizielle Demo-Store (Nuxt 4 + Tailwind + UnoCSS) dient als Referenzimplementierung:

```bash
npx degit shopware/frontends/templates/vue-demo-store my-shop
```

Weitere Templates im Monorepo unter `templates/`.

## Nuxt-Modul vs. Nuxt-Layer

| Merkmal | `@shopware/nuxt-module` | `@shopware/cms-base-layer` |
|---|---|---|
| Art | Nuxt-Modul (Plugin-Registrierung) | Nuxt-Layer (Komponenten + Composables) |
| Funktion | `createAPIClient`, SSR-Cookie-Handling, Context-Token | Vue-Komponenten für alle CMS-Block/Element/Section-Typen |
| Integration | `modules: ['@shopware/nuxt-module']` | `extends: ['@shopware/cms-base-layer']` |
| Konfiguration | `shopware: { endpoint, accessToken }` | `shopware-cms: {}` |
