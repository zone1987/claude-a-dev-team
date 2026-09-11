# A test run leaves the shop as it found it

**No test may add a row that outlives it.**

A suite that leaves entities behind fills the administration with noise nobody can tell
from real configuration, and it eventually changes what the next run measures. This is not
tidiness — it is the difference between a test environment and a landfill.

## What it looks like when this goes wrong

Twenty-one shipping methods named `Test-ShippingMethod-107193782568048` in the shipping
settings, one per test run, indistinguishable from the two real ones. Nobody notices for a
week, because each run adds only one.

The cause was not a missing clean-up. The clean-up existed, ran, and **failed silently** on
every single run.

## Three levels, and each exists because the one before it failed

### 1. The suite's own TestDataService

Every entity created through `TestDataService` is registered with `addCreatedRecord()` and
deleted when the test ends. **Every entity a test creates must go through it** — a direct
API call bypasses the whole mechanism.

```typescript
// Right: the suite knows about this and will remove it.
const product = await TestDataService.createBasicProduct({ … });

// Wrong: nothing will ever delete this.
await AdminApiContext.post('product', { data: { … } });
```

If you need something the suite cannot build, extend `TestDataService` and call
`this.addCreatedRecord(entity, id)` yourself.

### 2. The plugin's own cleanUp override — the one that is easy to get wrong

**A record that something still points at cannot be deleted, and the suite's delete fails
without saying so.** Anything a test attaches to the sales channel has to be detached
first, in `cleanUp()`, before `super.cleanUp()` runs:

```typescript
export class YourTestDataService extends TestDataService {
    private originalShippingMethodId: string | null = null;
    private originalCurrencyId: string | null = null;
    private readonly assignedShippingMethodIds: string[] = [];

    async useShippingMethodInStorefront(shippingMethodId: string): Promise<void> {
        if (this.originalShippingMethodId === null) {
            this.originalShippingMethodId = this.defaultSalesChannel.shippingMethodId ?? null;
        }

        this.assignedShippingMethodIds.push(shippingMethodId);

        const response = await this.AdminApiClient.patch(
            `sales-channel/${this.defaultSalesChannel.id}`,
            { data: { shippingMethodId, shippingMethods: [{ id: shippingMethodId }] } },
        );
        expect(response.ok()).toBeTruthy();
    }

    override async cleanUp(): Promise<APIResponse | null> {
        if (this.originalShippingMethodId !== null) {
            await this.AdminApiClient.patch(`sales-channel/${this.defaultSalesChannel.id}`, {
                data: { shippingMethodId: this.originalShippingMethodId },
            });
            this.originalShippingMethodId = null;
        }

        if (this.originalCurrencyId !== null) {
            await this.AdminApiClient.patch(`sales-channel/${this.defaultSalesChannel.id}`, {
                data: { currencyId: this.originalCurrencyId },
            });
            this.originalCurrencyId = null;
        }

        // The many-to-many row survives the patch above and keeps a foreign key on the
        // shipping method, so the delete in super.cleanUp() is refused and the method
        // stays behind. This is the line that was missing for 21 runs.
        while (this.assignedShippingMethodIds.length > 0) {
            const shippingMethodId = this.assignedShippingMethodIds.pop();

            await this.AdminApiClient.delete(
                `sales-channel/${this.defaultSalesChannel.id}/shipping-methods/${shippingMethodId}`,
            );
        }

        return super.cleanUp();
    }
}
```

**Patching the default is not the same as removing the assignment.** Both are needed.

The same shape applies to anything else a test points at a channel: payment methods,
themes, languages, currencies. Record the original, restore it, remove the association.

### 3. global-teardown.ts — the net, and the alarm

Runs once after the whole suite. It removes the sales channel the suite creates for itself
(which the suite never cleans up), and anything named `Test-*` that survived the first two
levels.

```typescript
import { chromium, type FullConfig } from '@playwright/test';

async function globalTeardown(config: FullConfig): Promise<void> {
    const baseURL = process.env['APP_URL'] ?? 'https://your-shop.ddev.site';
    const accessKey = process.env['SHOPWARE_ACCESS_KEY_ID'];
    const secretKey = process.env['SHOPWARE_SECRET_ACCESS_KEY'];

    if (accessKey === undefined || secretKey === undefined) {
        return;
    }

    const browser = await chromium.launch();
    const context = await browser.newContext({ ignoreHTTPSErrors: true });

    try {
        const auth = await context.request.post(`${baseURL}api/oauth/token`, {
            data: {
                grant_type: 'client_credentials',
                client_id: accessKey,
                client_secret: secretKey,
            },
        });

        const { access_token: token } = (await auth.json()) as { access_token: string };
        const headers = { Authorization: `Bearer ${token}` };

        // The customer has to go first: it holds a foreign key on the channel, and the
        // channel delete is refused while it exists.
        const channels = await context.request.post(`${baseURL}api/search/sales-channel`, {
            headers,
            data: { filter: [{ type: 'contains', field: 'name', value: 'acceptance test' }], limit: 50 },
        });

        const { data: channelRows } = (await channels.json()) as { data?: Array<{ id: string }> };

        for (const channel of channelRows ?? []) {
            const customers = await context.request.post(`${baseURL}api/search/customer`, {
                headers,
                data: { filter: [{ type: 'equals', field: 'salesChannelId', value: channel.id }], limit: 500 },
            });

            const { data: customerRows } = (await customers.json()) as { data?: Array<{ id: string }> };

            for (const customer of customerRows ?? []) {
                await context.request.delete(`${baseURL}api/customer/${customer.id}`, { headers });
            }

            await context.request.delete(`${baseURL}api/sales-channel/${channel.id}`, { headers });
        }

        const entities: Array<[string, string]> = [
            ['shipping-method', 'Test-'],
            ['product', 'Test-'],
            ['category', 'Test-'],
            ['product-manufacturer', 'Test-'],
            ['rule', 'Test-'],
            ['promotion', 'Test-'],
        ];

        for (const [entity, prefix] of entities) {
            const search = await context.request.post(`${baseURL}api/search/${entity}`, {
                headers,
                data: { filter: [{ type: 'prefix', field: 'name', value: prefix }], limit: 500 },
            });

            const { data } = (await search.json()) as { data?: Array<{ id: string }> };

            if (data === undefined || data.length === 0) {
                continue;
            }

            process.stdout.write(
                `\nClean-up gap: ${data.length} ${entity} record(s) survived the suite's own teardown; removing them.\n`,
            );

            for (const row of data) {
                await context.request.delete(`${baseURL}api/${entity}/${row.id}`, { headers });
            }
        }
    } finally {
        await context.close();
        await browser.close();
    }
}

export default globalTeardown;
```

Registered in `playwright.config.ts`:

```typescript
export default defineConfig({
    testDir: './tests',
    globalTeardown: './global-teardown.ts',
    …
});
```

**A line in its output is a defect, not a cleanup.** It means level 1 or 2 has a gap, and
the gap gets fixed there. This level is the alarm, not the solution.

## How to prove it

Not by reading the code. By counting:

```bash
count() { ddev mysql -uroot -proot db -e "
SELECT (SELECT COUNT(*) FROM shipping_method_translation WHERE name LIKE 'Test-%') AS shipping,
       (SELECT COUNT(*) FROM product_translation WHERE name LIKE 'Test-%')         AS products,
       (SELECT COUNT(*) FROM sales_channel_translation WHERE name LIKE '%acceptance%') AS channels,
       (SELECT COUNT(*) FROM customer)                                             AS customers;" -N; }

count
ddev playwright test
count
ddev playwright test
count
```

**All three lines must be identical.** Two runs, because a clean-up that works once may
still leave the second run's data behind.

## The one exception, decided deliberately

**Cart rows.** Each test leaves one behind, and this is accepted.

A cart belongs to a session rather than to an entity, so no entity clean-up can see it.
The storefront offers no action to empty one — there is a store-api route, but reaching it
from a browser test means reconstructing the session server-side. They appear in no
administration list, every real shop visit creates them identically, and Shopware's own
`cart.cleanup` scheduled task (daily, `run_interval` 86400) removes abandoned ones.

Six rows a day, self-healing, invisible. Written down here so nobody rediscovers it as a
problem and spends an afternoon on it.

## What is not yours to delete

The shop's own data. When clearing up after a suite that misbehaved, check before deleting:

```sql
SELECT COUNT(*) FROM `order` WHERE …;    -- orders are never test litter
SELECT MIN(created_at), MAX(created_at) FROM `order`;
```

Orders predating the test work are the shop's, not the suite's. Delete by name prefix and
by explicit id, never by "everything created today".
