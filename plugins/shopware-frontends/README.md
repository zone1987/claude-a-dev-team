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

| Skill | Beschreibung |
|---|---|
| `sw-frontends-overview` | Überblick über Shopware Frontends (headless/composable Storefronts): Architektur, die @shopware-Pakete (api-client, composables, api-gen, cms-base, helpers), Store-API-getrieben, Vue 3 / Nuxt-Starter, Abgrenzung zum Twig-Storefront |
| `sw-api-client-js` | Der @shopware/api-client für headless Shopware-Frontends: createAPIClient, invoke(operation), Store-API-Aufrufe, Context-Token-Handling, Request-Hooks, Admin-Client-Variante |
| `sw-api-gen-types` | TypeScript-Typen für Shopware-Frontends generieren mit @shopware/api-gen: OpenAPI-Schema laden (loadSchema) und Typen erzeugen (generate), eigene/Plugin-Endpunkte einbeziehen, #shopware Alias |
| `sw-composables` | Die @shopware/composables (Vue 3) für headless Shopware-Frontends: useCart, useCheckout, useProductSearch, useListing, useCustomer, useUser, useSessionContext, useNavigation, useCms; Bereitstellung via app context |
| `sw-frontends-b2b` | Shopware Frontends B2B-Features: Quote Management (Angebot anfragen, ablehnen, aendern, Bestellung aus Angebot), Quick Order, useB2bQuoteManagement Composable |
| `sw-frontends-best-practices` | Best Practices fuer Shopware Frontends: Performance (Lighthouse), Bilder (WebP, responsive, CLS, LCP), Error Handling, Testing (E2E Playwright, A/B, Accessibility mit axe-core), Deployment (SSR/SSG/SPA, Nitro, Vercel, Netlify), CORS, devSto |
| `sw-frontends-cms` | CMS-Rendering in Shopware-Frontends mit @shopware/cms-base: Sections/Blocks/Elemente aus der Store-API rendern, Komponenten-Resolver (CmsGenericElement/Block), eigene CMS-Komponenten registrieren/überschreiben |
| `sw-frontends-customization` | Anpassung von Shopware Frontends: Composables ueberschreiben/erweitern, CMS-Komponenten anpassen (fehlende Komponenten, Overwriting), Routing (SeoUrl, resolvePath), Mehrsprachigkeit (vue-i18n, Domains), Nuxt Layers fuer Multi-Brand, Sitemap |
| `sw-frontends-deployment` | Deployment-Strategien fuer Shopware Frontends: SSR (Server-Side Rendering), SSG (Static Site Generation), SPA, Nitro-Presets (Vercel, Netlify, Cloudflare), HTTPS localhost, CORS, Proxy, Troubleshooting (412, devStorefrontUrl, DDEV) |
| `sw-frontends-examples` | Konkrete Code-Rezepte fuer Shopware Frontends: Login-Formular, Warenkorb (Cart), Checkout, Produktlisting (useListing, Filter, Pagination), Produktdetailseite, Wunschliste (Wishlist), Preisanzeige (Tiers, Liste/Streichpreis), JSON-LD, B2B Q |
| `sw-frontends-features` | Shopware Frontends Feature-Implementierungen: Wishlist (lokal+remote, sync), Broadcasting (Tab-Synchronisation via BroadcastChannel), Maintenance Mode (Erkennung, 503-Error, IP-Allowlisting), Sitemap (Admin+Frontends), Custom Products Exten |
| `sw-frontends-framework` | Shopware Frontends interne Architektur: Packages (api-client, helpers, composables, nuxt-module, cms-base), Context-Composables, Shared Composables, Styling/UnoCSS, Design Tokens |
| `sw-frontends-getting-started` | Shopware Frontends Projektstart, Templates, Setup und Konfiguration |
| `sw-frontends-helpers` | Die @shopware/helpers für Shopware-Frontends: Preis-/Währungsformatierung, Übersetzungs-Helfer (getTranslatedProperty), URL-/SEO-Helfer (buildUrlPrefix), Media-/Thumbnail-Helfer, Cart-/Preis-Utilities |
| `sw-frontends-i18n` | Shopware Frontends Mehrsprachigkeit: vue-i18n Setup, Same-Domain vs |
| `sw-frontends-integrations` | Integrationen fuer Shopware Composable Frontends: Payment (PayPal Express, Adyen, Amazon Pay, Braintree, Mollie), CMS (Storyblok, Strapi), Commercial (B2B Quick-Order, B2B Quote-Management, Custom Products, Digital Sales Rooms), Community M |
| `sw-frontends-nuxt` | Ein Shopware-Frontend mit Nuxt/Vue aufsetzen: Vue-Starter-Template (Nuxt 4 / Vue 3 / Vite / Tailwind), api-client + composables als Nuxt-Plugin bereitstellen, SSR-Context-Token, Projektstruktur |
| `sw-frontends-routing` | Shopware Frontends Routing: SeoUrl-Aufloesung, URL-zu-Route (useNavigationSearch), Route-zu-Seite (Produkt/Kategorie/Landing), getCategoryRoute/getProductRoute Helper, SEO-API-Calls einsparen via History State, catch-all [...all].vue Patter |
| `sw-frontends-session-context` | Session-/Kontext-Handling in Shopware-Frontends: useSessionContext, der sw-context-token (Persistenz in Cookie/Storage), Sprache/Währung/Versand/Zahlung wechseln, SSR-sicheres Token-Handling in Nuxt |

## Agents (1)

| Agent | Beschreibung |
|---|---|
| `shopware-frontends-dev` | Spezialist für Shopware Frontends (headless/composable Storefronts): @shopware/api-client, @shopware/api-gen (Typgenerierung), @shopware/composables (useCart/useCheckout/…), @shopware/cms-base (CMS-Rendering), @shopware/helpers, Vue 3 / Nux |
