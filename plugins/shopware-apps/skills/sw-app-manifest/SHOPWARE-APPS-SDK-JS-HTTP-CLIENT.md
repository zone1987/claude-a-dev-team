---
title: JS SDK HTTP Client
impact: HIGH
impactDescription: The HTTP client handles OAuth2 authentication automatically for API calls
tags: sdk, javascript, http-client, api, oauth2
---

## JS SDK HTTP Client

The HTTP client automatically handles OAuth2 token management for Shopware API communication.

### Usage via Context

```typescript
const ctx = await app.contextResolver.fromAPI(request);

// Direct fetch-like API
const response = await ctx.httpClient.get('/api/product');
const response = await ctx.httpClient.post('/api/product', { body: data });
const response = await ctx.httpClient.patch('/api/product/id', { body: data });
const response = await ctx.httpClient.delete('/api/product/id');
```

### EntityRepository

```typescript
import { EntityRepository, Criteria } from '@shopware-ag/app-server-sdk';

const repo = new EntityRepository(ctx.httpClient, 'product');

// Search
const criteria = new Criteria();
criteria.addFilter({ type: 'equals', field: 'active', value: true });
const result = await repo.search(criteria);

// Upsert (create or update)
await repo.upsert([{ id: 'uuid', name: 'Product Name' }]);

// Delete
await repo.delete([{ id: 'uuid' }]);
```

### SyncService for Batch Operations

```typescript
import { SyncService } from '@shopware-ag/app-server-sdk';

const sync = new SyncService(ctx.httpClient);
await sync.sync([
    { entity: 'product', action: 'upsert', payload: [{ id: 'uuid', name: 'New' }] },
    { entity: 'category', action: 'delete', payload: [{ id: 'uuid' }] },
]);
```
