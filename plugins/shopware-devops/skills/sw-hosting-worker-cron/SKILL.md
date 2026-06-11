---
name: sw-hosting-worker-cron
description: >
  Shopware 6 Message Queue Worker, Scheduled Tasks, Cron-Jobs, systemd, supervisord.
  Triggers: "message queue worker", "messenger:consume", "scheduled task", "cron job",
  "admin worker", "worker setup", "systemd shopware", "supervisord shopware",
  "Message-Queue Worker", "Scheduled Tasks", "Hintergrundprozesse", "RabbitMQ",
  "async queue", "low_priority queue", "failed queue", "messenger transport"
---

# Shopware Hosting — Worker & Cron

Refer to `references/deep/worker-cron.md` for full systemd unit files and supervisord config.

## CLI Worker (recommended for production)

```bash
bin/console messenger:consume async low_priority --time-limit=60 --memory-limit=512M
```

Disable admin worker when CLI worker is in use:
```yaml
# config/packages/shopware.yaml
shopware:
    admin_worker:
        enable_admin_worker: false
```

Also consume the failed queue separately — messages won't be retried otherwise.

## systemd (3 instances)

```ini
# /etc/systemd/system/shopware_consumer@.service
[Service]
Type=simple
User=www-data
Restart=always
WorkingDirectory=/var/www/html
ExecStart=php /var/www/html/bin/console messenger:consume --time-limit=60 --memory-limit=512M async low_priority
```

```bash
systemctl enable shopware_consumer@{1..3}.service
systemctl enable shopware_consumer.target
systemctl start shopware_consumer.target
```

## Scheduled Tasks

```bash
bin/console scheduled-task:run          # long-running daemon
# or via cron:
*/5 * * * * php /var/www/html/bin/console scheduled-task:run --no-wait
```

Run with Symfony Scheduler (experimental, since 6.6):
```bash
bin/console messenger:consume scheduler_shopware
```

List tasks: `bin/console scheduled-task:list`

## Message queue transports

```dotenv
MESSENGER_TRANSPORT_DSN=amqp://guest:guest@localhost:5672/%2f/default
MESSENGER_TRANSPORT_LOW_PRIORITY_DSN=amqp://guest:guest@localhost:5672/%2f/low_prio
MESSENGER_TRANSPORT_FAILURE_DSN=amqp://guest:guest@localhost:5672/%2f/failure
```

## Mail via queue

```yaml
# config/packages/framework.yaml
framework:
    mailer:
        message_bus: 'messenger.default_bus'
```

See also: `sw-hosting-performance` (auto_setup disable), `sw-hosting-installation` (Docker worker container).

Full reference: `references/deep/worker-cron.md`
