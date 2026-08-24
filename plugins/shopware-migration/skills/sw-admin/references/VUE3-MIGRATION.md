# Shopware — migrating the administration to Vue 3

Shopware 6.6 moved the administration to Vue 3 (Vue 2 reached end of life on 31 December 2023).
**6.7 removed the Vue migration build**, so a plugin can no longer lean on Vue 2 behaviour: it has to
be fully Vue 3.

## Contents

- [Who is affected](#who-is-affected)
- [The step-by-step pass](#the-step-by-step-pass)
- [APIs the migration build used to cover](#apis-the-migration-build-used-to-cover)
- [Known issues](#known-issues)

## Who is affected

| Extension type | Affected |
|---|---|
| App-based | no |
| Plugin-based with custom administration code | yes, refactoring likely |

**One plugin version cannot serve both 6.5 and 6.6+.** It needs separate versions in the store — `1.x`
for 6.5.x, `2.0` for 6.6 and newer.

A full rewrite is not needed; the effort scales with how much of Vue's internal API the plugin uses.
Enabling eslint's Vue 3 rule set automates part of the check.

## The step-by-step pass

Have the latest `trunk` or a release candidate, the plugin installed and active, and
`composer run watch:admin` running.

1. **Align `package.json`** with the administration's dependencies.
2. **Templates**, in any order: replace every `sw-field` with its specific component; check `v-model`
   usages, event listeners, deprecated slot syntax, `router-view` transition combinations, `key`
   attributes and filter usages.
3. **Code**: search for **`this.$`**. That prefix marks Vue's internal API, and those calls are very
   likely to break — `this.$tc` being the exception.

## APIs the migration build used to cover

These are the changes seen most often in Shopware's own codebase. The list is not exhaustive; the
official Vue 3 migration guide is.

**`$listeners` removed** — event listeners are part of `$attrs` in Vue 3.

**`$scopedSlots` removed** — `$slots` unifies all slots and exposes them as functions:

```js
this.$scopedSlots.header    // Vue 2
this.$slots.header()        // Vue 3
```

**`$children` removed** — use a template ref:

```js
this.$children.childrenMethod();          // Vue 2
this.$refs.childrenRef.childrenMethod();  // Vue 3
```

**`$on`, `$off`, `$once` removed, with no replacement.** `$emit` still works for handlers a parent
attached declaratively. Otherwise use provide/inject with a registration pattern — there is no
general recipe, it depends on the case:

```js
// Vue 2
created() {
    this.$parent.$on('doSomething', this.eventHandler);
},
beforeDestroy() {
    this.$parent.$off('doSomething', this.eventHandler);
}

// Vue 3 — the parent provides the handler
inject: ['registerDoSomething', 'unregisterDoSomething'],
created() {
    this.registerDoSomething(this.eventHandler);
},
beforeDestroy() {
    this.unregisterDoSomething(this.eventHandler);
}
```

**`$set` and `$delete` removed** — Vue 3's reactivity is built on ES6 proxies, so plain assignment is
reactive:

```js
this.$set(this.myObject, 'key', 'value');   // Vue 2
this.$delete(this.myObject, 'key');

this.myObject.key = 'value';                // Vue 3
delete this.myObject.key;
```

## Known issues

**Lifecycle hooks fire more than once.** For an asynchronously loaded component Vue 3 emits the hook
for the `AsyncComponentWrapper` *and* the component, so `@hook:mounted` may run twice. Only use such
hooks where running twice is harmless.

**Checking for a slot changed.** A property on `this.$slots` no longer proves the slot exists — verify
that `slotName` actually contains a v-node.

**`this.$parent` is unreliable.** Vue 3 wraps async components in an `AsyncWrapperComponent`, so the
virtual DOM tree differs: where Vue 2 needed `this.$parent`, Vue 3 may need
`this.$parent.$parent`. Avoid it altogether — it is an anti-pattern; use services or events.

**Vue DevTools cripples performance** in large Vue 3 applications. The GitHub issue has seen next to
no maintainer activity.

**`v-model` has several breaking changes** — consult the official guide.

**Vuex loses reactivity** if a getter alters state data.

**Form field ids changed.** Administration fields no longer carry the previous id, which was used
almost exclusively in tests. Add a `name` attribute with a unique value to fix a failing test.

**Prop defaults lost `this`.** A default function has no access to the component scope, so
`this.$tc` is unavailable — use `Shopware.Snippet.tc`.

**Mutating a prop now fails hard.** It was always an anti-pattern; Vue 2 simply did not always detect
it.

## Source

- [administration/vue3.html](https://developer.shopware.com/docs/guides/upgrades-migrations/administration/vue3.html) — the 6.6 upgrade, FAQ and known issues
- [administration/vue-migration-build.html](https://developer.shopware.com/docs/guides/upgrades-migrations/administration/vue-migration-build.html) — the APIs the removed migration build covered

Shopware 6.7, retrieved 2026-08-21.
