---
name: shopware-6.7-migration
description: Use when migrating Shopware plugins from 6.6 to 6.7, upgrading admin components from sw-* to mt-* (Meteor), migrating from Webpack to Vite, converting Vuex to Pinia, adopting Vue 3 Composition API, or updating PHP code with constructor property promotion. Trigger on "6.6 to 6.7", "6.7 migration", "migrate plugin", "upgrade shopware", "meteor components", "sw- to mt-", "mt-button", "mt-text-field", "mt-select", "mt-banner", "mt-card", "mt-tabs", "webpack to vite", "vuex to pinia".
---

# Shopware 6.6 to 6.7 Plugin Migration

This skill guides the migration of Shopware 6 plugins from version 6.6 to 6.7. It covers breaking changes in the **administration** (Meteor components, Vite, Pinia) and **PHP backend** (constructor promotion, coding standards).

## Migration Checklist

- [ ] Replace all `sw-*` components with `mt-*` Meteor equivalents
- [ ] Migrate build system from Webpack to Vite
- [ ] Remove `src/Resources/app/administration/build/webpack.config.js` (and the `build/` directory if it becomes empty)
- [ ] Remove `src/Resources/app/administration/src/init/svg-icons.init.js` (and the `init/` directory if it becomes empty)
- [ ] Remove `src/Resources/app/administration/src/app/assets/icons/svg/ff-icon.svg`
- [ ] Remove `src/Resources/app/administration/src/app/assets/icons/icons.js`
- [ ] Remove `src/Resources/app/administration/src/app/assets/` if empty (including subdirectories that contain only empty directories)
- [ ] Update Admin SDK (`admin-extension-sdk` → `meteor-admin-sdk`)
- [ ] Migrate Vuex stores to Pinia (`Shopware.State` → `Shopware.Store`)
- [ ] Replace deprecated storefront iterator helpers with native JS
- [ ] Apply PHP constructor property promotion
- [ ] Update coding style (braces, DocBlocks, type declarations)
- [ ] Adopt domain exception factory pattern
- [ ] Replace constant classes with PHP 8.1 backed enums where applicable
- [ ] Update `composer.json` conflict to `"shopware/core": "<6.7 || >=6.8"`
- [ ] Increment `composer.json` `"version"`: bump major by 1, reset minor and patch to 0 (e.g. `1.3.2` → `2.0.0`)
- [ ] Audit and update `require-dev` packages to latest stable versions
- [ ] Verify all required plugin root files exist (create missing ones from `shopware-plugins` templates)
- [ ] Update class DocBlock annotations to correct order (description, `@method`, blank line, `@class`, `@package`)
- [ ] Remove unused code (dead PHP classes/methods, unreferenced JS/Vue components, unused Twig blocks, orphaned services, unused class properties)

## Quick Reference: Task → File

| Task | Reference | Example Template |
|------|-----------|------------------|
| sw-* → mt-* component mapping (all 25 components) | `references/component-mapping.md` | — |
| Full page/modal/list migration examples | `references/component-examples.md` | `examples/detail-page-after.html.twig`, `examples/modal-after.html.twig` |
| Webpack → Vite build migration | `references/build-system-migration.md` | `examples/vite.config.js` |
| Admin SDK package rename | `references/build-system-migration.md` | — |
| Vuex → Pinia state management | `references/state-management-migration.md` | `examples/pinia-store.js` |
| Constructor property promotion | `references/php-migration.md` | `examples/constructor-promotion.php` |
| Domain exception factory pattern | `references/php-migration.md` | `examples/domain-exception.php` |
| PHP Enums for constants | `references/php-migration.md` | — |
| Coding style rules | `references/php-migration.md` | `shopware-plugins/examples/coding-style.md` |
| composer.json version constraints | — | `examples/composer-67.json` |
| Composer packages audit & plugin file structure | `references/composer-packages-audit.md` | `shopware-plugins/examples/composer.json` |

## How to Use

1. Identify the migration task from the Quick Reference table
2. Read the corresponding `references/*.md` file for the full guide
3. Use `examples/*` templates as starting points where available
4. Follow `shopware-plugins/examples/coding-style.md` for all PHP conventions

## Codemod Tool

Shopware provides an automated ESLint-based codemod for admin component migration:

```bash
composer run admin:code-mods -- --plugin-name=YourPluginName --shopware-version=6.7 --fix
```

Options: `--shopware-root=PATH`, `--src=PATH`, `--ignore-git`. Always review output — the codemod adds `// TODO` comments for items requiring manual migration (especially `sw-data-grid` → `mt-data-table`).

## Key Changes at a Glance

### Administration: sw-* → mt-* Components

All `sw-*` wrappers are deprecated (removal in v6.8.0). The universal migration pattern:

| Pattern | Old (sw-*) | New (mt-*) |
|---------|-----------|------------|
| Value binding | `:value="x"` + `@input="fn"` | `v-model="x"` |
| Button danger | `variant="danger"` | `variant="critical"` |
| Button ghost | `variant="ghost"` | `variant="secondary" :ghost="true"` |
| Alert variants | `error` / `warning` / `success` | `critical` / `attention` / `positive` |
| Icon sizing | `:small` / `:large` | `size="16px"` / `size="32px"` |
| Modal sizing | `variant="large"` | `width="l"` |
| Popover | `sw-popover` | `mt-floating-ui` |
| Button router-link | `:router-link="{ name: 'x' }"` | `@click="$router.push({ name: 'x' })"` — kein `<router-link>` Wrapper |
| Password toggle | `:passwordToggleAble` | `:toggable` |
| Alert icon | `:showIcon="false"` | `:hideIcon="true"` |
| Tabs | Child `<sw-tabs-item>` components | `:items` array prop |
| `sw-page` / `sw-card-view` | — | **Kein Ersatz** — bleiben `sw-*`, kein `mt-page` vorhanden |
| `sw-skeleton` / `sw-skeleton-bar` | — | **Kein Ersatz** — `mt-skeleton` existiert nicht, nicht verwenden |

Full mapping with prop/event/slot tables for all 25 components: `references/component-mapping.md`
Detailed migration guide with real before/after examples for 19 deprecated wrapper components: `references/component-migration-guide.md`

### Administration: Build & State

| Change | Old | New |
|--------|-----|-----|
| Build tool | Webpack 5 | Vite 6 |
| State management | Vuex 4 (`Shopware.State`) | Pinia 2.3 (`Shopware.Store`) |
| Mutations | `Shopware.State.commit('module/mutation', val)` | `store.property = val` (direct) |
| Admin SDK | `@shopware-ag/admin-extension-sdk` | `@shopware-ag/meteor-admin-sdk@^6.4.0` |
| Component lib | — | `@shopware-ag/meteor-component-library@^4.24.0` |
| Vue | 2.7 / 3 compat | 3.5 |
| Module import | `require()` / `require.context()` | `import()` / `import.meta.glob()` |

### PHP

| Change | Old | New |
|--------|-----|-----|
| Constructor | Property + assignment | `private readonly` promoted parameters |
| Empty body | `{ }` on new line | `{}` on closing paren line |
| Exceptions | `throw new \RuntimeException(...)` | `throw MyPluginException::specificError(...)` |
| Constants | `class Status { const X = 'x'; }` | `enum Status: string { case X = 'x'; }` |

## Workflow

When migrating a plugin:

1. **Audit** — identify all sw-* components, Vuex usage, old SDK imports, non-promoted constructors
2. **Audit composer & files** — follow `references/composer-packages-audit.md` to verify `require-dev` packages and required plugin root files. Use `shopware-plugins` skill templates for missing files.
3. **Install dependencies** — run `composer install` inside the plugin via DDEV:
   ```bash
   ddev exec bash -c "cd shopware/custom/static-plugins/{PluginName} && composer install"
   ```
4. **Run Rector** — dry-run first, then apply. Rector handles constructor promotion, deprecated API replacements, and PHP-level changes:
   ```bash
   # Dry-run (review changes)
   ddev exec bash -c "cd shopware/custom/static-plugins/{PluginName} && composer run rector"
   # Apply
   ddev exec bash -c "cd shopware/custom/static-plugins/{PluginName} && vendor/bin/rector process --clear-cache"
   ```
5. **Run codemod** — `composer run admin:code-mods -- --plugin-name=YourPlugin --shopware-version=6.7 --fix`
6. **Review codemod output** — fix TODO comments using `references/component-mapping.md`
7. **Update build system** — follow `references/build-system-migration.md`. Delete these obsolete files and clean up empty directories afterward:
   - `src/Resources/app/administration/build/webpack.config.js` → remove `build/` if empty
   - `src/Resources/app/administration/src/init/svg-icons.init.js` → remove `init/` if empty
   - `src/Resources/app/administration/src/app/assets/icons/svg/ff-icon.svg`
   - `src/Resources/app/administration/src/app/assets/icons/icons.js`
   - Remove `src/Resources/app/administration/src/app/assets/` if it contains only empty directories
8. **Migrate state** — follow `references/state-management-migration.md`
9. **Update PHP** — fix remaining issues not covered by Rector, follow `references/php-migration.md`
10. **Remove unused code** — delete dead PHP classes/methods, unused class properties, unreferenced Vue/JS components, unused Twig blocks and template overrides, orphaned Symfony services and routes
11. **Update composer.json** — see `examples/composer-67.json`
12. **Build Storefront** — if any Storefront JS, SCSS, or Twig files were changed, trigger a storefront build:
    ```bash
    # Preferred (if shopware-cli available)
    ddev exec shopware-cli project storefront-build --only-extensions {PluginName}
    # Fallback
    ddev exec bash -c "cd shopware && bin/build-storefront.sh"
    ```
13. **Build Administration** — if any Admin Vue/JS files were changed, trigger an admin build:
    ```bash
    # Preferred (if shopware-cli available)
    ddev exec shopware-cli project admin-build --only-extensions {PluginName}
    # Fallback
    ddev exec bash -c "cd shopware && bin/build-administration.sh"
    ```
14. **Test** — verify pages, run PHPUnit

## Searching the Shopware Documentation

When you need up-to-date information from the Shopware developer docs, use the Algolia search API:

**Step 1 — Search:** POST to the Algolia endpoint, replacing `"query"` value with your search term:

```bash
curl -s -X POST \
  "https://j1y01x9hgm-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(5.19.0)%3B%20Lite%20(5.19.0)%3B%20Browser%3B%20docsearch%20(3.9.0)%3B%20docsearch-react%20(3.9.0)%3B%20docsearch.js%20(3.9.0)&x-algolia-api-key=711e1cadf66a3957aaf183a58aad12a7&x-algolia-application-id=J1Y01X9HGM" \
  -H "Content-Type: application/json" \
  -d '{
    "requests": [{
      "query": "YOUR_SEARCH_TERM",
      "indexName": "beta-developer-shopware",
      "attributesToRetrieve": ["hierarchy.lvl0","hierarchy.lvl1","hierarchy.lvl2","hierarchy.lvl3","hierarchy.lvl4","hierarchy.lvl5","hierarchy.lvl6","content","type","url"],
      "attributesToSnippet": ["hierarchy.lvl1:10","hierarchy.lvl2:10","hierarchy.lvl3:10","hierarchy.lvl4:10","hierarchy.lvl5:10","hierarchy.lvl6:10","content:10"],
      "snippetEllipsisText": "…",
      "highlightPreTag": "<mark>",
      "highlightPostTag": "</mark>",
      "hitsPerPage": 30,
      "clickAnalytics": false,
      "filters": "version:main",
      "length": 30,
      "offset": 0
    }]
  }'
```

**Step 2 — Parse results:** The response contains `results[0].hits[]` sorted by relevance (best match first). Each hit has a `url` field pointing to the documentation page.

**Step 3 — Fetch the page:** Use `WebFetch` on the `url` from the top hit(s) to retrieve the full documentation content.

## Cross-References

- **Plugin scaffolding & development**: `shopware-plugins` skill
- **Plugin file templates** (for missing files): `shopware-plugins/examples/` — use this skill to create any missing root files
- **Composer package versions**: Use WebFetch on Packagist JSON URLs as described in `shopware-plugins` skill (section "Resolving require-dev Package Versions")
- **Coding style**: `shopware-plugins/examples/coding-style.md`
- **Domain exceptions ADR**: `shopware-plugins/adr/2022-02-24-domain-exceptions.md`
- **Feature flags ADR**: `shopware-plugins/adr/2022-01-20-feature-flags-for-major-versions.md`
- **Admin SDK ADR**: `shopware-plugins/adr/2022-06-27-providing-the-admin-extension-sdk.md`

## Rules

1. README-Datei immer auf **Deutsch** erstellen.
2. `composer.json` `"version"`: Majorversion um 1 erhöhen, Minor und Patch auf 0 setzen (z.B. `1.3.2` → `2.0.0`).
3. Always review codemod output manually — never trust automated migration blindly.
4. `sw-data-grid` → `mt-data-table` always requires manual migration.
5. `mt-skeleton` does not exist — never use it; there is no Meteor replacement for `sw-skeleton`/`sw-skeleton-bar`.
6. `mt-text-editor` requires feature flag `METEOR_TEXT_EDITOR`.
7. Vuex is deprecated, not removed — but migrate now to avoid v6.8 breakage.
8. All PHP code must follow `shopware-plugins/examples/coding-style.md`.
9. Use `Shopware.Store.register()` (not `defineStore()` directly) for Pinia stores.
10. Class DocBlock annotation order: description/`@method` first, then blank line, then `@class` and `@package` last.
11. Rector config for 6.7 must use `ShopwareSetList::SHOPWARE_6_7_0` and `ShopwareSetList::SHOPWARE_6_8_0` sets only.
12. During migration: remove unused code — PHP classes/methods with no references, unused class properties, Vue/JS components not registered or imported, Twig blocks that only call `parent()` with no additions, orphaned service definitions in `services.xml`.
13. After all changes: run a **Storefront build** if any Storefront JS/SCSS/Twig files were modified; run an **Admin build** if any Administration Vue/JS files were modified. Use `shopware-cli` if available, otherwise fall back to `bin/build-storefront.sh` / `bin/build-administration.sh`.
