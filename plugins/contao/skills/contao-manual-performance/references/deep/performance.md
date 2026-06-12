# Contao 5.x — Performance

Quellen:
- https://docs.contao.org/5.x/manual/de/performance/
- https://docs.contao.org/5.x/manual/de/performance/cronjobs/
- https://docs.contao.org/5.x/manual/de/performance/http-caching/
- https://docs.contao.org/5.x/manual/de/performance/php-setup/

---

## Übersicht

Performance hängt von mehreren Infrastrukturfaktoren ab: Webserver (Apache, Nginx, LiteSpeed), Betriebssystem und Speicherlösung (HDD vs. SSD). Es gibt keine universell perfekte Konfiguration für Contao. Dieses Kapitel ist eine Sammlung bewährter Praktiken.

---

## 1. Cronjob-Framework

### Grundprinzip

Contao enthält ein integriertes Cronjob-Framework, das Entwicklern eine einheitliche Registrierung von Cronjobs für Erweiterungen ermöglicht.

**Standardverhalten**: Cronjobs werden bei jedem Websitebesuch ausgeführt → kann Performance beeinträchtigen.

**Empfehlung**: Echte Server-Cronjobs einrichten.

**Wichtig**: Nicht alle registrierten Jobs laufen bei Websitebesuchen. Die Backend-Suchindexierung erfolgt **ausschließlich über einen echten CLI-Cronjob**.

### Konfiguration

Das Framework benötigt nur **einen minütlich ausgeführten Cronjob**, der alle registrierten Aufgaben verwaltet:

```cron
* * * * * <php-binary> <contao-verzeichnis>/vendor/bin/contao-console contao:cron
```

**Praktisches Beispiel (Plesk)**:
```cron
* * * * * /opt/plesk/php/8.2/bin/php /var/www/vhosts/my.host.com/vendor/bin/contao-console contao:cron
```

---

## 2. HTTP-Caching

### Grundprinzip

Contao nutzt HTTP-Standards für Caching. Das System arbeitet mit einem **integrierten Cache-Proxy**, der Antworten basierend auf HTTP-Headern zwischenspeichert. Das System funktioniert „out-of-the-box" mit guten Standardwerten.

### Wichtige Cache-Control-Header

| Header | Beschreibung |
|--------|-------------|
| `private` | Nur Browser darf cachen |
| `public` | Browser und Proxies dürfen cachen |
| `max-age` | Cache-Dauer in Sekunden (private Clients) |
| `s-maxage` | Cache-Dauer für öffentliche Caches |

**Beispiel**:
```
Cache-Control: max-age=3600, s-maxage=7200, public
```
→ Private Clients: 1 Stunde, öffentliche Caches: 2 Stunden

### Cache-Status-Indikatoren

Der `Contao-Cache`-Header zeigt den Cache-Status:

| Wert | Bedeutung |
|------|-----------|
| `miss` | Kein Cache-Eintrag; Contao wird ausgeführt |
| `miss/store` | Neuer Cache-Eintrag wird gespeichert |
| `fresh` | Antwort kommt aus dem Cache |

### Wann wird Caching deaktiviert (private)?

Das System erzwingt `Cache-Control: private`, wenn:
- `Authorization`-Header vorhanden (Authentifizierung)
- PHP-Session aktiv
- Response-Cookies gesetzt werden
- Relevante Request-Cookies vorhanden sind

### Cookie-Management

Contao ignoriert standardmäßig irrelevante Cookies (z.B. `_ga_*`, `_pk_*`) und ermöglicht so bessere Cache-Quoten.

Konfiguration via Umgebungsvariablen:
```env
COOKIE_ALLOW_LIST=PHPSESSID,csrf_https-contao_csrf_token,csrf_contao_csrf_token,trusted_device,REMEMBERME
COOKIE_REMOVE_FROM_DENY_LIST=__utm.+,AMP_TOKEN
```

### Cache-Tagging

Antworten erhalten intern `X-Cache-Tags` mit Referenzen zu Datenbankeinträgen. Bei Änderungen invalidiert Contao automatisch alle betroffenen Cache-Einträge — präzise Invalidierung statt komplettes Cache-Leeren.

### Query-Parameter optimieren

Tracking-Parameter wie `utm_*` deaktivieren das Caching. Lösung:
```env
QUERY_PARAMS_REMOVE_FROM_DENY_LIST=fbclid
```

⚠️ **Warnung**: Cache-Control deaktivieren, wenn Parameter aktiv genutzt werden.

### Konfigurationsempfehlungen

- Shared-Cache-Dauer ≥ Private-Cache-Dauer setzen
- Häufig geänderte Inhalte: niedrigere Werte
- Statische Inhalte: höhere Werte möglich

---

## 3. PHP-Setup

### PHP-Version

Stets die neueste von Contao unterstützte PHP-Version verwenden — jede Version bringt Leistungsverbesserungen.

| Contao-Version | Mindest-PHP |
|----------------|-------------|
| 5.7+ | PHP 8.3 |
| 5.5+ | PHP 8.2 |
| 5.0+ | PHP 8.1 |

### SAPI (Server API)

Die Server-API bestimmt, wie PHP mit dem Webserver kommuniziert.

**Empfehlung**: `fpm (php-fpm)` — einzige SAPI mit Unterstützung für `fastcgi_finish_request()`. Dies ermöglicht Contao, Aufräumarbeiten **nach** dem Senden der Antwort zu erledigen → verkürzte Antwortzeit für Besucher.

| SAPI | Empfehlung |
|------|-----------|
| `fpm` (php-fpm) | ✅ Empfohlen |
| `litespeed` | ✅ Gut |
| `mod_php` | ⚠️ Akzeptabel |
| `cgi` | ❌ Nicht empfohlen |

### OPcache

OPcache ist der **größte einzelne Leistungsgewinn** für PHP-Anwendungen.

**Wie PHP ohne OPcache arbeitet**:
1. Lexing: Quellcode in Tokens zerlegen
2. Parsing: Token-Mengen verstehen
3. Compilation: PHP-Code in Bytecode übersetzen
4. Execution: Bytecode ausführen

OPcache speichert den Bytecode nach Schritt 3 im RAM oder Dateisystem. Bei weiteren Requests wird Schritt 4 direkt ausgeführt — Schritte 1–3 entfallen.

**Empfohlene php.ini-Konfiguration:**

```ini
; Maximaler RAM für OPcache (in MB)
opcache.memory_consumption = 128

; Maximale Anzahl gecachter Dateien
opcache.max_accelerated_files = 20000

; Interne String-Tabelle (für Frameworks wie Symfony empfohlen: 32–64 MB)
opcache.interned_strings_buffer = 32

; Dateiänderungen NICHT automatisch prüfen (bessere Performance)
; Manuelles Leeren bei Deployment erforderlich!
opcache.validate_timestamps = 0
```

**OPcache leeren:**
- Contao Manager → Systemwartung
- Deployment-Tools (cachetool, smart-core/accelerator-cache-bundle)

**Hinweis**: CLI- und Web-Prozesse teilen keinen Bytecode-Cache — CLI-seitiges Leeren reicht nicht.

### Realpath Cache

PHP cached Dateisystem-Informationen (`stat()`-Aufrufe) innerhalb eines Prozesses. Diese Aufrufe sind relativ kostspielig.

**Empfohlene Konfiguration:**

```ini
realpath_cache_size = 4096K
realpath_cache_ttl = 600
```

⚠️ **Warnung**: Wenn `open_basedir` aktiviert ist, deaktiviert PHP den Realpath Cache zur Laufzeit! Viele Hoster nutzen `open_basedir` als Sicherheitsmaßnahme — dies wirkt sich negativ auf die Performance aus.

---

## Zusammenfassung: Optimierungsschritte

| Maßnahme | Aufwand | Wirkung |
|---------|---------|---------|
| Echten Cronjob einrichten | Niedrig | Mittel |
| PHP-Version aktualisieren | Mittel | Hoch |
| `php-fpm` verwenden | Mittel | Mittel |
| OPcache konfigurieren | Niedrig | Sehr hoch |
| `opcache.validate_timestamps=0` | Niedrig | Hoch |
| Realpath Cache erhöhen | Niedrig | Mittel |
| Cookie-Management | Mittel | Hoch (Cache-Trefferquote) |
| SSD statt HDD | Hoch | Hoch |
