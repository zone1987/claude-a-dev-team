# Symfony Flex Recipes — manifest.json vollständige Referenz

Quelle: `github.com/shopware/recipes` — analysiert aus allen `manifest.json`-Dateien.

## Verzeichnisstruktur eines Recipe

```
recipes/
└── <vendor>/
    └── <package>/
        └── <min-version>/
            ├── manifest.json       # Pflicht
            ├── post-install.txt    # Optional: Nachricht nach Installation
            ├── root/               # Optional: Kopiert nach Projekt-Root (leerer string als Ziel)
            ├── config/             # Optional: Kopiert nach %CONFIG_DIR%/
            ├── bin/                # Optional: Shell-Skripte
            ├── src/                # Optional: PHP-Stubs
            ├── .platform/          # Optional: Platform.sh-Konfig
            └── vendor-bin/         # Optional: bamarni/composer-bin-plugin Setup
```

**Versions-Matching:** `<min-version>` ist die Minimum-Paket-Version. Flex wählt die höchste Recipe-Version die zur installierten Version passt (z.B. Recipe `6.6` gilt für `6.6.0` bis `6.6.x`).

---

## Alle manifest.json Keys

### `copy-from-recipe` (object)

Kopiert Dateien/Verzeichnisse aus dem Recipe-Verzeichnis ins Projekt.

```json
"copy-from-recipe": {
    ".platform/":    ".platform/",
    "bin/":          "%BIN_DIR%/",
    "config/":       "%CONFIG_DIR%/",
    "custom/":       "custom/",
    "files/":        "files/",
    "public/":       "%PUBLIC_DIR%/",
    "src/":          "%SRC_DIR%/",
    "var/":          "var/",
    "docker/":       "docker/",
    "vendor-bin/":   "vendor-bin/",
    "root/":         ""
}
```

**Verzeichnis-Variablen:**

| Variable | Typischer Wert |
|----------|----------------|
| `%BIN_DIR%` | `bin/` |
| `%CONFIG_DIR%` | `config/` |
| `%PUBLIC_DIR%` | `public/` |
| `%SRC_DIR%` | `src/` |

**Spezialfall `"root/": ""`:** Alles in `root/`-Unterverzeichnis des Recipe wird direkt ins Projekt-Root kopiert.
Beispiel: `root/.environment` → `.environment` im Projektverzeichnis.

---

### `bundles` (object)

Registriert Symfony Bundles in `config/bundles.php`.

```json
"bundles": {
    "Shopware\\Core\\Framework\\Framework": ["all"],
    "Shopware\\Administration\\Administration": ["all"],
    "Shopware\\Storefront\\Storefront": ["all"],
    "Shopware\\Elasticsearch\\Framework\\ElasticsearchBundle": ["all"],
    "Symfony\\Bundle\\DebugBundle\\DebugBundle": ["dev"],
    "Shopware\\Core\\DevOps\\DevOps": ["e2e"]
}
```

**Environments:** `"all"`, `"dev"`, `"prod"`, `"test"`, `"e2e"` (Shopware-spezifisch), beliebig erweiterbar.

---

### `env` (object)

Fügt Einträge zur `.env` hinzu.

```json
"env": {
    "APP_ENV": "prod",
    "APP_URL": "http://127.0.0.1:8000",
    "APP_SECRET": "%generate(secret)%",
    "INSTANCE_ID": "%generate(secret)%",
    "DATABASE_URL": "mysql://root:root@localhost/shopware",
    "COMPOSER_ROOT_VERSION": "1.0.0",
    "#1": "### Messaging — wähle einen Transport:",
    "#2": "# MESSENGER_TRANSPORT_DSN=amqp://guest:guest@localhost:5672/%2f/messages"
}
```

**Besonderheiten:**
- `%generate(secret)%` — Flex generiert einen zufälligen Secret-Wert bei Installationszeit
- `#N`-Keys (Nummern als Suffix) — werden als Kommentarzeilen in `.env` eingefügt

---

### `gitignore` (array)

Fügt Einträge zur `.gitignore` hinzu.

```json
"gitignore": [
    ".env.local",
    ".env.local.php",
    ".env.*.local",
    "/public/bundles/*",
    "/public/media/*",
    "/public/thumbnail/*",
    "/public/theme/*",
    "/public/sitemap/*",
    "/var/*",
    "/files/*",
    "!/files/.htaccess",
    "!/files/theme-config"
]
```

**Negation:** `!`-Präfix negiert (Ausnahme aus einer vorher ignorierten Regel).

---

### `container` (object)

Setzt Container-Parameter und `env(...)`-Defaults im Symfony DI-Container.

```json
"container": {
    "shopware.store.frw": true,
    "default_cdn_strategy": "physical_filename",
    "shopware.cdn.strategy": "%env(default:default_cdn_strategy:SHOPWARE_CDN_STRATEGY_DEFAULT)%",
    "env(OPENSEARCH_URL)": "http://localhost:9200",
    "env(CACHE_URL)": "redis://localhost",
    "env(SESSION_REDIS_URL)": "redis://localhost",
    "env(MESSENGER_TRANSPORT_DSN)": "doctrine://default?auto_setup=false",
    "default_redis_database": "0",
    "default_redis_host": "rediscache.internal",
    "default_redis_port": "6379"
}
```

**`env(...)`-Keys** setzen Default-Werte für env-Variablen im Container (Fallback wenn env-Var nicht in `.env` gesetzt).
**Verschachtelte Default-Kette:** `%env(default:default_cdn_strategy:SHOPWARE_CDN_STRATEGY_DEFAULT)%` — nutzt Container-Parameter als Fallback.

---

### `docker-compose` (object)

Injiziert Services/Volumes in `docker-compose.yml` und/oder `docker-compose.override.yml`.

```json
"docker-compose": {
    "docker-compose.yml": {
        "services": [
            "database:",
            "  image: mariadb:11.8",
            "  environment:",
            "    MARIADB_DATABASE: shopware",
            "    MARIADB_USER: shopware",
            "    MARIADB_PASSWORD: shopware",
            "    MARIADB_ROOT_PASSWORD: root"
        ],
        "volumes": ["db-data:"]
    },
    "docker-compose.override.yml": {
        "services": [
            "database:",
            "  ports:",
            "    - \"3306\""
        ]
    }
}
```

Werte sind Arrays von YAML-Zeilen (zeilenbasiertes Merging).

---

### `makefile` (array)

Fügt Targets in ein `Makefile` im Projekt-Root ein.

```json
"makefile": [
    "up:",
    "\t@touch .env.local\n\tdocker compose up -d",
    "stop:",
    "\tdocker compose stop",
    "setup:",
    "\tdocker compose exec web composer install\n\tdocker compose exec web bin/console system:install"
]
```

`\n\t` trennt mehrere Befehle innerhalb eines Targets.

---

### `aliases` (array)

Kurzaliase für `composer require`.

```json
"aliases": ["paas", "fastly", "k8s", "devenv", "code-quality", "messenger", "mailer"]
```

```bash
composer require paas   # → shopware/paas-meta
composer require fastly  # → shopware/fastly-meta
```

---

### `conflict` (object)

Deklariert inkompatible Paket-Versionen.

```json
"conflict": {
    "symfony/framework-bundle": "<4.3",
    "php-http/discovery": ">=1.18"
}
```

---

### `composer-scripts` (object)

Registriert Composer-Scripts.

```json
"composer-scripts": {
    "assets:install": "symfony-cmd"
}
```

`"symfony-cmd"` macht es zu einem Symfony Console-Command-Shortcut in `composer.json`.
Leeres Objekt `{}` ist valide — registriert das Package ohne neue Scripts.

---

## `post-install.txt`

Text der nach Recipe-Installation angezeigt wird. Unterstützt Symfony Console Farbtags.

```
* Nach der ersten Installation fehlen im Storefront CSS-Dateien.
  * Fix: <comment>platform mount:download --mount 'files' --target 'files' -A app</comment>
  * Diese Dateien zum git-Repository hinzufügen und pushen.
```

---

## Shopware-spezifische Besonderheiten

### Version-Nummerierung

Shopware-Recipes nutzen Major.Minor-Versionen die den Shopware Release-Lines entsprechen:
`6.4`, `6.5`, `6.6`, `6.7`, `6.8` — keine SemVer.

Infrastruktur-Packages (`docker`, `paas-meta`, `fastly-meta`, `k8s-meta`) nutzen `0.x`/`1.x`/`2.x`.

### `e2e`-Environment

Shopware nutzt ein eigenes `e2e`-Environment für End-to-End-Tests.

```json
"bundles": {
    "Shopware\\Core\\DevOps\\DevOps": ["e2e"]
}
```

### `shopware/platform` Auto-Merge

CI (`sync-platform.php`) merged automatisch `core` + `administration` + `storefront` + `elasticsearch` in ein `shopware/platform`-Recipe für Legacy-Monorepo-Nutzer.

### CDN-Strategy-Kette

```json
"container": {
    "default_cdn_strategy": "physical_filename",
    "shopware.cdn.strategy": "%env(default:default_cdn_strategy:SHOPWARE_CDN_STRATEGY_DEFAULT)%"
}
```

Fallback-Kette: `SHOPWARE_CDN_STRATEGY_DEFAULT` env var → `default_cdn_strategy` Container-Parameter → `"physical_filename"`.

### `frosh/code-quality-meta` — vendor-bin Pattern

```json
"copy-from-recipe": {
    "vendor-bin/": "vendor-bin/"
}
```

Kopiert `composer.json`-Dateien für `bamarni/composer-bin-plugin` Sub-Vendors:
- `vendor-bin/cs-fixer/composer.json`
- `vendor-bin/phpstan/composer.json`
- `vendor-bin/rector/composer.json`

---

## Recipe erstellen (Checkliste)

1. **Verzeichnis:** `<vendor>/<package>/<min-version>/manifest.json`
2. **JSON:** 4-Leerzeichen-Einrückung, Datei mit Newline beenden
3. **YAML-Dateien:** `.yaml` (nicht `.yml`), `null` (nicht `~`)
4. **Placeholder-Dateien:** `.gitignore` (nicht `.gitkeep`)
5. **Shell-Skripte:** `shellcheck`-kompatibel
6. **Symfony-Commands:** Nicht in Makefile-Targets wrappen
7. **Config-Pfade:** Underscore-Notation
8. **Flex-Endpoint** in `composer.json` des Projekts setzen:

```json
"extra": {
    "symfony": {
        "endpoint": ["https://raw.githubusercontent.com/shopware/recipes/flex/main/index.json"]
    }
}
```
