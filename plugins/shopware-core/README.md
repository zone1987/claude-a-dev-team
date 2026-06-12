# shopware-core

**Wofür:** Plugin-Fundament: Bootstrap/Lifecycle, Dependency Injection, Decoration, Events/Subscriber, CLI-Commands, Config, Logging, Filesystem, Rate-Limiter, Feature-Flags, NumberRange, SystemConfig — plus Architektur-Überblick & Event-Katalog.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Wissen ist aus der Shopware-/OCTO-Quelle destilliert; Skills laden Tiefe progressiv aus `references/`.

## Installation (Claude Code)

```
/plugin marketplace add zone1987/claude-a-dev-team
/plugin install shopware-core@claude-a-dev-team
```

## Skills (18)

`sw-architecture-overview`, `sw-cli-command`, `sw-config-reference`, `sw-dependency-injection`, `sw-event-catalog`, `sw-events-subscriber`, `sw-extension-points`, `sw-feature-flags`, `sw-filesystem`, `sw-logging`, `sw-number-range`, `sw-plugin-base`, `sw-plugin-config`, `sw-plugin-lifecycle`, `sw-rate-limiter`, `sw-service-decoration`, `sw-service-tags`, `sw-system-config`

## Agents (3)

- **`shopware-backend`** — Spezialist für Shopware-6.7 Backend-Fundamentals: Plugin-Basis/Lifecycle, Dependency Injection & services.xml, Service-Decoration & Tags, Event-Subscriber, CLI-Commands, Logging, Filesystem, Rate-Limi
- **`shopware-dev`** — Orchestrator und Standard-Einstieg für ALLE Shopware-6.7-Entwicklungsaufgaben.
- **`shopware-event-mapper`** — Introspektions-Agent: scannt ein Shopware-6-Projekt (Core-Vendor + custom/plugins) nach Events und erzeugt einen gecachten Katalog (.shopware-catalog/events.md) mit Event-Name/Konstante, Event-Klasse,

## Commands (4)

- **`/sw-command-create`** — Scaffold eines CLI-Commands (bin/console) in einem Shopware-6-Plugin inkl.
- **`/sw-config-create`** — Scaffold/Erweiterung der Plugin-Konfiguration (config.xml) eines Shopware-6-Plugins mit Cards und Input-Feldern.
- **`/sw-event-map`** — Scannt das aktuelle Shopware-Projekt (Core + custom) und erzeugt/aktualisiert den Event-Katalog .shopware-catalog/events.md (Event-Name/Konstante, Event-Klasse, Dispatch-Ort, Argumente/Payload) als Gr
- **`/sw-plugin-create`** — Scaffold eines neuen Shopware-6-Plugins mit korrekten Owner-/Namens-/Namespace-Konventionen, composer.json, Plugin-Klasse und Grundstruktur.
