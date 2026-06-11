---
name: sw-hosting-performance
description: >
  Shopware 6 Performance-Tuning — PHP OPcache, classmap-authoritative, MySQL-Tuning, HTTP-Cache, zstd, Logging.
  Triggers: "performance tuning", "performance tweaks", "opcache config", "php optimization",
  "mysql optimization", "classmap authoritative", "env.local.php", "performance verbessern",
  "PHP Config", "OPcache", "zstd compression", "benchmark", "shopware performance",
  "disable auto_setup", "rate limiter config"
---

# Shopware Hosting — Performance Tweaks

Refer to `references/deep/performance.md` for the full list of all tweaks.

## PHP OPcache (php.ini)

```ini
zend.assertions=-1
opcache.enable_file_override=1
opcache.interned_strings_buffer=20
opcache.validate_timestamps=0    ; requires PHP-FPM restart on deploy!
zend.detect_unicode=0
realpath_cache_ttl=3600
opcache.max_accelerated_files=20000
; optional preload (requires FPM restart on cache clear):
opcache.preload=/var/www/html/var/cache/opcache-preload.php
opcache.preload_user=www-data
```

## Composer autoloader

```json
"config": {
    "optimize-autoloader": true,
    "classmap-authoritative": true
}
```

Only use `classmap-authoritative` when ALL plugins are Composer-managed.

## env.local.php (skip .env parsing in production)

```bash
bin/console dotenv:dump prod
```

## MySQL tuning
- Set `group_concat_max_len ≥ 320000` and remove `ONLY_FULL_GROUP_BY` from `sql_mode`
- Then set `SQL_SET_DEFAULT_SESSION_VARIABLES=0`

## HTTP Cache enable

```dotenv
SHOPWARE_HTTP_CACHE_ENABLED=1
```

## Mail performance

```yaml
shopware:
    mail:
        update_mail_variables_on_send: false
```

## Compression (zstd, since 6.6.4)

```yaml
shopware:
    cart:
        compress: true
        compression_method: zstd
    cache:
        cache_compression: true
        cache_compression_method: 'zstd'
```

## Messenger auto_setup disable

```dotenv
MESSENGER_TRANSPORT_DSN=redis://localhost?auto_setup=false
```

Run `bin/console messenger:setup-transports` on deploy.

## App URL check disable

```dotenv
APP_URL_CHECK_DISABLED=1
```

## Logging (reduce in production)

```yaml
# config/packages/prod/monolog.yaml
monolog:
    handlers:
        main:
            level: error
            buffer_size: 30
        business_event_handler_buffer:
            level: error
```

## Disable Symfony Secrets (if unused)

```yaml
framework:
    secrets:
        enabled: false
```

See also: `sw-hosting-caching-http` (Redis caches), `sw-hosting-database` (MySQL cluster).

Full reference: `references/deep/performance.md`
