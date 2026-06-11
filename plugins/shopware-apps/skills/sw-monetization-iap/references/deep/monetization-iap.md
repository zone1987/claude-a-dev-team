# Shopware Monetarisierung & In-App Purchases (vollständige Referenz)

Quellen: `guides/development/monetization/index.md`, `monetization/in-app-purchases.md`

## Monetarisierungsmodelle im Überblick

### Paid Extensions

Erweiterungen mit Einmalkauf oder Subscription-Modell über den Shopware Store verkaufen.
Pricing und Lizenzierung werden im Shopware Account verwaltet.

### In-App Purchases (IAP)

Bestimmte Features innerhalb derselben Extension hinter einer Paywall sperren.
**Verfügbar ab Shopware 6.6.9.0.**

Nützlich für:
- Kostenlose Basisversion + bezahlte Premium-Features
- Feature-Add-ons zur Haupt-Extension

### Commission-based Integrations

Wenn eine Extension externe Services integriert und Umsatz generiert (z.B. transaktionsbasierte Gebühren):
→ Shopware Technology Partner (STP)-Vereinbarung kann erforderlich sein.

**Alle monetarisierten Extensions müssen die [Quality Guidelines](../../testing/store/quality-guidelines.md) erfüllen.**

---

## In-App Purchases — Technische Details

### IAP-Kauf auslösen

Via `sw.iap.purchase()` aus dem Meteor Admin SDK:

```vue
<template>
  <!-- Button nur anzeigen, wenn noch nicht gekauft -->
  <p>Mit diesem Kauf erhaltest du das Premium-Feature: ...</p>
  <mt-button @click="onClick">
    Kaufen
  </mt-button>
</template>

<script setup>
import * as sw from '@shopware/meteor-admin-sdk';

function onClick() {
  sw.iap.purchase({ identifier: 'my-iap-identifier' });
}
</script>
```

**Verantwortlichkeiten des Entwicklers:**
- Button bereitstellen
- Button ausblenden, wenn IAP nicht mehrfach kaufbar ist
- Der Checkout-Prozess wird von Shopware selbst bereitgestellt

**Alternative**: Manuell via `window.postMessage` mit formatiertem IAP-Identifier an die Administration.

### IAP-Token-Format

Shopware sendet bei jedem Request einen JWT als Nachweis aktiver In-App Purchases:
- **GET-Requests**: Query-Parameter `in-app-purchases`
- **POST-Requests**: Request-Body unter `source.inAppPurchases`

Der JWT enthält im Payload die Liste aller gekauften IAP-Identifier.

### Token-Validierung — PHP (Symfony mit shopware/app-bundle)

```php
#[Route(path: '/app/admin', name: 'admin')]
public function admin(ModuleAction $action): Response {
    return $this->render('admin.html.twig', [
        'inAppPurchases' => $action->inAppPurchases->all(),
    ]);
}
```

Twig-Template — IAP-Daten in JavaScript injizieren:

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

Für Plain PHP: `shopware/app-php-sdk` verwenden.
Beispiel: https://github.com/shopware/app-php-sdk/blob/main/examples/index.php

### Token-Validierung — Non-PHP App-Server

JWT/JOSE-Bibliothek der jeweiligen Sprache verwenden. Tokens sind signierte JWTs — Signatur via Shopware's Public Keys validieren.

**JWKS-Endpunkt**: `https://api.shopware.com/inappfeatures/jwks`

Node.js Beispiel mit `jose`:

```js
import { jwtVerify, createRemoteJWKSet } from 'jose';

const JWKS = createRemoteJWKSet(new URL('https://api.shopware.com/inappfeatures/jwks'));

const { payload } = await jwtVerify(token, JWKS);
console.log(payload);
// Enthält Liste gekaufter IAP-Identifier
// z.B.: { features: ['my-iap-identifier', 'another-feature'] }
```

### Admin-Initialanfrage

IAP werden auch mit der initialen `sw-main-hidden` Admin-Anfrage übertragen.
Für JavaScript-Zugriff → in die Anwendung injizieren (siehe Template-Beispiel oben).

### IAP-Gateway-Event

Apps können verfügbare IAPs manipulieren via:
[In-App Purchase Gateway](../../plugins/apps/gateways/in-app-purchase/in-app-purchase-gateway)

---

## Best Practices für IAP-Implementierung

1. **Nicht kaufbare IAPs verbergen**: Button nur anzeigen, wenn IAP verfügbar und noch nicht gekauft
2. **Server-seitige Prüfung**: Immer serverseitig den JWT validieren — nie nur client-seitige Checks
3. **Graceful Degradation**: Basis-Features ohne IAP verfügbar lassen
4. **Klare UX**: Nutzer müssen verstehen, welches Feature sie kaufen und was sie dafür erhalten
5. **JWKS-Caching**: Public Keys cachen, nicht bei jedem Request neu laden

## Weiterführende Links

- Konzept-Dokumentation: `concepts/framework/in-app-purchases`
- Extension Partner Dokumentation: https://docs.shopware.com/en/account-en/extension-partner/in-app-purchases
- Meteor Admin SDK: https://github.com/shopware/meteor/tree/main/packages/admin-sdk
- Quality Guidelines: `guides/development/testing/store/quality-guidelines.md`
