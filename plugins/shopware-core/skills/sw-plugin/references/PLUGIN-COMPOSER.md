# Shopware 6 — The Plugin `composer.json`

Head, `conflict`, `require-dev`, `config.allow-plugins`, all 22 scripts.

## The head

```json
{
    "name": "{plugin-vendor}/{plugin-kebab-case}",
    "description": "What this plugin does, in one sentence",
    "version": "{version}",
    "type": "shopware-platform-plugin",
    "license": "proprietary",
    "authors": [
        { "name": "{VendorLabel}", "homepage": "{vendor-homepage}" }
    ],
    "require": {
        "php": ">=8.3"
    },
    "conflict": {
        "shopware/core":           "< {shopwareMinor} || >= {shopwareNext}",
        "shopware/storefront":     "< {shopwareMinor} || >= {shopwareNext}",
        "shopware/administration": "< {shopwareMinor} || >= {shopwareNext}"
    },
    "extra": {
        "shopware-plugin-class": "{PluginName}\\{PluginName}",
        "label":       { "de-DE": "…", "en-GB": "…" },
        "description": { "de-DE": "…", "en-GB": "…" }
    },
    "autoload":     { "psr-4": { "{PluginName}\\": "src/" } },
    "autoload-dev": { "psr-4": { "{PluginName}\\Tests\\": "tests/" } }
}
```

For a 6.7 plugin, `{shopwareMinor}` is `6.7` and `{shopwareNext}` is `6.8`.

### Why the `conflict` block matters more than it looks

It says: this plugin is built for the stated Shopware version and for no other. Without it
Composer installs the plugin under the next major too, where changed signatures cause a
fatal — not at install time, but on the first page view in production.

It has a second effect that is easily missed: **it forbids writing code for the next
major.** Putting a 6.8 set into `rector.php` while `conflict` excludes 6.8 produces code
for a version the plugin is not allowed to run under at all.

### `autoload-dev` is mandatory as soon as there are tests

Without the entry PHPUnit does not find the test classes, and the error message ("Class not
found") points at the test file instead of at the missing autoload rule.

## `require-dev`, complete

```json
{
    "require-dev": {
        "cyclonedx/cyclonedx-php-composer": "^6.2",
        "friendsofphp/php-cs-fixer":        "3.95.15",
        "frosh/shopware-rector":            "^0.6.0",
        "infection/infection":              "0.35.4",
        "phpat/phpat":                      "0.12.4",
        "phpstan/extension-installer":      "^1.4",
        "phpstan/phpstan":                  "2.2.8",
        "phpstan/phpstan-deprecation-rules":"2.0.5",
        "phpstan/phpstan-phpunit":          "2.0.18",
        "phpstan/phpstan-strict-rules":     "2.0.12",
        "phpstan/phpstan-symfony":          "2.0.20",
        "rector/rector":                    "^2.0",
        "rector/type-perfect":              "2.1.4"
    }
}
```

| Package | What for | Why pinned exactly like this |
|---|---|---|
| `cyclonedx/cyclonedx-php-composer` | generates `sbom.json` | `^6.2`, because the SBOM format is stable |
| `friendsofphp/php-cs-fixer` | code style | **pinned exactly.** A new minor brings new rules into existing sets — the next run then reformats a thousand lines nobody touched |
| `frosh/shopware-rector` | Shopware-specific Rector rules | the minor that contains the set for your own Shopware version |
| `infection/infection` | PHP mutation testing | **pinned exactly.** The mutator catalogue changes between versions; a different version yields a different score for unchanged code |
| `phpat/phpat` | architecture rules as PHPStan rules | pinned exactly, because the API still moves before 1.0 |
| `phpstan/extension-installer` | registers the extensions automatically | otherwise each one has to be wired into `phpstan.neon` by hand |
| `phpstan/phpstan` | static analysis | **pinned exactly.** A new minor finds new errors in unchanged code, and the gate turns red without anyone having done anything |
| `phpstan/phpstan-deprecation-rules` | reports calls to `@deprecated` | the basis for `UPGRADE-*.md` |
| `phpstan/phpstan-phpunit` | understands assertions and mocks | without it PHPStan reports wrong types in tests |
| `phpstan/phpstan-strict-rules` | forbids loose comparisons, implicit casts | |
| `phpstan/phpstan-symfony` | knows the container | detects wrong service IDs and `get()` return types |
| `rector/rector` | automated modernisation | `^2.0` |
| `rector/type-perfect` | stricter type rules than PHPStan alone | |

## `config.allow-plugins` — without this block three of them do not load

Composer has only executed plugin packages since version 2.2 if they are explicitly
allowed. Three of the packages above are such plugins:

```json
{
    "config": {
        "allow-plugins": {
            "cyclonedx/cyclonedx-php-composer": true,
            "infection/extension-installer":    true,
            "phpstan/extension-installer":      true,
            "symfony/runtime":                  false
        },
        "sort-packages": true
    }
}
```

**Without the entry Composer asks interactively** — and in a non-interactive run (CI,
`--no-interaction`) it declines. The consequence: `phpstan/extension-installer` does not
register the five extensions, PHPStan runs without them and then reports different errors
than it does locally.

**`symfony/runtime: false`** is deliberate: the plugin is not a standalone Symfony program,
it is loaded by Shopware. The runtime bootstrap would only get in the way here.

**`sort-packages: true`** keeps `require` and `require-dev` alphabetical — otherwise the
order depends on who installed what and when, and every `composer require` produces an
unnecessary diff.

## What deliberately is NOT in `require-dev`: `phpunit/phpunit`

PHPUnit comes from the project: `../../../vendor/bin/phpunit`.

**Why:** Shopware ships PHPUnit itself, together with the core's test helpers
(`IntegrationTestBehaviour`, `KernelTestBehaviour`, `DatabaseTransactionBehaviour`). A
second PHPUnit inside the plugin loads a second autoloader with a different version, and
the core's test helpers break with errors that look like test failures but are not. There
is exactly one PHPUnit, and it belongs to the project.

## All 22 scripts, verbatim

```json
{
    "scripts": {
        "gate":       ["@gate:fix", "@gate:check"],
        "gate:fix":   ["@rector:fix", "@cs-fix"],
        "gate:check": ["@phpstan", "@cs", "@rector", "@lint:scss", "@test:unit"],

        "changelog": "VERSION=$(composer config version) && git cliff --config cliff.toml --tag \"$VERSION\" --output CHANGELOG.md",

        "phpstan":       "phpstan analyse --memory-limit=1G",
        "cs":            "php-cs-fixer fix --dry-run --diff",
        "cs-fix":        "php-cs-fixer fix",
        "lint:scss":     "npm --prefix src/Resources/app/storefront run lint:scss",
        "lint:scss-fix": "npm --prefix src/Resources/app/storefront run lint:scss:fix",
        "rector":        "rector process --dry-run --no-progress-bar",
        "rector:fix":    "rector process --no-progress-bar",

        "test":             ["@test:unit", "@test:admin", "@test:integration"],
        "test:unit":        "../../../vendor/bin/phpunit -c phpunit.unit.xml.dist",
        "test:integration": "../../../vendor/bin/phpunit -c phpunit.xml.dist --testsuite=integration",
        "test:admin":       "npm --prefix src/Resources/app/administration run unit",

        "coverage:unit":        "../../../vendor/bin/phpunit -c phpunit.coverage.unit.xml.dist",
        "coverage:integration": "../../../vendor/bin/phpunit -c phpunit.coverage.integration.xml.dist --testsuite=integration",
        "coverage:all":         "../../../vendor/bin/phpunit -c phpunit.coverage.all.xml.dist",
        "coverage":             ["@coverage:unit", "@coverage:integration", "@coverage:all"],

        "infection":      "infection --show-mutations --no-interaction --threads=1 --only-covering-test-cases",
        "mutation:admin": "npm --prefix src/Resources/app/administration run mutation",
        "mutation":       ["@infection", "@mutation:admin"]
    }
}
```

### `scripts-descriptions` belongs with it

Without it `composer list` shows names only:

```json
{
    "scripts-descriptions": {
        "gate":         "Runs the fixers, then every check. The one command before a commit.",
        "coverage:all": "The coverage figure that counts: unit and integration measured together.",
        "infection":    "Mutation testing for PHP. Run last, when no task is open."
    }
}
```

### Three details in the scripts

| Detail | Why |
|---|---|
| `npm --prefix` instead of `cd` | `npm --prefix <path> run <script>` changes the working directory for npm without leaving the shell. A `cd` in a Composer script does not work reliably, because every entry runs in its own shell — the `cd` of one command is gone again in the next |
| `--threads=1` on Infection | see the Infection configuration |
| `composer changelog` runs on the host | not in DDEV: `git cliff` reads the git history |

→ Directory layout and `.gitignore`: [PLUGIN-STRUCTURE.md](PLUGIN-STRUCTURE.md)
→ Checklist for a new plugin: [PLUGIN-CHECKLIST.md](PLUGIN-CHECKLIST.md)
