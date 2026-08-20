# Shopware Hosting — Caching & Storage

Refer to `CACHING-HTTP-DETAIL.md` for full YAML examples.

## Contents

- [HTTP Cache](#http-cache)
- [Object Cache (Redis)](#object-cache-redis)
- [Session (Redis)](#session-redis)
- [Cart (Redis)](#cart-redis)
- [Number Ranges (Redis)](#number-ranges-redis)
- [Lock Store (Redis)](#lock-store-redis)
- [Increment Storage (Redis)](#increment-storage-redis)
- [Delayed cache invalidation (Redis)](#delayed-cache-invalidation-redis)

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

Full reference: `CACHING-HTTP-DETAIL.md`
