---
name: sw-javascript
description: Shopware JavaScript testing: Jest for the administration and the storefront, Vue component tests. Use when writing a Jest or Vue test for Shopware.
---

# Shopware JavaScript testing

Jest with Shopware's own setup. Administration and storefront have different configurations.

## Read the standard first

**[`sw-testing-standard`](../sw-testing-standard/SKILL.md) decides what must exist**; this
skill covers how to write it.

- **`STANDARD-JEST-ADMIN.md`** and **`STANDARD-JEST-STOREFRONT.md`** carry the complete,
  running configurations for a *plugin* — Shopware ships none, so every file is the
  plugin's own. **If the setup does not exist yet, it is created.**
- **100 % coverage, enforced by `coverageThreshold`.** Every component, function,
  statement, method, button, page, dropdown, flow and mixin the plugin ships. The run
  fails below it, so a gap cannot reach the branch quietly.
- **Dead code is deleted, not covered.** A branch that cannot be true is removed; a test
  written only to reach a line is what the mutation rules forbid.

## Reference map

- **[JEST-ADMIN.md](references/JEST-ADMIN.md)**: Admin JS/Vue tests run with Jest.
- **[JEST-STOREFRONT.md](references/JEST-STOREFRONT.md)**: Test storefront JS plugins with Jest.
- **[VUE-TEST.md](references/VUE-TEST.md)**: Test admin components with `@vue/test-utils`; obtain the final component through `Shopware.Component.build`.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
