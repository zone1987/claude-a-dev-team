---
title: In-App Purchase Gateway
impact: LOW
impactDescription: IAP gateways restrict specific in-app purchases via server-side logic
tags: gateway, in-app-purchases, iap, restriction
---

## In-App Purchase Gateway

Since Shopware 6.6.9.0, IAP gateways allow apps to restrict specific in-app purchases through server-side logic.

### Manifest Configuration

```xml
<gateways>
    <inAppPurchases>https://my-app.com/iap/gateway</inAppPurchases>
</gateways>
```

### Behavior

During IAP checkout, Shopware calls the gateway with the IAP the user intends to purchase. The app can approve or restrict the purchase.

### Current Scope

Currently restricts checkout for new IAP only. Future: filtering entire IAP lists before display.

### Important Notes

- **5-second timeout**
- No additional configuration needed beyond manifest
- Plugin event: `InAppPurchasesGatewayEvent`
