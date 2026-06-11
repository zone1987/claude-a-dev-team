# shopware-cli project — Vollständige Referenz

## project create

Neues Shopware 6 Projekt anlegen. Interaktiv wenn ohne Flags aufgerufen.

```bash
# Interaktiv
shopware-cli project create

# Mit allen Flags
shopware-cli project create my-shop latest \
  --git \
  --docker \
  --with-elasticsearch \
  --with-amqp \
  --deployment shopware-paas \
  --ci github
```

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--docker` | false | Docker für composer install verwenden |
| `--with-elasticsearch` | false | OpenSearch/Elasticsearch-Support einschließen |
| `--with-amqp` | false | AMQP Queue (symfony/amqp-messenger) einschließen |
| `--no-audit` | false | `composer audit` nicht blockierend |
| `--git` | false | git-Repository initialisieren |
| `--version string` | | SW-Version: `6.6.0.0`, `6.7.0.0`, `latest` |
| `--deployment string` | | `none` \| `deployer` \| `platformsh` \| `shopware-paas` |
| `--ci string` | | `none` \| `github` \| `gitlab` |

**Deployment-Optionen:**
- `shopware-paas` → installiert `shopware/paas-meta` Recipe (Platform.sh-Konfig)
- `platformsh` → allgemeine Platform.sh-Konfig
- `deployer` → Deployer PHP-Konfiguration
- `none` → keine Deployment-Konfig

## project ci

Vollständige CI/CD-Build-Pipeline für Produktions-Deployments:
1. `composer install --no-dev --optimize-autoloader`
2. Extension-Assets bauen (Admin + Storefront)
3. Symfony-Cache warmup
4. `assets:install`
5. MJML kompilieren (falls vorhanden)
6. Checksums generieren

```bash
shopware-cli project ci .
shopware-cli project ci . --with-dev-dependencies
shopware-cli project ci . --force   # außerhalb CI
```

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--with-dev-dependencies` | false | `require-dev` behalten |
| `--force` | false | Auch außerhalb CI / bei dirty git tree ausführen |

**Umgebungsvariablen die `project ci` liest:**
- `APP_CACHE_DIR` — Cache-Verzeichnis (Standard: `var/cache`)
- `SHOPWARE_SKIP_ASSET_INSTALL_CACHE_INVALIDATION=1` — Cache-Invalidierung beim Build überspringen (PaaS-Optimierung)
- `CI` — Muss gesetzt sein (oder `--force` nutzen)

## project admin-build / storefront-build

```bash
# Nur Admin
shopware-cli project admin-build .
shopware-cli project admin-build . --only-extensions MyPlugin,OtherPlugin
shopware-cli project admin-build . --skip-extensions LegacyPlugin

# Nur Storefront + theme:compile
shopware-cli project storefront-build .
shopware-cli project storefront-build . --skip-theme-compile
shopware-cli project storefront-build . --force-install-dependencies
```

**admin-build Flags:**

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--skip-assets-install` | false | `assets:install` danach nicht ausführen |
| `--force-install-dependencies` | false | npm install erzwingen |
| `--only-extensions string` | | Kommagetrennte Extension-Liste |
| `--skip-extensions string` | | Ausschlussliste |
| `--only-custom-static-extensions` | false | Nur `custom/static-plugins` |

**storefront-build zusätzliche Flags:**

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--skip-theme-compile` | false | `theme:compile` überspringen |

## project worker

Messenger-Consumer starten. Auto-Restart bei Absturz (rate-limited: 1 Neustart/10s).
SIGTERM/SIGINT führen zu Graceful Stop.

```bash
# 1 Worker
shopware-cli project worker

# 3 Worker parallel
shopware-cli project worker 3

# Custom Queues
shopware-cli project worker --queue async,low_priority 2

# Mit Graceful Stop (60s warten vor SIGKILL)
shopware-cli project worker --graceful-stop-limit 60

# Verboses Logging
shopware-cli project worker --verbose
```

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--verbose` | false | `-vvv` für alle Worker |
| `--queue string` | `async,failed,low_priority` (SW>=6.5.7) | Kommagetrennte Queue-Namen |
| `--memory-limit string` | `512M` | Memory-Limit pro Worker-Run |
| `--time-limit string` | `120` | Zeit-Limit pro Worker-Run (Sekunden) |
| `--graceful-stop-limit uint` | 0 | Sekunden für Graceful SIGTERM vor SIGKILL (0=sofort) |
| `--limit uint` | 0 | Max. Messages pro Worker-Run (0=unbegrenzt) |

## project dump

Pure-Go MySQL-Dumper ohne externe `mysqldump`-Binary.

```bash
# Einfach (DATABASE_URL aus .env)
shopware-cli project dump

# Mit Anonymisierung und Kompression
shopware-cli project dump --clean --anonymize --compression gzip

# Auf stdout (Pipeline)
shopware-cli project dump --output -

# Explizite Verbindungsdaten
shopware-cli project dump -u shopware -p shopware --host localhost --database shopware

# Parallel (5 Tabellen gleichzeitig)
shopware-cli project dump --parallel 5

# Komprimiert mit zstd
shopware-cli project dump --compression zstd --output dump.sql.zst
```

| Flag | Kurz | Default | Beschreibung |
|------|------|---------|--------------|
| `--host` | | (aus DATABASE_URL) | MySQL-Host |
| `--database` | | (aus DATABASE_URL) | Datenbankname |
| `--username` | `-u` | (aus DATABASE_URL) | MySQL-User |
| `--password` | `-p` | (aus DATABASE_URL) | MySQL-Passwort |
| `--port` | | (aus DATABASE_URL) | MySQL-Port |
| `--output` | | `dump.sql` | Ausgabedatei oder `-` für stdout |
| `--clean` | | false | Tabellen überspringen: `cart`, `messenger_messages`, `message_queue_stats`, `dead_message`, `increment`, `log_entry`, `sales_channel_api_context` |
| `--skip-lock-tables` | | false | `LOCK TABLES` überspringen (nötig für limitierte Berechtigungen) |
| `--anonymize` | | false | Kundendaten anonymisieren: E-Mail, Name, Adresse, etc. |
| `--compression` | | | `gzip` (Datei bekommt `.gz`) \| `zstd` (Datei bekommt `.zst`) |
| `--quick` | | false | Quick-Option (deaktiviert row-by-row Buffer) |
| `--parallel` | | 0 | Tabellen parallel dumpen (0=sequentiell) |
| `--insert-into-limit` | | 0 | Max. Rows pro INSERT-Statement (0=kein Limit) |

## project console

Passthrough zu `bin/console`. Flag-Parsing deaktiviert (alle Argumente werden direkt übergeben).
Tab-Completion für alle Symfony Console-Commands verfügbar.

```bash
shopware-cli project console cache:clear
shopware-cli project console plugin:install --activate MyPlugin
shopware-cli project console system:install --shop-name "My Shop" --shop-email info@example.com
```

## project extension (via Admin API)

Erfordern konfigurierte Admin-API in `.shopware-project.yml`.

```bash
# Extensions listen
shopware-cli project extension list
shopware-cli project extension list --json

# Lifecycle
shopware-cli project extension install MyPlugin
shopware-cli project extension install --activate MyPlugin
shopware-cli project extension activate MyPlugin
shopware-cli project extension deactivate MyPlugin
shopware-cli project extension uninstall MyPlugin
shopware-cli project extension delete MyPlugin

# Updates
shopware-cli project extension update MyPlugin
shopware-cli project extension update all
shopware-cli project extension outdated
shopware-cli project extension outdated --json

# Lokale Extension hochladen
shopware-cli project extension upload path/to/MyPlugin --activate
shopware-cli project extension upload path/to/MyPlugin --increase-version
```

## project admin-api

```bash
# GET-Request
shopware-cli project admin-api GET /api/product?limit=5

# POST-Request
shopware-cli project admin-api POST /api/product \
  '{"name": "Test", "productNumber": "TEST-001", "stock": 10}'

# Nur Token ausgeben (für curl-Pipelines)
shopware-cli project admin-api GET /api/product --output-token
```

## project doctor

Diagnose ohne Side-Effects:
- `.shopware-project.yml` lesen und validieren
- Shopware-Version erkennen
- Alle Extensions und Bundles auflisten
- Potenzielle Probleme berichten

```bash
shopware-cli project doctor .
```

## project validate

```bash
shopware-cli project validate .
shopware-cli project validate . --reporter github
shopware-cli project validate . --only phpstan
shopware-cli project validate . --local-only   # nur custom/*
```

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--reporter string` | auto | `summary` \| `json` \| `github` \| `gitlab` \| `junit` \| `markdown` |
| `--only string` | | Kommagetrennte Tool-Liste |
| `--exclude string` | | Tools ausschließen |
| `--no-copy` | false | Kein tmp-Dir |
| `--local-only` | false | Nur `custom/*`-Ordner scannen |

## project autofix

```bash
# composer-based Plugins zu Composer/Packagist migrieren
shopware-cli project autofix composer-plugins

# Zu Symfony Flex migrieren
shopware-cli project autofix flex
```

`autofix flex` modifiziert:
- `composer.json`: Flex-Endpoint hinzufügen, Scripts anpassen
- `.env`: Flex-kompatible Struktur
- `config/`: Aufräumen nach Recipe-Pattern

## project generate-jwt

```bash
# Dateien schreiben: config/jwt/private.pem + config/jwt/public.pem
shopware-cli project generate-jwt .

# Als Env-Vars ausgeben (für CI/Secrets)
shopware-cli project generate-jwt . --env
# → JWT_PRIVATE_KEY=<base64>
# → JWT_PUBLIC_KEY=<base64>
```

## project image-proxy

Lokaler Proxy für Entwicklung mit Produktions-Medien. Serviert Images aus lokalem `public/`,
leitet Misses an Upstream weiter und cached Responses.

```bash
shopware-cli project image-proxy --url https://production.example.com
shopware-cli project image-proxy --url https://production.example.com --port 8081
shopware-cli project image-proxy --url https://production.example.com --clear
```

Erstellt beim Start eine temporäre Shopware-Filesystem-Konfig und entfernt sie beim Beenden.

## project upgrade-check

```bash
shopware-cli project upgrade-check .
# → Interaktive Versionsauswahl
# → Listet inkompatible Extensions mit Details
```

Nutzt Admin-API wenn konfiguriert, sonst `composer.lock` für Versionsanalyse.

## project config-schema

```bash
shopware-cli project config-schema > shopware-project-schema.json
```

## project clear-cache

```bash
shopware-cli project clear-cache
# → Nutzt Admin-API wenn konfiguriert
# → Fallback: var/cache löschen
```
