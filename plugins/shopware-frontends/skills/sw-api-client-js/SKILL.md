---
name: sw-api-client-js
description: >
  Der @shopware/api-client für headless Shopware-Frontends: createAPIClient, invoke(operation), Store-API-Aufrufe,
  Context-Token-Handling, Request-Hooks, Admin-Client-Variante. Trigger: "@shopware/api-client", "createAPIClient",
  "invoke api-client", "store-api client js", "apiClient.invoke", "frontends api client". Shopware Frontends.
---

# Shopware Frontends — @shopware/api-client

Typisierter Client gegen die **Store API**. `createAPIClient` erzeugt die Instanz, `invoke` ruft eine typisierte
Operation auf.

```ts
import { createAPIClient } from '@shopware/api-client';
import type { operations } from '#shopware'; // generierte Typen (sw-api-gen-types)

const apiClient = createAPIClient<operations>({
  baseURL: 'https://shop.example.com/store-api',
  accessToken: import.meta.env.SHOPWARE_ACCESS_TOKEN, // sw-access-key
});

const { data } = await apiClient.invoke('readProduct post /product', { body: { limit: 10 } });
```

Der Client verwaltet den `sw-context-token` automatisch (Warenkorb/Login-State, `sw-frontends-session-context`).
Request-/Response-Hooks (`apiClient.hook`) für Token-Persistenz/Fehler. Typen kommen aus `@shopware/api-gen`.
Für reine API-Fakten (Endpunkte/Header) → Plugin `shopware-api`.

→ Vollständige Referenz: [references/deep/api-client-reference.md](references/deep/api-client-reference.md)
