---
name: sw-structure-map
description: Scan this Shopware project for its plugins, apps and theme plugins, record which storefront templates and blocks each overrides, and write .shopware-catalog/structure.md.
argument-hint: "[--refresh]"
allowed-tools: Read, Glob, Grep, Bash, Write, Task
model: haiku
---

Build the project's storefront structure catalogue.

1. If `.shopware-catalog/structure.md` exists and `--refresh` was not given, report its date and the
   counts it records, then stop. Regenerating a current catalogue wastes a scan.
2. Otherwise delegate to `shopware-storefront:shopware-structure-mapper`.
3. Report: extensions found by directory, which are theme plugins, how many storefront templates and
   blocks are overridden, own CMS elements and JS plugins, and every core template overridden by
   more than one extension.

Run this after installing or updating an extension, after a Shopware update, and before planning any
storefront change — an extension may already override the template in question.

The core structure is documented in the `sw-structure` skill; this command records only what this
project adds. Invent nothing, and name what you could not determine.
