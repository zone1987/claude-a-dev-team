# Shopware 6 — bin/console Command Reference

> Source: `resources/references/core-reference/commands-reference.md`

```bash
bin/console [command] [parameter]
```

---

## Contents

- [General](#general)
- [Administration](#administration)
- [App](#app)
- [Assets](#assets)
- [Bundle](#bundle)
- [Cache](#cache)
- [Cart](#cart)
- [Changelog](#changelog)
- [Config](#config)
- [Customer](#customer)
- [DAL](#dal)
- [Database](#database)
- [Debug](#debug)
- [Dotenv](#dotenv)
- [Error](#error)
- [Elasticsearch / OpenSearch (es)](#elasticsearch-opensearch-es)
- [Feature Flags](#feature-flags)
- [Framework](#framework)
- [HTTP](#http)
- [Import](#import)
- [Integration](#integration)
- [Lint](#lint)
- [Mailer](#mailer)
- [make:plugin — Plugin Scaffolding](#makeplugin-plugin-scaffolding)
- [Media](#media)
- [Messenger](#messenger)
- [Number Range](#number-range)
- [Plugin](#plugin)
- [Product Export](#product-export)
- [Router](#router)
- [S3](#s3)
- [Sales Channel](#sales-channel)
- [Scheduled Task](#scheduled-task)
- [Secrets](#secrets)
- [Server](#server)
- [Services](#services)
- [Sitemap](#sitemap)
- [Snippets](#snippets)
- [State Machine](#state-machine)
- [Store](#store)
- [System](#system)
- [Theme](#theme)
- [Translation](#translation)
- [User](#user)

## General

| Command | Description |
|:--------|:------------|
| `about` | Shows project information |
| `completion` | Prints the shell completion script |
| `help` | Shows help for a command |
| `list` | Lists all commands |

---

## Administration

| Command | Description |
|:--------|:------------|
| `administration:delete-extension-local-public-files` | Deletes all local public files of an extension (run after `assets:install`) |
| `administration:delete-files-after-build` | Deletes unnecessary administration files after the build |

---

## App

| Command | Description |
|:--------|:------------|
| `app:activate` | Activates the app in the folder with the given name |
| `app:create` | Creates an app skeleton |
| `app:deactivate` | Deactivates the app |
| `app:install` | Installs the app |
| `app:list` | Lists all apps |
| `app:refresh` | `[app:update]` Refreshes installed apps |
| `app:uninstall` | Uninstalls the app |
| `app:url-change:resolve` | Resolves app URL changes |
| `app:validate` | Checks manifests for errors |

---

## Assets

| Command | Description |
|:--------|:------------|
| `assets:install` | Installs bundle web assets into the public directory |

---

## Bundle

| Command | Description |
|:--------|:------------|
| `bundle:dump` | `[administration:dump:plugins|administration:dump:bundles]` Creates a JSON file with the bundle configuration |

---

## Cache

| Command | Description |
|:--------|:------------|
| `cache:clear` | Clears the cache |
| `cache:clear:all` | Clears all caches/pools, invalidates tags, removes old kernel cache directories |
| `cache:clear:delayed` | Invalidates delayed cache keys/tags |
| `cache:clear:http` | Clears the HTTP cache only |
| `cache:pool:clear` | Clears cache pools |
| `cache:pool:delete` | Deletes an item from a cache pool |
| `cache:pool:invalidate-tags` | Invalidates cache tags for all or specific pools |
| `cache:pool:list` | Lists available cache pools |
| `cache:pool:prune` | Prunes cache pools |
| `cache:warmup` | Warms up an empty cache |
| `cache:watch:delayed` | Watches delayed cache keys/tags |

---

## Cart

| Command | Description |
|:--------|:------------|
| `cart:migrate` | Migrates carts from Redis to the database |

---

## Changelog

| Command | Description |
|:--------|:------------|
| `changelog:change` | Prints all changes of a specific / unreleased version |
| `changelog:check` | Validates changelog file(s) in the `changelog/_unreleased` folder |
| `changelog:create` | Creates a changelog markdown file in `/changelog/_unreleased` |
| `changelog:release` | Creates or updates the final changelog for a new release |

---

## Config

| Command | Description |
|:--------|:------------|
| `config:dump-reference` | Prints the default configuration for an extension |

---

## Customer

| Command | Description |
|:--------|:------------|
| `customer:delete-unused-guests` | Deletes unused guest customers |

---

## DAL

| Command | Description |
|:--------|:------------|
| `dal:create:entities` | Creates entity classes |
| `dal:create:hydrators` | Creates hydrator classes |
| `dal:migration:create` | Creates a migration for the entity schema |
| `dal:create:schema` | Creates the database schema |
| `dal:refresh:index` | Refreshes the index for an entity |
| `dal:validate` | Validates DAL definitions |

---

## Database

| Command | Description |
|:--------|:------------|
| `database:clean-personal-data` | Cleans personal data from the database |
| `database:create-migration` | Creates a new migration file |
| `database:migrate` | Runs all migrations |
| `database:migrate-destructive` | Runs all destructive migrations |
| `database:refresh-migration` | Refreshes the migration status |

---

## Debug

| Command | Description |
|:--------|:------------|
| `debug:autowiring` | Lists classes/interfaces for autowiring |
| `debug:business-events` | Prints all business events |
| `debug:config` | Prints the current configuration of an extension |
| `debug:container` | Shows the current services of the application |
| `debug:dotenv` | Lists all dotenv files with variables and values |
| `debug:event-dispatcher` | Shows configured listeners |
| `debug:messenger` | Lists messages for message buses |
| `debug:router` | Shows the current routes |
| `debug:scheduler` | Lists schedules and recurring messages |
| `debug:serializer` | Shows serialization information for classes |
| `debug:translation` | Shows translation message information |
| `debug:twig` | Shows Twig functions, filters, globals and tests |
| `debug:validator` | Shows validation constraints for classes |

---

## Dotenv

| Command | Description |
|:--------|:------------|
| `dotenv:dump` | Compiles .env files into .env.local.php |

---

## Error

| Command | Description |
|:--------|:------------|
| `error:dump` | Dumps error pages as static HTML files |

---

## Elasticsearch / OpenSearch (es)

| Command | Description |
|:--------|:------------|
| `es:admin:index` | Indexes Elasticsearch for the admin search |
| `es:admin:mapping:update` | Updates the Elasticsearch index mapping for the admin |
| `es:admin:reset` | Resets the admin Elasticsearch indexing |
| `es:admin:test` | Tests the admin search index |
| `es:create:alias` | Creates the Elasticsearch alias |
| `es:index` | Re-indexes all entities in Elasticsearch |
| `es:index:cleanup` | Cleans up outdated indices |
| `es:mapping:update` | Updates the Elasticsearch index mapping |
| `es:reset` | Resets the Elasticsearch index |
| `es:status` | Shows the status of the Elasticsearch index |
| `es:test:analyzer` | Tests an Elasticsearch analyzer |

---

## Feature Flags

| Command | Description |
|:--------|:------------|
| `feature:disable` | Disables feature flags |
| `feature:dump` | `[administration:dump:features]` Creates a JSON file with the feature config |
| `feature:enable` | Enables feature flags |
| `feature:list` | Lists all registered features |

---

## Framework

| Command | Description |
|:--------|:------------|
| `framework:demodata` | Generates demo data |
| `framework:dump:class:schema` | Prints the schema of the given entity |
| `framework:schema` | Prints the API definition as JSON |

---

## HTTP

| Command | Description |
|:--------|:------------|
| `http:cache:warm:up` | Warms up the HTTP cache |

---

## Import

| Command | Description |
|:--------|:------------|
| `import:entity` | Imports entities from a CSV file |
| `import-export:delete-expired` | Deletes all expired import/export files |

---

## Integration

| Command | Description |
|:--------|:------------|
| `integration:create` | Creates an integration and prints key and secret |

---

## Lint

| Command | Description |
|:--------|:------------|
| `lint:container` | Checks injected service arguments against types |
| `lint:translations` | Validates translation files |
| `lint:twig` | Validates Twig templates |
| `lint:xliff` | Validates XLIFF files |
| `lint:yaml` | Validates YAML files |

---

## Mailer

| Command | Description |
|:--------|:------------|
| `mailer:test` | Tests mailer transports by sending a test mail |

---

## make:plugin — Plugin Scaffolding

| Command | Description |
|:--------|:------------|
| `make:plugin:admin-module` | Generates an administration module skeleton |
| `make:plugin:command` | Generates a plugin CLI command skeleton |
| `make:plugin:composer` | Generates the Composer configuration for a plugin |
| `make:plugin:config` | Generates a plugin system config skeleton |
| `make:plugin:custom-fieldset` | Generates a custom field set for a plugin |
| `make:plugin:entity` | Generates entity scaffolding for a plugin |
| `make:plugin:event-subscriber` | Generates an event subscriber skeleton |
| `make:plugin:javascript-plugin` | Generates a JavaScript plugin skeleton |
| `make:plugin:plugin-class` | Generates the base plugin class |
| `make:plugin:scheduled-task` | Generates a scheduled task skeleton |
| `make:plugin:store-api-route` | Generates a Store API route skeleton |
| `make:plugin:storefront-controller` | Generates a storefront controller |
| `make:plugin:tests` | Generates a plugin test skeleton |

---

## Media

| Command | Description |
|:--------|:------------|
| `media:delete-local-thumbnails` | Deletes physical thumbnails when remote thumbnails are enabled |
| `media:delete-unused` | Deletes media files that were never used. Flags: `--dry-run`, `--grace-period-days=N`, `--folder-entity=PRODUCT` |
| `media:generate-media-types` | Generates media types for all media entities |
| `media:generate-thumbnails` | Generates thumbnails for all media entities |
| `media:update-path` | Updates the `path` column of all media entries |

---

## Messenger

| Command | Description |
|:--------|:------------|
| `messenger:consume` | Consumes messages |
| `messenger:failed:remove` | Removes messages from the failure transport |
| `messenger:failed:retry` | Retries messages from the failure transport |
| `messenger:failed:show` | Shows messages from the failure transport |
| `messenger:setup-transports` | Prepares the infrastructure for the transport |
| `messenger:stats` | Shows the message count for transports |
| `messenger:stop-workers` | Stops workers after the current message |

---

## Number Range

| Command | Description |
|:--------|:------------|
| `number-range:migrate` | Migrates the increment storage of a number range |

---

## Plugin

| Command | Description |
|:--------|:------------|
| `plugin:activate` | Activates the given plugins |
| `plugin:create` | Creates a plugin skeleton |
| `plugin:deactivate` | Deactivates the given plugins |
| `plugin:install` | Installs the given plugins |
| `plugin:list` | Lists all plugins |
| `plugin:refresh` | Refreshes the plugin list from the file system |
| `plugin:uninstall` | Uninstalls the given plugins |
| `plugin:update` | Updates the given plugins |
| `plugin:update:all` | Installs all available plugin updates |
| `plugin:zip-import` | Imports a plugin from a ZIP file |

---

## Product Export

| Command | Description |
|:--------|:------------|
| `product-export:generate` | Generates a product export file |

---

## Router

| Command | Description |
|:--------|:------------|
| `router:match` | Debugs routes by simulating a path match |

---

## S3

| Command | Description |
|:--------|:------------|
| `s3:set-visibility` | Sets all files in the S3 filesystem to public |

---

## Sales Channel

| Command | Description |
|:--------|:------------|
| `sales-channel:create` | Creates a new sales channel |
| `sales-channel:create:storefront` | Creates a new storefront sales channel |
| `sales-channel:list` | Lists all sales channels |
| `sales-channel:maintenance:disable` | Disables maintenance mode |
| `sales-channel:maintenance:enable` | Enables maintenance mode |
| `sales-channel:update:domain` | Updates a sales channel domain |

---

## Scheduled Task

| Command | Description | Version |
|:--------|:------------|:--------|
| `scheduled-task:deactivate` | Deactivates a scheduled task | 6.7.2.0 |
| `scheduled-task:register` | Registers all scheduled tasks | |
| `scheduled-task:run` | Runs scheduled tasks | |
| `scheduled-task:run-single` | Runs a single scheduled task | 6.5.5.0 |
| `scheduled-task:list` | Lists all scheduled tasks | 6.5.5.0 |
| `scheduled-task:schedule` | Schedules a scheduled task | 6.7.2.0 |

---

## Secrets

| Command | Description |
|:--------|:------------|
| `secrets:decrypt-to-local` | Decrypts all secrets into the local vault |
| `secrets:encrypt-from-local` | Encrypts local secrets into the vault |
| `secrets:generate-keys` | Generates new encryption keys |
| `secrets:list` | Lists all secrets |
| `secrets:remove` | Removes a secret from the vault |
| `secrets:reveal` | Shows the value of a secret |
| `secrets:set` | Sets a secret in the vault |

---

## Server

| Command | Description |
|:--------|:------------|
| `server:dump` | Starts a dump server (collects and shows dumps) |
| `server:log` | Starts a log server (shows logs in real time) |

---

## Services

| Command | Description |
|:--------|:------------|
| `services:install` | Installs all services |

---

## Sitemap

| Command | Description |
|:--------|:------------|
| `sitemap:generate` | Generates sitemaps for one or all active shops |

---

## Snippets

| Command | Description |
|:--------|:------------|
| `snippets:validate` | Validates snippets |

---

## State Machine

| Command | Description |
|:--------|:------------|
| `state-machine:dump` | Dumps a state machine as a Graphviz file |

---

## Store

| Command | Description |
|:--------|:------------|
| `store:download` | Downloads a plugin from the store |
| `store:login` | Logs in to the store |

---

## System

| Command | Description |
|:--------|:------------|
| `system:check` | Checks the system health of the Shopware application |
| `system:config:get` | Reads a config value |
| `system:config:set` | Sets a config value |
| `system:configure-shop` | Configures the shop |
| `system:generate-app-secret` | Generates a new app secret |
| `system:install` | Installs the Shopware 6 system |
| `system:is-installed` | Checks whether the system is installed (exit code 0 = installed) |
| `system:setup` | Starts the system setup |
| `system:setup:staging` | Installs Shopware 6 in staging mode |
| `system:update:finish` | Finishes the update process |
| `system:update:prepare` | Prepares the update process |

---

## Theme

| Command | Description |
|:--------|:------------|
| `theme:change` | Changes the active theme for a sales channel |
| `theme:compile` | Compiles the theme |
| `theme:create` | Creates a theme skeleton |
| `theme:dump` | Dumps the theme configuration |
| `theme:prepare-icons` | Prepares theme icons |
| `theme:refresh` | Refreshes the theme configuration |

---

## Translation

| Command | Description |
|:--------|:------------|
| `translation:extract` | Extracts missing translation keys from the code |
| `translation:install` | Downloads and installs translations from GitHub |
| `translation:pull` | Pulls translations from a provider |
| `translation:push` | Pushes translations to a provider |

---

## User

| Command | Description |
|:--------|:------------|
| `user:change-password` | Changes the password of a user |
| `user:create` | Creates a new user |
| `user:list` | Lists current users |
