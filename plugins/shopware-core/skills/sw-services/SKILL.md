---
name: sw-services
description: Shopware services: dependency injection, service decoration, service tags, event subscribers, the event catalogue, CLI commands. Use when registering a Shopware service, subscriber or console command.
---

# Shopware services and events

Extend by event subscriber first, decorator second — the platform's own guidance and the reason the event catalogue exists.

## Reference map

- **[CLI-COMMAND.md](CLI-COMMAND.md)**: A plugin command is a plain Symfony command, registered via `#[AsCommand]`. [CLI-COMMAND-COMMANDS](CLI-COMMAND-COMMANDS.md).
- **[DEPENDENCY-INJECTION.md](DEPENDENCY-INJECTION.md)**: Register services in `src/Resources/config/services.xml`. [DEPENDENCY-INJECTION-DI](DEPENDENCY-INJECTION-DI.md).
- **[EVENT-CATALOG.md](EVENT-CATALOG.md)**: Answers: **"which events exist in THIS project and what do they carry?"** — from a cached catalogu….
- **[EVENTS-SUBSCRIBER.md](EVENTS-SUBSCRIBER.md)**: The **preferred** extension path. [EVENTS-SUBSCRIBER-SUBSCRIBERS](EVENTS-SUBSCRIBER-SUBSCRIBERS.md).
- **[SERVICE-DECORATION.md](SERVICE-DECORATION.md)**: The decorator implements the same interface, holds the `.inner` service and delegates.
- **[SERVICE-TAGS.md](SERVICE-TAGS.md)**: Tags make services discoverable for Shopware/Symfony. [SERVICE-TAGS-TAGS](SERVICE-TAGS-TAGS.md).

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
