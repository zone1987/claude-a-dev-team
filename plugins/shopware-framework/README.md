# shopware-framework

> The framework building blocks above the DAL: async, rules, flows, APIs, mail, media, search.

`shopware-framework` covers the **framework features above the plain DAL** — everything a plugin uses to
implement business logic, asynchronicity, extension points and interfaces.

Included: **ScheduledTasks** (cron-like jobs) and the **message queue** (Symfony Messenger: messages, handlers,
middleware) for asynchronous processing; the **Rule Builder** (custom rules + administration conditions) and the
**Flow Builder** (custom actions, triggers, transactional behaviour) for configurable automation; custom
**Store API routes** (customer-facing) and **Admin API controllers** (backend actions) together with **ACL**;
**webhooks** for external receivers; **app scripts** (Twig-based server logic); **mail** (templates + data/events,
including the **complete variable tree** of all 39 standard mail templates); **media and thumbnails**; plus the
search/performance infrastructure **Elasticsearch/OpenSearch** and **Redis** (cache, cart persister, session,
locks).

The specialist **`shopware-framework-dev`** and the scaffolders **`/sw-scheduled-task`**, **`/sw-flow-action`**,
**`/sw-rule`**, **`/sw-store-api-route`** speed up the implementation. **When to use:** for recurring or
asynchronous jobs, rule- and flow-based logic, custom API endpoints, mail delivery, media or search. The
matching data models come from `shopware-data`, the plugin foundation from `shopware-core`.

Part of the **[claude-a-dev-team](../../README.md)** marketplace. The knowledge is distilled from the official
sources and embedded; depth sits in flat reference files beside each SKILL.md, loaded on demand.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-framework@claude-a-dev-team
```

## Skills (4)

| Skill | Description |
|---|---|
| `sw-api` | Shopware API extension: Store API routes and overrides, Admin API controllers, API ACL, webhooks, app scripts. Use when adding or overriding a Shopware Store API or Admin API route |
| `sw-automation` | Shopware automation: Flow Builder actions and triggers, custom rules and conditions, scheduled tasks, the event reference. Use when the request names a Shopware flow, rule or scheduled task |
| `sw-content` | Shopware content services: mail templates and variables, media handling and thumbnails, Elasticsearch. Use when the request names a Shopware mail template, media or Elasticsearch |
| `sw-messaging` | Shopware messaging: the message queue, handlers, middleware, Redis configuration. Use when the request names a Shopware message queue, message handler or Redis |

## Agents (1)

| Agent | Description |
|---|---|
| `shopware-framework-dev` | Specialist for Shopware 6.7 framework features: ScheduledTasks, message queue (Messenger), Rule Builder (custom rules), Flow Builder (actions/triggers/transactions), Store API and Admin API routes, ACL, webhooks, app scripts, mail templates/d |

## Commands (4)

| Command | Description |
|---|---|
| `/sw-flow-action` | Scaffolds a Shopware 6 Flow Builder action (PHP + administration component) incl |
| `/sw-rule` | Scaffolds a Shopware 6 custom rule (PHP rule + administration condition component) for the Rule Builder, incl |
| `/sw-scheduled-task` | Scaffolds a Shopware 6 ScheduledTask + handler including services.xml registration (task tag + message handler) |
| `/sw-store-api-route` | Scaffolds a Shopware 6 Store API route (abstract + route + response struct) with _routeScope store-api and registration |
