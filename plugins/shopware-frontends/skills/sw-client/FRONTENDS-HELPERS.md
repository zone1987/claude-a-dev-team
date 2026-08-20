# Shopware Frontends — @shopware/helpers

Pure utility functions (no state) for recurring tasks in headless frontends:

- **Translations**: `getTranslatedProperty(entity, 'name')` — returns the translated value (translated array).
- **Prices/currency**: format helpers for gross/net/list price, currency symbol.
- **URLs/SEO**: `getProductRoute`/`getCategoryRoute`, `buildUrlPrefix` (language prefix) for SEO paths.
- **Media/thumbnails**: pick the matching thumbnail/`srcset` from a media entity.
- **Cart**: helper functions for line item calculations/display.

```ts
import { getTranslatedProperty, getProductRoute } from '@shopware/helpers';
const name = getTranslatedProperty(product, 'name');
const to = getProductRoute(product);
```

Complements the composables (`sw-composables`); for API calls use `sw-api-client-js`. Functions are tree-shakeable
and can be imported individually.

→ Complete reference: [FRONTENDS-HELPERS-HELPERS-REFERENCE.md](FRONTENDS-HELPERS-HELPERS-REFERENCE.md)
