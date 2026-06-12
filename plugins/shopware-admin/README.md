# shopware-admin

> Die Administration als Vue-3-App (Pinia/Vite/Meteor).

`shopware-admin` behandelt die **Administration** — eine eigenständige **Vue-3-Single-Page-App** mit **Pinia**
(State), **Vite** (Build) und der **Meteor-Komponentenbibliothek** (`mt-*`), erweitert über das globale
`Shopware`-Objekt.

Abgedeckt: eigene **Module** (`Module.register`), **Komponenten** (neu registrieren *und* per
`Component.override` erweitern), **Routing**/Navigation/Menü, **Datenhandling** über `repositoryFactory` + JS-
`Criteria`, **Pinia**- (und Legacy-Vuex-)Stores, eigene **Services/ApiServices**, **Mixins**, **Direktiven**,
**Snippets**, **Assets/Styles**, **ACL/Berechtigungen**, **Error-Handling**, **Data-Grids**, die
**Meteor-Komponenten** (`mt-*`) inkl. eingebauter **Utils/Filter**, der **Vite**-Build und das
**Meteor-Admin-SDK** (App-/Plugin-Erweiterung via postMessage, Locations, Data-Selectors) sowie **TypeScript**.

Die **Admin-Introspektion** (`/sw-admin-map`, `sw-admin-catalog`) katalogisiert alle Module, Komponenten (inkl.
**Slots/Props/Events**), Services, Stores, Mixins, Direktiven und Filter des konkreten Projekts. Spezialist:
**`shopware-admin`**; Scaffolder **`/sw-admin-module`**, **`/sw-admin-component`**. **Wann nutzen:** für Backend-/
Verwaltungs-Oberflächen. Bedien-/Betreiberwissen (nicht Code) liegt in `shopware-merchant`.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Das Wissen ist aus den offiziellen Quellen destilliert und eingebettet; Skills laden ihre Tiefe progressiv aus `references/`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-admin@claude-a-dev-team
```

## Skills (29)

`sw-admin-acl-permissions`, `sw-admin-api-requests`, `sw-admin-assets`, `sw-admin-catalog`, `sw-admin-component`, `sw-admin-component-override`, `sw-admin-data-grid`, `sw-admin-data-handling`, `sw-admin-directives`, `sw-admin-error-handling`, `sw-admin-menu`, `sw-admin-mixins`, `sw-admin-module`, `sw-admin-pinia-store`, `sw-admin-repository-js`, `sw-admin-routing`, `sw-admin-sdk`, `sw-admin-services`, `sw-admin-snippets`, `sw-admin-styles`, `sw-admin-typescript`, `sw-admin-utils-filters`, `sw-admin-vite`, `sw-admin-vuex-store`, `sw-meteor-admin-sdk`, `sw-meteor-components`, `sw-meteor-composables`, `sw-meteor-getting-started`, `sw-meteor-usage-guidelines`

## Agents (2)

- **`shopware-admin-mapper`** — Introspektions-Agent: scannt ein Shopware-6-Projekt nach Admin-Bausteinen (Core-Administration + custom) und erzeugt einen gecachten Katalog (.shopware-catalog/admin.md) mit Modulen, Komponenten, Services, Mixins, Direkt
- **`shopware-admin`** — Spezialist für die Shopware-6.7-Administration (Vue 3, Pinia, Vite, Meteor mt-*): Module, Komponenten (neu/override), Routing/Navigation/ACL, Datenhandling (repositoryFactory/Criteria), Services/ApiServices, Mixins/Direk

## Commands (3)

- **`/sw-admin-component`** — Scaffold einer Admin-Komponente in Shopware 6 (Vue 3) — index.js (Component.register), .html.twig (Meteor mt-*), optional .scss; oder ein Component.override.
- **`/sw-admin-map`** — Scannt das aktuelle Shopware-Projekt (Core-Administration + custom) und erzeugt/aktualisiert den Admin-Katalog .shopware-catalog/admin.md (Module, Komponenten, Services, Stores, Mixins, Direktiven, Filter, ApiServices).
- **`/sw-admin-module`** — Scaffold eines Admin-Moduls in Shopware 6 (Vue 3) — module/<name>/index.js mit Module.register, List/Detail-Pages, Navigation, Snippets, ACL.
