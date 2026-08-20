# Contao 5.x — System

Sources:
- https://docs.contao.org/5.x/manual/de/system/
- https://docs.contao.org/5.x/manual/de/system/einstellungen/
- https://docs.contao.org/5.x/manual/de/system/systemwartung/
- https://docs.contao.org/5.x/manual/de/system/preview-link/
- https://docs.contao.org/5.x/manual/de/system/debug-modus/

---

## Contents

- [Overview](#overview)
- [1. Einstellungen (Settings)](#1-einstellungen-settings)
- [2. Configuration files](#2-configuration-files)
- [3. Environment variables (.env)](#3-environment-variables-env)
- [4. Configuring e-mail dispatch](#4-configuring-e-mail-dispatch)
- [5. Systemwartung (System maintenance)](#5-systemwartung-system-maintenance)
- [6. Preview links](#6-preview-links)
- [7. Debug mode](#7-debug-mode)

## Overview

The "System" area in the Contao backend comprises system-wide settings and tools. Basic system settings affect Contao as an application — an incorrect configuration can lead to malfunctions.

---

## 1. Einstellungen (Settings)

### Global settings

| Setting | Description |
|-------------|-------------|
| **Admin-E-Mail** (Admin e-mail) | Receives notifications about locked accounts and new registrations. Format: `Name <email@example.com>` |

### Date and time

Formats follow the PHP `date()` function. In the backend only numeric formats are permitted.

| Format example | Output |
|----------------|---------|
| `Y-m-d` | 2025-01-28 (ISO-8601) |
| `d.m.Y` | 28.01.2025 (German) |
| `d.m.y` | 28.01.25 (short form) |
| `H:i:s` | 20:36:59 (24h) |
| `g:i A` | 8:36 PM (12h) |

**Time zone**: set this up before creating the website! Contao stores all time information as a Unix timestamp — later changes only apply to newly created entries.

### Backend settings

| Setting | Description |
|-------------|-------------|
| Do not shorten elements | Disables the parent view shortening |
| Items per page | Default: 30 records |
| Max. records per page | Protection against exceeding the PHP memory limit |

#### Further backend options via `config/config.yaml`

```yaml
contao:
    backend:
        attributes:
            app-name: 'Meine App'
            app-version: 1.2.3
        custom_css:
            - files/backend/custom.css
        custom_js:
            - files/backend/custom.js
        badge_title: develop
        route_prefix: '/admin'
        crawl_concurrency: 10   # ab 5.3
```

| Key | Description |
|-----|-------------|
| `attributes` | HTML attributes for the `<body>` tag |
| `custom_css` | Custom stylesheets (URL-reachable) |
| `custom_js` | Custom JavaScript files |
| `badge_title` | Badge title (e.g. "STAGING") |
| `route_prefix` | Backend path (default: `/contao`) |

### Security settings

| Setting | Description |
|-------------|-------------|
| Request token | CSRF protection; disabling it is insecure! |
| Permitted HTML tags | By default all tags are filtered |
| Permitted HTML attributes | `data-*` possible as a wildcard |
| Password hash | Hashing algorithm (default: PHP default) |

Permitted tags/attributes: `*` as a placeholder for all.

### File settings

| Setting | Description |
|-------------|-------------|
| Permitted download file types | Determines the downloadable formats |
| Permitted upload file types | Determines the uploadable formats |
| Max. upload file size | In bytes (1 MiB = 1,048,576 bytes) |
| Max. image width/height | Automatic downscaling when exceeded |

### Default access rights

| Setting | Description |
|-------------|-------------|
| Default owner | User for pages without defined rights |
| Default group | Group for pages without defined rights |
| Default access rights | Default permissions |

---

## 2. Configuration files

### parameters.yaml

Environment-specific parameters (database credentials, SMTP):

```yaml
# config/parameters.yaml
parameters:
    database_host: localhost
    database_port: 3306
    database_user: root
    database_password: 'mein-passwort'
    database_name: contao
    mailer_transport: smtp
    mailer_host: smtp.example.com
    mailer_user: mail@example.com
    mailer_password: 'smtp-passwort'
    mailer_port: 587
    mailer_encryption: tls
```

**Note**: put passwords consisting only of digits or containing special characters in single quotes.

### config.yaml

Application configuration:

```yaml
# config/config.yaml
contao:
    localconfig:
        adminEmail: 'admin@example.com'
        dateFormat: d.m.Y
        timeZone: Europe/Berlin
        undoPeriod: 2592000
```

Contao automatically loads `config_prod.yaml` or `config_dev.yaml`, otherwise `config.yaml`.

**CLI help:**
```bash
php vendor/bin/contao-console config:dump-reference contao
php vendor/bin/contao-console debug:config contao
```

### localconfig reference (common keys)

| Key | Default | Description |
|-----|----------|-------------|
| `adminEmail` | – | Admin e-mail address |
| `dateFormat` | `d.m.Y` | Date format |
| `timeFormat` | `H:i` | Time format |
| `datimFormat` | `d.m.Y H:i` | Date/time format |
| `timeZone` | – | Time zone |
| `logPeriod` | 604800 (7 days) | Log retention in seconds |
| `undoPeriod` | 2592000 (30 days) | Restore period |
| `versionPeriod` | 7776000 (90 days) | Version retention |
| `maxResultsPerPage` | – | Max. records per page |
| `resultsPerPage` | 30 | Items per page |
| `minPasswordLength` | 8 | Min. password length |
| `maxPaginationLinks` | 7 | Pagination links |
| `imageWidth` | – | Max. image width on upload |
| `imageHeight` | – | Max. image height on upload |
| `maxFileSize` | – | Max. upload size |

---

## 3. Environment variables (.env)

Variables are defined in `.env`. `.env.local` overrides `.env` automatically.

### Important variables

| Variable | Description |
|----------|-------------|
| `APP_ENV` | `prod` (default) or `dev` (debug mode) |
| `APP_SECRET` | Basis for the CSRF token (32 characters, random) |
| `DATABASE_URL` | `mysql://user:pass@host:port/dbname` |
| `MAILER_DSN` | `smtp://user:pass@smtp.example.com:587` |

### Cache-relevant variables

| Variable | Description |
|----------|-------------|
| `COOKIE_ALLOW_LIST` | Cookies that are relevant for caching |
| `COOKIE_REMOVE_FROM_DENY_LIST` | Exceptions from the default deny list |
| `QUERY_PARAMS_ALLOW_LIST` | Query parameters for cache handling |
| `QUERY_PARAMS_REMOVE_FROM_DENY_LIST` | Exceptions from the parameter deny list |

Default `COOKIE_ALLOW_LIST`:
```
COOKIE_ALLOW_LIST=PHPSESSID,csrf_https-contao_csrf_token,csrf_contao_csrf_token,trusted_device,REMEMBERME
```

### Proxy configuration

```env
TRUSTED_PROXIES=192.0.2.1
TRUSTED_HOSTS=my.proxy.com
```

### DNS mapping (as of Contao 5.3)

Automates domain changes when copying between environments:

```env
DNS_MAPPING='{
    "www.example.com": "http://example.local",
    "www.foobar.org": "http://foobar.local"
}'
```

---

## 4. Configuring e-mail dispatch

### Via .env.local (recommended)

```env
MAILER_DSN=smtp://benutzername:passwort@smtp.example.com:587
```

**Note**: user name and password must be URL-encoded (`@` → `%40`).

### Several e-mail configurations

**Step 1**: define the transports:
```yaml
# config/config.yaml
framework:
    mailer:
        transports:
            website1: smtps://user%%40example.org:passwort@example.org
            website2: smtps://user%%40example.de:passwort@example.de
```

**Step 2**: make them available in the Contao framework:
```yaml
contao:
    mailer:
        transports:
            website1:
                from: email@example.org
            website2:
                from: Lorem Ipsum <email@example.de>
```

**Step 3**: translations (optional):
```yaml
# translations/mailer_transports.de.yaml
website1: 'SMTP für Webseite 1'
website2: 'SMTP für Webseite 2'
```

### Testing e-mail

```bash
php vendor/bin/contao-console mailer:test \
    --from=sender@example.com \
    --subject=Testmail \
    --body=Testinhalt \
    recipient@example.com
```

### Clearing the cache after configuration changes

```bash
php vendor/bin/contao-console cache:clear --env=prod --no-warmup
php vendor/bin/contao-console cache:warmup --env=prod
```

---

## 5. Systemwartung (System maintenance)

### Maintenance mode

Puts the Contao installation into maintenance mode:
- The frontend is **not reachable** for regular visitors
- The backend remains accessible
- Logged-in users can bypass the mode via the frontend preview
- Every starting point can be put into maintenance mode individually

**Purpose**: larger backend rebuilding work, when frontend changes should not yet be visible.

Via CLI:
```bash
php vendor/bin/contao-console contao:maintenance-mode enable
php vendor/bin/contao-console contao:maintenance-mode disable
```

Disabling manually: delete the file `var/maintenance.html`.

### Crawler (search index)

Pages are indexed automatically when called up in the frontend. For a manual rebuild:

```bash
vendor/bin/contao-console contao:crawl
```

**Domain configuration for the CLI call** (since no HTTP context is present):
```yaml
# config/parameters.yaml
parameters:
    router.request_context.host: 'example.org'
    router.request_context.scheme: 'https'
```

#### Indexing protected pages

```yaml
# config/config.yaml
contao:
    search:
        index_protected: true
```

A frontend user with access to protected pages is logged in automatically when the index is built.

#### Speeding up the crawler

```bash
# Debug-CSV aktivieren
vendor/bin/contao-console contao:crawl --enable-debug-csv

# Gleichzeitige Requests erhöhen
vendor/bin/contao-console contao:crawl --concurrency=10

# Tiefe begrenzen
vendor/bin/contao-console contao:crawl --max-depth=3
```

**Excluding pages**:
- Via `robots.txt` with `User-Agent: contao/crawler`
- HTML attribute: `<a href="..." data-escargot-ignore>` (all crawlers)
- HTML attribute: `<a href="..." data-skip-search-index>` (search index only)

#### Basic authentication for the crawler

```yaml
# config/config.yaml
contao:
    crawl:
        default_http_client_options:
            auth_basic: 'benutzername:passwort'
```

### Daten bereinigen (Purge data)

Under "Daten bereinigen" the following can be purged manually:
- Old thumbnails
- XML sitemaps after Seitenstruktur (Page Structure) changes
- The search index
- The version history
- System logs

---

## 6. Preview links

Preview links make it possible to share frontend previews with external people.

**Creation**: click "URL teilen" (Share URL) in the frontend preview.

**Configurable options:**

| Option | Description |
|--------|-------------|
| Target URL | The frontend page to be shared |
| Expires after | 1 day, 7 days or 30 days |
| Show unpublished | Whether unpublished elements are visible |
| Activate | Enable/block the link |

Links that have been created are managed under **System → Vorschau-Links** (Preview links).

---

## 7. Debug mode

### Ways to enable it

**1. Via an environment variable** (permanent):
```env
APP_ENV=dev
```
⚠️ **Never use this on live servers!**

**2. Via the backend** (for the current user):
- Click the bug icon in the backend → sets a cookie

**3. Via the Contao Manager**:
- Systemwartung (System maintenance) → debug mode button

### Advantages of debug mode

| Feature | Description |
|---------|-------------|
| Stack trace | Errors are shown with a complete stack trace |
| No cache | The page cache is disabled |
| Symfony profiler | Toolbar and profiler available |
| No combining | CSS/JS are loaded individually |
| Template names | Visible as HTML comments in the source code |

### Symfony profiler

The toolbar appears at the bottom edge of the browser. It shows:
- PHP/Symfony/Contao versions
- VarDumper output
- Memory usage
- Database queries and their times
- User information
- Errors, warnings, deprecations

Logs: `var/logs/`
