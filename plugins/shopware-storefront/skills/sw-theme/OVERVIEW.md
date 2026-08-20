# Shopware 6 — Theme

A theme is a plugin whose class implements `ThemeInterface`; its core is the `theme.json` in
`src/Resources/`.

```json
{
  "name": "FfTheme",
  "author": "A-Dev-Team",
  "views": ["@Storefront", "@Plugins", "@FfTheme"],
  "style": ["@Storefront", "app/storefront/src/scss/base.scss"],
  "script": ["@Storefront", "app/storefront/dist/storefront/js/ff-theme.js"],
  "asset": ["@Storefront", "app/storefront/src/assets"]
}
```

`theme.json` defines the view/style/script/asset order and the config fields (`sw-theme-config`).
Activate: `bin/console theme:change`; compile: `theme:compile`. Inheritance works through `@` references
(`sw-theme-inheritance`). Pure styling without a dedicated theme also works as plugin SCSS (`sw-storefront-scss`).
