# Shopware monetization & in-app purchases (complete reference)

Sources: `guides/development/monetization/index.md`, `monetization/in-app-purchases.md`

## Contents

- [Monetization models at a glance](#monetization-models-at-a-glance)
- [In-App Purchases — technical details](#in-app-purchases--technical-details)
- [Best practices for IAP implementation](#best-practices-for-iap-implementation)
- [Further links](#further-links)

## Monetization models at a glance

### Paid Extensions

Sell extensions with a one-off purchase or subscription model through the Shopware Store.
Pricing and licensing are managed in the Shopware Account.

### In-App Purchases (IAP)

Lock specific features behind a paywall within the same extension.
**Available from Shopware 6.6.9.0.**

Useful for:
- Free base version + paid premium features
- Feature add-ons for the main extension

### Commission-based Integrations

When an extension integrates external services and generates revenue (e.g. transaction-based fees):
→ a Shopware Technology Partner (STP) agreement may be required.

**All monetized extensions must meet the Quality Guidelines.**

---

## In-App Purchases — technical details

### Triggering an IAP purchase

Via `sw.iap.purchase()` from the Meteor Admin SDK:

```vue
<template>
  <!-- Only show the button when not yet purchased -->
  <p>With this purchase you get the premium feature: ...</p>
  <mt-button @click="onClick">
    Buy
  </mt-button>
</template>

<script setup>
import * as sw from '@shopware/meteor-admin-sdk';

function onClick() {
  sw.iap.purchase({ identifier: 'my-iap-identifier' });
}
</script>
```

**Developer responsibilities:**
- Provide the button
- Hide the button when the IAP cannot be purchased more than once
- The checkout process is provided by Shopware itself

**Alternative**: manually via `window.postMessage` with a formatted IAP identifier to the Administration.

### IAP token format

With every request Shopware sends a JWT as proof of active in-app purchases:
- **GET requests**: query parameter `in-app-purchases`
- **POST requests**: request body under `source.inAppPurchases`

The JWT payload contains the list of all purchased IAP identifiers.

### Token validation — PHP (Symfony with shopware/app-bundle)

```php
#[Route(path: '/app/admin', name: 'admin')]
public function admin(ModuleAction $action): Response {
    return $this->render('admin.html.twig', [
        'inAppPurchases' => $action->inAppPurchases->all(),
    ]);
}
```

Twig template — inject the IAP data into JavaScript:

```html
<!DOCTYPE html>
<html>
    <head>
        <script>
            try {
                window.inAppPurchases = JSON.parse('{{ inAppPurchases | json_encode | raw }}');
            } catch (e) {
                window.inAppPurchases = {};
                console.error('Unable to decode In-App Purchases', e);
            }
        </script>
    </head>
</html>
```

For plain PHP: use `shopware/app-php-sdk`.
Example: https://github.com/shopware/app-php-sdk/blob/main/examples/index.php

### Token validation — non-PHP app servers

Use the JWT/JOSE library of the respective language. Tokens are signed JWTs — validate the signature via Shopware's public keys.

**JWKS endpoint**: `https://api.shopware.com/inappfeatures/jwks`

Node.js example with `jose`:

```js
import { jwtVerify, createRemoteJWKSet } from 'jose';

const JWKS = createRemoteJWKSet(new URL('https://api.shopware.com/inappfeatures/jwks'));

const { payload } = await jwtVerify(token, JWKS);
console.log(payload);
// Contains the list of purchased IAP identifiers
// e.g.: { features: ['my-iap-identifier', 'another-feature'] }
```

### Initial admin request

IAPs are also transmitted with the initial `sw-main-hidden` admin request.
For JavaScript access → inject them into the application (see the template example above).

### IAP gateway event

Apps can manipulate the available IAPs via:
In-App Purchase Gateway

---

## Best practices for IAP implementation

1. **Hide non-purchasable IAPs**: only show the button when the IAP is available and not yet purchased
2. **Server-side check**: always validate the JWT server-side — never rely on client-side checks alone
3. **Graceful degradation**: keep base features available without an IAP
4. **Clear UX**: users must understand which feature they are buying and what they get for it
5. **JWKS caching**: cache the public keys, do not reload them on every request

## Further links

- Concept documentation: `concepts/framework/in-app-purchases`
- Extension partner documentation: https://docs.shopware.com/en/account-en/extension-partner/in-app-purchases
- Meteor Admin SDK: https://github.com/shopware/meteor/tree/main/packages/admin-sdk
- Quality Guidelines: `guides/development/testing/store/quality-guidelines.md`
