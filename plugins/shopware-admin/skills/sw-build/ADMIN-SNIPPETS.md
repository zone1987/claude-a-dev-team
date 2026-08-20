# Shopware 6 — Admin snippets

Admin translations as JSON under `module/<name>/snippet/<locale>.json`, registered in the module.

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

`$tc` (with pluralisation/parameters) or `$t`. Prefix keys with the module name to avoid collisions. Storefront
snippets are separate (`shopware-storefront` → `sw-storefront-translations`). Umlauts as UTF-8.
