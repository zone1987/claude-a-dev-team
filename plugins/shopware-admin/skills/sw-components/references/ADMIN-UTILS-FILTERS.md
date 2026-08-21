# Shopware 6 — Admin utils & filters

The admin offers many helpers on the `Shopware` object — before writing your own code, check whether one already exists.

## Utils — `Shopware.Utils`
`createId()` (UUID), `get(obj, 'a.b', default)`, `object.*` (deepCopy, merge, cloneDeep), `array.*`,
`string.*` (camelCase, snakeCase, capitalizeString), `format.*`, `debounce`, `throttle`, `types.*` (isObject…).

```js
const id = Shopware.Utils.createId();
const name = Shopware.Utils.get(product, 'manufacturer.name', '—');
```

## Filters — `Shopware.Filter.getByName(...)` / in the template
`date`, `currency`, `fileSize`, `truncate`, `striphtml`, `asset`, `mediaName`, `unicodeUri`.

```twig
{{ order.orderDateTime | date({ hour: '2-digit', minute: '2-digit' }) }}
{{ price | currency(currencyIso) }}
{{ media.fileSize | fileSize }}
```

## Further
`Shopware.Classes.ApiService`/`ShopwareError`, `Shopware.Defaults` (LIVE_VERSION, systemLanguageId…),
`Shopware.Context.api`, `Shopware.Feature.isActive()`. Which of these are actually available/registered in the project:
catalog via `sw-admin-catalog` / `/sw-admin-map`.
