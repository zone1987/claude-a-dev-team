# Composer Packages & Plugin Structure Audit

During migration to Shopware 6.7, verify that the plugin's `require-dev` packages and its
root-level files match the target state below. A plugin coming from 6.6 usually carries a
legacy tool chain (Psalm, PHP_CodeSniffer, ECS); migrating it means replacing that chain,
not extending it.

---

## Contents

- [1. Required `require-dev` Packages](#1-required-require-dev-packages)
- [2. Required Composer Scripts](#2-required-composer-scripts)
- [3. Required Plugin Files](#3-required-plugin-files)
- [4. Legacy Tool Chain to Remove](#4-legacy-tool-chain-to-remove)
- [5. Workflow](#5-workflow)

## 1. Required `require-dev` Packages

Exactly these 13 packages belong in `require-dev`. Nothing else, and nothing less.

| Package | Purpose | Constraint |
|---------|---------|------------|
| `cyclonedx/cyclonedx-php-composer` | produces `sbom.json` | `^6.2` |
| `friendsofphp/php-cs-fixer` | code style | pinned exactly |
| `frosh/shopware-rector` | Shopware-specific Rector rules | the minor carrying the plugin's own Shopware set |
| `infection/infection` | PHP mutation testing | pinned exactly |
| `phpat/phpat` | architecture rules as PHPStan rules | pinned exactly |
| `phpstan/extension-installer` | registers the PHPStan extensions automatically | `^1.4` |
| `phpstan/phpstan` | static analysis | pinned exactly |
| `phpstan/phpstan-deprecation-rules` | reports calls to `@deprecated` — the source for `UPGRADE-*.md` | pinned exactly |
| `phpstan/phpstan-phpunit` | understands assertions and mocks | pinned exactly |
| `phpstan/phpstan-strict-rules` | forbids loose comparisons and implicit casts | pinned exactly |
| `phpstan/phpstan-symfony` | knows the container | pinned exactly |
| `rector/rector` | automated modernisation | `^2.0` |
| `rector/type-perfect` | stricter type rules than PHPStan alone | pinned exactly |

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

Use WebFetch on Packagist JSON URLs (`https://repo.packagist.org/p2/{vendor}/{package}.json`)
to resolve the current stable versions before pinning.

**Why most of them are pinned exactly instead of with `^`:** a new minor of PHPStan finds
new errors in unchanged code, a new minor of php-cs-fixer brings new rules into existing
sets, and a new Infection version ships a different mutator catalogue and therefore a
different score for the same code. The gate would turn red without anybody having changed
anything.

**`phpunit/phpunit` deliberately does NOT belong here.** PHPUnit comes from the project:
`../../../vendor/bin/phpunit`. A second PHPUnit inside the plugin loads a second
autoloader, and the core's test traits break with errors that look like test failures but
are not.

### `config.allow-plugins`

Three of the packages above are Composer plugins and do not load without being allowed:

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

Without this block Composer asks interactively and refuses in a non-interactive run, so
`phpstan/extension-installer` never registers the five extensions and PHPStan silently
reports different errors than it does locally.

### License

`"license": "proprietary"` — in `composer.json`, in every `package.json`, and in the
`LICENSE` file. There is no MIT alternative for a plugin of ours.

## 2. Required Composer Scripts

The plugin has 22 scripts. `composer gate` is **the** command before every commit: it
first fixes (`gate:fix`), then checks (`gate:check`).

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

`gate:fix` changes files, `gate:check` only reports. Rector runs before php-cs-fixer,
because Rector rewrites and php-cs-fixer formats what it produced — the other way round
the formatting is undone again.

### Audit Steps

1. Read the plugin's `composer.json`
2. Compare `require-dev` against the 13 packages above — add what is missing, remove the legacy chain (section 4)
3. Compare `scripts` against the list above — `gate`, `gate:fix` and `gate:check` must exist
4. Verify `config.allow-plugins` and `"license": "proprietary"`
5. Verify the `conflict` block names the next major (`>= 6.8.0.0` for a 6.7 plugin)

## 3. Required Plugin Files

Every plugin contains the following root-level files. Missing files are created from the
templates of the `shopware-plugins` skill (`examples/` directory).

```
{PluginName}/
├── .editorconfig                → shopware-plugins/examples/editorconfig
├── .gitignore                   → shopware-plugins/examples/gitignore
├── .gitlab-ci.yml               → shopware-plugins/examples/gitlab-ci.yml
├── .php-cs-fixer.dist.php       → shopware-plugins/examples/php-cs-fixer.dist.php
├── CHANGELOG.md                 → shopware-plugins/examples/CHANGELOG.md
├── cliff.toml                   → shopware-plugins/examples/cliff.toml
├── composer.json                → shopware-plugins/examples/composer.json
├── LICENSE                      → shopware-plugins/examples/license-proprietary.txt
├── phpstan.neon                 → shopware-plugins/examples/phpstan.neon
├── rector.php                   → shopware-plugins/examples/rector.php
├── readme.md                    → shopware-plugins/examples/readme.md
├── UPGRADE-{SHOPWARE-NEXT}.md   → written from the deprecation findings, see DEPRECATION-HANDLING.md
└── src/
    └── {PluginName}.php         → shopware-plugins/examples/PluginClass.php
```

### Audit Steps

1. List all files in the plugin root directory
2. Compare against the required files list above
3. For each missing file:
   a. Read the corresponding template from `shopware-plugins/examples/`
   b. Replace placeholders (`{PluginName}`, `{vendor}`, etc.) with actual values
   c. Create the file in the plugin root
4. For existing files, verify they are not empty and contain valid content
5. Delete the legacy configuration files listed in section 4

### File Purpose Quick Reference

| File | Purpose |
|------|---------|
| `.editorconfig` | Editor settings (indentation, charset, line endings) |
| `.gitignore` | Git ignore rules (vendor/, node_modules/, etc.) |
| `.gitlab-ci.yml` | CI/CD pipeline configuration |
| `.php-cs-fixer.dist.php` | php-cs-fixer configuration — the only code style tool |
| `CHANGELOG.md` | Version history following Keep a Changelog format |
| `cliff.toml` | Git-cliff changelog generator config |
| `composer.json` | PHP dependencies, autoloading, Shopware metadata, the 22 scripts |
| `LICENSE` | Proprietary license text, end year = current year |
| `phpstan.neon` | PHPStan configuration (`level: max`, no `ignoreErrors`) |
| `rector.php` | Rector configuration — the Shopware set of the released version only |
| `readme.md` | Plugin documentation and usage instructions |
| `UPGRADE-{SHOPWARE-NEXT}.md` | Deprecation findings and what replaces them |

## 4. Legacy Tool Chain to Remove

A plugin written for 6.6 or earlier typically still carries the chain below. It is
legacy — what the audit finds, not what the audit leaves behind.

| Legacy (found in old plugins) | Target state |
|---|---|
| `vimeo/psalm`, `psalm/plugin-symfony` in `require-dev` | `phpstan/phpstan` plus its five extensions and `rector/type-perfect` |
| `squizlabs/php_codesniffer` in `require-dev` | `friendsofphp/php-cs-fixer` |
| `symplify/easy-coding-standard` in `require-dev` | `friendsofphp/php-cs-fixer` |
| `psalm.xml` in the plugin root | `phpstan.neon` |
| `.phpcs.xml` in the plugin root | `.php-cs-fixer.dist.php` |
| `ecs.php` in the plugin root | `.php-cs-fixer.dist.php` |
| Scripts `psalm`, `phpcs`, `phpcs-report`, `phpcs-fix`, `ecs`, `ecs-fix` | `gate`, `gate:fix`, `gate:check` plus `phpstan`, `cs`, `cs-fix`, `rector`, `rector:fix` |
| `"license": "MIT"` | `"license": "proprietary"` |
| MIT text in `LICENSE` | the proprietary license text, rewritten in full |

The `LICENSE` file is rewritten completely, not amended: an MIT text with a changed
heading still grants redistribution, because that permission sits in the body, not in the
title.

## 5. Workflow

When auditing a plugin during migration:

1. **Check composer packages** — the 13 packages of section 1 present, the legacy chain of section 4 removed
2. **Check composer scripts** — `gate` / `gate:fix` / `gate:check` present, the legacy scripts gone
3. **Check the license** — `proprietary` in `composer.json`, in every `package.json` and in `LICENSE`; end year = current year
4. **Check plugin files** — required root-level files exist, legacy configuration files deleted
5. **Create missing files** — use templates from `shopware-plugins` skill
6. **Update the dependencies** — inside the container:

```bash
ddev exec bash -c "cd /var/www/html/shopware/custom/static-plugins/<PLUGIN-NAME> && composer update"
```

7. **Run the gate** — inside the container:

```bash
ddev exec bash -c "cd /var/www/html/shopware/custom/static-plugins/<PLUGIN-NAME> && composer gate"
```

Every command runs in the container. The one exception is `composer changelog`, because
`git cliff` reads the git history, which lives on the host.
