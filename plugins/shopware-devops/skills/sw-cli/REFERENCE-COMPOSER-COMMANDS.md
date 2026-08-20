# Shopware 6 — Composer dev commands reference

> Source: `resources/references/core-reference/composer-commands-reference.md`
> Only available in the `shopware/shopware` GitHub repository (core development), not in regular projects.
> Regular projects use the `./bin/*.sh` scripts.

```bash
composer [command] [parameter]
```

---

## Setup & Build

| Command | Description |
|:--------|:------------|
| `setup` | Resets this Shopware instance and reinstalls it (the database is dropped!) |
| `build:js` | Builds Administration & Storefront (combination of `build:js:admin` & `build:js:storefront`) |
| `build:js:admin` | Builds the Administration — including `bundle:dump`, `feature:dump`, `admin:generate-entity-schema-types`, `assets:install` |
| `build:js:component-library` | Builds the component library |
| `watch:admin` | Builds the Administration with hot module reloading |
| `build:js:storefront` | Builds storefront JavaScript — including `bundle:dump`, `feature:dump`, `theme:compile` |
| `check:license` | Checks third-party licenses for Composer dependencies |
| `reset` | Resets Shopware without `composer install` / `npm install` (faster when no dependencies changed) |

---

## Administration

| Command | Description |
|:--------|:------------|
| `admin:create:test` | Generates a test boilerplate |
| `admin:generate-entity-schema-types` | Converts entity schemas into data types |
| `admin:unit` | Starts the Jest unit test suite for the Administration |
| `admin:unit:watch` | Starts the interactive Jest unit test watcher for the Administration |
| `admin:unit:prepare-vue3` | Prepares the Jest test suite for the Administration with Vue3 |
| `admin:unit:vue3` | Starts the Jest unit test suite for the Administration with Vue3 |
| `admin:unit:watch:vue3` | Starts the interactive Jest unit test watcher for the Administration with Vue3 |
| `npm:admin:check-license` | Checks third-party licenses for the Administration |
| `watch:admin` | Builds the Administration with hot module reloading |

---

## Storefront

| Command | Description |
|:--------|:------------|
| `build:js:storefront` | Builds storefront JavaScript — including `bundle:dump`, `feature:dump`, `theme:compile` |
| `npm:storefront:check-license` | Checks third-party licenses for the storefront |
| `watch:storefront` | Builds the storefront with hot module reloading |

---

## Test suite & development

| Command | Description |
|:--------|:------------|
| `bc-check` | Checks for backward compatibility breaks in the current branch |
| `e2e:setup` | Installs a clean Shopware instance for E2E and runs `e2e:prepare` |
| `e2e:open` | Opens the Cypress E2E test suite UI |
| `e2e:prepare` | Installs the Admin Extension SDK test plugin with fixtures and dumps the database |
| `ecs` | Checks all files with Easy Coding Standard |
| `ecs-fix` | Checks and fixes ECS issues where possible |
| `eslint` | Code style check of all JS/TS files (Administration/Storefront/E2E) |
| `eslint:admin` | Code style check of Administration JS/TS |
| `eslint:admin:fix` | Code style check and fix of Administration JS/TS |
| `eslint:e2e` | Code style check of E2E JS/TS |
| `eslint:e2e:fix` | Code style check and fix of E2E JS/TS |
| `eslint:storefront` | Code style check of storefront JS/TS |
| `init:testdb` | Initializes the test database |
| `lint` | Shorthand for `stylelint`, `eslint`, `ecs`, `lint:changelog`, `lint:snippets` |
| `lint:changelog` | Validates changelogs |
| `lint:snippets` | Validates snippet existence in all core languages |
| `phpstan` | Runs the PHP static analysis tool |
| `phpunit` | Starts the PHP unit test suite |
| `phpunit:quarantined` | Starts the PHP unit test suite for quarantined tests |
| `storefront:unit` | Starts the Jest unit test suite for the storefront |
| `storefront:unit:watch` | Starts the interactive Jest unit test watcher for the storefront |
