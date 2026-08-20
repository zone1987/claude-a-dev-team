# shopware-core

> The foundation of every Shopware 6 plugin development.

`shopware-core` is the **entry point** for any work with Shopware 6.7 and bundles the building blocks needed in
practically every plugin. It starts with **architectural orientation** (Shopware is *not* standard
Symfony/Doctrine: its own DAL instead of an ORM, `Criteria` instead of a QueryBuilder, **events before
decorators**, three APIs) and extends from the **plugin foundation** (bootstrap class, `composer.json`, PSR-4,
the vendor-prefix naming convention) to every cross-cutting concern.

Covered: **dependency injection** (`services.xml`, autowiring, argument binding), **service decoration**
(when to use it instead of an event) and **service tags**, the **event/subscriber system** and **extension
points**, custom **CLI commands**, **logging** (dedicated Monolog channel / `PluginLoggerTrait`),
**filesystem** (Flysystem), **rate limiter**, **feature flags**, **NumberRange** and the
**SystemConfigService**. The **event catalogue** (`sw-services` + `/sw-event-map`) additionally produces an
introspection of every event present in the project including its arguments — the basis for any subscriber.

This is also where the **orchestrator `shopware-dev`** lives — the default entry point that assigns a task to
the right domain and delegates to the specialists in the other plugins. For pure backend work below the DAL,
`shopware-backend` takes over. **When to use:** always — as the base. Data models go to `shopware-data`,
framework features (queue/flow/rules/mail/media) to `shopware-framework`.

Part of the **[claude-a-dev-team](../../README.md)** marketplace. The knowledge is distilled from the official
sources and embedded; depth sits in flat reference files beside each SKILL.md, loaded on demand.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-core@claude-a-dev-team
```

## Skills (3)

| Skill | Description |
|---|---|
| `sw-platform` | Shopware platform services: system config, config reference, logging, filesystem, rate limiter, number ranges. Use when the request names Shopware system config or logging |
| `sw-plugin` | Shopware plugin fundamentals: base class, lifecycle, plugin configuration, extension points, feature flags. Use when creating or configuring a Shopware plugin |
| `sw-services` | Shopware services: dependency injection, service decoration, service tags, event subscribers, the event catalogue, CLI commands. Use when registering a Shopware service, subscriber or console command |

## Agents (3)

| Agent | Description |
|---|---|
| `shopware-backend` | Specialist for Shopware 6.7 backend fundamentals: plugin base/lifecycle, dependency injection and services.xml, service decoration and tags, event subscribers, CLI commands, logging, filesystem, rate limiter, feature flags, NumberRange, SystemC |
| `shopware-dev` | Orchestrator and default entry point for ALL Shopware 6.7 development tasks |
| `shopware-event-mapper` | Introspection agent: scans a Shopware 6 project (core vendor + custom/plugins) for events and produces a cached catalogue (.shopware-catalog/events.md) with event name/constant, event class, dispatch location and arguments/payload (getters/con |

## Commands (4)

| Command | Description |
|---|---|
| `/sw-command-create` | Scaffolds a CLI command (bin/console) in a Shopware 6 plugin incl |
| `/sw-config-create` | Scaffolds or extends the plugin configuration (config.xml) of a Shopware 6 plugin with cards and input fields |
| `/sw-event-map` | Scans the current Shopware project (core + custom) and creates or updates the event catalogue .shopware-catalog/events.md (event name/constant, event class, dispatch location, arguments/payload) as the basis for subscribers |
| `/sw-plugin-create` | Scaffolds a new Shopware 6 plugin with correct owner/name/namespace conventions, composer.json, plugin class and base structure |
