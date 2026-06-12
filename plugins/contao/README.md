# contao

> Eine vollumfängliche Entwickler-Bibliothek für das Contao-5.x-CMS (Symfony-basiert).

`contao` ist die — vom Shopware-Teil unabhängige — **Entwickler-Bibliothek für Contao 5.x**, ein Symfony-basiertes Open-Source-CMS. Sie ist aus der offiziellen Entwickler-Dokumentation (`docs.contao.org/5.x/dev`) destilliert und deckt das Framework in voller Breite ab.

**Einstieg & Konzepte:** Core-Konzepte, Initial-Setup (Managed Edition / Symfony-Application), erste Schritte, Bundle-/Extension-Entwicklung, Manager-Plugin, Namespaces, Coding-Standards, Übersetzungen.

**Framework / Bausteine:** **DCA** (Data Container Array) als Herzstück der Backend-Datenpflege — vollständige Referenz zu `config`, `list`, `fields` (alle Feld-Typen + `eval` + `sql`), `palettes`/Subpalettes und allen **Callbacks**, plus `PaletteManipulator`. **Models/ORM** (Collections, Customization, Enumerations). **Content-Elemente** und **Front-/Backend-Module** im modernen **Fragment-Controller**-Stil (`#[AsContentElement]` / `#[AsFrontendModule]`), **Page-Controller**, **Routing** (inkl. Content-Routing), **Insert-Tags**, das moderne **Twig-Template-System** (Architektur, Erstellen, Debugging, Quick-Reference) sowie **Backend-Widgets**. Dazu die Infrastruktur: **Security** (Data-Container-Voter, Preview-Mode), **Filesystem** (Virtual Filesystem), **Image-Processing** (Picture-Factory, Image-Sizes, Image-Studio), **Caching/CSP**, **Cron**, **Async-Messaging & Jobs**, **Logging**, **Migrations**, **Request-Tokens**, **Response-Context**, **Search-Indexing**, **Maintenance** und **Profiler**.

**Referenzen (vollständig):** **alle ~69 Hooks** (Parameter/Rückgabe/Zeitpunkt + `#[AsHook]`-Nutzung), die komplette **Twig**-Erweiterung (Functions/Filters/Globals/Tags), alle **Backend-Widgets**, die **DCA**-Referenz sowie **Services/Events/Commands/Config/Request-Attributes**.

Der Spezialist **`contao-dev`** orchestriert alle Themen; die Scaffolder **`/contao-dca`**, **`/contao-content-element`**, **`/contao-module`** und **`/contao-hook`** erzeugen konventionskonforme Bausteine. **Wann nutzen:** für jede Entwicklung mit oder in Contao 5.x.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Wissen aus der offiziellen Contao-Doku destilliert und eingebettet; Skills laden Tiefe progressiv aus `references/`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install contao@claude-a-dev-team
```

## Skills (40)

`adt-contao-dal`, `contao-core-concepts`, `contao-asset-management`, `contao-backend-modules`, `contao-backend-routes`, `contao-caching`, `contao-coding-standards`, `contao-content-elements`, `contao-cron`, `contao-csp`, `contao-dca-framework`, `contao-dca-reference`, `contao-extension-bundle`, `contao-filesystem`, `contao-fragment-controllers`, `contao-frontend-modules`, `contao-getting-started`, `contao-hooks`, `contao-hooks-reference`, `contao-image-processing`, `contao-initial-setup`, `contao-insert-tags`, `contao-logging`, `contao-maintenance`, `contao-manager-plugin`, `contao-messaging-jobs`, `contao-migrations`, `contao-models`, `contao-page-controllers`, `contao-profiler`, `contao-reference-misc`, `contao-request-tokens`, `contao-response-context`, `contao-routing`, `contao-search-indexing`, `contao-security`, `contao-templates`, `contao-translations`, `contao-twig-reference`, `contao-widgets-reference`

## Agents (1)

- **`contao-dev`** — Orchestrator & Spezialist für die Entwicklung mit Contao 5.x (Symfony-basiertes CMS).

## Commands (4)

- **`/contao-content-element`** — Scaffold eines Contao-Content-Elements als Fragment-Controller (#[AsContentElement]) inkl.
- **`/contao-dca`** — Scaffold einer Contao-DCA-Konfiguration (Data Container Array) für eine Tabelle tl_* — config, list (sorting/label/operations), fields (mit eval + sql), palettes, optional callbacks + Model.
- **`/contao-hook`** — Scaffold eines Contao-Hook-Listeners (#[AsHook('hookName')]) mit korrekter Methoden-Signatur des gewählten Hooks.
- **`/contao-module`** — Scaffold eines Contao-Frontend-Moduls als Fragment-Controller (#[AsFrontendModule]) inkl.

## Hooks
- **PostToolUse** (Edit/Write): kontextsensitiver Reminder bei Contao-Dateien (DCA/Controller/Templates) — Coding-Standards/ECS, Cache/Migrations. Siehe `hooks/hooks.json`.
