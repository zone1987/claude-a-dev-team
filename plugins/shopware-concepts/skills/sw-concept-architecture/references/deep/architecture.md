# Shopware 6 — Vollständige Architektur-Doku

Quellen: `concepts/framework/architecture/index.md`, `administration-concept.md`, `storefront-concept.md`

---

## Überblick (concepts/framework/architecture/index.md)

Shopware folgt einer modularen, API-first-Architektur auf Basis von Symfony und modernen Frontend-Technologien.
Drei primäre Domänen, die unabhängig voneinander weiterentwickelt werden können:

- **Core** — Backend-Fundament: Business-Logik, DAL, APIs, Extension-Mechanismus
- **Storefront** — kundenseitiger Präsentationslayer: Sales Channels, Store API
- **Administration** — Management-Interface für Händler und Operatoren

Vereint durch gemeinsame API-Schicht und konsistentes Plugin-System.

### Architekturprinzipien

- **API-first** — alle Funktionalität über APIs erreichbar (headless und composable commerce)
- **Separation of Concerns** — Frontend (Storefront/Admin) von Backend-Logik entkoppelt
- **Erweiterbarkeit** — Plugins via Events, Services und Extension Points (keine Core-Modifikation)
- **Asynchrone Verarbeitung** — Background Tasks via Message Queues und Workers
- **Domain-driven Structure** — Business-Logik nach Commerce-Domänen organisiert

### Core-Komponenten

- Data Abstraction Layer (DAL) für Datenbankinteraktion
- Business Services und Domain-Logik
- Sales Channel und Store APIs
- Plugin- und Event-System
- Messaging und Scheduled Task Infrastructure

---

## Administration (concepts/framework/architecture/administration-concept.md)

### Einführung

- Symfony Bundle mit Single Page Application (SPA) in JavaScript (Vue.js)
- Sitzt konzeptionell auf dem Core — ähnlich wie Storefront
- Kommuniziert mit Core ausschließlich via Admin API (REST-basiert)
- Headless-Applikation aus custom Vue.js-Komponenten
- SASS für Styling, Twig.js für Templates, Vue I18n für Übersetzungen, Webpack für Bundling

### Hauptaufgaben

- UI für alle administrativen Aufgaben des Shop-Betreibers
- **Keine Business-Logik** — flache Modul-Liste, spiegelt Core-Module
- Inheritance: Plugins können Komponenten überschreiben oder erweitern
- Data Management: Entitäten des Core verwalten, REST-API-Kommunikation
- State Management: Router, lokale Komponenten-States

### Struktur

```
shopware/src/Administration/Resources/app/administration/src/
├── app/     — Framework-abhängige Grundfunktionalität
├── core/    — Admin API-Bindung und Services
└── module/  — UI + State Management pro Thema (spiegelt Core-Module)
```

### Module und Komponenten

- **Modul** = Navigations-Eintrag; enthält Pages, Views, Components
- **Page** = Einstiegspunkt, rendert vollständige Seite; enthält Views
- **View** = Untergeordneter Teil einer Page; enthält Components
- **Component** = Styling + Markup + Logik (MVC collapsed into one)

Beispiel Order-Modul (`sw-order`):
```
module/sw-order/
├── acl/        — ACL-Mapping (viewer, editor, creator, deleter)
├── component/  — Teilkomponenten
├── page/       — sw-order-create, sw-order-detail, sw-order-list
├── snippet/    — Übersetzungsdateien
├── state/      — Pinia-State
└── view/       — Views
```

### Inheritance (Erweiterbarkeit)

- `Component.extend()` — neue Komponente erstellen
- `Component.override()` — bestehendes Verhalten überschreiben
- Twig.js-Templates anpassen
- Methoden und Computed Properties erweitern

### ACL in der Administration

- CRUD-Berechtigungen pro Modul (`create`, `read`, `update`, `delete`)
- Default-Rollen: `viewer`, `editor`, `creator`, `deleter`
- Custom Roles via Admin-UI oder Plugin-Entwicklung
- Granulare Rechte pro Modul

---

## Storefront (concepts/framework/architecture/storefront-concept.md)

### Einführung

- PHP-Frontend; sitzt konzeptionell auf dem Core
- Twig als Template-Engine, SASS für Styles, Bootstrap als CSS-Framework
- Webpack für Bundling und Transpiling
- Nutzt intern Store API-Routen für Datenbeschaffung

### Hauptaufgaben

1. **Pages und Pagelets erstellen** — Composite Data Loading
2. **Requests auf den Core mappen** — via Store API-Routen
3. **Templates rendern** — Twig-basiert, vollständig anpassbar
4. **Theming** — Theme-Engine für Layout-Anpassungen

### Store API im Kontext Storefront

In der traditionellen Twig-Storefront ruft der Browser **nicht direkt** die Store API auf.
Stattdessen nutzen Storefront-Controller die Store API intern zur Datenbeschaffung.
Storefront nutzt Session-basierte Auth; Store API selbst ist zustandslos mit Header-Auth.

### Pages und Pagelets

- **Page** — vollständige Seite; 3-Klassen-Namespace:
  - **Page-Struct** — repräsentiert die Daten
  - **PageLoader** — erstellt Page-Structs
  - **PageEvent** — sauberer Erweiterungspunkt
- **Pagelet** — Teil einer Page oder via XHR-Route erreichbar; wie Page strukturiert

### Composite Data Handling

Beispiel `AccountOrderPage`:

1. Controller empfängt Request, fordert Page vom PageLoader an
2. `AccountOrderPageLoader` ruft `GenericPageLoader` auf (Header, Footer)
3. Zusätzliche Daten via Store API-Route (`OrderRoute`) laden
4. `AccountOrderPageLoadedEvent` dispatchen (Plugin-Erweiterungspunkt)
5. Page-Struct mit Template rendern

### Struktur

```
Storefront/
├── Controller/         — Routing + Page-Struct-Übergabe an Twig
├── Page/               — Page-Structs + PageLoader
├── Pagelet/            — Pagelet-Structs + Loader
├── Resources/          — Templates, Snippets, Assets (Bootstrap-Struktur)
├── Theme/              — Theme-Engine
└── ...
```

### Übersetzungen in der Storefront

- JSON-Dateien in `Resources/snippet/<locale>/` (z.B. `de_DE`)
- Twig: `{{ "general.homeLink"|trans }}`
- Pluralisierung und Variablen via `%`-Wrapper
