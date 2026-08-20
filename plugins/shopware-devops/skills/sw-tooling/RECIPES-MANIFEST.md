# Symfony Flex recipes — complete manifest.json reference

Source: `github.com/shopware/recipes` — analyzed from all `manifest.json` files.

## Contents

- [Directory structure of a recipe](#directory-structure-of-a-recipe)
- [All manifest.json keys](#all-manifestjson-keys)
- [`post-install.txt`](#post-installtxt)
- [Shopware-specific characteristics](#shopware-specific-characteristics)
- [Creating a recipe (checklist)](#creating-a-recipe-checklist)

## Directory structure of a recipe

```
recipes/
└── <vendor>/
    └── <package>/
        └── <min-version>/
            ├── manifest.json       # Required
            ├── post-install.txt    # Optional: message shown after installation
            ├── root/               # Optional: copied to the project root (empty string as target)
            ├── config/             # Optional: copied to %CONFIG_DIR%/
            ├── bin/                # Optional: shell scripts
            ├── src/                # Optional: PHP stubs
            ├── .platform/          # Optional: Platform.sh config
            └── vendor-bin/         # Optional: bamarni/composer-bin-plugin setup
```

**Version matching:** `<min-version>` is the minimum package version. Flex picks the highest recipe version matching the installed version (e.g. recipe `6.6` applies to `6.6.0` through `6.6.x`).

---

## All manifest.json keys

### `copy-from-recipe` (object)

Copies files/directories from the recipe directory into the project.

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

**Directory variables:**

| Variable | Typical value |
|----------|----------------|
| `%BIN_DIR%` | `bin/` |
| `%CONFIG_DIR%` | `config/` |
| `%PUBLIC_DIR%` | `public/` |
| `%SRC_DIR%` | `src/` |

**Special case `"root/": ""`:** everything in the recipe's `root/` subdirectory is copied directly into the project root.
Example: `root/.environment` → `.environment` in the project directory.

---

### `bundles` (object)

Registers Symfony bundles in `config/bundles.php`.

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

**Environments:** `"all"`, `"dev"`, `"prod"`, `"test"`, `"e2e"` (Shopware-specific), extensible at will.

---

### `env` (object)

Adds entries to `.env`.

```json
"env": {
    "APP_ENV": "prod",
    "APP_URL": "http://127.0.0.1:8000",
    "APP_SECRET": "%generate(secret)%",
    "INSTANCE_ID": "%generate(secret)%",
    "DATABASE_URL": "mysql://root:root@localhost/shopware",
    "COMPOSER_ROOT_VERSION": "1.0.0",
    "#1": "### Messaging — pick a transport:",
    "#2": "# MESSENGER_TRANSPORT_DSN=amqp://guest:guest@localhost:5672/%2f/messages"
}
```

**Characteristics:**
- `%generate(secret)%` — Flex generates a random secret value at installation time
- `#N` keys (numbers as suffix) — inserted as comment lines into `.env`

---

### `gitignore` (array)

Adds entries to `.gitignore`.

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

**Negation:** the `!` prefix negates (an exception to a previously ignored rule).

---

### `container` (object)

Sets container parameters and `env(...)` defaults in the Symfony DI container.

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

**`env(...)` keys** set default values for env variables in the container (a fallback when the env var is not set in `.env`).
**Nested default chain:** `%env(default:default_cdn_strategy:SHOPWARE_CDN_STRATEGY_DEFAULT)%` — uses a container parameter as the fallback.

---

### `docker-compose` (object)

Injects services/volumes into `docker-compose.yml` and/or `docker-compose.override.yml`.

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

Values are arrays of YAML lines (line-based merging).

---

### `makefile` (array)

Inserts targets into a `Makefile` in the project root.

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

`\n\t` separates several commands inside one target.

---

### `aliases` (array)

Short aliases for `composer require`.

```json
"aliases": ["paas", "fastly", "k8s", "devenv", "code-quality", "messenger", "mailer"]
```

```bash
composer require paas   # → shopware/paas-meta
composer require fastly  # → shopware/fastly-meta
```

---

### `conflict` (object)

Declares incompatible package versions.

```json
"conflict": {
    "symfony/framework-bundle": "<4.3",
    "php-http/discovery": ">=1.18"
}
```

---

### `composer-scripts` (object)

Registers Composer scripts.

```json
"composer-scripts": {
    "assets:install": "symfony-cmd"
}
```

`"symfony-cmd"` turns it into a Symfony console command shortcut in `composer.json`.
An empty object `{}` is valid — it registers the package without new scripts.

---

## `post-install.txt`

Text shown after the recipe is installed. Supports Symfony Console color tags.

```
* After the first installation, CSS files are missing in the storefront.
  * Fix: <comment>platform mount:download --mount 'files' --target 'files' -A app</comment>
  * Add these files to the git repository and push.
```

---

## Shopware-specific characteristics

### Version numbering

Shopware recipes use major.minor versions matching the Shopware release lines:
`6.4`, `6.5`, `6.6`, `6.7`, `6.8` — no SemVer.

Infrastructure packages (`docker`, `paas-meta`, `fastly-meta`, `k8s-meta`) use `0.x`/`1.x`/`2.x`.

### The `e2e` environment

Shopware uses its own `e2e` environment for end-to-end tests.

```json
"bundles": {
    "Shopware\\Core\\DevOps\\DevOps": ["e2e"]
}
```

### `shopware/platform` auto-merge

CI (`sync-platform.php`) automatically merges `core` + `administration` + `storefront` + `elasticsearch` into one `shopware/platform` recipe for legacy monorepo users.

### CDN strategy chain

```json
"container": {
    "default_cdn_strategy": "physical_filename",
    "shopware.cdn.strategy": "%env(default:default_cdn_strategy:SHOPWARE_CDN_STRATEGY_DEFAULT)%"
}
```

Fallback chain: `SHOPWARE_CDN_STRATEGY_DEFAULT` env var → `default_cdn_strategy` container parameter → `"physical_filename"`.

### `frosh/code-quality-meta` — the vendor-bin pattern

```json
"copy-from-recipe": {
    "vendor-bin/": "vendor-bin/"
}
```

Copies `composer.json` files for `bamarni/composer-bin-plugin` sub-vendors:
- `vendor-bin/cs-fixer/composer.json`
- `vendor-bin/phpstan/composer.json`
- `vendor-bin/rector/composer.json`

---

## Creating a recipe (checklist)

1. **Directory:** `<vendor>/<package>/<min-version>/manifest.json`
2. **JSON:** four-space indentation, end the file with a newline
3. **YAML files:** `.yaml` (not `.yml`), `null` (not `~`)
4. **Placeholder files:** `.gitignore` (not `.gitkeep`)
5. **Shell scripts:** `shellcheck`-compatible
6. **Symfony commands:** do not wrap them in Makefile targets
7. **Config paths:** underscore notation
8. **Set the Flex endpoint** in the project's `composer.json`:

```json
"extra": {
    "symfony": {
        "endpoint": ["https://raw.githubusercontent.com/shopware/recipes/flex/main/index.json"]
    }
}
```
