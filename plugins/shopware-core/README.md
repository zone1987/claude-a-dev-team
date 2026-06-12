# shopware-core

> Das Fundament jeder Shopware-6-Plugin-Entwicklung.

`shopware-core` ist der **Einstiegspunkt** für jede Arbeit mit Shopware 6.7 und bündelt die Bausteine, die in
praktisch jedem Plugin gebraucht werden. Es beginnt bei der **Architektur-Orientierung** (Shopware ist *nicht*
Standard-Symfony/Doctrine: eigene DAL statt ORM, `Criteria` statt QueryBuilder, **Events vor Decorators**,
drei APIs) und reicht über das **Plugin-Fundament** (Bootstrap-Klasse, `composer.json`, PSR-4, die
A-Dev-Team-Owner-Konventionen `Ff`/`Adt`/`Ag`/`Pb`) bis zu allen Querschnitts-Themen.

Abgedeckt sind: **Dependency Injection** (`services.xml`, Autowiring, Argument-Binding), **Service-Decoration**
(wann statt Event) und **Service-Tags**, das **Event-/Subscriber-System** und **Extension Points**, eigene
**CLI-Commands**, **Logging** (eigener Monolog-Channel / `PluginLoggerTrait`), **Filesystem** (Flysystem),
**Rate-Limiter**, **Feature-Flags**, **NumberRange** und der **SystemConfigService**. Der **Event-Katalog**
(`sw-event-catalog` + `/sw-event-map`) erstellt zusätzlich eine Introspektion aller im Projekt vorhandenen Events
inkl. Argumente — die Grundlage für jeden Subscriber.

Hier wohnt auch der **Orchestrator `shopware-dev`** — der Standard-Einstieg, der eine Aufgabe der richtigen Domäne
zuordnet und an die Spezialisten der anderen Plugins delegiert. Für reines Backend unterhalb der DAL springt
`shopware-backend` ein. **Wann nutzen:** immer — als Basis. Datenmodelle → `shopware-data`, Framework-Features
(Queue/Flow/Rules/Mail/Media) → `shopware-framework`.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Das Wissen ist aus den offiziellen Quellen destilliert und eingebettet; Skills laden ihre Tiefe progressiv aus `references/`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-core@claude-a-dev-team
```

## Skills (18)

`sw-architecture-overview`, `sw-cli-command`, `sw-config-reference`, `sw-dependency-injection`, `sw-event-catalog`, `sw-events-subscriber`, `sw-extension-points`, `sw-feature-flags`, `sw-filesystem`, `sw-logging`, `sw-number-range`, `sw-plugin-base`, `sw-plugin-config`, `sw-plugin-lifecycle`, `sw-rate-limiter`, `sw-service-decoration`, `sw-service-tags`, `sw-system-config`

## Agents (3)

- **`shopware-backend`** — Spezialist für Shopware-6.7 Backend-Fundamentals: Plugin-Basis/Lifecycle, Dependency Injection & services.xml, Service-Decoration & Tags, Event-Subscriber, CLI-Commands, Logging, Filesystem, Rate-Limiter, Feature-Flags, 
- **`shopware-dev`** — Orchestrator und Standard-Einstieg für ALLE Shopware-6.7-Entwicklungsaufgaben.
- **`shopware-event-mapper`** — Introspektions-Agent: scannt ein Shopware-6-Projekt (Core-Vendor + custom/plugins) nach Events und erzeugt einen gecachten Katalog (.shopware-catalog/events.md) mit Event-Name/Konstante, Event-Klasse, Dispatch-Ort und Ar

## Commands (4)

- **`/sw-command-create`** — Scaffold eines CLI-Commands (bin/console) in einem Shopware-6-Plugin inkl.
- **`/sw-config-create`** — Scaffold/Erweiterung der Plugin-Konfiguration (config.xml) eines Shopware-6-Plugins mit Cards und Input-Feldern.
- **`/sw-event-map`** — Scannt das aktuelle Shopware-Projekt (Core + custom) und erzeugt/aktualisiert den Event-Katalog .shopware-catalog/events.md (Event-Name/Konstante, Event-Klasse, Dispatch-Ort, Argumente/Payload) als Grundlage für Subscrib
- **`/sw-plugin-create`** — Scaffold eines neuen Shopware-6-Plugins mit korrekten Owner-/Namens-/Namespace-Konventionen, composer.json, Plugin-Klasse und Grundstruktur.
