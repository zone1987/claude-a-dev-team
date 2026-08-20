# Shopware 6 — Admin-Direktiven

Eingebaute Vue-Direktiven der Admin im Template nutzen:

```twig
<mt-button v-tooltip="{ message: $tc('ff.hint') }">…</mt-button>
<input v-autofocus />
```

Häufig: `v-tooltip`, `v-autofocus`, `v-draggable`/`v-droppable` (Drag&Drop), `v-responsive`. Eigene Direktive:

```js
Shopware.Directive.register('ff-highlight', { mounted(el, binding) { el.style.outline = binding.value; } });
```

Für reine Stil-/Layout-Anpassungen meist SCSS bevorzugen (`sw-admin-styles`).
