# Shopware 6 — sw-* → mt-* (Meteor) migration

In 6.7, Meteor components (`mt-*`) supersede the legacy `sw-*` components. Migration = replace components +
adjust changed props/events/slots.

| Legacy | Meteor | Common change |
|---|---|---|
| `sw-card` | `mt-card` | Slots/props partly different |
| `sw-button` | `mt-button` | `variant`/`ghost` instead of old props |
| `sw-text-field` | `mt-text-field` | `v-model:value` instead of `v-model` |
| `sw-select`/`sw-single-select` | `mt-select` | Options/events adjusted |
| `sw-alert` | `mt-banner` | — |
| `sw-modal` | `mt-modal` | — |

Approach: replace template components, `v-model` → `v-model:value` (where needed), check event names, resolve deprecation
warnings. Mapping details + examples in the references of the `shopware-6.7-migration` skill.

→ [../shopware-6.7-migration/`METEOR-COMPONENT-MAP-COMPONENT-MAPPING.md`](../shopware-6.7-migration/`METEOR-COMPONENT-MAP-COMPONENT-MAPPING.md`), [../shopware-6.7-migration/`METEOR-COMPONENT-MAP-COMPONENT-EXAMPLES.md`](../shopware-6.7-migration/`METEOR-COMPONENT-MAP-COMPONENT-EXAMPLES.md`)
