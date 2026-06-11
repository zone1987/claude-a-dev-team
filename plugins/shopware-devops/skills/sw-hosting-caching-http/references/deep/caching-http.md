# Shopware 6 — Caching & Storage (Deep Reference)

Sources: `guides/hosting/performance/caches.md`, `guides/hosting/performance/session.md`, `guides/hosting/performance/cart-storage.md`, `guides/hosting/performance/number-ranges.md`, `guides/hosting/performance/lock-store.md`, `guides/hosting/performance/increment.md`

## HTTP Cache

```dotenv
SHOPWARE_HTTP_CACHE_ENABLED=1
SHOPWARE_HTTP_DEFAULT_TTL=7200    # deprecated in 6.8, use HTTP Caching Policies
```

For production: use Varnish or Fastly (see `sw-hosting-webserver` deep reference).

Storage: always uses App Cache (see below). Move to reverse proxy for multi-server setups.

## App Cache (Object Cache)

Default: filesystem adapter (`var/cache`). Not suitable for multi-server setups.

### Redis

```yaml
# config/packages/cache.yaml
framework:
    cache:
        app: cache.adapter.redis_tag_aware
        system: cache.adapter.redis_tag_aware
        default_redis_provider: redis://localhost
```

`cache.adapter.redis_tag_aware` requires Shopware ≥ 6.5.8.3. Otherwise use `cache.adapter.redis`.

Requires PHP Redis extension. Eviction: `volatile-lru`. No persistence needed.

### Redis URL formats

```
redis://localhost:6379
redis://auth@localhost:6379
redis://localhost:6379/1
redis://localhost:6379?timeout=1
redis:///var/run/redis.sock
redis://auth@/var/run/redis.sock
```

## Session Storage

Default: PHP `session.save_handler` (typically filesystem).

### Via php.ini

```ini
session.save_handler = redis
session.save_path = "tcp://host:6379?database=0"
```

### Via Shopware config

```yaml
# config/packages/redis.yml
framework:
    session:
        handler_id: "redis://host:port/0"
```

Redis config for sessions: persistence (RDB + AOF), eviction `allkeys-lru`.

### Other session handlers

```php
// config/services.php
$services->set('session.db', PdoSessionHandler::class)->args([...]);
```

```yaml
framework:
    session:
        handler_id: "session.db"
```

Available: `PdoSessionHandler`, `MemcachedSessionHandler`, `MongoDbSessionHandler`.

## Cart Storage

Default: database (can cause binlog explosion and performance issues at high throughput).

### Redis (since 6.6.8.0)

```yaml
# config/packages/shopware.yaml
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

### Before 6.6.8.0

```yaml
shopware:
    cart:
        redis_url: 'redis://host:port/dbindex?persistent=1'
```

### Migrate carts

```bash
bin/console cart:migrate sql         # DB → Redis
bin/console cart:migrate redis       # Redis → DB
```

Redis config: persistence (RDB + AOF), eviction `volatile-lru`.

## Number Ranges

Default: database (atomic DB operations → bottleneck at high order volume).

### Redis (since 6.6.8.0)

```yaml
shopware:
    redis:
        connections:
            persistent:
                dsn: 'redis://host:port/dbindex'
    number_range:
        increment_storage: 'redis'
        config:
            connection: 'persistent'
```

### Before 6.6.8.0

```yaml
shopware:
    number_range:
        increment_storage: "Redis"
        redis_url: 'redis://host:port/dbindex'
```

### Migrate number ranges

```bash
bin/console number-range:migrate SQL Redis
```

**Warning:** Migration is NOT atomic. Run during deployment/maintenance only.

Redis config: persistence (RDB + AOF), eviction `volatile-lru`.

## Lock Store

Default: local file lock (breaks in cluster setups).

### Redis

```yaml
# config/packages/lock.yaml
framework:
    lock: 'redis://127.0.0.1:6379/0'
```

All Symfony lock stores are supported. Always use remote store in cluster setups.

## Increment Storage

Default: database `increment` table (causes locks when many workers run).

### Redis (since 6.6.8.0)

```yaml
shopware:
    redis:
        connections:
            persistent:
                dsn: 'redis://host:port/dbindex'
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

### Before 6.6.8.0

```yaml
shopware:
    increment:
        user_activity:
            type: 'redis'
            config:
                url: 'redis://host:port/dbindex'
        message_queue:
            type: 'redis'
            config:
                url: 'redis://host:port/dbindex'
```

### Disable increment storage

```yaml
shopware:
    increment:
        user_activity:
            type: 'array'
        message_queue:
            type: 'array'
```

When disabled: Queue Notification and Module Usage Overview in Admin won't work.

## Delayed Cache Invalidation (Redis)

```yaml
shopware:
    cache:
        invalidation:
            delay_options:
                storage: redis
                connection: 'ephemeral'
```

Default interval: 5 minutes (adjust via `scheduled_task.run_interval` for `shopware.invalidate_cache`).

Disable logged-in/cart cache invalidation (for projects without user-specific content):
```yaml
shopware:
    cache:
        invalidation:
            http_cache: []
```
