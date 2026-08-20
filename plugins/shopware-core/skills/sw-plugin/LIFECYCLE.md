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

→ Alle Hooks, Reihenfolge & Beispiele: [LIFECYCLE-DETAIL.md](LIFECYCLE-DETAIL.md)
