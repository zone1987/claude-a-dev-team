# shopware-migration

> Version upgrades of existing plugins (6.6 → 6.7 → 6.8).

`shopware-migration` guides the **upgrade of existing plugins** between Shopware major versions from a
**developer perspective** (updating a shop as an operator belongs to `shopware-merchant`).

Included: an **upgrade overview** (strategy, using `UPGRADE-*.md`/`RELEASE_INFO`, stepping through each minor/major)
and the concrete migration paths for **6.6 → 6.7 (→ 6.8)**: admin components **`sw-*` → Meteor `mt-*`** (mapping
of props/events/slots), **Webpack → Vite**, **Vuex → Pinia**, **PHP migration patterns** (changed signatures/
interfaces such as the new payment handler, modern PHP features) as well as systematic **deprecation handling**
(finding notices, Rector codemods, major feature flags). In addition, the admin-specific upgrade topics (Vue 3
transition, migration build, native Vue roadmap) and translation/language pack migration.

Specialist: **`shopware-migrator`** (opus); scaffolder/helper **`/sw-migrate-component`**. **When to use:** when
raising a plugin to a new Shopware version.

Part of the marketplace **[claude-a-dev-team](../../README.md)**. The knowledge is distilled from the official sources and embedded; each skill keeps its depth in flat SCREAMING-CASE.md reference files next to its `SKILL.md`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-migration@claude-a-dev-team
```

## Skills (2)

| Skill | Description |
|---|---|
| `sw-admin` | Shopware administration migration: sw-* to Meteor mt-* component mapping, Webpack to Vite, Vuex to Pinia. Use when migrating Shopware administration code to 6.7 |
| `sw-upgrade` | Shopware upgrades: the 6.6 to 6.7 to 6.8 path, release notes, resolving deprecations, PHP-side migration patterns. Use when upgrading a Shopware plugin to a newer version |

## Agents (1)

| Agent | Description |
|---|---|
| `shopware-migrator` | Specialist for Shopware 6 version upgrades of plugins (code migration): 6.6→6.7→6.8, admin sw-*→Meteor mt-*, Webpack→Vite, Vuex→Pinia, PHP signature/API changes, deprecations, Rector |

## Commands (1)

| Command | Description |
|---|---|
| `/sw-migrate-component` | Migrates an admin component/template from legacy sw-* to Meteor mt-* (Shopware 6.7), including related adjustments |
