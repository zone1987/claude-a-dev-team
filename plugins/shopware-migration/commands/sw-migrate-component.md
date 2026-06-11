---
name: sw-migrate-component
description: Migriert eine Admin-Komponente/ein Template von Legacy sw-* auf Meteor mt-* (Shopware 6.7) inkl. Props/Events/Slots-Anpassung.
argument-hint: <pfad-oder-komponente> [--plugin <PluginName>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-migrate-component

Migriere Admin-Komponente(n) von `sw-*` zu Meteor `mt-*`. Skill: `sw-meteor-component-map`.

## Ablauf
1. Ziel-Datei/Komponente lesen; alle `sw-*`-Komponenten im Template finden.
2. Pro Komponente: durch `mt-*`-Pendant ersetzen, Props/Events anpassen (`v-model` → `v-model:value` wo nötig,
   geänderte Event-Namen/Props), Slots prüfen.
3. Deprecation-Warnungen auflösen; `composer eslint:admin:fix` empfehlen.
4. Hinweis: visuell/funktional prüfen (Admin-Watcher), ggf. Tests anpassen.

Mapping-Tabelle/Beispiele im Skill `sw-meteor-component-map`. Bei breitem Umbau an `shopware-migrator` übergeben.
