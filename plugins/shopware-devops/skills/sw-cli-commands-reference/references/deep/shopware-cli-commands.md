# shopware-cli — Vollständige Befehls-Referenz

Alle Befehle des offiziellen Shopware CLI (`github.com/shopware/shopware-cli`).
Quelle: Shopware Developer Documentation (Produkt-Bereich `tools/cli`, Stand 2026).

---

## Installation

### macOS / Linux (Homebrew)
```bash
brew install --cask shopware/tap/shopware-cli
```

### Debian / Ubuntu (APT)
```bash
curl -1sLf 'https://dl.cloudsmith.io/public/friendsofshopware/stable/setup.deb.sh' | sudo -E bash
sudo apt install shopware-cli
```

### Fedora / CentOS / RHEL (YUM/DNF)
```bash
curl -1sLf 'https://dl.cloudsmith.io/public/friendsofshopware/stable/setup.rpm.sh' | sudo -E bash
sudo dnf install shopware-cli
```

### Arch Linux (AUR)
```bash
yay -S shopware-cli-bin
```

### Nix
```bash
nix profile install nixpkgs#shopware-cli
# oder aus FriendsOfShopware:
nix profile install github:FriendsOfShopware/nur-packages#shopware-cli
```

### Docker (Binary-Copy in eigenes Image)
```dockerfile
COPY --from=ghcr.io/shopware/shopware-cli:bin /shopware-cli /usr/local/bin/shopware-cli
```

### Docker (direkte Nutzung)
```bash
docker run --rm -v $(pwd):$(pwd) -w $(pwd) -u $(id -u) \
  ghcr.io/shopware/shopware-cli extension build FroshPlatformAdminer
```

### GitHub Actions
```yaml
- name: Install shopware-cli
  uses: shopware/shopware-cli-action@v3
```

### GitLab CI
```yaml
build:
  image:
    name: ghcr.io/shopware/shopware-cli:latest
    entrypoint: ["/bin/sh", "-c"]
  script:
    - shopware-cli --version
```

### Aus Source (Go 1.20+)
```bash
git clone https://github.com/shopware/shopware-cli
cd shopware-cli
go mod tidy
go build -o shopware-cli .
```

---

## Globale Flags

| Flag | Kurz | Default | Beschreibung |
|------|------|---------|--------------|
| `--verbose` | | `false` | Debug-Ausgabe aktivieren |
| `--no-interaction` | `-n` | `false` | Keine interaktiven Eingaben (CI-safe) |
| `--version` | | | Version ausgeben und beenden |
| `--help` | `-h` | | Hilfe zum Befehl anzeigen |

---

## extension — Extension-Befehle

### `extension build <path>`

Assets einer Extension bauen (Administration + Storefront). Liest die Shopware-Version aus `composer.json` oder `manifest.xml` und nutzt die niedrigste kompatible Version.

```bash
shopware-cli extension build path/to/MyPlugin
```

**Konfiguration via `.shopware-extension.yml`:**
```yaml
build:
  shopwareVersionConstraint: '6.6.9.0'  # Version-Override
  extraBundles:
    - path: src/Foo                      # Zusätzliche Bundles
    - path: src/Bar
      name: BarBundle                    # Optionaler Name-Override
  zip:
    assets:
      enable_es_build_for_admin: true    # ESBuild für Admin (standalone, schneller)
      enable_es_build_for_storefront: true
      npm_strict: true                   # Nur Runtime-Deps installieren
      enabled: true
      before_hooks: []
      after_hooks: []
      disable_sass: false
```

**SHOPWARE_PROJECT_ROOT:** Für vollständige Kontrolle über den Build kann eine bestehende Shopware-Installation verwendet werden:
```bash
SHOPWARE_PROJECT_ROOT=/path/to/shopware shopware-cli extension build path/to/MyPlugin
```

**Bundle-Typ (kein Plugin):** Composer-Type `shopware-bundle` + `shopware-bundle-name` in `extra`:
```json
{
  "type": "shopware-bundle",
  "extra": { "shopware-bundle-name": "MyBundle" }
}
```

---

### `extension zip <path>`

Release-Zip erstellen: kopiert Extension, baut Assets, entfernt unnötige Dateien, erstellt Archiv im aktuellen Verzeichnis.

```bash
shopware-cli extension zip path/to/MyPlugin
shopware-cli extension zip path/to/MyPlugin --disable-git
shopware-cli extension zip path/to/MyPlugin --git-commit abc123
shopware-cli extension zip path/to/MyPlugin --release
shopware-cli extension zip path/to/MyPlugin --overwrite-version=1.0.0
shopware-cli extension zip path/to/MyPlugin --overwrite-app-backend-url=https://example.com
shopware-cli extension zip path/to/MyPlugin --overwrite-app-backend-secret=MySecret
```

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--disable-git` | `false` | Kein Git-Tag verwenden, aktuellen Quellcode nutzen |
| `--git-commit` | | Spezifischen Tag oder Commit angeben |
| `--release` | `false` | Release-Modus: App-Secret entfernen, Changelog generieren |
| `--overwrite-version` | | Version in `composer.json`/`manifest.xml` überschreiben |
| `--overwrite-app-backend-url` | | Alle externen URLs in `manifest.xml` ersetzen |
| `--overwrite-app-backend-secret` | | App-Secret in `manifest.xml` ersetzen |

**Standard:** verwendet letzten git-Tag. `--disable-git` nutzt aktuellen Code.

**Composer-Dependencies (< SW 6.5):** Automatisches `composer install` + Entfernung von Duplikaten.
```yaml
build:
  zip:
    composer:
      enabled: false  # Deaktivieren
```

**Dateien ausschließen:**
```yaml
build:
  zip:
    pack:
      excludes:
        paths:
          - tests/
          - .github/
```

**Checksum-Generierung:** Automatisch. Ausschlüsse konfigurierbar:
```yaml
build:
  zip:
    checksum:
      ignore:
        - src/Resources/config/services.php
```

**Changelog-Generierung (mit `--release`):**
```yaml
changelog:
  enabled: true
  pattern: '^NEXT-\d+'
  variables:
    ticket: '^(NEXT-\d+)\s'
  template: |
    {{range .Commits}}- [{{ .Message }}](https://issues.shopware.com/issues/{{ .Variables.ticket }})
    {{end}}
```

---

### `extension validate <path>`

Extension validieren — nützlich in CI/CD-Pipelines vor dem Release.

```bash
shopware-cli extension validate path/to/MyPlugin
shopware-cli extension validate --full path/to/MyPlugin
shopware-cli extension validate --full path/to/MyPlugin --check-against lowest
shopware-cli extension validate --full path/to/MyPlugin --check-against highest
shopware-cli extension validate --full path/to/MyPlugin --only phpstan
shopware-cli extension validate --full path/to/MyPlugin --only "phpstan,eslint,stylelint"
shopware-cli extension validate --full path/to/MyPlugin --reporter github
```

| Flag | Beschreibung |
|------|--------------|
| `--full` | Alle Tools ausführen (PHPStan, ESLint, Stylelint, ...) |
| `--check-against` | `lowest` oder `highest` — Shopware-Version für Checks |
| `--only` | Spezifische Tools (kommagetrennt) |
| `--reporter` | Ausgabeformat: `summary` (default), `json`, `junit`, `github`, `markdown` |

**Basis-Prüfungen (ohne `--full`):**
- `composer.json` hat `shopware/core`-Requirement
- Extension-Metadaten: `name`, `label` (DE+EN), `description` (DE+EN, 150–185 Zeichen)
- PHP-Linting mit minimaler PHP-Version (7.3, 7.4, 8.1, 8.2 — per WebAssembly, kein lokales PHP nötig)
- `theme.json` Parsing und Assets
- Snippet-Dateien haben identische Schlüssel

**Verfügbare Tools mit `--only`:**

| Tool | Beschreibung |
|------|--------------|
| `phpstan` | PHP statische Analyse |
| `sw-cli` | Shopware CLI eigene Checks |
| `stylelint` | CSS/SCSS Linting |
| `admin-twig` | Admin Twig Template-Checks |
| `php-cs-fixer` | PHP Code Style |
| `prettier` | Code-Formatierung |
| `eslint` | JavaScript/TypeScript Linting |
| `rector` | PHP Code Refactoring |

**Ignores konfigurieren (`.shopware-extension.yaml`):**
```yaml
validation:
  ignore:
    - identifier: 'Shopware.XXXXXX'
    - identifier: 'Shopware.XXXXXX'
      path: 'path/to/file.php'
    - message: 'Some error message'
      path: 'path/to/file.php'
    - message: 'Some error message'
```

**Projekt-Scan (alle Extensions auf einmal):**
```bash
shopware-cli extension validate --full /path/to/project-root
```
Ignores per `.shopware-project.yaml` mit gleicher Syntax.

---

### `extension fix <path>`

Automatisches Refactoring: Rector (PHP), ESLint (JavaScript), Custom Rules (Admin Twig). Ändert Dateien in-place!

```bash
shopware-cli extension fix path/to/MyPlugin
docker run --rm -v "$(pwd)":/ext ghcr.io/shopware/shopware-cli extension fix /ext
```

Shopware-Version für Rector-Regeln: aus `composer.json` → `shopware/core`-Constraint.

---

### `extension format <path>`

Code formatieren: PHP (PHP-CS-Fixer nach Shopware Coding Standard), JavaScript/CSS/SCSS (Prettier), Admin Twig.

```bash
shopware-cli extension format path/to/MyPlugin
shopware-cli extension format path/to/MyPlugin --dry-run
docker run --rm -v "$(pwd)":/ext ghcr.io/shopware/shopware-cli extension format /ext
docker run --rm -v "$(pwd)":/ext ghcr.io/shopware/shopware-cli extension format /ext --dry-run
```

| Flag | Beschreibung |
|------|--------------|
| `--dry-run` | Vorschau ohne Dateiänderungen |

**Konfiguration:** `.php-cs-fixer.dist.php` im Extension-Root (PHP), `.prettierrc` (JS/CSS/SCSS).

---

### `extension admin-watch <path-to-extension> <url-to-shopware>`

Standalone Admin Watcher: injiziert nur geänderte Extension-Dateien in bestehende Admin-Build. Startet in Millisekunden (im Gegensatz zum regulären Watcher).

```bash
shopware-cli extension admin-watch path/to/MyPlugin http://localhost
shopware-cli extension admin-watch path/to/MyPlugin1 path/to/MyPlugin2 http://localhost
shopware-cli extension admin-watch path/to/shopware-project http://localhost  # Auto-Detect
shopware-cli extension admin-watch path/to/MyPlugin http://localhost --listen :9000
shopware-cli extension admin-watch path/to/MyPlugin http://localhost --external-url https://dev.example.com
```

| Flag | Beschreibung |
|------|--------------|
| `--listen` | Port ändern (default: zufällig) |
| `--external-url` | URL für Reverse-Proxy-Setups (SSL etc.) |

Mehrere Extensions: alle Pfade angeben, letztes Argument ist die Shopware-URL.

---

### `extension get-version <path>`

Version der Extension ausgeben.

```bash
shopware-cli extension get-version path/to/MyPlugin
```

---

### `extension get-changelog <path>`

English Changelog der Extension ausgeben.

```bash
shopware-cli extension get-changelog path/to/MyPlugin
```

---

## project — Projekt-Befehle

### `project create <folder-name> [version]`

Neues Shopware-Projekt anlegen.

```bash
shopware-cli project create my-shop
shopware-cli project create my-shop 6.6.0.0
shopware-cli project create my-shop latest     # Neueste Stable
shopware-cli project create my-shop dev-trunk  # Neueste Dev
```

---

### `project ci <path>`

Vollständige CI/CD-Build-Pipeline: `composer install`, Asset-Build (nur fehlende), Bereinigung, Snippet-Merging.

```bash
shopware-cli project ci .
shopware-cli project ci /path/to/shopware --with-dev-dependencies
```

| Flag | Beschreibung |
|------|--------------|
| `--with-dev-dependencies` | Composer Dev-Dependencies ebenfalls installieren |

**Was passiert:**
1. `composer install` (Production-Deps)
2. Fehlende Extension-Assets kompilieren
3. `node_modules` und andere unnötige Dateien löschen
4. Extension-Asset-Quellcode löschen
5. Admin-Snippets mergen

**Private Composer-Repositories:**
```bash
SHOPWARE_PACKAGES_TOKEN=xxx shopware-cli project ci .
# oder
COMPOSER_AUTH='{"http-basic": {...}}' shopware-cli project ci .
```

**Build-Hooks in `.shopware-project.yml`:**
```yaml
build:
  hooks:
    pre:
      - 'echo "Starting build"'
    pre-composer:
      - 'cp .env.ci .env'
    post-composer:
      - 'bin/console secrets:decrypt-to-local --force'
    pre-assets:
      - 'npm install --prefix custom/plugins/MyPlugin'
    post-assets:
      - 'rm -rf node_modules'
    post:
      - 'echo "Build complete"'
```

**Verfügbare Hooks:** `pre`, `pre-composer`, `post-composer`, `pre-assets`, `post-assets`, `post`.
Variable `PROJECT_ROOT` steht in allen Hooks zur Verfügung.

**Vollständige `.shopware-project.yml` Konfiguration:**
```yaml
compatibility_date: '2026-02-11'

build:
  browserslist: 'defaults'
  cleanup_paths:
    - 'node_modules'
  disable_asset_copy: false
  exclude_extensions:
    - 'SwagExample'
  keep_extension_source: false
  keep_source_maps: false
  remove_extension_assets: false
  force_extension_build:
    - name: 'SomePlugin'
  bundles:
    - path: src/MyBundle
    - path: src/MyFancyBundle
      name: MyGreatFancyBundle
  mjml:
    enabled: false
    searchPaths:
      - custom/plugins
      - custom/static-plugins
  hooks:
    pre: []
    post: []
    pre-composer: []
    post-composer: []
    pre-assets: []
    post-assets: []
```

**MJML Email-Template-Kompilierung (ab v0.6.32, mit FroshPlatformTemplateMail):**
```yaml
build:
  mjml:
    enabled: true
    searchPaths:
      - custom/plugins
      - custom/static-plugins
```
Kompiliert `.html.mjml` → `.html.twig` und entfernt die `.mjml`-Dateien.

**Bundles deklarieren (empfohlen via `.shopware-project.yml`):**
```yaml
build:
  bundles:
    - path: src/MyBundle
    - path: src/MyFancyBundle
      name: MyGreatFancyBundle
```

**Docker-Beispiel:**
```dockerfile
#syntax=docker/dockerfile:1.4
FROM ghcr.io/shopware/docker-base:8.3 AS base-image
FROM ghcr.io/shopware/shopware-cli:latest-php-8.3 AS shopware-cli

FROM shopware-cli AS build
ARG SHOPWARE_PACKAGES_TOKEN
ADD . /src
WORKDIR /src
RUN --mount=type=secret,id=composer_auth,dst=/src/auth.json \
    --mount=type=cache,target=/root/.composer \
    --mount=type=cache,target=/root/.npm \
    /usr/local/bin/entrypoint.sh shopware-cli project ci /src

FROM base-image
COPY --from=build --chown=82 --link /src /var/www/html
```

---

### `project admin-build <path>`

Administration-Assets für alle Extensions bauen.

```bash
shopware-cli project admin-build .
shopware-cli project admin-build . --only-custom-static-extensions
```

| Flag | Beschreibung |
|------|--------------|
| `--only-custom-static-extensions` | Nur Extensions in `custom/static-plugins/` bauen |

Entspricht `bin/build-administration.sh`.

---

### `project storefront-build <path>`

Storefront-Assets bauen + `theme:compile`.

```bash
shopware-cli project storefront-build .
shopware-cli project storefront-build . --only-custom-static-extensions
```

| Flag | Beschreibung |
|------|--------------|
| `--only-custom-static-extensions` | Nur Extensions in `custom/static-plugins/` bauen |

Entspricht `bin/build-storefront.sh`.

---

### `project admin-watch <path>`

Admin webpack Dev-Server starten.

```bash
shopware-cli project admin-watch .
shopware-cli project admin-watch . --only-extensions MyPlugin,OtherPlugin
shopware-cli project admin-watch . --skip-extensions ThirdPartyPlugin
```

| Flag | Beschreibung |
|------|--------------|
| `--only-extensions` | Nur bestimmte Extensions watchen (kommagetrennt) |
| `--skip-extensions` | Bestimmte Extensions ausschließen |

Entspricht `bin/watch-administration.sh`.

---

### `project storefront-watch <path>`

Storefront webpack Hot-Reload-Proxy starten.

```bash
shopware-cli project storefront-watch .
```

Entspricht `bin/watch-storefront.sh`.

---

### `project dump [flags]`

MySQL-Dump erstellen (native Go-Implementierung, kein `mysqldump` nötig).

```bash
shopware-cli project dump
shopware-cli project dump --host 127.0.0.1 --username root --password root --database sw6
shopware-cli project dump --clean
shopware-cli project dump --anonymize
shopware-cli project dump --compression=gzip
shopware-cli project dump --compression=zstd
shopware-cli project dump --skip-lock-tables
```

| Flag | Beschreibung |
|------|--------------|
| `--host` | Datenbank-Host |
| `--username` | Datenbank-Benutzer |
| `--password` | Datenbank-Passwort |
| `--database` | Datenbank-Name |
| `--clean` | Log-/temporäre Tabellen ohne Inhalt (cart, log_entry, message_queue_stats, ...) |
| `--anonymize` | Bekannte Benutzerdaten anonymisieren |
| `--compression` | `gzip` oder `zstd` |
| `--skip-lock-tables` | Tabellen-Lock überspringen |

**Daten-Rewriting:**
```yaml
# .shopware-project.yml
dump:
  rewrite:
    customer:
      email: "faker.Internet().Email()"
      firstName: "'Anonymized'"
```

**Tabellen ohne Inhalt:**
```yaml
dump:
  nodata:
    - log_entry
    - dead_message
```

**Tabellen komplett ignorieren:**
```yaml
dump:
  ignore:
    - some_temp_table
```

**WHERE-Clause:**
```yaml
dump:
  where:
    order: 'createdAt > "2024-01-01"'
```

**Standardmäßig bereinigt (`--clean`):** `cart`, `customer_recovery`, `dead_message`, `enqueue`, `messenger_messages`, `increment`, `elasticsearch_index_task`, `log_entry`, `message_queue_stats`, `notification`, `payment_token`, `refresh_token`, `version`, `version_commit`, `version_commit_data`, `webhook_event_log`.

---

### `project worker <amount>`

Mehrere Messenger-Consumer gleichzeitig starten.

```bash
shopware-cli project worker 2
shopware-cli project worker 4
```

Für Production: supervisord oder systemd bevorzugen.

---

### `project clear-cache`

Cache leeren (Shortcut für `bin/console cache:clear`).

```bash
shopware-cli project clear-cache
```

Wenn in `.shopware-project.yml` eine API-Verbindung konfiguriert ist, wird der Remote-Cache geleert.

---

### `project console <command>`

Passthrough zu `bin/console` ohne in das Projekt-Verzeichnis wechseln zu müssen.

```bash
shopware-cli project console cache:clear
shopware-cli project console plugin:list
```

---

### `project admin-api [method] [path]`

Admin-API-Requests mit automatischer JWT-Authentifizierung.

```bash
shopware-cli project admin-api --output-token        # JWT-Token ausgeben
shopware-cli project admin-api GET /_info/version
shopware-cli project admin-api POST /product -d '{"name": "Test"}'
shopware-cli project admin-api GET /order -H "sw-language-id: xxx"
```

| Flag | Beschreibung |
|------|--------------|
| `--output-token` | JWT-Token ausgeben statt Request machen |
| `-d` | Request-Body (wie curl) |
| `-H` | Zusätzliche Header (wie curl) |

---

### `project image-proxy`

Lokalen HTTP-Server starten, der statische Dateien aus `public/` serviert und bei fehlenden Dateien an Upstream-Server weiterleitet (mit Cache).

```bash
shopware-cli project image-proxy
shopware-cli project image-proxy --url https://production.example.com
shopware-cli project image-proxy --port 3000
shopware-cli project image-proxy --clear
shopware-cli project image-proxy --external-url https://dev.example.com
shopware-cli project image-proxy --skip-config
```

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--url` | aus Config | Upstream-Server URL |
| `--port` | `8080` | Listen-Port |
| `--clear` | `false` | Cache vor Start leeren |
| `--external-url` | `http://localhost:{port}` | Externe URL für Shopware-Config (Reverse-Proxy) |
| `--skip-config` | `false` | Shopware-Config-Datei nicht erstellen |

**Konfiguration in `.shopware-project.yml`:**
```yaml
image_proxy:
  url: https://production.example.com
```

**Ablauf:** Lokale `public/`-Dateien → Cache (`var/cache/image-proxy/`) → Upstream-Proxy → Cache speichern.

Erstellt automatisch `config/packages/zzz-sw-cli-image-proxy.yml` und entfernt sie beim Stoppen.

---

### `project extension list`

Alle installierten Extensions via Admin API auflisten.

```bash
shopware-cli project extension list
```

### `project extension install <name>`

Extension installieren.

```bash
shopware-cli project extension install MyPlugin
```

### `project extension uninstall <name>`

Extension deinstallieren.

```bash
shopware-cli project extension uninstall MyPlugin
```

### `project extension update <name>`

Extension aktualisieren.

```bash
shopware-cli project extension update MyPlugin
```

### `project extension outdated`

Extensions mit verfügbaren Updates anzeigen.

```bash
shopware-cli project extension outdated
```

### `project extension upload <zip-path>`

Extension-Zip auf Shopware-Instanz hochladen.

```bash
shopware-cli project extension upload MyPlugin-1.0.0.zip
```

### `project extension delete <name>`

Extension von Shopware-Instanz löschen.

```bash
shopware-cli project extension delete MyPlugin
```

---

### `project autofix flex`

Projekt zu Symfony Flex migrieren (< SW 6.5 → 6.5+). Verschiebt Konfigurationsdateien, aktualisiert `composer.json` und `bin/console`.

```bash
shopware-cli project autofix flex
```

Backup vor Ausführung empfohlen!

---

### `project autofix composer-plugins`

Lokal installierte Plugins zu Composer migrieren (via Shopware Packagist).

```bash
shopware-cli project autofix composer-plugins
```

Benötigt Shopware Packages Token aus dem Shopware Account.

---

### `project fix <path>`

Automatisches Refactoring auf gesamtes Projekt anwenden.

```bash
shopware-cli project fix path/to/project
docker run --rm -v "$(pwd)":/project ghcr.io/shopware/shopware-cli project fix /project
```

---

### `project format <path>`

Code-Formatierung auf gesamtes Projekt anwenden.

```bash
shopware-cli project format path/to/project
shopware-cli project format path/to/project --dry-run
```

---

## account — Account-Befehle

### `account login`

OIDC/OAuth2 Browser-Login bei Shopware Account.

```bash
shopware-cli account login
```

**CI/CD (kein Browser):** Umgebungsvariablen setzen:
```bash
SHOPWARE_CLI_ACCOUNT_CLIENT_ID=xxx
SHOPWARE_CLI_ACCOUNT_CLIENT_SECRET=yyy
```

Client ID und Secret: Shopware Account → Extension Partner → Development → [Generieren].

---

### `account logout`

Lokalen Token-Cache invalidieren.

```bash
shopware-cli account logout
```

---

### `account merchant shop list`

Alle zugänglichen Shops auflisten.

```bash
shopware-cli account merchant shop list
```

---

### `account merchant shop configure-composer <domain>`

Composer-Repository konfigurieren (`auth.json` erstellen + `composer.json` aktualisieren).

```bash
shopware-cli account merchant shop configure-composer my-shop.example.com
```

Tab-Completion für verfügbare Domains unterstützt.

---

### `account producer extension list`

Alle eigenen Store-Extensions auflisten.

```bash
shopware-cli account producer extension list
shopware-cli account producer extension list --search MyPlugin
```

| Flag | Beschreibung |
|------|--------------|
| `--search` | Nach Name filtern |

---

### `account producer extension upload <zip-path>`

Extension-Zip in Shopware Store hochladen + automatischen Code-Review triggern.

```bash
shopware-cli account producer extension upload MyPlugin-1.0.0.zip
shopware-cli account producer extension upload MyPlugin-1.0.0.zip --skip-for-review-result
```

| Flag | Beschreibung |
|------|--------------|
| `--skip-for-review-result` | Nicht auf Code-Review-Ergebnis warten |

**Voraussetzungen:**
- Login via `account login`
- Zip mit allen Assets (via `extension zip --release`)
- `CHANGELOG*.md` in der Zip mit Changelog-Eintrag für neue Version
- Validiert via `extension validate`

Prüft zuerst, ob Version bereits existiert. Kompatibilität aus `composer.json`/`manifest.xml`.

---

### `account producer extension info pull <path>`

Aktuelle Store-Seiten-Daten (Beschreibung, Bilder, Metadaten) in lokales `.shopware-extension.yml` und `src/Resources/store/` herunterladen.

```bash
shopware-cli account producer extension info pull path/to/MyPlugin
```

---

### `account producer extension info push <path>`

Lokale Store-Seiten-Daten (`.shopware-extension.yml`, Bilder) in Shopware Account hochladen.

```bash
shopware-cli account producer extension info push path/to/MyPlugin
```

**Bilder-Konfiguration in `.shopware-extension.yml`:**
```yaml
store:
  images:
    - file: src/Resources/store/screenshot1.png
      priority: 1
      activate:
        de: true
        en: true
      preview:
        de: false
        en: false
  # oder Verzeichnis:
  image_directory: src/Resources/store/images/
  automatic_bugfix_version_compatibility: true
```

**Verzeichnis-Struktur (nach Sprache):**
```
src/Resources/store/images/
├── de/
│   ├── 0.png
│   ├── 1.png
│   └── 2.png  # preview
└── en/
    ├── 0.png
    ├── 1.png
    └── 2.png  # preview
```

---

## Umgebungsvariablen

| Variable | Beschreibung |
|----------|--------------|
| `CI` | CI-Umgebung erkennen |
| `SHOPWARE_CLI_PREVIOUS_TAG` | Vorherigen Git-Tag für Changelog überschreiben |
| `CI_PROJECT_URL` | GitLab CI Projekt-URL für Changelog |
| `SHOPWARE_CLI_NO_SYMFONY_CLI` | Symfony CLI-Nutzung deaktivieren |
| `APP_ENV` | Anwendungsumgebung |
| `SHOPWARE_PROJECT_ROOT` | Shopware-Projekt für Extension-Build verwenden |
| `SHOPWARE_CLI_DISABLE_WASM_CACHE` | WASM-Cache für PHP-Linting deaktivieren |
| `SHOPWARE_PACKAGES_TOKEN` | Token für packages.shopware.com (private Composer-Repos) |
| `COMPOSER_AUTH` | Inhalt von `auth.json` als Umgebungsvariable |
| `SHOPWARE_CLI_ACCOUNT_CLIENT_ID` | CI/CD: Account Client ID |
| `SHOPWARE_CLI_ACCOUNT_CLIENT_SECRET` | CI/CD: Account Client Secret |

---

## Compatibility Date

Beide `.shopware-extension.yml` und `.shopware-project.yml` unterstützen:

```yaml
compatibility_date: '2026-02-11'
```

Aktiviert neue Verhaltensänderungen ab dem angegebenen Datum. Fehlt das Feld, wird `2026-02-11` als Fallback verwendet (mit Warnung).

Format: `YYYY-MM-DD`.

---

## Typische Workflows

### Extension Release (vollständig)

```bash
# 1. Assets bauen
shopware-cli extension build MyPlugin/

# 2. Validieren
shopware-cli extension validate --full MyPlugin/
shopware-cli extension validate --full MyPlugin/ --check-against lowest

# 3. Zip erstellen
shopware-cli extension zip MyPlugin/ --release

# 4. Store-Seite aktualisieren
shopware-cli account login
shopware-cli account producer extension info push MyPlugin/

# 5. Extension hochladen
shopware-cli account producer extension upload MyPlugin-1.0.0.zip
```

### CI/CD mit GitHub Actions

```yaml
- name: Install shopware-cli
  uses: shopware/shopware-cli-action@v3

- name: Build extension
  run: shopware-cli extension build .

- name: Validate extension
  run: shopware-cli extension validate --full . --reporter github

- name: Create zip
  run: shopware-cli extension zip . --release

- name: Upload to Store
  env:
    SHOPWARE_CLI_ACCOUNT_CLIENT_ID: ${{ secrets.SW_CLIENT_ID }}
    SHOPWARE_CLI_ACCOUNT_CLIENT_SECRET: ${{ secrets.SW_CLIENT_SECRET }}
  run: shopware-cli account producer extension upload *.zip
```

### Projekt-Deployment

```bash
shopware-cli project ci /var/www/shopware
```
