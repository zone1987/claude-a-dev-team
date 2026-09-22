---
name: sw-platform
description: Shopware platform services: system config, config reference, logging, filesystem, rate limiter, number ranges. Use when the request names Shopware system config or logging.
---

# Shopware platform services

Infrastructure a plugin consumes rather than extends.

## Reference map

- **[CONFIG-REFERENCE.md](references/CONFIG-REFERENCE.md)**: Complete webserver configurations for Nginx, Apache and Caddy.
- **[FILESYSTEM.md](references/FILESYSTEM.md)**: Shopware wraps storage in League\Flysystem.
- **[LOGGING.md](references/LOGGING.md)**: Every plugin logs into its **own Monolog channel** — the configuration, the `build()` override Shopware needs but does not do for you, what is logged and what never is, and how the logger is asserted in a test.
- **[NUMBER-RANGE.md](references/NUMBER-RANGE.md)**: Use the `NumberRangeValueGenerator` for sequential, configurable numbers — never count up yourself.
- **[RATE-LIMITER.md](references/RATE-LIMITER.md)**: Shopware ships limiters.
- **[SYSTEM-CONFIG.md](references/SYSTEM-CONFIG.md)**: Central access to configuration.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
