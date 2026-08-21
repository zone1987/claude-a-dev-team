# Shopware 6 — complete architecture documentation

Sources: `concepts/framework/architecture/index.md`, `administration-concept.md`, `storefront-concept.md`

---

## Contents

- [Overview (concepts/framework/architecture/index.md)](#overview-conceptsframeworkarchitectureindexmd)
- [Administration (concepts/framework/architecture/administration-concept.md)](#administration-conceptsframeworkarchitectureadministration-conceptmd)
- [Storefront (concepts/framework/architecture/storefront-concept.md)](#storefront-conceptsframeworkarchitecturestorefront-conceptmd)

## Overview (concepts/framework/architecture/index.md)

Shopware follows a modular, API-first architecture built on Symfony and modern frontend technologies.
Three primary domains that can be developed further independently of each other:

- **Core** — backend foundation: business logic, DAL, APIs, extension mechanism
- **Storefront** — customer-facing presentation layer: sales channels, Store API
- **Administration** — management interface for merchants and operators

Unified by a common API layer and a consistent plugin system.

### Architecture principles

- **API-first** — all functionality reachable via APIs (headless and composable commerce)
- **Separation of concerns** — frontend (storefront/admin) decoupled from backend logic
- **Extensibility** — plugins via events, services and extension points (no core modification)
- **Asynchronous processing** — background tasks via message queues and workers
- **Domain-driven structure** — business logic organised by commerce domains

### Core components

- Data Abstraction Layer (DAL) for database interaction
- Business services and domain logic
- Sales channel and store APIs
- Plugin and event system
- Messaging and scheduled task infrastructure

---

## Administration (concepts/framework/architecture/administration-concept.md)

### Introduction

- Symfony bundle with a single page application (SPA) in JavaScript (Vue.js)
- Conceptually sits on top of the core — similar to the storefront
- Communicates with the core exclusively via the Admin API (REST-based)
- Headless application made of custom Vue.js components
- SASS for styling, Twig.js for templates, Vue I18n for translations, Webpack for bundling

### Main responsibilities

- UI for all administrative tasks of the shop operator
- **No business logic** — flat module list, mirrors the core modules
- Inheritance: plugins can override or extend components
- Data management: manage core entities, REST API communication
- State management: router, local component states

### Structure

```
shopware/src/Administration/Resources/app/administration/src/
├── app/     — framework-dependent base functionality
├── core/    — Admin API binding and services
└── module/  — UI + state management per topic (mirrors the core modules)
```

### Modules and components

- **Module** = navigation entry; contains pages, views, components
- **Page** = entry point, renders a complete page; contains views
- **View** = subordinate part of a page; contains components
- **Component** = styling + markup + logic (MVC collapsed into one)

Order module example (`sw-order`):
```
module/sw-order/
├── acl/        — ACL mapping (viewer, editor, creator, deleter)
├── component/  — sub-components
├── page/       — sw-order-create, sw-order-detail, sw-order-list
├── snippet/    — translation files
├── state/      — Pinia state
└── view/       — views
```

### Inheritance (extensibility)

- `Component.extend()` — create a new component
- `Component.override()` — override existing behaviour
- Adjust Twig.js templates
- Extend methods and computed properties

### ACL in the administration

- CRUD permissions per module (`create`, `read`, `update`, `delete`)
- Default roles: `viewer`, `editor`, `creator`, `deleter`
- Custom roles via the admin UI or plugin development
- Granular rights per module

---

## Storefront (concepts/framework/architecture/storefront-concept.md)

### Introduction

- PHP frontend; conceptually sits on top of the core
- Twig as template engine, SASS for styles, Bootstrap as CSS framework
- Webpack for bundling and transpiling
- Uses Store API routes internally to fetch data

### Main responsibilities

1. **Create pages and pagelets** — composite data loading
2. **Map requests onto the core** — via Store API routes
3. **Render templates** — Twig-based, fully customisable
4. **Theming** — theme engine for layout adjustments

### The Store API in the storefront context

In the traditional Twig storefront the browser does **not** call the Store API directly.
Instead, storefront controllers use the Store API internally to fetch data.
The storefront uses session-based auth; the Store API itself is stateless with header auth.

### Pages and pagelets

- **Page** — complete page; 3-class namespace:
  - **Page struct** — represents the data
  - **PageLoader** — creates page structs
  - **PageEvent** — clean extension point
- **Pagelet** — part of a page or reachable via an XHR route; structured like a page

### Composite data handling

`AccountOrderPage` example:

1. Controller receives the request, asks the PageLoader for the page
2. `AccountOrderPageLoader` calls `GenericPageLoader` (header, footer)
3. Load additional data via a Store API route (`OrderRoute`)
4. Dispatch `AccountOrderPageLoadedEvent` (plugin extension point)
5. Render the page struct with the template

### Structure

```
Storefront/
├── Controller/         — routing + handing the page struct to Twig
├── Page/               — page structs + PageLoader
├── Pagelet/            — pagelet structs + loader
├── Resources/          — templates, snippets, assets (Bootstrap structure)
├── Theme/              — theme engine
└── ...
```

### Translations in the storefront

- JSON files in `Resources/snippet/<locale>/` (e.g. `de_DE`)
- Twig: `{{ "general.homeLink"|trans }}`
- Pluralisation and variables via the `%` wrapper
