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

→ Full configuration per subsystem (cache/cart/session/increment/lock/messenger): [REDIS-DETAIL.md](REDIS-DETAIL.md)
