# shopware-frontends

> Headless/composable storefronts with the official @shopware packages.

`shopware-frontends` documents **Shopware Frontends** — the official route to **decoupled (headless)
storefronts** on top of the Store API, as an alternative to the Twig storefront.

Covered are the `@shopware` packages and how they work together: **`@shopware/api-client`** (typed client,
`createAPIClient`/`invoke`, hooks, context token), **`@shopware/api-gen`** (generating TypeScript types from the
OpenAPI schema), **`@shopware/composables`** (40+ Vue composables such as `useCart`, `useCheckout`,
`useProductSearch`, `useListing`, `useCustomer`), **`@shopware/cms-base`** (headless CMS rendering),
**`@shopware/helpers`** (prices, translations, URLs) as well as **session/context handling** (SSR-safe) and the
**Nuxt setup**. Plus the official Frontends documentation: **routing**, **i18n/multi-language**, **B2B**, further
**features** (wishlist, broadcasting, sitemap …), **best practices/deployment** and **integrations** (Storyblok,
payment …).

Specialist: **`shopware-frontends-dev`**. **When to use:** for custom Vue/Nuxt frontends or a PWA. The API itself
(auth/endpoints) lives in `shopware-api`, custom Store API routes in `shopware-framework`, the classic storefront
in `shopware-storefront`.

Part of the **[claude-a-dev-team](../../README.md)** marketplace. The knowledge is distilled from the official sources and embedded; each skill's depth sits in flat SCREAMING-CASE.md reference files next to its SKILL.md and is loaded progressively.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-frontends@claude-a-dev-team
```

## Skills (3)

| Skill | Description |
|---|---|
| `sw-building` | Shopware Frontends application: getting started, framework choice, Nuxt setup, routing, CMS rendering, i18n, customisation, features, B2B. Use when building a headless Shopware storefront. |
| `sw-client` | Shopware Frontends client: `@shopware/api-client`, `api-gen` types, composables, session and context tokens. Use when the request names the Shopware `api-client`, `api-gen` or a composable. |
| `sw-practice` | Shopware Frontends practice: best practices, worked examples, third-party integrations, deployment. Use when deploying a Shopware Frontends storefront or looking for an example. |

## Agents (1)

| Agent | Description |
|---|---|
| `shopware-frontends-dev` | Specialist for Shopware Frontends (headless/composable storefronts): `@shopware/api-client`, `@shopware/api-gen` (type generation), `@shopware/composables` (`useCart`/`useCheckout`/…), `@shopware/cms-base` (CMS rendering), `@shopware/helpers`, Vue 3 / Nux… |
