---
name: sw-migration
description: Scaffold einer Shopware-6 Datenbank-Migration (MigrationStep) mit korrektem Timestamp, update()/updateDestructive() und Shopware-Konventionen (BINARY(16) id, DATETIME(3)).
argument-hint: <Beschreibung> [--plugin <PluginName>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-migration

Erzeuge eine Migration im Ziel-Plugin. Skill: `sw-database-migration`.

## Ablauf
1. Beschreibung (PascalCase) + Ziel-Plugin bestimmen. Timestamp = aktuelle Unix-Zeit (eindeutig, größer als bestehende).
2. Zielordner `src/Migration/` (bzw. `src/Migration/V6_7/`), Klasse `Migration{ts}{Beschreibung}` extends `MigrationStep`.
3. `getCreationTimestamp()`, `update(Connection)` (non-destructive, `CREATE TABLE IF NOT EXISTS` / additive `ALTER`),
   `updateDestructive(Connection)` (löschende Änderungen) implementieren.
4. Konventionen: `id BINARY(16)`, `created_at DATETIME(3) NOT NULL`, `updated_at DATETIME(3) NULL`, InnoDB/utf8mb4,
   FKs mit passenden ON DELETE-Regeln.
5. Hinweis: `bin/console database:migrate --all <PluginName>` (destructive separat via `--all` nach Deprecation-Frist).

Niemals bestehende Migrationen ändern — immer neue anlegen. SQL parametrisiert/idempotent halten.
