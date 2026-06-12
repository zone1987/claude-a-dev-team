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

| Skill | Beschreibung |
|---|---|
| `sw-architecture-overview` | Shopware 6 Grundarchitektur & Orientierung — wann ist Shopware NICHT Standard-Symfony/Doctrine |
| `sw-cli-command` | Eigene CLI-Commands (bin/console) in einem Shopware-6-Plugin: Symfony-Command registrieren, Argumente/Optionen, SymfonyStyle-Output, Naming-Konvention |
| `sw-config-reference` | Shopware 6 Webserver-Konfiguration — vollständige Referenz-Configs für Nginx, Apache und Caddy |
| `sw-dependency-injection` | Dependency Injection in Shopware-6-Plugins: services.xml registrieren, Autowiring, Argument-Binding, Service laden in der Plugin-Bundle-Struktur (Resources/config/services.xml) |
| `sw-event-catalog` | Den projektspezifischen Event-Katalog von Shopware nutzen — welche Events es im KONKRETEN Projekt gibt (Core + custom), ihre Event-Klasse, der Event-Name/Konstante, wo sie dispatcht werden und welche Argumente/Payload sie tragen (Getter/Con |
| `sw-events-subscriber` | Auf Shopware-6-Events reagieren mit EventSubscriberInterface: Business-Events, Entity-/Write-Events, Storefront-Page-Loaded-Events, Kernel-Events; Events finden und Prioritäten setzen |
| `sw-extension-points` | Das Shopware-6 Extension-System (ADR "extended event system"): Extension Points nutzen und eigene erstellen, Unterschied Extension Points vs |
| `sw-feature-flags` | Feature-Flags in Shopware 6: Features registrieren und abfragen (Feature::isActive), Major-Feature-Flags, experimentelle Features, Flag bei Bedarf umschalten |
| `sw-filesystem` | Dateien in Shopware 6 über das Filesystem-Abstraction (Flysystem) lesen/schreiben: public vs |
| `sw-logging` | Logging in Shopware-6-Plugins: eigener Monolog-Channel, plugin-eigene Log-Datei, PluginLoggerTrait, Log-Levels |
| `sw-number-range` | Fortlaufende Nummern in Shopware 6 über NumberRange erzeugen (Bestell-/Kunden-/eigene Nummernkreise): NumberRangeValueGeneratorInterface, eigenen Nummernkreis-Typ registrieren |
| `sw-plugin-base` | Eine Shopware-6-Plugin-Basis anlegen: Plugin-Bootstrap-Klasse, composer.json, PSR-4-Autoload, Owner-/Namens-Konventionen (A-Dev-Team Ff, A-Dev-Team Adt, Andreas Gerhardt Ag, Pfötchenbuddies Pb) |
| `sw-plugin-config` | Plugin-Konfiguration in Shopware 6: config.xml (Cards, Input-Felder, Typen, Defaults) und das Auslesen via SystemConfigService |
| `sw-plugin-lifecycle` | Shopware-6-Plugin-Lifecycle implementieren: install/postInstall, update/postUpdate, activate, deactivate, uninstall (mit keepUserData), und der InstallContext/UninstallContext |
| `sw-rate-limiter` | Rate-Limiting in Shopware 6: eingebaute Limiter, eigene Limits für (Store-)API-Routen/Controller konfigurieren, RateLimiter-Service |
| `sw-service-decoration` | Bestehende Shopware-6-Services per Decorator-Pattern anpassen (statt überschreiben) und WANN Decoration statt Event sinnvoll ist |
| `sw-service-tags` | Service-Tags in Shopware 6: getaggte Services, Service-Locator, kernel.event_subscriber, shopware.entity.definition, Tagged-Iterator-Argumente und Compiler-Pass-Nutzung |
| `sw-system-config` | Konfigurationswerte in Shopware 6 lesen/schreiben mit SystemConfigService: Scopes (global vs |

## Agents (3)

| Agent | Beschreibung |
|---|---|
| `shopware-backend` | Spezialist für Shopware-6.7 Backend-Fundamentals: Plugin-Basis/Lifecycle, Dependency Injection & services.xml, Service-Decoration & Tags, Event-Subscriber, CLI-Commands, Logging, Filesystem, Rate-Limiter, Feature-Flags, NumberRange, SystemC |
| `shopware-dev` | Orchestrator und Standard-Einstieg für ALLE Shopware-6.7-Entwicklungsaufgaben |
| `shopware-event-mapper` | Introspektions-Agent: scannt ein Shopware-6-Projekt (Core-Vendor + custom/plugins) nach Events und erzeugt einen gecachten Katalog (.shopware-catalog/events.md) mit Event-Name/Konstante, Event-Klasse, Dispatch-Ort und Argumenten/Payload (Ge |

## Commands (4)

| Command | Beschreibung |
|---|---|
| `/sw-command-create` | Scaffold eines CLI-Commands (bin/console) in einem Shopware-6-Plugin inkl |
| `/sw-config-create` | Scaffold/Erweiterung der Plugin-Konfiguration (config.xml) eines Shopware-6-Plugins mit Cards und Input-Feldern |
| `/sw-event-map` | Scannt das aktuelle Shopware-Projekt (Core + custom) und erzeugt/aktualisiert den Event-Katalog .shopware-catalog/events.md (Event-Name/Konstante, Event-Klasse, Dispatch-Ort, Argumente/Payload) als Grundlage für Subscriber |
| `/sw-plugin-create` | Scaffold eines neuen Shopware-6-Plugins mit korrekten Owner-/Namens-/Namespace-Konventionen, composer.json, Plugin-Klasse und Grundstruktur |
