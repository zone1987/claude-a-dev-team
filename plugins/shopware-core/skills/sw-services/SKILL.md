---
name: sw-services
description: Shopware services: dependency injection, service decoration, service tags, event subscribers, the event catalogue, CLI commands. Use when registering a Shopware service, subscriber or console command.
---

# Shopware services and events

Extend by event subscriber first, decorator second — the platform's own guidance and the reason the event catalogue exists.

## Reference map

- **[CLI-COMMAND.md](references/CLI-COMMAND.md)**: A plugin command is a plain Symfony command, registered via `#[AsCommand]`. [CLI-COMMAND-COMMANDS](references/CLI-COMMAND-COMMANDS.md).
- **[DEPENDENCY-INJECTION.md](references/DEPENDENCY-INJECTION.md)**: Services are registered in **PHP, not XML, and without autowiring** — Shopware's `XmlFileLoader` is `@deprecated tag:v6.8.0`. Structure, explicit arguments, decorators, and the tags you now set by hand. Legacy XML and autowiring: [DEPENDENCY-INJECTION-DI](references/DEPENDENCY-INJECTION-DI.md).
- **[EVENT-CATALOG.md](references/EVENT-CATALOG.md)**: Answers: **"which events exist in THIS project and what do they carry?"** — from a cached catalogu….
- **[EVENTS-SUBSCRIBER.md](references/EVENTS-SUBSCRIBER.md)**: The **preferred** extension path. [EVENTS-SUBSCRIBER-SUBSCRIBERS](references/EVENTS-SUBSCRIBER-SUBSCRIBERS.md).
- **[SERVICE-RESET.md](references/SERVICE-RESET.md)**: A service that caches needs `ResetInterface` **and** the `kernel.reset` tag — without `autoconfigure` the interface alone does nothing, silently.
- **[SERVICE-DECORATION.md](references/SERVICE-DECORATION.md)**: The decorator implements the same interface, holds the `.inner` service and delegates.
- **[SERVICE-TAGS.md](references/SERVICE-TAGS.md)**: Tags make services discoverable for Shopware/Symfony. [SERVICE-TAGS-TAGS](references/SERVICE-TAGS-TAGS.md).

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
