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

| Skill | Beschreibung |
|---|---|
| `sw-accessibility` | Shopware 6 Storefront Barrierefreiheit (a11y): WCAG 2.1 AA, BITV 2.0, Feature-Flag ACCESSIBILITY_TWEAKS, Breaking-Changes-Handling, Checklist (ARIA, Fokus, Tastatur, Semantik, Farben, Modals, Skip Links) |
| `sw-ajax-data` | Daten per JavaScript im Shopware-6-Storefront laden: HttpClient / StoreApiClient, fetch gegen frontend.*-Route oder store-api, Daten via data-Attribute ins DOM, JSON-Response aus Controller |
| `sw-captcha` | Captcha im Shopware-6-Storefront: eingebaute Captchas (Honeypot, basicCaptcha, googleReCaptcha) nutzen/konfigurieren und ein eigenes Captcha via AbstractCaptcha registrieren |
| `sw-cookie-manager` | Cookies & Cookie-Consent im Shopware-6-Storefront: Cookie zur Cookie-Konfiguration hinzufügen via CookieProviderInterface (Decorator), auf Consent-Änderungen reagieren |
| `sw-custom-sorting` | Eigene Sortier-Option für das Produkt-Listing in Shopware 6: ProductSortingEntity per Migration/Fixture anlegen, Felder + Richtung, im Listing verfügbar machen |
| `sw-js-event-catalog` | Den projektspezifischen Katalog der JavaScript-Storefront-Events von Shopware nutzen — welche JS-Events es im KONKRETEN Projekt gibt (Core + custom), WO sie published werden ($emitter.publish), WO subscribed wird (document.$emitter.subscrib |
| `sw-js-events` | Auf JavaScript-Events im Shopware-6-Storefront reagieren: PluginManager-Events, document.$emitter, native Events, zwischen JS-Plugins kommunizieren |
| `sw-js-plugin-catalog` | Den projektspezifischen Katalog der JavaScript-Storefront-Plugins von Shopware nutzen — welche JS-Plugins es im KONKRETEN Projekt gibt (Core + custom), was sie tun, wo sie liegen, welcher Selector/welche Optionen, wie man sie überschreibt/e |
| `sw-js-plugin-extend` | Ein bestehendes JS-Storefront-Plugin in Shopware 6 erweitern (statt ersetzen): PluginManager.extend, einzelne Methoden ergänzen, super-Aufruf |
| `sw-js-plugin-override` | Ein bestehendes JS-Storefront-Plugin in Shopware 6 vollständig ersetzen via PluginManager.override (gleicher Name) |
| `sw-listing-filter` | Eigener Listing-Filter (Facette) im Shopware-6-Storefront: ProductListingCriteriaEvent / ProductListingResultEvent, Filter-Aggregation hinzufügen, im Template rendern |
| `sw-page-loader` | Einen Storefront-PageLoader in Shopware 6 bauen: GenericPageLoader nutzen, eigene Daten ergänzen, PageLoadedEvent dispatchen; Page-Loader-Extension-Architektur |
| `sw-scss-catalog` | Introspektions-Skill: scannt alle SCSS-Dateien eines konkreten Shopware-Projekts (Core + Plugins + aktives Theme) und legt einen Katalog in `.shopware-catalog/scss.md` ab |
| `sw-scss-structure` | Vollständige SCSS-Struktur des Shopware 6 Storefronts (Trunk-Quelle) |
| `sw-scss-variables` | SCSS-Variablen im Shopware-6-Storefront bereitstellen/überschreiben: Theme-Config-Felder → SCSS-Variablen, Variablen per Subscriber injizieren, theme_config() |
| `sw-seo-urls` | SEO-URLs in Shopware 6: eigene SeoUrlRoute (AbstractSeoUrlRoute) + Template, SEO-URLs generieren/aktualisieren, seoUrl() im Twig, robots.txt erweitern |
| `sw-sitemap` | Sitemap in Shopware 6 erweitern: eigene URLs via AbstractUrlProvider hinzufügen, Sitemap-Einträge entfernen/ändern, Sitemap-Generierung |
| `sw-storefront-assets` | Statische Assets & Medien im Shopware-6-Storefront: public/-Assets, asset()/theme assets, assets:install, Thumbnails via searchMedia/sw_thumbnails |
| `sw-storefront-caching` | HTTP-/Page-Caching im Shopware-6-Storefront: @httpCache-Attribut, Cache-Tags, ESI/sw_include, no-store für dynamische Inhalte, reverse proxy |
| `sw-storefront-controller` | Eigener Storefront-Controller in Shopware 6: StorefrontController erweitern, Route definieren (routes.xml / #[Route]), renderStorefront(), Page laden, redirect/JSON |
| `sw-storefront-data` | Zusätzliche Daten an eine bestehende Storefront-Page hängen (ohne eigenen Controller) via Subscriber auf das PageLoadedEvent und addExtension |
| `sw-storefront-icons` | Eigene SVG-Icons im Shopware-6-Storefront: Icon-Set unter Resources/app/storefront/dist/assets/icon, sw_icon mit pack, Icon überschreiben |
| `sw-storefront-js-plugin` | Ein eigenes JavaScript-Storefront-Plugin in Shopware 6 schreiben & registrieren: Plugin extends window.PluginBaseClass, init(), this.options, _registerEvents, data-Selector, Registrierung in main.js via PluginManager.register, Build |
| `sw-storefront-page` | Eine Storefront-Page in Shopware 6: Page-Struct (extends Page) + PageLoader, der Pagelets/Daten zusammensetzt und ein PageLoadedEvent dispatcht |
| `sw-storefront-pagelet` | Ein Storefront-Pagelet in Shopware 6: wiederverwendbarer Teilbereich (extends Pagelet) mit eigenem PageletLoader, ideal für AJAX-Nachladung |
| `sw-storefront-scss` | Eigenes SCSS/Styling im Storefront eines Shopware-6-Plugins: base.scss unter Resources/app/storefront/src/scss, Einbindung, Bootstrap-5-Nutzung, Build |
| `sw-storefront-translations` | Storefront-Snippets (Übersetzungen) in Shopware 6: snippet/<locale>.json unter Resources, \|trans, Platzhalter, Snippet-Set/Namespacing |
| `sw-storefront-typescript` | TypeScript in Shopware-6-Storefront-Plugins: tsconfig einrichten, JS-Storefront-Plugins als .ts schreiben, PluginBaseClass/Optionen typisieren, eigene Types/Interfaces & .d.ts, window/PluginManager-Typen |
| `sw-theme` | Ein Storefront-Theme in Shopware 6 erstellen: ThemePlugin (extends ThemeInterface/Plugin), theme.json, Struktur, Theme aktivieren/kompilieren |
| `sw-theme-assets` | Assets und Icons in einem Shopware 6 Theme: theme.json asset-Pfade, theme:compile kopiert Assets, Twig asset()-Funktion, SCSS-Pfadvariable, custom Icon-Packs (iconSets), sw_icon Twig-Tag |
| `sw-theme-compile` | Shopware 6 Theme kompilieren: theme:compile, theme:refresh, Dev-Server/Watch (shopware-cli storefront-watch, composer run storefront:dev-server), JS-Build via shopware-cli/webpack, atomic compilation |
| `sw-theme-config` | Theme-Konfiguration in Shopware 6: config-Felder in theme.json (Farben, Fonts, Tabs/Blocks/Sections), als SCSS-Variablen & theme_config() nutzbar, Defaults |
| `sw-theme-create` | Shopware 6 Theme via CLI erstellen: theme:create, Verzeichnisstruktur, plugin:install --activate, theme:change (SalesChannel-Zuweisung), theme.json-Gerüst komplett |
| `sw-theme-inheritance` | Theme-Vererbung in Shopware 6: @-Referenzen in theme.json (@Storefront, @ParentTheme), Reihenfolge von views/style/ script/asset, Bootstrap-Util-Imports |
| `sw-theme-multiple` | Mehrere Themes in Shopware 6: configInheritance (Theme-Konfig vererben), je SalesChannel ein anderes Theme zuweisen, Basis-Theme + Channel-Theme-Muster, theme:change pro SalesChannel |
| `sw-theme-storefront-customization` | Storefront im Theme anpassen: SCSS/JS hinzufügen, Bootstrap-Variablen überschreiben (overrides.scss), responsive Breakpoints customizen (sw-breakpoint-*), @StorefrontBootstrap (ohne Shopware-Skin) |
| `sw-twig-extension` | Eine eigene Twig-Extension in Shopware 6 registrieren (AbstractExtension): Functions/Filters für Storefront-Templates, Service-Tag twig.extension |
| `sw-twig-functions` | Eingebaute Storefront-Twig-Funktionen in Shopware 6 nutzen: sw_icon, sw_thumbnails/searchMedia, seoUrl, sw_csrf, config/theme_config, sw_include |
| `sw-twig-templates` | Storefront-Twig-Templates in Shopware 6 überschreiben/erweitern: Verzeichnis-Konvention Resources/views/storefront, {% sw_extends %}, {% block %} überschreiben, {{ parent() }}, Header/Footer anpassen |

## Agents (2)

| Agent | Beschreibung |
|---|---|
| `shopware-js-plugin-mapper` | Introspektions-Agent: scannt ein Shopware-6-Projekt nach JavaScript-Storefront-Plugins UND JS-Events (Core-Storefront + custom) und erzeugt zwei gecachte Kataloge: .shopware-catalog/js-plugins.md (Plugin-Name, Datei, Aufgabe, Selector, Opti |
| `shopware-storefront` | Spezialist für das Shopware-6.7-Storefront: Controller/Pages/Pagelets/PageLoader, Daten an Pages hängen, Twig (Templates/Extensions/Funktionen), SCSS/Assets/Icons/Theme, JavaScript-Storefront-Plugins (schreiben/überschreiben/ erweitern), AJ |

## Commands (4)

| Command | Beschreibung |
|---|---|
| `/sw-controller` | Scaffold eines Storefront-Controllers in Shopware 6 inkl. Route (routes.xml/#[Route]), PageLoader + Page-Struct und Twig-Template |
| `/sw-js-plugin-map` | Scannt das aktuelle Shopware-Projekt nach JavaScript-Storefront-Plugins UND JS-Events (Core + custom) und erzeugt/aktualisiert .shopware-catalog/js-plugins.md (Name, Datei, Aufgabe, Selector, Optionen, Registrierung, Overrides) und .shopwar |
| `/sw-js-plugin` | Scaffold eines JavaScript-Storefront-Plugins in Shopware 6 (PluginBaseClass) inkl |
| `/sw-theme` | Scaffold eines Storefront-Themes in Shopware 6 (Theme-Plugin mit theme.json, ThemeInterface, SCSS/JS-Struktur und Config-Feldern) |
