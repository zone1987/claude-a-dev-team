# Shopware 6 — Admin-State (Vuex, Legacy)

Vuex ist **deprecated** (durch Pinia ersetzt). Relevant nur noch für bestehende Core-Stores, die über
`Shopware.State` erreichbar sind.

```js
const context = Shopware.State.get('context');     // Lesen eines Core-Vuex-Stores
```

Für **neuen** Code Pinia nutzen (`sw-admin-pinia-store`). Bestehende eigene Vuex-Stores nach `Shopware.Store`
migrieren: `state` als Funktion, Mutations → direkt in Actions, `mapState`/`mapGetters` → `Shopware.Store.get`.
Die 6.6→6.7-Migration ist im Plugin `shopware-migration` beschrieben.
