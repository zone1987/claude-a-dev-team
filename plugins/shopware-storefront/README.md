# shopware-storefront

> Everything for the customer-facing storefront (Twig + JavaScript + SCSS/theme).

`shopware-storefront` covers the **customer-facing storefront** in its full breadth — server-side (PHP/Twig) as well
as client-side (JavaScript/TypeScript, SCSS/theme).

Server-side: **controllers**, **pages/pagelets** and **PageLoaders**, enriching existing pages via
`*PageLoadedEvent` + `addExtension`, **Twig** (template override with `sw_extends`/blocks, custom extensions/
functions), **caching** (httpCache/ESI), **SEO URLs** & **sitemap**, **cookie consent**, **captcha**,
**listing filters** and **custom sorting**, **snippets** (i18n). Client-side: **JavaScript storefront plugins**
(`PluginBaseClass`, `data-*` binding, `PluginManager`), **overriding/extending** existing plugins,
**AJAX**/`HttpClient`, **JS events** (`$emitter`), **assets/icons** and the complete **theme system**
(creating a theme, `theme.json` config, inheritance, assets, compilation). Plus **TypeScript** in the storefront and
**accessibility**.

Three **introspections** make the current state of a project tangible: the **JS plugin catalogue**
(`/sw-js-plugin-map`), the **JS event catalogue** (publish/subscribe + arguments) and the **SCSS structure
catalogue** (which file/variable lives where). Scaffolders: **`/sw-controller`**, **`/sw-js-plugin`**,
**`/sw-theme`**. **When to use:** for a shop frontend built on the classic Twig storefront. For decoupled frontends
use `shopware-frontends` instead.

Part of the **[claude-a-dev-team](../../README.md)** marketplace. The knowledge is distilled from the official sources and embedded; each skill's depth sits in flat SCREAMING-CASE.md reference files next to its SKILL.md and is loaded progressively.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-storefront@claude-a-dev-team
```

## Skills (5)

| Skill | Description |
|---|---|
| `sw-controller` | Shopware Storefront controllers, Pages, Pagelets, PageLoaders, attaching data, AJAX routes. Use when building a Shopware Storefront controller or page. |
| `sw-features` | Shopware Storefront features: listing filters, custom sorting, SEO URLs, sitemap, cookie consent, captcha, HTTP caching. Use when the request names a Shopware listing filter or SEO URL. |
| `sw-javascript` | Shopware Storefront JavaScript: writing, overriding and extending plugins, the plugin and event catalogues, TypeScript. Use when the request names a Shopware Storefront JS plugin or its events. |
| `sw-theme` | Shopware themes: creating a theme, `theme.json` config, inheritance, multiple themes, compilation, SCSS structure and variables, assets and icons. Use when building or styling a Shopware theme. |
| `sw-twig` | Shopware Storefront Twig: template inheritance and blocks, Twig extensions, available functions, snippets. Use when overriding a Shopware Storefront template or writing a Twig extension. |

## Agents (2)

| Agent | Description |
|---|---|
| `shopware-js-plugin-mapper` | Introspection agent: scans a Shopware 6 project for JavaScript storefront plugins AND JS events (core storefront + custom) and produces two cached catalogues: `.shopware-catalog/js-plugins.md` (plugin name, file, purpose, selector, opti… |
| `shopware-storefront` | Specialist for the Shopware 6.7 storefront: controllers/pages/pagelets/PageLoaders, attaching data to pages, Twig (templates/extensions/functions), SCSS/assets/icons/theme, JavaScript storefront plugins (writing/overriding/extending), AJ… |

## Commands (4)

| Command | Description |
|---|---|
| `/sw-controller` | Scaffolds a Shopware 6 storefront controller including its route (`routes.xml`/`#[Route]`), a PageLoader + Page struct and a Twig template |
| `/sw-js-plugin-map` | Scans the current Shopware project for JavaScript storefront plugins AND JS events (core + custom) and creates/updates `.shopware-catalog/js-plugins.md` (name, file, purpose, selector, options, registration, overrides) and `.shopwar…` |
| `/sw-js-plugin` | Scaffolds a Shopware 6 JavaScript storefront plugin (`PluginBaseClass`) including |
| `/sw-theme` | Scaffolds a Shopware 6 storefront theme (theme plugin with `theme.json`, `ThemeInterface`, SCSS/JS structure and config fields) |
