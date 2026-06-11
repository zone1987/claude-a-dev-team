---
name: sw-monetization-iap
description: >
  Shopware In-App Purchases (IAP) — Features hinter Paywall in Extensions.
  `sw.iap.purchase()` via Meteor Admin SDK, JWT-Token-Validierung (PHP SDK / jose),
  JWKS-Endpunkt `https://api.shopware.com/inappfeatures/jwks`, IAP-Gateway-Events.
  Monetarisierungsmodelle: Einmalkauf, Subscription, Commission. Trigger:
  "in-app purchase shopware", "iap shopware", "feature paywall extension",
  "sw.iap.purchase", "in-app-purchases jwt", "iap token validieren", "JWKS shopware",
  "meteor admin sdk iap", "shopware monetization", "paid extension", "extension verkaufen",
  "subscription shopware plugin". Ab Shopware 6.6.9.0.
---

# Shopware In-App Purchases (IAP)

Ab **Shopware 6.6.9.0**. Ermöglicht, bestimmte Features hinter einer Paywall zu sperren — innerhalb derselben Extension.

## IAP-Kauf auslösen (Meteor Admin SDK)

```vue
<template>
  <mt-button @click="onClick">Feature kaufen</mt-button>
</template>

<script setup>
import * as sw from '@shopware/meteor-admin-sdk';

function onClick() {
  sw.iap.purchase({ identifier: 'my-feature-identifier' });
}
</script>
```

Checkout-Prozess wird von Shopware bereitgestellt. Button anzeigen/verbergen liegt beim Entwickler.

## Aktive IAPs prüfen

IAP-JWT kommt in jedem Request als:
- GET: Query-Parameter `in-app-purchases`
- POST: Request-Body `source.inAppPurchases`

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
// payload enthält Liste gekaufter IAP-Identifier
```

## Monetarisierungsmodelle

| Modell | Beschreibung |
|---|---|
| **Paid Extension** | Einmalkauf oder Subscription im Shopware Store (via Shopware Account) |
| **In-App Purchases** | Features einzeln kaufbar innerhalb der Extension |
| **Commission-based** | Externe Service-Integration mit Transaktions-Gebühren → STP-Vertrag nötig |

Alle monetarisierten Extensions müssen Shopware Quality Guidelines erfüllen.
Details und IAP-Gateway-Events: `references/deep/monetization-iap.md`.
