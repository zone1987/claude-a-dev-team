# Shopware In-App Purchases (IAP)

From **Shopware 6.6.9.0** onwards. Allows locking specific features behind a paywall — within the same extension.

## Triggering an IAP purchase (Meteor Admin SDK)

```vue
<template>
  <mt-button @click="onClick">Buy feature</mt-button>
</template>

<script setup>
import * as sw from '@shopware/meteor-admin-sdk';

function onClick() {
  sw.iap.purchase({ identifier: 'my-feature-identifier' });
}
</script>
```

The checkout process is provided by Shopware. Showing/hiding the button is up to the developer.

## Checking active IAPs

The IAP JWT arrives with every request as:
- GET: query parameter `in-app-purchases`
- POST: request body `source.inAppPurchases`

### PHP (Symfony/app-bundle)

```php
#[Route(path: '/app/admin', name: 'admin')]
public function admin(ModuleAction $action): Response {
    return $this->render('admin.html.twig', [
        'inAppPurchases' => $action->inAppPurchases->all(),
    ]);
}
```

Template: `window.inAppPurchases = JSON.parse('{{ inAppPurchases | json_encode | raw }}');`

### Non-PHP (jose / Node.js)

```js
import { jwtVerify, createRemoteJWKSet } from 'jose';

const JWKS = createRemoteJWKSet(new URL('https://api.shopware.com/inappfeatures/jwks'));
const { payload } = await jwtVerify(token, JWKS);
// payload contains the list of purchased IAP identifiers
```

## Monetization models

| Model | Description |
|---|---|
| **Paid Extension** | One-off purchase or subscription in the Shopware Store (via Shopware Account) |
| **In-App Purchases** | Features purchasable individually within the extension |
| **Commission-based** | External service integration with transaction fees → STP agreement required |

All monetized extensions must meet the Shopware Quality Guidelines.
Details and IAP gateway events: `SW-MONETIZATION-IAP-MONETIZATION-IAP.md`.
