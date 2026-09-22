---
name: sw-migrate-component
description: Migrates an administration component or template from legacy sw-* to Meteor mt-* (Shopware 6.7), adjusting props, events and slots.
argument-hint: <path-or-component> [--plugin <PluginName>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-migrate-component

Migrates administration components from `sw-*` to Meteor `mt-*`. Skill: `sw-admin`.

## Steps

1. Read the target file and find every `sw-*` component in the template.
2. Per component: replace it with its `mt-*` counterpart, adjust props and events
   (`v-model` → `v-model:value` where needed, renamed events and props), check the slots.
3. **Every `mt-button` gets `size="default"` explicitly.** The component defaults to
   `size="small"` — 32 pixels against the 40 of every core control beside it.
   → `shopware-admin` → `sw-meteor` → `COMPONENTS.md`
4. Resolve the deprecation warnings.
5. Run `npm --prefix src/Resources/app/administration run lint:js:fix` and
   `composer test:admin` — Jest enforces 100 % on all four metrics, so a migrated
   component with a changed API fails the suite rather than the browser.
6. Rebuild and look at it:
   `ddev exec shopware-cli project admin-build --only-extensions <PluginName>`.

**A component with no Meteor counterpart in this version stays as it is** and goes into
`UPGRADE-<next>.md` instead. Writing code for a version the plugin declares a conflict
with produces code the shop is not allowed to run.

Mapping table and examples: the `sw-admin` skill. For a wholesale rebuild, hand over to
`shopware-migration:shopware-migrator`.

## Before it counts as done

`composer gate` green, `composer test:admin` green, and the component seen in the browser.
→ `shopware-testing` → `sw-testing-standard`
