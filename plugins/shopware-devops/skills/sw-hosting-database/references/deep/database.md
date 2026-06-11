# Shopware 6 — Database & Redis (Deep Reference)

Sources: `guides/hosting/infrastructure/database.md`, `guides/hosting/infrastructure/redis.md`

## MySQL / MariaDB Requirements

- Minimum: MariaDB ≥ 10.11.6, MySQL ≥ 8.0.22
- Recommended: MariaDB 11.4 / MySQL 8.4
- `max_allowed_packet ≥ 32M`
- `group_concat_max_len ≥ 320000`
- `sql_mode` must NOT contain `ONLY_FULL_GROUP_BY`

## Database cluster

### Shopware read/write split

Shopware automatically routes `INSERT`/`UPDATE`/`DELETE` to the primary and read queries to replicas. After any write in a request, all subsequent queries in that request use the primary to maintain consistency.

### ProxySQL (recommended)
Use [ProxySQL](https://proxysql.com/) as DB proxy instead of configuring Shopware to connect to multiple servers directly. Benefits: connection pooling, load balancing, failover, query caching.

### Configure replicas

```dotenv
DATABASE_URL=mysql://user:pass@primary:3306/shopware
DATABASE_REPLICA_0_URL=mysql://user:pass@replica1:3306/shopware
DATABASE_REPLICA_1_URL=mysql://user:pass@replica2:3306/shopware
```

### MySQL variables on all servers

```sql
-- Set in MySQL config file (my.cnf):
group_concat_max_len = 320000
-- Remove ONLY_FULL_GROUP_BY from sql_mode
```

After configuring MySQL directly:
```dotenv
SQL_SET_DEFAULT_SESSION_VARIABLES=0
```

## Reconnect for long-running environments (FrankenPHP worker mode)

FrankenPHP keeps connections alive, which can exceed MySQL's `wait_timeout` and cause `MySQL server has gone away` errors.

```bash
composer require facile-it/doctrine-mysql-come-back
```

```dotenv
# Without replicas:
DATABASE_URL="mysql://user:pass@localhost:3306/db?wrapperClass=Facile\DoctrineMySQLComeBack\Doctrine\DBAL\Connection&driverOptions[x_reconnect_attempts]=3"

# With replicas:
DATABASE_URL="mysql://user:pass@localhost:3306/db?wrapperClass=Facile\DoctrineMySQLComeBack\Doctrine\DBAL\Connections\PrimaryReadReplicaConnection&driverOptions[x_reconnect_attempts]=3"
DATABASE_REPLICA_0_URL="mysql://user:pass@replica:3306/db"
```

## Redis Overview

Redis can be used for:
- Caching (HTTP cache + object cache) — ephemeral
- Sessions — durable/aging
- Cart — durable/critical
- Number ranges — durable/critical
- Lock store — durable/critical
- Increment storage — durable
- Message queue — optional

**Important:** Different eviction policies cannot be applied to different databases within the same Redis instance. Use separate instances for different data categories.

## Redis data categories

### 1. Ephemeral (caches)

| Setting | Value |
|---|---|
| Eviction policy | `volatile-lru` |
| Persistence | None (in-memory only) |
| Use for | HTTP cache, object cache |

### 2. Durable but "aging" (sessions)

| Setting | Value |
|---|---|
| Eviction policy | `allkeys-lru` |
| Persistence | RDB + AOF |
| Use for | Sessions |

### 3. Durable and critical (cart, numbers, locks)

| Setting | Value |
|---|---|
| Eviction policy | `volatile-lru` |
| Persistence | RDB + AOF |
| Use for | Cart, number ranges, lock store, increment |

## Named Redis connections (since 6.6.8.0)

```yaml
# config/packages/shopware.yaml
shopware:
    redis:
        connections:
            ephemeral:
                dsn: 'redis://host1:port/1'
            ephemeral_2:
                dsn: '%env(REDIS_EPHEMERAL)%/2'
            persistent:
                dsn: 'redis://host2:port/2?persistent=1'
```

Connection names are used as service names in the container — follow service naming conventions.

## Connection pooling (persistent connections)

```yaml
shopware:
    redis:
        connections:
            ephemeral:
                dsn: 'redis://host:port/dbindex?persistent=1'
```

`persistent=1` refers to TCP connection pooling, NOT data persistence.

## Redis cluster settings

Add to `php.ini` when using Redis cluster:
```ini
redis.clusters.cache_slots=1
```

This skips cluster node lookup on each connection (performance optimization).

## Recommended 5-Redis setup (cluster production)

1. **Session + Cart** — persistent, `allkeys-lru` / `volatile-lru`
2. **cache.object** — ephemeral, `volatile-lru`, no persistence
3. **Lock store + Increment storage** — persistent, `volatile-lru`
4. **Number Ranges** — persistent, `volatile-lru`
5. **Message Queue** — configure via `MESSENGER_TRANSPORT_DSN=redis://...`

## PHP Redis extension

The PHP Redis extension (not Predis) is preferred for:
- Persistent connections support
- Better performance in high-load
- Redis cluster support

## Redis SSL/TLS

Use `rediss://` scheme for SSL connections:
```yaml
dsn: 'rediss://host:6380/0'
```
