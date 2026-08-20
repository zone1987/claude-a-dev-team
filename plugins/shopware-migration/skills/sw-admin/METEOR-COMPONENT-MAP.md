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

→ [../shopware-6.7-migration/`METEOR-COMPONENT-MAP-COMPONENT-MAPPING.md`](../shopware-6.7-migration/`METEOR-COMPONENT-MAP-COMPONENT-MAPPING.md`), [../shopware-6.7-migration/`METEOR-COMPONENT-MAP-COMPONENT-EXAMPLES.md`](../shopware-6.7-migration/`METEOR-COMPONENT-MAP-COMPONENT-EXAMPLES.md`)
