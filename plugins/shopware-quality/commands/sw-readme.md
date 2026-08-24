---
name: sw-readme
description: Generates or updates a README for a Shopware 6 plugin following the established schema (installation, configuration, features, compatibility).
argument-hint: [--plugin <PluginName>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-readme

Create or update the plugin README. Skill: `sw-release` (the schema and structure).

## Steps
1. Settle the target plugin; read `composer.json` (name, label, version, target Shopware version)
   and the features already present in the code.
2. Write the README to the schema: title and description, installation
   (`plugin:install --activate`), configuration, features, compatibility (the Shopware version), and
   licence or support where they apply.
3. Respect an existing README — update and extend it rather than overwriting it blindly.

The changelog is separate: `/sw-changelog`.
