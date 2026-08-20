---
name: sw-platform
description: Shopware platform services: system config, config reference, logging, filesystem, rate limiter, number ranges. Use when the request names Shopware system config or logging.
---

# Shopware platform services

Infrastructure a plugin consumes rather than extends.

## Reference map

- **[CONFIG-REFERENCE.md](CONFIG-REFERENCE.md)**: Vollständige Webserver-Konfigurationen für Nginx, Apache und Caddy. [CONFIG-REFERENCE-SERVER-CONFIGS](CONFIG-REFERENCE-SERVER-CONFIGS.md).
- **[FILESYSTEM.md](FILESYSTEM.md)**: Shopware kapselt Storage über League\Flysystem. [FILESYSTEM-DETAIL](FILESYSTEM-DETAIL.md).
- **[LOGGING.md](LOGGING.md)**: Plugins sollten in einen **eigenen Monolog-Channel** loggen, nicht in den Core-Channel.
- **[NUMBER-RANGE.md](NUMBER-RANGE.md)**: Für fortlaufende, konfigurierbare Nummern den `NumberRangeValueGenerator` nutzen — nicht selbst hochzählen.
- **[RATE-LIMITER.md](RATE-LIMITER.md)**: Shopware liefert Limiter. [RATE-LIMITER-DETAIL](RATE-LIMITER-DETAIL.md).
- **[SYSTEM-CONFIG.md](SYSTEM-CONFIG.md)**: Zentraler Zugriff auf Konfiguration.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
