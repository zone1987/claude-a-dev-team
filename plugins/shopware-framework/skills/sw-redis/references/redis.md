# Redis Integration

## Overview

Plugins can use Redis for caching, session storage, and custom data storage. Shopware supports Redis through Symfony's cache and session components.

## Accessing Redis via Cache Pool

The recommended approach is to use Symfony's cache pools:

```xml
<!-- services.xml -->
<service id="FfContentPlus\Service\CacheService">
    <argument type="service" id="cache.object"/>
</service>
```

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

## Using CacheInvalidator with Tags

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

## Tagged Cache (HttpCache)

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

## Direct Redis Connection

For advanced use cases requiring direct Redis access:

```xml
<service id="FfContentPlus\Service\RedisService">
    <argument>%env(REDIS_URL)%</argument>
</service>
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

## Cache Pools Available

| Pool | Purpose |
|------|---------|
| `cache.object` | General object cache |
| `cache.http` | HTTP response cache |
| `cache.rate_limiter` | Rate limiter storage |
