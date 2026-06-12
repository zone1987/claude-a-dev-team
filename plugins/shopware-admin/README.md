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

| Skill | Beschreibung |
|---|---|
| `sw-admin-acl-permissions` | ACL/Berechtigungen im Shopware-6-Admin: Shopware.Service('privileges').addPrivilegeMappingEntry, acl.can(), privilege an Modul/Route/Navigation koppeln, viewer/editor/creator/deleter |
| `sw-admin-api-requests` | Eigene API-Requests im Shopware-6-Admin: httpClient/ApiService, eigenen ApiService registrieren, gegen eigene Admin-API-Route (api/_action) sprechen, Auth-Header |
| `sw-admin-assets` | Assets im Shopware-6-Admin: statische Dateien/Bilder in der Administration, asset-Pfade, Icons (mt-icon/sw-icon), Medien aus dem DAL |
| `sw-admin-catalog` | Den projektspezifischen Admin-Katalog von Shopware nutzen — welche Admin-Module, Komponenten, Services, Mixins, Direktiven, Filter und ApiServices es im KONKRETEN Projekt (Core + custom) gibt, wo sie liegen und was sie tun |
| `sw-admin-component` | Eine eigene Admin-Komponente in Shopware 6 registrieren (Vue 3): Shopware.Component.register, .twig-Template, index.js, Composition/Options API, Meteor-Komponenten nutzen |
| `sw-admin-component-override` | Eine bestehende Admin-Komponente in Shopware 6 überschreiben/erweitern: Shopware.Component.override, Twig-Block override mit {% parent %}, override hinzufügen ohne Original zu ersetzen |
| `sw-admin-data-grid` | Listen/Tabellen im Shopware-6-Admin: sw-data-grid/sw-entity-listing, Columns, Sortierung/Paginierung via listing-Mixin, Bulk-Edit, Inline-Edit |
| `sw-admin-data-handling` | Datenhandling im Shopware-6-Admin: repositoryFactory, Criteria (JS), search/save/delete, Entity-/EntityCollection- Objekte, Context |
| `sw-admin-directives` | Direktiven im Shopware-6-Admin: eingebaute Direktiven (v-tooltip, v-autofocus, v-droppable/v-draggable) nutzen, eigene Direktive via Shopware.Directive.register |
| `sw-admin-error-handling` | Fehlerbehandlung im Shopware-6-Admin: notification-Mixin (createNotificationError), API-Fehler aus Promise fangen, Error-Config/error codes, Validierungsfehler an Feldern |
| `sw-admin-menu` | Navigationseinträge im Shopware-6-Admin: navigation im Module.register (label/path/parent/position/icon), Settings-Item, Einträge unter bestehende Bereiche hängen |
| `sw-admin-mixins` | Mixins im Shopware-6-Admin: Shopware.Mixin.getByName nutzen (notification, listing, placeholder), eigenes Mixin registrieren |
| `sw-admin-module` | Ein eigenes Admin-Modul in Shopware 6 registrieren: Shopware.Module.register, routes, navigation, settingsItem, Verzeichnisstruktur module/<name>/ |
| `sw-admin-pinia-store` | State-Management im Shopware-6.7-Admin mit Pinia: Shopware.Store.register, state/getters/actions, Store nutzen, Migration von Vuex |
| `sw-admin-repository-js` | Das Admin-Repository (JS) in Shopware 6 im Detail: create/get/search/save/delete/clone/syncDeleted, Entity & EntityCollection erzeugen, Versionskontext, association lazy load |
| `sw-admin-routing` | Admin-Routing in Shopware 6: Routen im Module.register (routes), Parameter, meta.parentPath, $router/$route, bestehende Routen erweitern (routeMiddleware), Tab zu Modul hinzufügen |
| `sw-admin-sdk` | Grundlagen der Shopware-6.7-Administration (Vue 3): das globale Shopware-Objekt, Verzeichnis Resources/app/administration/src, main.js Einstieg, Vite-Build, Meteor-Komponenten (mt-*), Composition API |
| `sw-admin-services` | Eigene Services im Shopware-6-Admin registrieren und injizieren: Application.addServiceProvider, inject in Komponenten, vorhandene Services (repositoryFactory, systemConfigApiService, ...) |
| `sw-admin-snippets` | Admin-Übersetzungen (Snippets) in Shopware 6: snippet/<locale>.json + Shopware.Snippet, $tc/$t im Template, Platzhalter/Pluralisierung, Registrierung im Modul |
| `sw-admin-styles` | Styling im Shopware-6-Admin: SCSS in der Komponente (<name>.scss), BEM-Konvention, Meteor-Design-Tokens/Variablen, responsive |
| `sw-admin-typescript` | TypeScript in Shopware-6-Admin-Plugins: tsconfig einrichten, Vue-3-Komponenten/Services/Pinia-Stores typisieren, globale Shopware-Typen nutzen, eigene Types/Interfaces & .d.ts-Deklarationen, Entity-Typen, ts-Migration einzelner Dateien |
| `sw-admin-utils-filters` | Eingebaute Helfer im Shopware-6-Admin: Shopware.Utils (createId/get/object/array/string/debounce/format), Shopware.Filter (date, currency, fileSize, truncate, ...), Shopware.Classes, Shopware.Defaults |
| `sw-admin-vite` | Build des Shopware-6.7-Admin-Plugins mit Vite: Verzeichnis Resources/app/administration, main.js Entry, build/administration, Watcher, Migration von Webpack |
| `sw-admin-vuex-store` | Legacy-Vuex-Stores im Shopware-6-Admin: Shopware.State (deprecated), bestehende Core-Vuex-Stores lesen, Migration nach Pinia |
| `sw-meteor-admin-sdk` | Das @shopware-ag/meteor-admin-sdk: Shopware-Administration aus Apps/Plugins erweitern (ui.menu/module/actionButton/tabs/modal/sidebar/mainModule/settings/cms/mediaModal/componentSection, data repository, location, notification, toast, conte |
| `sw-meteor-components` | Die Meteor-Komponentenbibliothek im Shopware-6.7-Admin: mt-*-Komponenten (mt-card, mt-button, mt-text-field, mt-select, mt-banner, mt-modal, mt-tabs, mt-data-table ...), Props/Events, Verhältnis zu Legacy sw-* |
| `sw-meteor-composables` | Composables und Direktiven der Meteor Component Library: v-tooltip, v-draggable, v-droppable, v-sticky-column, useId, useEmptySlotCheck, useFutureFlags, useSnackbar, DeviceHelperPlugin |
| `sw-meteor-getting-started` | Installation und Setup der Meteor Component Library, des Token-Pakets und des Icon-Kits in eigenen Projekten |
| `sw-meteor-usage-guidelines` | Meteor Design System — Best Practices, Design-Prinzipien, Accessibility-Guidelines, Wording/Content, Komponent-Lifecycle (Future/Stable/Deprecated), Storybook-Docs-Standard, Do/Don't-Patterns |

## Agents (2)

| Agent | Beschreibung |
|---|---|
| `shopware-admin-mapper` | Introspektions-Agent: scannt ein Shopware-6-Projekt nach Admin-Bausteinen (Core-Administration + custom) und erzeugt einen gecachten Katalog (.shopware-catalog/admin.md) mit Modulen, Komponenten, Services, Mixins, Direktiven, Filtern und Ap |
| `shopware-admin` | Spezialist für die Shopware-6.7-Administration (Vue 3, Pinia, Vite, Meteor mt-*): Module, Komponenten (neu/override), Routing/Navigation/ACL, Datenhandling (repositoryFactory/Criteria), Services/ApiServices, Mixins/Direktiven, Snippets/Asse |

## Commands (3)

| Command | Beschreibung |
|---|---|
| `/sw-admin-component` | Scaffold einer Admin-Komponente in Shopware 6 (Vue 3) — index.js (Component.register), .html.twig (Meteor mt-*), optional .scss; oder ein Component.override |
| `/sw-admin-map` | Scannt das aktuelle Shopware-Projekt (Core-Administration + custom) und erzeugt/aktualisiert den Admin-Katalog .shopware-catalog/admin.md (Module, Komponenten, Services, Stores, Mixins, Direktiven, Filter, ApiServices) |
| `/sw-admin-module` | Scaffold eines Admin-Moduls in Shopware 6 (Vue 3) — module/<name>/index.js mit Module.register, List/Detail-Pages, Navigation, Snippets, ACL |
