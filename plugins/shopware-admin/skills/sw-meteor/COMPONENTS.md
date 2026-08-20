# Shopware 6 — Meteor components (mt-*)

In 6.7 the **Meteor Component Library** (`mt-*`) is the standard toolkit (replaces legacy `sw-*`,
ADR "implementation of meteor component library").

| Meteor | Purpose (legacy sw-*) |
|---|---|
| `mt-card` | Container (`sw-card`) |
| `mt-button` | Button (`sw-button`) |
| `mt-text-field` / `mt-textarea` / `mt-number-field` | Inputs (`sw-text-field` …) |
| `mt-select` / `mt-entity-single-select` | Selection |
| `mt-switch` / `mt-checkbox` | Boolean |
| `mt-banner` | Notices (`sw-alert`) |
| `mt-modal` | Dialog (`sw-modal`) |
| `mt-tabs` | Tabs |
| `mt-data-table` | Table |
| `mt-icon` | Icon |

Props/events partly differ from `sw-*` (e.g. `v-model:value`, event names). When migrating existing plugins
observe the mapping (plugin `shopware-migration` → `sw-meteor-component-map`). Always build new UIs with `mt-*`.

**Deep reference documentation:**
- All mt-* components (props/events/slots): `COMPONENTS-DETAIL.md`
- Meteor Icon Kit (naming scheme, icon list): `COMPONENTS-ICON-KIT.md`
- Design tokens (CSS custom properties): `COMPONENTS-TOKENS.md`
