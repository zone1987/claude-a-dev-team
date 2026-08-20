# Shopware 6 — Admin-Navigation/Menü

Menüeinträge werden im Modul über `navigation` (Hauptmenü) bzw. `settingsItem` (Einstellungen) definiert.

```js
navigation: [{
    id: 'ff-example',
    label: 'ff-example.general.title',
    path: 'ff.example.index',
    parent: 'sw-catalogue',   // unter bestehenden Bereich hängen
    position: 50,
    icon: 'regular-cog',
}],
settingsItem: [{ name: 'ff-example', to: 'ff.example.index', label: 'ff-example.general.title', group: 'plugins', icon: 'regular-cog' }],
```

`parent` referenziert bestehende Navigation-IDs (`sw-catalogue`, `sw-order`, `sw-marketing`, …). Sichtbarkeit
an ACL-Privilege koppeln (`privilege: 'ff_example.viewer'`, `sw-admin-acl-permissions`). Labels über Snippets (`sw-admin-snippets`).
