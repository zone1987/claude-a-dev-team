# shopware-framework

**Wofür:** Framework-Features: ScheduledTasks, MessageQueue, Rule-Builder, Flow-Builder, Store-/Admin-API-Routen, ACL, Webhooks, App-Scripts, Mail (inkl. Variablen-Baum), Media, Elasticsearch, Redis.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Wissen ist aus der Shopware-/OCTO-Quelle destilliert; Skills laden Tiefe progressiv aus `references/`.

## Installation (Claude Code)

```
/plugin marketplace add zone1987/claude-a-dev-team
/plugin install shopware-framework@claude-a-dev-team
```

## Skills (25)

`sw-admin-api-controller`, `sw-api-acl`, `sw-app-script`, `sw-custom-rule`, `sw-elasticsearch`, `sw-elasticsearch-extension`, `sw-events-reference`, `sw-flow-action`, `sw-flow-reference`, `sw-flow-transaction`, `sw-flow-trigger`, `sw-mail-data`, `sw-mail-template`, `sw-mail-variables`, `sw-media-handling`, `sw-media-thumbnail`, `sw-message-handler`, `sw-message-middleware`, `sw-message-queue`, `sw-redis`, `sw-rule-condition`, `sw-scheduled-task`, `sw-store-api-override`, `sw-store-api-route`, `sw-webhook`

## Agents (1)

- **`shopware-framework-dev`** — Spezialist für Shopware-6.7 Framework-Features: ScheduledTasks, Message Queue (Messenger), Rule Builder (eigene Rules), Flow Builder (Actions/Trigger/Transaktionen), Store-API-/Admin-API-Routen, ACL, 

## Commands (4)

- **`/sw-flow-action`** — Scaffold einer Shopware-6 Flow-Builder-Action (PHP + Admin-Komponente) inkl.
- **`/sw-rule`** — Scaffold einer Shopware-6 Custom Rule (PHP Rule + Admin-Bedingungs-Komponente) für den Rule Builder, inkl.
- **`/sw-scheduled-task`** — Scaffold eines Shopware-6 ScheduledTask + Handler inkl. services.xml-Registrierung (Task-Tag + Message-Handler).
- **`/sw-store-api-route`** — Scaffold einer Shopware-6 Store-API-Route (Abstract + Route + Response-Struct) mit _routeScope store-api und Registrierung.
