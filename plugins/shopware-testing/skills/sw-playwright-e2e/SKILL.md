---
name: sw-playwright-e2e
description: >
  End-to-End-Tests für Shopware 6 mit Playwright (Acceptance Test Suite): Setup, Page-Objects/Fixtures, Storefront-
  & Admin-Flows, gegen laufende Instanz. Trigger: "Playwright shopware", "E2E Test shopware", "acceptance test suite",
  "End-to-End shopware", "browser test shopware". Shopware 6.7.
---

# Shopware 6 — E2E (Playwright)

Shopware nutzt **Playwright** für E2E/Acceptance-Tests (ADR „acceptance test suite", löst Cypress ab) — gegen eine
laufende Shop-Instanz, kleinste Stufe der Test-Pyramide (wenige, kritische Flows).

```ts
import { test, expect } from '@playwright/test';

test('add to cart', async ({ page }) => {
    await page.goto('/');
    await page.getByRole('button', { name: 'In den Warenkorb' }).first().click();
    await expect(page.locator('.offcanvas-cart')).toBeVisible();
});
```

Page-Objects/Fixtures für wiederkehrende Flows; Testdaten über API/Fixtures vorbereiten. Sparsam einsetzen
(langsam/teuer) — Logik in Unit/Integration abdecken. Storefront- und Admin-Flows möglich.
