---
name: sw-admin-map
description: Scannt das aktuelle Shopware-Projekt (Core-Administration + custom) und erzeugt/aktualisiert den Admin-Katalog .shopware-catalog/admin.md (Module, Komponenten, Services, Stores, Mixins, Direktiven, Filter, ApiServices).
argument-hint: [--custom-only]
allowed-tools: Read, Glob, Grep, Bash, Write, Task
model: haiku
---

# /sw-admin-map

Erzeuge/aktualisiere den Admin-Katalog. Delegiere an den Agent `shopware-admin-mapper` (Skill `sw-admin-catalog`).

## Ablauf
1. Scan-Bereich: Core `vendor/shopware/administration/Resources/app/administration/src/**` + custom
   `custom/plugins/*/src/Resources/app/administration/src/**`. Bei `--custom-only` nur custom.
2. Erfasse Registrierungen: `Module.register`, `Component.register/override`, `addServiceProvider`, `Store.register`,
   `Mixin.register`, `Directive.register`, `Filter.register`, `extends *ApiService`.
   Pro Komponente zusätzlich **Props, Events, Slots (`<slot name>`) und Twig-Blocks (`{% block %}`)** + Zweck erfassen
   (auch genutzte/registrierte Meteor `mt-*` bzw. Core `sw-*`).
3. Schreibe `.shopware-catalog/admin.md` (Abschnitte Module/Components/Services/Stores/Mixins/Directives/Filters/ApiServices).
4. Kopf mit Scan-Datum/Bereich/Anzahl; Kurzzusammenfassung ausgeben.

Effizient via grep. Nur real vorhandene Bausteine — nichts erfinden.
