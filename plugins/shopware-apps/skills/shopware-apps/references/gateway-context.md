---
title: Context Gateway
impact: LOW
impactDescription: Context gateways allow apps to interact with and manipulate customer context
tags: gateway, context, customer, login
---

## Context Gateway

Since Shopware 6.7.1.0, context gateways enable apps to manipulate the customer context during shopping.

### Manifest Configuration

```xml
<gateways>
    <context>https://my-app.com/context/gateway</context>
</gateways>
```

### Storefront JavaScript Integration

```javascript
import ContextGatewayClient from 'src/service/context-gateway-client.service';

const client = new ContextGatewayClient('myAppName');
const response = await client.call({ some: 'data' });
await client.navigate(response, '/custom/target');
```

### Available Commands

- Change active currency/language
- Register new customers
- Log in existing customers (without password)
- Modify customer context

### Security Warning

This gateway allows **password-less customer login**. Ensure your app server is properly secured.

### Important Notes

- **5-second timeout**
- Maximum one command per type, one login/register per response
- Plugin event: `ContextGatewayCommandsCollectedEvent`
