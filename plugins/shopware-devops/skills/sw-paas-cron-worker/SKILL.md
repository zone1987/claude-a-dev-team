---
name: sw-paas-cron-worker
description: >
  Shopware PaaS Native Cron Jobs und Worker: Konfiguration in application.yaml,
  CLI-Verwaltung, History, Logs, Aktivierung/Deaktivierung, Timezones.
  Shopware PaaS (Platform.sh) Worker für Message Queue und Scheduled Tasks.
  Trigger: "paas cron job", "sw-paas cronjob", "paas cron einrichten",
  "paas worker konfigurieren", "paas scheduled task", "paas cron aktivieren",
  "paas cron history", "paas cron logs", "paas message queue worker",
  "application.yaml cronJobs".
---

# Shopware PaaS Native — Cron Jobs & Worker

> Cron Jobs ergänzen Shopware's Scheduled Tasks, ersetzen sie nicht.

## Cron Job in application.yaml definieren

```yaml
cronJobs:
  - name: guest-cleanup          # kebab-case, a-z 0-9 -
    schedule: "0 3 * * *"        # Cron-Syntax (5-Felder)
    command: "bin/console customer:delete-unused-guests"
    timezone: Europe/Berlin      # IANA-Timezone (Default: UTC)

  - name: es-index-cleanup
    schedule: "0 4 * * 0"
    command: "bin/console es:index:cleanup"
```

**Wichtig:** Cron Jobs sind nach Deploy **deaktiviert** → explizit aktivieren!

## CLI-Verwaltung

```bash
# Auflisten
sw-paas application cronjob list
sw-paas application cron list

# Details
sw-paas application cronjob get --id <id>

# Aktivieren/Deaktivieren (Deployment nötig!)
sw-paas application cronjob update --id <id> --enable
sw-paas application cronjob update --id <id> --disable
sw-paas application cronjob update --enable --all
sw-paas application cronjob update --disable --all

# Interaktiv (Menü: ↑↓ navigate, Space toggle, a alle, d keine, Enter bestätigen)
sw-paas application cronjob update

# History (61 Tage)
sw-paas application cronjob history list
sw-paas application cronjob history list --date 2024-01-15
sw-paas application cronjob history list --cronjob-id <id>

# Logs
sw-paas application cronjob logs
sw-paas application cron logs --run-id <run-id>
sw-paas application cron logs --follow
```

## Cron-Syntax Beispiele

| Schedule | Beschreibung |
|----------|-------------|
| `0 3 * * *` | Täglich um 03:00 |
| `*/15 * * * *` | Alle 15 Minuten |
| `0 0 * * 0` | Sonntag um Mitternacht |
| `30 8 1 * *` | 1. des Monats um 08:30 |

## Vertiefung

[references/deep/cron-worker.md](references/deep/cron-worker.md)
