---
name: sw-automation
description: Shopware automation: Flow Builder actions and triggers, custom rules and conditions, scheduled tasks, the event reference. Use when the request names a Shopware flow, rule or scheduled task.
---

# Shopware rules, flows and tasks

Reacting to events without code changes. The event reference lists every dispatchable event.

## Reference map

- **[CUSTOM-RULE.md](CUSTOM-RULE.md)**: Eine Rule kapselt eine Bedingung, die der Rule Builder auswertet. [CUSTOM-RULE-RULES](CUSTOM-RULE-RULES.md).
- **[EVENTS-REFERENCE.md](EVENTS-REFERENCE.md)**: Vollständige Tabelle aller Webhook-Events mit Event-Name, Beschreibung, benötigten Permissions und Payload-St…. [EVENTS-REFERENCE-WEBHOOK-EVENTS-REFERENCE](EVENTS-REFERENCE-WEBHOOK-EVENTS-REFERENCE.md).
- **[FLOW-ACTION.md](FLOW-ACTION.md)**: Eine Action wird im Flow Builder als Reaktion auf einen Trigger ausgeführt. [FLOW-ACTION-FLOW-BUILDER](FLOW-ACTION-FLOW-BUILDER.md).
- **[FLOW-REFERENCE.md](FLOW-REFERENCE.md)**: Schema für `Resources/flow-action.xml` in Apps: `<flow-actions>` → `<flow-action>` mit `<meta>`, `<headers>`,…. [FLOW-REFERENCE-FLOW-ACTION-REFERENCE](FLOW-REFERENCE-FLOW-ACTION-REFERENCE.md).
- **[FLOW-TRANSACTION.md](FLOW-TRANSACTION.md)**: Seit ADR „transactional flow actions" / „move flow execution after business process" laufen Flow-Actions **na….
- **[FLOW-TRIGGER.md](FLOW-TRIGGER.md)**: Trigger im Flow Builder sind Business-Events, die `FlowEventAware` implementieren und über Aware-Interfaces D….
- **[RULE-CONDITION.md](RULE-CONDITION.md)**: Jede Custom Rule braucht eine Admin-Komponente, die die Bedingung im Rule Builder darstellt.
- **[SCHEDULED-TASK.md](SCHEDULED-TASK.md)**: Zwei Klassen: ein `ScheduledTask` und ein `ScheduledTaskHandler`. [SCHEDULED-TASK-SCHEDULED-TASKS](SCHEDULED-TASK-SCHEDULED-TASKS.md).

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (framework guides and reference) plus the Shopware 6.7 source, retrieved 2026-08-20.
