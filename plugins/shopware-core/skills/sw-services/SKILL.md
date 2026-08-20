---
name: sw-services
description: Shopware services: dependency injection, service decoration, service tags, event subscribers, the event catalogue, CLI commands. Use when registering a Shopware service, subscriber or console command.
---

# Shopware services and events

Extend by event subscriber first, decorator second — the platform's own guidance and the reason the event catalogue exists.

## Reference map

- **[CLI-COMMAND.md](CLI-COMMAND.md)**: Ein Plugin-Command ist ein normaler Symfony-Command, registriert via `#[AsCommand]`. [CLI-COMMAND-COMMANDS](CLI-COMMAND-COMMANDS.md).
- **[DEPENDENCY-INJECTION.md](DEPENDENCY-INJECTION.md)**: Services werden in `src/Resources/config/services.xml` registriert. [DEPENDENCY-INJECTION-DI](DEPENDENCY-INJECTION-DI.md).
- **[EVENT-CATALOG.md](EVENT-CATALOG.md)**: Beantwortet: **„welche Events existieren in DIESEM Projekt und was tragen sie?"** — aus einem gecachten Katal….
- **[EVENTS-SUBSCRIBER.md](EVENTS-SUBSCRIBER.md)**: Der **bevorzugte** Erweiterungsweg. [EVENTS-SUBSCRIBER-SUBSCRIBERS](EVENTS-SUBSCRIBER-SUBSCRIBERS.md).
- **[SERVICE-DECORATION.md](SERVICE-DECORATION.md)**: Der Decorator implementiert dasselbe Interface, hält den `.inner`-Service und delegiert.
- **[SERVICE-TAGS.md](SERVICE-TAGS.md)**: Tags machen Services für Shopware/Symfony auffindbar. [SERVICE-TAGS-TAGS](SERVICE-TAGS-TAGS.md).

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
