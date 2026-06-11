---
name: sw-plugin-lifecycle
description: >
  Shopware-6-Plugin-Lifecycle implementieren: install/postInstall, update/postUpdate, activate, deactivate,
  uninstall (mit keepUserData), und der InstallContext/UninstallContext.
  Trigger: "Plugin lifecycle", "install/uninstall Methode", "activate deactivate", "keepUserData",
  "Daten beim Deinstallieren behalten", "plugin update method", "Migration bei Plugin-Update". Shopware 6.7.
---

# Shopware 6 — Plugin-Lifecycle

Die Plugin-Klasse kann Lifecycle-Hooks überschreiben. Jeder bekommt einen Context mit `getContext()`,
`getPlugin()` und (bei uninstall) `keepUserData()`.

```php
public function uninstall(UninstallContext $uninstallContext): void
{
    parent::uninstall($uninstallContext);
    if ($uninstallContext->keepUserData()) {
        return; // Tabellen/Daten NICHT löschen
    }
    // Aufräumen: eigene Tabellen droppen etc.
}
```

Faustregeln: Schema-Änderungen über **Migrations** (`sw-migration` / `shopware-data`), nicht im Lifecycle.
Bei `uninstall` immer `keepUserData()` respektieren. `activate`/`deactivate` für Daten, die nur bei aktivem Plugin gelten.

→ Alle Hooks, Reihenfolge & Beispiele: [references/lifecycle.md](references/lifecycle.md)
