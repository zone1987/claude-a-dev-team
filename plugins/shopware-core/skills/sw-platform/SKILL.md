---
name: sw-platform
description: Shopware platform services: system config, config reference, logging, filesystem, rate limiter, number ranges. Use when the request names Shopware system config or logging.
---

# Shopware platform services

Infrastructure a plugin consumes rather than extends.

## Reference map

- **[CONFIG-REFERENCE.md](CONFIG-REFERENCE.md)**: Complete webserver configurations for Nginx, Apache and Caddy. [CONFIG-REFERENCE-SERVER-CONFIGS](CONFIG-REFERENCE-SERVER-CONFIGS.md).
- **[FILESYSTEM.md](FILESYSTEM.md)**: Shopware wraps storage in League\Flysystem. [FILESYSTEM-DETAIL](FILESYSTEM-DETAIL.md).
- **[LOGGING.md](LOGGING.md)**: Plugins should log into their **own Monolog channel**, not into the core channel.
- **[NUMBER-RANGE.md](NUMBER-RANGE.md)**: Use the `NumberRangeValueGenerator` for sequential, configurable numbers — never count up yourself.
- **[RATE-LIMITER.md](RATE-LIMITER.md)**: Shopware ships limiters. [RATE-LIMITER-DETAIL](RATE-LIMITER-DETAIL.md).
- **[SYSTEM-CONFIG.md](SYSTEM-CONFIG.md)**: Central access to configuration.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
