# Shopware PaaS Native — Cron Jobs & Worker

> Cron jobs complement Shopware's scheduled tasks, they do not replace them.

## Define a cron job in application.yaml

```yaml
cronJobs:
  - name: guest-cleanup          # kebab-case, a-z 0-9 -
    schedule: "0 3 * * *"        # Cron syntax (5 fields)
    command: "bin/console customer:delete-unused-guests"
    timezone: Europe/Berlin      # IANA timezone (default: UTC)

  - name: es-index-cleanup
    schedule: "0 4 * * 0"
    command: "bin/console es:index:cleanup"
```

**Important:** cron jobs are **disabled** after a deploy → enable them explicitly!

## CLI management

```bash
# List
sw-paas application cronjob list
sw-paas application cron list

# Details
sw-paas application cronjob get --id <id>

# Enable/disable (a deployment is required!)
sw-paas application cronjob update --id <id> --enable
sw-paas application cronjob update --id <id> --disable
sw-paas application cronjob update --enable --all
sw-paas application cronjob update --disable --all

# Interactive (menu: ↑↓ navigate, Space toggle, a all, d none, Enter confirm)
sw-paas application cronjob update

# History (61 days)
sw-paas application cronjob history list
sw-paas application cronjob history list --date 2024-01-15
sw-paas application cronjob history list --cronjob-id <id>

# Logs
sw-paas application cronjob logs
sw-paas application cron logs --run-id <run-id>
sw-paas application cron logs --follow
```

## Cron syntax examples

| Schedule | Description |
|----------|-------------|
| `0 3 * * *` | Daily at 03:00 |
| `*/15 * * * *` | Every 15 minutes |
| `0 0 * * 0` | Sunday at midnight |
| `30 8 1 * *` | 1st of the month at 08:30 |

## Deep dive

[CRON-WORKER-DETAIL.md](CRON-WORKER-DETAIL.md)
