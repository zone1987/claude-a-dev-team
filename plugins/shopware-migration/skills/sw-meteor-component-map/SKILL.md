---
name: sw-meteor-component-map
description: >
  Migration der Shopware-Admin-Komponenten von sw-* zu Meteor mt-* (6.6→6.7): Komponenten-Mapping, geänderte Props/Events/
  Slots, v-model:value, Ersetzungsstrategie. Trigger: "sw- zu mt-", "Meteor migration", "mt-button mt-text-field mt-select",
  "Komponenten mapping shopware", "sw-card mt-card", "v-model:value meteor". Shopware 6.7.
---

# Shopware 6 — sw-* → mt-* (Meteor) Migration

In 6.7 lösen Meteor-Komponenten (`mt-*`) die Legacy-`sw-*`-Komponenten ab. Migration = Komponenten ersetzen +
geänderte Props/Events/Slots anpassen.

| Legacy | Meteor | Häufige Änderung |
|---|---|---|
| `sw-card` | `mt-card` | Slots/Props teils anders |
| `sw-button` | `mt-button` | `variant`/`ghost` statt alter Props |
| `sw-text-field` | `mt-text-field` | `v-model:value` statt `v-model` |
| `sw-select`/`sw-single-select` | `mt-select` | Optionen/Events angepasst |
| `sw-alert` | `mt-banner` | — |
| `sw-modal` | `mt-modal` | — |

Vorgehen: Template-Komponenten ersetzen, `v-model` → `v-model:value` (wo nötig), Event-Namen prüfen, Deprecation-Warnungen
auflösen. Mapping-Details + Beispiele in den References des Skills `shopware-6.7-migration`.

→ [../shopware-6.7-migration/references/component-mapping.md](../shopware-6.7-migration/references/component-mapping.md), [../shopware-6.7-migration/references/component-examples.md](../shopware-6.7-migration/references/component-examples.md)
