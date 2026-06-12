# shopware-framework

> Die Framework-Bausteine oberhalb der DAL: Async, Regeln, Flows, APIs, Mail, Media, Suche.

`shopware-framework` deckt die **Framework-Features oberhalb der reinen DAL** ab — also alles, womit ein Plugin
Geschäftslogik, Asynchronität, Erweiterungspunkte und Schnittstellen umsetzt.

Enthalten: **ScheduledTasks** (Cron-artige Aufgaben) und die **Message Queue** (Symfony Messenger: Messages,
Handler, Middleware) für asynchrone Verarbeitung; der **Rule Builder** (eigene Rules + Admin-Bedingungen) und der
**Flow Builder** (eigene Actions, Trigger, Transaktionsverhalten) für konfigurierbare Automatisierung; eigene
**Store-API-Routen** (kundenseitig) und **Admin-API-Controller** (Backend-Aktionen) samt **ACL**; **Webhooks** für
externe Empfänger; **App-Scripts** (Twig-basierte Server-Logik); **Mail** (Templates + Daten/Events, inkl. des
**vollständigen Variablen-Baums** aller 39 Standard-Mail-Templates); **Media & Thumbnails**; sowie die Such-/
Performance-Infrastruktur **Elasticsearch/OpenSearch** und **Redis** (Cache, Cart-Persister, Session, Locks).

Der Spezialist **`shopware-framework-dev`** und die Scaffolder **`/sw-scheduled-task`**, **`/sw-flow-action`**,
**`/sw-rule`**, **`/sw-store-api-route`** beschleunigen die Umsetzung. **Wann nutzen:** für wiederkehrende/
asynchrone Jobs, regel-/flow-basierte Logik, eigene API-Endpunkte, Mailversand, Medien oder Suche. Datenmodelle
dazu liefert `shopware-data`, das Plugin-Fundament `shopware-core`.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Das Wissen ist aus den offiziellen Quellen destilliert und eingebettet; Skills laden ihre Tiefe progressiv aus `references/`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-framework@claude-a-dev-team
```

## Skills (25)

`sw-admin-api-controller`, `sw-api-acl`, `sw-app-script`, `sw-custom-rule`, `sw-elasticsearch`, `sw-elasticsearch-extension`, `sw-events-reference`, `sw-flow-action`, `sw-flow-reference`, `sw-flow-transaction`, `sw-flow-trigger`, `sw-mail-data`, `sw-mail-template`, `sw-mail-variables`, `sw-media-handling`, `sw-media-thumbnail`, `sw-message-handler`, `sw-message-middleware`, `sw-message-queue`, `sw-redis`, `sw-rule-condition`, `sw-scheduled-task`, `sw-store-api-override`, `sw-store-api-route`, `sw-webhook`

## Agents (1)

- **`shopware-framework-dev`** — Spezialist für Shopware-6.7 Framework-Features: ScheduledTasks, Message Queue (Messenger), Rule Builder (eigene Rules), Flow Builder (Actions/Trigger/Transaktionen), Store-API-/Admin-API-Routen, ACL, Webhooks, App-Script

## Commands (4)

- **`/sw-flow-action`** — Scaffold einer Shopware-6 Flow-Builder-Action (PHP + Admin-Komponente) inkl.
- **`/sw-rule`** — Scaffold einer Shopware-6 Custom Rule (PHP Rule + Admin-Bedingungs-Komponente) für den Rule Builder, inkl.
- **`/sw-scheduled-task`** — Scaffold eines Shopware-6 ScheduledTask + Handler inkl. services.xml-Registrierung (Task-Tag + Message-Handler).
- **`/sw-store-api-route`** — Scaffold einer Shopware-6 Store-API-Route (Abstract + Route + Response-Struct) mit _routeScope store-api und Registrierung.
