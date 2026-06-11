---
name: sw-meteor-components
description: >
  Die Meteor-Komponentenbibliothek im Shopware-6.7-Admin: mt-*-Komponenten (mt-card, mt-button, mt-text-field,
  mt-select, mt-banner, mt-modal, mt-tabs, mt-data-table ...), Props/Events, Verhältnis zu Legacy sw-*. Trigger:
  "Meteor component", "mt-card", "mt-button", "mt-text-field", "mt-select", "mt-modal", "welche Admin-Komponente",
  "sw- vs mt-". Shopware 6.7.
---

# Shopware 6 — Meteor-Komponenten (mt-*)

In 6.7 ist die **Meteor Component Library** (`mt-*`) der Standard-Baukasten (löst Legacy `sw-*` ab,
ADR „implementation of meteor component library").

| Meteor | Zweck (Legacy sw-*) |
|---|---|
| `mt-card` | Container (`sw-card`) |
| `mt-button` | Button (`sw-button`) |
| `mt-text-field` / `mt-textarea` / `mt-number-field` | Eingaben (`sw-text-field` …) |
| `mt-select` / `mt-entity-single-select` | Auswahl |
| `mt-switch` / `mt-checkbox` | Bool |
| `mt-banner` | Hinweise (`sw-alert`) |
| `mt-modal` | Dialog (`sw-modal`) |
| `mt-tabs` | Tabs |
| `mt-data-table` | Tabelle |
| `mt-icon` | Icon |

Props/Events teils anders als bei `sw-*` (z.B. `v-model:value`, Event-Namen). Bei Migration bestehender Plugins
Mapping beachten (Plugin `shopware-migration` → `sw-meteor-component-map`). Neue UIs immer mit `mt-*` bauen.
