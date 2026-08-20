# Shopware 6 — Admin navigation/menu

Menu entries are defined in the module via `navigation` (main menu) or `settingsItem` (settings).

```js
navigation: [{
    id: 'ff-example',
    label: 'ff-example.general.title',
    path: 'ff.example.index',
    parent: 'sw-catalogue',   // attach under an existing area
    position: 50,
    icon: 'regular-cog',
}],
settingsItem: [{ name: 'ff-example', to: 'ff.example.index', label: 'ff-example.general.title', group: 'plugins', icon: 'regular-cog' }],
```

`parent` references existing navigation IDs (`sw-catalogue`, `sw-order`, `sw-marketing`, …). Tie visibility
to an ACL privilege (`privilege: 'ff_example.viewer'`, `sw-admin-acl-permissions`). Labels via snippets (`sw-admin-snippets`).
