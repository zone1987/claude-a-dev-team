# shopware-frontends

> Headless/Composable Storefronts mit den offiziellen @shopware-Paketen.

`shopware-frontends` dokumentiert **Shopware Frontends** — den offiziellen Weg zu **entkoppelten (headless)
Storefronts** auf Basis der Store API, als Alternative zum Twig-Storefront.

Abgedeckt sind die `@shopware`-Pakete und ihr Zusammenspiel: **`@shopware/api-client`** (typisierter Client,
`createAPIClient`/`invoke`, Hooks, Context-Token), **`@shopware/api-gen`** (TypeScript-Typen aus der OpenAPI
generieren), **`@shopware/composables`** (40+ Vue-Composables wie `useCart`, `useCheckout`, `useProductSearch`,
`useListing`, `useCustomer`), **`@shopware/cms-base`** (CMS-Rendering headless), **`@shopware/helpers`** (Preise,
Übersetzungen, URLs) sowie **Session-/Context-Handling** (SSR-sicher) und das **Nuxt-Setup**. Dazu die offizielle
Frontends-Doku: **Routing**, **i18n/Mehrsprachigkeit**, **B2B**, weitere **Features** (Wishlist, Broadcasting,
Sitemap …), **Best Practices/Deployment** und **Integrationen** (Storyblok, Payment …).

Spezialist: **`shopware-frontends-dev`**. **Wann nutzen:** für eigene Vue/Nuxt-Frontends bzw. PWA. Die API selbst
(Auth/Endpunkte) liegt in `shopware-api`, eigene Store-API-Routen in `shopware-framework`, das klassische Storefront
in `shopware-storefront`.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Das Wissen ist aus den offiziellen Quellen destilliert und eingebettet; Skills laden ihre Tiefe progressiv aus `references/`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-frontends@claude-a-dev-team
```

## Skills (19)

`sw-frontends-overview`, `sw-api-client-js`, `sw-api-gen-types`, `sw-composables`, `sw-frontends-b2b`, `sw-frontends-best-practices`, `sw-frontends-cms`, `sw-frontends-customization`, `sw-frontends-deployment`, `sw-frontends-examples`, `sw-frontends-features`, `sw-frontends-framework`, `sw-frontends-getting-started`, `sw-frontends-helpers`, `sw-frontends-i18n`, `sw-frontends-integrations`, `sw-frontends-nuxt`, `sw-frontends-routing`, `sw-frontends-session-context`

## Agents (1)

- **`shopware-frontends-dev`** — Spezialist für Shopware Frontends (headless/composable Storefronts): @shopware/api-client, @shopware/api-gen (Typgenerierung), @shopware/composables (useCart/useCheckout/…), @shopware/cms-base (CMS-Rendering), @shopware/
