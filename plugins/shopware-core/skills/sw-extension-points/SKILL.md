---
name: sw-extension-points
description: >
  Das Shopware-6 Extension-System (ADR "extended event system"): Extension Points nutzen und eigene erstellen,
  Unterschied Extension Points vs. klassische Events. Trigger: "extension point", "Extension-System",
  "extends extension", "eigene Erweiterungsstelle", "extension vs event", "Shopware\\Core\\Framework\\Extensions".
  Shopware 6.7.
---

# Shopware 6 — Extension Points

Ergänzend zu Events bietet Shopware **Extension Points**: definierte Stellen, an denen der Kern eine `Extension`
dispatcht, deren `result` ein Plugin ersetzen/anreichern kann (mehr als ein reines „nachträglich reagieren").

```php
// Auf einen Extension-Point reagieren (pre/post)
public static function getSubscribedEvents(): array
{
    return [ MyCoreExtension::class . '.pre' => 'beforeCompute' ];
}
```

- **Event** = benachrichtigt, Listener kann Seiteneffekte/Manipulation am mitgereichten Objekt machen.
- **Extension Point** = umschließt eine Kernoperation; das Plugin kann das Ergebnis liefern/ändern (ideal für „Verhalten ersetzen").

Eigene Extension Points für Plugins: `Extension` ableiten und im Service via `ExtensionDispatcher` umschließen.
Wenn ein klassisches Event reicht, dieses bevorzugen (`sw-events-subscriber`).
