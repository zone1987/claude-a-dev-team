---
name: sw-admin-snippets
description: >
  Admin-Übersetzungen (Snippets) in Shopware 6: snippet/<locale>.json + Shopware.Snippet, $tc/$t im Template,
  Platzhalter/Pluralisierung, Registrierung im Modul. Trigger: "Admin Snippet", "$tc admin", "snippet json admin",
  "Übersetzung Administration", "Shopware.Snippet", "de-DE admin snippet". Shopware 6.7.
---

# Shopware 6 — Admin-Snippets

Admin-Übersetzungen als JSON unter `module/<name>/snippet/<locale>.json`, im Modul registriert.

```js
// module/ff-example/snippet/de-DE.json + index.js
import deDE from './snippet/de-DE.json';
Shopware.Module.register('ff-example', { snippets: { 'de-DE': deDE, 'en-GB': enGB }, /* ... */ });
```
```json
{ "ff-example": { "general": { "title": "FF Beispiel" }, "detail": { "items": "{count} Einträge" } } }
```
```twig
{{ $tc('ff-example.general.title') }}
{{ $tc('ff-example.detail.items', count, { count }) }}
```

`$tc` (mit Pluralisierung/Parametern) bzw. `$t`. Keys mit Modul-Präfix gegen Kollisionen. Storefront-Snippets
sind getrennt (`shopware-storefront` → `sw-storefront-translations`). Umlaute als UTF-8.
