# Shopware 6 — Admin state (Vuex, legacy)

Vuex is **deprecated** (replaced by Pinia). Relevant only for existing core stores that are
reachable via `Shopware.State`.

```js
const context = Shopware.State.get('context');     // Reading a core Vuex store
```

For **new** code use Pinia (`sw-admin-pinia-store`). Migrate your own existing Vuex stores to `Shopware.Store`:
`state` as a function, mutations → directly into actions, `mapState`/`mapGetters` → `Shopware.Store.get`.
The 6.6→6.7 migration is described in the `shopware-migration` plugin.
