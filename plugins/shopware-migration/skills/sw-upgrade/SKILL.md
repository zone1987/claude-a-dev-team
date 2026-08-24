---
name: sw-upgrade
description: Shopware upgrades: the 6.6 to 6.7 to 6.8 path, release notes, resolving deprecations, PHP-side migration patterns. Use when upgrading a Shopware plugin to a newer version.
---

# Shopware version upgrades

What breaks between versions and how to fix it. Start with the deprecation list for your target version.

## Reference map

The 6.7 path, in the order an upgrade needs them:

- **[MIGRATION-67-OVERVIEW.md](references/MIGRATION-67-OVERVIEW.md)**: the 6.6 to 6.7 path itself.
- **[MIGRATION-67-COMPONENT-GUIDE.md](references/MIGRATION-67-COMPONENT-GUIDE.md)**: how to convert
  an administration component, step by step.
- **[MIGRATION-67-COMPONENT-MAPPING.md](references/MIGRATION-67-COMPONENT-MAPPING.md)**: which
  `sw-*` component becomes which `mt-*` one.
- **[MIGRATION-67-COMPONENT-EXAMPLES.md](references/MIGRATION-67-COMPONENT-EXAMPLES.md)**: worked
  before-and-after conversions.
- **[MIGRATION-67-STATE-MANAGEMENT.md](references/MIGRATION-67-STATE-MANAGEMENT.md)**: Vuex to Pinia.
- **[MIGRATION-67-BUILD-SYSTEM.md](references/MIGRATION-67-BUILD-SYSTEM.md)**: Webpack to Vite.
- **[MIGRATION-67-PHP.md](references/MIGRATION-67-PHP.md)**: changed PHP signatures and APIs.
- **[MIGRATION-67-COMPOSER-AUDIT.md](references/MIGRATION-67-COMPOSER-AUDIT.md)**: which packages
  need a version bump.

Component reference, every prop, slot, event and example the generator extracted. Each bundle opens
on a table of contents linking every component in it, so look one up by name:

- **[MT-COMPONENTS.md](references/MT-COMPONENTS.md)**: all 58 Meteor `mt-*` components — the
  migration targets.
- **[SW-COMPONENTS-A-E.md](references/SW-COMPONENTS-A-E.md)**: 391 `sw-*` components, `sw-address`
  to `sw-extension-*`.
- **[SW-COMPONENTS-F-M.md](references/SW-COMPONENTS-F-M.md)**: 176 components, `sw-field` to
  `sw-multi-select`.
- **[SW-COMPONENTS-N-S.md](references/SW-COMPONENTS-N-S.md)**: 370 components, `sw-notification` to
  `sw-system-config`.
- **[SW-COMPONENTS-T-Z.md](references/SW-COMPONENTS-T-Z.md)**: 49 components, `sw-tabs` to
  `sw-users-permissions-*`.

Across versions:

- **[OVERVIEW.md](references/OVERVIEW.md)**: the upgrade sequence version by version.
- **[LANGUAGE-PACK.md](references/LANGUAGE-PACK.md)**: the Language Pack plugin becomes incompatible in 6.8; the translation:install path out of it.
- **[DEPRECATION-HANDLING.md](references/DEPRECATION-HANDLING.md)**: finding and resolving
  deprecations.
- **[PHP-MIGRATION-PATTERNS.md](references/PHP-MIGRATION-PATTERNS.md)**: PHP-side migration patterns.
- **[RELEASE-NOTES.md](references/RELEASE-NOTES.md)**: what each release changed.
- **[RELEASE-NOTES-67.md](references/RELEASE-NOTES-67.md)**: the 6.7 release notes in full.
- **[RELEASE-NOTES-VERSION-HIGHLIGHTS.md](references/RELEASE-NOTES-VERSION-HIGHLIGHTS.md)**: the
  headline change per version.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20. Upgrade notes come from the UPGRADE-*.md files in the shopware/shopware repository.
