---
title: Apps as Themes
impact: MEDIUM
impactDescription: Apps with theme.json become assignable themes per sales channel
tags: storefront, themes, theme-json, sales-channel
---

## Apps as Themes

Apps can function as full themes by including a `theme.json` file.

### Key Difference

| Aspect | Standard App | Theme App (with theme.json) |
|--------|-------------|----------------------------|
| Visibility | Active on all sales channels | Only visible when assigned to a sales channel |
| Activation | Automatic on install | Requires explicit assignment in admin |

### Directory Structure

```
MyTheme/
├── Resources/
│   ├── views/storefront/...
│   ├── app/storefront/src/scss/base.scss
│   ├── app/storefront/src/main.js
│   └── theme.json
└── manifest.xml
```

### Migration from Plugin Theme

1. Replace `composer.json` and plugin base class with `manifest.xml`
2. Copy `src/Resources` to app's `Resources` directory
3. Template and JavaScript code typically works without changes
