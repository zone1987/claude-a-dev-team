---
title: JS SDK Hono Integration
impact: HIGH
impactDescription: Hono integration provides the fastest way to build a Shopware app server
tags: sdk, javascript, hono, framework, app-server
---

## JS SDK Hono Integration

The JS SDK provides a `configureAppServer()` helper that auto-registers all lifecycle and registration endpoints on a Hono app.

### Setup

```typescript
import { Hono } from 'hono';
import { AppServer, InMemoryShopRepository } from '@shopware-ag/app-server-sdk';
import { configureAppServer } from '@shopware-ag/app-server-sdk/integration/hono';

const app = new AppServer({
    appName: 'MyApp',
    appSecret: 'my-secret',
    authorizeCallbackUrl: 'https://my-app.com/app/register/confirm',
}, new InMemoryShopRepository());

const server = new Hono();
configureAppServer(server, app);

// Auto-registered routes:
// POST /app/register
// POST /app/register/confirm
// POST /app/activate
// POST /app/deactivate
// POST /app/delete

export default server;
```

### Adding Custom Endpoints

```typescript
// Webhook handler
server.post('/webhook/product-changed', async (c) => {
    const ctx = await app.contextResolver.fromAPI(c.req.raw);
    // ctx.payload contains the webhook data
    // ctx.httpClient is pre-authenticated
    return c.json({ success: true });
});

// Admin module (iframe)
server.get('/admin/module', async (c) => {
    const ctx = await app.contextResolver.fromBrowser(c.req.raw);
    return c.html('<html>...</html>');
});

// Action button handler
server.post('/action/restock', async (c) => {
    const ctx = await app.contextResolver.fromAPI(c.req.raw);
    const { ids } = ctx.payload.data;
    // Process action...
    return c.json({
        actionType: 'notification',
        payload: { status: 'success', message: 'Restocked!' }
    });
});
```
