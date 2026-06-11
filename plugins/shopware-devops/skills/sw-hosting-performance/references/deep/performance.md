# Shopware 6 — Performance Tweaks (Deep Reference)

Sources: `guides/hosting/performance/performance-tweaks.md`, `guides/hosting/performance/performance.md`, `guides/hosting/performance/k6.md`

## PHP OPcache (php.ini)

```ini
; disable assert evaluation
zend.assertions=-1

; cache file_exists and is_file checks
; WARNING: leads to errors after cache clear until opcache is cleared
opcache.enable_file_override=1

; increase OPcache string buffer (Shopware has many files)
opcache.interned_strings_buffer=20

; disable timestamp validation (production)
; WARNING: requires PHP-FPM restart on every deployment
opcache.validate_timestamps=0

; disable BOM check
zend.detect_unicode=0

; increase realpath cache
realpath_cache_ttl=3600
realpath_cache_size=4096k

; increase max accelerated files
opcache.max_accelerated_files=20000
```

## OPcache preload (optional, +2-5% perf)

```ini
opcache.preload=/var/www/html/var/cache/opcache-preload.php
opcache.preload_user=www-data
```

**Drawbacks:**
- Requires PHP-FPM restart after each cache clear
- Requires PHP-FPM restart after each file change
- Extension Manager in Admin won't work

**PCRE JIT:**
```bash
php -i | grep 'PCRE JIT Target'
```

## Composer autoloader optimization

```json
{
    "config": {
        "optimize-autoloader": true,
        "classmap-authoritative": true
    }
}
```

`classmap-authoritative=true`: Only when ALL plugins are managed by Composer.
Disables live class lookup — significant performance improvement.

```bash
composer dump-autoload
```

## env.local.php (production)

Skip .env file parsing on every request:
```bash
bin/console dotenv:dump prod
# or:
bin/console system:setup --dump-env
```

Available since Shopware 6.4.15.0.

## HTTP Cache enable

```dotenv
SHOPWARE_HTTP_CACHE_ENABLED=1
```

Use reverse proxy (Varnish/Fastly) for multi-server setups.

## MySQL optimization

```dotenv
SQL_SET_DEFAULT_SESSION_VARIABLES=0
```

Prerequisites:
- `group_concat_max_len ≥ 320000`
- `sql_mode` without `ONLY_FULL_GROUP_BY`

## DAL vs plain SQL

The DAL is flexible but slower. Use plain DBAL/SQL for internal processes where only IDs are needed.
See ADR: [When to use plain SQL or DAL](https://developer.shopware.com/docs/resources/references/adr/2021-05-14-when-to-use-plain-sql-or-dal)

## Elasticsearch must-have for large catalogs

MySQL cannot handle large product assortments well. Set `SHOPWARE_ES_THROW_EXCEPTION=1` in production if ES is required (prevents MySQL overload fallback).

## Mail performance

```yaml
shopware:
    mail:
        update_mail_variables_on_send: false
```

Disables example mail writes to DB on each send (used for admin autocomplete).

## Compression (since 6.6.4.0)

```yaml
shopware:
    cart:
        compress: true
        compression_method: zstd   # faster than gzip, better ratio

    cache:
        cache_compression: true
        cache_compression_method: 'zstd'
```

`zstd` PHP extension required. After changing cache compression, clear cache.

## Messenger auto_setup disable

```dotenv
MESSENGER_TRANSPORT_DSN=redis://localhost?auto_setup=false
```

Run `bin/console messenger:setup-transports` on deploy.

## App URL check disable

```dotenv
APP_URL_CHECK_DISABLED=1
```

Disables self-HTTP-request on admin load to validate APP_URL.

## Logging level (production)

```yaml
# config/packages/prod/monolog.yaml
monolog:
    handlers:
        main:
            level: error
            buffer_size: 30       # prevents memory overflow for long-lived jobs
        business_event_handler_buffer:
            level: error          # set to 'info' to log all flow events
```

## Disable Symfony Secrets

```yaml
framework:
    secrets:
        enabled: false
```

## Increment storage

Move from DB to Redis (prevents DB lock contention with multiple workers).
See `sw-hosting-caching-http` for Redis configuration.

Disable completely if queue stats are not needed:
```yaml
shopware:
    increment:
        user_activity:
            type: 'array'
        message_queue:
            type: 'array'
```

## Reduce product data in listings (since 6.7.12.0)

Enable in Admin: Settings > Products > "Load reduced product data in listings" (`core.listing.partialDataLoading`).

Benefits: lower DB load, memory, transfer size. New installations have this enabled by default.

## Disable Product Stream Indexer (since 6.6.10.0)

```yaml
shopware:
    product_stream:
        indexer:
            enabled: false
```

Drawback: category pages not updated on product stream changes until HTTP cache expires.

## Disable scheduled sitemap generation (since 6.7.1.0)

```yaml
shopware:
    sitemap:
        scheduled_task:
            enabled: false
```

Then set up a dedicated cronjob: `0 2 * * * php bin/console sitemap:generate`

## Speculation Rules API (experimental, since 6.6.10.0)

Enable in Admin > Settings > System > Storefront.
Pre-renders pages on moderate interaction (user must hover/touch a link).
Warning: increases server load and may affect analytics.

## Benchmarking tools

- [locust](https://locust.io/)
- [k6](https://k6.io/)
- Blackfire, Tideways, Datadog

Generic product benchmarks don't apply to custom projects — always use project-specific benchmarks.
