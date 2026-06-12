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

| Skill | Beschreibung |
|---|---|
| `adt-contao-dal` | Contao DAL – Models, Collections, Enumerations, Custom Models, DCA-Grundlagen |
| `contao-core-concepts` | Contao 5 Kernkonzepte: DCA & Models, Front-End-Module, Content Elements, Templating, Assets & Images, Hooks, Extensions/Bundles, Insert Tags |
| `contao-asset-management` | Contao 5 Asset Management: TL_CSS/TL_JAVASCRIPT/TL_HEAD/TL_BODY globale Arrays, Pipe-Optionen (static/media/async/version), Template::generateStyleTag/generateScriptTag, Twig add-Tag, Symfony Asset Component, contao-components-Pakete |
| `contao-backend-modules` | Contao 5 Backend-Module: BE_MOD-Registrierung, tables/stylesheet/javascript/callback, Translations (modules.xlf), custom Actions, DCA-Integration, Backend-Routen-Verweis |
| `contao-backend-routes` | Contao 5 Backend-Routen: AbstractBackendController, Route-Attribut mit _scope=backend, Backend-Template (be_main), BackendMenuListener (BACKEND_MENU_BUILD-Event), Backend-Assets global und per DCA (TL_CSS/TL_JAVASCRIPT) |
| `contao-caching` | Contao 5 HTTP-Caching – Cache-Tags, Expiration, Validation, Invalidation, ESI, Fragment-Caching |
| `contao-coding-standards` | Contao 5 Coding Standards & Namenskonventionen: Symfony Coding Standards, FQCN-Servicenamen, contao/easy-coding-standard, empfohlene Namespace-Struktur (Controller/EventListener/Model/…), Klassen-Suffix-Konventionen, Publishing-Checkliste |
| `contao-content-elements` | Contao 5 Content Elements: AbstractContentElementController, AsContentElement-Attribut, DCA-Palette, Twig-Template, Nested Fragments, Wrapper-Elemente, Translations, PageModel |
| `contao-cron` | Contao 5 Cron-Framework – AsCronJob, Intervalle, Scope-aware, Async Cron Jobs, ProcessUtil |
| `contao-csp` | Contao 5.3 Content Security Policy – CspHandler, Nonces, Hashes, WysiwygStyleProcessor |
| `contao-dca-framework` | Contao 5 DCA aus Framework-Sicht: Callbacks registrieren, PaletteManipulator, Custom Drivers |
| `contao-dca-reference` | Contao 5.x Data Container Array (DCA) Vollreferenz: config-Keys, list/sorting/ label/operations/global_operations, fields (alle inputTypes, eval-Optionen, sql, relations, enums, virtual fields), palettes/subpalettes/__selector__, alle Callb |
| `contao-extension-bundle` | Contao 5 Extensions/Bundles erstellen und veröffentlichen: Bundle-Klasse, Manager Plugin, composer.json type=contao-bundle, service config, routing, Packagist-Publishing, Namespaces & Klassennamens-Konventionen, Coding Standards |
| `contao-filesystem` | Contao 5 Filesystem – VirtualFilesystem, MountManager, DBAFS, Flysystem-Konfiguration (experimentell) |
| `contao-fragment-controllers` | Contao 5 Fragment Controllers: Konzept (Subrequest/Partial), FE-Module & Content Elements als Fragments, Legacy-Klassen erweitern, custom Fragment Types, FragmentRegistry |
| `contao-frontend-modules` | Contao 5 Front-End-Module: AbstractFrontendModuleController, AsFrontendModule-Attribut, tl_module DCA-Palette, Twig-Template, Service-Tag-Optionen, PageModel-Zugriff |
| `contao-getting-started` | Contao 5 Getting Started: Übersicht, Verzeichnisstruktur, Konfigurationsdateien, Service-/Route-Setup, DCA-Basics, Hooks-Überblick, Translations im Einstieg |
| `contao-hooks` | Contao 5.x Hook-System: Was Hooks sind, wie man Listener registriert (#[AsHook] Attribut, Service-Tag contao.hook, Priorität, invokable Services, Legacy $GLOBALS['TL_HOOKS']) |
| `contao-hooks-reference` | Vollständige Referenz aller ~69 Contao-5.x-Hooks: Parameter (Typen), Rückgabewerte, Auslösezeitpunkt, Beispiele – gruppiert nach Domäne |
| `contao-image-processing` | Contao 5 Bildverarbeitung – ImageFactory, PictureFactory, Image Studio, Image Sizes (config.yaml) |
| `contao-initial-setup` | Contao 5 Initial Setup: Managed Edition vs. Symfony Application, composer create-project, contao-setup Script, Managed Edition Kernel, automatische Bundle-Konfiguration |
| `contao-insert-tags` | Contao 5 Insert Tags: AsInsertTag/AsBlockInsertTag-Attribute, InsertTagResult, OutputType, Flags (AsInsertTagFlag), Legacy-Hook, Caching-Verhalten, EBNF-Syntax |
| `contao-logging` | Contao 5 Logging – Monolog, ContaoContext, System-Log, Log-Channels, Autowiring |
| `contao-maintenance` | Contao 5 Maintenance-Module und Purge-Tasks – MaintenanceModuleInterface, TL_MAINTENANCE, TL_PURGE |
| `contao-manager-plugin` | Contao 5 Manager Plugin: BundlePluginInterface, ConfigPluginInterface, ExtensionPluginInterface, DependentPluginInterface, RoutingPluginInterface, HttpCacheSubscriberPluginInterface, Firewall/Monolog-Konfiguration, composer.json extra |
| `contao-messaging-jobs` | Contao 5 Async Messaging (Symfony Messenger) + Jobs-Framework (5.7) |
| `contao-migrations` | Contao 5 Datenmigrations-Framework – MigrationInterface, AbstractMigration, shouldRun, MigrationResult |
| `contao-models` | Contao 5 ORM – Models, Collections, Custom Models, Enumerations (ab 5.3) |
| `contao-page-controllers` | Contao 5 Page Controllers: AsPage-Attribut, type/path/urlSuffix/contentComposition, Seitenstruktur-Integration, URL-Generierung, UrlGeneratorInterface, PageModel |
| `contao-profiler` | Contao 5 Profiler – Symfony Web Developer Toolbar, Profiler-Erweiterungen, nur dev-Modus |
| `contao-reference-misc` | Contao 5.x Referenz — Services, Events, Commands, Config und Request-Attributes: alle Core-Services (ContaoFramework, Router, ScopeMatcher, Slug, InsertTagParser, ImageSizes, ContentUrlGenerator u.a.), alle Events (MenuEvent, SitemapEvent,  |
| `contao-request-tokens` | Contao 5 CSRF-Schutz / Request Tokens – Double Submit Cookie, CsrfTokenManager, Symfony-Forms |
| `contao-response-context` | Contao 5 Response Context – HtmlHeadBag, JsonLdManager, CSP, Fragment-Kommunikation mit Page-Controller |
| `contao-routing` | Contao 5 Routing: custom Routes, Request-Attribute (_scope/_token_check/_bypass_maintenance), Content Routing (ContentUrlGenerator, ContentUrlResolver), Legacy-URL-Parameter (auto_item) |
| `contao-search-indexing` | Contao 5 Suchindexierung – SearchIndexListener, IndexerInterface, contao:crawl, JSON-LD, noSearch |
| `contao-security` | Contao 5 Security – Symfony Voters, DCA-Permissions (CRUD), Preview Mode, Custom Backend Access |
| `contao-templates` | Contao 5 Twig-Template-System: Architektur (ContaoFilesystemLoader, @Contao-Namespace, Managed Namespace, Vererbungshierarchie), Templates erstellen (Extends/Include/Embed/ Macros/Components), Debugging (debug:contao-twig, dump), Legacy-PHP |
| `contao-translations` | Contao 5 Translations: TL_LANG-Array, Domains (default/tl_content/modules/…), PHP- und XLIFF-Format, Symfony-Integration ab 5.3 (contao_-Prefix, YAML), Translator-Service, Twig trans-Filter, Template-Zugriff |
| `contao-twig-reference` | Contao 5.x Twig-Erweiterungen Vollreferenz: alle Funktionen (figure, attrs, content_element, frontend_module, insert_tag, csp_hash, csp_nonce, csp_source, contao_section, contao_sections, content_url, picture_config, prefix_url, backend_ico |
| `contao-widgets-reference` | Contao 5.x Backend-Widget Vollreferenz: alle Form-Widgets (checkbox, checkboxWizard, fileTree, imageSize, inputUnit, listWizard, moduleWizard, optionWizard, password, picker, radio, select, serpPreview, tableWizard, textarea, text, timePeri |

## Skills — Benutzerhandbuch (17)

| Skill | Beschreibung |
|---|---|
| `contao-manual-overview` | Contao 5.x Handbuch — Einleitung: Was ist Contao, CMS-Grundbegriffe, Open-Source-Lizenz (LGPL), das Contao-Netzwerk (contao.org, GitHub, Community, Social Media) und Schnelldurchlauf (Backend/Frontend, Seitenstruktur, Layouts, Module, Theme |
| `contao-manual-articles-content` | Contao 5.x Handbuch — Artikelverwaltung & alle Inhaltselemente (Text, Media, Link, Datei, Include, Legacy, Akkordeon, Slider, Verschiedenes) |
| `contao-manual-backend` | Contao 5.x Handbuch — Administrationsbereich: Backend aufrufen und aufbauen (Infoleiste, Navigation, Arbeitsbereich, Vorschaubereich), alle Tastaturkürzel, Datensätze auflisten (Listen-, Eltern-, Baumansicht, Sortieren/Filtern/Suchen), Date |
| `contao-manual-cli` | Contao 5.x Handbuch — Kommandozeilenbefehle: contao:automator (Wartungsaufgaben), contao:backup:create/list/restore (Datenbank-Backups, Aufbewahrungsrichtlinien), contao:crawl (Suchindex, Broken-Link-Checker, Optionen), debug:dca, contao:ma |
| `contao-manual-core-extensions` | Contao 5.x Handbuch — Core-Erweiterungen: News/Blog, Kalender/Events, FAQ, Newsletter (je Verwaltung + Frontend-Module) sowie Kommentare und Auflistungs-Modul |
| `contao-manual-file-management` | Contao 5.x Handbuch — Dateiverwaltung: Dateien und Ordner verwalten (Upload, FTP-Sync, Drag & Drop, UUID-basiertes Dateisystem), Metadaten (Titel, Alt-Text, Caption, Lizenz, mehrsprachig), Downloads kontrollieren (öffentliche vs |
| `contao-manual-form-generator` | Contao 5.x Handbuch — Formulargenerator: Formulare konfigurieren, alle Formularfeld-Typen, E-Mail-/Datenbankversand, Suchformular erstellen |
| `contao-manual-insert-tags-tokens` | Contao 5.x Handbuch — Insert-Tags & Simple Tokens: vollständige Referenz aller Tags (Links, User, Page, Env, Include, Misc), Flags, verschachtelte Tags und Simple-Token-Syntax mit Bedingungslogik |
| `contao-manual-installation` | Contao 5.x Handbuch — Installation: Systemvoraussetzungen (PHP, MySQL, Webserver), Installation per Contao Manager oder Composer CLI, Contao aktualisieren (Major/Minor/Bugfix, LTS), Erweiterungen verwalten, lokale Entwicklungsumgebungen (DD |
| `contao-manual-layout` | Contao 5.x Handbuch — Layout: Theme-Manager (Themes, Stylesheets, Seitenlayouts), alle Frontend-Module (Navigation, Benutzer, Suche, Anwendungen, Verschiedenes) und Templates (PHP & Twig) |
| `contao-manual-migration` | Contao 5.x Handbuch — Update und Migration: Semantic Versioning (Major/Minor/Bugfix/LTS), Migration Contao 3.5 → 4.x (Schritt-für-Schritt), Migration Contao 4.13 → 5.x (composer.json, Ordnerstruktur public/, Interne Stylesheets exportieren, |
| `contao-manual-page-structure` | Contao 5.x Handbuch — Seitenstruktur: Seiten als zentrale Elemente, alle Seitentypen (Reguläre Seite, Weiterleitung, 401/403/404/503-Fehlerseiten, News-Feed etc.), Multidomain-Betrieb, mehrsprachige Webseiten (URL-Präfix, Sprachfallback, Ro |
| `contao-manual-performance` | Contao 5.x Handbuch — Performance: HTTP-Caching (Cache-Control, Shared Cache, X-Cache-Tags, Invalidierung, Cookie/Query-Parameter-Allowlist), PHP-Setup (SAPI, OPcache, Realpath Cache, php.ini-Empfehlungen), Cronjob-Framework (contao:cron, W |
| `contao-manual-system` | Contao 5.x Handbuch — System: Einstellungen (Backend, Datum/Zeit, Sicherheit, Uploads, Zugriffsrechte, parameters.yaml, config.yaml, Umgebungsvariablen, E-Mail-Versand/SMTP), Systemwartung (Wartungsmodus, Crawler/Suchindex, Daten bereinigen |
| `contao-manual-third-party-extensions` | Contao 5.x Handbuch — Drittanbieter-Erweiterungen: Animated Timeline, EasyThemes, Isotope eCommerce, Maklermodul, Merger², MetaModels, News Facebook Sync und weitere |
| `contao-manual-tutorials` | Contao 5.x Handbuch — Anleitungen: Erste Startseite, Contao Demo, DCA-Anpassungen, Sass/Less, TinyMCE-Konfiguration, Grid-System, SVG, Formulardaten speichern, Wartungstemplate, Testversionen, lokale Installation (DDEV, Devilbox, Laragon) |
| `contao-manual-user-management` | Contao 5.x Handbuch — Benutzerverwaltung: Backend-Benutzer (Gruppen, Rechtevererbung, Pagemounts, Filemounts, erlaubte Module/Elemente/Felder, Zwei-Faktor-Authentifizierung, Benutzerkonten) und Frontend-Mitglieder (Mitgliedergruppen, Person |

## Agents (2)

| Agent | Beschreibung |
|---|---|
| `contao-dev` | Orchestrator & Spezialist für die Entwicklung mit Contao 5.x (Symfony-basiertes CMS) |
| `contao-manual-guide` | Berater für Contao-5.x-Anwender/Redakteure/Administratoren (Bedienung, NICHT Entwicklung): beantwortet „wie mache ich X im Contao-Backend" anhand des destillierten Benutzerhandbuchs — Installation, Administrationsbereich, Seitenstruktur, Ar |

## Commands (4)

| Command | Beschreibung |
|---|---|
| `/contao-content-element` | Scaffold eines Contao-Content-Elements als Fragment-Controller (#[AsContentElement]) inkl |
| `/contao-dca` | Scaffold einer Contao-DCA-Konfiguration (Data Container Array) für eine Tabelle tl_* — config, list (sorting/label/operations), fields (mit eval + sql), palettes, optional callbacks + Model |
| `/contao-hook` | Scaffold eines Contao-Hook-Listeners (#[AsHook('hookName')]) mit korrekter Methoden-Signatur des gewählten Hooks |
| `/contao-module` | Scaffold eines Contao-Frontend-Moduls als Fragment-Controller (#[AsFrontendModule]) inkl |

## Hooks (1)

| Hook | Beschreibung |
|---|---|
| `PostToolUse` | Edit/Write/MultiEdit — kontextsensitive Lint-/Katalog-Reminder bei passenden Dateien; nicht-blockierend (`hooks/hooks.json`) |
