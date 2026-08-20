# Shopware 6 — Admin styling

One `.scss` per component next to `index.js`/`.twig`, imported in the component's `index.js`. BEM naming scheme with
a component prefix.

```scss
// ff-example-card.scss
.ff-example-card {
    &__title { font-weight: 600; }
    &--active { border-color: var(--color-shopware-brand-500); }
}
```

Use Meteor/admin design tokens as CSS custom properties (`--color-*`, spacing) — no hardcoded values. Lint:
`composer stylelint` / `eslint:admin`. Build via Vite (`sw-admin-vite`). UI building blocks: Meteor components (`sw-meteor-components`).
