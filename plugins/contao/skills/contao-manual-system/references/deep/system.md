# Contao 5.x — System

Quellen:
- https://docs.contao.org/5.x/manual/de/system/
- https://docs.contao.org/5.x/manual/de/system/einstellungen/
- https://docs.contao.org/5.x/manual/de/system/systemwartung/
- https://docs.contao.org/5.x/manual/de/system/preview-link/
- https://docs.contao.org/5.x/manual/de/system/debug-modus/

---

## Übersicht

Der Bereich „System" im Contao-Backend umfasst systemweite Einstellungen und Werkzeuge. Grundlegende Systemeinstellungen beeinflussen Contao als Applikation — fehlerhafte Konfiguration kann zu Fehlfunktionen führen.

---

## 1. Einstellungen

### Globale Einstellungen

| Einstellung | Beschreibung |
|-------------|-------------|
| **Admin-E-Mail** | Empfängt Benachrichtigungen über gesperrte Konten und neue Registrierungen. Format: `Name <email@example.com>` |

### Datum und Zeit

Formate folgen der PHP `date()`-Funktion. Im Backend nur numerische Formate erlaubt.

| Formatbeispiel | Ausgabe |
|----------------|---------|
| `Y-m-d` | 2025-01-28 (ISO-8601) |
| `d.m.Y` | 28.01.2025 (Deutsch) |
| `d.m.y` | 28.01.25 (Kurzform) |
| `H:i:s` | 20:36:59 (24h) |
| `g:i A` | 8:36 PM (12h) |

**Zeitzone**: Vor Websiteerstellung einrichten! Contao speichert alle Zeitangaben als Unix-Timestamp — spätere Änderungen gelten nur für neu erstellte Einträge.

### Backend-Einstellungen

| Einstellung | Beschreibung |
|-------------|-------------|
| Elemente nicht verkürzen | Deaktiviert Parent-View-Verkürzung |
| Elemente pro Seite | Standard: 30 Datensätze |
| Max. Datensätze pro Seite | Schutz vor PHP Memory Limit Überschreitungen |

#### Weitere Backend-Optionen via `config/config.yaml`

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

| Key | Beschreibung |
|-----|-------------|
| `attributes` | HTML-Attribute für `<body>`-Tag |
| `custom_css` | Eigene Stylesheets (URL-erreichbar) |
| `custom_js` | Eigene JavaScript-Dateien |
| `badge_title` | Badge-Titel (z.B. „STAGING") |
| `route_prefix` | Backend-Pfad (Standard: `/contao`) |

### Sicherheitseinstellungen

| Einstellung | Beschreibung |
|-------------|-------------|
| Anfrage-Token | CSRF-Schutz; Deaktivierung unsicher! |
| Erlaubte HTML-Tags | Standardmäßig werden alle Tags gefiltert |
| Erlaubte HTML-Attribute | `data-*` als Wildcard möglich |
| Passwort-Hash | Hashing-Algorithmus (Standard: PHP-Default) |

Erlaubte Tags/Attribute: `*` als Platzhalter für alle.

### Datei-Einstellungen

| Einstellung | Beschreibung |
|-------------|-------------|
| Erlaubte Download-Dateitypen | Bestimmt herunterladbare Formate |
| Erlaubte Upload-Dateitypen | Bestimmt hochladbare Formate |
| Max. Upload-Dateigröße | In Bytes (1 MiB = 1.048.576 Bytes) |
| Max. Bildbreite/-höhe | Automatische Verkleinerung bei Überschreitung |

### Standard-Zugriffsrechte

| Einstellung | Beschreibung |
|-------------|-------------|
| Standardbesitzer | Benutzer für Seiten ohne definierte Rechte |
| Standardgruppe | Gruppe für Seiten ohne definierte Rechte |
| Standardzugriffsrechte | Default-Permissions |

---

## 2. Konfigurationsdateien

### parameters.yaml

Umgebungsspezifische Parameter (Datenbankzugänge, SMTP):

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

**Hinweis**: Passwörter aus nur Ziffern oder mit Sonderzeichen in Hochkommata setzen.

### config.yaml

Anwendungskonfiguration:

```yaml
# config/config.yaml
contao:
    localconfig:
        adminEmail: 'admin@example.com'
        dateFormat: d.m.Y
        timeZone: Europe/Berlin
        undoPeriod: 2592000
```

Contao lädt automatisch `config_prod.yaml` oder `config_dev.yaml`, andernfalls `config.yaml`.

**CLI-Hilfe:**
```bash
php vendor/bin/contao-console config:dump-reference contao
php vendor/bin/contao-console debug:config contao
```

### localconfig-Referenz (häufige Keys)

| Key | Standard | Beschreibung |
|-----|----------|-------------|
| `adminEmail` | – | Admin-E-Mail-Adresse |
| `dateFormat` | `d.m.Y` | Datumsformat |
| `timeFormat` | `H:i` | Zeitformat |
| `datimFormat` | `d.m.Y H:i` | Datums-/Zeitformat |
| `timeZone` | – | Zeitzone |
| `logPeriod` | 604800 (7 Tage) | Log-Aufbewahrung in Sekunden |
| `undoPeriod` | 2592000 (30 Tage) | Wiederherstellungsperiode |
| `versionPeriod` | 7776000 (90 Tage) | Versions-Aufbewahrung |
| `maxResultsPerPage` | – | Max. Datensätze pro Seite |
| `resultsPerPage` | 30 | Elemente pro Seite |
| `minPasswordLength` | 8 | Min. Passwortlänge |
| `maxPaginationLinks` | 7 | Blätter-Links |
| `imageWidth` | – | Max. Bildbreite beim Upload |
| `imageHeight` | – | Max. Bildhöhe beim Upload |
| `maxFileSize` | – | Max. Upload-Größe |

---

## 3. Umgebungsvariablen (.env)

Variablen werden in `.env` definiert. `.env.local` überschreibt `.env` automatisch.

### Wichtige Variablen

| Variable | Beschreibung |
|----------|-------------|
| `APP_ENV` | `prod` (Standard) oder `dev` (Debug-Modus) |
| `APP_SECRET` | CSRF-Token-Basis (32 Zeichen, zufällig) |
| `DATABASE_URL` | `mysql://user:pass@host:port/dbname` |
| `MAILER_DSN` | `smtp://user:pass@smtp.example.com:587` |

### Cache-relevante Variablen

| Variable | Beschreibung |
|----------|-------------|
| `COOKIE_ALLOW_LIST` | Cookies, die für Caching relevant sind |
| `COOKIE_REMOVE_FROM_DENY_LIST` | Ausnahmen aus der Standard-Deny-Liste |
| `QUERY_PARAMS_ALLOW_LIST` | Query-Parameter für Cache-Handling |
| `QUERY_PARAMS_REMOVE_FROM_DENY_LIST` | Ausnahmen aus der Parameter-Deny-Liste |

Standard `COOKIE_ALLOW_LIST`:
```
COOKIE_ALLOW_LIST=PHPSESSID,csrf_https-contao_csrf_token,csrf_contao_csrf_token,trusted_device,REMEMBERME
```

### Proxy-Konfiguration

```env
TRUSTED_PROXIES=192.0.2.1
TRUSTED_HOSTS=my.proxy.com
```

### DNS-Mapping (ab Contao 5.3)

Automatisiert Domain-Änderungen beim Kopieren zwischen Umgebungen:

```env
DNS_MAPPING='{
    "www.example.com": "http://example.local",
    "www.foobar.org": "http://foobar.local"
}'
```

---

## 4. E-Mail-Versand konfigurieren

### Via .env.local (empfohlen)

```env
MAILER_DSN=smtp://benutzername:passwort@smtp.example.com:587
```

**Hinweis**: Benutzername und Passwort müssen URL-kodiert sein (`@` → `%40`).

### Mehrere E-Mail-Konfigurationen

**Schritt 1**: Transports definieren:
```yaml
# config/config.yaml
framework:
    mailer:
        transports:
            website1: smtps://user%%40example.org:passwort@example.org
            website2: smtps://user%%40example.de:passwort@example.de
```

**Schritt 2**: In Contao Framework verfügbar machen:
```yaml
contao:
    mailer:
        transports:
            website1:
                from: email@example.org
            website2:
                from: Lorem Ipsum <email@example.de>
```

**Schritt 3**: Übersetzungen (optional):
```yaml
# translations/mailer_transports.de.yaml
website1: 'SMTP für Webseite 1'
website2: 'SMTP für Webseite 2'
```

### E-Mail testen

```bash
php vendor/bin/contao-console mailer:test \
    --from=sender@example.com \
    --subject=Testmail \
    --body=Testinhalt \
    recipient@example.com
```

### Cache nach Konfigurationsänderungen leeren

```bash
php vendor/bin/contao-console cache:clear --env=prod --no-warmup
php vendor/bin/contao-console cache:warmup --env=prod
```

---

## 5. Systemwartung

### Wartungsmodus

Versetzt die Contao-Installation in den Wartungsmodus:
- Frontend für reguläre Besucher **nicht erreichbar**
- Backend bleibt zugänglich
- Angemeldete Benutzer können den Modus über Frontend-Vorschau umgehen
- Jeder Startpunkt kann einzeln in den Wartungsmodus versetzt werden

**Einsatzzweck**: Größere Backend-Umbauarbeiten, wenn Frontend-Änderungen noch nicht sichtbar sein sollen.

Via CLI:
```bash
php vendor/bin/contao-console contao:maintenance-mode enable
php vendor/bin/contao-console contao:maintenance-mode disable
```

Manuell deaktivieren: Datei `var/maintenance.html` löschen.

### Crawler (Suchindex)

Seiten werden beim Frontend-Aufruf automatisch indiziert. Für manuelle Neuerstellung:

```bash
vendor/bin/contao-console contao:crawl
```

**Domain-Konfiguration für CLI-Aufruf** (da kein HTTP-Kontext vorhanden):
```yaml
# config/parameters.yaml
parameters:
    router.request_context.host: 'example.org'
    router.request_context.scheme: 'https'
```

#### Geschützte Seiten indizieren

```yaml
# config/config.yaml
contao:
    search:
        index_protected: true
```

Ein Frontend-Benutzer mit Zugriff auf geschützte Seiten wird beim Indexaufbau automatisch angemeldet.

#### Crawler beschleunigen

```bash
# Debug-CSV aktivieren
vendor/bin/contao-console contao:crawl --enable-debug-csv

# Gleichzeitige Requests erhöhen
vendor/bin/contao-console contao:crawl --concurrency=10

# Tiefe begrenzen
vendor/bin/contao-console contao:crawl --max-depth=3
```

**Seiten ausschließen**:
- Via `robots.txt` mit `User-Agent: contao/crawler`
- HTML-Attribut: `<a href="..." data-escargot-ignore>` (alle Crawler)
- HTML-Attribut: `<a href="..." data-skip-search-index>` (nur Suchindex)

#### Basic Authentication für Crawler

```yaml
# config/config.yaml
contao:
    crawl:
        default_http_client_options:
            auth_basic: 'benutzername:passwort'
```

### Daten bereinigen

Unter „Daten bereinigen" können manuell bereinigt werden:
- Alte Vorschaubilder
- XML-Sitemaps nach Seitenstruktur-Änderungen
- Suchindex
- Versionsverlauf
- Systemlogs

---

## 6. Vorschau-Links

Vorschau-Links ermöglichen es, Frontend-Vorschauen mit externen Personen zu teilen.

**Erstellung**: In der Frontend-Vorschau auf „URL teilen" klicken.

**Konfigurierbare Optionen:**

| Option | Beschreibung |
|--------|-------------|
| Ziel-URL | Die zu teilende Frontend-Seite |
| Läuft ab nach | 1 Tag, 7 Tage oder 30 Tage |
| Unveröffentlichtes anzeigen | Ob unveröffentlichte Elemente sichtbar sind |
| Aktivieren | Link freischalten/sperren |

Angelegte Links werden unter **System → Vorschau-Links** verwaltet.

---

## 7. Debug-Modus

### Aktivierungsmöglichkeiten

**1. Via Umgebungsvariable** (dauerhaft):
```env
APP_ENV=dev
```
⚠️ **Nie auf Live-Servern verwenden!**

**2. Via Backend** (für aktuellen Benutzer):
- Im Backend auf das Käfer-Icon klicken → setzt Cookie

**3. Via Contao Manager**:
- Systemwartung → Debug-Modus-Schaltfläche

### Vorteile des Debug-Modus

| Feature | Beschreibung |
|---------|-------------|
| Stack Trace | Fehler werden mit vollständigem Stacktrace angezeigt |
| Kein Cache | Seitencache ist deaktiviert |
| Symfony Profiler | Toolbar und Profiler verfügbar |
| Keine Kombinierung | CSS/JS werden einzeln geladen |
| Template-Namen | Als HTML-Kommentare im Quellcode sichtbar |

### Symfony Profiler

Toolbar erscheint am unteren Browser-Rand. Zeigt:
- PHP/Symfony/Contao-Versionen
- VarDumper-Ausgaben
- Speicherauslastung
- Datenbankabfragen und -zeiten
- Benutzerinformationen
- Fehler, Warnungen, Deprecations

Logs: `var/logs/`
