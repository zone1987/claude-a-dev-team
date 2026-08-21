# Shopware 6 — E2E (Playwright)

Shopware uses **Playwright** for E2E/acceptance tests (ADR "acceptance test suite", replacing Cypress) — against a
running shop instance, the smallest tier of the test pyramid (few, critical flows).

```ts
import { test, expect } from '@playwright/test';

test('add to cart', async ({ page }) => {
    await page.goto('/');
    await page.getByRole('button', { name: 'In den Warenkorb' }).first().click();
    await expect(page.locator('.offcanvas-cart')).toBeVisible();
});
```

Use page objects/fixtures for recurring flows; prepare test data through the API or fixtures. Apply sparingly
(slow/expensive) — cover logic in unit/integration tests. Both storefront and admin flows are possible.
