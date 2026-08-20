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

**Tiefe Referenz-Dokumentation:**
- Alle mt-*-Komponenten (Props/Events/Slots): `COMPONENTS-DETAIL.md`
- Meteor Icon Kit (Namensschema, Icon-Liste): `COMPONENTS-ICON-KIT.md`
- Design-Tokens (CSS-Custom-Properties): `COMPONENTS-TOKENS.md`
