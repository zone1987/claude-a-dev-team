/**
 * Shopware App Server using Hono + JS SDK
 * Install: npm install hono @shopware-ag/app-server-sdk
 */
import { Hono } from 'hono';
import { AppServer, InMemoryShopRepository } from '@shopware-ag/app-server-sdk';
import type { Context } from 'hono';

// Initialize App Server
const app = new Hono();
const shopRepository = new InMemoryShopRepository();
const appServer = new AppServer(
  {
    appName: 'MyApp',
    appSecret: 'my-secret',
    authorizeCallbackUrl: 'https://my-app.example.com/app/register/confirm',
  },
  shopRepository
);

// --- Registration Endpoints ---

app.get('/app/register', async (c: Context) => {
  const resp = await appServer.registration.authorize(c.req.raw);
  return new Response(resp.body, {
    status: resp.statusCode,
    headers: resp.headers,
  });
});

app.post('/app/register/confirm', async (c: Context) => {
  const resp = await appServer.registration.authorizeCallback(c.req.raw);
  return new Response(resp.body, {
    status: resp.statusCode,
    headers: resp.headers,
  });
});

// --- Webhook Endpoint ---

app.post('/webhook/product-changed', async (c: Context) => {
  const context = await appServer.contextResolver.fromSource(c.req.raw);

  const shopId = context.shop.getShopId();
  const event = context.payload.source?.event;
  const entityIds = context.payload.data?.ids ?? [];

  console.log(`[${shopId}] Event: ${event}, IDs: ${entityIds.join(', ')}`);

  // Use HTTP client to call Shopware API
  const httpClient = await appServer.httpClient(context.shop);
  const response = await httpClient.post('/api/search/product', {
    body: JSON.stringify({
      ids: entityIds,
      limit: entityIds.length,
    }),
  });

  console.log(`Fetched ${response.body.total} products`);

  return c.json({ success: true });
});

// --- Action Button Endpoint ---

app.post('/action/sync-product', async (c: Context) => {
  const context = await appServer.contextResolver.fromSource(c.req.raw);
  const ids = context.payload.data?.ids ?? [];

  // Process action button click
  console.log(`Syncing products: ${ids.join(', ')}`);

  // Return notification response
  return c.json({
    actionType: 'notification',
    payload: {
      status: 'success',
      message: `Successfully synced ${ids.length} product(s).`,
    },
  });
});

// --- Payment Endpoints ---

app.post('/payment/pay', async (c: Context) => {
  const context = await appServer.contextResolver.fromSource(c.req.raw);
  const order = context.payload.order;
  const orderTransaction = context.payload.orderTransaction;

  console.log(`Processing payment for order ${order.orderNumber}`);

  // Sync payment: return status immediately
  const response = new Response(
    JSON.stringify({ status: 'paid' }),
    { headers: { 'Content-Type': 'application/json' } }
  );

  return appServer.signer.signResponse(response, context.shop);
});

app.post('/payment/refund', async (c: Context) => {
  const context = await appServer.contextResolver.fromSource(c.req.raw);

  const response = new Response(
    JSON.stringify({ status: 'refunded' }),
    { headers: { 'Content-Type': 'application/json' } }
  );

  return appServer.signer.signResponse(response, context.shop);
});

// --- Flow Action Endpoint ---

app.post('/flow/slack-notify', async (c: Context) => {
  const context = await appServer.contextResolver.fromSource(c.req.raw);

  const config = context.payload.config;
  const params = context.payload.data;

  console.log(`Slack notify: #${config.channel} - Order ${params.order_number}`);

  return c.json({ success: true });
});

// --- Admin Module (iFrame) ---

app.get('/admin/dashboard', async (c: Context) => {
  const context = await appServer.contextResolver.fromSource(c.req.raw);
  const shopUrl = context.shop.getShopUrl();

  return c.html(`
    <!DOCTYPE html>
    <html>
    <head>
      <title>App Dashboard</title>
      <script>window.parent.postMessage('sw-app-loaded', '*');</script>
    </head>
    <body>
      <h1>My App Dashboard</h1>
      <p>Connected to: ${shopUrl}</p>
    </body>
    </html>
  `);
});

export default app;
