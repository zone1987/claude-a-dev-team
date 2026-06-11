# Composer Packages & Plugin Structure Audit

During migration to Shopware 6.7, verify that all composer `require-dev` packages are up-to-date and that the plugin contains all required project files.

---

## 1. Required `require-dev` Packages

Use WebFetch on Packagist JSON URLs (`https://repo.packagist.org/p2/{vendor}/{package}.json`) to resolve the latest stable versions. Replace `{LATEST}` placeholders with `^MAJOR.MINOR` constraint.

| Package | Purpose | Packagist URL |
|---------|---------|---------------|
| `frosh/shopware-rector` | Shopware-specific Rector rules | `https://repo.packagist.org/p2/frosh/shopware-rector.json` |
| `rector/rector` | Automated code refactoring | `https://repo.packagist.org/p2/rector/rector.json` |
| `vimeo/psalm` | Static analysis | `https://repo.packagist.org/p2/vimeo/psalm.json` |
| `psalm/plugin-symfony` | Psalm Symfony integration | `https://repo.packagist.org/p2/psalm/plugin-symfony.json` |
| `squizlabs/php_codesniffer` | Coding standards checker | `https://repo.packagist.org/p2/squizlabs/php_codesniffer.json` |
| `friendsofphp/php-cs-fixer` | Code style fixer | `https://repo.packagist.org/p2/friendsofphp/php-cs-fixer.json` |
| `symplify/easy-coding-standard` | Unified coding standard tool | `https://repo.packagist.org/p2/symplify/easy-coding-standard.json` |

### Version Constraint Convention

Use caret (`^`) constraints based on the latest stable version:

```json
{
    "require-dev": {
        "frosh/shopware-rector": "^0.5",
        "rector/rector": "^2.3",
        "vimeo/psalm": "^6.15",
        "psalm/plugin-symfony": "^5.3",
        "squizlabs/php_codesniffer": "^4.0",
        "friendsofphp/php-cs-fixer": "^3.94",
        "symplify/easy-coding-standard": "^13.0"
    }
}
```

### Audit Steps

1. Read the plugin's `composer.json`
2. For each package in the table above, check if it exists in `require-dev`
3. If missing, add it with the latest stable `^MAJOR.MINOR` constraint
4. If present but outdated (major version behind), update the constraint
5. Verify `composer.json` has all required scripts (see `shopware-plugins` skill `examples/composer.json`)

### Required Composer Scripts

```json
{
    "scripts": {
        "rector": "./vendor/bin/rector process --dry-run --clear-cache",
        "psalm": "./vendor/bin/psalm --show-info=true --no-cache",
        "phpcs": "./vendor/bin/phpcs .",
        "phpcs-report": "./vendor/bin/phpcs --report=summary .",
        "phpcs-fix": "./vendor/bin/php-cs-fixer fix src",
        "ecs": "./vendor/bin/ecs check src",
        "ecs-fix": "./vendor/bin/ecs check src --fix"
    }
}
```

---

## 2. Required Plugin Files

Every plugin must contain the following root-level files. Missing files must be created using the templates from the `shopware-plugins` skill (`examples/` directory).

```
{PluginName}/
├── .editorconfig          → shopware-plugins/examples/editorconfig
├── .gitignore             → shopware-plugins/examples/gitignore
├── .gitlab-ci.yml         → shopware-plugins/examples/gitlab-ci.yml
├── .phpcs.xml             → shopware-plugins/examples/phpcs.xml
├── CHANGELOG.md           → shopware-plugins/examples/CHANGELOG.md
├── cliff.toml             → shopware-plugins/examples/cliff.toml
├── composer.json          → shopware-plugins/examples/composer.json
├── ecs.php                → shopware-plugins/examples/ecs.php
├── LICENSE                → shopware-plugins/examples/license-proprietary.txt (or MIT)
├── psalm.xml              → shopware-plugins/examples/psalm.xml
├── rector.php             → shopware-plugins/examples/rector.php
├── readme.md              → shopware-plugins/examples/readme.md
└── src/
    └── {PluginName}.php   → shopware-plugins/examples/PluginClass.php
```

### Audit Steps

1. List all files in the plugin root directory
2. Compare against the required files list above
3. For each missing file:
   a. Read the corresponding template from `shopware-plugins/examples/`
   b. Replace placeholders (`{PluginName}`, `{vendor}`, etc.) with actual values
   c. Create the file in the plugin root
4. For existing files, verify they are not empty and contain valid content

### File Purpose Quick Reference

| File | Purpose |
|------|---------|
| `.editorconfig` | Editor settings (indentation, charset, line endings) |
| `.gitignore` | Git ignore rules (vendor/, node_modules/, etc.) |
| `.gitlab-ci.yml` | CI/CD pipeline configuration |
| `.phpcs.xml` | PHP CodeSniffer configuration |
| `CHANGELOG.md` | Version history following Keep a Changelog format |
| `cliff.toml` | Git-cliff changelog generator config |
| `composer.json` | PHP dependencies, autoloading, Shopware metadata |
| `ecs.php` | Easy Coding Standard configuration |
| `LICENSE` | License file (MIT or proprietary) |
| `psalm.xml` | Psalm static analysis configuration |
| `rector.php` | Rector automated refactoring configuration |
| `readme.md` | Plugin documentation and usage instructions |

---

## 3. Workflow

When auditing a plugin during migration:

1. **Check composer packages** — verify all `require-dev` packages are present and up-to-date
2. **Check plugin files** — verify all required root-level files exist
3. **Create missing files** — use templates from `shopware-plugins` skill
4. **Update outdated packages** — bump version constraints to latest stable
5. **Run `composer update`** — verify all dependencies resolve correctly
