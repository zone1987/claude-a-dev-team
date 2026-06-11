# shopware-cli — Alle Commands (erschöpfend)

Quelle: `github.com/shopware/shopware-cli` (Go, v0.6.x). Analysiert aus `cmd/` und `internal/`.

## Globale Flags (persistent, alle Commands)

| Flag | Kurz | Default | Beschreibung |
|------|------|---------|--------------|
| `--verbose` | | false | Debug-Ausgabe aktivieren |
| `--no-interaction` | `-n` | false | Alle interaktiven Fragen deaktivieren (CI-safe) |
| `--version` | | | Version ausgeben und beenden |

---

## account

### `account login`
OIDC/OAuth2 Browser-Flow gegen Shopware Account.
Keine zusätzlichen Flags.

### `account logout`
Lokalen Token-Cache invalidieren.
Keine Flags.

### `account producer extension list`
Alle eigenen Store-Extensions auflisten.

| Flag | Beschreibung |
|------|--------------|
| `--search string` | Ergebnisse nach Name filtern |

### `account producer extension info pull [path]`
Store-Informationen (Beschreibung HTML, Installation Manual, Images, Icon) aus Shopware Account in lokales `.shopware-extension.yml` und `src/Resources/store/` ziehen.

Kein zusätzlicher Flag.

### `account producer extension info push [zip-oder-path]`
Lokale Store-Infos (`.shopware-extension.yml`, `src/Resources/store/`) in Shopware Account hochladen.

Kein zusätzlicher Flag.

### `account producer extension upload [zip]`
Extension-Zip in Store hochladen, Code-Review triggern.

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--skip-for-review-result` | false | Nicht auf Code-Review-Ergebnis warten |

---

## extension

### `extension admin-watch [path...] [host]`
ESBuild Dev-Proxy für Shopware Administration. Compiliert Extensions live und proxied den Admin.

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--listen string` | `:8080` | Listen-Adresse (host:port) |
| `--external-url string` | | Externe URL (Reverse-Proxy-Setup) |

### `extension build [path...]`
Admin- und Storefront-JS/CSS-Assets für eine oder mehrere Extensions bauen.
ESBuild/Webpack je nach Extension-Typ. Respektiert `SHOPWARE_PROJECT_ROOT` für Versionseinschränkungen.
Keine Flags.

### `extension get-changelog [path]`
Extension-Changelog auf stdout ausgeben.

| Flag | Beschreibung |
|------|--------------|
| `--language string` | Sprachkey, kommagetrennte Fallback-Liste (z.B. `de_DE,en_GB`) |

### `extension config-schema`
JSON-Schema für `.shopware-extension.yml` auf stdout. Keine Flags.

### `extension fix [path]`
Code-Fixer ausführen: PHPCSFixer, ESLint autofix, etc. Benötigt git-Repository.

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--only string` | | Nur bestimmte Tools ausführen (kommagetrennt: `phpstan,eslint`) |
| `--allow-non-git` | false | Auch ohne git-Repo ausführen |

### `extension format [path]`
Formatter ausführen: Prettier, PHP-CS-Fixer, etc.

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--only string` | | Nur bestimmte Tools |
| `--dry-run` | false | Nur melden, nicht anwenden |

### `extension get-name [path]`
Technical Name der Extension ausgeben (aus Ordner oder Zip). Keine Flags.

### `extension get-version [path]`
Version der Extension ausgeben (aus Ordner oder Zip). Keine Flags.

### `extension prepare [path]`
Composer-Dependencies installieren + Aufräumen als Vorbereitung für Zip-Erstellung.
Läuft dieselbe Pre-Zip-Pipeline wie `extension zip`. Keine Flags.

### `extension validate [path]`
Extension validieren. Standard: nur schnelle shopware-cli-eigene Checks.

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--full` | false | PHPStan, ESLint, Stylelint, PHP-CS-Fixer, Rector, Prettier, Twig mitausführen |
| `--store-compliance` | false | Store-Compliance-Checks erzwingen (ignoriert custom ignore lists) |
| `--reporter string` | auto | Ausgabeformat: `summary`, `json`, `github`, `gitlab`, `junit`, `markdown` |
| `--check-against string` | `highest` | Shopware-Version: `highest` oder `lowest` |
| `--only string` | | Nur bestimmte Tools |
| `--exclude string` | | Tools ausschließen |
| `--no-copy` | false | Extension nicht in tmp-Dir kopieren |

### `extension zip [path] [branch]`
Release-Zip aus Extension-Ordner erstellen. Standardmäßig via git-Export.

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--disable-git` | false | Quellordner direkt verwenden (kein git-Export) |
| `--release` | false | Release-Modus (entfernt App-Backend-Secret) |
| `--overwrite-app-backend-url string` | | Backend-URL in `manifest.xml` ersetzen |
| `--overwrite-app-backend-secret string` | | App-Secret in `manifest.xml` ersetzen |
| `--overwrite-version string` | | Version in Zip überschreiben |
| `--use-git-tag-as-version` | false | Erkannten git-Tag als Version verwenden |
| `--output-directory string` | | Ausgabe-Verzeichnis für Zip |
| `--git-commit string` | | Bestimmten Commit/Tag exportieren |
| `--filename string` | | Expliziter Zip-Dateiname (Standard: `<name>-<tag>.zip`) |

---

## project

### `project admin-api [method] [path]`
Authentifizierter Admin-REST-API-Wrapper. Liest Credentials aus `.shopware-project.yml`.

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--output-token` | false | Nur Bearer-Token ausgeben |
| `--no-default-headers` | false | Kein `Content-Type`/`Accept: application/json` |

### `project admin-build [project-dir]` (alias: `build-admin`)
Admin-JS/CSS für alle Extensions bauen.

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--skip-assets-install` | false | `assets:install` danach nicht ausführen |
| `--force-install-dependencies` | false | npm install erzwingen (auch wenn `node_modules` existiert) |
| `--only-extensions string` | | Kommagetrennte Extension-Liste |
| `--skip-extensions string` | | Kommagetrennte Ausschlussliste |
| `--only-custom-static-extensions` | false | Nur `custom/static-plugins` |

### `project admin-watch [path]` (alias: `watch-admin`)
Admin webpack Dev-Server starten.

| Flag | Beschreibung |
|------|--------------|
| `--only-extensions string` | Extensions filtern |
| `--skip-extensions string` | Extensions ausschließen |
| `--only-custom-static-extensions bool` | Nur `custom/static-plugins` |

### `project autofix composer-plugins`
Generiert `composer require`-Kommandos, um Plugins aus `custom/plugins` zu Composer/Packagist zu migrieren. Interaktiv.

### `project autofix flex`
Migriert Projekt von manuellem Layout zu Symfony Flex. Ändert `composer.json` und `.env`. Interaktive Bestätigung.

### `project ci [project-dir]`
Vollständige CI-Build-Pipeline: composer install, Extension-Assets, Cache warmup, Assets install, MJML, Checksums.

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--with-dev-dependencies` | false | `require-dev` in composer install behalten |
| `--force` | false | Auch außerhalb CI / dirty git tree ausführen |

### `project clear-cache`
Shopware-Cache leeren. Nutzt Admin-API wenn konfiguriert, sonst `var/cache` löschen. Keine Flags.

### `project config init`
`.shopware-project.yml` interaktiv anlegen. Keine Flags (benötigt Interaction).

### `project config-schema`
JSON-Schema für `.shopware-project.yml` auf stdout. Keine Flags.

### `project console [args...]`
`bin/console`-Passthrough. Flag-Parsing auf CLI-Seite deaktiviert. Tab-Completion für alle Console-Commands.

### `project create [name] [version]`
Neues Shopware 6 Projekt erstellen.

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--docker` | false | Docker für composer install verwenden |
| `--with-elasticsearch` | false | OpenSearch/ES-Support einschließen |
| `--with-amqp` | false | AMQP Queue (symfony/amqp-messenger) einschließen |
| `--no-audit` | false | `composer audit` nicht blockierend |
| `--git` | false | git-Repository initialisieren |
| `--version string` | | SW-Version: `6.6.0.0`, `latest`, etc. |
| `--deployment string` | | Deployment: `none`, `deployer`, `platformsh`, `shopware-paas` |
| `--ci string` | | CI-System: `none`, `github`, `gitlab` |

### `project doctor [project-dir]`
Projekt auf Probleme prüfen: Config lesen, SW-Version erkennen, Extensions/Bundles auflisten. Keine Flags.

### `project dump`
MySQL-Datenbank dumpen. Auto-detect `DATABASE_URL` aus `.env`/`.env.local`.

| Flag | Kurz | Default | Beschreibung |
|------|------|---------|--------------|
| `--host` | | | MySQL-Host |
| `--database` | | | Datenbankname |
| `--username` | `-u` | | MySQL-User |
| `--password` | `-p` | | MySQL-Passwort |
| `--port` | | | MySQL-Port |
| `--output` | | `dump.sql` | Ausgabedatei oder `-` für stdout |
| `--clean` | | false | Cart, messenger_messages, etc. überspringen |
| `--skip-lock-tables` | | false | `LOCK TABLES` überspringen |
| `--anonymize` | | false | Kundendaten anonymisieren |
| `--compression` | | | `gzip` (`.gz`) oder `zstd` (`.zst`) |
| `--quick` | | false | Quick-Option (kein row-by-row buffer) |
| `--parallel` | | 0 | Tabellen parallel dumpen (0=deaktiviert) |
| `--insert-into-limit` | | 0 | Max. Rows pro INSERT |

### `project extension activate [name...]`
Extensions aktivieren (installiert erst wenn nötig). Keine Flags.

### `project extension deactivate [name...]`
Extensions deaktivieren. Keine Flags.

### `project extension delete [name...]`
Extensions deaktivieren, deinstallieren und entfernen. Keine Flags.

### `project extension install [name...]`

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--activate` | false | Direkt nach Install aktivieren |

### `project extension list` (alias: `ls`)

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--json` | false | Als JSON-Array ausgeben |

### `project extension outdated`
Extensions mit verfügbaren Updates auflisten. Exit-Code != 0 wenn veraltete Extensions vorhanden.

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--json` | false | Als JSON-Array ausgeben |

### `project extension uninstall [name...]`
Deaktivieren + Deinstallieren (Dateien bleiben). Keine Flags.

### `project extension update [name... | all]`

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--disable-store-update` | false | Kein Download von store.shopware.com |

### `project extension upload [path]`
Lokale Extension zippen und auf Remote-Shop hochladen.

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--activate` | false | Nach Upload installieren + aktivieren + updaten |
| `--increase-version` | false | Patch-Version vor Upload inkrementieren |

### `project fix [project-dir]`

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--only string` | | Nur bestimmte Tools |
| `--allow-non-git` | false | Ohne git-Repo erlauben |

### `project format [project-dir]`

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--only string` | | Nur bestimmte Tools |
| `--dry-run` | false | Nur melden |

### `project generate-jwt [project-dir]`
2048-Bit RSA-Schlüsselpaar generieren.

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--env` | false | Als `JWT_PRIVATE_KEY`/`JWT_PUBLIC_KEY` env vars ausgeben statt Dateien schreiben |

### `project image-proxy`
Lokaler HTTP-Proxy: serviert Images aus `public/`, Misses werden upstream weitergeleitet und gecached.

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--port string` | `8080` | Port |
| `--url string` | | Upstream-URL |
| `--clear` | false | Cache leeren vor Start |
| `--external-url string` | | Externe URL für generierten SW-Config |
| `--skip-config` | false | Kein Shopware-Filesystem-Config schreiben/entfernen |

### `project storefront-build [path]` (alias: `build-storefront`)

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--skip-assets-install` | false | `assets:install` überspringen |
| `--skip-theme-compile` | false | `theme:compile` überspringen |
| `--force-install-dependencies` | false | npm install erzwingen |
| `--only-extensions string` | | Extensions filtern |
| `--skip-extensions string` | | Extensions ausschließen |
| `--only-custom-static-extensions` | false | Nur `custom/static-plugins` |

### `project storefront-watch [path]` (alias: `watch-storefront`)
Storefront webpack Hot-Proxy.

| Flag | Beschreibung |
|------|--------------|
| `--only-extensions string` | Extensions filtern |
| `--skip-extensions string` | Extensions ausschließen |
| `--only-custom-static-extensions bool` | Nur `custom/static-plugins` |

### `project upgrade-check`
Extensions auf Kompatibilität mit zukünftiger SW-Version prüfen (interaktiv, Versionsauswahl). Keine Flags.

### `project validate [project-dir]`

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--reporter string` | auto | `summary`, `json`, `github`, `gitlab`, `junit`, `markdown` |
| `--only string` | | Nur bestimmte Tools |
| `--exclude string` | | Tools ausschließen |
| `--no-copy` | false | Kein tmp-Dir |
| `--local-only` | false | Nur `custom/*`-Ordner scannen |

### `project worker [amount]`
Messenger-Consumer starten. Restart bei Fehler (rate-limited: 1x/10s). SIGTERM/SIGINT-safe.

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--verbose` | false | `-vvv` für worker |
| `--queue string` | | Kommagetrennte Queue-Namen (Standard: `async,failed,low_priority` für SW >=6.5.7) |
| `--memory-limit string` | `512M` | Memory-Limit pro Worker |
| `--time-limit string` | `120` | Zeit-Limit pro Worker-Run (Sekunden) |
| `--graceful-stop-limit uint` | 0 | Sekunden für Graceful SIGTERM vor SIGKILL |
| `--limit uint` | 0 | Max. Messages pro Worker-Run |
