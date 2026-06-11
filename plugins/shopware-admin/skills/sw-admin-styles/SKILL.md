---
name: sw-admin-styles
description: >
  Styling im Shopware-6-Admin: SCSS in der Komponente (<name>.scss), BEM-Konvention, Meteor-Design-Tokens/Variablen,
  responsive. Trigger: "Admin SCSS", "Komponente Styling admin", "BEM admin", "admin css", "design tokens admin",
  "styles administration". Shopware 6.7.
---

# Shopware 6 — Admin-Styling

Pro Komponente eine `.scss` neben `index.js`/`.twig`, importiert im Komponenten-`index.js`. BEM-Namensschema mit
Komponenten-Präfix.

```scss
// ff-example-card.scss
.ff-example-card {
    &__title { font-weight: 600; }
    &--active { border-color: var(--color-shopware-brand-500); }
}
```

Meteor/Admin-Design-Tokens als CSS-Custom-Properties (`--color-*`, Spacing) nutzen — keine Hardcodes. Lint:
`composer stylelint` / `eslint:admin`. Build via Vite (`sw-admin-vite`). UI-Bausteine: Meteor-Komponenten (`sw-meteor-components`).
