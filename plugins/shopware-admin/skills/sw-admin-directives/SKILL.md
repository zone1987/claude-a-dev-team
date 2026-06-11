---
name: sw-admin-directives
description: >
  Direktiven im Shopware-6-Admin: eingebaute Direktiven (v-tooltip, v-autofocus, v-droppable/v-draggable) nutzen,
  eigene Direktive via Shopware.Directive.register. Trigger: "Admin Directive", "v-tooltip", "Shopware.Directive.register",
  "eigene Direktive admin", "v-autofocus", "drag drop directive". Shopware 6.7.
---

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
