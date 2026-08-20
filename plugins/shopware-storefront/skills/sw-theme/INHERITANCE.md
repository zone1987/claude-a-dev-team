# Shopware 6 — Theme inheritance

Themes inherit via `@` references in `theme.json`. The array order determines override priority
(later entries override earlier ones).

```json
"style": ["@Storefront", "@ParentTheme", "app/storefront/src/scss/base.scss"]
```

- `@Storefront` = default theme base (always first), then optionally a parent theme, and finally your own SCSS/JS.
- Import only **Bootstrap utilities/variables** (do not duplicate compiled CSS) — performance/ADR "atomic theme compilation".
- `views` controls Twig template resolution (template inheritance, `sw-twig-templates`).

When only extending an existing shop, plugin SCSS/template overrides are often the better choice than a separate theme.
