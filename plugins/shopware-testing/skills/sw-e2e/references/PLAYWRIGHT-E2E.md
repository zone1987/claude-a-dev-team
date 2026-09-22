# Shopware 6 — Playwright end-to-end

**The full setup — the location `tests/E2E/`, the `avhulst/ddev-browserless` add-on, the
complete `playwright.config.ts`, the three `.env` files, the pinned versions and the
clean-up rule — lives in the `sw-testing-standard` skill, `STANDARD-PLAYWRIGHT.md` and
`STANDARD-CLEANUP.md`.** This file covers writing a spec once that exists.

## Not "sparingly"

Older guidance called end-to-end tests expensive and advised a handful of critical flows.
**That does not apply here.** Whatever the plugin ships gets covered: every administration
page it adds, every storefront output it produces, every configuration switch that changes
what a user sees. It is the only level that reaches Twig at all, and the only one that
answers "does the shopper see the right thing".

Unit and integration tests still carry the logic — that is why they are 100 %. Playwright
carries the rendering, which nothing else can.

## Built on the Acceptance Test Suite, not on plain Playwright

`@shopware-ag/acceptance-test-suite` supplies the shop customer, the API clients, the page
objects and `TestDataService`. Do not reimplement them, and do not create entities outside
`TestDataService` — anything it does not know about is never cleaned up.

```typescript
import { expect, test } from '@fixtures/AcceptanceTest';

test.describe('the free shipping progress in the off-canvas cart', { tag: ['@YourPlugin'] }, () => {
    test.beforeEach(async ({ TestDataService }) => {
        // A sales channel the suite has just created has no compiled theme, and therefore
        // no storefront JavaScript at all.
        await TestDataService.compileThemeForSalesChannel();
        // The suite's channel is not necessarily on the shop's default currency.
        await TestDataService.useDefaultCurrency();
    });

    test('tells the shopper what is still missing', async ({
        ShopCustomer,
        TestDataService,
        StorefrontProductDetail,
        FreeShippingProgressDisplay,
    }) => {
        const shippingMethod =
            await TestDataService.createShippingMethodWithFreeShippingThreshold(100);
        await TestDataService.useShippingMethodInStorefront(shippingMethod.id);
        await FreeShippingProgressDisplay.useShippingMethod(shippingMethod.id);

        const product = await TestDataService.createProductAtGrossPrice(40);
        await FreeShippingProgressDisplay.putInCart(StorefrontProductDetail.url(product));

        await ShopCustomer.goesTo(FreeShippingProgressDisplay.url());

        await expect(FreeShippingProgressDisplay.container).toBeVisible();
    });
});
```

## What the example above encodes

**Test names are sentences that state the rule.** `'tells the shopper what is still
missing'`, not `'works'`.

**Selectors live in a page object, never inline.** They are the contract a theme relies on;
a change to one has to be visible as a change to the contract.

**The cart is filled through the buy button.** A hand-built post to
`checkout/line-item/add` from `page.evaluate` returns 404 or silently adds nothing.

**The off-canvas is reached through `checkout/offcanvas`**, the route the storefront's own
JavaScript calls. Driving it directly keeps the test about the output rather than about a
dialog animation.

**Amounts are read back, never assumed.** The shop decides what a cart is worth: a product
created at 40 arrives as 35.66 because the suite treats the number as net.

## Administration flows

Same rules. Page objects under `page-objects/administration/`, and every page the plugin
adds gets one:

```typescript
test('lists the offers once a supplier carries the product', async ({
    AdminPage,
    TestDataService,
    ProductDetail,
}) => {
    const productId = await TestDataService.getAnyProductId();
    await TestDataService.createSupplierWithOffer(productId, { name: 'Card probe one' });

    await AdminPage.goto(ProductDetail.url(productId));

    await expect(ProductDetail.offerGrid).toBeVisible();
    await expect(ProductDetail.offerGrid).toContainText('Card probe one');
});
```

## Running

The specs run inside the DDEV web container, but the browser does not live there: it runs
in a container of its own, provided by the
[`avhulst/ddev-browserless`](https://github.com/avhulst/ddev-browserless) add-on and
reached over `ws://browserless:3000/chromium/playwright`. Start it on the host first:

```bash
ddev browserless on
ddev exec -d /var/www/html/shopware/custom/static-plugins/<PLUGIN-NAME>/tests/E2E \
    npx playwright test
```

`-d` sets the working directory **inside the container** — the one holding
`playwright.config.ts`. The report afterwards:

```bash
npx playwright show-report tests/E2E/playwright-report
```

Never `docker exec`; a restart is `ddev restart`.

**If a long test dies with `Target page, context or browser has been closed`**, it is not
the test: `BROWSERLESS_TIMEOUT` in `.ddev/.env.browserless` is too small. The value and
the reasoning are in the `sw-testing-standard` skill, `STANDARD-PLAYWRIGHT.md`.

## Not part of `composer gate`

They need a running shop with the plugin installed, its storefront built, and the
browserless container started. Run them before a release and after any change to a
template or an administration page.

## The suite is not finished until it leaves no trace

→ **`STANDARD-CLEANUP.md`**. Counted, not assumed: entity counts before and after two
consecutive runs must be identical.
