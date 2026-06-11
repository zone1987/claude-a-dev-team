# shopware-cli extension — Vollständige Referenz

## extension build

Baut Admin- und Storefront-Assets für eine oder mehrere Extensions.

```bash
shopware-cli extension build path/to/MyPlugin
shopware-cli extension build plugin-a/ plugin-b/ plugin-c/
SHOPWARE_PROJECT_ROOT=/var/www/shop shopware-cli extension build path/to/MyPlugin
```

- Nutzt ESBuild für moderne Extensions, Webpack für Legacy
- `SHOPWARE_PROJECT_ROOT` setzt den Shopware-Kontext für Versionsbestimmung
- Erzeugt Assets unter `src/Resources/public/`

## extension admin-watch

ESBuild-basierter Dev-Proxy für die Shopware Administration. Compiliert Extension-Assets live
und proxied den Shopware Admin zum Browser.

```bash
shopware-cli extension admin-watch path/to/MyPlugin http://localhost
shopware-cli extension admin-watch path/to/MyPlugin http://localhost --listen :9000
shopware-cli extension admin-watch path/to/MyPlugin http://localhost --external-url https://my-tunnel.example.com
```

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--listen string` | `:8080` | Listen-Adresse (host:port) |
| `--external-url string` | | Externe URL (z.B. für ngrok/Reverse-Proxy) |

## extension validate

```bash
# Schnelle Basis-Prüfung
shopware-cli extension validate path/to/MyPlugin

# Vollständige Prüfung (PHPStan Level 8, ESLint, Stylelint, Prettier, Rector, Twig)
shopware-cli extension validate --full path/to/MyPlugin

# Store-Compliance (ignoriert custom ignore lists)
shopware-cli extension validate --full --store-compliance path/to/MyPlugin

# CI-Ausgabe für GitHub Actions
shopware-cli extension validate --full --reporter github path/to/MyPlugin

# Nur gegen niedrigste unterstützte SW-Version prüfen
shopware-cli extension validate --full --check-against lowest path/to/MyPlugin

# Nur PHPStan und ESLint
shopware-cli extension validate --full --only phpstan,eslint path/to/MyPlugin
```

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--full` | false | PHPStan, ESLint, Stylelint, PHP-CS-Fixer, Rector, Prettier, Twig |
| `--store-compliance` | false | Store-Compliance-Checks erzwingen |
| `--reporter string` | auto | `summary` \| `json` \| `github` \| `gitlab` \| `junit` \| `markdown` |
| `--check-against string` | `highest` | SW-Version: `highest` \| `lowest` |
| `--only string` | | Kommagetrennte Tool-Liste |
| `--exclude string` | | Tools ausschließen |
| `--no-copy` | false | Extension nicht in tmp-Dir kopieren |

**Reporter-Auswahl:**
- `auto`: Terminal → `summary`, CI (GitHub Actions) → `github`, CI (GitLab) → `gitlab`
- `github`: Annotations in GitHub Actions
- `gitlab`: Code-Quality-Report für GitLab
- `junit`: JUnit XML für Test-Reports
- `markdown`: Markdown-Tabelle

## extension zip

Erstellt Release-Zip via git-Export (Standard) oder direkt aus dem Quellordner.

```bash
# Standard: git HEAD exportieren
shopware-cli extension zip path/to/MyPlugin

# Ohne git (z.B. für dirty working tree)
shopware-cli extension zip path/to/MyPlugin --disable-git

# Release-Modus (entfernt App-Backend-Secret)
shopware-cli extension zip path/to/MyPlugin --release

# Spezifischen Branch/Tag exportieren
shopware-cli extension zip path/to/MyPlugin v1.2.3

# Git-Tag automatisch als Version verwenden
shopware-cli extension zip path/to/MyPlugin --use-git-tag-as-version

# In bestimmtes Verzeichnis ausgeben
shopware-cli extension zip path/to/MyPlugin --output-directory ./dist/

# App-Backend-URL überschreiben (für Multi-Environment)
shopware-cli extension zip path/to/MyPlugin --overwrite-app-backend-url https://prod.example.com

# Version überschreiben
shopware-cli extension zip path/to/MyPlugin --overwrite-version 2.0.0
```

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--disable-git` | false | Quellordner direkt nutzen, kein git-Export |
| `--release` | false | App-Backend-Secret aus `manifest.xml` entfernen |
| `--overwrite-app-backend-url string` | | Backend-URL in `manifest.xml` ersetzen |
| `--overwrite-app-backend-secret string` | | App-Secret in `manifest.xml` ersetzen |
| `--overwrite-version string` | | Version in Zip überschreiben |
| `--use-git-tag-as-version` | false | Erkannten git-Tag als Version verwenden (inkompatibel mit `--disable-git` und `--overwrite-version`) |
| `--output-directory string` | | Ausgabe-Verzeichnis |
| `--git-commit string` | | Bestimmten Commit-Hash oder Tag exportieren |
| `--filename string` | | Expliziter Dateiname (Standard: `<Name>-<tag>.zip`) |

**Zip-Inhalt-Kontrolle:**
Die Dateien die in den Zip kommen werden durch `.gitignore` und `.shopware-extension.yml` `excluded_paths` gesteuert.

## extension fix

```bash
shopware-cli extension fix path/to/MyPlugin
shopware-cli extension fix --only phpcs,eslint path/to/MyPlugin
shopware-cli extension fix --allow-non-git path/to/MyPlugin
```

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--only string` | | Kommagetrennte Tool-Liste (`phpstan`, `eslint`, `phpcs`, etc.) |
| `--allow-non-git` | false | Auch ohne git-Repo ausführen |

Benötigt git-Repository (prüft auf staged/unstaged Changes für Safety).

## extension format

```bash
shopware-cli extension format path/to/MyPlugin
shopware-cli extension format --dry-run path/to/MyPlugin
shopware-cli extension format --only prettier path/to/MyPlugin
```

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--only string` | | Kommagetrennte Tool-Liste |
| `--dry-run` | false | Nur Diff anzeigen, nicht anwenden |

## extension prepare

Pre-Zip-Pipeline ohne Zip-Erstellung: Composer-Deps installieren, Dev-Files entfernen.

```bash
shopware-cli extension prepare path/to/MyPlugin
```

Keine Flags. Nützlich für Custom-Zip-Pipelines.

## extension get-name / get-version

```bash
shopware-cli extension get-name path/to/MyPlugin    # → MyPlugin
shopware-cli extension get-version path/to/MyPlugin  # → 1.2.3
shopware-cli extension get-name MyPlugin-1.2.3.zip
shopware-cli extension get-version MyPlugin-1.2.3.zip
```

Liest aus Ordnername oder Zip-Inhalt. Keine Flags.

## extension get-changelog

```bash
shopware-cli extension get-changelog path/to/MyPlugin
shopware-cli extension get-changelog --language de_DE path/to/MyPlugin
shopware-cli extension get-changelog --language de_DE,en_GB path/to/MyPlugin  # Fallback
```

| Flag | Beschreibung |
|------|--------------|
| `--language string` | Sprachkey, kommagetrennte Fallback-Liste |

## extension config-schema

```bash
shopware-cli extension config-schema > shopware-extension-schema.json
```

JSON-Schema für `.shopware-extension.yml`. Kein Flag.

---

## Typischer Release-Workflow

```bash
# 1. Assets bauen
shopware-cli extension build path/to/MyPlugin

# 2. Validieren (lokal: ohne --full; CI: mit --full)
shopware-cli extension validate --full path/to/MyPlugin

# 3. Zip erstellen
shopware-cli extension zip path/to/MyPlugin --use-git-tag-as-version --release

# 4. In Store hochladen
shopware-cli account login
shopware-cli account producer extension upload MyPlugin-1.2.3.zip
```

## Typischer Dev-Workflow

```bash
# Admin-Dev-Proxy (ESBuild, hot reload)
shopware-cli extension admin-watch path/to/MyPlugin http://localhost

# Storefront: shopware-cli project storefront-watch . statt extension-Pendant
```
