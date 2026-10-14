# Shopware 6 — `.config/shopware-extension.yml`

Every plugin carries the `shopware-cli` extension configuration. It decides what goes into the
release archive, so development files never reach a shop.

## Contents

- [Where it lives](#where-it-lives)
- [The complete file](#the-complete-file)
- [Why each block](#why-each-block)
- [Traps](#traps)

## Where it lives

`.config/shopware-extension.yml` in the plugin root. The documentation names this as the
preferred path. `.shopware-extension.yml` and `.shopware-extension.yaml` in the root are legacy
fallbacks and are not used for new plugins.

The JSON schema comes from the installed CLI: `shopware-cli extension config-schema`.

## The complete file

```yaml
# yaml-language-server: $schema=https://shopware.github.io/shopware-cli/shopware-extension-schema.json
compatibility_date: {YYYY-MM-DD}

build:
  zip:
    pack:
      excludes:
        paths:
          - CONTEXT.md
          - CLAUDE.md
          - adr
          - tests
          - bin
          - build
          - var
          - docs
          - infection.json5
          - phpstan.neon
          - rector.php
          - cliff.toml
          - phpunit.xml.dist
          - phpunit.unit.xml.dist
          - phpunit.coverage.all.xml.dist
          - phpunit.coverage.integration.xml.dist
          - phpunit.coverage.unit.xml.dist
          - .php-cs-fixer.dist.php
          - .editorconfig
          - src/Resources/app/administration/test
          - src/Resources/app/administration/jest.config.js
          - src/Resources/app/administration/babel.config.js
          - src/Resources/app/administration/eslint.config.js
          - src/Resources/app/administration/stryker.config.json
          - src/Resources/app/administration/.prettierrc.json
          - src/Resources/app/administration/.prettierignore
          - src/Resources/app/administration/.stylelintrc.json
          - src/Resources/app/storefront/test
          - src/Resources/app/storefront/jest.config.js
          - src/Resources/app/storefront/babel.config.js
          - src/Resources/app/storefront/eslint.config.js
          - src/Resources/app/storefront/stryker.config.json
          - src/Resources/app/storefront/.prettierrc.json
          - src/Resources/app/storefront/.prettierignore
          - src/Resources/app/storefront/.stylelintrc.json
```

Drop the lines of an app the plugin does not have. A path that does not exist is harmless, a
development file that ships is not.

## Why each block

| Entry | Why |
|---|---|
| `compatibility_date` | The CLI only applies behaviour changes rolled out on or before this date. Without it, the CLI falls back to `2026-02-11` and logs a warning on every run. Set it to the day the file is created |
| `build.zip.pack.excludes.paths` | The archive is built from the git tree minus these paths. Without them, ADRs, tests, tool configurations and the working notes ship to every shop |
| `CONTEXT.md`, `CLAUDE.md`, `adr` | working notes and decision records, for the maintainers only |
| `tests`, `build`, `var` | test suites, Infection configuration and reports |
| `docs` | maintainer documents: `DEPRECATIONS.md`, `UPGRADE-*.md` for the next Shopware major, mutation baselines |
| Root tool configurations | PHPStan, Rector, php-cs-fixer, PHPUnit, Infection and git-cliff run in development only |
| App test and tool files | Jest, Babel, ESLint, Prettier, Stylelint and Stryker belong to development, the built assets under `src/Resources/public/` are what ships |

`README.md`, `LICENSE`, `SECURITY.md` and `CHANGELOG.md` stay in the archive: the shop operator
reads them.

## Traps

| Trap | Consequence |
|---|---|
| `excludes` written as a list (`excludes: [tests/]`) | rejected by the schema. The shape is an object with `paths` |
| `excluded_paths` as key | does not exist, nothing is excluded |
| `extension zip` | deprecated, use `extension package` |
| `extension package` with `shopware/core` only under `conflict` | fails with `require.shopware/core is required`. A plugin built for a store or a zip needs the constraint under `require` as well, decided per plugin when the first archive is built |

## Source

[developer.shopware.com/docs/products/tools/cli/extension-commands/configuration](https://developer.shopware.com/docs/products/tools/cli/extension-commands/configuration.html),
retrieved 2026-10-14. Schema and the `require.shopware/core` error measured with
`shopware-cli` 0.19.1 (`extension config-schema`, `extension package`) on 2026-10-14.
