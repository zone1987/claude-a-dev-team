---
name: sw-vuex-to-pinia
description: >
  Migration des Admin-State von Vuex zu Pinia (Shopware 6.6→6.7): Shopware.State → Shopware.Store, Mutations→Actions,
  mapState/mapGetters ersetzen. Trigger: "Vuex zu Pinia", "Shopware.State migration", "Pinia migration admin",
  "state management migration shopware", "registerModule pinia". Shopware 6.7.
---

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

→ [../shopware-6.7-migration/references/state-management-migration.md](../shopware-6.7-migration/references/state-management-migration.md)
