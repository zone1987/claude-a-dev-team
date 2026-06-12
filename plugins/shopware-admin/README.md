# shopware-admin

**Wofür:** Administration (Vue 3 / Pinia / Vite / Meteor mt-*): Module, Komponenten, Routing, Datenhandling, Services, Mixins, ACL, Meteor-Admin-SDK, TypeScript — plus Admin-Bausteine-Introspektion (inkl. Slots/Props/Events).

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Wissen ist aus der Shopware-/OCTO-Quelle destilliert; Skills laden Tiefe progressiv aus `references/`.

## Installation (Claude Code)

```
/plugin marketplace add zone1987/claude-a-dev-team
/plugin install shopware-admin@claude-a-dev-team
```

## Skills (29)

`sw-admin-acl-permissions`, `sw-admin-api-requests`, `sw-admin-assets`, `sw-admin-catalog`, `sw-admin-component`, `sw-admin-component-override`, `sw-admin-data-grid`, `sw-admin-data-handling`, `sw-admin-directives`, `sw-admin-error-handling`, `sw-admin-menu`, `sw-admin-mixins`, `sw-admin-module`, `sw-admin-pinia-store`, `sw-admin-repository-js`, `sw-admin-routing`, `sw-admin-sdk`, `sw-admin-services`, `sw-admin-snippets`, `sw-admin-styles`, `sw-admin-typescript`, `sw-admin-utils-filters`, `sw-admin-vite`, `sw-admin-vuex-store`, `sw-meteor-admin-sdk`, `sw-meteor-components`, `sw-meteor-composables`, `sw-meteor-getting-started`, `sw-meteor-usage-guidelines`

## Agents (2)

- **`shopware-admin-mapper`** — Introspektions-Agent: scannt ein Shopware-6-Projekt nach Admin-Bausteinen (Core-Administration + custom) und erzeugt einen gecachten Katalog (.shopware-catalog/admin.md) mit Modulen, Komponenten, Serv
- **`shopware-admin`** — Spezialist für die Shopware-6.7-Administration (Vue 3, Pinia, Vite, Meteor mt-*): Module, Komponenten (neu/override), Routing/Navigation/ACL, Datenhandling (repositoryFactory/Criteria), Services/ApiSe

## Commands (3)

- **`/sw-admin-component`** — Scaffold einer Admin-Komponente in Shopware 6 (Vue 3) — index.js (Component.register), .html.twig (Meteor mt-*), optional .scss; oder ein Component.override.
- **`/sw-admin-map`** — Scannt das aktuelle Shopware-Projekt (Core-Administration + custom) und erzeugt/aktualisiert den Admin-Katalog .shopware-catalog/admin.md (Module, Komponenten, Services, Stores, Mixins, Direktiven, Fi
- **`/sw-admin-module`** — Scaffold eines Admin-Moduls in Shopware 6 (Vue 3) — module/<name>/index.js mit Module.register, List/Detail-Pages, Navigation, Snippets, ACL.
