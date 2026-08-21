# Shopware 6 — Vuex → Pinia (admin state)

Pinia is the new standard (ADR "replace Vuex with Pinia"). Migrate custom Vuex modules to `Shopware.Store`.

| Vuex (old) | Pinia (new) |
|---|---|
| `Shopware.State.registerModule('x', {...})` | `Shopware.Store.register('x', {...})` |
| `state` as an object | `state: () => ({...})` |
| `mutations` | directly in `actions` (no commit) |
| `getters` (with state arg) | `getters` |
| `Shopware.State.get('x')` / `mapState` | `Shopware.Store.get('x')` |

Replace component accesses (`mapState`/`mapGetters`) with direct `Shopware.Store.get(...)` access.
Core legacy stores partly remain readable via `Shopware.State`. Details: references of the `shopware-6.7-migration` skill.

→ [../shopware-6.7-migration/`VUEX-TO-PINIA-STATE-MANAGEMENT-MIGRATION.md`](../shopware-6.7-migration/`VUEX-TO-PINIA-STATE-MANAGEMENT-MIGRATION.md`)
