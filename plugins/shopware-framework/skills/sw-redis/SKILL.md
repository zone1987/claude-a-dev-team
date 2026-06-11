---
name: sw-redis
description: >
  Redis/Valkey in Shopware 6 nutzen: Cache, Cart-Persister, Session, Number-Range-Increment, Lock-Store, Messenger-Transport
  über Redis konfigurieren (config/packages, REDIS_URL, Adapter). Trigger: "Redis shopware", "Valkey", "Redis cache",
  "Redis cart persister", "Redis session", "redis adapter shopware", "REDIS_URL", "Increment Redis". Shopware 6.7.
---

# Shopware 6 — Redis

Redis (bzw. Valkey) wird in Shopware optional als schneller Speicher für mehrere Subsysteme genutzt — über
Konfiguration (kein Code nötig im Standardfall).

## Einsatzbereiche
| Bereich | Konfiguration |
|---|---|
| **Cache** (App/HTTP) | Symfony-Cache-Adapter auf Redis (`framework.cache.app`) |
| **Cart-Persister** | Warenkorb in Redis statt DB (ADR „redis-cart-persister") |
| **Session** | Session-Handler auf Redis |
| **Number-Range-Increment** | Increment-Storage Redis (clustersicher, schnell) |
| **Lock-Store** | Symfony Lock über Redis |
| **Messenger-Transport** | Queue-Transport via Redis (Alternative zu DB/AMQP) |

```yaml
# config/packages/shopware.yaml (Beispiel-Auszüge)
shopware:
    cart:
        redis_url: '%env(REDIS_URL)%'
    number_range:
        increment_storage: 'Redis'
        redis_url: '%env(REDIS_URL)%'
```

`REDIS_URL` (z.B. `redis://localhost:6379/0`) als Env setzen; je Subsystem eigene DB-Index/Connection empfehlenswert.
In der Cloud/PaaS oft vorkonfiguriert (`shopware-devops` → `sw-paas`). Performance/Skalierung profitieren stark von Redis.

→ Vollständige Konfiguration je Subsystem (Cache/Cart/Session/Increment/Lock/Messenger): [references/redis.md](references/redis.md)
