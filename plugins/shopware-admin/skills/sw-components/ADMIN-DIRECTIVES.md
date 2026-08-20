# Shopware 6 — Admin directives

Use the admin's built-in Vue directives in the template:

```twig
<mt-button v-tooltip="{ message: $tc('ff.hint') }">…</mt-button>
<input v-autofocus />
```

Common ones: `v-tooltip`, `v-autofocus`, `v-draggable`/`v-droppable` (drag & drop), `v-responsive`. Your own directive:

```js
Shopware.Directive.register('ff-highlight', { mounted(el, binding) { el.style.outline = binding.value; } });
```

For purely stylistic/layout adjustments, SCSS is usually preferable (`sw-admin-styles`).
