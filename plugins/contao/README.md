# contao

> A comprehensive library for the Contao 5.x CMS : development AND operation (end-user manual).

`contao` is the library for **Contao 5.x** (Symfony-based CMS), independent of the Shopware part, and covers **two perspectives**: the **developer documentation** (`docs.contao.org/5.x/dev`) and the **end-user manual** (`docs.contao.org/5.x/manual/de`, German).

**Development (`contao-backend`, `contao-core`, `contao-data`, `contao-frontend`, `contao-platform`):** **DCA** (Data Container Array : config/list/fields/palettes/callbacks, PaletteManipulator), **Models/ORM**, **content elements** and **frontend/backend modules** as fragment controllers, **page controllers**, **routing**, **Twig templates**, **insert tags**, **backend widgets**, **all ~69 hooks**, **security/filesystem/image processing**, **caching/CSP/cron/messaging/logging/migrations/search indexing**, **bundle/extension** development and the **Manager plugin** : plus complete references (DCA, hooks, Twig, widgets, services/events/commands).

**Operation (`contao-manual-*`, German end-user manual):** the complete editor/admin manual : installation, **administration area**, **page structure**, **articles and content elements**, **layout/themes/modules**, **file and user management**, **form generator**, the **core extensions** (news/calendar/FAQ/comments/newsletter), third-party extensions, **CLI**, system/performance, migration and numerous how-tos : including screenshots.

Two agents: **`contao-dev`** (development, orchestrates all topics) and **`contao-manual-guide`** (operation/editorial advisor). Scaffolders: **`/contao-dca`**, **`/contao-content-element`**, **`/contao-module`**, **`/contao-hook`**; plus a **PostToolUse hook** (coding standards/cache reminders). **When to use:** for any work with or in Contao 5.x.

Part of the marketplace **[claude-a-dev-team](../../README.md)**. The knowledge is distilled from the official Contao documentation and embedded; each skill keeps its depth in flat SCREAMING-CASE.md reference files next to its `SKILL.md`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install contao@claude-a-dev-team
```

## Skills : Development (5)

| Skill | Description |
|---|---|
| `contao-backend` | Contao 5 backend: backend modules, backend routes, page controllers, routing, request tokens, response context. Use when building a Contao backend module or route |
| `contao-core` | Contao 5 fundamentals: bundle structure, Manager plugin, setup, coding standards, logging, profiler. Use when the request names Contao setup, a Contao bundle or the Manager plugin |
| `contao-data` | Contao 5 data layer: DCA definition and reference, Models, Collections, migrations, search indexing. Use when the request names a Contao DCA, tl_ table, Contao Model or migration |
| `contao-frontend` | Contao 5 frontend: content elements, frontend modules, fragment controllers, Twig templates, insert tags, widgets. Use when building a Contao content element or frontend module |
| `contao-platform` | Contao 5 platform services: hooks and the hook reference, security, CSP, filesystem, caching, cron, translations. Use when the request names a Contao hook or Contao caching |

## Skills : German end-user manual (3)

| Skill | Description |
|---|---|
| `contao-manual-basics` | Contao 5 user manual: installation, the backend interface, system settings, user and permission management, CLI. Use when asked how to operate or administer Contao |
| `contao-manual-content` | Contao 5 user manual: page structure, articles and content elements, layout and themes, file management. Use when asked how to build pages or content in the Contao backend |
| `contao-manual-features` | Contao 5 user manual: form generator, core extensions such as news and calendar, third-party extensions. Use when asked about a Contao form or a Contao extension in the backend |

## Agents (2)

| Agent | Description |
|---|---|
| `contao-dev` | Orchestrator and specialist for development with Contao 5.x (Symfony-based CMS) |
| `contao-manual-guide` | Advisor for Contao 5.x users/editors/administrators (operation, NOT development): answers "how do I do X in the Contao backend" based on the distilled German end-user manual : installation, administration area, page structure, articles and more |

## Commands (4)

| Command | Description |
|---|---|
| `/contao-content-element` | Scaffolds a Contao content element as a fragment controller (#[AsContentElement]), including the related files |
| `/contao-dca` | Scaffolds a Contao DCA configuration (Data Container Array) for a tl_* table : config, list (sorting/label/operations), fields (with eval + sql), palettes, optional callbacks + Model |
| `/contao-hook` | Scaffolds a Contao hook listener (#[AsHook('hookName')]) with the correct method signature of the chosen hook |
| `/contao-module` | Scaffolds a Contao frontend module as a fragment controller (#[AsFrontendModule]), including the related files |

## Hooks (1)

| Hook | Description |
|---|---|
| `PostToolUse` | Edit/Write/MultiEdit : context-sensitive lint/catalog reminders on matching files; non-blocking (`hooks/hooks.json`) |
