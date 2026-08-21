# Shopware Frontends — @shopware/api-client

Typed client against the **Store API**. `createAPIClient` creates the instance, `invoke` calls a typed
operation.

```ts
import { createAPIClient } from '@shopware/api-client';
import type { operations } from '#shopware'; // generated types (sw-api-gen-types)

const apiClient = createAPIClient<operations>({
  baseURL: 'https://shop.example.com/store-api',
  accessToken: import.meta.env.SHOPWARE_ACCESS_TOKEN, // sw-access-key
});

const { data } = await apiClient.invoke('readProduct post /product', { body: { limit: 10 } });
```

The client manages the `sw-context-token` automatically (cart/login state, `sw-frontends-session-context`).
Request/response hooks (`apiClient.hook`) for token persistence/errors. Types come from `@shopware/api-gen`.
For pure API facts (endpoints/headers) → plugin `shopware-api`.

→ Complete reference: [API-CLIENT-JS-API-CLIENT-REFERENCE.md](API-CLIENT-JS-API-CLIENT-REFERENCE.md)
