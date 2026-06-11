---
name: sw-hosting-caching-http
description: >
  Shopware 6 Caching — HTTP-Cache, Object-Cache, Redis-Cache, Session, Cart, Lock-Store, Increment, Number-Ranges.
  Triggers: "cache configuration", "redis cache", "http cache", "object cache", "session storage",
  "cart storage", "lock store", "increment storage", "number ranges", "cache setup",
  "Cache konfigurieren", "Redis für Cache", "Session Redis", "Warenkorb Redis",
  "cache:adapter:redis", "cache pool", "delayed invalidation"
---

# Shopware Hosting — Caching & Storage

Refer to `references/deep/caching-http.md` for full YAML examples.

## HTTP Cache

```dotenv
SHOPWARE_HTTP_CACHE_ENABLED=1
SHOPWARE_HTTP_DEFAULT_TTL=7200
```

For production: use Varnish/Fastly as reverse proxy (see `sw-hosting-webserver`).

## Object Cache (Redis)

```yaml
# config/packages/cache.yaml
framework:
    cache:
        app: cache.adapter.redis_tag_aware
        system: cache.adapter.redis_tag_aware
        default_redis_provider: redis://localhost
```

Requires `cache.adapter.redis_tag_aware` since Shopware 6.5.8.3.

## Session (Redis)

```yaml
# config/packages/redis.yml
framework:
    session:
        handler_id: "redis://host:port/0"
```

Eviction: `allkeys-lru`, persistence: RDB + AOF.

## Cart (Redis)

```yaml
shopware:
    redis:
        connections:
            persistent:
                dsn: 'redis://host:port/dbindex?persistent=1'
    cart:
        storage:
            type: 'redis'
            config:
                connection: 'persistent'
```

Migrate: `bin/console cart:migrate sql`

## Number Ranges (Redis)

```yaml
shopware:
    number_range:
        increment_storage: 'redis'
        config:
            connection: 'persistent'
```

Migrate: `bin/console number-range:migrate SQL Redis`

## Lock Store (Redis)

```yaml
# config/packages/lock.yaml
framework:
    lock: 'redis://127.0.0.1:6379/0'
```

## Increment Storage (Redis)

```yaml
shopware:
    increment:
        user_activity:
            type: 'redis'
            config:
                connection: 'persistent'
        message_queue:
            type: 'redis'
            config:
                connection: 'persistent'
```

Disable: set `type: 'array'` to skip DB locks (Admin queue stats won't work).

## Delayed cache invalidation (Redis)

```yaml
shopware:
    cache:
        invalidation:
            delay_options:
                storage: redis
                connection: 'ephemeral'
```

See also: `sw-hosting-database` (Redis named connections), `sw-hosting-webserver` (Varnish).

Full reference: `references/deep/caching-http.md`
