---
name: sw-migration
description: Scaffold a Shopware 6 database migration (MigrationStep) with the correct timestamp, update()/updateDestructive() and Shopware conventions (BINARY(16) id, DATETIME(3)).
argument-hint: <Description> [--plugin <PluginName>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-migration

Create a migration in the target plugin. Skill: `sw-write`.

## Steps
1. Determine the description (PascalCase) and the target plugin. Timestamp = the current Unix time (unique, higher than existing ones).
2. Target directory `src/Migration/` (or `src/Migration/V6_7/`), class `Migration{ts}{Description}` extends `MigrationStep`.
3. Implement `getCreationTimestamp()`, `update(Connection)` (non-destructive, `CREATE TABLE IF NOT EXISTS` / additive `ALTER`),
   and `updateDestructive(Connection)` (the deleting changes).
4. Conventions: `id BINARY(16)`, `created_at DATETIME(3) NOT NULL`, `updated_at DATETIME(3) NULL`, InnoDB/utf8mb4,
   foreign keys with suitable ON DELETE rules.
5. Point out `bin/console database:migrate --all <PluginName>` (destructive runs separately, after the deprecation period).

Never change an existing migration — always add a new one. Keep SQL parameterised and idempotent.
