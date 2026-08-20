# shopware-admin

> The administration as a Vue 3 app (Pinia/Vite/Meteor).

`shopware-admin` deals with the **administration** — a standalone **Vue 3 single-page app** with **Pinia**
(state), **Vite** (build) and the **Meteor component library** (`mt-*`), extended through the global
`Shopware` object.

Covered: custom **modules** (`Module.register`), **components** (registering new ones *and* extending existing ones
via `Component.override`), **routing**/navigation/menu, **data handling** through `repositoryFactory` + the JS
`Criteria`, **Pinia** (and legacy Vuex) stores, custom **services/ApiServices**, **mixins**, **directives**,
**snippets**, **assets/styles**, **ACL/permissions**, **error handling**, **data grids**, the
**Meteor components** (`mt-*`) including the built-in **utils/filters**, the **Vite** build and the
**Meteor Admin SDK** (extending the admin from an app/plugin via postMessage, locations, data selectors) as well as
**TypeScript**.

The **admin introspection** (`/sw-admin-map`, `sw-data`) catalogues all modules, components (including
**slots/props/events**), services, stores, mixins, directives and filters of the project at hand. Specialist:
**`shopware-admin`**; scaffolders **`/sw-admin-module`**, **`/sw-admin-component`**. **When to use:** for backend/
administration interfaces. Operator knowledge (not code) lives in `shopware-merchant`.

Part of the **[claude-a-dev-team](../../README.md)** marketplace. The knowledge is distilled from the official sources and embedded; each skill's depth sits in flat SCREAMING-CASE.md reference files next to its SKILL.md and is loaded progressively.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-admin@claude-a-dev-team
```

## Skills (4)

| Skill | Description |
|---|---|
| `sw-build` | Shopware admin build: Vite configuration, TypeScript, SCSS and styles, static assets, snippets and translations. Use when configuring the Shopware administration build or its assets. |
| `sw-components` | Shopware admin components: creating and overriding components, modules, menu entries, routing, data grids, directives, mixins, filters. Use when building a Shopware administration module or component. |
| `sw-data` | Shopware admin data: `repositoryFactory` and `Criteria` in JS, API requests, Pinia and Vuex stores, services, error handling, ACL. Use when loading or saving data in the Shopware administration. |
| `sw-meteor` | Shopware Meteor: getting started, `mt-*` components, composables, usage guidelines, the Meteor Admin SDK for apps. Use when the request names Meteor, an `mt-*` component or the Admin SDK. |

## Agents (2)

| Agent | Description |
|---|---|
| `shopware-admin-mapper` | Introspection agent: scans a Shopware 6 project for admin building blocks (core administration + custom) and produces a cached catalogue (`.shopware-catalog/admin.md`) listing modules, components, services, mixins, directives, filters and Ap… |
| `shopware-admin` | Specialist for the Shopware 6.7 administration (Vue 3, Pinia, Vite, Meteor `mt-*`): modules, components (new/override), routing/navigation/ACL, data handling (`repositoryFactory`/`Criteria`), services/ApiServices, mixins/directives, snippets/asse… |

## Commands (3)

| Command | Description |
|---|---|
| `/sw-admin-component` | Scaffolds a Shopware 6 admin component (Vue 3) — `index.js` (`Component.register`), `.html.twig` (Meteor `mt-*`), optionally `.scss`; or a `Component.override` |
| `/sw-admin-map` | Scans the current Shopware project (core administration + custom) and creates/updates the admin catalogue `.shopware-catalog/admin.md` (modules, components, services, stores, mixins, directives, filters, ApiServices) |
| `/sw-admin-module` | Scaffolds a Shopware 6 admin module (Vue 3) — `module/<name>/index.js` with `Module.register`, list/detail pages, navigation, snippets, ACL |
