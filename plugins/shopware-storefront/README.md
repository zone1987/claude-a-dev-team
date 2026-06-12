# shopware-storefront

> Alles für die kundenseitige Storefront (Twig + JavaScript + SCSS/Theme).

`shopware-storefront` umfasst die **kundenseitige Storefront** in ihrer ganzen Breite — serverseitig (PHP/Twig) wie
clientseitig (JavaScript/TypeScript, SCSS/Theme).

Serverseitig: **Controller**, **Pages/Pagelets** und **PageLoader**, das Anreichern bestehender Seiten über
`*PageLoadedEvent` + `addExtension`, **Twig** (Template-Override mit `sw_extends`/Blöcken, eigene Extensions/
Funktionen), **Caching** (httpCache/ESI), **SEO-URLs** & **Sitemap**, **Cookie-Consent**, **Captcha**,
**Listing-Filter** und **Custom-Sorting**, **Snippets** (i18n). Clientseitig: **JavaScript-Storefront-Plugins**
(`PluginBaseClass`, `data-*`-Bindung, `PluginManager`), das **Überschreiben/Erweitern** bestehender Plugins,
**AJAX**/`HttpClient`, **JS-Events** (`$emitter`), **Assets/Icons** und das vollständige **Theme-System**
(Theme erstellen, `theme.json`-Config, Inheritance, Assets, Kompilierung). Dazu **TypeScript** im Storefront und
**Accessibility**.

Drei **Introspektionen** machen den Ist-Zustand des Projekts greifbar: **JS-Plugin-Katalog** (`/sw-js-plugin-map`),
**JS-Event-Katalog** (publish/subscribe + Argumente) und der **SCSS-Strukturkatalog** (wo welche Datei/Variable liegt).
Scaffolder: **`/sw-controller`**, **`/sw-js-plugin`**, **`/sw-theme`**. **Wann nutzen:** für Shop-Frontend mit dem
klassischen Twig-Storefront. Entkoppelte Frontends stattdessen → `shopware-frontends`.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Das Wissen ist aus den offiziellen Quellen destilliert und eingebettet; Skills laden ihre Tiefe progressiv aus `references/`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-storefront@claude-a-dev-team
```

## Skills (39)

`sw-accessibility`, `sw-ajax-data`, `sw-captcha`, `sw-cookie-manager`, `sw-custom-sorting`, `sw-js-event-catalog`, `sw-js-events`, `sw-js-plugin-catalog`, `sw-js-plugin-extend`, `sw-js-plugin-override`, `sw-listing-filter`, `sw-page-loader`, `sw-scss-catalog`, `sw-scss-structure`, `sw-scss-variables`, `sw-seo-urls`, `sw-sitemap`, `sw-storefront-assets`, `sw-storefront-caching`, `sw-storefront-controller`, `sw-storefront-data`, `sw-storefront-icons`, `sw-storefront-js-plugin`, `sw-storefront-page`, `sw-storefront-pagelet`, `sw-storefront-scss`, `sw-storefront-translations`, `sw-storefront-typescript`, `sw-theme`, `sw-theme-assets`, `sw-theme-compile`, `sw-theme-config`, `sw-theme-create`, `sw-theme-inheritance`, `sw-theme-multiple`, `sw-theme-storefront-customization`, `sw-twig-extension`, `sw-twig-functions`, `sw-twig-templates`

## Agents (2)

- **`shopware-js-plugin-mapper`** — Introspektions-Agent: scannt ein Shopware-6-Projekt nach JavaScript-Storefront-Plugins UND JS-Events (Core-Storefront + custom) und erzeugt zwei gecachte Kataloge: .shopware-catalog/js-plugins.md (Plugin-Name, Datei, Auf
- **`shopware-storefront`** — Spezialist für das Shopware-6.7-Storefront: Controller/Pages/Pagelets/PageLoader, Daten an Pages hängen, Twig (Templates/Extensions/Funktionen), SCSS/Assets/Icons/Theme, JavaScript-Storefront-Plugins (schreiben/überschre

## Commands (4)

- **`/sw-controller`** — Scaffold eines Storefront-Controllers in Shopware 6 inkl. Route (routes.xml/#[Route]), PageLoader + Page-Struct und Twig-Template.
- **`/sw-js-plugin-map`** — Scannt das aktuelle Shopware-Projekt nach JavaScript-Storefront-Plugins UND JS-Events (Core + custom) und erzeugt/aktualisiert .shopware-catalog/js-plugins.md (Name, Datei, Aufgabe, Selector, Optionen, Registrierung, Ove
- **`/sw-js-plugin`** — Scaffold eines JavaScript-Storefront-Plugins in Shopware 6 (PluginBaseClass) inkl.
- **`/sw-theme`** — Scaffold eines Storefront-Themes in Shopware 6 (Theme-Plugin mit theme.json, ThemeInterface, SCSS/JS-Struktur und Config-Feldern).
