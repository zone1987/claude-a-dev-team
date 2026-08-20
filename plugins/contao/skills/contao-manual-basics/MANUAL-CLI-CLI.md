# Contao 5.x — Command line commands (CLI)

Sources:
- https://docs.contao.org/5.x/manual/de/cli/
- https://docs.contao.org/5.x/manual/de/cli/automator/
- https://docs.contao.org/5.x/manual/de/cli/datenbank-backups/
- https://docs.contao.org/5.x/manual/de/cli/crawl/
- https://docs.contao.org/5.x/manual/de/cli/maintenance-mode/
- https://docs.contao.org/5.x/manual/de/cli/migrate/
- https://docs.contao.org/5.x/manual/de/cli/resize-images/
- https://docs.contao.org/5.x/manual/de/cli/user/
- https://docs.contao.org/5.x/manual/de/cli/dca/

---

## Contents

- [Overview](#overview)
- [1. contao:automator](#1-contaoautomator)
- [2. contao:backup (database backups)](#2-contaobackup-database-backups)
- [3. contao:crawl](#3-contaocrawl)
- [4. contao:maintenance-mode](#4-contaomaintenance-mode)
- [5. contao:migrate](#5-contaomigrate)
- [6. contao:resize-images](#6-contaoresize-images)
- [7. contao:user](#7-contaouser)
- [8. debug:dca](#8-debugdca)

## Overview

The command line offers numerous ways to increase productivity. The Contao Manager provides a graphical interface for some CLI functions, but covers only a fraction of them.

**Show all available commands:**
```bash
php vendor/bin/contao-console list
```

**Help for a command:**
```bash
php vendor/bin/contao-console <befehl> --help
```

---

## 1. contao:automator

Interface to the Contao class `Automator` for general maintenance tasks.

**Syntax:**
```bash
php vendor/bin/contao-console contao:automator [<task>]
```

Without `<task>` an interactive selection appears.

**Available tasks:**

| Task | Function |
|---------|----------|
| `purgeSearchTables` | Delete the search index (`tl_search`, `tl_search_index`) |
| `purgeUndoTable` | Empty the recycle bin (`tl_undo`) — **cannot be undone!** |
| `purgeVersionTable` | Delete the version history (`tl_version`) |
| `purgeSystemLog` | Delete the system log |
| `purgeImageCache` | Clear the image cache (processed/scaled images) |
| `purgeScriptCache` | Clear the JavaScript and CSS cache |
| `purgePageCache` | Clear the HTML page cache |
| `purgeSearchCache` | Clear the search result cache |
| `purgeInternalCache` | Clear the internal Contao cache |
| `purgeTempFolder` | Empty the temporary folder (`system/tmp`) |
| `purgeRegistrations` | Delete member registrations that were not activated |
| `purgeOptInTokens` | Delete expired double opt-in tokens |
| `purgeXmlFiles` | Delete XML files from `generateXmlFiles` |
| `generateSitemap` | Create `sitemap.xml` from the page tree |
| `generateXmlFiles` | Create XML files + call the hook |
| `generateSymlinks` | Create symlinks to the web directory |
| `generateInternalCache` | Warm up the internal cache |

---

## 2. contao:backup (database backups)

Comprehensive backup system for Contao databases. Backups are stored in `var/backups/` by default.

### contao:backup:create

```bash
php vendor/bin/contao-console contao:backup:create
```

Backup file name: `backup__20220126153243.sql.gz` (automatically with a timestamp).

**Custom name:**
```bash
php vendor/bin/contao-console contao:backup:create mein_backup__20220101000000.sql
```

**Options:**

| Option | Description |
|--------|-------------|
| `--ignore-tables` / `-i` | Exclude comma-separated tables |
| `--format` | Output format: `txt` or `json` |

### contao:backup:list

```bash
php vendor/bin/contao-console contao:backup:list
```

Shows the existing backups with their creation date and size.

### contao:backup:restore

```bash
# Neuestes Backup wiederherstellen
php vendor/bin/contao-console contao:backup:restore

# Spezifisches Backup wiederherstellen
php vendor/bin/contao-console contao:backup:restore backup__20220126153243.sql.gz
```

### Automated backups

**Cronjob (daily at 23:10):**
```cron
10 23 * * * /pfad/zum/system/vendor/bin/contao-console contao:backup:create
```

### Configuration

```yaml
# config/config.yaml
contao:
    backup:
        # Tabellen die nicht gesichert werden (z.B. Logs, Crawl-Daten)
        ignore_tables:
            - tl_crawl_queue
            - tl_log
            - tl_search
            - tl_search_index
            - tl_search_term
        # Maximale Anzahl aufzubewahrender Backups
        keep_max: 5
        # Aufbewahrungsintervalle (ältestes Backup pro Intervall behalten)
        keep_intervals:
            - '1D'   # 1 Tag
            - '7D'   # 7 Tage
            - '14D'  # 14 Tage
            - '1M'   # 1 Monat
```

**Time specifiers:**
- `Y` years, `M` months, `D` days, `W` weeks
- `T` prefix for: `H` hours, `M` minutes, `S` seconds
- Can be combined: `1Y2MT5H`

**Note:** `keep_max` should be at least 1 greater than the number of `keep_intervals`.

---

## 3. contao:crawl

HTTP crawler based on the Escargot library. Systematically crawls all URLs.

**Syntax:**
```bash
php vendor/bin/contao-console contao:crawl [options] [<job>]
```

The optional `job` argument allows interrupted crawling processes to be resumed.

### Subscribers

| Subscriber | Function |
|------------|---------|
| `search-index` | Update the search index (only when the search is enabled) |
| `broken-link-checker` | Check for broken links |

### Options

| Option | Description |
|--------|-------------|
| `--subscribers` / `-s` | Comma-separated list of enabled subscribers |
| `--concurrency` / `-c` | Number of simultaneous requests (default: 5) |
| `--delay` | Delay between requests (in microseconds) |
| `--max-requests` | Maximum requests per run |
| `--max-depth` | Crawl depth (default: 3) |
| `--enable-debug-csv` | Enable a CSV file (as `crawl_debug_log.csv`) |
| `--debug-csv-path` | Specify a custom CSV path |

### Examples

```bash
# Nur Suchindex aktualisieren
vendor/bin/contao-console contao:crawl -s search-index

# 10 gleichzeitige Requests, max. 2 Ebenen tief
vendor/bin/contao-console contao:crawl --concurrency=10 --max-depth=2

# Debug-CSV erstellen
vendor/bin/contao-console contao:crawl --enable-debug-csv
```

### Prerequisites

The domain must be configured in the starting point. For the CLI without an HTTP context:
```yaml
# config/parameters.yaml
parameters:
    router.request_context.host: 'example.org'
    router.request_context.scheme: 'https'
```

---

## 4. contao:maintenance-mode

Puts the entire installation (backend and frontend) into maintenance mode.

**Syntax:**
```bash
php vendor/bin/contao-console contao:maintenance-mode [options] [<state>]
```

**States:**

| State | Description |
|-------|-------------|
| `enable` / `on` | Enable maintenance mode |
| `disable` / `off` | Disable maintenance mode |

**Options:**

| Option | Description |
|--------|-------------|
| `--template` | Alternative Twig template (default: `@ContaoCore/Error/service_unavailable.html.twig`) |
| `--templateVars` | Additional template variables as JSON |

**Disabling manually:** delete the file `var/maintenance.html`.

---

## 5. contao:migrate

Carries out database migrations — after new installations, Contao updates or extension installations.

Comprises:
- Update scripts
- Registered migrations from extensions
- Legacy files
- Database schema updates

**Syntax:**
```bash
php vendor/bin/contao-console contao:migrate [options]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--with-deletes` | Run migrations with `DROP` commands |
| `--schema-only` | Migrate the database schema only (no update scripts) |
| `--migrations-only` | Migrations only, no table updates |
| `--dry-run` | Show pending changes without executing them |
| `--no-interaction` | Answer confirmation questions automatically with "yes" |
| `--no-backup` | Disable the default database backup |

---

## 6. contao:resize-images

Creates missing, lazily generated images.

**Syntax:**
```bash
php vendor/bin/contao-console contao:resize-images [options]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--concurrent` | Simultaneous processes or CPU limit. A value < 0.5 = max. 50% CPU |
| `--time-limit` | Time limit in seconds |
| `--image` | A specific image (without the `assets/images` prefix, e.g. `1/foobar-f6eac395d.jpg`) |
| `--no-sub-process` | No subprocesses (careful: extreme memory consumption possible) |
| `--preserve-missing` | Keep deferred image references to images that do not exist |

**Example for hosting with a CPU limit:**
```bash
php vendor/bin/contao-console contao:resize-images --concurrent=0.3 --time-limit=300
```

---

## 7. contao:user

Management of backend users.

### contao:user:list

```bash
php vendor/bin/contao-console contao:user:list [options]
```

| Option | Description |
|--------|-------------|
| `--admins` | Show administrators only |
| `--column` | Columns to display (can be used multiple times) |
| `--format` | Output format: `txt` or `json` |

### contao:user:create

```bash
php vendor/bin/contao-console contao:user:create [options]
```

Interactive prompting for all details when run without options.

| Option | Description |
|--------|-------------|
| `--username` | User name |
| `--name` | Full name |
| `--email` | E-mail address |
| `--password` | Password |
| `--admin` | Create as an administrator |
| `--groups` | Group IDs (comma-separated) |
| `--change-password` | Force a password change at the first login |

### contao:user:password

```bash
php vendor/bin/contao-console contao:user:password <benutzername>
```

⚠️ **Security**: do not pass the password directly as an argument — it is stored in the bash history!

---

## 8. debug:dca

Development tool for analysing Data Container Array (DCA) configurations.

**Syntax:**
```bash
php vendor/bin/contao-console debug:dca <container>
```

**Example:**
```bash
php vendor/bin/contao-console debug:dca tl_page
```

Outputs the **final, assembled** configuration of the container — after all modifications by the application and extensions.

Useful for understanding which fields, callbacks and configurations are active.
