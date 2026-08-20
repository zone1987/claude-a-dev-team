# Shopware 6 — Vuex → Pinia (Admin-State)

Pinia ist der neue Standard (ADR „replace Vuex with Pinia"). Eigene Vuex-Module nach `Shopware.Store` migrieren.

| Vuex (alt) | Pinia (neu) |
|---|---|
| `Shopware.State.registerModule('x', {...})` | `Shopware.Store.register('x', {...})` |
| `state` als Objekt | `state: () => ({...})` |
| `mutations` | direkt in `actions` (kein commit) |
| `getters` (mit state-Arg) | `getters` |
| `Shopware.State.get('x')` / `mapState` | `Shopware.Store.get('x')` |

Komponenten-Zugriffe (`mapState`/`mapGetters`) durch direkten `Shopware.Store.get(...)`-Zugriff ersetzen.
Core-Legacy-Stores bleiben teils über `Shopware.State` lesbar. Details: References des Skills `shopware-6.7-migration`.

→ [../shopware-6.7-migration/`VUEX-TO-PINIA-STATE-MANAGEMENT-MIGRATION.md`](../shopware-6.7-migration/`VUEX-TO-PINIA-STATE-MANAGEMENT-MIGRATION.md`)
