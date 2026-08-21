# Shopware PaaS Native — Cron Jobs & Worker (Deep Reference)

Sources: `products/paas/shopware/guides/cronjobs.md`,
`products/paas/shopware-paas/setup-template.md` (worker section)

---

## Contents

- [Cron jobs in PaaS Native](#cron-jobs-in-paas-native)
- [Configuration in application.yaml](#configuration-in-applicationyaml)
- [Field reference](#field-reference)
- [Name format](#name-format)
- [Cron syntax](#cron-syntax)
- [Timezones](#timezones)
- [CLI management](#cli-management)
- [Execution History](#execution-history)
- [Logs](#logs)
- [Worker in classic Shopware PaaS (Platform.sh)](#worker-in-classic-shopware-paas-platformsh)
- [Complete application.yaml with cron jobs](#complete-applicationyaml-with-cron-jobs)

## Cron jobs in PaaS Native

### Important note

PaaS Native cron jobs do **not** replace Shopware's scheduled tasks.
They are an addition and do not interact with the scheduled task system.

---

## Configuration in application.yaml

```yaml
cronJobs:
  - name: guest-cleanup
    schedule: "0 3 * * *"
    command: "bin/console customer:delete-unused-guests"
    timezone: Europe/Berlin      # Optional, default: UTC

  - name: es-index-cleanup
    schedule: "0 4 * * 0"
    command: "bin/console es:index:cleanup"
    # timezone: UTC (default)

  - name: midnight-report
    schedule: "0 0 * * *"
    command: "bin/console report:generate"
    timezone: America/New_York
```

Cron jobs are created, updated or removed automatically on deploy.

---

## Field reference

| Field | Required | Default | Description |
|------|-------------|---------|-------------|
| `name` | Yes | — | Unique identifier |
| `schedule` | Yes | — | Cron expression (5 fields) |
| `command` | Yes | — | Shell command to run |
| `timezone` | No | `UTC` | IANA timezone |

---

## Name format

Allowed:
- Lowercase letters (`a-z`), digits (`0-9`), hyphens (`-`)
- Must begin and end with a letter or digit
- Minimum length: 2 characters

Valid: `guest-cleanup`, `daily-cleanup`, `es-index-cleanup`
Invalid: `My-Job` (uppercase letter), `-my-job` (leading hyphen), `my_job` (underscore)

---

## Cron syntax

```
┌─────────── Minute (0–59)
│ ┌───────── Hour (0–23)
│ │ ┌─────── Day (1–31)
│ │ │ ┌───── Month (1–12)
│ │ │ │ ┌─── Weekday (0–6, Sunday=0)
│ │ │ │ │
* * * * *
```

| Schedule | Description |
|----------|-------------|
| `0 3 * * *` | Daily at 03:00 |
| `*/15 * * * *` | Every 15 minutes |
| `0 0 * * 0` | Every Sunday at midnight |
| `30 8 1 * *` | 1st of the month at 08:30 |
| `0 9-17 * * 1-5` | Hourly Mon-Fri 9-17 |

---

## Timezones

Default: `UTC`. Any [IANA timezone](https://www.iana.org/time-zones) is allowed.

**Not allowed:** `Local` — always use a specific identifier.

Examples: `Europe/Berlin`, `America/New_York`, `Asia/Tokyo`

---

## CLI management

### List

```bash
sw-paas application cronjob list
sw-paas application cron list           # Alias

# JSON output
sw-paas application cronjob list -o json

# With specific IDs
sw-paas application cronjob list \
  --organization-id <org-id> \
  --project-id <project-id> \
  --application-id <app-id>
```

The output contains: ID, name, schedule, command, timezone, enabled status, last run, last status.

### Details of a cron job

```bash
sw-paas application cronjob get --id <cronjob-id>
# Without --id: interactive selection
```

### Enable / disable

**Important:** cron jobs are **disabled by default** after a deploy.
After changes via the CLI: a new deployment is required!

```bash
# Interactive mode (menu)
sw-paas application cronjob update
# Navigation: ↑/↓ | Toggle: Space | Enable all: a | Disable all: d | Confirm: Enter | Cancel: q/Esc

# Specific job
sw-paas application cronjob update --id <cronjob-id> --enable
sw-paas application cronjob update --id <cronjob-id> --disable

# All jobs
sw-paas application cronjob update --enable --all
sw-paas application cronjob update --disable --all
```

**Note:** `--enable` and `--disable` are mutually exclusive. So are `--all` and `--id`.

---

## Execution History

History is retained for **61 days**.

```bash
# All executions
sw-paas application cronjob history list

# Filter by date
sw-paas application cronjob history list --date 2024-01-15

# Time range
sw-paas application cronjob history list --from "2024-01-15 08:00" --to "2024-01-15 18:00"

# For a specific job
sw-paas application cronjob history list --cronjob-id <cronjob-id>

# A specific run
sw-paas application cronjob history list --run-id <run-id>

# Pagination
sw-paas application cronjob history list --limit 100 --offset 50
```

**Note:** `--date` cannot be combined with `--from`/`--to`.

### History output

| Field | Description |
|------|-------------|
| Run ID | Unique run identifier |
| Status | `RUNNING`, `SUCCEEDED`, `FAILED` |
| Timestamp | Timestamp in the selected timezone |
| Timezone | Timezone used |
| Failure Reason | Cause of failure (only with `FAILED`) |

---

## Logs

```bash
sw-paas application cronjob logs
sw-paas application cron logs          # Alias

# A specific run
sw-paas application cronjob logs --run-id <run-id>

# With a job filter and history limit
sw-paas application cronjob logs \
  --cronjob-id <cronjob-id> \
  --history-limit 100

# Live stream
sw-paas application cronjob logs --follow
sw-paas application cron logs --follow
```

At the end of every output: a Grafana Explore URL for further investigation.

---

## Worker in classic Shopware PaaS (Platform.sh)

In `.platform/applications.yaml`:

```yaml
workers:
  queue:
    commands:
      start: php bin/console messenger:consume --memory-limit=256M --time-limit=60 async
  scheduled_task:
    commands:
      start: php bin/console scheduled-task:run --memory-limit=256M --time-limit=60
```

Workers are copies of the app instance after the build hook.
Default: message queue worker + scheduled task worker.

---

## Complete application.yaml with cron jobs

```yaml
app:
  php:
    version: "8.3"
  environment_variables: []

services:
  mysql:
    version: "8.0"
  opensearch:
    enabled: false

cronJobs:
  - name: guest-cleanup
    schedule: "0 3 * * *"
    command: "bin/console customer:delete-unused-guests"

  - name: es-index-cleanup
    schedule: "0 4 * * 0"
    command: "bin/console es:index:cleanup"

  - name: sitemap-generation
    schedule: "0 2 * * *"
    command: "bin/console sales-channel:update-domains"
    timezone: Europe/Berlin

  - name: cache-warmup
    schedule: "30 1 * * *"
    command: "bin/console http:cache:warm:up"
```
