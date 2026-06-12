# contao

> Eine vollumfängliche Bibliothek für das Contao-5.x-CMS — Entwicklung UND Bedienung (Benutzerhandbuch).

`contao` ist die — vom Shopware-Teil unabhängige — Bibliothek für **Contao 5.x** (Symfony-basiertes CMS) und deckt **zwei Perspektiven** ab: die **Entwickler-Doku** (`docs.contao.org/5.x/dev`) und das **Benutzerhandbuch** (`docs.contao.org/5.x/manual/de`).

**Entwicklung (`contao-*`):** **DCA** (Data Container Array — config/list/fields/palettes/callbacks, PaletteManipulator), **Models/ORM**, **Content-Elemente** & **Front-/Backend-Module** als Fragment-Controller, **Page-Controller**, **Routing**, **Twig-Templates**, **Insert-Tags**, **Backend-Widgets**, **alle ~69 Hooks**, **Security/Filesystem/Image-Processing**, **Caching/CSP/Cron/Messaging/Logging/Migrations/Search-Indexing**, **Bundle-/Extension**-Entwicklung & **Manager-Plugin** — plus vollständige Referenzen (DCA, Hooks, Twig, Widgets, Services/Events/Commands).

**Bedienung (`contao-manual-*`):** das komplette Redakteurs-/Admin-Handbuch — Installation, **Administrationsbereich**, **Seitenstruktur**, **Artikel & Inhaltselemente**, **Layout/Themes/Module**, **Datei-/Benutzerverwaltung**, **Formulargenerator**, die **Core-Erweiterungen** (News/Kalender/FAQ/Kommentare/Newsletter), Drittanbieter-Erweiterungen, **CLI**, System/Performance, Migration und zahlreiche Anleitungen — inkl. Screenshots.

Zwei Agents: **`contao-dev`** (Entwicklung, orchestriert alle Themen) und **`contao-manual-guide`** (Bedien-/Redaktions-Berater). Scaffolder: **`/contao-dca`**, **`/contao-content-element`**, **`/contao-module`**, **`/contao-hook`**; dazu ein **PostToolUse-Hook** (Coding-Standards/Cache-Reminder). **Wann nutzen:** für jede Arbeit mit oder in Contao 5.x.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Wissen aus der offiziellen Contao-Doku destilliert und eingebettet; Skills laden Tiefe progressiv aus `references/`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install contao@claude-a-dev-team
```

## Skills — Entwicklung (40)

`adt-contao-dal`, `contao-core-concepts`, `contao-asset-management`, `contao-backend-modules`, `contao-backend-routes`, `contao-caching`, `contao-coding-standards`, `contao-content-elements`, `contao-cron`, `contao-csp`, `contao-dca-framework`, `contao-dca-reference`, `contao-extension-bundle`, `contao-filesystem`, `contao-fragment-controllers`, `contao-frontend-modules`, `contao-getting-started`, `contao-hooks`, `contao-hooks-reference`, `contao-image-processing`, `contao-initial-setup`, `contao-insert-tags`, `contao-logging`, `contao-maintenance`, `contao-manager-plugin`, `contao-messaging-jobs`, `contao-migrations`, `contao-models`, `contao-page-controllers`, `contao-profiler`, `contao-reference-misc`, `contao-request-tokens`, `contao-response-context`, `contao-routing`, `contao-search-indexing`, `contao-security`, `contao-templates`, `contao-translations`, `contao-twig-reference`, `contao-widgets-reference`

## Skills — Benutzerhandbuch (17)

`contao-manual-overview`, `contao-manual-articles-content`, `contao-manual-backend`, `contao-manual-cli`, `contao-manual-core-extensions`, `contao-manual-file-management`, `contao-manual-form-generator`, `contao-manual-insert-tags-tokens`, `contao-manual-installation`, `contao-manual-layout`, `contao-manual-migration`, `contao-manual-page-structure`, `contao-manual-performance`, `contao-manual-system`, `contao-manual-third-party-extensions`, `contao-manual-tutorials`, `contao-manual-user-management`

## Agents (2)

- **`contao-dev`** — Orchestrator & Spezialist für die Entwicklung mit Contao 5.x (Symfony-basiertes CMS).
- **`contao-manual-guide`** — Berater für Contao-5.x-Anwender/Redakteure/Administratoren (Bedienung, NICHT Entwicklung): beantwortet „wie mache ich X im Contao-Backend" anhand des destillierten Benutzerhandbuchs — Installation, Administrationsbereich

## Commands (4)

- **`/contao-content-element`** — Scaffold eines Contao-Content-Elements als Fragment-Controller (#[AsContentElement]) inkl.
- **`/contao-dca`** — Scaffold einer Contao-DCA-Konfiguration (Data Container Array) für eine Tabelle tl_* — config, list (sorting/label/operations), fields (mit eval + sql), palettes, optional callbacks + Model.
- **`/contao-hook`** — Scaffold eines Contao-Hook-Listeners (#[AsHook('hookName')]) mit korrekter Methoden-Signatur des gewählten Hooks.
- **`/contao-module`** — Scaffold eines Contao-Frontend-Moduls als Fragment-Controller (#[AsFrontendModule]) inkl.

## Hooks
- **PostToolUse** (Edit/Write): Coding-Standards/Cache-Reminder bei Contao-Dateien. Siehe `hooks/hooks.json`.
