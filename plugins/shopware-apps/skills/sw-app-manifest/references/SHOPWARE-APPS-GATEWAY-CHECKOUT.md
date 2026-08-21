---
title: Checkout Gateway
impact: LOW
impactDescription: Checkout gateways enable decision-making during checkout based on cart/context
tags: gateway, checkout, cart, commands
---

## Checkout Gateway

Since Shopware 6.6.3.0, checkout gateways allow apps to make decisions during checkout based on cart contents and sales channel context.

### Manifest Configuration

```xml
<gateways>
    <checkout>https://my-app.com/checkout/gateway</checkout>
</gateways>
```

### Request Payload

Shopware sends: current `SalesChannelContext`, `Cart` data, available payment and shipping methods.

### Response

Respond with a list of commands to:
- Manipulate the cart
- Modify available payment methods
- Adjust shipping methods
- Add cart errors

### Important Notes

- **5-second timeout** — respond within this timeframe
- Activates automatically after app installation
- Plugin event: `CheckoutGatewayCommandsCollectedEvent`
