---
title: JavaScript SDK Setup
impact: HIGH
impactDescription: The JS SDK provides the foundation for building Node.js/Deno/Bun app servers
tags: sdk, javascript, node, setup, app-server, installation
---

## JavaScript SDK Setup

The `@shopware-ag/app-server-sdk` package provides everything needed to build a Shopware app server in JavaScript/TypeScript.

### Installation

```bash
npm install --save @shopware-ag/app-server-sdk
```

### Basic Setup

```typescript
import { AppServer, InMemoryShopRepository } from '@shopware-ag/app-server-sdk';

const app = new AppServer({
    appName: 'MyApp',
    appSecret: 'my-secret',
    authorizeCallbackUrl: 'https://my-app.com/app/register/confirm',
}, new InMemoryShopRepository());
```

### Shop Repository Options

| Package | Storage |
|---------|---------|
| `InMemoryShopRepository` | Built-in, for development |
| `@shopware-ag/app-server-sdk-dynamodb` | AWS DynamoDB |
| `@shopware-ag/app-server-sdk-cloudflare` | Cloudflare KV |
| `@shopware-ag/app-server-sdk-deno-kv` | Deno KV |
| `@shopware-ag/app-server-sdk-bun-sqlite` | Bun SQLite |
| `@shopware-ag/app-server-sdk-better-sqlite3` | Better SQLite3 |

### Registration Flow

```typescript
// 1. Handle initial registration (GET /app/register)
const response = await app.registration.authorize(request);

// 2. Handle confirmation callback (POST /app/register/confirm)
await app.registration.authorizeCallback(request);
```

### Context Resolution

```typescript
// From admin iframe (browser context)
const ctx = await app.contextResolver.fromBrowser(request);

// From webhook/action button (API context)
const ctx = await app.contextResolver.fromAPI(request);
```

The context object provides:
- `ctx.shop` — Shop details (ID, URL, secret)
- `ctx.httpClient` — Pre-authenticated HTTP client
- `ctx.payload` — Request payload (typed with generics)
