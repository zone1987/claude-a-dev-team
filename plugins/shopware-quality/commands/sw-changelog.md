---
name: sw-changelog
description: Fügt einem Shopware-6-Plugin einen Changelog-Eintrag hinzu (Keep-a-Changelog) und bumpt optional die Version in composer.json.
argument-hint: [--plugin <PluginName>] [--bump major|minor|patch]
allowed-tools: Read, Glob, Grep, Write, Edit
model: haiku
---

# /sw-changelog

Pflege den Plugin-Changelog. Skill: `sw-changelog`.

## Ablauf
1. Ziel-Plugin + Änderungen erfragen/aus git-diff ableiten; Kategorien Added/Changed/Fixed/Removed.
2. `CHANGELOG.md` (anlegen falls fehlt) mit neuem Versions-Abschnitt + Datum ergänzen (neueste oben).
3. Bei `--bump` die `version` in `composer.json` entsprechend erhöhen (semver) und konsistent halten.

Bestehende Einträge nie ändern — nur neue hinzufügen.
