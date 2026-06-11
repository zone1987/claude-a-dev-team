# Shopware 6 — Worker & Cron (Deep Reference)

Sources: `guides/hosting/infrastructure/message-queue.md`, `guides/hosting/infrastructure/scheduled-task.md`

## Message Queue Overview

Shopware uses Symfony Messenger + Enqueue for async message processing. Default transport: database (good for dev, not production). Recommended: RabbitMQ or Redis.

**Admin worker** processes messages in the browser — only suitable for development.

## CLI Worker (recommended for production)

```bash
bin/console messenger:consume async low_priority --time-limit=60 --memory-limit=512M
```

Options:
- `--time-limit=60` — stop after 60 seconds
- `--memory-limit=128M` — stop if memory exceeds limit
- Consume multiple transports for prioritization (left-to-right priority)

**Turn off admin worker:**
```yaml
# config/packages/shopware.yaml
shopware:
    admin_worker:
        enable_admin_worker: false
```

**Also consume failed queue:**
```bash
bin/console messenger:consume failed
```
Messages won't be retried if failed queue is not consumed.

## systemd setup (3 instances)

```ini
# /etc/systemd/system/shopware_consumer@.service
[Unit]
Description=Shopware Message Queue Consumer, instance %i
PartOf=shopware_consumer.target

[Service]
Type=simple
User=www-data
Restart=always
WorkingDirectory=/var/www/html
ExecStart=php /var/www/html/bin/console messenger:consume --time-limit=60 --memory-limit=512M async low_priority

[Install]
WantedBy=shopware_consumer.target
```

```ini
# /etc/systemd/system/shopware_consumer.target
[Install]
WantedBy=multi-user.target

[Unit]
Description=shopware_consumer service
```

```bash
systemctl enable shopware_consumer@{1..3}.service
systemctl enable shopware_consumer.target
systemctl start shopware_consumer.target
```

## Supervisord

See [Symfony documentation](https://symfony.com/doc/current/messenger.html#supervisor-configuration).

## Admin Worker config

```yaml
shopware:
    admin_worker:
        enable_admin_worker: true
        poll_interval: 30
        transports: ["async", "low_priority"]
```

## Mail via message queue

```yaml
# config/packages/framework.yaml
framework:
    mailer:
        message_bus: 'messenger.default_bus'
```

## Transport configuration

### Environment variables

| Variable | Default | Description |
|---|---|---|
| `MESSENGER_TRANSPORT_DSN` | (empty) | Default async queue DSN |
| `MESSENGER_TRANSPORT_LOW_PRIORITY_DSN` | (empty) | Low priority queue DSN |
| `MESSENGER_TRANSPORT_FAILURE_DSN` | (empty) | Failed messages queue DSN |

### RabbitMQ example

```dotenv
MESSENGER_TRANSPORT_DSN=amqp://guest:guest@localhost:5672/%2f/default
MESSENGER_TRANSPORT_LOW_PRIORITY_DSN=amqp://guest:guest@localhost:5672/%2f/low_prio
MESSENGER_TRANSPORT_FAILURE_DSN=amqp://guest:guest@localhost:5672/%2f/failure
```

### Custom transport routing

```yaml
# config/packages/framework.yaml
framework:
    messenger:
        transports:
            async: "%env(MESSENGER_TRANSPORT_DSN)%"
            entity_indexing: "%env(MESSENGER_TRANSPORT_ENTITY_DSN)%"
        routing:
            'Shopware\Core\Framework\DataAbstractionLayer\Indexing\EntityIndexingMessage': entity_indexing
            '*': async
```

Routing overwrite (since 6.6.4.0 / 6.5.12.0):
```yaml
shopware:
    messenger:
        routing_overwrite:
            'Shopware\Core\Framework\DataAbstractionLayer\Indexing\EntityIndexingMessage': entity_indexing
```

## Failed messages

Default retries: 3 times. After 3 failures → dead letter transport.
Configure via `MESSENGER_TRANSPORT_FAILURE_DSN`.

See [Symfony docs](https://symfony.com/doc/current/messenger.html#retries-failures).

## Worker count

No universal recommendation — depends on message types and volumes:
- Product indexing: slow messages → more workers
- Email sending: fast messages → fewer workers
- Use queue monitoring to adjust

## Scheduled Tasks

### Default tasks

| Name | Interval (s) |
|---|---|
| `log_entry.cleanup` | 86400 |
| `shopware.invalidate_cache` | 20 |
| `app_update` | 86400 |
| `version.cleanup` | 86400 |
| `product_keyword_dictionary.cleanup` | 604800 |
| `product_export_generate_task` | 60 |
| `shopware.sitemap_generate` | 86400 |
| `cart.cleanup` | 86400 |
| `shopware.elasticsearch.create.alias` | 300 |

### Running scheduled tasks

Long-running daemon:
```bash
bin/console scheduled-task:run
```

Via cron (`--no-wait` available since 6.5.5.0):
```bash
*/5 * * * * /usr/bin/php /var/www/html/bin/console scheduled-task:run --no-wait
```

With Symfony Scheduler (experimental, since 6.6):
```bash
bin/console messenger:consume scheduler_shopware
```

Note: Restart required after interval changes in DB.

### Management commands (since 6.7.2.0)

```bash
bin/console scheduled-task:list
bin/console scheduled-task:schedule
bin/console scheduled-task:deactivate
```

## Disable scheduled sitemap (since 6.7.1.0)

```yaml
shopware:
    sitemap:
        scheduled_task:
            enabled: false
```

Then use a dedicated cron:
```bash
0 2 * * * cd /var/www/html && php bin/console sitemap:generate
```
