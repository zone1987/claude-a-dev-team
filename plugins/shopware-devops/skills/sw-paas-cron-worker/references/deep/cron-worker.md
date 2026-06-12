# Shopware PaaS Native — Cron Jobs & Worker (Deep Reference)

Quellen: `products/paas/shopware/guides/cronjobs.md`,
`products/paas/shopware-paas/setup-template.md` (Worker-Sektion)

---

## Cron Jobs in PaaS Native

### Wichtiger Hinweis

PaaS-Native Cron Jobs ersetzen **nicht** Shopware's Scheduled Tasks.
Sie sind eine Ergänzung und interagieren nicht mit dem Scheduled-Task-System.

---

## Konfiguration in application.yaml

```yaml
cronJobs:
  - name: guest-cleanup
    schedule: "0 3 * * *"
    command: "bin/console customer:delete-unused-guests"
    timezone: Europe/Berlin      # Optional, Default: UTC

  - name: es-index-cleanup
    schedule: "0 4 * * 0"
    command: "bin/console es:index:cleanup"
    # timezone: UTC (Default)

  - name: midnight-report
    schedule: "0 0 * * *"
    command: "bin/console report:generate"
    timezone: America/New_York
```

Cron Jobs werden automatisch erstellt, aktualisiert oder entfernt beim Deploy.

---

## Feld-Referenz

| Feld | Erforderlich | Default | Beschreibung |
|------|-------------|---------|-------------|
| `name` | Ja | — | Eindeutiger Bezeichner |
| `schedule` | Ja | — | Cron-Ausdruck (5-Felder) |
| `command` | Ja | — | Auszuführender Shell-Befehl |
| `timezone` | Nein | `UTC` | IANA-Timezone |

---

## Name-Format

Erlaubt:
- Kleinbuchstaben (`a-z`), Ziffern (`0-9`), Bindestriche (`-`)
- Muss mit Buchstabe oder Ziffer beginnen und enden
- Mindestlänge: 2 Zeichen

Gültig: `guest-cleanup`, `daily-cleanup`, `es-index-cleanup`
Ungültig: `My-Job` (Großbuchstabe), `-my-job` (Bindestrich am Anfang), `my_job` (Unterstrich)

---

## Cron-Syntax

```
┌─────────── Minute (0–59)
│ ┌───────── Stunde (0–23)
│ │ ┌─────── Tag (1–31)
│ │ │ ┌───── Monat (1–12)
│ │ │ │ ┌─── Wochentag (0–6, Sonntag=0)
│ │ │ │ │
* * * * *
```

| Schedule | Beschreibung |
|----------|-------------|
| `0 3 * * *` | Täglich um 03:00 |
| `*/15 * * * *` | Alle 15 Minuten |
| `0 0 * * 0` | Jeden Sonntag um Mitternacht |
| `30 8 1 * *` | 1. des Monats um 08:30 |
| `0 9-17 * * 1-5` | Stündlich Mo-Fr 9-17 Uhr |

---

## Timezones

Standard: `UTC`. Beliebige [IANA-Timezone](https://www.iana.org/time-zones) erlaubt.

**Nicht erlaubt:** `Local` — immer spezifische Identifier verwenden.

Beispiele: `Europe/Berlin`, `America/New_York`, `Asia/Tokyo`

---

## CLI-Verwaltung

### Auflisten

```bash
sw-paas application cronjob list
sw-paas application cron list           # Alias

# JSON-Ausgabe
sw-paas application cronjob list -o json

# Mit spezifischen IDs
sw-paas application cronjob list \
  --organization-id <org-id> \
  --project-id <project-id> \
  --application-id <app-id>
```

Ausgabe enthält: ID, Name, Schedule, Command, Timezone, Enabled-Status, Last Run, Last Status.

### Details eines Cron Jobs

```bash
sw-paas application cronjob get --id <cronjob-id>
# Ohne --id: Interaktive Auswahl
```

### Aktivieren / Deaktivieren

**Wichtig:** Cron Jobs sind nach Deploy **standardmäßig deaktiviert**.
Nach Änderungen via CLI: Neues Deployment erforderlich!

```bash
# Interaktiver Modus (Menü)
sw-paas application cronjob update
# Navigation: ↑/↓ | Toggle: Space | Alle an: a | Alle aus: d | Bestätigen: Enter | Abbruch: q/Esc

# Spezifischer Job
sw-paas application cronjob update --id <cronjob-id> --enable
sw-paas application cronjob update --id <cronjob-id> --disable

# Alle Jobs
sw-paas application cronjob update --enable --all
sw-paas application cronjob update --disable --all
```

**Hinweis:** `--enable` und `--disable` schließen sich gegenseitig aus. `--all` und `--id` ebenso.

---

## Execution History

History wird **61 Tage** aufbewahrt.

```bash
# Alle Ausführungen
sw-paas application cronjob history list

# Nach Datum filtern
sw-paas application cronjob history list --date 2024-01-15

# Zeitbereich
sw-paas application cronjob history list --from "2024-01-15 08:00" --to "2024-01-15 18:00"

# Für spezifischen Job
sw-paas application cronjob history list --cronjob-id <cronjob-id>

# Spezifischen Run
sw-paas application cronjob history list --run-id <run-id>

# Pagination
sw-paas application cronjob history list --limit 100 --offset 50
```

**Hinweis:** `--date` kann nicht mit `--from`/`--to` kombiniert werden.

### History-Ausgabe

| Feld | Beschreibung |
|------|-------------|
| Run ID | Eindeutige Run-Kennung |
| Status | `RUNNING`, `SUCCEEDED`, `FAILED` |
| Timestamp | Zeitstempel in gewählter Timezone |
| Timezone | Verwendete Timezone |
| Failure Reason | Fehlerursache (nur bei `FAILED`) |

---

## Logs

```bash
sw-paas application cronjob logs
sw-paas application cron logs          # Alias

# Spezifischen Run
sw-paas application cronjob logs --run-id <run-id>

# Mit Job-Filter und History-Limit
sw-paas application cronjob logs \
  --cronjob-id <cronjob-id> \
  --history-limit 100

# Live-Stream
sw-paas application cronjob logs --follow
sw-paas application cron logs --follow
```

Am Ende jeder Ausgabe: Grafana Explore URL für Weiteruntersuchung.

---

## Worker in klassischem Shopware PaaS (Platform.sh)

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

Worker sind Kopien der App-Instanz nach dem Build-Hook.
Standard: Message-Queue-Worker + Scheduled-Task-Worker.

---

## Vollständiges application.yaml mit Cron Jobs

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
