---
name: sw-js-plugin-map
description: Scannt das aktuelle Shopware-Projekt nach JavaScript-Storefront-Plugins UND JS-Events (Core + custom) und erzeugt/aktualisiert .shopware-catalog/js-plugins.md (Name, Datei, Aufgabe, Selector, Optionen, Registrierung, Overrides) und .shopware-catalog/js-events.md (Event-Name, Publish-/Subscribe-Orte, Argumente).
argument-hint: [--custom-only]
allowed-tools: Read, Glob, Grep, Bash, Write, Task
model: haiku
---

# /sw-js-plugin-map

Erzeuge/aktualisiere den JS-Plugin-Katalog. Delegiere an den Agent `shopware-js-plugin-mapper`
(Skill `sw-js-plugin-catalog`).

## Ablauf
1. Scan-Bereich: Core-Storefront (`vendor/shopware/storefront/Resources/app/storefront/src/plugin/**`) + custom
   (`custom/plugins/*/src/Resources/app/storefront/src/**`). Bei `--custom-only` nur custom.
2. Erfasse Plugin-Klassen (`*.plugin.js`), `static options`/Optionen und die `PluginManager.register/override/extend`-
   Einträge (Name ↔ Selector ↔ Klasse).
3. Schreibe `.shopware-catalog/js-plugins.md` (Plugins) **und** `.shopware-catalog/js-events.md` (JS-Events:
   Publish-/Subscribe-Orte, Argumente/`detail`, Typ) — Formate aus `sw-js-plugin-catalog`/`sw-js-event-catalog`.
4. Kopf mit Scan-Datum/Bereich/Anzahl; Kurzzusammenfassung ausgeben.

Effizient via grep (`PluginManager.register|override|extend`, `class .*Plugin`, `\$emitter\.(publish|subscribe)`,
`dispatchEvent\(new CustomEvent`). Nur real Vorhandenes.
