---
title: In-App Purchases
impact: LOW
impactDescription: Monetize app features by locking them behind paywalls
tags: in-app-purchases, iap, monetization, meteor-sdk
---

## In-App Purchases

Since Shopware 6.6.9.0, developers can monetize apps by locking features behind a paywall.

### Triggering Purchase (Meteor Admin SDK)

```vue
<template>
    <mt-button @click="buyFeature">Buy Premium Feature</mt-button>
</template>

<script setup>
import * as sw from '@shopware/meteor-admin-sdk';

function buyFeature() {
    sw.iap.purchase({ identifier: 'my-premium-feature' });
}
</script>
```

### Verifying Purchases

Purchased IAPs are delivered as a JWT token:
- Query parameter: `in-app-purchases`
- Request body field: `inAppPurchases`

### Node.js Verification

```javascript
import { jwtVerify, createRemoteJWKSet } from 'jose';

const JWKS = createRemoteJWKSet(
    new URL('https://api.shopware.com/inappfeatures/jwks')
);

const { payload } = await jwtVerify(token, JWKS);
// payload contains purchased IAP identifiers
```

### PHP/Symfony Verification

```php
#[Route('/app/admin', name: 'admin')]
public function admin(ModuleAction $action): Response
{
    $purchases = $action->inAppPurchases->all();
    return $this->render('admin.html.twig', [
        'inAppPurchases' => $purchases,
    ]);
}
```

### Best Practices

- Implement purchase buttons and visibility logic yourself
- Always validate JWT signatures
- Hide purchase buttons for already-purchased, non-repeatable IAPs
- Use JWT claims to gate feature availability
