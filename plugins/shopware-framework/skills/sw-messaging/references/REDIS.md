# Shopware 6 — Redis

Redis (or Valkey) is used in Shopware optionally as fast storage for several subsystems — through
configuration (no code needed by default).

## Areas of use
| Area | Configuration |
|---|---|
| **Cache** (app/HTTP) | Symfony cache adapter on Redis (`framework.cache.app`) |
| **Cart persister** | Cart in Redis instead of the DB (ADR "redis-cart-persister") |
| **Session** | Session handler on Redis |
| **Number range increment** | Increment storage Redis (cluster-safe, fast) |
| **Lock store** | Symfony Lock through Redis |
| **Messenger transport** | Queue transport via Redis (alternative to DB/AMQP) |

```yaml
# config/packages/shopware.yaml (example excerpts)
shopware:
    cart:
        redis_url: '%env(REDIS_URL)%'
    number_range:
        increment_storage: 'Redis'
        redis_url: '%env(REDIS_URL)%'
```

Set `REDIS_URL` (e.g. `redis://localhost:6379/0`) as an env; a separate DB index/connection per subsystem is recommended.
In the cloud/PaaS often preconfigured (`shopware-devops` → `sw-paas`). Performance/scaling benefit strongly from Redis.

## Redis Integration

### Contents

- [Overview](#overview)
- [Accessing Redis via Cache Pool](#accessing-redis-via-cache-pool)
- [Using CacheInvalidator with Tags](#using-cacheinvalidator-with-tags)
- [Tagged Cache (HttpCache)](#tagged-cache-httpcache)
- [Direct Redis Connection](#direct-redis-connection)
- [Cache Pools Available](#cache-pools-available)

### Overview

Plugins can use Redis for caching, session storage, and custom data storage. Shopware supports Redis through Symfony's cache and session components.

### Accessing Redis via Cache Pool

The recommended approach is to use Symfony's cache pools:

```php
// src/Resources/config/services/cache.php — PHP, not XML
// (`XmlFileLoader` is `@deprecated tag:v6.8.0`), explicitly and without autowiring.
$services->set(CacheService::class)
    ->args([service('cache.object')]);
```

→ `shopware-core` → `sw-services` → `DEPENDENCY-INJECTION.md`

```php
<?php declare(strict_types=1);

namespace FfContentPlus\Service;

use Psr\Cache\CacheItemPoolInterface;
use Shopware\Core\Framework\Log\Package;

#[Package('custom-plugins')]
class CacheService
{
    public function __construct(
        private readonly CacheItemPoolInterface $cache,
    )
    {
    }

    public function getCachedData(string $key): mixed
    {
        $item = $this->cache->getItem($key);

        if ($item->isHit()) {
            return $item->get();
        }

        return null;
    }

    public function setCachedData(string $key, mixed $data, int $ttl = 3600): void
    {
        $item = $this->cache->getItem($key);
        $item->set($data);
        $item->expiresAfter($ttl);
        $this->cache->save($item);
    }

    public function invalidate(string $key): void
    {
        $this->cache->deleteItem($key);
    }
}
```

### Using CacheInvalidator with Tags

```php
use Shopware\Core\Framework\Adapter\Cache\CacheInvalidator;

class FfContentPlusCacheInvalidator
{
    public function __construct(
        private readonly CacheInvalidator $cacheInvalidator,
    )
    {
    }

    public function invalidateContentPlusData(): void
    {
        $this->cacheInvalidator->invalidate([
            'ff-content-plus-data',
        ]);
    }
}
```

### Tagged Cache (HttpCache)

For Store API and storefront responses:

```php
use Shopware\Core\Framework\Adapter\Cache\StoreApiRouteCacheTagsEvent;

class CacheTagSubscriber implements EventSubscriberInterface
{
    public static function getSubscribedEvents(): array
    {
        return [
            StoreApiRouteCacheTagsEvent::class => 'onCacheTags',
        ];
    }

    public function onCacheTags(StoreApiRouteCacheTagsEvent $event): void
    {
        $event->addTags(['ff-content-plus-data']);
    }
}
```

### Direct Redis Connection

For advanced use cases requiring direct Redis access:

```php
// src/Resources/config/services/redis.php
use FfContentPlus\Service\RedisService;

use function Symfony\Component\DependencyInjection\Loader\Configurator\env;

$services->set(RedisService::class)
    ->args([env('REDIS_URL')]);
```

```php
class RedisService
{
    private \Redis $redis;

    public function __construct(string $redisUrl)
    {
        $this->redis = new \Redis();
        $parsed = parse_url($redisUrl);
        $this->redis->connect($parsed['host'], $parsed['port'] ?? 6379);
    }
}
```

### Cache Pools Available

| Pool | Purpose |
|------|---------|
| `cache.object` | General object cache |
| `cache.http` | HTTP response cache |
| `cache.rate_limiter` | Rate limiter storage |
