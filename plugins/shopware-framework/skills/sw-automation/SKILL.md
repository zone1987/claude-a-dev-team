---
name: sw-automation
description: Shopware automation: Flow Builder actions and triggers, custom rules and conditions, scheduled tasks, the event reference. Use when the request names a Shopware flow, rule or scheduled task.
---

# Shopware rules, flows and tasks

Reacting to events without code changes. The event reference lists every dispatchable event.

## Reference map

- **[CUSTOM-RULE.md](references/CUSTOM-RULE.md)**: A rule encapsulates a condition that the Rule Builder evaluates. [CUSTOM-RULE-RULES](references/CUSTOM-RULE-RULES.md).
- **[EVENTS-REFERENCE.md](references/EVENTS-REFERENCE.md)**: Complete table of all webhook events with event name, description, required permissions and payload str…. [EVENTS-REFERENCE-WEBHOOK-EVENTS-REFERENCE](references/EVENTS-REFERENCE-WEBHOOK-EVENTS-REFERENCE.md).
- **[FLOW-ACTION.md](references/FLOW-ACTION.md)**: An action runs in the Flow Builder in reaction to a trigger. [FLOW-ACTION-FLOW-BUILDER](references/FLOW-ACTION-FLOW-BUILDER.md).
- **[FLOW-REFERENCE.md](references/FLOW-REFERENCE.md)**: Schema for `Resources/flow-action.xml` in apps: `<flow-actions>` → `<flow-action>` with `<meta>`, `<headers>`,…. [FLOW-REFERENCE-FLOW-ACTION-REFERENCE](references/FLOW-REFERENCE-FLOW-ACTION-REFERENCE.md).
- **[FLOW-TRANSACTION.md](references/FLOW-TRANSACTION.md)**: Since the ADRs "transactional flow actions" / "move flow execution after business process", flow actions run **af….
- **[FLOW-TRIGGER.md](references/FLOW-TRIGGER.md)**: Triggers in the Flow Builder are business events that implement `FlowEventAware` and expose data via aware i….
- **[RULE-CONDITION.md](references/RULE-CONDITION.md)**: Every custom rule needs an admin component that renders the condition in the Rule Builder.
- **[SCHEDULED-TASK.md](references/SCHEDULED-TASK.md)**: Two classes: a `ScheduledTask` and a `ScheduledTaskHandler`. [SCHEDULED-TASK-SCHEDULED-TASKS](references/SCHEDULED-TASK-SCHEDULED-TASKS.md).

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (framework guides and reference) plus the Shopware 6.7 source, retrieved 2026-08-20.
