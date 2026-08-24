---
name: sw-changelog
description: Adds a changelog entry to a Shopware 6 plugin (Keep a Changelog) and optionally bumps the version in composer.json.
argument-hint: [--plugin <PluginName>] [--bump major|minor|patch]
allowed-tools: Read, Glob, Grep, Write, Edit
model: haiku
---

# /sw-changelog

Maintain the plugin changelog. Skill: `sw-release`.

## Steps
1. Settle the target plugin and the changes — ask, or derive them from the git diff; categories are
   Added, Changed, Fixed and Removed.
2. Extend `CHANGELOG.md` (creating it where absent) with a new version section and date, newest
   first.
3. With `--bump`, raise `version` in `composer.json` accordingly (semver) and keep the two
   consistent.

Never edit an existing entry — only add new ones.
