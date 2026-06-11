---
name: sw-admin-utils-filters
description: >
  Eingebaute Helfer im Shopware-6-Admin: Shopware.Utils (createId/get/object/array/string/debounce/format),
  Shopware.Filter (date, currency, fileSize, truncate, ...), Shopware.Classes, Shopware.Defaults. Trigger:
  "Shopware.Utils", "Admin Filter", "currency filter", "date filter admin", "createId admin", "fileSize filter",
  "utils helper admin", "$options filter". Shopware 6.7.
---

# Shopware 6 — Admin-Utils & -Filter

Die Admin bietet viele Helfer am `Shopware`-Objekt — vor eigenem Code prüfen, ob es schon existiert.

## Utils — `Shopware.Utils`
`createId()` (UUID), `get(obj, 'a.b', default)`, `object.*` (deepCopy, merge, cloneDeep), `array.*`,
`string.*` (camelCase, snakeCase, capitalizeString), `format.*`, `debounce`, `throttle`, `types.*` (isObject…).

```js
const id = Shopware.Utils.createId();
const name = Shopware.Utils.get(product, 'manufacturer.name', '—');
```

## Filter — `Shopware.Filter.getByName(...)` / im Template
`date`, `currency`, `fileSize`, `truncate`, `striphtml`, `asset`, `mediaName`, `unicodeUri`.

```twig
{{ order.orderDateTime | date({ hour: '2-digit', minute: '2-digit' }) }}
{{ price | currency(currencyIso) }}
{{ media.fileSize | fileSize }}
```

## Weitere
`Shopware.Classes.ApiService`/`ShopwareError`, `Shopware.Defaults` (LIVE_VERSION, systemLanguageId…),
`Shopware.Context.api`, `Shopware.Feature.isActive()`. Welche im Projekt real verfügbar/registriert sind:
Katalog via `sw-admin-catalog` / `/sw-admin-map`.
